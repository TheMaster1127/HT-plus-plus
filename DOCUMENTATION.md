# HT++: HeavenToC++ Programming Language Documentation <a id="htpp"></a>

## Table of Contents

1. [Usage and Syntax](#usage-and-syntax)
2. [Features](#features)
3. [Editors for Code](#editors-for-code)
4. [Script Showcase](#script-showcase)

---

## Usage and Syntax <a id="usage-and-syntax"></a>

[Go back](#htpp)

This section provides an overview of the usage and syntax of the HT++ programming language.

### Coding Style: Allman Style

In HeavenToC++ (HT++) programming, it is crucial to adhere to the Allman coding style to ensure code readability and avoid errors. The Allman style dictates placing curly braces on their own lines, and failure to follow this style may result in errors during execution.

#### Example of Allman Style:

```ahk
func int nameOfFunc(int a, int b)
{
    return a + b
}
```

### Note:

- **MUST**: Use the Allman style consistently throughout your HT++ code.
- **WILL**: Failure to use the Allman style may lead to errors during execution.

Adhering to the Allman coding style not only helps maintain clean and organized code but also ensures compatibility and error-free execution in HT++ programming.

### Syntax Overview

In HeavenToC++ (HT++), the coding style follows the Allman style, where curly braces are placed on their own lines. Additionally, comments are denoted by a semicolon `;` for single-line comments and by using semicolon `;` for each line in multi-line comments. There are no block comments.

#### Variables and Data Types

In HT++, variables are declared and assigned using the Allman style, and variable names follow the same conventions as in AutoHotkey. Here's how you declare and assign variables:

```ahk
int myNumber := 42
str myString := "Hello, World!"
bool isFlagSet := true

int8 var1  := 64
int16 var2 := 32000
int32 var3 := 2147483647
int64 var4 := 1152921504606846976
```

- **`int`**:
  - The size of `int` is implementation-defined but must be at least 16 bits.
  - On most modern systems and platforms (like x86 and x86_64), `int` is commonly 32 bits.
  - `int` can vary between 16, 32, or even 64 bits depending on the platform.

HT++ supports various data types, including numeric, string, and boolean types.

#### Control Structures

Control structures in HT++, including conditional statements and loops, follow the Allman style as well.

##### If-Else Statements

```ahk
if (condition)
{
    ; Code block executed if condition is true
}
else
{
    ; Code block executed if condition is false
}
```

##### Loops

```ahk
Loop
{
    ; Code block to be repeated
}
```

#### Functions

Functions in HT++ are declared using the Allman style, and return statements are in lowercase. Here's how you declare and define functions:

```ahk
; HT++ Functions Documentation

; Functions return different types of values.
; Choosing the correct return type ensures proper function behavior.
; Below are examples for each return type:

; int function
; Use for operations with whole numbers.
; Returns a whole number as the result.
func int add(int a, int b)
{
    return a + b
}

; str function
; Use for text or string manipulation.
; Returns the resulting string.
func str concatenate(str a, str b)
{
    return a . b
}

; void function
; Use for actions that don't require a return value.
; Performs an action like displaying a message.
func void printMessage(str message)
{
    MsgBox, % message
}

; bool function
; Use to return true or false based on a condition.
; Evaluates a condition and returns a boolean value.
func bool isEven(int number)
{
    if (Mod(number, 2) == 0)
    {
        return true
    }
    else
    {
        return false
    }
}

; float function
; Use for operations with decimal numbers.
; Returns a decimal number as the result.
func float divide(float a, float b)
{
    return a / b
}

; Example Usage
; Simply label the main function since before we used other functions
main:

; int function example
int resultInt := add(3, 4)
MsgBox, % "Result of add(3, 4): " . STR(resultInt)

; str function example
str resultStr := concatenate("Hello, ", "World!")
MsgBox, % "Result of concatenate('Hello, ', 'World!'): " . resultStr

; void function example
printMessage("This is a message")

; bool function example
bool resultBool := isEven(10)
MsgBox, % "Is 10 even? " . STR(resultBool)

; float function example
float resultFloat := divide(7.5, 2.5)
MsgBox, % "Result of divide(7.5, 2.5): " . STR(resultFloat)
```

Functions with arrays as the param:

```ahk
func void testIntArray(arr int intArray, str secondParam)
{
MsgBox, % intArray
MsgBox, % "the secondParam is: " . secondParam
}

func void testStrArray(arr str strArray, str secondParam)
{
MsgBox, % strArray
MsgBox, % "the secondParam is: " . secondParam
}

func void testFloatArray(arr float floatArray, str secondParam)
{
MsgBox, % floatArray
MsgBox, % "the secondParam is: " . secondParam
}

; Simply label the main function since before we used other functions
main:

arr int intArray
arr str strArray
arr float floatArray

arr intArray .= 5
arr strArray .= "hello"
arr floatArray .= 3.14

str secondParam := "this is the secondParam"

testIntArray(intArray, secondParam)
testStrArray(strArray, secondParam)
testFloatArray(floatArray, secondParam)
```

Functions in HT++ must be declared at the top of the script following the rules of C++.

#### Comments

Comments in HT++ are denoted by a semicolon `;` for single-line comments and are placed on their own lines for multi-line comments.

```ahk
; This is a single-line comment

/*
This is a multiline comment.
It can span multiple lines.
Everything between the opening and closing is a comment.
*/
```

### Usage Overview

HT++ is designed for simplicity and ease of use, following the Allman coding style throughout the language. It is suitable for various applications, including web development, scripting, and learning programming concepts.

### Example Usage

Here's an example demonstrating the usage of variables, control structures, and functions in HT++:

```ahk
func int nameOfFunc(int num1, int num2)
{
return num1 + num2
}

; simply label the main function since before we used other functions
main:

int myNumber := 42
str myString := "Hello, World!"

if (myNumber > 0)
{
    MsgBox, % "Number is positive: " . STR(myNumber)
}
else
{
    MsgBox, % "Number is non-positive: " . STR(myNumber)
}

int nameOfFuncOut := nameOfFunc(3, 4)
MsgBox, % "Result of nameOfFunc: " . STR(nameOfFuncOut)
```

WARNING: NEVER NAME A VARIABLE THE SAME NAME AS A FUNCTION NAME

### Conclusion

HT++ follows the Allman coding style for consistency and readability. Its simplicity and versatility make it suitable for various programming tasks.

---

## Features <a id="features"></a>

[Go back](#htpp)

Explore the various features offered by the HT++ programming language in this section.

### Table of Contents

1. [Functions](#htpp-functions)
2. [If, else, else if](#if-else-else-if)
3. [Random](#random)
4. [Sleep](#sleep)
5. [Msgbox](#msgbox)
6. [FileRead](#fileread)
7. [FileAppend](#fileappend)
8. [SetTimer](#settimer)
9. [Labels](#labels)
10. [Gosub](#gosub)
11. [Return/return](#return)
12. [Loop](#loop)
13. [Loop, Parse](#loop-parse)
14. [Variables](#variables)
15. [Arrays](#arrays)
16. [RunCMD and ExitApp](#runcmd-and-exitapp)
17. [Comments](#htpp-comments)
18. [Sort](#sort)
19. [getDataFromAPI and getDataFromJSON](#getdatafromapi-and-getdatafromjson)
20. [Math Functions](#math-functions)
21. [Build-in Functions](#build-in-functions)
22. [Build-in Variables](#build-in-variables)

---

### Functions <a id="htpp-functions"></a>

[Go back](#features)

In HeavenToC++ (HT++), functions are indispensable for organizing and structuring code efficiently. By encapsulating reusable blocks of code, functions enhance modularity, readability, and maintainability. Adhering to the Allman Style coding convention is crucial for defining functions in HT++, ensuring clarity and consistency in code formatting.

#### Syntax:

```ahk
func type nameOfFunc(type param1, type param2, ...)
{
    ; Function body
    return result
}
```

#### Warning:

Ensure that the opening curly brace `{` is placed on a new line when defining functions in HeavenToC++ (HT++). Failure to adhere to this convention will result in errors, and the function will not be recognized.

Functions in HT++ must be declared at the top of the script following the rules of C++.

#### Parameters:

- `nameOfFunc`: The name of the function, following the Allman Style convention.
- `param1`, `param2`, ...: Parameters that the function accepts for processing.

#### Example:

```ahk
func int sum(int a, int b)
{
    return a + b
}
```

In this example, the `sum` function takes two parameters `a` and `b`, adds them together, and returns the result.

#### Note:

- Consistent indentation and spacing within the function body enhance code readability.
- All functions in HT++ are similar to C++'s scope.
- You can't declare function inside a function

#### Usage:

Functions serve various purposes, such as mathematical calculations, data processing, and executing specific actions based on input parameters.

```ahk
; HT++ Functions Documentation

; Functions return different types of values.
; Choosing the correct return type ensures proper function behavior.
; Below are examples for each return type:

; int function
; Use for operations with whole numbers.
; Returns a whole number as the result.
func int add(int a, int b)
{
    return a + b
}

; str function
; Use for text or string manipulation.
; Returns the resulting string.
func str concatenate(str a, str b)
{
    return a . b
}

; void function
; Use for actions that don't require a return value.
; Performs an action like displaying a message.
func void printMessage(str message)
{
    MsgBox, % message
}

; bool function
; Use to return true or false based on a condition.
; Evaluates a condition and returns a boolean value.
func bool isEven(int number)
{
    if (Mod(number, 2) == 0)
    {
        return true
    }
    else
    {
        return false
    }
}

; float function
; Use for operations with decimal numbers.
; Returns a decimal number as the result.
func float divide(float a, float b)
{
    return a / b
}

; Example Usage
; Simply label the main function since before we used other functions
main:

; int function example
int resultInt := add(3, 4)
MsgBox, % "Result of add(3, 4): " . STR(resultInt)

; str function example
str resultStr := concatenate("Hello, ", "World!")
MsgBox, % "Result of concatenate('Hello, ', 'World!'): " . resultStr

; void function example
printMessage("This is a message")

; bool function example
bool resultBool := isEven(10)
MsgBox, % "Is 10 even? " . STR(resultBool)

; float function example
float resultFloat := divide(7.5, 2.5)
MsgBox, % "Result of divide(7.5, 2.5): " . STR(resultFloat)
```

Functions with arrays as the param:

```ahk
func void testIntArray(arr int intArray, str secondParam)
{
MsgBox, % intArray
MsgBox, % "the secondParam is: " . secondParam
}

func void testStrArray(arr str strArray, str secondParam)
{
MsgBox, % strArray
MsgBox, % "the secondParam is: " . secondParam
}

func void testFloatArray(arr float floatArray, str secondParam)
{
MsgBox, % floatArray
MsgBox, % "the secondParam is: " . secondParam
}

; Simply label the main function since before we used other functions
main:

arr int intArray
arr str strArray
arr float floatArray

arr intArray .= 5
arr strArray .= "hello"
arr floatArray .= 3.14

str secondParam := "this is the secondParam"

testIntArray(intArray, secondParam)
testStrArray(strArray, secondParam)
testFloatArray(floatArray, secondParam)
```

Functions in HT++ empower developers to structure code effectively and promote code reuse. By following the Allman Style convention and leveraging global function scope, developers can create well-organized and maintainable scripts in HeavenToC++.

---

### If, else, else if <a id="if-else-else-if"></a>

[Go back](#features)

The `If`, `else`, and `else if` statements in HeavenToC++ (HT++) are fundamental control structures used for making decisions and executing different blocks of code based on specified conditions. These statements provide the ability to create branching logic within scripts, enabling developers to implement conditional behavior.

#### Syntax:

```ahk
if (condition)
{
    ; Code to execute if the condition is true
}
else if (anotherCondition)
{
    ; Code to execute if the first condition is false and this condition is true
}
else
{
    ; Code to execute if all preceding conditions are false
}
```

#### Parameters:

- `condition`: A Boolean expression that evaluates to either true or false.
- `anotherCondition`: An additional Boolean expression used in `else if` statements.

#### Example:

```ahk
; Example demonstrating the usage of if, else if, and else statements

int x := 10

if (x > 10)
{
    MsgBox, x is greater than 10
}
else if (x < 10)
{
    MsgBox, x is less than 10
}
else
{
    MsgBox, x is equal to 10
}
```

#### Advanced Usage:

In addition to simple comparisons, HT++ supports various logical operators such as `&&` (logical AND), `||` (logical OR), `and`, `or`, and negation `!` (logical NOT). These operators can be combined to form complex conditional expressions.

```ahk
; Example demonstrating the usage of logical operators in conditional expressions

int var1 := 3
int var2 := 5

if (var1 = 3) && (var2 = 5) or (var2 != 6)
{
    MsgBox, Condition is true
}
else
{
    MsgBox, Condition is false
}
```

Additionally, functions can be used within conditional statements to evaluate conditions dynamically. The `!` operator can be used to negate the result of a function call.

```ahk
; Example demonstrating the usage of function calls and negation in conditional statements

if (!collision())
{
    MsgBox, No collision detected
}
else
{
    MsgBox, Collision detected
}
```

In this example, the `collision` function is called within the `if` statement, and its return value is negated using the `!` operator. If the result of the `collision` function is false (indicating no collision), the message "No collision detected" is displayed. Otherwise, if a collision is detected, the message "Collision detected" is displayed.

#### Note:

- It's important to properly use parentheses to ensure the desired evaluation order when combining logical operators.
- Functions can be called within conditional statements to evaluate conditions dynamically, providing flexibility in script behavior.

The `If`, `else if`, and `else` statements, along with logical operators, provide powerful tools for implementing conditional logic in HeavenToC++ (HT++) scripts. By combining these features, developers can create dynamic and responsive applications capable of handling various scenarios and user inputs effectively.

---

### Random <a id="random"></a>

[Go back](#features)

The `Random` feature in HeavenToC++ (HT++) enables developers to generate random numbers within specified ranges. This functionality is particularly useful for scenarios where randomness is required, such as in game development, simulations, or randomized algorithms.

#### Syntax:

```ahk
Random, OutputVar, Min, Max
```

#### Parameters:

- `OutputVar`: The variable to store the generated random number.
- `Min`: The minimum value of the range (inclusive).
-
- `Max`: The maximum value of the range (inclusive).

#### Example:

```ahk
; Generate a random number between 1 and 100
Random, randomNumber, 1, 100

; Display the generated random number
MsgBox, % "Random number: " . STR(randomNumber)
```

or

```ahk
int var1 := 1
int var2 := 100

; Putting % doesn’t really matter; it’s just in case my muscle memory from AutoHotkey.

Random, OutputVar, %var1%, var2
; Display the generated random number
MsgBox, % "Random number: " . STR(OutputVar)
```

#### Usage:

The `Random` feature provides a simple yet effective way to introduce randomness into HT++ scripts. Whether it's for generating random numbers for game mechanics, simulating probabilistic events, or implementing randomized algorithms, the `Random` function offers flexibility and versatility in handling randomization requirements.

With the `Random` feature in HeavenToC++ (HT++), developers can easily incorporate randomness into their scripts, adding an element of unpredictability and dynamism to their applications. Whether it's for game development, simulations, or other scenarios requiring randomness, the `Random` function offers a straightforward solution for generating random numbers within specified ranges.

---

### Sleep <a id="sleep"></a>

[Go back](#features)

The `Sleep` feature in HeavenToC++ (HT++) allows developers to introduce delays or pauses in their scripts, which can be useful for various purposes such as controlling the timing of actions, implementing animations, or simulating real-time behavior.

#### Syntax:

```ahk
Sleep, Delay
```

#### Parameters:

- `Delay`: The duration of the pause in milliseconds. This can be an integer or a variable containing the desired delay duration.

#### Example:

```ahk
; Pause script execution for 2 seconds (2000 milliseconds)
Sleep, 2000
```

#### Usage:

The `Sleep` function is commonly used when precise timing is required between consecutive actions in a script. By specifying the desired delay duration, developers can control the pace of script execution, ensuring that actions occur at the intended times.

```ahk
; Example of using Sleep in a script
; This script waits for 3 seconds, then displays a message box
Sleep, 3000
MsgBox, Three seconds have passed!

; or

int sleepTime := 3000
Sleep, % sleepTime
MsgBox, Three seconds have passed!
```

In this example, the `Sleep` function is used to pause the script execution for 3000 milliseconds (3 seconds) before displaying a message box.

#### Note:

- Be mindful of using excessive `Sleep` statements, as they can introduce unnecessary delays and impact script performance.

The `Sleep` function in HeavenToC++ (HT++) provides a simple yet effective way to introduce pauses or delays in scripts, allowing developers to control the timing of actions and create more dynamic and interactive applications. Whether it's for controlling animations, simulating real-time behavior, or implementing precise timing in script execution, the `Sleep` function offers versatility and flexibility in managing script flow and timing.

---

### Msgbox <a id="msgbox"></a>

[Go back](#features)

The `MsgBox` function in HeavenToC++ (HT++) prints the text in the console. IT DOSE NOT MAKE A MSGBOX WINDOW EVEN IF THE NAME SUGGESTS IT.
#### Syntax:

```ahk
MsgBox, Text
```

#### Parameters:

- `Text`: The text printed in the console.

#### Note:

- The `MsgBox` function allows developers to prints the text in the console.
#### Examples:

```ahk
; Display a simple message box with text "Hello, World!"
MsgBox, Hello, World!

; declare the var1 as a string
str var1

; display varables
var1 := "hello man"
MsgBox, % var1

; display varables + text
var1 := "hello man"
MsgBox, % var1 . " how are you"

; or

var1 := "how are you"
MsgBox, % "hello man" . " " . var1

; you can also do
MsgBox, You can simply add text here
```

The `MsgBox` function in HeavenToC++ (HT++) provides developers with a versatile tool for creating informative and interactive ways to print to the console, enhancing user experience and facilitating communication between the script and the user. The `MsgBox` function offers flexibility and convenience in implementing various printing scenarios within HT++ scripts.

---

### FileRead <a id="fileread"></a>

[Go back](#features)

---

The `FileRead` feature in HeavenToC++ (HT++) allows you to read the contents of a file into a variable within your script.

#### Syntax:

```ahk
FileRead, OutputVar, FileName
```

#### Parameters:

- `OutputVar`: The variable to store the contents of the file.
- `FileName`: The name of the file to read. This can be specified as a literal string or using variables directly in the filename argument.

#### Example:

```ahk
; Read text content from the specified file if it's in the same folder as the script

; YOU MUST ALWAYS DECLARE THE VARIABLE
str FileContent
FileRead, FileContent, FileName.txt

; Display the content of the file
MsgBox, % FileContent

; To use a file path, we need to put it in a string like this
str FileName := "C:\\path\\to\\the\\file.extension"
FileRead, FileContent, % FileName

; Display the content of the file
MsgBox, % FileContent
```

#### Note:

- The contents of the file are read into the specified variable (`OutputVar`), allowing you to manipulate or display the file contents as needed within your script.

By following these guidelines, you can effectively use the `FileRead` feature in HeavenToC++ (HT++) to read text content from external files and incorporate it into your script.

---

### FileAppend <a id="fileappend"></a>

[Go back](#features)

---

The `FileAppend` feature in HeavenToC++ (HT++) enables you to append text content to a file.

#### Syntax:

```ahk
FileAppend, %TextToAppend%, FileName
```

#### Parameters:

- `TextToAppend`: The text content to append to the file.
- `FileName`: The name of the file to which the text will be appended. This can be specified as a literal string or using variables directly in the filename argument.

#### Example:

```ahk
; Append text content to the specified file
str text := "hello man"
FileAppend, %text%, FileName.txt
```

#### Note:

- The specified `TextToAppend` will be appended to the end of the file specified by `FileName`.

---

### SetTimer <a id="settimer"></a>

[Go back](#features)

In HeavenToC++ (HT++), the `SetTimer` command is used to create and control timers within the script. Timers allow developers to execute specific actions or functions at regular intervals, providing a mechanism for scheduling tasks and automating processes.

#### Syntax:

```ahk
SetTimer, LabelName, Option
```

#### Parameters:

- `LabelName`: The name of the label or subroutine to be executed when the timer elapses.
- `Option`: Specifies the interval and state of the timer. It can take one of the following values:
  - `Interval`: Specifies the interval in milliseconds at which the timer should elapse and trigger the execution of the specified label or subroutine.
  - `On`: Starts or enables the timer.
  - `Off`: Stops or disables the timer.

#### How to use it

```ahk
; set the timers helper vars here in the global scope

; timer 1 code1 using the count method
int code1TimerCount := 0
int code1TimerIsOnOrOff := 1

; timer 2 code2 using the count method
int code2TimerCount := 0
int code2TimerIsOnOrOff := 1


code1:
if (code1TimerIsOnOrOff = 1)
{
; using the count method
code1TimerCount++

; code here
; code here
; code here
; code here
MsgBox, % "hi111111111 = " . STR(code1TimerCount)
MsgBox, % A_TickCount
; code here
; code here
; code here
; code here

; using the count method
if (code1TimerCount = 5)
{
code1TimerCount := 0

code1TimerIsOnOrOff := 0
if (code1TimerIsOnOrOff = 0) && (code2TimerIsOnOrOff = 0)
{
SetTimer, code1, Off
} ; using the count method

}
}
else
{
if (code1TimerIsOnOrOff = 0) && (code2TimerIsOnOrOff = 0)
{
SetTimer, code1, Off
}

}
Return

code2:
if (code2TimerIsOnOrOff = 1)
{

; using the count method
code2TimerCount++
; using the count method

; code here
; code here
; code here
; code here
MsgBox, % "hi2 = " . STR(code2TimerCount)
MsgBox, % A_TickCount
; code here
; code here
; code here
; code here

; using the count method
if (code2TimerCount = 5)
{
code2TimerCount := 0

code2TimerIsOnOrOff := 0

if (code1TimerIsOnOrOff = 0) && (code2TimerIsOnOrOff = 0)
{
SetTimer, code2, Off
}
} ; using the count method

}
else
{
if (code1TimerIsOnOrOff = 0) && (code2TimerIsOnOrOff = 0)
{
SetTimer, code2, Off
}

}
Return

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; timer 3 code3 using the once the code is done method
int code3TimerIsOnOrOff := 1

; timer 4 code4 using the count method
int code4TimerCount := 0
int code4TimerIsOnOrOff := 1

; timer 5 code5 using the once the code is done method
int code5TimerIsOnOrOff := 1

code3:
if (code3TimerIsOnOrOff = 1)
{

; code here
; code here
; code here
; code here
MsgBox, % "hi3333333"
MsgBox, % A_TickCount
; code here
; code here
; code here
; code here

;; code here start
Loop, 10000000
{
; some code
if (A_Index = 9999990)
{
break
}
}
;; code here end

; using the once the code is done method

code3TimerIsOnOrOff := 0
if (code3TimerIsOnOrOff = 0) && (code4TimerIsOnOrOff = 0) && (code5TimerIsOnOrOff = 0)
{
SetTimer, code3, Off
}

}
else
{
if (code3TimerIsOnOrOff = 0) && (code4TimerIsOnOrOff = 0) && (code5TimerIsOnOrOff = 0)
{
SetTimer, code3, Off
}

}
Return

code4:
if (code4TimerIsOnOrOff = 1)
{
; using the count method
code4TimerCount++

; code here
; code here
; code here
; code here
MsgBox, % "hi444444 = " . STR(code4TimerCount)
MsgBox, % A_TickCount
; code here
; code here
; code here
; code here
;; code here start
Loop, 10000000
{
; some code
if (A_Index = 9999990)
{
break
}
}
;; code here end

; using the count method
if (code4TimerCount = 5)
{
code4TimerCount := 0

code4TimerIsOnOrOff := 0
if (code3TimerIsOnOrOff = 0) && (code4TimerIsOnOrOff = 0) && (code5TimerIsOnOrOff = 0)
{
SetTimer, code4, Off
} ; using the count method

}
}
else
{
if (code3TimerIsOnOrOff = 0) && (code4TimerIsOnOrOff = 0) && (code5TimerIsOnOrOff = 0)
{
SetTimer, code4, Off
}

}
Return

code5:
if (code5TimerIsOnOrOff = 1)
{

; code here
; code here
; code here
; code here
MsgBox, % "hi555555"
MsgBox, % A_TickCount
; code here
; code here
; code here
; code here

;; code here start
Loop, 10000000
{
; some code
if (A_Index = 9999990)
{
break
}
}
;; code here end

; using the once the code is done method

code5TimerIsOnOrOff := 0
if (code3TimerIsOnOrOff = 0) && (code4TimerIsOnOrOff = 0) && (code5TimerIsOnOrOff = 0)
{
SetTimer, code5, Off
}

}
else
{
if (code3TimerIsOnOrOff = 0) && (code4TimerIsOnOrOff = 0) && (code5TimerIsOnOrOff = 0)
{
SetTimer, code5, Off
}

}
Return

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; simply label the main function since before we used other functions
main:

int StartTime := INT(A_TickCount)

; set the timers helper vars in the global scope
SetTimers
; WE MUST PUT THE TIMER WITH THE LEAST CYCLE TIME ON TOP TO BOTTOM UNLESS THE ARE THE SAME
SetTimer, code1, 500
SetTimer, code2, 1000
StartTimers
; code will countie after the timers stop

MsgBox, =====================================
MsgBox, =====================================
MsgBox, =====================================

; reset the timers helper vars here in between sesions

; timer 1 code1 using the count method
code1TimerCount := 0
code1TimerIsOnOrOff := 1

; timer 2 code2 using the count method
code2TimerCount := 0
code2TimerIsOnOrOff := 1

SetTimers
; WE MUST PUT THE TIMER WITH THE LEAST CYCLE TIME ON TOP TO BOTTOM UNLESS THE ARE THE SAME
SetTimer, code2, 500
SetTimer, code1, 1000
StartTimers
; code will countie after the timers stop

MsgBox, =====================================
MsgBox, =====================================
MsgBox, =====================================

; set the timers helper vars in the global scope

SetTimers
; WE MUST PUT THE TIMER WITH THE LEAST CYCLE TIME ON TOP TO BOTTOM UNLESS THE ARE THE SAME

; if you are using the once the code is done method
; then you can just set the timer to 10 ms
SetTimer, code3, 10
SetTimer, code4, 900
SetTimer, code5, 900
StartTimers

int ElapsedTime := INT(A_TickCount) - StartTime

int ms := ElapsedTime

; Calculate the components
int hours := Floor(ms / 3600000)
ms := Mod(ms, 3600000)
int minutes := Floor(ms / 60000)
ms := Mod(ms, 60000)
int seconds := Floor(ms / 1000)
int milliseconds := Mod(ms, 1000)

; Display the result
str ElapsedTime123 := ""
ElapsedTime123 .= STR(hours) . "h " . STR(minutes) . "m " . STR(seconds) . "s " . STR(milliseconds) . "ms"

MsgBox, % ElapsedTime123

; No need to add Return to the main function since it ends at the bottom
; And we always must use it cuz c++ will run it not us and its a must
; BUT if you don't declare any functions we don't need to add the main label
```

#### Note:

- Timers in HT++ typically involve setting up a label or subroutine to be executed at specified intervals using the `SetTimer` command.
- The `Option` parameter determines the behavior of the timer:
  - When `Interval` is specified, the timer will elapse at the specified interval and trigger the execution of the specified label or subroutine.
  - When `On` is specified, the timer is started or enabled, allowing it to trigger at the specified interval.
  - When `Off` is specified, the timer is stopped or disabled, preventing it from triggering until it is re-enabled using the `On` option.

#### Usage:

Timers are commonly used in scripts to perform periodic tasks, such as checking for updates, refreshing data, or triggering specific actions at regular intervals. By utilizing timers, developers can automate repetitive tasks and improve the efficiency and responsiveness of their scripts and applications.

#### Important Note:

- When using timers, ensure that the specified label or subroutine is defined and contains the necessary code to be executed when the timer elapses.
- Use caution when enabling or disabling timers dynamically during script execution to avoid unintended behavior or conflicts with other script logic.

The `SetTimer` command in HT++ provides a flexible and powerful way to incorporate timed events and automation into scripts, enabling developers to create more dynamic and responsive applications. By leveraging timers, developers can enhance the functionality and usability of their scripts by scheduling tasks and executing actions at specified intervals.

---

### Labels <a id="labels"></a>

[Go back](#features)

Labels in HeavenToC++ (HT++) serve as markers within the script to designate specific sections of code for execution. They are commonly used in conjunction with `Gosub` commands to redirect the script flow to the labeled sections.

#### Syntax:

Labels are defined using a colon `:` followed by the label name.

Example:

```ahk
LabelName:
    ; Code to be executed within the label
Return
```

#### Usage:

Labels are typically used in conjunction with `Gosub` commands to direct the script flow to the labeled section. The `Gosub` command is used to call a subroutine defined by a label.

#### Example:

```ahk
Label1:
    MsgBox, We are in Label1
; Use uppercase Return to end the label
Return

; simply label the main function since before we used other functions
main:

; We will go to the label
gosub, Label1
```

In this example, the script invokes the `Gosub` command to execute the code within the `Label1` section. Once the execution of the labeled code is complete, the script continues execution after the `Gosub` command.

#### Note:

- Labels provide a means to organize and structure the script flow, making it easier to manage and maintain complex scripts.
- Always use an uppercase `Return` at the end of a label to signify its termination, ensuring proper script execution.
- Labels are often utilized in combination with conditional statements and loops to control the flow of the script based on certain conditions or criteria.

For more information on `Return`, refer to [Return/return](#return).

---

### Gosub <a id="gosub"></a>

[Go back](#features)

In HeavenToC++ (HT++), the `Gosub` command is used to call a subroutine defined by a label within the script. Subroutines are sections of code marked by labels, and the `Gosub` command redirects the script flow to execute the code within the specified subroutine.

#### Syntax:

```ahk
Gosub, Target
```

#### Parameters:

- `Target`: The name of the label marking the subroutine to be executed.

#### Usage:

The `Gosub` command is commonly used to organize code into manageable sections and facilitate code reuse by invoking specific subroutines as needed.

#### Example:

Consider the following example demonstrating the usage of the `Gosub` command:

```ahk
; Define a label marking the start of the subroutine
Subroutine1:
    MsgBox, This is Subroutine 1
    Return

; Define another label marking the start of another subroutine
Subroutine2:
    MsgBox, This is Subroutine 2
    Return

; simply label the main function since before we used other functions
main:

; Main script execution begins here
MsgBox, Main script execution started

; Call Subroutine1 using Gosub
Gosub, Subroutine1

; Continue main script execution after Subroutine1
MsgBox, Back to main script execution

; Call Subroutine2 using Gosub
Gosub, Subroutine2

; Continue main script execution after Subroutine2
MsgBox, Script execution completed
```

#### Output:

```
Main script execution started
This is Subroutine 1
Back to main script execution
This is Subroutine 2
Script execution completed
```

In this example, the `Gosub` command is used to call two different subroutines (`Subroutine1` and `Subroutine2`) defined by labels within the script. The script flow is redirected to execute the code within each subroutine, and after the execution of each subroutine, the script continues execution from where the `Gosub` command was called.

#### Note:

- Subroutines defined by labels provide a way to organize code into logical sections and improve code readability and maintainability.
- Always use an uppercase `Return` at the end of a subroutine to signify its termination, ensuring proper script execution.
- The `Gosub` command is typically used within conditional statements, loops, or other control structures to direct the script flow based on certain conditions or criteria.

---

### Return/return <a id="return"></a>

[Go back](#features)

The `Return` command in HeavenToC++ (HT++) serves distinct purposes based on its context within the script. It's crucial to differentiate between the uppercase `Return` and lowercase `return` to ensure proper script functionality and execution control.

#### 1. Uppercase `Return` at the End of Labels, Subroutines, and Hotkeys:

When concluding a label or subroutine, use the uppercase `Return` at the end to signify its termination. This ensures clarity in script structure and prevents unexpected behavior.

Example:

```ahk
Label1:
    ; Code for Label1
    if (var1 = 5)
    {
        ; Use lowercase return to stop label execution any further
        return
    }
    ; Use uppercase Return to end the label
    Return
```

#### 2. Lowercase `return` to Stop Code Execution:

Place lowercase `return` anywhere in the script to halt code execution after its occurrence. This is particularly useful when you want to prevent the script from proceeding further under certain conditions.

Example:

```ahk
If (condition)
{
    ; Code to be executed if the condition is met

    ; Use lowercase return to stop code execution
    return
}

; Code that should only run if the condition is not met
```

#### 3. Lowercase `return` in Functions:

Inside functions, utilize lowercase `return` to exit the function and return a value if necessary. This maintains consistency in coding style within the context of functions.

Example:

```ahk
func int sum(int a,int b)
{
    ; Function body
    return a + b
}
```

By understanding and applying these conventions, developers can manage script flow effectively, ensure proper termination of blocks, and enhance code readability in HeavenToC++ scripts.

---

### Loop <a id="loop"></a>

[Go back](#features)

The `Loop` feature in HeavenToC++ (HT++) provides a mechanism for repeating a block of code a specified number of times or until a certain condition is met. This functionality is essential for automating repetitive tasks, iterating over data structures, and implementing various control flow structures within scripts.

#### Syntax:

```ahk
Loop, Count
{
    ; Code block to be repeated
}
```

or

```ahk
Loop
{
    ; Code block to be repeated until a condition is met
    if (condition)
    {
        ; Code to execute if the condition is true
        break
    }
}
```

#### Parameters:

- `Count`: Optional. Specifies the number of iterations to execute the loop. If omitted, the loop will continue indefinitely until a `break` statement or other termination condition is encountered.

#### Example 1: Looping a Specific Number of Times

```ahk
; Loop 5 times and display a message
Loop, 5
{
    MsgBox, % "Iteration " . STR(A_Index)
}
```

#### Output 1:

```
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
```

#### Example 2: Looping Until a Condition is Met

```ahk
; Loop until a condition is met
Loop
{
    ; Code block to be repeated
    if (A_Index >= 5)
    {
        ; Exit the loop if the condition is true
        break
    }
}
```

In this example, the loop continues indefinitely until the condition `A_Index >= 5` is met. Once the condition is true, the loop terminates using the `break` statement.

#### Note:

- The loop variable `A_Index` contains the current iteration index within the loop.
- The `break` statement can be used to exit the loop prematurely based on a specific condition.
- The `Loop` feature provides flexibility in controlling the flow of execution within scripts, allowing for both fixed iteration counts and dynamic termination conditions.

The `Loop` feature in HeavenToC++ (HT++) offers a versatile mechanism for iterating over code blocks, enabling developers to automate repetitive tasks and implement various control flow structures within their scripts.

---

### Loop, Parse <a id="loop-parse"></a>

[Go back](#features)

The `Loop, Parse` feature in HeavenToC++ (HT++) facilitates the parsing of strings into separate elements based on a specified delimiter. This functionality is particularly useful for breaking down and processing data stored in delimited formats.

#### Syntax:

```ahk
Loop, Parse, InputString, Delimiters, OmitChars
{
    ; Action to be performed for each parsed element
    ; A_Index contains the current loop iteration index
    ; A_LoopField contains the current parsed element
}
```

#### Parameters:

- `InputString`: The string to be parsed.
- `Delimiters`: A string containing one or more characters used as delimiters for parsing. By default, if no delimiters are specified, each character in the input string will be treated as a separate element.
- `OmitChars`: Optional. A string containing one or more characters to be omitted during parsing.

#### Example 1: Parse Each Character

```ahk
; Example input string
str inputString := "Hello World"

; Parse the input string character by character
Loop, Parse, inputString
{
    ; A_LoopField contains the current parsed character
    MsgBox, % "Character " . STR(A_Index) . ": " . A_LoopField
}
```

#### Output 1:

```
Character 1: H
Character 2: e
Character 3: l
Character 4: l
Character 5: o
Character 6:
Character 7: W
Character 8: o
Character 9: r
Character 10: l
Character 11: d
```

#### Example 2: Parse Using `n` and `r` Delimiters

```ahk
; Example input string with newline and carriage return
str inputString := "Line 1`nLine 2`rLine 3"

; Parse the input string using `n` and `r` as delimiters
Loop, Parse, inputString, `n, `r
{
    ; A_LoopField contains the current parsed line
    MsgBox, % "Line " . STR(A_Index) . ": " . A_LoopField
}
```

#### Output 2:

```
Line 1: Line 1
Line 2: Line 2
Line 3: Line 3
```

#### Example 3: Parse Using Commas as Delimiters

```ahk
; Example input string with commas
str var1 := "Apple,Orange,Banana"

; Parse the input string using commas as delimiters
Loop, Parse, var1, `,
{
    ; A_LoopField contains the current parsed element
    MsgBox, % "Fruit " . STR(A_Index) . ": " . A_LoopField
}
```

#### Output 3:

```
Fruit 1: Apple
Fruit 2: Orange
Fruit 3: Banana
```

#### Example 4: Parse Using Pipe as Delimiters

```ahk
; Example input string with pipes
str var2 := "Alpha|Beta|Gamma"

; Parse the input string using pipes as delimiters
Loop, Parse, var2, "|"
{
    ; A_LoopField contains the current parsed element
    MsgBox, % "Value " . STR(A_Index) . ": " . A_LoopField
}
```

#### Output 4:

```
Value 1: Alpha
Value 2: Beta
Value 3: Gamma
```

In these examples, the `Loop, Parse` feature is utilized to parse the input strings into separate elements based on the specified delimiters. Each example demonstrates parsing the input string using different delimiters (`n`, `r`, `,`, `|`) to extract individual elements. The loop variable `A_LoopField`contains the current parsed element during each iteration, and`A_Index` contains the current loop iteration index.

The `Loop, Parse` feature in HT++ provides a convenient and efficient way to process delimited strings, making it easier to work with structured data in various applications. Whether dealing with configuration settings, text processing, or other delimited data formats, the `Loop, Parse` functionality offers a powerful tool for data manipulation and extraction within HeavenToC++ scripts.

---

### Variables <a id="variables"></a>

[Go back](#features)

Variables in HeavenToC++ (HT++) are used to store and manipulate data values within scripts. They provide a means of storing information that can be referenced and modified throughout the script.

#### Declaration and Assignment:

Variables in HT++ are dynamically typed, meaning they can hold values of any data type without requiring explicit declaration. To assign a value to a variable, use the variable name followed by the assignment operator `:=`. For example:

```ahk
int myNumber := 42
str myString := "Hello, World!"
float myFloat := 3.14
bool myFlagSet := true
; we also have int8, int16, int32 and int64
```

#### Data Types:

HT++ supports various data types for variables, including:

- **Numeric**: Integers, decimals, and floating-point numbers.
- **String**: Textual data enclosed in double quotes.
- **Boolean**: True or false values.

#### Naming Convention:

Variable names in HT++ are case-insensitive and can consist of letters, digits, and underscores. However, they must begin with a letter. Descriptive names are recommended to reflect the purpose or content of the variable for better code readability.
Don't declare variables with names like let, var, or const since this will result in an error upon execution.

WARNING: NEVER NAME A VARIABLE THE SAME NAME AS A FUNCTION NAME

#### Scope:

Variables in HT++ have the same scope rules as C++, as HT++ transpiles to C++. This means:

- **Global Scope**: Variables declared outside of any function or block have global scope and can be accessed from anywhere within the script.
- **Local Scope**: Variables declared inside a function or block have local scope and are accessible only within that function or block.

#### Example:

```ahk
; Declare and assign variables
int myNumber := 42
str myString := "Hello, World!"
float myFloat := 3.14
bool myFlagSet := true

; Display variable values
MsgBox, % "Number: " . STR(myNumber) . "`nString: " . myString . "`nFloat: " . STR(myFloat) . "`nmyFlagSet is: " . STR(myFlagSet)
```

### Using Variables in Features

Variables in HeavenToC++ (HT++) can be utilized in various features to enhance flexibility and customization. Here's how to use variables in different contexts, ensuring to follow the specified methods:

#### 1. Normal Usage:

In normal usage, variables are concatenated with other strings or values using the `.` operator. Here is all the places you MUST use it.

1. In MsgBox:
   Specifically, in a MsgBox, we need to start with `%` just like down below. Make sure there is a space both before and after `%`:

```ahk
MsgBox, % "var1 is " . var1
```

#### 2. Single Usage:

In single usage, variables are enclosed within `%` symbols and directly inserted into the script. For example:

```ahk
FileAppend, %var1%, filename.txt
```

Please note: In these examples, ensure to follow the specified methods and refrain from using other types of variable usage for consistency and compatibility within HeavenToC++ (HT++).

#### Note:

- Variable names are case-insensitive.
- Avoid using reserved keywords as variable names to prevent conflicts.
- Ensure descriptive variable names for clarity and maintainability.
- Initialize variables before using them to avoid unexpected behavior.

Variables play a crucial role in storing and manipulating data within HeavenToC++ (HT++) scripts, providing developers with the flexibility to create dynamic and interactive applications.

---

### Arrays <a id="arrays"></a>

[Go back](#features)

In HT++ arrays are versatile data structures that can store multiple values under a single name. Arrays allow you to group related data together and perform operations on that data efficiently. Here’s what you need to know about arrays in HT++:

- **1-Indexed Arrays**: In HT++, arrays are 1-indexed, meaning the first element is accessed using index `1`. The 0th element is used to store the number of elements in the array by default.

#### **Understanding the Array Structure**

**Indexing**:

- **1-Indexed**: The array starts with index `1`. For example, `MyArray[1]` refers to the first element.
- **0th Element**: The element at index `0` holds the number of elements in the array. This is useful for determining the size of the array.

#### **Creating and Using Arrays**

1. **Declaration**:
   Arrays must be declared with a specific type (`int`, `float`, or `str`). If no type is specified, the array defaults to `str`. You can declare arrays for integers, floating-point numbers, or strings.

   ```ahk
   ; Integer array
   arr int MyIntArray

   ; Float array
   arr float MyFloatArray

   ; String array
   arr str MyStringArray
   ```

2. **Adding Elements**:
   Elements can be added to an array using the `arr` keyword followed by the array name and the `.=` operator. For indexed arrays, you can also directly assign values to specific indices.

   ```ahk
   ; Adding elements to an integer array
   arr MyIntArray .= 5
   MyIntArray[2] := 10
   ```

3. **Reassigning Elements**:
   To update or change the value of an element at a specific index, use the index notation.

   ```ahk
   ; Reassign an element in the float array
   MyFloatArray[1] := 7.5
   ```

4. **Printing Array Elements**:
   To print or display the contents of an array, use `MsgBox`. For integer or float arrays, you may need to use the `STR()` function to convert array elements to string format.

   ```ahk
   MsgBox, % "The number of elements in the array MyIntArray is: " . STR(MyIntArray[0])
   MsgBox, Here are all the elements in the array MyIntArray
   MsgBox, % MyIntArray
   ```

5. **Splitting Strings into Arrays**:
   You can split a string into an array using a delimiter. This is useful for parsing text data.

   ```ahk
   str text := "one two three four"
   arr splitArray := arrSplit(text, " ")
   ```

#### **Examples**

Here are examples of working with different types of arrays in HT++:

##### Integer Arrays

```ahk
; Declare an integer array
arr int MyArray123

; Add elements to the array
arr MyArray123 .= 6
arr MyArray123 .= 6

; Add an element to the second position
MyArray123[2] += 9

; Reassign an element
MyArray123[3] := 7

; Display array information
MsgBox, % "The number of elements in MyArray123 is: " . STR(MyArray123[0])
MsgBox, Here are all the elements in MyArray123
MsgBox, % MyArray123
```

##### Float Arrays

```ahk
; Declare a float array
arr float MyArray123456

; Add elements to the array
arr MyArray123456 .= 6.5
arr MyArray123456 .= 9
MyArray123456[2] += 9.1
arr MyArray123456 .= 6.9

; Reassign an element
MyArray123456[3] := 7

; Display array information
MsgBox, % "The number of elements in MyArray123456 is: " . STR(MyArray123456[0])
MsgBox, Here are all the elements in MyArray123456
MsgBox, % MyArray123456
```

##### String Arrays and Splitting

```ahk
; string arrays

; declare the array
arr str MyArray12345678

; add an element to the array
arr MyArray12345678 .= "hello"

; add an element to the array
arr MyArray12345678 .= "man"

; concatenate an element to the second element of the array array
MyArray12345678[2] .= " how"

; add an element to the array
arr MyArray12345678 .= "is"

; reassign an element in the array
MyArray12345678[3] := "are"

; add an element to the array
arr MyArray12345678 .= "you"

; we can also do this

MsgBox, % "the number of elements in the array MyArray12345678 is: " . MyArray12345678[0]
MsgBox, Here are all the elements in the array MyArray12345678
MsgBox, % MyArray12345678

; Declare a string variable and split it into an array
str text := "some text with spaces"
arr splitArray := arrSplit(text, " ")

; Display array information
MsgBox, % "The number of elements in splitArray is: " . splitArray[0]
MsgBox, Here are all the elements in splitArray
MsgBox, % splitArray
```

**Note:** If you don’t specify the type of the array, it defaults to `str`.

#### **Example Function: Removing Repeating Words**

```ahk
func str removeRepeatingWords(str text)
{
    str out
    arr words := arrSplit(text, " ")
    arr words .= " "

    Loop, Parse, text, " "
    {
        if (A_LoopField != words[A_Index + 1])
        {
            out .= A_LoopField . " "
        }
    }
    StringTrimRight, out, out, 1
    return out
}

; Main function
main:
str text := "hello hello hello man man whats up up today today how are you you doing"
MsgBox, % removeRepeatingWords(text)
```

In this example, the function `removeRepeatingWords` removes consecutive duplicate words from a string by splitting the text into an array, processing it, and then reconstructing the string without repeats.

---

### RunCMD and ExitApp <a id="runcmd-and-exitapp"></a>

[Go back](#features)

1. [RunCMD](#runcmd)
2. [ExitApp](#exitapp)

### RunCMD <a id="runcmd"></a>

[Go back](#runcmd-and-exitapp)

The `RunCMD` function in HeavenToC++ (HT++) allows developers to execute a system command or script from within the current HT++ script. This can be particularly useful for integrating external processes or automating tasks that require command-line operations. It works on both Windows and Linux-like systems.

#### Syntax:

```ahk
RunCMD(Command)
```

#### Parameters:

- **Command**: The system command or script to be executed. This should be a string.

#### Examples:

```ahk
; run a simple command and display the output in a message box
str output := RunCMD("echo Hello, World!")
MsgBox, % output
```

This function will execute the specified system command or script and display the output in a message box.

#### Note:

- The `RunCMD` function is used to run system commands or external scripts from within the HT++ script.
- It works on both Windows and Linux-like systems.

### ExitApp <a id="exitapp"></a>

[Go back](#runcmd-and-exitapp)

The `ExitApp` feature in HeavenToC++ (HT++) allows developers to terminate the currently active script. This functionality is particularly useful for terminating script execution programmatically.

#### Syntax:

```ahk
ExitApp
```

#### Examples:

```ahk
; terminate the currently active script
ExitApp
```

This command will terminate the script execution.

#### Note:

- The `ExitApp` command is used to terminate script execution.

---

### Comments <a id="htpp-comments"></a>

[Go back](#features)

In HeavenToC++ (HT++), comments play a vital role in enhancing code readability and providing additional context for developers.

#### Syntax:

```ahk
; This is a single-line comment in HeavenToC++ (HT++)
```

```ahk
/*
This is a multiline comment.
It can span multiple lines.
Everything between the opening and closing is a comment.
*/
```

#### Usage:

Single-line comments are prefixed with a semicolon `;` and are typically placed on separate lines to ensure clarity and readability. They are used to add explanatory notes, document code behavior, or temporarily disable code segments without removing them entirely.

```ahk
; Define variables
int var1 := 5
; Initialize var1 with value 5

int var2 := 10
; Initialize var2 with value 10

; Calculate the sum of var1 and var2
int result := var1 + var2
; Store the result in the result variable

; Display the result
MsgBox, % "The sum is: " . STR(result)
; Show the sum in a message box
```

In this example, single-line comments are placed on separate lines to document variable initialization, calculation, and message display steps, providing clarity and context to the code.

#### Warning:

Do not add comments on the same line as code statements in HeavenToC++ (HT++). Placing comments inline with code is not supported.

**DO NOT** place comments on the same line as code statements in HeavenToC++ (HT++).

#### Note:

- Single-line comments should be concise and focused, providing relevant information to aid in code understanding.

Comments in HeavenToC++ (HT++) are invaluable tools for improving code comprehension and facilitating collaboration among developers. By leveraging single-line comments effectively, developers can create well-documented and maintainable scripts in HeavenToC++.

---

### Sort <a id="sort"></a>

[Go back](#features)

The `Sort` command in HT++ arranges the contents of a variable in alphabetical, numerical, or random order, and optionally removes duplicates.

#### Syntax:

```ahk
Sort, VarName , Options
```

#### Parameters:

- **VarName**: The name of the variable whose contents will be sorted. This cannot be an expression.

- **Options**: A string of one or more options (in any order, with optional spaces in between) from the Options section below.

#### Options:

- **C**: Case-sensitive sort (ignored if the `N` option is also present). If both `C` and `CL` are omitted, uppercase letters A-Z are considered identical to their lowercase counterparts for sorting purposes.

- **Dx**: Specifies `x` as the delimiter character for `VarName`. Default delimiter is linefeed (`n).

- **N**: Numeric sort. Treats each item as a number rather than a string for sorting purposes.

- **R**: Sorts in reverse order (alphabetically or numerically depending on other options).

- **Random**: Sorts in random order. Overrides other options except `D`, `Z`, and `U`.

- **U**: Removes duplicate items from the list so that every item is unique.

#### Examples:

```ahk
; declare the variable MyVar as a string
str MyVar

; Example 1: Sort alphabetically (default) with linefeed delimiter
MyVar := "apple`norange`nbanana`ngrape`napple`nbanana"
Sort, MyVar
MsgBox, % "Sorted Alphabetically:`n" . MyVar

; Example 2: Sort alphabetically case-insensitively with removal of duplicates
MyVar := "Apple`nOrange`nbanana`nGRAPE`nApple`nBanana"
Sort, MyVar, CU
MsgBox, % "Sorted Case-Insensitive with Unique:`n" . MyVar

; Example 3: Sort numerically
MyVar := "10`n2`n30`n4`n25`n1"
Sort, MyVar, N
MsgBox, % "Sorted Numerically:`n" . MyVar

; Example 4: Sort in reverse alphabetical order
MyVar := "apple`norange`nbanana`ngrape"
Sort, MyVar, R
MsgBox, % "Sorted Reverse Alphabetically:`n" . MyVar

; Example 5: Sort alphabetically with a custom delimiter (comma)
MyVar := "apple,orange,banana,grape"
Sort, MyVar, D,
MsgBox, % "Sorted with Custom Delimiter (comma):`n" . MyVar

; Example 6: Sort randomly and remove duplicates case-insensitively
MyVar := "apple`norange`nbanana`norange`napple`ngrape"
Sort, MyVar, Random
MsgBox, % "Sorted Randomly with Unique:`n" . MyVar

; Example 7: Sort numerically in reverse order with case-sensitive removal of duplicates
MyVar := "10`n2`n30`n2`n25`n1"
Sort, MyVar, NRUC
MsgBox, % "Sorted Numerically in Reverse with Unique and Case-Sensitive:`n" . MyVar
```

#### Remarks:

- This command is primarily used to sort a variable containing a list of lines, typically separated by linefeed (`n) characters.
- To populate a variable with lines from a file, use `FileRead` to load the entire file content into `MyVar`.

#### Notes:

- Ensure proper understanding of sorting behavior based on chosen options (`C`, `CL`, `N`, etc.) to achieve desired sorting results.
- Consider performance implications, especially when using `CL` option due to locale-based sorting.

---

### getDataFromAPI and getDataFromJSON <a id="getdatafromapi-and-getdatafromjson"></a>

[Go back](#features)

1. [getDataFromAPI](#getdatafromapi)
2. [getDataFromJSON](#getdatafromjson)

---

### getDataFromAPI <a id="getdatafromapi"></a>

[Go back](#getdatafromapi-and-getdatafromjson)

The `getDataFromAPI` function in HeavenToC++ (HT++) performs an HTTP GET request to retrieve data from an external API endpoint and processes the response asynchronously.

#### Syntax:

```ahk
getDataFromAPI(url)
```

#### Parameters:

- `url`: The URL of the API endpoint to request data from.

#### Example Usage:

```ahk
str jsonOutput := getDataFromAPI("https://api.example.com/data")
```

#### Notes:

- The `getDataFromAPI` function initiates an HTTP GET request to the specified API endpoint.

---

### getDataFromJSON <a id="getdatafromjson"></a>

[Go back](#getdatafromapi-and-getdatafromjson)

The `getDataFromJSON` function in HeavenToC++ (HT++) retrieves specific data from a JSON string using a path-like syntax to navigate nested objects and arrays.

#### Syntax:

```ahk
getDataFromJSON(jsonString, path)
```

#### Parameters:

- `jsonString`: The JSON string containing the data to parse.
- `path`: The path specifying the location of the desired data within the JSON structure.

#### Returns:

- The value retrieved from the specified path within the JSON structure.

#### JSON Path Examples and Usage:

```ahk
; Example usage:
str jsonData := getDataFromAPI("https://jsonplaceholder.typicode.com/users")

; Define JSON paths to retrieve specific data
str path1 := "[0].name"
str path2 := "[0].username"
str path3 := "[0].email"

MsgBox, % getDataFromJSON(jsonData, path1)
MsgBox, % getDataFromJSON(jsonData, path2)
MsgBox, % getDataFromJSON(jsonData, path3)
```

You can open the API URL in your web browser, then copy the JSON response from the API. Next, go to [jsonpathfinder.com](https://jsonpathfinder.com/) and paste the JSON. Then find your paths. Make sure not to copy the `x.` at the beginning of the string from the JSON path.

#### Notes:

- The `getDataFromJSON` function enables navigation through nested JSON objects using a path-like syntax.
- This function simplifies data extraction from complex JSON responses retrieved from APIs or other sources.

---

### Math Functions <a id="math-functions"></a>

[Go back](#features)

A collection of mathematical functions available in HT++.

1. [Abs](#abs)
2. [ACos](#acos)
3. [ASin](#asin)
4. [ATan](#atan)
5. [Ceil](#ceil)
6. [Cos](#cos)
7. [Exp](#exp)
8. [Floor](#floor)
9. [Ln](#ln)
10. [Log](#log)
11. [Round](#round)
12. [Sin](#sin)
13. [Sqrt](#sqrt)
14. [Tan](#tan)

---

## Explanation of Math Functions

### Abs <a id="abs"></a>

[Go back](#math-functions)

**Abs**: Returns the absolute value of a number.

#### Syntax:

```ahk
int result := Abs(number)
```

#### Parameters:

- _number_: The number for which you want to find the absolute value.

#### Return Value:

- Returns the absolute value of the input number.

#### Example:

```ahk
int absValue := Abs(-5)
MsgBox, % "The absolute value of -5 is " . STR(absValue)
```

---

### ACos <a id="acos"></a>

[Go back](#math-functions)

**ACos**: Returns the arccosine (in radians) of a number.

#### Syntax:

```ahk
float result := ACos(number)
```

#### Parameters:

- _number_: The number for which you want to find the arccosine.

#### Return Value:

- Returns the arccosine of the input number in radians.

#### Example:

```ahk
float arcCos := ACos(0.5)
MsgBox, % "The arccosine of 0.5 is " . STR(arcCos)
```

---

### ASin <a id="asin"></a>

[Go back](#math-functions)

**ASin**: Returns the arcsine (in radians) of a number.

#### Syntax:

```ahk
float result := ASin(number)
```

#### Parameters:

- _number_: The number for which you want to find the arcsine.

#### Return Value:

- Returns the arcsine of the input number in radians.

#### Example:

```ahk
float arcSin := ASin(0.5)
MsgBox, % "The arcsine of 0.5 is " . STR(arcSin)
```

---

### ATan <a id="atan"></a>

[Go back](#math-functions)

**ATan**: Returns the arctangent (in radians) of a number.

#### Syntax:

```ahk
float result := ATan(number)
```

#### Parameters:

- _number_: The number for which you want to find the arctangent.

#### Return Value:

- Returns the arctangent of the input number in radians.

#### Example:

```ahk
float arcTan := ATan(0.5)
MsgBox, % "The arctangent of 0.5 is " . STR(arcTan)
```

---

### Ceil <a id="ceil"></a>

[Go back](#math-functions)

**Ceil**: Returns the smallest integer greater than or equal to a number.

#### Syntax:

```ahk
int result := Ceil(number)
```

#### Parameters:

- _number_: The number for which you want to find the smallest integer greater than or equal to.

#### Return Value:

- Returns the smallest integer greater than or equal to the input number.

#### Example:

```ahk
int ceiled := Ceil(4.3)
MsgBox, % "The smallest integer greater than or equal to 4.3 is " . STR(ceiled)
```

---

### Cos <a id="cos"></a>

[Go back](#math-functions)

**Cos**: Returns the cosine of an angle (in radians).

#### Syntax:

```ahk
float result := Cos(angle)
```

#### Parameters:

- _angle_: The angle (in radians) for which you want to find the cosine.

#### Return Value:

- Returns the cosine of the input angle.

#### Example:

```ahk
float cosValue := Cos(0)
MsgBox, % "The cosine of 0 radians is " . STR(cosValue)
```

---

### Exp <a id="exp"></a>

[Go back](#math-functions)

**Exp**: Returns the value of E raised to the power of a number.

#### Syntax:

```ahk
float result := Exp(number)
```

#### Parameters:

- _number_: The exponent to which E is raised.

#### Return Value:

- Returns E raised to the power of the input number.

#### Example:

```ahk
float expValue := Exp(2)
MsgBox, % "E raised to the power of 2 is " . STR(expValue)
```

---

### Floor <a id="floor"></a>

[Go back](#math-functions)

**Floor**: Returns the largest integer less than or equal to a number.

#### Syntax:

```ahk
int result := Floor(number)
```

#### Parameters:

- _number_: The number for which you want to find the largest integer less than or equal to.

#### Return Value:

- Returns the largest integer less than or equal to the input number.

#### Example:

```ahk
int floored := Floor(4.9)
MsgBox, % "The largest integer less than or equal to 4.9 is " . STR(floored)
```

---

### Ln <a id="ln"></a>

[Go back](#math-functions)

**Ln**: Returns the natural logarithm of a number.

#### Syntax:

```ahk
float result := Ln(number)
```

#### Parameters:

- _number_: The number for which you want to find the natural logarithm.

#### Return Value:

- Returns the natural logarithm of the input number.

#### Example:

```ahk
float lnValue := Ln(2.71828)
MsgBox, % "The natural logarithm of 2.71828 is " . STR(lnValue)
```

---

### Log <a id="log"></a>

[Go back](#math-functions)

**Log**: Returns the logarithm of a number to a specified base.

#### Syntax:

```ahk
float result := Log(number)
```

#### Parameters:

- _number_: The number for which you want to find the natural logarithm.

#### Return Value:

- Returns the natural logarithm of the input number.

#### Example:

```ahk
float logValue := Log(100)
MsgBox, % "The natural logarithm of 100 is " . STR(logValue)
```

---

### Round <a id="round"></a>

[Go back](#math-functions)

**Round**: Returns the nearest integer to a number.

#### Syntax:

```ahk
int result := Round(number)
```

#### Parameters:

- _number_: The number to be rounded.

#### Return Value:

- Returns the nearest integer to the input number.

#### Example:

```ahk
int rounded := Round(4.6)
MsgBox, % "The nearest integer to 4.6 is " . STR(rounded)
```

---

### Sin <a id="sin"></a>

[Go back](#math-functions)

**Sin**: Returns the sine of an angle (in radians).

#### Syntax:

```ahk
float result := Sin(angle)
```

#### Parameters:

- _angle_: The angle (in radians) for which you want to find the sine.

#### Return Value:

- Returns the sine of the input angle.

#### Example:

```ahk
float sinValue := Sin(0)
MsgBox, % "The sine of 0 radians is " . STR(sinValue)
```

---

### Sqrt <a id="sqrt"></a>

[Go back](#math-functions)

**Sqrt**: Returns the square root of a number.

#### Syntax:

```ahk
float result := Sqrt(number)
```

#### Parameters:

- _number_: The number for which you want to find the square root.

#### Return Value:

- Returns the square root of the input number.

#### Example:

```ahk
float sqrtValue := Sqrt(9)
MsgBox, % "The square root of 9 is " . STR(sqrtValue)
```

---

### Tan <a id="tan"></a>

[Go back](#math-functions)

**Tan**: Returns the tangent of an angle (in radians).

#### Syntax:

```ahk
float result := Tan(angle)
```

#### Parameters:

- _angle_: The angle (in radians) for which you want to find the tangent.

#### Return Value:

- Returns the tangent of the input angle.

#### Example:

```ahk
float tanValue := Tan(0)
MsgBox, % "The tangent of 0 radians is " . STR(tanValue)
```

---

### Build-in Functions <a id="build-in-functions"></a>

[Go back](#features)

A collection of Build-in Function available in HT++.

1. [str](#str)
2. [int](#int)
3. [float](#float)
4. [input](#input)
5. [Chr](#chr)
6. [InStr](#instr)
7. [RegExMatch](#regexmatch)
8. [RegExReplace](#regexreplace)
9. [StrLen](#strlen)
10. [SubStr](#substr)
11. [Trim](#trim)
12. [StrReplace](#strreplace)
13. [Mod](#mod)
14. [Asc](#asc)
15. [StrLower](#strlower)

---

## Explanation of Build-in Functions

### str <a id="str"></a>

[Go back](#build-in-functions)

**str**: Converts a value into its string representation.

#### Syntax:

```ahk
result := STR(value)
```

#### Parameters:

- _value_: The value to convert into a string representation.

#### Return Value:

- Returns a string representation of the input value.

#### Example 1:

```ahk
int number := 42
str strNumber := STR(number)
MsgBox, % "The string representation of " . STR(number) . " is " . strNumber
```

#### Explanation:

The `STR` function converts a value into its string representation. In HT++, you cannot concatenate strings directly with numbers. You need to use `STR()` to convert numbers to strings for concatenation or other string operations.

In Example 1:

- `STR(number)` converts the number `42` into the string `"42"`.
- The variable `strNumber` now holds the string representation of `number`.
- The `MsgBox` command displays a message box showing: "The string representation of 42 is 42".

#### Example 2:

```ahk
age := 30
MsgBox, % "Your current age is " . STR(age)
```

#### Explanation:

In Example 2:

- `STR(age)` converts the number `30` into the string `"30"`.
- The `MsgBox` command concatenates the string `"Your current age is "` with the result of `STR(age)`, resulting in the message box displaying: "Your current age is 30".

This function is essential for converting numbers or other non-string values into strings when performing operations like concatenation, displaying messages, or storing textual data in variables.

---

### INT <a id="int"></a>

[Go back](#build-in-functions)

**int**: Converts a value into an integer.

#### Syntax:

```ahk
result := INT(value)
```

#### Parameters:

- _value_: The value to convert into an integer.

#### Return Value:

- Returns the integer representation of the input value.

#### Example:

```ahk
str numberAsString := "42"
int intValue := INT(numberAsString)
MsgBox, % "The integer value of " . numberAsString . " is " . STR(intValue)
```

#### Explanation:

The `INT` function converts a string representation of a number into an integer. In HT++, this is particularly useful when dealing with numeric input that is initially in string format, such as data from user input or external sources.

In the Example:

- `INT(numberAsString)` converts the string `"42"` into the integer `42`.
- The variable `intValue` now holds the integer representation of `numberAsString`.
- The `MsgBox` command displays a message box showing: "The integer value of 42 is 42".

This function is essential for converting string representations of numbers or floating-point numbers into integers when performing calculations, comparisons, or storing numeric data in variables.

---

### FLOAT <a id="float"></a>

[Go back](#build-in-functions)

The `FLOAT` function converts string representation of a number into a floating-point number in HT++. This is useful when dealing with numeric input that requires decimal precision.

#### Syntax:

```ahk
result = FLOAT(value)
```

#### Parameters:

- _value_: The value to convert into a floating-point number.

#### Return Value:

- Returns the floating-point representation of the input value.

#### Example:

```ahk
str stringFloat := "42.55"
float floatValue := FLOAT(stringFloat)
MsgBox, % "The floating-point value of " . stringFloat . " is " . STR(floatValue)
```

This function is essential for converting integer values, string representations of numbers, or other non-floating-point values into floating-point numbers when performing calculations, handling decimal data, or storing numeric data in variables in HT++.

---

### input <a id="input"></a>

[Go back](#build-in-functions)

**input**: Prompts the user for input and returns the user's response.

#### Syntax:

```ahk
str userInput = input(prompt)
```

#### Parameters:

- _prompt_: The text message to display to the user when asking for input.

#### Return Value:

- Returns the text entered by the user as a string.

#### Example 1:

```ahk
str userName := input("Please enter your name: ")
MsgBox, % "Hello, " . userName . "!"
```

#### Explanation:

The `input` function displays a prompt to the user and captures their input as a string. This is useful for gathering user input in a script, such as names, preferences, or other data.

In Example 1:

- `input("Please enter your name: ")` shows a prompt asking the user to enter their name.
- The variable `userName` captures the user's input.
- `MsgBox` then displays a greeting message: "Hello, [userName]!"

#### Example 2:

```ahk
str userAge := input("Enter your age: ")
MsgBox, % "You are " . userAge . " years old."
```

#### Explanation:

In Example 2:

- `input("Enter your age: ")` prompts the user to enter their age.
- The variable `userAge` stores the input as a string.
- `MsgBox` displays a message: "You are [userAge] years old."

The `input` function is essential for creating interactive scripts that require user feedback or data. It enables the script to capture and use user-provided information in various applications.

---

### Chr <a id="chr"></a>

[Go back](#build-in-functions)

**Chr**: Returns the character corresponding to a specified ASCII code.

#### Syntax:

```ahk
str result := Chr(asciiCode)
```

#### Parameters:

- _asciiCode_: The ASCII code for which you want to retrieve the corresponding character.

#### Return Value:

- Returns the character corresponding to the input ASCII code.

#### Example:

```ahk
str character := Chr(65)
MsgBox, % "The character corresponding to ASCII code 65 is " . character
```

---

### InStr <a id="instr"></a>

[Go back](#build-in-functions)

**InStr**: Returns true if a substring is found within a string; otherwise, returns false.

#### Syntax:

```ahk
InStr(haystack, needle)
```

#### Parameters:

- _haystack_: The string in which you want to search for the substring.
- _needle_: The substring you want to find within the haystack.

#### Return Value:

- Returns true if the substring is found within the string; otherwise, returns false.

#### Example:

```ahk
str var1 := "Hello World"

if (InStr(var1, "World"))
{
    MsgBox, % "We found 'World' in " . var1
}
```

---

### RegExMatch <a id="regexmatch"></a>

[Go back](#build-in-functions)

**RegExMatch**: Searches a string using a regular expression pattern and returns the position and length of the match.

#### Syntax:

```ahk
result := RegExMatch(subject, regexPattern, outputArray)
```

#### Parameters:

- _subject_: The string you want to search using the regular expression pattern.
- _regexPattern_: The regular expression pattern to match against the string.
- _outputArray_: (Optional) An array to store the position and length of the match.

#### Return Value:

- Returns the position of the match within the string. If outputArray is provided, it also stores the position and length of the match in the specified array.

### Example

```ahk
; Example
str var1 := "Hello World"
str regex := "World"
int matchPosition := RegExMatch(var1, regex)
if (matchPosition > 0)
{
    MsgBox, % "Found " . "'" . regex . "'" . " at position " . STR(matchPosition)
}
else
{
    MsgBox, No match found.
}
```

- **Explanation:**
  - **`var1 := "Hello World"`**: Defines a string `var1` containing "Hello World".
  - **`regex := "World"`**: Specifies a regular expression pattern to search for the substring "World".
  - **`matchPosition := RegExMatch(var1, regex)`**: Calls the `RegExMatch` function to find the position of the substring defined by `regex` within `var1`.
  - **`if (matchPosition > 0)`**: Checks if a match was found (`matchPosition` greater than 0).
  - **`MsgBox, Found '%regex%' at position %matchPosition%`**: Displays a message box indicating the position where the match was found if `regex` matches `var1`.
  - **`else`**: Executes if no match is found, displaying "No match found."

These examples demonstrate the usage of the `RegExMatch` function in HT++, using the provided implementation to perform regex matches and handle output as specified. Each example illustrates different scenarios where `RegExMatch` is used to find matches within strings using regular expressions in HT++.

---

### RegExReplace <a id="regexreplace"></a>

[Go back](#build-in-functions)

**RegExReplace**: Searches for and replaces occurrences of a regular expression pattern within a string.

#### Syntax:

```ahk
result := RegExReplace(subject, regexPattern, replacement)
```

#### Parameters:

- _subject_: The string in which to search for replacements using the regular expression pattern.
- _regexPattern_: The regular expression pattern to search for within the string.
- _replacement_: The replacement string to substitute in place of matches found.

#### Return Value:

- Returns the modified string with replacements performed. If _outputVar_ is provided, the modified string is stored in _outputVar_.

#### Example 1:

```ahk
str modifiedString := RegExReplace("Hello World", "World", "Universe")
MsgBox, % modifiedString
```

#### Example 2:

```ahk
str original := "The quick brown fox jumps over the lazy dog."
str modified := RegExReplace(original, "\\b\\w{4}\\b", "****")
MsgBox, % "Original: " . original . " Modified: " . modified
```

In these examples:

- Example 1 replaces "World" with "Universe" in the string "Hello World".
- Example 2 replaces all 4-letter words with "\*\*\*\*" in a given string.

Each example demonstrates different uses of the `RegExReplace` function to manipulate strings based on regular expression patterns.

---

### StrLen <a id="strlen"></a>

[Go back](#build-in-functions)

**StrLen**: Returns the length of a string.

#### Syntax:

```ahk
int result := StrLen(string)
```

#### Parameters:

- _string_: The string for which you want to find the length.

#### Return Value:

- Returns the length of the input string.

#### Example:

```ahk
int length := StrLen("Hello World")
MsgBox, % "The length of the string is " . STR(length)
```

---

### SubStr <a id="substr"></a>

[Go back](#build-in-functions)

**SubStr**: Returns a substring from a string.

#### Syntax:

```ahk
str result := SubStr(string, startPos, length)
```

#### Parameters:

- _string_: The string from which you want to extract a substring.
- _startPos_: The starting position of the substring.
- _length_: (Optional) The length of the substring to extract.

#### Return Value:

- Returns the extracted substring.

#### Example:

```ahk
str substring := SubStr("Hello World", 7)
MsgBox, % "The substring is " . substring

substring := SubStr("Hello World", 1, 5)
MsgBox, % "The first 5 characters are " . substring
```

---

### Trim <a id="trim"></a>

[Go back](#build-in-functions)

**Trim**: Removes leading and trailing whitespace from a string.

#### Syntax:

```ahk
str result := Trim(string)
```

#### Parameters:

- _string_: The string from which you want to remove leading and trailing whitespace.

#### Return Value:

- Returns the string with leading and trailing whitespace removed.

#### Example:

```ahk
str trimmedString := Trim("  Hello World  ")
MsgBox, % "The trimmed string is " . trimmedString
```

---

### StrReplace <a id="strreplace"></a>

[Go back](#build-in-functions)

**StrReplace**: Replaces occurrences of a substring within a string.

#### Syntax:

```ahk
str result := StrReplace(string, find, replace)
```

#### Parameters:

- _string_: The string in which you want to replace occurrences of a substring.
- _find_: The substring you want to replace.
- _replace_: The replacement string.

#### Return Value:

- Returns the modified string with occurrences of the substring replaced.

#### Example:

```ahk
str str1 := "Hello World"

str modifiedString := StrReplace(str1, "World", "Universe")
MsgBox, % "The modified string is " . modifiedString
```

---

### Mod <a id="mod"></a>

[Go back](#build-in-functions)

**Mod**: Returns the remainder of a division operation.

#### Syntax:

```ahk
result := Mod(dividend, divisor)
```

#### Parameters:

- _dividend_: The number to be divided.
- _divisor_: The number by which to divide the dividend.

#### Return Value:

- Returns the remainder of the division operation.

#### Example:

```ahk
; Define a string with a list of numbers separated by commas
str numbers := "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 33, 34, 20, 61, 100"

; Start a loop to parse each number from the string
Loop, Parse, numbers, ", "
{
    ; Convert the current loop field (A_LoopField) to an integer and check if it's even
    if (!Mod(INT(A_LoopField), 2))
    {
        ; If the number is even, display a message box with the even number
        MsgBox, % "The number " . A_LoopField . " is even"
    }
    else
    {
        ; If the number is odd, display a message box with the odd number
        MsgBox, % "The number " . A_LoopField . " is odd"
    }
}
```

---

### Asc <a id="asc"></a>

[Go back](#build-in-functions)

**Asc**: Returns the ASCII code of a character.

#### Syntax:

```ahk
int result := Asc(character)
```

#### Parameters:

- _character_: The character for which you want to retrieve the ASCII code.

#### Return Value:

- Returns the ASCII code of the input character.

#### Example:

```ahk
int asciiCode := Asc("A")
MsgBox, % "The ASCII code of 'A' is " . STR(asciiCode)
```

---

### StrLower <a id="strlower"></a>

[Go back](#build-in-functions)

**StrLower**: Converts a string to lowercase.

#### Syntax:

```ahk
str result := StrLower(string)
```

#### Parameters:

- _string_: The string to convert to lowercase.

#### Return Value:

- Returns the lowercase version of the input string.

#### Example:

```ahk
str var1 := "Hello World"
str lowercase := StrLower(var1)
MsgBox, % "The lowercase version of " . var1 . " is " . lowercase
```

This modified section explains the usage and purpose of `StrLower()` in HT++, demonstrating how to use it with an example. You can use this format to provide clear documentation for the `StrLower()` function.

---

### Build-in Variables <a id="build-in-variables"></a>

[Go back](#features)

Build-in Variables provided by HT++ for various purposes.

1. [A_Index](#a_index)
2. [A_LoopField](#a_loopfield)
3. [A_TickCount](#a_tickcount)
4. [A_Now](#a_now)
5. [A_YYYY](#a_yyyy)
6. [A_MM](#a_mm)
7. [A_DD](#a_dd)
8. [A_MMMM](#a_mmmm)
9. [A_MMM](#a_mmm)
10. [A_DDDD](#a_dddd)
11. [A_DDD](#a_ddd)
12. [A_Hour](#a_hour)
13. [A_Min](#a_min)
14. [A_Sec](#a_sec)
15. [A_Space](#a_space)
16. [A_Tab](#a_tab)

---

## Explanation of Build-in Variables

### A_Index <a id="a_index"></a>

[Go back](#build-in-variables)

**A_Index**: Contains the number of the current loop iteration in a loop.

#### Example:

```ahk
Loop, 5
{
    MsgBox, % "Loop iteration: " . STR(A_Index)
}
```

---

### A_LoopField <a id="a_loopfield"></a>

[Go back](#build-in-variables)

**A_LoopField**: Contains the contents of the current field (column) in a loop that is iterating over a delimited file or string.

#### Example:

```ahk
str var1 := "apple,banana,orange"

Loop, Parse, var1, `,
{
    MsgBox, % "Current field: " . A_LoopField
}
```

---

### A_TickCount <a id="a_tickcount"></a>

[Go back](#build-in-variables)

**A_TickCount**: Contains the number of milliseconds elapsed since the program started.

#### Example:

```ahk
int StartTime := INT(A_TickCount)

; code here
Sleep, 1500

int ElapsedTime := INT(A_TickCount) - StartTime
int ms := ElapsedTime

; Calculate the components
int hours := Floor(ms / 3600000)
ms := Mod(ms, 3600000)
int minutes := Floor(ms / 60000)
ms := Mod(ms, 60000)
int seconds := Floor(ms / 1000)
int milliseconds := Mod(ms, 1000)

; Display the result
str ElapsedTime123
ElapsedTime123 .= STR(hours) . "h " . STR(minutes) . "m " . STR(seconds) . "s " . STR(milliseconds) . "ms"

MsgBox, % ElapsedTime123
```

---

### A_Now <a id="a_now"></a>

[Go back](#build-in-variables)

**A_Now**: Contains the current local time in "Month/Day/Year, Hour:Minute:Second AM/PM" format.

#### Example:

```ahk
MsgBox, % "Current local time: " . A_Now
```

---

### A_YYYY <a id="a_yyyy"></a>

[Go back](#build-in-variables)

**A_YYYY**: Contains the current year in four digits.

#### Example:

```ahk
MsgBox, % "Current year: " . A_YYYY
```

---

### A_MM <a id="a_mm"></a>

[Go back](#build-in-variables)

**A_MM**: Contains the current month in two digits.

#### Example:

```ahk
MsgBox, % "Current month: " . A_MM
```

---

### A_DD <a id="a_dd"></a>

[Go back](#build-in-variables)

**A_DD**: Contains the current day of the month in two digits.

#### Example:

```ahk
MsgBox, % "Current day: " . A_DD
```

---

### A_MMMM <a id="a_mmmm"></a>

[Go back](#build-in-variables)

**A_MMMM**: Contains the full name of the current month.

#### Example:

```ahk
MsgBox, % "Full name of current month: " . A_MMMM
```

---

### A_MMM <a id="a_mmm"></a>

[Go back](#build-in-variables)

**A_MMM**: Contains the abbreviated name of the current month.

#### Example:

```ahk
MsgBox, % "Abbreviated name of current month: " . A_MMM
```

---

### A_DDDD <a id="a_dddd"></a>

[Go back](#build-in-variables)

**A_DDDD**: Contains the full name of the current day of the week.

#### Example:

```ahk
MsgBox, % "Full name of current day: " . A_DDDD
```

---

### A_DDD <a id="a_ddd"></a>

[Go back](#build-in-variables)

**A_DDD**: Contains the abbreviated name of the current day of the week.

#### Example:

```ahk
MsgBox, % "Abbreviated name of current day: " . A_DDD
```

---

### A_Hour <a id="a_hour"></a>

[Go back](#build-in-variables)

**A_Hour**: Contains the current hour in two digits (24-hour format).

#### Example:

```ahk
MsgBox, % "Current hour: " . A_Hour
```

---

### A_Min <a id="a_min"></a>

[Go back](#build-in-variables)

**A_Min**: Contains the current minute in two digits.

#### Example:

```ahk
MsgBox, % "Current minute: " . A_Min
```

---

### A_Sec <a id="a_sec"></a>

[Go back](#build-in-variables)

**A_Sec**: Contains the current second in two digits.

#### Example:

```ahk
MsgBox, % "Current second: " . A_Sec
```

---

### A_Space <a id="a_space"></a>

[Go back](#build-in-variables)

**A_Space**: Represents the space key.

#### Example:

```ahk
MsgBox, % "Hello" . A_Space . "man"
```

---

### A_Tab <a id="a_tab"></a>

[Go back](#build-in-variables)

**A_Tab**: Represents the tab key.

#### Example:

```ahk
MsgBox, % "|" . A_Tab . "Hello man|"
```

---

## Editors for Code <a id="editors-for-code"></a>

[Go back](#htpp)

Discover the recommended code editor for working with the HT++ programming language.

Check out the best editor for HT++ at https://github.com/TheMaster1127/SciTE4HTH

---

## Script Showcase <a id="script-showcase"></a>

[Go back](#htpp)

View a showcase of programs created using the HT++ programming language, demonstrating its capabilities.

Check some code written in HT++ at https://github.com/TheMaster1127/HT-plus-plus/blob/main/test.htpp

---
