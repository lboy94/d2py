#include <windows.h>
#include <stdio.h>
#include "npc.h"

BOOL __fastcall PacketReceived_Handler(BYTE* pPacket, DWORD dwSize)
{
	printf("Received: %d bytes, id: %2x\n", dwSize, pPacket[0]);
	npcPackets(pPacket, dwSize);
	return TRUE;
}