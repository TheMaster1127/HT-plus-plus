# Define a dictionary to store dynamic variables
variables = {}

def LoopParseFunc(var, delimiter1="", delimiter2=""):
    import re
    if not delimiter1 and not delimiter2:
        # If no delimiters are provided, return a list of characters
        items = list(var)
    else:
        # Construct the regular expression pattern for splitting the string
        pattern = r'[' + re.escape(delimiter1) + re.escape(delimiter2) + r']+'
        # Split the string using the constructed pattern
        items = re.split(pattern, var)
    return items

def InStr(Haystack, Needle, CaseSensitive=True, StartingPos=1, Occurrence=1):
    if Haystack is None or Needle is None:
        return False
    StartingPos = max(StartingPos, 1)
    if not CaseSensitive:
        Haystack = Haystack.lower()
        Needle = Needle.lower()
    count = 0
    for i in range(StartingPos - 1, len(Haystack)):
        if Haystack[i:i + len(Needle)] == Needle:
            count += 1
            if count == Occurrence:
                return True
    return False  
def SubStr(str, startPos, length=None):
    if str is None or str == "":
        return ""
    if length is None or length == "":
        length = len(str) - startPos + 1
    if startPos < 1:
        startPos = len(str) + startPos
    return str[startPos - 1:startPos - 1 + length]
def Trim(inputString):
    if inputString is None:
        return ""
    return inputString.strip()
  
def StrReplace(originalString, find, replaceWith):
    # Use the replace method to replace occurrences of 'find' with 'replaceWith'
    return originalString.replace(find, replaceWith)
def StringTrimLeft(input, numChars):
    # Convert input to a string if it's not already a string
    if not isinstance(input, str):
        input = str(input)  # Convert input to string
    # Check if the input is long enough to perform trimming
    if len(input) >= numChars:
        return input[numChars:]  # Trim the string from the left
    else:
        return input  # Return input unchanged if numChars is larger than string length
def StringTrimRight(input, numChars):
    # Convert input to a string if it's not already a string
    if not isinstance(input, str):
        input = str(input)  # Convert input to string
    # Check if the input is long enough to perform trimming
    if len(input) >= numChars:
        return input[:-numChars]  # Trim the string from the right
    else:
        return input  # Return input unchanged if numChars is larger than string length
def StrLower(string):
    return string.lower()
def RegExReplace(inputStr, regexPattern, replacement):
    # Create a regular expression object using the provided pattern
    import re
    regex = re.compile(regexPattern, re.MULTILINE)  # re.MULTILINE for multi-line matching
    # Use the sub() method to perform the regex replacement
    resultStr = regex.sub(replacement, inputStr)
    # Return the modified string
    return resultStr
def StrSplit(inputStr, delimiter, num):
    # Check if the delimiter is empty
    if delimiter == '':
        # Return an empty string since splitting with an empty delimiter is not possible
        return ''
    # Split the input string based on the delimiter
    parts = inputStr.split(delimiter)
    # Return the part specified by the num parameter (1-based index)
    if 0 < num <= len(parts):
        return parts[num - 1]  # Return the specified part (0-based index)
    else:
        return ''  # Return an empty string if num is out of range
def Chr(number):
    # Check if the number is None
    if number is None:
        # Return an empty string
        return ""
    # Check if the number is within the valid Unicode range
    if 0 <= number <= 0x10FFFF:
        # Convert the number to a character using chr()
        return chr(number)
    else:
        # Return an empty string for invalid numbers
        return ""

# Custom Mod function in Python
def Mod(dividend, divisor):
    return dividend % divisor
import os
def FileRead(path):
    # Remove any extra double quotes around the path
    path = path.strip('"')
    # Ensure the path is absolute
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return ''
    except Exception as e:
        return None
import os
def FileAppend(content, path):
    # Remove any extra double quotes around the path
    path = path.strip('"')
    # Ensure the path is absolute
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)
    try:
        with open(path, 'a', encoding='utf-8') as file:  # 'a' mode for append
            file.write(content)
        return True
    except Exception as e:
        return False
import os
def FileDelete(path):
    # Ensure the path is absolute
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)
    try:
        if os.path.exists(path):
            os.remove(path)
    except Exception:
        pass    

import os
import sys
def GetParams():
    # Check if any command line arguments are provided
    if len(sys.argv) < 2:
        return ""
    # Store the provided command line arguments
    params = []
    for arg in sys.argv[1:]:
        if os.path.exists(arg):
            arg = os.path.abspath(arg)
        params.append(arg)
    return "\n".join(params)
import random
def SortLikeAHK(var_name, options):
    # Determine delimiter based on options
    delimiter = '\n'
    if 'D' in options:
        delimiter = options[options.index('D') + 1]
    
    # Split the input variable by delimiter
    items = var_name.split(delimiter)
    
    # Remove empty items and strip whitespace
    items = [item.strip() for item in items if item.strip()]
    
    # Apply sorting based on options
    if 'N' in options:
        # Numeric sort
        items.sort(key=lambda x: int(x))
    elif 'Random' in options:
        # Random sort
        random.shuffle(items)
    else:
        # Default alphabetical sort
        items.sort(key=lambda x: x.lower() if 'C' not in options else x)
    
    # Reverse if 'R' option is present
    if 'R' in options:
        items.reverse()
    
    # Remove duplicates if 'U' option is present
    if 'U' in options:
        seen = set()
        unique_items = []
        for item in items:
            lower_item = item.lower() if 'C' not in options else item
            if lower_item not in seen:
                seen.add(lower_item)
                unique_items.append(item)
        items = unique_items
    
    # Join the sorted items back into a string
    sorted_var = delimiter.join(items)
    
    return sorted_var
def RegExMatch(Haystack, NeedleRegEx, OutputVar=None, StartingPos=0):
    import re
    if Haystack is None or NeedleRegEx is None:
        return None
    regex = re.compile(NeedleRegEx)
    match = regex.search(Haystack)
    if match:
        if OutputVar is not None:
            OutputVar.append(match.group(0))
        return match.start() + 1
    else:
        return 0
def isVarAnumKindaVar(strrrrr):
    variables['strrrrr'] = strrrrr
    variables['strLettersStart'] = 48
    for A_Index1 in range(1, 10 + 1):
        variables['A_Index1'] = A_Index1
        if (InStr(variables['strrrrr'] , Chr(variables['strLettersStart']))):
            return True
        variables['strLettersStart'] += 1
    return False
def varDetect(strrrrr):
    variables['strrrrr'] = strrrrr
    if (InStr(variables['strrrrr'] , "-")):
        return False
    variables['numFixhsidhkcjzdls'] = 0
    items = LoopParseFunc(variables['strrrrr'])
    for A_Index2, A_LoopField2 in enumerate(items, start=1):
        variables['A_Index2'] = A_Index2
        variables['A_LoopField2'] = A_LoopField2
        variables['numFixhsidhkcjzdls'] += 1
    variables['numFixhsidhkcjzdls22'] = 0
    items = LoopParseFunc(variables['strrrrr'])
    for A_Index3, A_LoopField3 in enumerate(items, start=1):
        variables['A_Index3'] = A_Index3
        variables['A_LoopField3'] = A_LoopField3
        if (variables['A_LoopField3'] == Chr(48))or(variables['A_LoopField3'] == Chr(49))or(variables['A_LoopField3'] == Chr(50))or(variables['A_LoopField3'] == Chr(51))or(variables['A_LoopField3'] == Chr(52))or(variables['A_LoopField3'] == Chr(53))or(variables['A_LoopField3'] == Chr(54))or(variables['A_LoopField3'] == Chr(55))or(variables['A_LoopField3'] == Chr(56))or(variables['A_LoopField3'] == Chr(57))or(variables['A_LoopField3'] == Chr(46)):
            variables['numFixhsidhkcjzdls22'] += 1
    if (variables['numFixhsidhkcjzdls'] == variables['numFixhsidhkcjzdls22']):
        return False
    variables['strLettersStart'] = 97
    for A_Index4 in range(1, 26 + 1):
        variables['A_Index4'] = A_Index4
        if (InStr(variables['strrrrr'] , Chr(variables['strLettersStart']))):
            return True
        variables['strLettersStart'] += 1
    variables['strLettersStart'] = 65
    for A_Index5 in range(1, 26 + 1):
        variables['A_Index5'] = A_Index5
        if (InStr(variables['strrrrr'] , Chr(variables['strLettersStart']))):
            return True
        variables['strLettersStart'] += 1
    variables['strLettersStart'] = 48
    for A_Index6 in range(1, 10 + 1):
        variables['A_Index6'] = A_Index6
        if (InStr(variables['strrrrr'] , Chr(variables['strLettersStart']))):
            return True
        variables['strLettersStart'] += 1
    if (InStr(variables['strrrrr'] , Chr(95))):
        return True
    if (InStr(variables['strrrrr'] , Chr(37))):
        return True
    return False
