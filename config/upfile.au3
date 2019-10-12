ControlFocus("打开","","Edit1")

WinWait("[CLASS:#32770]","",10)

ControlSetText("打开","","Edit1","C:\Users\Administrator\123.jpg")
Sleep(2000)

ControlClick("打开","","Button1");
Sleep(2000)