#ifndef _PACKETSENDER_H_
#define _PACKETSENDER_H_

void sendGame(unsigned char* data, int len);
void recvGame(unsigned char* data, int len);

void overheadChat(const char* text);

void gameChat(const char* name, int whisper, const char* text);

#endif