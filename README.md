# HT++

HT++ is a statically-typed programming language that transpiles to C++. It features an AutoHotkey (AHK)-like syntax with static types, combining ease of use with the performance and power of C++. This allows for the development of efficient and versatile scripts that can run on any device where C++ is supported, ensuring compatibility across every platform.

#### Install localy

1. Clone this repository
2. The tarnspiler is HT++.py
3. You can make a .htpp file then use the HT++.py to transpile it to C++ for example:
```
python HT++.py file_name.htpp
```
you should get a .cpp file whit the same name as the .htpp
When you transpile the .htpp script it will replace the .cpp whit the same name if it exists.

I recommend using SciTE4HTH where i added HT++ support.

Why use SciTE4HTH for HT++?
- It provides syntax highlighting and code completion for the HT++ language, making it easier to write and read HT++ scripts.

How to use SciTE4HTH for HT++:
1. Download and install the SciTE4HTH editor from https://github.com/TheMaster1127/SciTE4HTH
2. Go to the htpp.properties and put the full path of your HT++.py then restart the SciTE editor by re-opening it.
3. Open SciTE and create a new file with the .htpp extension (or open an existing .htpp file).
4. Write your HT++ code in the editor. You'll get syntax highlighting and code completion as you type.
5. To transpile your HT++ code to C++, simply press F5 or Crtl+F7 or click the "Run" button. This will transpile the HT++ code.

That's it! SciTE4HTH gives you a user-friendly environment to write HT++ scripts, with helpful features like syntax highlighting and code completion, while allowing you to easily transpile to HT++ code with just a few clicks or keystrokes.

#### Usage Example

HT++ currently supports a subset of commands similar to AutoHotkey:

- Functions
- If, else, else if
- Random
- Sleep 
- Msgbox
- FileRead 
- FileAppend 
- SetTimer 
- Labels
- Gosub
- Return/return
- Loop
- Loop, Parse
- Variables
- Arrays
- RunCMD and ExitApp
- Comments
- Sort
- getDataFromAPI and getDataFromJSON 
- Math Functions
- Build-in Functions
- Build-in Variables

here is the full documentation: [Documentation](https://github.com/TheMaster1127/HT-plus-plus/wiki)
