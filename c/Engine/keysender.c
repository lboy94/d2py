/*
+	Title: Automate class
+	Author: LordVader
+	Updated: 11/05/2007
*/
#include "keysender.h"
#include <windows.h>
#include <winable.h>
#include <Stdio.h>

#pragma comment(lib, "User32")

//#pragma warning (disable:4996) // typesafe string manipulation warnings
//#pragma warning (disable:4018) // signed/unsigned mismatch warnings

#define DELAY 50
HWND getWindowByTitle(const char* szTitle)
{
	HWND hReturn;

	hReturn = FindWindowA( 0, szTitle );
	return hReturn;
}

// Prevents keyboard+mouse from reaching window, but our thread can still use
// SendInput to pass events.
//void blockInput(HWND hWnd, int bState) {SendMessageA(hWnd,BlockInput(bState),0,0);}
/*
// Dunno wtf this is.
int checkIconic(HWND hWnd)
{
	int bReturn = FALSE;
	RECT rc;
	//if(IsIconic(hWnd) != 0)
	//{
		GetWindowRect( hWnd, &rc );
		SetWindowPos( hWnd, HWND_TOPMOST, rc.left, rc.top, 0, 0, SWP_NOSIZE | SWP_NOZORDER );
		bReturn = TRUE;
	//}
	return bReturn;
}

// Toggle whether window's shown/hidden.
void toggleShowHide(HWND hWnd, int bValue) {ShowWindow( hWnd, (bValue)?SW_SHOW:SW_HIDE );}


void sendClick(HWND hWnd, int nSide, int X, int Y)
{
	LPARAM Pos = MAKELPARAM(X, Y);
	SendMessage( hWnd, WM_MOUSEMOVE, 0, Pos );
	Sleep(DELAY);
	switch(nSide) {
		case LEFT_CLICK: {
			SendMessage( hWnd, WM_LBUTTONDOWN, MK_LBUTTON, Pos );
			SendMessage( hWnd, WM_LBUTTONUP, MK_LBUTTON, Pos );
			Sleep(DELAY);
		}
		break;
		case MIDDLE_CLICK: {
			SendMessage( hWnd, WM_MBUTTONDOWN, MK_MBUTTON, Pos );
			SendMessage( hWnd, WM_MBUTTONUP, MK_MBUTTON, Pos );
			Sleep(DELAY);
		}
		break;
		case RIGHT_CLICK: {
			SendMessage( hWnd, WM_RBUTTONDOWN, MK_RBUTTON, Pos );
			SendMessage( hWnd, WM_RBUTTONUP, MK_RBUTTON, Pos );
			Sleep(DELAY);
		}
		break;
		case DOUBLE_LCLICK: {
			SendMessage( hWnd, WM_LBUTTONDOWN, MK_LBUTTON, Pos );
			SendMessage( hWnd, WM_LBUTTONUP, MK_LBUTTON, Pos );
			Sleep(DELAY);
			SendMessage( hWnd, WM_LBUTTONDOWN, MK_LBUTTON, Pos );
			SendMessage( hWnd, WM_LBUTTONUP, MK_LBUTTON, Pos );
			Sleep(DELAY);
		}
		break;
		case DOUBLE_MCLICK: {
			SendMessage( hWnd, WM_MBUTTONDOWN, MK_MBUTTON, Pos );
			SendMessage( hWnd, WM_MBUTTONUP, MK_MBUTTON, Pos );
			Sleep(DELAY);
			SendMessage( hWnd, WM_MBUTTONDOWN, MK_MBUTTON, Pos );
			SendMessage( hWnd, WM_MBUTTONUP, MK_MBUTTON, Pos );
			Sleep(DELAY);
		}
		break;
		case DOUBLE_RCLICK: {
			SendMessage( hWnd, WM_RBUTTONDOWN, MK_RBUTTON, Pos );
			SendMessage( hWnd, WM_RBUTTONUP, MK_RBUTTON, Pos );
			Sleep(DELAY);
			SendMessage( hWnd, WM_RBUTTONDOWN, MK_RBUTTON, Pos );
			SendMessage( hWnd, WM_RBUTTONUP, MK_RBUTTON, Pos );
			Sleep(DELAY);
		}
		break;
	}
}

void sendKeyString( HWND hWnd, const char szKey[] )
{
    for(int i = 0 ; i < strlen( szKey ) ; i++)  {
	if( islower( szKey[i] ) ) {
		PostMessage( hWnd,WM_CHAR,(WPARAM)szKey[i], 0 );
		//Sleep(DELAY);
	} else {
		PostMessage( hWnd, WM_KEYDOWN, VK_SHIFT, 0 );
		//Sleep(DELAY);
		PostMessage( hWnd, WM_CHAR, (WPARAM)szKey[i], 0 ); 
		//Sleep(DELAY);
		PostMessage( hWnd, WM_KEYUP, VK_SHIFT, 0 );
		//Sleep(DELAY);
	}
    }
}
*/

HWND wnd=NULL;

BOOL CALLBACK EnumWindowsProc(HWND hwnd, LPARAM lParam) {
	DWORD pid, mypid;
	char txt[255];
	char txt2[255];

	mypid = GetProcessId(GetCurrentProcess());

	GetWindowThreadProcessId(hwnd, &pid);
	if (mypid==pid) {
		GetWindowText(hwnd, txt, 255);
		GetClassName(hwnd, txt2, 255);
		printf("mypid: %d, pid: %d, hwnd: %x\n\ttxt: %s\n\tclass: %s\n", mypid, pid, hwnd, txt, txt2);
		if (strstr(txt2, "Diablo II")!=NULL) {
			wnd = hwnd;
			printf("#############\nFound window! %x\n", wnd);
		}
	}
	return TRUE;
}

void getWindow() 
{
	//HWND wnd = getWindowByTitle("Diablo II");
	wnd = NULL;
	printf("EnumWindows returned: %d\n",  EnumWindows(EnumWindowsProc, 0));
	printf("wnd==%x\n", wnd);
}
void sendKey( HWND hWnd, UINT vKey )
{
	// PostMessage returns instantly, SendMessage waits for response?
	SendMessage( hWnd, WM_KEYDOWN, toupper(vKey), 0 );
	SendMessage( hWnd, WM_CHAR, vKey, ( 0x00000000 | (VK_ACCEPT<<16) ));
	SendMessage( hWnd, WM_KEYUP, toupper(vKey), 0 );
}

void typeText(char* str) 
{	
	if (!wnd) getWindow();

	for (int i=0;i<strlen(str);i++) {
		sendKey(wnd, str[i]);
	}
}