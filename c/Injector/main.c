/*
 *	Simple loader that injects a DLL with the same name (and directory) 
 * into the first instance of Game.exe that it finds.
 *
 * Credit: Darawk's tutorial, mostly.
 */
#include <windows.h>
#include <stdio.h>
#include <tlhelp32.h> 

#pragma comment(lib, "Advapi32")

int setDebugPrivilege() 
{
	HANDLE hToken;
	LUID seDebugNameValue;
	TOKEN_PRIVILEGES tp;

	if (!OpenProcessToken(GetCurrentProcess(),TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, &hToken )) {
		printf("OpenProcessToken failed with error code %d.\n", GetLastError());
		return 1;
	}

	if (!LookupPrivilegeValue(NULL, SE_DEBUG_NAME, &seDebugNameValue )) {
		printf("LookupPrivilegeValue failed with error code %d.\n", GetLastError());
		CloseHandle(hToken); return 1;
	}

	tp.PrivilegeCount=1;
	tp.Privileges[0].Luid = seDebugNameValue;
	tp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;

	if (AdjustTokenPrivileges(hToken, FALSE, &tp, sizeof(tp), NULL, NULL )) {
		CloseHandle(hToken);
		return 0;
	} else {
		printf("AdjustTokenPrivileges failed with error code %d.\n", GetLastError());
		CloseHandle(hToken); return 1;
	}
} 

int injectToPid(int pid, char* path) 
{
	HANDLE hProcess;
	PVOID mem;
	HANDLE hThread;
	HANDLE hLibrary;
	DWORD error;
	

	hProcess = OpenProcess(PROCESS_CREATE_THREAD | PROCESS_QUERY_INFORMATION | 
				PROCESS_VM_OPERATION | PROCESS_VM_WRITE | PROCESS_VM_READ, FALSE, pid);
		
	if (hProcess == INVALID_HANDLE_VALUE)
	{
		fprintf(stderr, "Cannot open pid: %d\n", pid);
		return 1;
	}
	
	mem = VirtualAllocEx(hProcess, NULL, strlen(path) + 1, MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE);

	if (mem == NULL)
	{
		fprintf(stderr, "Can't allocate memory in process. %d\n", GetLastError());
		CloseHandle(hProcess);
		return 1;
	}

	if (WriteProcessMemory(hProcess, mem, (void*)path, strlen(path) + 1, NULL) == 0)
	{
		fprintf(stderr, "Can't write to memory in process.\n");
		VirtualFreeEx(hProcess, mem, strlen(path) + 1, MEM_RELEASE);
		CloseHandle(hProcess);
		return 1;
	}

	hThread = CreateRemoteThread(hProcess, NULL, 0, 
		(LPTHREAD_START_ROUTINE)GetProcAddress(GetModuleHandle("KERNEL32.DLL"),"LoadLibraryA"), mem, 0, NULL);
	if (hThread == INVALID_HANDLE_VALUE)
	{
		fprintf(stderr, "Can't create a thread in process.\n");
		VirtualFreeEx(hProcess, mem, strlen(path) + 1, MEM_RELEASE);
		CloseHandle(hProcess);
		return 1;
	}

	if (WaitForSingleObject(hThread, INFINITE)==WAIT_FAILED) {
		printf("WaitForSingleObject failed while waiting for RemoteThread to finish.\n");
		CloseHandle(hProcess);
		return 1;
	}

	hLibrary = NULL;
	if (!GetExitCodeThread(hThread, (LPDWORD)&hLibrary))
	{
		printf("Can't get exit code for thread, GetLastError() = %i.\n", GetLastError());
		CloseHandle(hThread);
		VirtualFreeEx(hProcess, mem, strlen(path) + 1, MEM_RELEASE);
		CloseHandle(hProcess);
		return 1;
	}

	CloseHandle(hThread);
	VirtualFreeEx(hProcess, mem, strlen(path) + 1, MEM_RELEASE);

	if (hLibrary == NULL)
	{
		hThread = CreateRemoteThread(hProcess, NULL, 0, (LPTHREAD_START_ROUTINE) GetProcAddress(GetModuleHandle("KERNEL32.DLL"),"GetLastError"), 0, 0, NULL);
		if (hThread == INVALID_HANDLE_VALUE)
		{
			fprintf(stderr, "LoadLibraryA returned NULL and can't get last error.\n");
			CloseHandle(hProcess);
			return 1;
		}

		WaitForSingleObject(hThread, INFINITE);
		GetExitCodeThread(hThread, &error);

		CloseHandle(hThread);

		printf("LoadLibrary return NULL, GetLastError() is %i\n", error);
		CloseHandle(hProcess);
		return 1;
	}

	CloseHandle(hProcess);

	printf("Injected %08x\n", (DWORD)hLibrary);
	
	return 0;
}


DWORD getIdFromName(char *procName)
{
   PROCESSENTRY32 pe;
   HANDLE thSnapshot;
   BOOL retval, ProcFound=FALSE;

   thSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);

   if(thSnapshot == INVALID_HANDLE_VALUE)
   {
      printf("Error: unable to create toolhelp snapshot");
      exit(1);
   }

   pe.dwSize = sizeof(PROCESSENTRY32);

    retval = Process32First(thSnapshot, &pe);

   while(retval)
   {
      if(strstr(pe.szExeFile, procName) )
      {
         ProcFound = TRUE;
         break;
      }

      retval    = Process32Next(thSnapshot,&pe);
      pe.dwSize = sizeof(PROCESSENTRY32);
   }

   // add in error checking lol
   if (!ProcFound) {
	   printf("Process '%s' not found!\n", procName);
	   exit(1);
   }
   return pe.th32ProcessID;
} 

int isWinNT() {return (GetVersion() < 0x80000000);}


int main(int argc, char* argv[])
{
	int pid,i; char path[MAX_PATH];

	// check OS compatibility
	if (!isWinNT()) {
		printf("Injector uses the CreateRemoteThread method, which \
			does not work outside Windows NT-based systems.");
		return 1;
	}

	if (!GetFullPathName(argv[0], MAX_PATH, path, NULL)) {
		printf("Couldn't get full path of executable. Error code %d.\n", GetLastError());
		return 1;
	}

	i = strlen(path);
	path[--i]='l'; path[--i]='l'; path[--i]='d';

	printf("Injecting: %s\n", path);
	setDebugPrivilege();

	pid = getIdFromName("Game.exe");
	injectToPid(pid, path);

	return 0;
}