def isVarAfuncOrWhat(varInVarTranspiler, funcNames, allVarsChars, allVarsInts):
    variables['varInVarTranspiler'] = varInVarTranspiler
    variables['funcNames'] = funcNames
    variables['allVarsChars'] = allVarsChars
    variables['allVarsInts'] = allVarsInts
    if (InStr(variables['varInVarTranspiler'] , "%")):
        variables['nameOfVarr11'] = Trim(StrSplit(variables['varInVarTranspiler'] , "%" , 1))
        variables['nameOfVarr12'] = Trim(StrSplit(variables['varInVarTranspiler'] , "%" , 2))
        if (SubStr(variables['nameOfVarr12'] , 1 , 1)== "["):
            variables['nameOfVarr12'] = StringTrimRight(variables['nameOfVarr12'], 1)
            variables['nameOfVarr12'] = StringTrimLeft(variables['nameOfVarr12'], 1)
            variables['nameOfVarr111'] = "variables[" + Chr(34) + variables['nameOfVarr11'] + Chr(34) + " + std::string(variables[" + Chr(34) + variables['nameOfVarr12'] + Chr(34) + "])]"
        else:
            variables['nameOfVarr111'] = "variables[" + Chr(34) + variables['nameOfVarr11'] + Chr(34) + " + STR(" + variables['nameOfVarr12'] + ")]"
        return variables['nameOfVarr111']
    items = LoopParseFunc(variables['allVarsChars'], "\n", "\r")
    for A_Index7, A_LoopField7 in enumerate(items, start=1):
        variables['A_Index7'] = A_Index7
        variables['A_LoopField7'] = A_LoopField7
        if (Trim(variables['varInVarTranspiler'])== Trim(variables['A_LoopField7'])):
            return variables['varInVarTranspiler']
    items = LoopParseFunc(variables['allVarsInts'], "\n", "\r")
    for A_Index8, A_LoopField8 in enumerate(items, start=1):
        variables['A_Index8'] = A_Index8
        variables['A_LoopField8'] = A_LoopField8
        if (Trim(variables['varInVarTranspiler'])== Trim(variables['A_LoopField8'])):
            return variables['varInVarTranspiler']
    items = LoopParseFunc(variables['funcNames'], "|")
    for A_Index9, A_LoopField9 in enumerate(items, start=1):
        variables['A_Index9'] = A_Index9
        variables['A_LoopField9'] = A_LoopField9
        if (variables['varInVarTranspiler'] == variables['A_LoopField9']):
            return variables['varInVarTranspiler']
        if (InStr(Trim(variables['varInVarTranspiler']), variables['A_LoopField9'] + "(")):
            return variables['varInVarTranspiler']
    if (SubStr(variables['varInVarTranspiler'] , 1 , 1)== "["):
        variables['varInVarTranspiler'] = StringTrimLeft(variables['varInVarTranspiler'], 1)
        variables['varInVarTranspiler'] = StringTrimRight(variables['varInVarTranspiler'], 1)
        return "variables[" + Chr(34) + variables['varInVarTranspiler'] + Chr(34) + "]"
    if (varDetect(variables['varInVarTranspiler'])):
        return variables['varInVarTranspiler']
    if (isVarAnumKindaVar(variables['varInVarTranspiler'])):
        return variables['varInVarTranspiler']
    if (variables['varInVarTranspiler'] == "."):
        return "+"
    if (variables['varInVarTranspiler'] == "="):
        return "=="
    if (variables['varInVarTranspiler'] == "or"):
        return "||"
    if (variables['varInVarTranspiler'] == "and"):
        return "&&"
    return variables['varInVarTranspiler']
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
def varTranspiler(var123, funcNames, allVarsChars, allVarsInts):
    variables['var123'] = var123
    variables['funcNames'] = funcNames
    variables['allVarsChars'] = allVarsChars
    variables['allVarsInts'] = allVarsInts
    variables['var123out'] = ""
    variables['lastType'] = ""
    variables['typeMode'] = 0
    #MsgBox, % var123
    variables['var123'] = StrReplace(variables['var123'] , ") or (" , " || ")
    variables['var123'] = StrReplace(variables['var123'] , ") || (" , " || ")
    variables['var123'] = StrReplace(variables['var123'] , ") and (" , " && ")
    variables['var123'] = StrReplace(variables['var123'] , ") && (" , " && ")
    variables['var123'] = StrReplace(variables['var123'] , ")  or  (" , "  ||  ")
    variables['var123'] = StrReplace(variables['var123'] , ")  ||  (" , "  ||  ")
    variables['var123'] = StrReplace(variables['var123'] , ")  and  (" , "  &&  ")
    variables['var123'] = StrReplace(variables['var123'] , ")  &&  (" , "  &&  ")
    variables['var123'] = StrReplace(variables['var123'] , "," , " , ")
    variables['var123'] = StrReplace(variables['var123'] , "(" , " ( ")
    variables['var123'] = StrReplace(variables['var123'] , ")" , " ) ")
    items = LoopParseFunc(variables['var123'], " ")
    for A_Index10, A_LoopField10 in enumerate(items, start=1):
        variables['A_Index10'] = A_Index10
        variables['A_LoopField10'] = A_LoopField10
        if (variables['A_LoopField10'] == "int")or(variables['A_LoopField10'] == "str"):
            variables['typeMode'] = 1
            variables['lastType'] = Trim(variables['A_LoopField10'])
        if (variables['A_LoopField10']  != "int")and(variables['A_LoopField10']  != "str")and(variables['typeMode'] == 1):
            variables['varInVarTranspiler'] = Trim(variables['A_LoopField10'])
            variables['varOut2out'] = isVarAfuncOrWhat(variables['varInVarTranspiler'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            if (variables['lastType'] == "int"):
                variables['varOut2out'] = "INT(" + variables['varOut2out'] + ")"
            if (variables['lastType'] == "str"):
                variables['varOut2out'] = "std::string(" + variables['varOut2out'] + ")"
            variables['var123out'] += str(variables['varOut2out']) + " "
            variables['typeMode'] = 0
        elif (variables['A_LoopField10']  != "int")and(variables['A_LoopField10']  != "str")and(variables['typeMode'] == 0):
            variables['varInVarTranspiler'] = Trim(variables['A_LoopField10'])
            variables['varOut2out'] = isVarAfuncOrWhat(variables['varInVarTranspiler'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            variables['var123out'] += str(variables['varOut2out']) + " "
    variables['var123out'] = StringTrimRight(variables['var123out'], 1)
    return variables['var123out']
def transpileLowVariables(sstr):
    variables['sstr'] = sstr
    variables['sstr'] = Trim(variables['sstr'])
    variables['outOftranspileVariablesOut'] = Chr(34)
    if (InStr(variables['sstr'] , Chr(37))):
        items = LoopParseFunc(variables['sstr'], "%")
        for A_Index11, A_LoopField11 in enumerate(items, start=1):
            variables['A_Index11'] = A_Index11
            variables['A_LoopField11'] = A_LoopField11
            if (Mod(variables['A_Index11'] , 2)):
                variables['outOftranspileVariablesOut'] += variables['A_LoopField11']
            else:
                variables['outOftranspileVariablesOut'] += Chr(34) + " + variables['" + variables['A_LoopField11'] + Chr(39) + Chr(93) + " + " + Chr(34)
    else:
        variables['sstr'] = Chr(34) + variables['sstr'] + Chr(34)
        return variables['sstr']
    variables['outOftranspileVariablesOut'] = variables['outOftranspileVariablesOut'] + Chr(34)
    return variables['outOftranspileVariablesOut']
variables['CheckIFandElsesss1'] = "if ("
variables['CheckIFandElsesss2'] = "if("
variables['CheckIFandElsesss3'] = "if !("
variables['CheckIFandElsesss4'] = "if!("
variables['CheckIFandElsesss5'] = "else if ("
variables['CheckIFandElsesss6'] = "else if("
variables['CheckIFandElsesss7'] = "else if !("
variables['CheckIFandElsesss8'] = "else if!("
variables['CheckIFandElsesssNum'] = 0
variables['onceImportTime'] = 0
variables['weUseRandomAtLeastOnce'] = 0
variables['weEverUseVars'] = ""
variables['haveWeEverUsedAloop'] = 0
variables['usedLib'] = ""
variables['putEndPointFlask1Up'] = ""
variables['putEndPointFlask2Down'] = ""
variables['AindexcharLength'] = 1
variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 0
variables['pycodeAcurlyBraceAddSomeVrasFixLP'] = 0
variables['pycodeLoopfixa'] = ""
variables['out'] = ""
variables['HTpyCodeD1'] = ""
variables['skipLeftCuleyForFuncPLS'] = 0
variables['eavbnsalvbaslv'] = 0
variables['theMainFuncDec'] = 0
variables['upCode'] = ""
variables['removeNextCurlyBraceCpp'] = 0
variables['params'] = GetParams()
items = LoopParseFunc(variables['params'], "\n", "\r")
for A_Index12, A_LoopField12 in enumerate(items, start=1):
    variables['A_Index12'] = A_Index12
    variables['A_LoopField12'] = A_LoopField12
    if (variables['A_Index12'] == 1):
        print(variables['A_LoopField12'])
        variables['filePathOfCode'] = variables['A_LoopField12']
        #MsgBox, % filePathOfCode
        variables['code'] = FileRead("" + variables['filePathOfCode'] + "")
        #MsgBox, % code
    if (variables['A_Index12'] == 2):
        print(variables['A_LoopField12'])
#MsgBox, % code
variables['nothing'] = ""
variables['code'] = StrReplace(variables['code'] , Chr(13), variables['nothing'])
variables['codeTrimBeggining'] = ""
items = LoopParseFunc(variables['code'], "\n", "\r")
for A_Index13, A_LoopField13 in enumerate(items, start=1):
    variables['A_Index13'] = A_Index13
    variables['A_LoopField13'] = A_LoopField13
    variables['codeTrimBeggining'] += Trim(variables['A_LoopField13']) + "\n"
variables['code'] = StringTrimRight(variables['codeTrimBeggining'], 1)
variables['HTpyCodeOUT754754'] = ""
variables['areWEinSome34sNum'] = 0
variables['theIdNumOfThe34'] = 0
items = LoopParseFunc(variables['code'])
for A_Index14, A_LoopField14 in enumerate(items, start=1):
    variables['A_Index14'] = A_Index14
    variables['A_LoopField14'] = A_LoopField14
    variables[f'theIdNumOfThe34theVar{variables["A_Index14"]}'] = Chr(34)
items = LoopParseFunc(variables['code'])
for A_Index15, A_LoopField15 in enumerate(items, start=1):
    variables['A_Index15'] = A_Index15
    variables['A_LoopField15'] = A_LoopField15
    if (variables['A_LoopField15'] == Chr(34)):
        variables['areWEinSome34sNum'] += 1
    if (variables['areWEinSome34sNum'] == 1):
        if (variables['A_LoopField15']  != Chr(34)):
            if (variables['A_LoopField15'] == Chr(96)):
                variables[f'theIdNumOfThe34theVar{variables["theIdNumOfThe34"]}'] += Chr(92)
            else:
                variables[f'theIdNumOfThe34theVar{variables["theIdNumOfThe34"]}'] += variables['A_LoopField15']
        else:
            variables['theIdNumOfThe34'] += 1
            variables['HTpyCodeOUT754754'] += "ihuiuuhuuhtheidFor--asas-theuhturtyphoutr-" + Chr(65) + Chr(65) + str(variables['theIdNumOfThe34']) + Chr(65) + Chr(65)
    if (variables['areWEinSome34sNum'] == 2)or(variables['areWEinSome34sNum'] == 0):
        if (variables['A_LoopField15']  != Chr(34)):
            variables['HTpyCodeOUT754754'] += variables['A_LoopField15']
        variables['areWEinSome34sNum'] = 0
variables['code'] = variables['HTpyCodeOUT754754']
for A_Index16 in range(1, variables['theIdNumOfThe34'] + 1):
    variables['A_Index16'] = A_Index16
    variables[f'theIdNumOfThe34theVar{variables["A_Index16"]}'] += Chr(34)
variables['haveWeEverUsedArrays'] = 0
variables['allVarsChars'] = ""
variables['allVarsInts'] = ""
variables['funcNames'] = "std::string|INT|STR|FLOAT|arrSplit|LoopParseFunc|InStr|Random|Sleep|input|print|FileRead|StrLower|FileAppend|FileDelete|StrLen|Asc|Abs|ACos|ASin|ATan|Ceil|Cos|Exp|Ln|Log|Round|Sin|Sqrt|Tan|SubStr|Trim|StrReplace|StringTrimLeft|StringTrimRight|StrSplit|Chr|Mod|Floor|getDataFromJSON|GetParams|BuildInVars|RegExReplace|RegExMatch|RunCMD|SetTimer|ExitApp|getDataFromAPI|SortLikeAHK"
#"std::string|INT|STR|FLOAT|arrSplit|LoopParseFunc|InStr|Random|Sleep|input|print|FileRead|FileAppend|FileDelete|StrLen|Asc|Abs|ACos|ATan|Ceil|Cos|Exp|Ln|Log|Round|Sin|Sqrt|Tan|SubStr|Trim|StrReplace|StringTrimLeft|StringTrimRight|RegExReplace|StrSplit|Chr|Mod|Floor|getDataFromJSON|GetParams|BuildInVars|RegExReplace|RegExMatch|RunCMD|SetTimer|getDataFromAPI|SortLikeAHK"
#"input|int|chr|str|InStr|SubStr|Trim|StrReplace|StringTrimLeft|StringTrimRight|StrLower|RegExReplace|StrSplit|Chr|Mod|FileRead|FileAppend|FileDelete|GetParams|RunCMD|SortLikeAHK|BuildInVars|Floor|ExitApp|SetTimer|Abs|ACos|ASin|ATan|Ceil|Cos|Exp|Ln|Log|Round|Sin|Sqrt|Tan|RegExMatch|StrLen|Asc|getDataFromAPI|getDataFromJSON|float"
# func
items = LoopParseFunc(variables['code'], "\n", "\r")
for A_Index17, A_LoopField17 in enumerate(items, start=1):
    variables['A_Index17'] = A_Index17
    variables['A_LoopField17'] = A_LoopField17
    if (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 5)== "func "):
        variables['funcName123'] = StringTrimLeft(variables['A_LoopField17'], 5)
        variables['funcName123'] = Trim(StrSplit(variables['funcName123'] , "(" , 1))
        variables['funcName123'] = Trim(StrSplit(variables['funcName123'] , " " , 2))
        variables['funcNames'] += "|" + variables['funcName123']
variables['varAssignmentType'] = "="
variables['timer_thread'] = 0
variables['cppCode'] = ""
items = LoopParseFunc(variables['code'], "\n", "\r")
for A_Index18, A_LoopField18 in enumerate(items, start=1):
    variables['A_Index18'] = A_Index18
    variables['A_LoopField18'] = A_LoopField18
    variables['lineDone'] = 0
    if (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 10)== "msgbox, % "):
        variables['msgboxCode'] = StringTrimLeft(variables['A_LoopField18'], 10)
        variables['msgboxCode'] = varTranspiler(variables['msgboxCode'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['cppCode'] += "print(" + variables['msgboxCode'] + ");" + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 8)== "msgbox, "):
        variables['msgboxCode'] = StringTrimLeft(variables['A_LoopField18'], 8)
        variables['cppCode'] += "print(std::string(" + Chr(34) + variables['msgboxCode'] + Chr(34) + "));" + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 1)== ";"):
        variables['str1234'] = StringTrimLeft(variables['A_LoopField18'], 1)
        variables['cppCode'] += "//" + variables['str1234'] + "\n"
        variables['lineDone'] = 1
    elif (SubStr(variables['A_LoopField18'] , -1)== "++"):
        variables['str123'] = Trim(variables['A_LoopField18'])
        variables['str123'] = StringTrimRight(variables['str123'], 2)
        variables['out'] = variables['str123'] + "++;"
        variables['cppCode'] += variables['out'] + "\n"
        variables['lineDone'] = 1
    elif (SubStr(variables['A_LoopField18'] , -1)== "--"):
        variables['str123'] = Trim(variables['A_LoopField18'])
        variables['str123'] = StringTrimRight(variables['str123'], 2)
        variables['out'] = variables['str123'] + "--;"
        variables['cppCode'] += variables['out'] + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 6)== "sort, "):
        variables['str1'] = StringTrimLeft(variables['A_LoopField18'], 6)
        variables['str1'] = Trim(variables['str1'])
        variables['weHaveAcommaFixSortCommand'] = 0
        if (SubStr(variables['str1'] , 0)== Chr(44)):
            #MsgBox, comma YES
            variables['str1'] = StringTrimRight(variables['str1'], 1)
            variables['weHaveAcommaFixSortCommand'] = 1
        else:
            #MsgBox, comma NO
            variables['gg'] = 0
        variables['s'] = StrSplit(variables['str1'] , "," , 1)
        variables['out1'] = Trim(variables['s'])
        variables['s'] = StrSplit(variables['str1'] , "," , 2)
        variables['out2'] = Trim(variables['s'])
        if (variables['weHaveAcommaFixSortCommand'] == 1):
            variables['out2'] = variables['out2'] + Chr(44)
        variables['var1'] = variables['out1'] + " = SortLikeAHK(" + variables['out1'] + ", " + Chr(34) + variables['out2'] + Chr(34) + ");"
        variables['lineDone'] = 1
        variables['cppCode'] += variables['var1'] + "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 10)== "settimer, "):
        variables['str1'] = StringTrimLeft(variables['A_LoopField18'], 10)
        variables['str2'] = Trim(StrSplit(variables['str1'] , "," , 1))
        variables['str3'] = Trim(StrSplit(variables['str1'] , "," , 2))
        if (variables['str3'] == ""):
            variables['str3'] = Chr(34) + "10" + Chr(34)
        else:
            if (StrLower(variables['str3'])== "on"):
                variables['str3'] = Chr(34) + "On" + Chr(34)
            elif (StrLower(variables['str3'])== "off"):
                variables['str3'] = Chr(34) + "Off" + Chr(34)
            else:
                if (RegExMatch(variables['str3'] , "^\\d+$")):
                    variables['str3'] = Chr(34) + variables['str3'] + Chr(34)
                else:
                    variables['str3'] = "STR(" + variables['str3'] + ")"
        variables['out1'] = "SetTimer(" + variables['str2'] + ", " + variables['str3'] + ");"
        variables['lineDone'] = 1
        variables['cppCode'] += variables['out1'] + "\n"
    elif (StrLower(variables['A_LoopField18'])== "settimers"):
        variables['lineDone'] = 1
        variables['timer_thread'] += 1
        variables['cppCode'] += "std::thread timer_thread" + str(variables['timer_thread']) + "(TimerManager);\n"
    elif (StrLower(variables['A_LoopField18'])== "starttimers"):
        variables['lineDone'] = 1
        variables['cppCode'] += "timer_thread" + str(variables['timer_thread']) + ".join(); // Wait for TimerManager to finish\nshould_exit = false; // Reset the exit flag for the new TimerManager thread\n"
    elif (Trim(StrLower(variables['A_LoopField18']))== "exitapp"):
        variables['lineDone'] = 1
        variables['cppCode'] += "ExitApp();" + "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 7)== "gosub, "):
        #MsgBox, % A_LoopField18
        variables['sstr1'] = variables['A_LoopField18']
        variables['s'] = StrSplit(variables['sstr1'] , "," , 2)
        variables['out1'] = variables['s']
        variables['out1'] = Trim(variables['out1'])
        variables['out2'] = variables['out1'] + "();"
        #MsgBox, % out2
        variables['lineDone'] = 1
        variables['cppCode'] += variables['out2'] + "\n"
    elif (variables['A_LoopField18'] == "Return"):
        variables['cppCode'] += "}" + "\n"
        variables['lineDone'] = 1
    elif (RegExReplace(variables['A_LoopField18'] , "^\\w+:$" , "") != variables['A_LoopField18'])and(Trim(SubStr(variables['A_LoopField18'] , 0))== ":")and(variables['lineDone']  != 1)and(variables['A_LoopField18']  != "main:"):
        #MsgBox, % A_LoopField18
        variables['out1'] = variables['A_LoopField18']
        variables['out1'] = Trim(variables['out1'])
        variables['out1'] = StringTrimRight(variables['out1'], 1)
        variables['lineDone'] = 1
        variables['cppCode'] += "void " + variables['out1'] + "()\n{\n"
        #MsgBox, % out1
        #~ MsgBox, % see
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 10)== "fileread, "):
        variables['filereadCommand'] = StringTrimLeft(variables['A_LoopField18'], 10)
        variables['filereadCommand1varname'] = StrSplit(variables['filereadCommand'] , ", " , 1)
        variables['filereadCommand2path'] = StrSplit(variables['filereadCommand'] , ", " , 2)
        variables['filereadCommand2path'] = StrReplace(variables['filereadCommand2path'] , "\\" , "\\\\")
        if ( not (InStr(variables['filereadCommand2path'] , "%"))):
            variables['filereadCommand2path'] = Trim(transpileLowVariables(variables['filereadCommand2path']))
        else:
            variables['filereadCommand2path'] = StrReplace(variables['filereadCommand2path'] , "%" , "")
        variables['cppCode'] += variables['filereadCommand1varname'] + " = FileRead(" + variables['filereadCommand2path'] + ");\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 12)== "fileappend, "):
        variables['fileAppendCommand'] = StringTrimLeft(variables['A_LoopField18'], 12)
        variables['fileAppendCommand1varname'] = StrSplit(variables['fileAppendCommand'] , ", " , 1)
        variables['fileAppendCommand2path'] = StrSplit(variables['fileAppendCommand'] , ", " , 2)
        variables['fileAppendCommand2path'] = StrReplace(variables['fileAppendCommand2path'] , "\\" , "\\\\")
        if ( not (InStr(variables['fileAppendCommand2path'] , "%"))):
            variables['fileAppendCommand2path'] = Trim(transpileLowVariables(variables['fileAppendCommand2path']))
        else:
            variables['fileAppendCommand2path'] = StrReplace(variables['fileAppendCommand2path'] , "%" , "")
        variables['fileAppendCommand1varname'] = StrReplace(variables['fileAppendCommand1varname'] , "%" , "")
        variables['cppCode'] += "FileAppend(" + variables['fileAppendCommand1varname'] + ", " + variables['fileAppendCommand2path'] + ");\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 12)== "filedelete, "):
        variables['fileDeleteCommand'] = StringTrimLeft(variables['A_LoopField18'], 12)
        variables['fileDeleteCommand2path'] = StrSplit(variables['fileDeleteCommand'] , ", " , 1)
        variables['fileDeleteCommand2path'] = StrReplace(variables['fileDeleteCommand2path'] , "\\" , "\\\\")
        if ( not (InStr(variables['fileDeleteCommand2path'] , "%"))):
            variables['fileDeleteCommand2path'] = Trim(transpileLowVariables(variables['fileDeleteCommand2path']))
        else:
            variables['fileDeleteCommand2path'] = StrReplace(variables['fileDeleteCommand2path'] , "%" , "")
        variables['cppCode'] += "FileDelete(" + variables['fileDeleteCommand2path'] + ");\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 17)== StrLower("StringTrimRight, ")):
        variables['varr1'] = StrSplit(variables['A_LoopField18'] , "," , 2)
        variables['varr2'] = StrSplit(variables['A_LoopField18'] , "," , 3)
        variables['varr3'] = StrSplit(variables['A_LoopField18'] , "," , 4)
        variables['outt1'] = Trim(varTranspiler(variables['varr1'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts']))
        variables['outt2'] = Trim(varTranspiler(variables['varr2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts']))
        variables['outt3'] = Trim(varTranspiler(variables['varr3'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts']))
        variables['out'] = variables['outt1'] + " = " + "StringTrimRight(" + variables['outt2'] + ", " + variables['outt3'] + ");"
        variables['cppCode'] += variables['out'] + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 8)== StrLower("Random, ")):
        variables['varr1'] = StrSplit(variables['A_LoopField18'] , "," , 2)
        variables['varr2'] = StrSplit(variables['A_LoopField18'] , "," , 3)
        variables['varr3'] = StrSplit(variables['A_LoopField18'] , "," , 4)
        variables['varr1'] = StrReplace(variables['varr1'] , "%" , "")
        variables['varr2'] = StrReplace(variables['varr2'] , "%" , "")
        variables['varr3'] = StrReplace(variables['varr3'] , "%" , "")
        variables['varr1'] = "int " + variables['varr1']
        variables['varr1'] = StrReplace(variables['varr1'] , "  " , " ")
        variables['outt2'] = Trim(varTranspiler(variables['varr2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts']))
        variables['outt3'] = Trim(varTranspiler(variables['varr3'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts']))
        variables['out'] = variables['varr1'] + " = " + "Random(" + variables['outt2'] + ", " + variables['outt3'] + ");"
        variables['cppCode'] += variables['out'] + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 7)== StrLower("Sleep, ")):
        variables['varr1'] = StrSplit(variables['A_LoopField18'] , "," , 2)
        variables['varr1'] = StrReplace(variables['varr1'] , "%" , "")
        variables['varr1'] = StrReplace(variables['varr1'] , "  " , " ")
        variables['out'] = "Sleep(" + variables['varr1'] + ");"
        variables['cppCode'] += variables['out'] + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 16)== StrLower("StringTrimLeft, ")):
        variables['varr1'] = StrSplit(variables['A_LoopField18'] , "," , 2)
        variables['varr2'] = StrSplit(variables['A_LoopField18'] , "," , 3)
        variables['varr3'] = StrSplit(variables['A_LoopField18'] , "," , 4)
        variables['outt1'] = Trim(varTranspiler(variables['varr1'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts']))
        variables['outt2'] = Trim(varTranspiler(variables['varr2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts']))
        variables['outt3'] = Trim(varTranspiler(variables['varr3'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts']))
        variables['out'] = variables['outt1'] + " = " + "StringTrimLeft(" + variables['outt2'] + ", " + variables['outt3'] + ");"
        variables['cppCode'] += variables['out'] + "\n"
        variables['lineDone'] = 1
    elif (variables['A_LoopField18'] == "main:"):
        variables['theMainFuncDec'] = 1
        variables['cppCode'] += "\nint main(int argc, char* argv[])\n{\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 5)== "func "):
        variables['funcName123'] = StringTrimLeft(variables['A_LoopField18'], 5)
        variables['removeNextCurlyBraceCpp'] = 1
        variables['funcName123'] = StrReplace(variables['funcName123'] , " str " , " std::string ")
        variables['funcName123'] = StrReplace(variables['funcName123'] , "str " , "std::string ")
        variables['funcName123'] = StrReplace(variables['funcName123'] , "(str " , "(std::string ")
        variables['cppCode'] += variables['funcName123'] + "\n{\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 4)== "str "):
        variables['strVar'] = StringTrimLeft(variables['A_LoopField18'], 4)
        variables['strVar'] = Trim(variables['strVar'])
        variables['declareAvarNOvalue'] = 0
        if (InStr(variables['strVar'] , " := ")):
            variables['varAssignmentType'] = "="
        elif (InStr(variables['strVar'] , " += ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " .= ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " -= ")):
            variables['varAssignmentType'] = "-="
        elif (InStr(variables['strVar'] , " *= ")):
            variables['varAssignmentType'] = "*="
        elif (InStr(variables['strVar'] , " /= ")):
            variables['varAssignmentType'] = "/="
        else:
            variables['declareAvarNOvalue'] = 1
        if (variables['declareAvarNOvalue'] == 1):
            variables['nameOfVar1'] = Trim(StrSplit(variables['strVar'] , " " , 1))
            variables['nameOfVarSplit'] = StrSplit(variables['strVar'] , " " , 2)
            variables['nameOfVar2'] = Trim(StrSplit(variables['strVar'] , str(variables['nameOfVarSplit']), 2))
            variables['nameOfVar2'] = varTranspiler(variables['nameOfVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            variables['cppCode'] += "std::string " + variables['nameOfVar1'] + Chr(59) + "\n"
        else:
            variables['nameOfVar1'] = Trim(StrSplit(variables['strVar'] , " " , 1))
            variables['nameOfVarSplit'] = StrSplit(variables['strVar'] , " " , 2)
            variables['nameOfVar2'] = Trim(StrSplit(variables['strVar'] , str(variables['nameOfVarSplit']), 2))
            variables['nameOfVar2'] = varTranspiler(variables['nameOfVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            variables['cppCode'] += "std::string " + variables['nameOfVar1'] + " " + variables['varAssignmentType'] + " " + variables['nameOfVar2'] + Chr(59) + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 8)== "arr str "):
        variables['strVar'] = StringTrimLeft(variables['A_LoopField18'], 8)
        variables['strVar'] = Trim(variables['strVar'])
        variables['haveWeEverUsedArrays'] = 1
        variables['declareAvarNOvalue'] = 0
        if (InStr(variables['strVar'] , " := ")):
            variables['varAssignmentType'] = "="
        elif (InStr(variables['strVar'] , " += ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " .= ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " -= ")):
            variables['varAssignmentType'] = "-="
        elif (InStr(variables['strVar'] , " *= ")):
            variables['varAssignmentType'] = "*="
        elif (InStr(variables['strVar'] , " /= ")):
            variables['varAssignmentType'] = "/="
        else:
            variables['declareAvarNOvalue'] = 1
        # defalut type
        variables['arrType'] = "std::string"
        if (variables['declareAvarNOvalue'] == 1):
            variables['nameOfVar1'] = Trim(StrSplit(variables['strVar'] , " " , 1))
            variables['cppCode'] += "OneIndexedArray<" + variables['arrType'] + "> " + variables['nameOfVar1'] + Chr(59) + "\n"
        else:
            variables['nameOfVar1'] = Trim(StrSplit(variables['strVar'] , " " , 1))
            variables['nameOfVarSplit'] = StrSplit(variables['strVar'] , " " , 2)
            variables['nameOfVar2'] = Trim(StrSplit(variables['strVar'] , str(variables['nameOfVarSplit']), 2))
            variables['nameOfVar222223'] = variables['nameOfVar2']
            variables['nameOfVar2'] = varTranspiler(variables['nameOfVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            if (variables['varAssignmentType'] == "+="):
                variables['cppCode'] += variables['nameOfVar1'] + ".add(" + variables['nameOfVar222223'] + ")" + Chr(59) + "\n"
            else:
                variables['cppCode'] += "OneIndexedArray<" + variables['arrType'] + "> " + variables['nameOfVar1'] + " " + variables['varAssignmentType'] + " " + variables['nameOfVar2'] + Chr(59) + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 8)== "arr int "):
        variables['strVar'] = StringTrimLeft(variables['A_LoopField18'], 8)
        variables['strVar'] = Trim(variables['strVar'])
        variables['haveWeEverUsedArrays'] = 1
        variables['declareAvarNOvalue'] = 0
        if (InStr(variables['strVar'] , " := ")):
            variables['varAssignmentType'] = "="
        elif (InStr(variables['strVar'] , " += ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " .= ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " -= ")):
            variables['varAssignmentType'] = "-="
        elif (InStr(variables['strVar'] , " *= ")):
            variables['varAssignmentType'] = "*="
        elif (InStr(variables['strVar'] , " /= ")):
            variables['varAssignmentType'] = "/="
        else:
            variables['declareAvarNOvalue'] = 1
        # defalut type
        variables['arrType'] = "int"
        if (variables['declareAvarNOvalue'] == 1):
            variables['nameOfVar1'] = Trim(StrSplit(variables['strVar'] , " " , 1))
            variables['cppCode'] += "OneIndexedArray<" + variables['arrType'] + "> " + variables['nameOfVar1'] + Chr(59) + "\n"
        else:
            variables['nameOfVar1'] = Trim(StrSplit(variables['strVar'] , " " , 1))
            variables['nameOfVarSplit'] = StrSplit(variables['strVar'] , " " , 2)
            variables['nameOfVar2'] = Trim(StrSplit(variables['strVar'] , str(variables['nameOfVarSplit']), 2))
            variables['nameOfVar222223'] = variables['nameOfVar2']
            variables['nameOfVar2'] = varTranspiler(variables['nameOfVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            if (variables['varAssignmentType'] == "+="):
                variables['cppCode'] += variables['nameOfVar1'] + ".add(" + variables['nameOfVar222223'] + ")" + Chr(59) + "\n"
            else:
                variables['cppCode'] += "OneIndexedArray<" + variables['arrType'] + "> " + variables['nameOfVar1'] + " " + variables['varAssignmentType'] + " " + variables['nameOfVar2'] + Chr(59) + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 10)== "arr float "):
        variables['strVar'] = StringTrimLeft(variables['A_LoopField18'], 10)
        variables['strVar'] = Trim(variables['strVar'])
        variables['haveWeEverUsedArrays'] = 1
        variables['declareAvarNOvalue'] = 0
        if (InStr(variables['strVar'] , " := ")):
            variables['varAssignmentType'] = "="
        elif (InStr(variables['strVar'] , " += ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " .= ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " -= ")):
            variables['varAssignmentType'] = "-="
        elif (InStr(variables['strVar'] , " *= ")):
            variables['varAssignmentType'] = "*="
        elif (InStr(variables['strVar'] , " /= ")):
            variables['varAssignmentType'] = "/="
        else:
            variables['declareAvarNOvalue'] = 1
        # defalut type
        variables['arrType'] = "float"
        if (variables['declareAvarNOvalue'] == 1):
            variables['nameOfVar1'] = Trim(StrSplit(variables['strVar'] , " " , 1))
            variables['cppCode'] += "OneIndexedArray<" + variables['arrType'] + "> " + variables['nameOfVar1'] + Chr(59) + "\n"
        else:
            variables['nameOfVar1'] = Trim(StrSplit(variables['strVar'] , " " , 1))
            variables['nameOfVarSplit'] = StrSplit(variables['strVar'] , " " , 2)
            variables['nameOfVar2'] = Trim(StrSplit(variables['strVar'] , str(variables['nameOfVarSplit']), 2))
            variables['nameOfVar222223'] = variables['nameOfVar2']
            variables['nameOfVar2'] = varTranspiler(variables['nameOfVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            if (variables['varAssignmentType'] == "+="):
                variables['cppCode'] += variables['nameOfVar1'] + ".add(" + variables['nameOfVar222223'] + ")" + Chr(59) + "\n"
            else:
                variables['cppCode'] += "OneIndexedArray<" + variables['arrType'] + "> " + variables['nameOfVar1'] + " " + variables['varAssignmentType'] + " " + variables['nameOfVar2'] + Chr(59) + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 4)== "arr "):
        variables['strVar'] = StringTrimLeft(variables['A_LoopField18'], 4)
        variables['strVar'] = Trim(variables['strVar'])
        variables['haveWeEverUsedArrays'] = 1
        variables['declareAvarNOvalue'] = 0
        if (InStr(variables['strVar'] , " := ")):
            variables['varAssignmentType'] = "="
        elif (InStr(variables['strVar'] , " += ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " .= ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " -= ")):
            variables['varAssignmentType'] = "-="
        elif (InStr(variables['strVar'] , " *= ")):
            variables['varAssignmentType'] = "*="
        elif (InStr(variables['strVar'] , " /= ")):
            variables['varAssignmentType'] = "/="
        else:
            variables['declareAvarNOvalue'] = 1
        # defalut type
        variables['arrType'] = "std::string"
        if (variables['declareAvarNOvalue'] == 1):
            variables['nameOfVar1'] = Trim(StrSplit(variables['strVar'] , " " , 1))
            variables['cppCode'] += "OneIndexedArray<" + variables['arrType'] + "> " + variables['nameOfVar1'] + Chr(59) + "\n"
        else:
            variables['nameOfVar1'] = Trim(StrSplit(variables['strVar'] , " " , 1))
            variables['nameOfVarSplit'] = StrSplit(variables['strVar'] , " " , 2)
            variables['nameOfVar2'] = Trim(StrSplit(variables['strVar'] , str(variables['nameOfVarSplit']), 2))
            variables['nameOfVar222223'] = variables['nameOfVar2']
            variables['nameOfVar2'] = varTranspiler(variables['nameOfVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            if (variables['varAssignmentType'] == "+="):
                variables['cppCode'] += variables['nameOfVar1'] + ".add(" + variables['nameOfVar222223'] + ")" + Chr(59) + "\n"
            else:
                variables['cppCode'] += "OneIndexedArray<" + variables['arrType'] + "> " + variables['nameOfVar1'] + " " + variables['varAssignmentType'] + " " + variables['nameOfVar2'] + Chr(59) + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 1)== "["):
        variables['strVar'] = StringTrimLeft(variables['A_LoopField18'], 1)
        variables['strVar'] = Trim(variables['strVar'])
        variables['declareAvarNOvalue'] = 0
        if (InStr(variables['strVar'] , " := ")):
            variables['varAssignmentType'] = "="
        elif (InStr(variables['strVar'] , " += ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " .= ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " -= ")):
            variables['varAssignmentType'] = "-="
        elif (InStr(variables['strVar'] , " *= ")):
            variables['varAssignmentType'] = "*="
        elif (InStr(variables['strVar'] , " /= ")):
            variables['varAssignmentType'] = "/="
        else:
            variables['declareAvarNOvalue'] = 1
        if (variables['declareAvarNOvalue'] == 1):
            variables['nameOfVar1'] = Trim(StrSplit(variables['strVar'] , " " , 1))
            variables['nameOfVar1'] = StringTrimRight(variables['nameOfVar1'], 1)
            variables['nameOfVarSplit'] = StrSplit(variables['strVar'] , " " , 2)
            variables['nameOfVar2'] = Trim(StrSplit(variables['strVar'] , str(variables['nameOfVarSplit']), 2))
            variables['nameOfVar2'] = varTranspiler(variables['nameOfVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            variables['cppCode'] += "variables[" + Chr(34) + variables['nameOfVar1'] + Chr(34) + "]" + Chr(59) + "\n"
        else:
            variables['nameOfVar1'] = Trim(StrSplit(variables['strVar'] , " " , 1))
            variables['nameOfVar1'] = StringTrimRight(variables['nameOfVar1'], 1)
            variables['nameOfVarSplit'] = StrSplit(variables['strVar'] , " " , 2)
            variables['nameOfVar2'] = Trim(StrSplit(variables['strVar'] , str(variables['nameOfVarSplit']), 2))
            variables['nameOfVar2'] = varTranspiler(variables['nameOfVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            variables['cppCode'] += "variables[" + Chr(34) + variables['nameOfVar1'] + Chr(34) + "] " + variables['varAssignmentType'] + " " + variables['nameOfVar2'] + Chr(59) + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 5)== "char "):
        variables['varName123Temp'] = StringTrimLeft(variables['A_LoopField18'], 5)
        variables['varName'] = StrSplit(variables['varName123Temp'] , " " , 1)
        variables['lineDone'] = 1
        variables['strVar'] = StringTrimLeft(variables['A_LoopField18'], 5)
        variables['strVar'] = Trim(variables['strVar'])
        variables['declareAvarNOvalue'] = 0
        if (InStr(variables['strVar'] , " := ")):
            variables['varAssignmentType'] = "="
        elif (InStr(variables['strVar'] , " += ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " .= ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " -= ")):
            variables['varAssignmentType'] = "-="
        elif (InStr(variables['strVar'] , " *= ")):
            variables['varAssignmentType'] = "*="
        elif (InStr(variables['strVar'] , " /= ")):
            variables['varAssignmentType'] = "/="
        else:
            variables['declareAvarNOvalue'] = 1
        if (variables['declareAvarNOvalue'] == 1):
            variables['charVar1'] = Trim(StrSplit(variables['strVar'] , ":=" , 1))
            variables['didItFoundTheChar'] = 0
            variables['cppCode'] += "const char* " + variables['charVar1'] + Chr(59) + "\n"
        else:
            variables['charVar1'] = Trim(StrSplit(variables['strVar'] , ":=" , 1))
            variables['charVar2'] = Trim(StrSplit(variables['strVar'] , ":=" , 2))
            variables['didItFoundTheChar'] = 0
            variables['cppCode'] += "const char* " + variables['charVar1'] + " " + variables['varAssignmentType'] + " " + variables['charVar2'] + Chr(59) + "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 4)== "int ")or(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 5)== "int8 ")or(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 6)== "int16 ")or(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 6)== "int32 ")or(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 6)== "int64 "):
        variables['lineDone'] = 1
        if (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 5)== "int8 "):
            variables['varName123Temp'] = StringTrimLeft(variables['A_LoopField18'], 5)
        elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 4)== "int "):
            variables['varName123Temp'] = StringTrimLeft(variables['A_LoopField18'], 4)
        else:
            variables['varName123Temp'] = StringTrimLeft(variables['A_LoopField18'], 6)
        variables['intType'] = Trim(StrSplit(variables['A_LoopField18'] , " " , 1)) + "_t"
        variables['varName'] = StrSplit(variables['varName123Temp'] , " " , 1)
        variables['allVarsInts'] += variables['varName'] + "\n"
        if (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 5)== "int8 "):
            variables['strVar'] = StringTrimLeft(variables['A_LoopField18'], 5)
        elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 4)== "int "):
            variables['strVar'] = StringTrimLeft(variables['A_LoopField18'], 4)
        else:
            variables['strVar'] = StringTrimLeft(variables['A_LoopField18'], 6)
        variables['strVar'] = Trim(variables['strVar'])
        variables['declareAvarNOvalue'] = 0
        if (InStr(variables['strVar'] , " := ")):
            variables['varAssignmentType'] = "="
        elif (InStr(variables['strVar'] , " += ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " .= ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " -= ")):
            variables['varAssignmentType'] = "-="
        elif (InStr(variables['strVar'] , " *= ")):
            variables['varAssignmentType'] = "*="
        elif (InStr(variables['strVar'] , " /= ")):
            variables['varAssignmentType'] = "/="
        else:
            variables['declareAvarNOvalue'] = 1
        if (variables['declareAvarNOvalue'] == 1):
            variables['charVar1'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentType'] , 1))
            variables['charVar2'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentType'] , 2))
            variables['charVar1'] = StrSplit(variables['charVar1'] , " " , 1)
            variables['charVar2'] = varTranspiler(variables['charVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            #MsgBox, % intType
            if (variables['intType'] == "int_t"):
                variables['intType'] = "int"
            if (variables['intType'] == "int64_t"):
                variables['intType'] = "long long"
            variables['cppCode'] += variables['intType'] + " " + variables['charVar1'] + Chr(59) + "\n"
        else:
            variables['charVar1'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentType'] , 1))
            variables['charVar2'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentType'] , 2))
            variables['charVar1'] = StrSplit(variables['charVar1'] , " " , 1)
            variables['charVar2'] = varTranspiler(variables['charVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            #MsgBox, % intType
            if (variables['intType'] == "int_t"):
                variables['intType'] = "int"
            if (variables['intType'] == "int64_t"):
                variables['intType'] = "long long"
            variables['cppCode'] += variables['intType'] + " " + variables['charVar1'] + " " + variables['varAssignmentType'] + " " + variables['charVar2'] + Chr(59) + "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 6)== "float "):
        variables['lineDone'] = 1
        variables['varName123Temp'] = StringTrimLeft(variables['A_LoopField18'], 6)
        variables['varName'] = StrSplit(variables['varName123Temp'] , " " , 1)
        variables['strVar'] = StringTrimLeft(variables['A_LoopField18'], 6)
        variables['strVar'] = Trim(variables['strVar'])
        variables['declareAvarNOvalue'] = 0
        if (InStr(variables['strVar'] , " := ")):
            variables['varAssignmentType'] = "="
        elif (InStr(variables['strVar'] , " += ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " .= ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " -= ")):
            variables['varAssignmentType'] = "-="
        elif (InStr(variables['strVar'] , " *= ")):
            variables['varAssignmentType'] = "*="
        elif (InStr(variables['strVar'] , " /= ")):
            variables['varAssignmentType'] = "/="
        else:
            variables['declareAvarNOvalue'] = 1
        if (variables['declareAvarNOvalue'] == 1):
            variables['charVar1'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentType'] , 1))
            variables['charVar2'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentType'] , 2))
            variables['charVar1'] = StrSplit(variables['charVar1'] , " " , 1)
            variables['charVar2'] = varTranspiler(variables['charVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            #MsgBox, % intType
            variables['cppCode'] += "float" + " " + variables['charVar1'] + Chr(59) + "\n"
        else:
            variables['charVar1'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentType'] , 1))
            variables['charVar2'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentType'] , 2))
            variables['charVar1'] = StrSplit(variables['charVar1'] , " " , 1)
            variables['charVar2'] = varTranspiler(variables['charVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            #MsgBox, % intType
            variables['cppCode'] += "float" + " " + variables['charVar1'] + " " + variables['varAssignmentType'] + " " + variables['charVar2'] + Chr(59) + "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 5)== "bool "):
        variables['lineDone'] = 1
        variables['varName123Temp'] = StringTrimLeft(variables['A_LoopField18'], 5)
        variables['varName'] = StrSplit(variables['varName123Temp'] , " " , 1)
        variables['strVar'] = StringTrimLeft(variables['A_LoopField18'], 5)
        variables['strVar'] = Trim(variables['strVar'])
        variables['declareAvarNOvalue'] = 0
        if (InStr(variables['strVar'] , " := ")):
            variables['varAssignmentType'] = "="
        elif (InStr(variables['strVar'] , " += ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " .= ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " -= ")):
            variables['varAssignmentType'] = "-="
        elif (InStr(variables['strVar'] , " *= ")):
            variables['varAssignmentType'] = "*="
        elif (InStr(variables['strVar'] , " /= ")):
            variables['varAssignmentType'] = "/="
        else:
            variables['declareAvarNOvalue'] = 1
        if (variables['declareAvarNOvalue'] == 1):
            variables['charVar1'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentType'] , 1))
            variables['charVar2'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentType'] , 2))
            variables['charVar1'] = StrSplit(variables['charVar1'] , " " , 1)
            variables['charVar2'] = varTranspiler(variables['charVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            #MsgBox, % intType
            variables['cppCode'] += "bool" + " " + variables['charVar1'] + Chr(59) + "\n"
        else:
            variables['charVar1'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentType'] , 1))
            variables['charVar2'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentType'] , 2))
            variables['charVar1'] = StrSplit(variables['charVar1'] , " " , 1)
            variables['charVar2'] = varTranspiler(variables['charVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            #MsgBox, % intType
            variables['cppCode'] += "bool" + " " + variables['charVar1'] + " " + variables['varAssignmentType'] + " " + variables['charVar2'] + Chr(59) + "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 4)== "cat "):
        variables['lineDone'] = 1
        variables['strVar'] = StringTrimLeft(variables['A_LoopField18'], 4)
        variables['strVar'] = Trim(variables['strVar'])
        variables['declareAvarNOvalue'] = 0
        if (InStr(variables['strVar'] , " := ")):
            variables['varAssignmentType'] = "="
        elif (InStr(variables['strVar'] , " += ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " .= ")):
            variables['varAssignmentType'] = "+="
        elif (InStr(variables['strVar'] , " -= ")):
            variables['varAssignmentType'] = "-="
        elif (InStr(variables['strVar'] , " *= ")):
            variables['varAssignmentType'] = "*="
        elif (InStr(variables['strVar'] , " /= ")):
            variables['varAssignmentType'] = "/="
        else:
            variables['declareAvarNOvalue'] = 1
        if (variables['declareAvarNOvalue'] == 1):
            variables['nameOfVar1'] = Trim(StrSplit(variables['strVar'] , " " , 1))
            variables['nameOfVarSplit'] = StrSplit(variables['strVar'] , " " , 2)
            variables['nameOfVar2'] = Trim(StrSplit(variables['strVar'] , str(variables['nameOfVarSplit']), 2))
            variables['nameOfVar2'] = varTranspiler(variables['nameOfVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            variables['nameOfVar11'] = Trim(StrSplit(variables['nameOfVar1'] , "%" , 1))
            variables['nameOfVar12'] = Trim(StrSplit(variables['nameOfVar1'] , "%" , 2))
            if (SubStr(variables['nameOfVar12'] , 1 , 1)== "["):
                variables['nameOfVar12'] = StringTrimRight(variables['nameOfVar12'], 1)
                variables['nameOfVar12'] = StringTrimLeft(variables['nameOfVar12'], 1)
                variables['nameOfVar1'] = "variables[" + Chr(34) + variables['nameOfVar11'] + Chr(34) + " + std::string(variables[" + Chr(34) + variables['nameOfVar12'] + Chr(34) + "])]"
            else:
                variables['nameOfVar1'] = "variables[" + Chr(34) + variables['nameOfVar11'] + Chr(34) + " + STR(" + variables['nameOfVar12'] + ")]"
            variables['cppCode'] += variables['nameOfVar1'] + Chr(59) + "\n"
        else:
            variables['nameOfVar1'] = Trim(StrSplit(variables['strVar'] , " " , 1))
            variables['nameOfVarSplit'] = StrSplit(variables['strVar'] , " " , 2)
            variables['nameOfVar2'] = Trim(StrSplit(variables['strVar'] , str(variables['nameOfVarSplit']), 2))
            variables['nameOfVar2'] = varTranspiler(variables['nameOfVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            variables['nameOfVar11'] = Trim(StrSplit(variables['nameOfVar1'] , "%" , 1))
            variables['nameOfVar12'] = Trim(StrSplit(variables['nameOfVar1'] , "%" , 2))
            if (SubStr(variables['nameOfVar12'] , 1 , 1)== "["):
                variables['nameOfVar12'] = StringTrimRight(variables['nameOfVar12'], 1)
                variables['nameOfVar12'] = StringTrimLeft(variables['nameOfVar12'], 1)
                variables['nameOfVar1'] = "variables[" + Chr(34) + variables['nameOfVar11'] + Chr(34) + " + std::string(variables[" + Chr(34) + variables['nameOfVar12'] + Chr(34) + "])]"
            else:
                variables['nameOfVar1'] = "variables[" + Chr(34) + variables['nameOfVar11'] + Chr(34) + " + STR(" + variables['nameOfVar12'] + ")]"
            variables['cppCode'] += variables['nameOfVar1'] + " " + variables['varAssignmentType'] + " " + variables['nameOfVar2'] + Chr(59) + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 4)== StrLower(variables['CheckIFandElsesss1']))or(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 3)== StrLower(variables['CheckIFandElsesss2']))or(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 5)== StrLower(variables['CheckIFandElsesss3']))or(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 4)== StrLower(variables['CheckIFandElsesss4']))or(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 9)== StrLower(variables['CheckIFandElsesss5']))or(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 8)== StrLower(variables['CheckIFandElsesss6']))or(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 10)== StrLower(variables['CheckIFandElsesss7']))or(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 9)== StrLower(variables['CheckIFandElsesss8'])):
        variables['lineDone'] = 1
        if (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 4)== StrLower(variables['CheckIFandElsesss1'])):
            variables['CheckIFandElsesssNum'] = 4
            variables['CheckIFandElsesssNumNum'] = 1
        if (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 3)== StrLower(variables['CheckIFandElsesss2'])):
            variables['CheckIFandElsesssNum'] = 3
            variables['CheckIFandElsesssNumNum'] = 2
        if (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 5)== StrLower(variables['CheckIFandElsesss3'])):
            variables['CheckIFandElsesssNum'] = 5
            variables['CheckIFandElsesssNumNum'] = 3
        if (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 4)== StrLower(variables['CheckIFandElsesss4'])):
            variables['CheckIFandElsesssNum'] = 4
            variables['CheckIFandElsesssNumNum'] = 4
        if (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 9)== StrLower(variables['CheckIFandElsesss5'])):
            variables['CheckIFandElsesssNum'] = 9
            variables['CheckIFandElsesssNumNum'] = 5
        if (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 8)== StrLower(variables['CheckIFandElsesss6'])):
            variables['CheckIFandElsesssNum'] = 8
            variables['CheckIFandElsesssNumNum'] = 6
        if (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 10)== StrLower(variables['CheckIFandElsesss7'])):
            variables['CheckIFandElsesssNum'] = 10
            variables['CheckIFandElsesssNumNum'] = 7
        if (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 9)== StrLower(variables['CheckIFandElsesss8'])):
            variables['CheckIFandElsesssNum'] = 9
            variables['CheckIFandElsesssNumNum'] = 8
        variables['str123'] = StringTrimLeft(variables['A_LoopField18'], variables['CheckIFandElsesssNum'])
        variables['str123'] = StrReplace(variables['str123'] , "(" , " ( ")
        variables['str123'] = StrReplace(variables['str123'] , ")" , " ) ")
        variables['str123'] = StrReplace(variables['str123'] , "!" , " ! ")
        variables['str123'] = variables[f'CheckIFandElsesss{variables["CheckIFandElsesssNumNum"]}'] + Chr(32) + varTranspiler(variables['str123'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['str123'] = StrReplace(variables['str123'] , "( " , "(")
        variables['str123'] = StrReplace(variables['str123'] , " )" , ")")
        variables['str123'] = StrReplace(variables['str123'] , " ! " , "!")
        variables['str123'] = StrReplace(variables['str123'] , "std::string()" , "")
        variables['str123'] = StrReplace(variables['str123'] , "if " + Chr(40) + Chr(32), "if " + Chr(40))
        variables['str123'] = StrReplace(variables['str123'] , "!==" , "!=")
        variables['out123'] = variables['str123']
        variables['cppCode'] += variables['out123'] + "\n"
    elif (StrLower(variables['A_LoopField18'])== "loop"):
        # infinity loops
        variables['haveWeEverUsedAloop'] = 1
        variables['lineDone'] = 1
        variables['var1'] = "for (int A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " = 1;; A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + "++)"
        variables['nothing'] = ""
        variables['AindexcharLengthStr'] = variables['nothing'] + str(variables['AindexcharLength']) + variables['nothing']
        variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 1
        variables['pycodeLoopfixa'] += "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength']) + "\n"
        variables['pycodeLoopfixa1'] = "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength'])
        variables['AindexcharLength'] += 1
        variables['cppCode'] += variables['pycodeLoopfixa1'] + "\n" + variables['var1'] + "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 6)== "loop, ")and(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 8) != "loop, % ")and(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 7) != "loop % ")and(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 11) != StrLower("Loop, Parse")):
        variables['str123'] = variables['A_LoopField18']
        #MsgBox, % str123
        variables['out2'] = StringTrimLeft(variables['str123'], 6)
        #MsgBox % out2
        #MsgBox, % out2
        variables['out2'] = Trim(variables['out2'])
        variables['lineDone'] = 1
        variables['myVar'] = variables['out2']
        variables['lineYGI'] = varTranspiler(variables['myVar'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['line'] = variables['lineYGI']
        variables['haveWeEverUsedAloop'] = 1
        #MsgBox, % line
        variables['var1'] = "for (int A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " = 1; A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + "<= " + variables['line'] + "; ++A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + ")"
        variables['nothing'] = ""
        variables['AindexcharLengthStr'] = variables['nothing'] + str(variables['AindexcharLength']) + variables['nothing']
        variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 1
        variables['pycodeLoopfixa'] += "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength']) + "\n"
        variables['pycodeLoopfixa1'] = "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength'])
        variables['AindexcharLength'] += 1
        variables['cppCode'] += variables['pycodeLoopfixa1'] + "\n" + variables['var1'] + "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 8)== "loop, % "):
        variables['str123'] = variables['A_LoopField18']
        #MsgBox, % str123
        variables['lineDone'] = 1
        variables['out2'] = StringTrimLeft(variables['str123'], 8)
        #MsgBox % out2
        #MsgBox, % out2
        variables['out2'] = Trim(variables['out2'])
        variables['myVar'] = variables['out2']
        variables['lineYGI'] = varTranspiler(variables['myVar'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['line'] = variables['lineYGI']
        #MsgBox, % line
        variables['var1'] = "for (int A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " = 1; A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + "<= " + variables['line'] + "; ++A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + ")"
        variables['nothing'] = ""
        variables['AindexcharLengthStr'] = variables['nothing'] + str(variables['AindexcharLength']) + variables['nothing']
        variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 1
        variables['haveWeEverUsedAloop'] = 1
        variables['pycodeLoopfixa'] += "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength']) + "\n"
        variables['pycodeLoopfixa1'] = "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength'])
        variables['AindexcharLength'] += 1
        variables['cppCode'] += variables['pycodeLoopfixa1'] + "\n" + variables['var1'] + "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 13)== StrLower("Loop, Parse, ")):
        #std::vector<std::string> items = LoopParseFunc(variables["var1"], " ");
        variables['lineDone'] = 1
        variables['var1'] = variables['A_LoopField18']
        variables['var1'] = Trim(variables['var1'])
        variables['var1'] = StringTrimLeft(variables['var1'], 13)
        variables['line1'] = Trim(StrSplit(variables['var1'] , "," , 1))
        variables['line1'] = varTranspiler(variables['line1'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['line2'] = ""
        variables['line3'] = ""
        variables['itemsOut'] = ""
        variables['line2'] = Trim(StrSplit(variables['var1'] , "," , 2))
        variables['line3'] = Trim(StrSplit(variables['var1'] , "," , 3))
        if (InStr(variables['var1'] , Chr(96) + ",")):
            variables['line2'] = Chr(34) + "," + Chr(34)
            variables['itemsOut'] = "std::vector<std::string> items" + str(variables['AindexcharLength']) + " = LoopParseFunc(" + variables['line1'] + ", " + variables['line2'] + ");"
        else:
            if (variables['line2'] == "")and(variables['line3'] == ""):
                # nothing so only each char
                variables['itemsOut'] = "std::vector<std::string> items" + str(variables['AindexcharLength']) + " = LoopParseFunc(" + variables['line1'] + ");"
            if (variables['line2']  != "")and(variables['line3'] == ""):
                if (InStr(variables['line2'] , Chr(96))):
                    variables['line2'] = Chr(34) + variables['line2'] + Chr(34)
                variables['itemsOut'] = "std::vector<std::string> items" + str(variables['AindexcharLength']) + " = LoopParseFunc(" + variables['line1'] + ", " + variables['line2'] + ");"
            if (variables['line2']  != "")and(variables['line3']  != ""):
                if (InStr(variables['line2'] , Chr(96))):
                    variables['line2'] = Chr(34) + variables['line2'] + Chr(34)
                if (InStr(variables['line3'] , Chr(96))):
                    variables['line3'] = Chr(34) + variables['line3'] + Chr(34)
                variables['itemsOut'] = "std::vector<std::string> items" + str(variables['AindexcharLength']) + " = LoopParseFunc(" + variables['line1'] + ", " + variables['line2'] + ", " + variables['line3'] + ");"
            variables['itemsOut'] = StrReplace(variables['itemsOut'] , Chr(96), Chr(92))
        #for (size_t A_Index1 = 0; A_Index1 < items.size(); A_Index1++)
        variables['var1out'] = variables['itemsOut'] + "\n" + "for (size_t A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " = 1; A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " < items" + str(variables['AindexcharLength']) + ".size() + 1; A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + "++)"
        variables['nothing'] = ""
        variables['AindexcharLengthStr'] = variables['nothing'] + str(variables['AindexcharLength']) + variables['nothing']
        variables['theFixTextLoopLP'] = "std::string A" + Chr(95) + "LoopField" + str(variables['AindexcharLength']) + " = items" + str(variables['AindexcharLength']) + "[A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " - 1];"
        variables['pycodeAcurlyBraceAddSomeVrasFixLP'] = 1
        variables['haveWeEverUsedAloop'] = 1
        variables['pycodeLoopfixa'] += "lp|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength']) + "\n"
        variables['pycodeLoopfixa1'] = "lp|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength'])
        variables['AindexcharLength'] += 1
        variables['cppCode'] += variables['pycodeLoopfixa1'] + "\n" + variables['var1out'] + "\n"
        variables['lineDone'] = 1
    elif (StrLower(variables['A_LoopField18'])== "break"):
        variables['cppCode'] += variables['A_LoopField18'] + ";\n"
        variables['lineDone'] = 1
    elif (StrLower(variables['A_LoopField18'])== "continue"):
        variables['cppCode'] += variables['A_LoopField18'] + ";\n"
        variables['lineDone'] = 1
    elif (StrLower(variables['A_LoopField18'])== "return")or(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 7)== "return "):
        if (StrLower(variables['A_LoopField18'])== "return"):
            variables['cppCode'] += variables['A_LoopField18'] + ";\n"
            variables['lineDone'] = 1
        else:
            variables['varTranspiledReturn'] = StringTrimLeft(variables['A_LoopField18'], 7)
            variables['varTranspiledReturn'] = varTranspiler(variables['varTranspiledReturn'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            variables['cppCode'] += "return " + variables['varTranspiledReturn'] + ";\n"
            variables['lineDone'] = 1
    elif (InStr(variables['A_LoopField18'] , " := "))or(InStr(variables['A_LoopField18'] , " .= "))or(InStr(variables['A_LoopField18'] , " += "))or(InStr(variables['A_LoopField18'] , " -= "))or(InStr(variables['A_LoopField18'] , " *= "))or(InStr(variables['A_LoopField18'] , " /= "))and(variables['lineDone'] == 0):
        variables['lineDone'] = 1
        variables['strVar'] = variables['A_LoopField18']
        variables['strVar'] = Trim(variables['strVar'])
        if (InStr(variables['strVar'] , " := ")):
            variables['varAssignmentType'] = "="
        if (InStr(variables['strVar'] , " += ")):
            variables['varAssignmentType'] = "+="
        if (InStr(variables['strVar'] , " .= ")):
            variables['varAssignmentType'] = "+="
        if (InStr(variables['strVar'] , " -= ")):
            variables['varAssignmentType'] = "-="
        if (InStr(variables['strVar'] , " *= ")):
            variables['varAssignmentType'] = "*="
        if (InStr(variables['strVar'] , " /= ")):
            variables['varAssignmentType'] = "/="
        variables['nameOfVar1'] = Trim(StrSplit(variables['strVar'] , " " , 1))
        variables['nameOfVarSplit'] = StrSplit(variables['strVar'] , " " , 2)
        variables['nameOfVar2'] = Trim(StrSplit(variables['strVar'] , str(variables['nameOfVarSplit']), 2))
        variables['nameOfVar2'] = varTranspiler(variables['nameOfVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['cppCode'] += variables['nameOfVar1'] + " " + variables['varAssignmentType'] + " " + variables['nameOfVar2'] + Chr(59) + "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField18'])), 0)== Chr(41))and(variables['lineDone'] == 0):
        variables['str123'] = variables['A_LoopField18']
        variables['FuncNameWhatIsIt'] = StrSplit(variables['str123'] , "(" , 1)
        items = LoopParseFunc(variables['FuncNameWhatIsIt'])
        for A_Index19, A_LoopField19 in enumerate(items, start=1):
            variables['A_Index19'] = A_Index19
            variables['A_LoopField19'] = A_LoopField19
            variables['str123'] = StringTrimLeft(variables['str123'], 1)
        variables['outVarTransiled'] = varTranspiler(variables['str123'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['out'] = variables['FuncNameWhatIsIt'] + variables['outVarTransiled']
        variables['lineDone'] = 1
        variables['cppCode'] += variables['out'] + ";\n"
    else:
        # this is THE else
        if (variables['removeNextCurlyBraceCpp']  != 1):
            variables['removeNextCurlyBraceCpp'] = 0
            if (variables['skipLeftCuleyForFuncPLS']  != 1):
                if (SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 1)== Chr(125)):
                    variables['cppCode'] += Chr(125) + "\n"
                else:
                    if (variables['pycodeAcurlyBraceAddSomeVrasFixLP'] == 1)and(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 1)== Chr(123)):
                        variables['pycodeAcurlyBraceAddSomeVrasFixLP'] = 0
                        variables['cppCode'] += variables['A_LoopField18'] + "\n" + variables['theFixTextLoopLP'] + "\n"
                    else:
                        if (variables['pycodeAcurlyBraceAddSomeVrasFixNL'] == 1)and(SubStr(Trim(StrLower(variables['A_LoopField18'])), 1 , 1)== Chr(123)):
                            variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 0
                            variables['cppCode'] += variables['A_LoopField18'] + "\n" + "\n"
                        else:
                            variables['cppCode'] += variables['A_LoopField18'] + "\n"
            else:
                variables['skipLeftCuleyForFuncPLS'] = 0
        else:
            if (Trim(variables['A_LoopField18'])== "{")and(variables['removeNextCurlyBraceCpp'] == 1):
                variables['removeNextCurlyBraceCpp'] = 0
            else:
                variables['cppCode'] += variables['A_LoopField18'] + "\n"
variables['cppCode'] = StringTrimRight(variables['cppCode'], 1)
#s
if (variables['haveWeEverUsedAloop'] == 1):
    variables['pycodeLoopfixa'] = StringTrimRight(variables['pycodeLoopfixa'], 1)
    #OutputDebug, |%pycodeLoopfixa%|
    variables['AIndexLoopCurlyFix'] = 1
    items = LoopParseFunc(variables['pycodeLoopfixa'], "\n", "\r")
    for A_Index20, A_LoopField20 in enumerate(items, start=1):
        variables['A_Index20'] = A_Index20
        variables['A_LoopField20'] = A_LoopField20
        variables['str123'] = variables['A_LoopField20']
        variables['fixLoopLokingFor'] = variables['A_LoopField20']
        variables['fixLoopLokingForfound'] = 1
        variables['out1'] = StrSplit(variables['str123'] , "|" , 1)
        variables['out2'] = StrSplit(variables['str123'] , "|" , 3)
        #OutputDebug, |%out1%|
        #OutputDebug, |%out2%|
        variables['wasAtanyIfsElseAddAIndexLoopCurlyFix'] = 0
        if (variables['out1'] == "nl"):
            variables['inTarget'] = 0
            variables['insideBracket'] = 0
            variables['netsedCurly'] = 0
            variables['eldLoopNestedBADlol'] = 0
            variables['readyToEnd'] = 0
            variables['endBracketDOntPutThere'] = 0
            variables['dontSaveStr'] = 0
            variables['weAreDoneHereCurly'] = 0
            variables['DeleayOneCuzOfLoopParse'] = 0
            variables['fixLoopLokingForNum'] = 0
            variables['insdeAnestedLoopBAD'] = 0
            variables['foundTheTopLoop'] = 0
            variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] = ""
            items = LoopParseFunc(variables['cppCode'], "\n", "\r")
            for A_Index21, A_LoopField21 in enumerate(items, start=1):
                variables['A_Index21'] = A_Index21
                variables['A_LoopField21'] = A_LoopField21
                #MsgBox, dsfgsdefgesrdg1
                #MsgBox, |%A_LoopField21%|`n|%fixLoopLokingFor%|
                if (InStr(variables['A_LoopField21'] , variables['fixLoopLokingFor']))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['fixLoopLokingForNum'] = 1
                    #MsgBox, do we came here 1
                if (InStr(variables['A_LoopField21'] , "for "))and(variables['weAreDoneHereCurly']  != 1)and(variables['insdeAnestedLoopBAD']  != 1)and(variables['fixLoopLokingForNum'] == 1):
                    variables['s'] = StrSplit(variables['A_LoopField21'] , "A" + Chr(95) + "Index" , 2)
                    variables['out1z'] = variables['s']
                    variables['s'] = StrSplit(variables['out1z'] , " " , 1)
                    variables['out1z'] = Trim(variables['s'])
                    #MsgBox, % out1z
                    #MsgBox, do we came here 2
                    variables['fixLoopLokingForNum'] = 0
                    variables['foundTheTopLoop'] += 1
                    variables['inTarget'] = 1
                    #MsgBox, % A_LoopField21
                    variables['dontSaveStr'] = 1
                    variables['ALoopField'] = variables['A_LoopField21']
                    variables['DeleayOneCuzOfLoopParse'] = 1
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField'] + "\n"
                if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField21'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['insideBracket'] = 1
                if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField21'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['netsedCurly'] += 1
                if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField21'] , Chr(125)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['netsedCurly'] -= 1
                    variables['readyToEnd'] = 1
                if (InStr(variables['A_LoopField21'] , "for "))and(variables['insdeAnestedLoopBAD']  != 1)and(variables['foundTheTopLoop'] >= 2):
                    variables['insdeAnestedLoopBAD'] = 1
                    variables['insideBracket1'] = 0
                    variables['netsedCurly1'] = 0
                if (variables['inTarget'] == 1):
                    variables['foundTheTopLoop'] += 1
                if (variables['insdeAnestedLoopBAD'] == 1):
                    if (InStr(variables['A_LoopField21'] , Chr(123))):
                        variables['insideBracket1'] = 1
                    if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField21'] , Chr(123))):
                        variables['netsedCurly1'] += 1
                    if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField21'] , Chr(125))):
                        variables['netsedCurly1'] -= 1
                        variables['readyToEnd1'] = 1
                    if (InStr(variables['A_LoopField21'] , Chr(125)))and(variables['readyToEnd1'] == 1)and(variables['netsedCurly1'] == 0)and(variables['insideBracket'] == 1):
                        #MsgBox, % A_LoopField21
                        variables['eldLoopNestedBADlol'] = 1
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField21'] + "\n"
                if (variables['inTarget'] == 1)and(variables['dontSaveStr']  != 1)and(variables['fixLoopLokingForNum']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['ALoopField'] = variables['A_LoopField21']
                    # Replace "A_Index" with or without a following digit with "A_Index" + out1z
                    variables['ALoopField'] = RegExReplace(variables['ALoopField'] , "A" + Chr(95) + "Index(?:\\d+)?" , "A" + Chr(95) + "Index" + variables['out1z'])
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField'] + "\n"
                if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField21'] , Chr(125)))and(variables['readyToEnd'] == 1)and(variables['netsedCurly'] == 0)and(variables['weAreDoneHereCurly'] == 0)and(variables['dontSaveStr']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    #MsgBox, % A_LoopField21
                    variables['weAreDoneHereCurly'] = 1
                    variables['inTarget'] = 0
                    variables['endBracketDOntPutThere'] = 1
                variables['dontSaveStr'] = 0
                if (variables['inTarget']  != 1)and(variables['endBracketDOntPutThere']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField21'] + "\n"
                variables['endBracketDOntPutThere'] = 0
                if (variables['eldLoopNestedBADlol'] == 1):
                    variables['insdeAnestedLoopBAD'] = 0
            variables['strstysrstsytTRIMHELP'] = variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}']
            variables['strstysrstsytTRIMHELP'] = StringTrimRight(variables['strstysrstsytTRIMHELP'], 1)
            #MsgBox, % out4758686d86d86d86578991a%AIndexLoopCurlyFix%
            variables['cppCode'] = variables['strstysrstsytTRIMHELP']
            #MsgBox, % jsCode
            variables['wasAtanyIfsElseAddAIndexLoopCurlyFix'] = 1
        else:
            variables['inTarget'] = 0
            variables['insideBracket'] = 0
            variables['netsedCurly'] = 0
            variables['eldLoopNestedBADlol'] = 0
            variables['readyToEnd'] = 0
            variables['endBracketDOntPutThere'] = 0
            variables['dontSaveStr'] = 0
            variables['weAreDoneHereCurly'] = 0
            variables['DeleayOneCuzOfLoopParse'] = 0
            variables['fixLoopLokingForNum'] = 0
            variables['insdeAnestedLoopBAD'] = 0
            variables['foundTheTopLoop'] = 0
            variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] = ""
            items = LoopParseFunc(variables['cppCode'], "\n", "\r")
            for A_Index22, A_LoopField22 in enumerate(items, start=1):
                variables['A_Index22'] = A_Index22
                variables['A_LoopField22'] = A_LoopField22
                if (InStr(variables['A_LoopField22'] , variables['fixLoopLokingFor']))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['fixLoopLokingForNum'] = 1
                    #MsgBox, do we came here 3
                if (InStr(variables['A_LoopField22'] , "for "))and(variables['weAreDoneHereCurly']  != 1)and(variables['insdeAnestedLoopBAD']  != 1)and(variables['fixLoopLokingForNum'] == 1):
                    variables['s'] = StrSplit(variables['A_LoopField22'] , "A" + Chr(95) + "Index" , 2)
                    variables['out1z'] = variables['s']
                    variables['s'] = StrSplit(variables['out1z'] , " " , 1)
                    variables['out1z'] = Trim(variables['s'])
                    #MsgBox, % out1z
                    variables['fixLoopLokingForNum'] = 0
                    #MsgBox, do we came here 4
                    variables['foundTheTopLoop'] += 1
                    variables['inTarget'] = 1
                    #MsgBox, % A_LoopField22
                    variables['dontSaveStr'] = 1
                    variables['ALoopField'] = variables['A_LoopField22']
                    variables['DeleayOneCuzOfLoopParse'] = 1
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField'] + "\n"
                if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField22'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['insideBracket'] = 1
                if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField22'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['netsedCurly'] += 1
                if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField22'] , Chr(125)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['netsedCurly'] -= 1
                    variables['readyToEnd'] = 1
                if (InStr(variables['A_LoopField22'] , "for "))and(variables['insdeAnestedLoopBAD']  != 1)and(variables['foundTheTopLoop'] >= 2):
                    variables['insdeAnestedLoopBAD'] = 1
                    variables['insideBracket1'] = 0
                    variables['netsedCurly1'] = 0
                if (variables['inTarget'] == 1):
                    variables['foundTheTopLoop'] += 1
                if (variables['insdeAnestedLoopBAD'] == 1):
                    if (InStr(variables['A_LoopField22'] , Chr(123))):
                        variables['insideBracket1'] = 1
                    if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField22'] , Chr(123))):
                        variables['netsedCurly1'] += 1
                    if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField22'] , Chr(125))):
                        variables['netsedCurly1'] -= 1
                        variables['readyToEnd1'] = 1
                    if (InStr(variables['A_LoopField22'] , Chr(125)))and(variables['readyToEnd1'] == 1)and(variables['netsedCurly1'] == 0)and(variables['insideBracket'] == 1):
                        #MsgBox, % A_LoopField22
                        variables['eldLoopNestedBADlol'] = 1
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField22'] + "\n"
                if (variables['inTarget'] == 1)and(variables['dontSaveStr']  != 1)and(variables['fixLoopLokingForNum']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['ALoopField'] = variables['A_LoopField22']
                    # Replace "A_Index" with or without a following digit with "A_Index" + out1z
                    variables['ALoopField'] = RegExReplace(variables['ALoopField'] , "A" + Chr(95) + "Index(?:\\d+)?" , "A" + Chr(95) + "Index" + variables['out1z'])
                    # Replace "A_Index" with or without a following digit with "A_Index" + out1z
                    variables['ALoopField'] = RegExReplace(variables['ALoopField'] , "A" + Chr(95) + "LoopField(?:\\d+)?" , "A" + Chr(95) + "LoopField" + variables['out1z'])
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField'] + "\n"
                if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField22'] , Chr(125)))and(variables['readyToEnd'] == 1)and(variables['netsedCurly'] == 0)and(variables['weAreDoneHereCurly'] == 0)and(variables['dontSaveStr']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    #MsgBox, % A_LoopField22
                    variables['weAreDoneHereCurly'] = 1
                    variables['inTarget'] = 0
                    variables['endBracketDOntPutThere'] = 1
                variables['dontSaveStr'] = 0
                if (variables['inTarget']  != 1)and(variables['endBracketDOntPutThere']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField22'] + "\n"
                variables['endBracketDOntPutThere'] = 0
                if (variables['eldLoopNestedBADlol'] == 1):
                    variables['insdeAnestedLoopBAD'] = 0
            variables['strstysrstsytTRIMHELP'] = variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}']
            variables['strstysrstsytTRIMHELP'] = StringTrimRight(variables['strstysrstsytTRIMHELP'], 1)
            #MsgBox, % out4758686d86d86d86578991a%AIndexLoopCurlyFix%
            variables['cppCode'] = variables['strstysrstsytTRIMHELP']
            #MsgBox, % jsCode
            variables['wasAtanyIfsElseAddAIndexLoopCurlyFix'] = 1
        if (variables['wasAtanyIfsElseAddAIndexLoopCurlyFix'] == 1):
            variables['AIndexLoopCurlyFix'] += 1
            variables['wasAtanyIfsElseAddAIndexLoopCurlyFix'] = 0
    variables['out4758686d86dgt8r754444444'] = ""
    variables['hold'] = 0
    items = LoopParseFunc(variables['cppCode'], "\n", "\r")
    for A_Index23, A_LoopField23 in enumerate(items, start=1):
        variables['A_Index23'] = A_Index23
        variables['A_LoopField23'] = A_LoopField23
        variables['ignore'] = 0
        if (InStr(variables['A_LoopField23'] , "for ")):
            if (variables['hold'] == 1)and(variables['holdText'] == variables['A_LoopField23']):
                variables['ignore'] = 1
            else:
                variables['holdText'] = variables['A_LoopField23']
                variables['hold'] = 1
        if ( not (variables['ignore'])):
            variables['out4758686d86dgt8r754444444'] += variables['A_LoopField23'] + "\n"
    variables['out4758686d86dgt8r754444444'] = StringTrimRight(variables['out4758686d86dgt8r754444444'], 1)
    variables['cppCode'] = variables['out4758686d86dgt8r754444444']
variables['pyCodeOut1234565432'] = ""
items = LoopParseFunc(variables['cppCode'], "\n", "\r")
for A_Index24, A_LoopField24 in enumerate(items, start=1):
    variables['A_Index24'] = A_Index24
    variables['A_LoopField24'] = A_LoopField24
    variables['out'] = variables['A_LoopField24']
    if ( not (InStr(variables['out'] , "|itsaersdtgtgfergsdgfsegdfsedAA|"))):
        variables['pyCodeOut1234565432'] += variables['out'] + "\n"
variables['cppCode'] = StringTrimRight(variables['pyCodeOut1234565432'], 1)
variables['cppCodeOutOneLastFixFixFIX'] = ""
items = LoopParseFunc(variables['cppCode'], " ")
for A_Index25, A_LoopField25 in enumerate(items, start=1):
    variables['A_Index25'] = A_Index25
    variables['A_LoopField25'] = A_LoopField25
    variables['sstr1'] = variables['A_LoopField25']
    variables['sstr1'] = StrReplace(variables['sstr1'] , "A_TickCount" , "BuildInVars(" + Chr(34) + "A_TickCount" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "A_Now" , "BuildInVars(" + Chr(34) + "A_Now" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "A_YYYY" , "BuildInVars(" + Chr(34) + "A_YYYY" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "A_MMMM" , "BuildInVars(" + Chr(34) + "A_MMMM" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "A_MMM" , "BuildInVars(" + Chr(34) + "A_MMM" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "A_MM" , "BuildInVars(" + Chr(34) + "A_MM" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "A_DDDD" , "BuildInVars(" + Chr(34) + "A_DDDD" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "A_DDD" , "BuildInVars(" + Chr(34) + "A_DDD" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "A_DD" , "BuildInVars(" + Chr(34) + "A_DD" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "A_Hour" , "BuildInVars(" + Chr(34) + "A_Hour" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "A_Min" , "BuildInVars(" + Chr(34) + "A_Min" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "A_Sec" , "BuildInVars(" + Chr(34) + "A_Sec" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "A_Space" , "BuildInVars(" + Chr(34) + "A_Space" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "A_Tab" , "BuildInVars(" + Chr(34) + "A_Tab" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "BuildInVars(" + Chr(34) + "BuildInVars(" + Chr(34) + "A_DD" + Chr(34) + ")D" + Chr(34) + ")" , "BuildInVars(" + Chr(34) + "A_DDD" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "BuildInVars(" + Chr(34) + "BuildInVars(" + Chr(34) + "BuildInVars(" + Chr(34) + "A_DD" + Chr(34) + ")D" + Chr(34) + ")D" + Chr(34) + ")" , "BuildInVars(" + Chr(34) + "A_DDDD" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "BuildInVars(" + Chr(34) + "BuildInVars(" + Chr(34) + "A_DDD" + Chr(34) + ")D" + Chr(34) + ")" , "BuildInVars(" + Chr(34) + "A_DDDD" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "BuildInVars(" + Chr(34) + "BuildInVars(" + Chr(34) + "A_MM" + Chr(34) + ")M" + Chr(34) + ")" , "BuildInVars(" + Chr(34) + "A_MMM" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "BuildInVars(" + Chr(34) + "BuildInVars(" + Chr(34) + "BuildInVars(" + Chr(34) + "A_MM" + Chr(34) + ")M" + Chr(34) + ")M" + Chr(34) + ")" , "BuildInVars(" + Chr(34) + "A_MMMM" + Chr(34) + ")")
    variables['sstr1'] = StrReplace(variables['sstr1'] , "BuildInVars(" + Chr(34) + "BuildInVars(" + Chr(34) + "A_MMM" + Chr(34) + ")M" + Chr(34) + ")" , "BuildInVars(" + Chr(34) + "A_MMMM" + Chr(34) + ")")
    variables['cppCodeOutOneLastFixFixFIX'] += variables['sstr1'] + " "
variables['cppCode'] = StringTrimRight(variables['cppCodeOutOneLastFixFixFIX'], 1)
for A_Index26 in range(1, variables['theIdNumOfThe34'] + 1):
    variables['A_Index26'] = A_Index26
    variables['cppCode'] = StrReplace(variables['cppCode'] , "ihuiuuhuuhtheidFor--asas-theuhturtyphoutr-" + Chr(65) + Chr(65) + str(variables['A_Index26']) + Chr(65) + Chr(65), "std::string(" + variables[f'theIdNumOfThe34theVar{variables["A_Index26"]}'] + ")")
variables['cppCodeFixCharRemoveStd'] = ""
items = LoopParseFunc(variables['cppCode'], "\n", "\r")
for A_Index27, A_LoopField27 in enumerate(items, start=1):
    variables['A_Index27'] = A_Index27
    variables['A_LoopField27'] = A_LoopField27
    if (SubStr(Trim(StrLower(variables['A_LoopField27'])), 1 , 12)== "const char* "):
        variables['cppCodeFixCharRemoveStd123'] = variables['A_LoopField27']
        variables['cppCodeFixCharRemoveStd123'] = StrReplace(variables['cppCodeFixCharRemoveStd123'] , "std::string(" , "")
        variables['cppCodeFixCharRemoveStd123'] = StrReplace(variables['cppCodeFixCharRemoveStd123'] , ")" , "")
        variables['cppCodeFixCharRemoveStd'] += variables['cppCodeFixCharRemoveStd123'] + "\n"
    else:
        variables['cppCodeFixCharRemoveStd'] += variables['A_LoopField27'] + "\n"
variables['cppCode'] = StringTrimRight(variables['cppCodeFixCharRemoveStd'], 1)
if (variables['theMainFuncDec'] == 0):
    variables['upCode'] = "\nint main(int argc, char* argv[])\n{\n"
variables['uperCode'] = ""
variables['uperCodeLibs'] = ""
variables['uperCodeLibs'] += "#include <iostream>\n#include <sstream>\n#include <string>\n#include <cstdint>\n"
if (InStr(variables['cppCode'] , "variables[")):
    variables['uperCodeLibs'] += "\n#include <unordered_map>\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Define a map to store dynamic variables\n    std::unordered_map<std::string, std::string> variables;\n"
if (variables['haveWeEverUsedArrays'] == 1):
    variables['uperCodeLibs'] += "\n#include <vector>\n#include <string>\n#include <sstream>\n#include <stdexcept>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Forward declare OneIndexedArray template\ntemplate <typename T>\nclass OneIndexedArray;\n\n#define OneIndexedArray_DEFINED\n\n// Helper function to set the internal array's size as a string\ntemplate <typename T>\nvoid setInternalArraySize(T& element, size_t size) {\n    element = static_cast<T>(size);\n}\n\n// Specialization for std::string\ntemplate <>\nvoid setInternalArraySize<std::string>(std::string& element, size_t size) {\n    element = std::to_string(size);\n}\n\n// One-indexed dynamic array class\ntemplate <typename T>\nclass OneIndexedArray {\nprivate:\n    std::vector<T> internalArray;\n\npublic:\n    OneIndexedArray() {\n        internalArray.push_back(T{}); // Placeholder for element count\n    }\n\n    void add(const T& newElement) {\n        internalArray.push_back(newElement);\n        setInternalArraySize(internalArray[0], internalArray.size() - 1);\n    }\n\n    void setArray(const std::vector<T>& newArray) {\n        internalArray.resize(newArray.size() + 1);\n        std::copy(newArray.begin(), newArray.end(), internalArray.begin() + 1);\n        setInternalArraySize(internalArray[0], newArray.size());\n    }\n\n    T& operator[](size_t index) {\n        if (index >= internalArray.size()) {\n            internalArray.resize(index + 1);\n            setInternalArraySize(internalArray[0], internalArray.size() - 1);\n        }\n        return internalArray[index];\n    }\n\n    const T& operator[](size_t index) const {\n        if (index >= internalArray.size()) {\n            throw std::out_of_range(" + Chr(34) + "Index out of range" + Chr(34) + ");\n        }\n        return internalArray[index];\n    }\n\n    size_t size() const {\n        return static_cast<size_t>(internalArray.size() - 1);\n    }\n};\n\n// Function to split text into words based on a delimiter\nstd::vector<std::string> split(const std::string& text, const std::string& delimiter) {\n    std::vector<std::string> words;\n    std::istringstream stream(text);\n    std::string word;\n    while (std::getline(stream, word, delimiter[0])) { // assuming single character delimiter\n        words.push_back(word);\n    }\n    return words;\n}\n\n// Function to split text into a OneIndexedArray\nOneIndexedArray<std::string> arrSplit(const std::string& text, const std::string& delimiter) {\n    OneIndexedArray<std::string> array;\n    std::vector<std::string> words = split(text, delimiter);\n    array.setArray(words);\n    return array;\n}\n"
if (InStr(variables['cppCode'] , "INT("))or(InStr(variables['cppCode'] , "INT (")):
    variables['uperCodeLibs'] += "\n#include <string>\n#include <sstream>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Convert std::string to int\nint INT(const std::string& str) {\n    std::istringstream iss(str);\n    int value;\n    iss >> value;\n    return value;\n}\n"
if (InStr(variables['cppCode'] , "STR("))or(InStr(variables['cppCode'] , "STR (")):
    variables['uperCodeLibs'] += "\n#include <string>\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Convert various types to std::string\nstd::string STR(int value) {\n    return std::to_string(value);\n}\n\n// Convert various types to std::string\nstd::string STR(long long value) {\n    return std::to_string(value);\n}\n\nstd::string STR(float value) {\n    return std::to_string(value);\n}\n\nstd::string STR(double value) {\n    return std::to_string(value);\n}\n\nstd::string STR(size_t value) {\n    return std::to_string(value);\n}\n\nstd::string STR(bool value) {\n    return value ? " + Chr(34) + "1" + Chr(34) + " : " + Chr(34) + "0" + Chr(34) + ";\n}\n"
if (InStr(variables['cppCode'] , "FLOAT("))or(InStr(variables['cppCode'] , "FLOAT (")):
    variables['uperCodeLibs'] += "\n#include <string>\n#include <sstream>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Convert std::string to float\nfloat FLOAT(const std::string& str) {\n    std::istringstream iss(str);\n    float value;\n    iss >> value;\n    return value;\n}\n"
if (InStr(variables['cppCode'] , "InStr("))or(InStr(variables['cppCode'] , "InStr (")):
    variables['uperCodeLibs'] += "\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Function to check if needle exists in haystack (std::string overload)\nbool InStr(const std::string& haystack, const std::string& needle) {\n    return haystack.find(needle) != std::string::npos;\n}\n"
if (InStr(variables['cppCode'] , "Random("))or(InStr(variables['cppCode'] , "Random (")):
    variables['uperCodeLibs'] += "\n#include <cstdlib>\n#include <ctime>\n#include <random>\n"
    variables['uperCode'] = variables['uperCode'] + "\nint Random(int min, int max) {\n    // Create a random device to seed the generator\n    std::random_device rd;\n    \n    // Create a generator seeded with the random device\n    std::mt19937 gen(rd());\n    \n    // Define a distribution within the specified range\n    std::uniform_int_distribution<> dis(min, max);\n    \n    // Generate and return a random number within the specified range\n    return dis(gen);\n}\n"
if (InStr(variables['cppCode'] , "Sleep("))or(InStr(variables['cppCode'] , "Sleep (")):
    variables['uperCodeLibs'] += "\n#include <thread>\n#include <chrono>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Function to sleep for a specified number of milliseconds\nvoid Sleep(int milliseconds) {\n    std::this_thread::sleep_for(std::chrono::milliseconds(milliseconds));\n}\n\n"
if (InStr(variables['cppCode'] , "input("))or(InStr(variables['cppCode'] , "input (")):
    variables['uperCodeLibs'] += "\n#include <iostream>\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Function to get input from the user, similar to Python's input() function\nstd::string input(const std::string& prompt) {\n    std::string userInput;\n    std::cout << prompt; // Display the prompt to the user\n    std::getline(std::cin, userInput); // Get the entire line of input\n    return userInput;\n}\n\n"
if (InStr(variables['cppCode'] , "LoopParseFunc("))or(InStr(variables['cppCode'] , "LoopParseFunc (")):
    variables['uperCodeLibs'] += "\n#include <vector>\n#include <string>\n#include <regex>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Function to escape special characters for regex\nstd::string escapeRegex(const std::string& str) {\n    static const std::regex specialChars{R" + Chr(34) + "([-[" + Chr(92) + "]{}()*+?.," + Chr(92) + "^$|#" + Chr(92) + "s])" + Chr(34) + "};\n    return std::regex_replace(str, specialChars, R" + Chr(34) + "(" + Chr(92) + "$&)" + Chr(34) + ");\n}\n\n// Function to split a string based on delimiters\nstd::vector<std::string> LoopParseFunc(const std::string& var, const std::string& delimiter1 = " + Chr(34) + "" + Chr(34) + ", const std::string& delimiter2 = " + Chr(34) + "" + Chr(34) + ") {\n    std::vector<std::string> items;\n    if (delimiter1.empty() && delimiter2.empty()) {\n        // If no delimiters are provided, return a list of characters\n        for (char c : var) {\n            items.push_back(std::string(1, c));\n        }\n    } else {\n        // Escape delimiters for regex\n        std::string escapedDelimiters = escapeRegex(delimiter1 + delimiter2);\n        // Construct the regular expression pattern for splitting the string\n        std::string pattern = " + Chr(34) + "[" + Chr(34) + " + escapedDelimiters + " + Chr(34) + "]+" + Chr(34) + ";\n        std::regex regexPattern(pattern);\n        std::sregex_token_iterator iter(var.begin(), var.end(), regexPattern, -1);\n        std::sregex_token_iterator end;\n        while (iter != end) {\n            items.push_back(*iter++);\n        }\n    }\n    return items;\n}\n"
if (InStr(variables['cppCode'] , "print("))or(InStr(variables['cppCode'] , "print (")):
    variables['uperCodeLibs'] += "\n#include <iostream>\n#include <string>\n#include <type_traits>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Print function that converts all types to string if needed\ntemplate <typename T>\nvoid print(const T& value) {\n    if constexpr (std::is_same_v<T, std::string>) {\n        std::cout << value << std::endl;\n    } else if constexpr (std::is_same_v<T, int>) {\n        std::cout << std::to_string(value) << std::endl;\n    } else if constexpr (std::is_same_v<T, float>) {\n        std::cout << std::to_string(value) << std::endl;\n    } else if constexpr (std::is_same_v<T, double>) {\n        std::cout << std::to_string(value) << std::endl;\n    } else if constexpr (std::is_same_v<T, size_t>) {\n        std::cout << std::to_string(value) << std::endl;\n    } else if constexpr (std::is_same_v<T, bool>) {\n        std::cout << (value ? " + Chr(34) + "1" + Chr(34) + " : " + Chr(34) + "0" + Chr(34) + ") << std::endl;\n    } \n    #ifdef OneIndexedArray_DEFINED\n    else if constexpr (std::is_base_of_v<OneIndexedArray<std::string>, T>) {\n        for (size_t i = 1; i <= value.size(); ++i) {\n            std::cout << value[i] << std::endl;\n        }\n    } else if constexpr (std::is_base_of_v<OneIndexedArray<int>, T>) {\n        for (size_t i = 1; i <= value.size(); ++i) {\n            std::cout << std::to_string(value[i]) << std::endl;\n        }\n    } else if constexpr (std::is_base_of_v<OneIndexedArray<float>, T>) {\n        for (size_t i = 1; i <= value.size(); ++i) {\n            std::cout << std::to_string(value[i]) << std::endl;\n        }\n    } else if constexpr (std::is_base_of_v<OneIndexedArray<double>, T>) {\n        for (size_t i = 1; i <= value.size(); ++i) {\n            std::cout << std::to_string(value[i]) << std::endl;\n        }\n    }\n    #endif\n    else {\n        std::cout << " + Chr(34) + "Unsupported type" + Chr(34) + " << std::endl;\n    }\n}\n"
if (InStr(variables['cppCode'] , "FileRead("))or(InStr(variables['cppCode'] , "FileRead (")):
    variables['uperCodeLibs'] += "\n#include <fstream>\n#include <string>\n#include <filesystem>\n#include <stdexcept>\n"
    variables['uperCode'] = variables['uperCode'] + "\nstd::string FileRead(const std::string& path) {\n    std::ifstream file;\n    std::filesystem::path full_path;\n\n    // Check if the file path is an absolute path\n    if (std::filesystem::path(path).is_absolute()) {\n        full_path = path;\n    } else {\n        // If it's not a full path, prepend the current working directory\n        full_path = std::filesystem::current_path() / path;\n    }\n\n    // Open the file\n    file.open(full_path);\n    if (!file.is_open()) {\n        throw std::runtime_error(" + Chr(34) + "Error: Could not open the file." + Chr(34) + ");\n    }\n\n    // Read the file content into a string\n    std::string content;\n    std::string line;\n    while (std::getline(file, line)) {\n        content += line + '" + Chr(92) + "n';\n    }\n\n    file.close();\n    return content;\n}\n"
if (InStr(variables['cppCode'] , "FileAppend("))or(InStr(variables['cppCode'] , "FileAppend (")):
    variables['uperCodeLibs'] += "\n#include <fstream>\n#include <iostream>\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\nbool FileAppend(const std::string& content, const std::string& path) {\n    std::ofstream file;\n\n    // Open the file in append mode\n    file.open(path, std::ios::app);\n\n    if (!file.is_open()) {\n        std::cerr << " + Chr(34) + "Error: Could not open the file for appending." + Chr(34) + " << std::endl;\n        return false;\n    }\n\n    // Append the content to the file\n    file << content;\n\n    // Close the file\n    file.close();\n\n    return true;\n}\n\n"
if (InStr(variables['cppCode'] , "FileDelete("))or(InStr(variables['cppCode'] , "FileDelete (")):
    variables['uperCodeLibs'] += "\n#include <filesystem>\n#include <iostream>\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\nbool FileDelete(const std::string& path) {\n    std::filesystem::path file_path(path);\n\n    // Check if the file exists\n    if (!std::filesystem::exists(file_path)) {\n        std::cerr << " + Chr(34) + "Error: File does not exist." + Chr(34) + " << std::endl;\n        return false;\n    }\n\n    // Attempt to remove the file\n    if (!std::filesystem::remove(file_path)) {\n        std::cerr << " + Chr(34) + "Error: Failed to delete the file." + Chr(34) + " << std::endl;\n        return false;\n    }\n\n    return true;\n}\n"
if (InStr(variables['cppCode'] , "StrLen("))or(InStr(variables['cppCode'] , "StrLen (")):
    variables['uperCodeLibs'] += "\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\nsize_t StrLen(const std::string& str) {\n    return str.length();\n}\n"
if (InStr(variables['cppCode'] , "Asc("))or(InStr(variables['cppCode'] , "Asc (")):
    variables['uperCodeLibs'] += "\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\nint Asc(const std::string& str) {\n    if (!str.empty()) {\n        return static_cast<int>(str[0]);\n    }\n    return -1; // Return -1 if the string is empty\n}\n"
if (InStr(variables['cppCode'] , "Abs("))or(InStr(variables['cppCode'] , "Abs (")):
    variables['uperCodeLibs'] += "\n#include <cmath>\n"
    variables['uperCode'] = variables['uperCode'] + "\ndouble Abs(double value) {\n    return std::fabs(value);\n}\n\n"
if (InStr(variables['cppCode'] , "ACos("))or(InStr(variables['cppCode'] , "ACos (")):
    variables['uperCodeLibs'] += "\n#include <cmath>\n"
    variables['uperCode'] = variables['uperCode'] + "\ndouble ACos(double value) {\n    return std::acos(value);\n}\n"
if (InStr(variables['cppCode'] , "ASin("))or(InStr(variables['cppCode'] , "ASin (")):
    variables['uperCodeLibs'] += "\n#include <cmath>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Define your custom ASin function\ndouble ASin(double value) {\n    // Ensure the value is within the valid range for asin\n    if (value < -1.0 || value > 1.0) {\n        std::cerr << " + Chr(34) + "Error: Value out of range for arcsine function." + Chr(34) + " << std::endl;\n        return NAN;  // Return 'Not-a-Number' to indicate an error\n    }\n\n    return asin(value);  // Call the standard asin function\n}\n"
if (InStr(variables['cppCode'] , "ATan("))or(InStr(variables['cppCode'] , "ATan (")):
    variables['uperCodeLibs'] += "\n#include <cmath>\n"
    variables['uperCode'] = variables['uperCode'] + "\ndouble ATan(double value) {\n    return std::atan(value);\n}\n"
if (InStr(variables['cppCode'] , "Ceil("))or(InStr(variables['cppCode'] , "Ceil (")):
    variables['uperCodeLibs'] += "\n#include <cmath>\n"
    variables['uperCode'] = variables['uperCode'] + "\ndouble Ceil(double value) {\n    return std::ceil(value);\n}\n"
if (InStr(variables['cppCode'] , "Cos("))or(InStr(variables['cppCode'] , "Cos (")):
    variables['uperCodeLibs'] += "\n#include <cmath>\n"
    variables['uperCode'] = variables['uperCode'] + "\ndouble Cos(double angle) {\n    return std::cos(angle);\n}\n"
if (InStr(variables['cppCode'] , "Exp("))or(InStr(variables['cppCode'] , "Exp (")):
    variables['uperCodeLibs'] += "\n#include <cmath>\n"
    variables['uperCode'] = variables['uperCode'] + "\ndouble Exp(double value) {\n    return std::exp(value);\n}\n"
if (InStr(variables['cppCode'] , "Ln("))or(InStr(variables['cppCode'] , "Ln (")):
    variables['uperCodeLibs'] += "\n#include <cmath>\n"
    variables['uperCode'] = variables['uperCode'] + "\ndouble Ln(double value) {\n    return std::log(value);\n}\n"
if (InStr(variables['cppCode'] , "Log("))or(InStr(variables['cppCode'] , "Log (")):
    variables['uperCodeLibs'] += "\n#include <cmath>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Function that computes the logarithm with base 10\ndouble Log(double value) {\n    return std::log10(value);\n}\n"
if (InStr(variables['cppCode'] , "Round("))or(InStr(variables['cppCode'] , "Round (")):
    variables['uperCodeLibs'] += "\n#include <cmath>\n"
    variables['uperCode'] = variables['uperCode'] + "\ndouble Round(double value) {\n    return std::round(value);\n}\n"
if (InStr(variables['cppCode'] , "Sin("))or(InStr(variables['cppCode'] , "Sin (")):
    variables['uperCodeLibs'] += "\n#include <cmath>\n"
    variables['uperCode'] = variables['uperCode'] + "\ndouble Sin(double angle) {\n    return std::sin(angle);\n}\n"
if (InStr(variables['cppCode'] , "Sqrt("))or(InStr(variables['cppCode'] , "Sqrt (")):
    variables['uperCodeLibs'] += "\n#include <cmath>\n"
    variables['uperCode'] = variables['uperCode'] + "\ndouble Sqrt(double value) {\n    return std::sqrt(value);\n}\n"
if (InStr(variables['cppCode'] , "Tan("))or(InStr(variables['cppCode'] , "Tan (")):
    variables['uperCodeLibs'] += "\n#include <cmath>\n"
    variables['uperCode'] = variables['uperCode'] + "\ndouble Tan(double angle) {\n    return std::tan(angle);\n}\n"
if (InStr(variables['cppCode'] , "SubStr("))or(InStr(variables['cppCode'] , "SubStr (")):
    variables['uperCodeLibs'] += "\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\nstd::string SubStr(const std::string& str, int startPos, int length = -1) {\n    std::string result;\n    size_t strLen = str.size();\n\n    // Handle negative starting positions\n    if (startPos < 0) {\n        startPos += strLen;\n        if (startPos < 0) startPos = 0;\n    } else {\n        if (startPos > static_cast<int>(strLen)) return " + Chr(34) + "" + Chr(34) + "; // Starting position beyond string length\n        startPos -= 1; // Convert to 0-based index\n    }\n\n    // Handle length\n    if (length < 0) {\n        length = strLen - startPos; // Length to end of string\n    } else if (startPos + length > static_cast<int>(strLen)) {\n        length = strLen - startPos; // Adjust length to fit within the string\n    }\n\n    // Extract substring\n    result = str.substr(startPos, length);\n    return result;\n}\n"
if (InStr(variables['cppCode'] , "Trim("))or(InStr(variables['cppCode'] , "Trim (")):
    variables['uperCodeLibs'] += "\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\nstd::string Trim(const std::string &inputString) {\n    if (inputString.empty()) return " + Chr(34) + "" + Chr(34) + ";\n\n    size_t start = inputString.find_first_not_of(" + Chr(34) + " " + Chr(92) + "t" + Chr(92) + "n" + Chr(92) + "r" + Chr(92) + "f" + Chr(92) + "v" + Chr(34) + ");\n    size_t end = inputString.find_last_not_of(" + Chr(34) + " " + Chr(92) + "t" + Chr(92) + "n" + Chr(92) + "r" + Chr(92) + "f" + Chr(92) + "v" + Chr(34) + ");\n\n    return (start == std::string::npos) ? " + Chr(34) + "" + Chr(34) + " : inputString.substr(start, end - start + 1);\n}\n"
if (InStr(variables['cppCode'] , "StrReplace("))or(InStr(variables['cppCode'] , "StrReplace (")):
    variables['uperCodeLibs'] += "\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\nstd::string StrReplace(const std::string &originalString, const std::string &find, const std::string &replaceWith) {\n    std::string result = originalString;\n    size_t pos = 0;\n\n    while ((pos = result.find(find, pos)) != std::string::npos) {\n        result.replace(pos, find.length(), replaceWith);\n        pos += replaceWith.length();\n    }\n\n    return result;\n}\n"
if (InStr(variables['cppCode'] , "StringTrimLeft("))or(InStr(variables['cppCode'] , "StringTrimLeft (")):
    variables['uperCodeLibs'] += "\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\nstd::string StringTrimLeft(const std::string &input, int numChars) {\n    return (numChars <= input.length()) ? input.substr(numChars) : input;\n}\n"
if (InStr(variables['cppCode'] , "StringTrimRight("))or(InStr(variables['cppCode'] , "StringTrimRight (")):
    variables['uperCodeLibs'] += "\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\nstd::string StringTrimRight(const std::string &input, int numChars) {\n    return (numChars <= input.length()) ? input.substr(0, input.length() - numChars) : input;\n}\n"
if (InStr(variables['cppCode'] , "StrLower("))or(InStr(variables['cppCode'] , "StrLower (")):
    variables['uperCodeLibs'] += "\n#include <algorithm>\n#include <cctype>\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\nstd::string StrLower(const std::string &string) {\n    std::string result = string;\n    std::transform(result.begin(), result.end(), result.begin(), ::tolower);\n    return result;\n}\n"
if (InStr(variables['cppCode'] , "StrSplit("))or(InStr(variables['cppCode'] , "StrSplit (")):
    variables['uperCodeLibs'] += "\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\nstd::string StrSplit(const std::string &inputStr, const std::string &delimiter, int num) {\n    size_t start = 0, end = 0, count = 0;\n\n    while ((end = inputStr.find(delimiter, start)) != std::string::npos) {\n        if (++count == num) {\n            return inputStr.substr(start, end - start);\n        }\n        start = end + delimiter.length();\n    }\n\n    if (count + 1 == num) {\n        return inputStr.substr(start);\n    }\n\n    return " + Chr(34) + "" + Chr(34) + ";\n}\n"
if (InStr(variables['cppCode'] , "Chr("))or(InStr(variables['cppCode'] , "Chr (")):
    variables['uperCodeLibs'] += "\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\nstd::string Chr(int number) {\n    return (number >= 0 && number <= 0x10FFFF) ? std::string(1, static_cast<char>(number)) : " + Chr(34) + "" + Chr(34) + ";\n}\n\n"
if (InStr(variables['cppCode'] , "Mod("))or(InStr(variables['cppCode'] , "Mod (")):
    variables['uperCodeLibs'] += "\n#include <string>\n"
    variables['uperCode'] = variables['uperCode'] + "\nint Mod(int dividend, int divisor) {\n    return dividend % divisor;\n}\n"
if (InStr(variables['cppCode'] , "Floor("))or(InStr(variables['cppCode'] , "Floor (")):
    variables['uperCodeLibs'] += "\n#include <cmath>\n#include <limits>\n"
    variables['uperCode'] = variables['uperCode'] + "\ndouble Floor(double num) {\n    if (std::isnan(num)) {\n        return std::numeric_limits<double>::quiet_NaN();\n    }\n    return std::floor(num);\n}\n"
if (InStr(variables['cppCode'] , "getDataFromJSON("))or(InStr(variables['cppCode'] , "getDataFromJSON (")):
    variables['uperCodeLibs'] += "\n#include <string>\n#include <vector>\n#include <map>\n#include <sstream>\n#include <iomanip>\n#include <stdexcept>\n#include <cctype>\n#include <chrono>\n#include <cmath>\n"
    variables['uperCode'] = variables['uperCode'] + "\nstd::string trim(const std::string& str) {\n    auto start = str.begin();\n    while (start != str.end() && std::isspace(*start)) {\n        start++;\n    }\n    auto end = str.end();\n    do {\n        end--;\n    } while (std::distance(start, end) > 0 && std::isspace(*end));\n    return std::string(start, end + 1);\n}\n\nclass JSONValue {\npublic:\n    enum Type { Null, Boolean, Number, String, Array, Object };\n\n    JSONValue() : type(Null) {}\n    JSONValue(bool b) : type(Boolean), boolean_value(b) {}\n    JSONValue(double n) : type(Number), number_value(n) {}\n    JSONValue(const std::string& s) : type(String), string_value(s) {}\n    JSONValue(const std::vector<JSONValue>& a) : type(Array), array_value(a) {}\n    JSONValue(const std::map<std::string, JSONValue>& o) : type(Object), object_value(o) {}\n\n    Type getType() const { return type; }\n    bool isNull() const { return type == Null; }\n    bool isBoolean() const { return type == Boolean; }\n    bool isNumber() const { return type == Number; }\n    bool isString() const { return type == String; }\n    bool isArray() const { return type == Array; }\n    bool isObject() const { return type == Object; }\n\n    bool asBoolean() const { return boolean_value; }\n    double asNumber() const { return number_value; }\n    const std::string& asString() const { return string_value; }\n    const std::vector<JSONValue>& asArray() const { return array_value; }\n    const std::map<std::string, JSONValue>& asObject() const { return object_value; }\n\nprivate:\n    Type type;\n    bool boolean_value;\n    double number_value;\n    std::string string_value;\n    std::vector<JSONValue> array_value;\n    std::map<std::string, JSONValue> object_value;\n};\n\nclass JSONParser {\npublic:\n    static JSONValue parse(const std::string& json) {\n        size_t index = 0;\n        return parseValue(json, index);\n    }\n\nprivate:\n    static JSONValue parseValue(const std::string& json, size_t& index) {\n        skipWhitespace(json, index);\n        char c = json[index];\n        if (c == '{') {\n            return parseObject(json, index);\n        } else if (c == '[') {\n            return parseArray(json, index);\n        } else if (c == '" + Chr(34) + "') {\n            return parseString(json, index);\n        } else if (std::isdigit(c) || c == '-') {\n            return parseNumber(json, index);\n        } else if (c == 't' || c == 'f') {\n            return parseBoolean(json, index);\n        } else if (c == 'n') {\n            return parseNull(json, index);\n        }\n        throw std::runtime_error(" + Chr(34) + "Invalid JSON" + Chr(34) + ");\n    }\n\n    static JSONValue parseObject(const std::string& json, size_t& index) {\n        std::map<std::string, JSONValue> object;\n        index++; // Skip '{'\n        skipWhitespace(json, index);\n        if (json[index] == '}') {\n            index++;\n            return JSONValue(object);\n        }\n        while (true) {\n            std::string key = parseString(json, index).asString();\n            skipWhitespace(json, index);\n            if (json[index] != ':') throw std::runtime_error(" + Chr(34) + "Expected ':'" + Chr(34) + ");\n            index++;\n            JSONValue value = parseValue(json, index);\n            object[key] = value;\n            skipWhitespace(json, index);\n            if (json[index] == '}') {\n                index++;\n                return JSONValue(object);\n            }\n            if (json[index] != ',') throw std::runtime_error(" + Chr(34) + "Expected ',' or '}'" + Chr(34) + ");\n            index++;\n            skipWhitespace(json, index);\n        }\n    }\n\n    static JSONValue parseArray(const std::string& json, size_t& index) {\n        std::vector<JSONValue> array;\n        index++; // Skip '['\n        skipWhitespace(json, index);\n        if (json[index] == ']') {\n            index++;\n            return JSONValue(array);\n        }\n        while (true) {\n            array.push_back(parseValue(json, index));\n            skipWhitespace(json, index);\n            if (json[index] == ']') {\n                index++;\n                return JSONValue(array);\n            }\n            if (json[index] != ',') throw std::runtime_error(" + Chr(34) + "Expected ',' or ']'" + Chr(34) + ");\n            index++;\n            skipWhitespace(json, index);\n        }\n    }\n\n    static JSONValue parseString(const std::string& json, size_t& index) {\n        index++; // Skip opening quote\n        std::string result;\n        while (json[index] != '" + Chr(34) + "') {\n            if (json[index] == '" + Chr(92) + "" + Chr(92) + "') {\n                index++;\n                switch (json[index]) {\n                    case '" + Chr(34) + "': result += '" + Chr(34) + "'; break;\n                    case '" + Chr(92) + "" + Chr(92) + "': result += '" + Chr(92) + "" + Chr(92) + "'; break;\n                    case '/': result += '/'; break;\n                    case 'b': result += '" + Chr(92) + "b'; break;\n                    case 'f': result += '" + Chr(92) + "f'; break;\n                    case 'n': result += '" + Chr(92) + "n'; break;\n                    case 'r': result += '" + Chr(92) + "r'; break;\n                    case 't': result += '" + Chr(92) + "t'; break;\n                    default: throw std::runtime_error(" + Chr(34) + "Invalid escape sequence" + Chr(34) + ");\n                }\n            } else {\n                result += json[index];\n            }\n            index++;\n        }\n        index++; // Skip closing quote\n        return JSONValue(result);\n    }\n\n    static JSONValue parseNumber(const std::string& json, size_t& index) {\n        size_t start = index;\n        while (std::isdigit(json[index]) || json[index] == '-' || json[index] == '.' || json[index] == 'e' || json[index] == 'E') {\n            index++;\n        }\n        return JSONValue(std::stod(json.substr(start, index - start)));\n    }\n\n    static JSONValue parseBoolean(const std::string& json, size_t& index) {\n        if (json.substr(index, 4) == " + Chr(34) + "true" + Chr(34) + ") {\n            index += 4;\n            return JSONValue(true);\n        } else if (json.substr(index, 5) == " + Chr(34) + "false" + Chr(34) + ") {\n            index += 5;\n            return JSONValue(false);\n        }\n        throw std::runtime_error(" + Chr(34) + "Invalid boolean value" + Chr(34) + ");\n    }\n\n    static JSONValue parseNull(const std::string& json, size_t& index) {\n        if (json.substr(index, 4) == " + Chr(34) + "null" + Chr(34) + ") {\n            index += 4;\n            return JSONValue();\n        }\n        throw std::runtime_error(" + Chr(34) + "Invalid null value" + Chr(34) + ");\n    }\n\n    static void skipWhitespace(const std::string& json, size_t& index) {\n        while (index < json.length() && std::isspace(json[index])) {\n            index++;\n        }\n    }\n};\n\nstd::string getDataFromJSON(const std::string& json_data, const std::string& json_path) {\n    JSONValue root = JSONParser::parse(json_data);\n    std::istringstream path_stream(json_path);\n    std::string segment;\n    JSONValue current = root;\n\n    while (std::getline(path_stream, segment, '.')) {\n        segment = trim(segment);\n\n        size_t bracket_pos = segment.find('[');\n        if (bracket_pos != std::string::npos) {\n            std::string key = segment.substr(0, bracket_pos);\n            size_t index = std::stoi(segment.substr(bracket_pos + 1, segment.find(']') - bracket_pos - 1));\n\n            if (key.empty()) {\n                // This is a direct array access\n                if (current.isArray() && index < current.asArray().size()) {\n                    current = current.asArray()[index];\n                } else {\n                    return " + Chr(34) + "Array index out of bounds" + Chr(34) + ";\n                }\n            } else {\n                // This is an object access followed by array access\n                if (current.isObject() && current.asObject().find(key) != current.asObject().end()) {\n                    current = current.asObject().at(key);\n                    if (current.isArray() && index < current.asArray().size()) {\n                        current = current.asArray()[index];\n                    } else {\n                        return " + Chr(34) + "Array index out of bounds" + Chr(34) + ";\n                    }\n                } else {\n                    return " + Chr(34) + "Key not found: " + Chr(34) + " + key;\n                }\n            }\n        } else if (current.isObject() && current.asObject().find(segment) != current.asObject().end()) {\n            current = current.asObject().at(segment);\n        } else {\n            return " + Chr(34) + "Key not found: " + Chr(34) + " + segment;\n        }\n    }\n\n    if (current.isString()) return current.asString();\n    if (current.isNumber()) {\n        double num = current.asNumber();\n        if (num == floor(num)) {\n            return std::to_string(static_cast<long long>(num));\n        } else {\n            return std::to_string(num);\n        }\n    }\n    if (current.isBoolean()) return current.asBoolean() ? " + Chr(34) + "true" + Chr(34) + " : " + Chr(34) + "false" + Chr(34) + ";\n    if (current.isNull()) return " + Chr(34) + "null" + Chr(34) + ";\n\n    return " + Chr(34) + "Unsupported value type" + Chr(34) + ";\n}\n"
if (InStr(variables['cppCode'] , "GetParams("))or(InStr(variables['cppCode'] , "GetParams (")):
    variables['uperCodeLibs'] += "\n#include <string>\n#include <vector>\n#include <filesystem>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Function to get command-line parameters\nstd::string GetParams() {\n    std::vector<std::string> params;\n    for (int i = 1; i < __argc; ++i) {\n        std::string arg = __argv[i];\n        if (std::filesystem::exists(arg)) {\n            arg = std::filesystem::absolute(arg).string();\n        }\n        params.push_back(arg);\n    }\n    std::string result;\n    for (const auto& param : params) {\n        result += param + " + Chr(34) + "" + Chr(92) + "n" + Chr(34) + ";\n    }\n    return result;\n}\n"
if (InStr(variables['cppCode'] , "BuildInVars("))or(InStr(variables['cppCode'] , "BuildInVars (")):
    variables['uperCodeLibs'] += "\n#include <iostream>\n#include <chrono>\n#include <ctime>\n#include <sstream>\n#include <iomanip>\n#include <string>\n#include <limits>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Store the start time as a global variable\nstd::chrono::time_point<std::chrono::steady_clock> programStartTime = std::chrono::steady_clock::now();\n\n// Function to get built-in variables\nstd::string BuildInVars(const std::string& varName) {\n    auto now = std::chrono::system_clock::now();\n    std::time_t currentTime = std::chrono::system_clock::to_time_t(now);\n    std::tm* localTime = std::localtime(&currentTime);\n\n    std::ostringstream oss;\n\n    if (varName == " + Chr(34) + "A_TickCount" + Chr(34) + ") {\n        // Calculate milliseconds since program start\n        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now() - programStartTime).count();\n        if (duration > std::numeric_limits<int>::max()) {\n            // Handle overflow case\n            return " + Chr(34) + "Value too large" + Chr(34) + ";\n        } else {\n            return std::to_string(static_cast<int>(duration));\n        }\n    } else if (varName == " + Chr(34) + "A_Now" + Chr(34) + ") {\n        oss << std::put_time(localTime, " + Chr(34) + "%Y-%m-%d %H:%M:%S" + Chr(34) + ");\n    } else if (varName == " + Chr(34) + "A_YYYY" + Chr(34) + ") {\n        oss << std::put_time(localTime, " + Chr(34) + "%Y" + Chr(34) + ");\n    } else if (varName == " + Chr(34) + "A_MM" + Chr(34) + ") {\n        oss << std::put_time(localTime, " + Chr(34) + "%m" + Chr(34) + ");\n    } else if (varName == " + Chr(34) + "A_DD" + Chr(34) + ") {\n        oss << std::put_time(localTime, " + Chr(34) + "%d" + Chr(34) + ");\n    } else if (varName == " + Chr(34) + "A_MMMM" + Chr(34) + ") {\n        oss << std::put_time(localTime, " + Chr(34) + "%B" + Chr(34) + ");\n    } else if (varName == " + Chr(34) + "A_MMM" + Chr(34) + ") {\n        oss << std::put_time(localTime, " + Chr(34) + "%b" + Chr(34) + ");\n    } else if (varName == " + Chr(34) + "A_DDDD" + Chr(34) + ") {\n        oss << std::put_time(localTime, " + Chr(34) + "%A" + Chr(34) + ");\n    } else if (varName == " + Chr(34) + "A_DDD" + Chr(34) + ") {\n        oss << std::put_time(localTime, " + Chr(34) + "%a" + Chr(34) + ");\n    } else if (varName == " + Chr(34) + "A_Hour" + Chr(34) + ") {\n        oss << std::put_time(localTime, " + Chr(34) + "%H" + Chr(34) + ");\n    } else if (varName == " + Chr(34) + "A_Min" + Chr(34) + ") {\n        oss << std::put_time(localTime, " + Chr(34) + "%M" + Chr(34) + ");\n    } else if (varName == " + Chr(34) + "A_Sec" + Chr(34) + ") {\n        oss << std::put_time(localTime, " + Chr(34) + "%S" + Chr(34) + ");\n    } else if (varName == " + Chr(34) + "A_Space" + Chr(34) + ") {\n        return " + Chr(34) + " " + Chr(34) + ";\n    } else if (varName == " + Chr(34) + "A_Tab" + Chr(34) + ") {\n        return " + Chr(34) + "" + Chr(92) + "t" + Chr(34) + ";\n    } else {\n        return " + Chr(34) + "" + Chr(34) + ";\n    }\n    return oss.str();\n}\n"
if (InStr(variables['cppCode'] , "RegExReplace("))or(InStr(variables['cppCode'] , "RegExReplace (")):
    variables['uperCodeLibs'] += "\n#include <string>\n#include <regex>\n#include <iostream>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Function to perform regex replacement\nstd::string RegExReplace(const std::string& inputStr, const std::string& regexPattern, const std::string& replacement) {\n    std::regex re(regexPattern, std::regex_constants::ECMAScript | std::regex_constants::multiline);\n    return std::regex_replace(inputStr, re, replacement);\n}\n"
if (InStr(variables['cppCode'] , "RunCMD("))or(InStr(variables['cppCode'] , "RunCMD (")):
    variables['uperCodeLibs'] += "\n#include <iostream>\n#include <stdexcept>\n#include <string>\n#include <array>\n#include <memory>\n#include <cstdio>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Define a type alias for the deleter\nusing Deleter = void (*)(FILE*);\n\n// Function to run a system command\nstd::string RunCMD(const std::string& command) {\n    std::array<char, 128> buffer;\n    std::string result;\n#if defined(_WIN32)\n    std::unique_ptr<FILE, Deleter> pipe(_popen(command.c_str(), " + Chr(34) + "r" + Chr(34) + "), _pclose);\n#else\n    std::unique_ptr<FILE, Deleter> pipe(popen(command.c_str(), " + Chr(34) + "r" + Chr(34) + "), pclose);\n#endif\n    if (!pipe) {\n        throw std::runtime_error(" + Chr(34) + "popen() failed!" + Chr(34) + ");\n    }\n    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {\n        result += buffer.data();\n    }\n    return result;\n}\n\nint main(int argc, char* argv[]) {\n    try {\n        std::string output = RunCMD(" + Chr(34) + "echo foo" + Chr(34) + ");\n        std::cout << output;\n    } catch (const std::exception& e) {\n        std::cerr << " + Chr(34) + "Error: " + Chr(34) + " << e.what() << std::endl;\n    }\n    return 0;\n}\n"
if (InStr(variables['cppCode'] , "RegExMatch("))or(InStr(variables['cppCode'] , "RegExMatch (")):
    variables['uperCodeLibs'] += "\n#include <iostream>\n#include <string>\n#include <regex>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Function to perform regex matching and return the match position\nint RegExMatch(const std::string& haystack, const std::string& needleRegEx, std::string* outputVar = nullptr, int startingPos = 0) {\n    if (haystack.empty() || needleRegEx.empty()) {\n        return 0;\n    }\n\n    std::regex re(needleRegEx);\n    std::smatch match;\n\n    if (std::regex_search(haystack.begin() + startingPos, haystack.end(), match, re)) {\n        if (outputVar != nullptr) {\n            *outputVar = match.str(0);\n        }\n        return match.position(0) + 1; // To make it 1-based index\n    }\n\n    return 0;\n}\n"
if (InStr(variables['cppCode'] , "ExitApp("))or(InStr(variables['cppCode'] , "ExitApp (")):
    variables['uperCodeLibs'] += "\n#include <iostream>\n#include <cstdlib>\n"
    variables['uperCode'] = variables['uperCode'] + "\nvoid ExitApp() {\n    std::cout << " + Chr(34) + "Exiting application..." + Chr(34) + " << std::endl;\n    std::exit(0);\n}\n"
if (InStr(variables['cppCode'] , "SetTimer("))or(InStr(variables['cppCode'] , "SetTimer (")):
    variables['uperCodeLibs'] += "\n#include <iostream>\n#include <map>\n#include <functional>\n#include <chrono>\n#include <mutex>\n#include <string>\n#include <sstream>\n#include <atomic>\n#include <thread>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Structure to store timer information\nstruct TimerInfo {\n    std::function<void()> func;\n    int interval_ms;\n    bool active;\n    std::chrono::steady_clock::time_point last_execution;\n};\n\n// Maps to store the timers and their states\nstd::map<std::string, TimerInfo> timers;\nstd::mutex mtx; // Mutex for synchronizing access to shared data\nstd::atomic<bool> should_exit(false); // Flag to signal the application to exit\n\nvoid TimerManager() {\n    while (!should_exit) {\n        auto now = std::chrono::steady_clock::now();\n        {\n            std::lock_guard<std::mutex> lock(mtx);\n            bool any_active_timers = false;\n            for (auto& [name, timer] : timers) {\n                if (timer.active) {\n                    any_active_timers = true;\n                    auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(now - timer.last_execution);\n                    if (elapsed.count() >= timer.interval_ms) {\n                        timer.func();\n                        timer.last_execution = now;\n                    }\n                }\n            }\n            if (!any_active_timers) {\n                should_exit = true;\n            }\n        }\n        std::this_thread::sleep_for(std::chrono::milliseconds(10)); // Sleep for a short period to reduce CPU usage\n    }\n}\n\n// Global counter for unique timer names\nstatic int timer_counter = 0;\n\nvoid SetTimer(const std::function<void()>& func, const std::string& timeOrOnOff) {\n    std::lock_guard<std::mutex> lock(mtx); // Lock for safe access to shared data\n\n    // Create a unique identifier for the timer\n    std::string name = " + Chr(34) + "timer_" + Chr(34) + " + std::to_string(timer_counter++);\n\n    if (timeOrOnOff == " + Chr(34) + "On" + Chr(34) + ") {\n        timers[name] = {func, 10, true, std::chrono::steady_clock::now()};\n    } else if (timeOrOnOff == " + Chr(34) + "Off" + Chr(34) + ") {\n        // Find the timer with the matching function and turn it off\n        for (auto& [timer_name, timer] : timers) {\n            if (timer.func.target_type() == func.target_type() && timer.active) {\n                timer.active = false;\n                break;\n            }\n        }\n    } else {\n        try {\n            int interval_ms = std::stoi(timeOrOnOff);\n            timers[name] = {func, interval_ms, true, std::chrono::steady_clock::now()};\n        } catch (const std::invalid_argument&) {\n            std::cerr << " + Chr(34) + "Invalid interval value: " + Chr(34) + " << timeOrOnOff << std::endl;\n        }\n    }\n}\n"
if (InStr(variables['cppCode'] , "getDataFromAPI("))or(InStr(variables['cppCode'] , "getDataFromAPI (")):
    variables['uperCodeLibs'] += "\n#include <string>\n#include <array>\n#include <memory>\n#include <stdexcept>\n#include <cstdio>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Function to run a system command\nstd::string getDataFromAPIRunCMD(const std::string& command) {\n    std::array<char, 128> buffer;\n    std::string result;\n#if defined(_WIN32)\n    std::unique_ptr<FILE, decltype(&_pclose)> pipe(_popen(command.c_str(), " + Chr(34) + "r" + Chr(34) + "), _pclose);\n#else\n    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(command.c_str(), " + Chr(34) + "r" + Chr(34) + "), pclose);\n#endif\n    if (!pipe) {\n        throw std::runtime_error(" + Chr(34) + "popen() failed!" + Chr(34) + ");\n    }\n    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {\n        result += buffer.data();\n    }\n    return result;\n}\n\n\n// Function to fetch data from API\nstd::string getDataFromAPI(const std::string& url) {\n    std::string command = " + Chr(34) + "curl -s " + Chr(34) + " + url;\n    return getDataFromAPIRunCMD(command);\n}\n"
if (InStr(variables['cppCode'] , "SortLikeAHK("))or(InStr(variables['cppCode'] , "SortLikeAHK (")):
    variables['uperCodeLibs'] += "\n#include <string>\n#include <vector>\n#include <algorithm>\n#include <sstream>\n#include <unordered_set>\n#include <cctype>\n"
    variables['uperCode'] = variables['uperCode'] + "\n// Helper function to trim whitespace from both ends of a string\nstd::string trim(const std::string& str) {\n    const std::string whitespace = " + Chr(34) + " " + Chr(92) + "t" + Chr(92) + "n" + Chr(92) + "r" + Chr(92) + "f" + Chr(92) + "v" + Chr(34) + ";\n    size_t start = str.find_first_not_of(whitespace);\n    if (start == std::string::npos) return " + Chr(34) + "" + Chr(34) + ";\n    size_t end = str.find_last_not_of(whitespace);\n    return str.substr(start, end - start + 1);\n}\n\n// Helper function to convert string to lowercase\nstd::string toLower(const std::string& str) {\n    std::string lowerStr = str;\n    std::transform(lowerStr.begin(), lowerStr.end(), lowerStr.begin(), ::tolower);\n    return lowerStr;\n}\n\n// Function to sort case-insensitively but ensure lowercase items come last\nbool customSortCompare(const std::string& a, const std::string& b) {\n    std::string lowerA = toLower(a);\n    std::string lowerB = toLower(b);\n    if (lowerA == lowerB) {\n        // If case-insensitive equivalent, ensure lowercase items come last\n        if (std::islower(a[0]) && std::isupper(b[0])) {\n            return false; // a should come after b\n        } else if (std::isupper(a[0]) && std::islower(b[0])) {\n            return true; // a should come before b\n        }\n        return a < b; // Otherwise, sort lexicographically\n    }\n    return lowerA < lowerB;\n}\n\n// Function to remove exact duplicates (case-sensitive)\nstd::vector<std::string> removeExactDuplicates(const std::vector<std::string>& items) {\n    std::unordered_set<std::string> seen;\n    std::vector<std::string> uniqueItems;\n    for (const auto& item : items) {\n        if (seen.find(item) == seen.end()) {\n            seen.insert(item);\n            uniqueItems.push_back(item);\n        }\n    }\n    return uniqueItems;\n}\n\n// Main sorting function\nstd::string SortLikeAHK(const std::string& input, const std::string& options) {\n    std::string delimiter = " + Chr(34) + "" + Chr(92) + "n" + Chr(34) + ";\n    bool caseInsensitive = options.find('C') != std::string::npos;\n    bool unique = options.find('U') != std::string::npos;\n    bool reverse = options.find('R') != std::string::npos;\n    bool random = options.find(" + Chr(34) + "Random" + Chr(34) + ") != std::string::npos;\n    bool numeric = options.find('N') != std::string::npos;\n\n    // Custom delimiter\n    if (options.find('D') != std::string::npos) {\n        size_t delimiterPos = options.find('D') + 1;\n        if (delimiterPos < options.size()) {\n            delimiter = options.substr(delimiterPos, 1);\n        }\n    }\n\n    // Split input by delimiter\n    std::vector<std::string> items;\n    std::stringstream ss(input);\n    std::string item;\n    while (std::getline(ss, item, delimiter[0])) {\n        item = trim(item);  // Trim whitespace from each item\n        if (!item.empty()) {\n            items.push_back(item);\n        }\n    }\n\n    // Sort items\n    if (numeric) {\n        std::sort(items.begin(), items.end(), [](const std::string& a, const std::string& b) {\n            return std::stoi(a) < std::stoi(b);\n        });\n    } else {\n        std::sort(items.begin(), items.end(), customSortCompare);\n    }\n\n    // Remove exact duplicates if needed\n    if (unique) {\n        items = removeExactDuplicates(items);\n    }\n\n    // Apply reverse order if needed\n    if (reverse) {\n        std::reverse(items.begin(), items.end());\n    }\n\n    // Separate uppercase and lowercase items\n    std::vector<std::string> uppercaseItems;\n    std::vector<std::string> lowercaseItems;\n    \n    for (const auto& item : items) {\n        if (std::isupper(item[0])) {\n            uppercaseItems.push_back(item);\n        } else {\n            lowercaseItems.push_back(item);\n        }\n    }\n\n    // Combine sorted uppercase items with sorted lowercase items\n    std::string result;\n    for (const auto& item : uppercaseItems) {\n        result += item;\n        result += delimiter;\n    }\n    for (const auto& item : lowercaseItems) {\n        result += item;\n        if (&item != &lowercaseItems.back()) {\n            result += delimiter;\n        }\n    }\n\n    // Remove trailing delimiter if necessary\n    if (!result.empty() && result.back() == delimiter[0]) {\n        result.pop_back();\n    }\n\n    return result;\n}\n"
variables['uperCodeLibs'] = SortLikeAHK(variables['uperCodeLibs'], "U")
variables['downCode'] = "\nreturn 0;\n}"
variables['cppCode'] = variables['uperCodeLibs'] + "\n" + variables['uperCode'] + "\n" + variables['upCode'] + variables['cppCode'] + variables['downCode']
variables['cppCode'] = StrReplace(variables['cppCode'] , "std::string()" , "")
#MsgBox, % cppCode
variables['filePathOfCode'] = StringTrimRight(variables['filePathOfCode'], 4)
variables['filePathOfCode'] = variables['filePathOfCode'] + "cpp"
FileDelete("" + variables['filePathOfCode'] + "")
FileAppend("" + variables['cppCode'] + "", "" + variables['filePathOfCode'] + "")
