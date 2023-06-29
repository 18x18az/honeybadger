python -m nuitka --include-data-dir=resources=resources --standalone main.py
"%programfiles(x86)%\Inno Setup 6\iscc.exe" "scripts\innoscript.iss" "/version=%1"