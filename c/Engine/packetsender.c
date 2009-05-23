#include "functions.h"
#include <string.h>

void sendGame(unsigned char* data, int len) {
	SendPacket(len, 0, data);
}

void recvGame(unsigned char* data, int len) {
	ReceivePacket(data, len);
}

void overheadChat(const char* text)
{
	int n = (int)strlen(text);
	int length = n + 6;

	unsigned char* buffer = (unsigned char*)malloc(length);

	buffer[0] = 0x14;
	*(short*)(buffer + 1) = 0x00;
	memcpy(buffer + 3, text, strlen(text));
	buffer[strlen(text) + 3] = 0x00;
	buffer[strlen(text) + 4] = 0x00;
	buffer[strlen(text) + 5] = 0x00;

	sendGame(buffer, length);
	free(buffer);
}


void gameChat(const char* name, int whisper, const char* text)
{
	int length = (int)strlen(text) + (int)strlen(name) + 12;
	unsigned char* buffer = (unsigned char*)malloc(length); 

	int offset = 0;
	buffer[offset++] = 0x26;
	buffer[offset++] = whisper ? 0x02 : 0x01;
	buffer[offset++] = 0x00;
	buffer[offset++] = 0x02;
	buffer[offset++] = 0x00;
	buffer[offset++] = 0x00;
	buffer[offset++] = 0x00;
	buffer[offset++] = 0x00;
	buffer[offset++] = 0x00;
	buffer[offset++] = whisper ? 0x01 : 0x05;

	for (int i = 0; name[i] != '\0'; i++)   {buffer[offset++] = name[i];}
	buffer[offset++] = 0x00;

	for (int i = 0; text[i] != '\0'; i++)  {buffer[offset++] = text[i];}
	buffer[offset++] = 0x00;

	sendGame(buffer, length);
	free(buffer);
}