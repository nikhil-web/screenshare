Dim oShell
Set oShell = WScript.CreateObject ("WScript.Shell")
oShell.run "cmd /K main.py"
Set oShell = Nothing