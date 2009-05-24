#ifndef _NPC_H_
#define _NPC_H_
#include <Python.h>

void npcTrackerInit();

void npcPackets(unsigned char* data, int len);

PyMODINIT_FUNC PyInit_npc(void);


#endif