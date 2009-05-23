#ifndef _KEYSENDER_H_
#define _KEYSENDER_H_

enum MOUSE_ACTION {
	LEFT_CLICK,
	MIDDLE_CLICK,
	RIGHT_CLICK,
	DOUBLE_LCLICK,
	DOUBLE_MCLICK,
	DOUBLE_RCLICK,
};

//HWND getWindowByTitle(const char* szTitle);

// Prevents keyboard+mouse from reaching window, but our thread can still use
// SendInput to pass events.
//void blockInput(HWND hWnd, int bState);

// Dunno wtf this is.
//int checkIconic(HWND hWnd);

// Toggle whether window's shown/hidden.
//void toggleShowHide(HWND hWnd, int bValue);

//void sendClick(HWND hWnd, int nSide, int X, int Y);

//void sendKeyString( HWND hWnd, const char szKey[] );

//void sendKey( HWND hWnd, UINT vKey );


// ONLY THING I NEED TO EXPORT ATM
//
//  Types a sequence of characters to D2. Special characters might be
// anything from 0x09 (tab) to 0x1b (esc) to \r (enter) or whatever.
//
// Python string syntax for esc: '\x1b'
void typeText(char* str);

#endif