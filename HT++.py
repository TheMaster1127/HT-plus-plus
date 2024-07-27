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
        variables['nameOfVarr111'] = "variables[" + Chr(34) + variables['nameOfVarr11'] + Chr(34) + " + std::string(variables[" + Chr(34) + variables['nameOfVarr12'] + Chr(34) + "])]"
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
for A_Index11, A_LoopField11 in enumerate(items, start=1):
    variables['A_Index11'] = A_Index11
    variables['A_LoopField11'] = A_LoopField11
    if (variables['A_Index11'] == 1):
        print(variables['A_LoopField11'])
        variables['filePathOfCode'] = variables['A_LoopField11']
        variables['code'] = FileRead("" + variables['filePathOfCode'] + "")
    if (variables['A_Index11'] == 2):
        print(variables['A_LoopField11'])
#MsgBox, % code
variables['nothing'] = ""
variables['code'] = StrReplace(variables['code'] , Chr(13), variables['nothing'])
variables['codeTrimBeggining'] = ""
items = LoopParseFunc(variables['code'], "\n", "\r")
for A_Index12, A_LoopField12 in enumerate(items, start=1):
    variables['A_Index12'] = A_Index12
    variables['A_LoopField12'] = A_LoopField12
    variables['codeTrimBeggining'] += Trim(variables['A_LoopField12']) + "\n"
variables['code'] = StringTrimRight(variables['codeTrimBeggining'], 1)
variables['HTpyCodeOUT754754'] = ""
variables['areWEinSome34sNum'] = 0
variables['theIdNumOfThe34'] = 0
items = LoopParseFunc(variables['code'])
for A_Index13, A_LoopField13 in enumerate(items, start=1):
    variables['A_Index13'] = A_Index13
    variables['A_LoopField13'] = A_LoopField13
    variables[f'theIdNumOfThe34theVar{variables["A_Index13"]}'] = Chr(34)
items = LoopParseFunc(variables['code'])
for A_Index14, A_LoopField14 in enumerate(items, start=1):
    variables['A_Index14'] = A_Index14
    variables['A_LoopField14'] = A_LoopField14
    if (variables['A_LoopField14'] == Chr(34)):
        variables['areWEinSome34sNum'] += 1
    if (variables['areWEinSome34sNum'] == 1):
        if (variables['A_LoopField14']  != Chr(34)):
            if (variables['A_LoopField14'] == Chr(96)):
                variables[f'theIdNumOfThe34theVar{variables["theIdNumOfThe34"]}'] += Chr(92)
            else:
                variables[f'theIdNumOfThe34theVar{variables["theIdNumOfThe34"]}'] += variables['A_LoopField14']
        else:
            variables['theIdNumOfThe34'] += 1
            variables['HTpyCodeOUT754754'] += "ihuiuuhuuhtheidFor--asas-theuhturtyphoutr-" + Chr(65) + Chr(65) + str(variables['theIdNumOfThe34']) + Chr(65) + Chr(65)
    if (variables['areWEinSome34sNum'] == 2)or(variables['areWEinSome34sNum'] == 0):
        if (variables['A_LoopField14']  != Chr(34)):
            variables['HTpyCodeOUT754754'] += variables['A_LoopField14']
        variables['areWEinSome34sNum'] = 0
variables['code'] = variables['HTpyCodeOUT754754']
for A_Index15 in range(1, variables['theIdNumOfThe34'] + 1):
    variables['A_Index15'] = A_Index15
    variables[f'theIdNumOfThe34theVar{variables["A_Index15"]}'] += Chr(34)
variables['allVarsChars'] = ""
variables['allVarsInts'] = ""
variables['funcNames'] = "std::string|InStr|LoopParseFunc|print|FileRead|FileAppend|FileDelete|SubStr|Trim|StrReplace|StringTrimLeft|StringTrimRight|StrLower|RegExReplace|StrSplit|Chr|Mod|Floor|A_TickCount|STR|INT|FLOAT"
# func
items = LoopParseFunc(variables['code'], "\n", "\r")
for A_Index16, A_LoopField16 in enumerate(items, start=1):
    variables['A_Index16'] = A_Index16
    variables['A_LoopField16'] = A_LoopField16
    if (SubStr(Trim(StrLower(variables['A_LoopField16'])), 1 , 5)== "func "):
        variables['funcName123'] = StringTrimLeft(variables['A_LoopField16'], 5)
        variables['funcName123'] = Trim(StrSplit(variables['funcName123'] , "(" , 1))
        variables['funcNames'] += "|" + variables['funcName123']
variables['cppCode'] = ""
items = LoopParseFunc(variables['code'], "\n", "\r")
for A_Index17, A_LoopField17 in enumerate(items, start=1):
    variables['A_Index17'] = A_Index17
    variables['A_LoopField17'] = A_LoopField17
    variables['lineDone'] = 0
    if (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 10)== "msgbox, % "):
        variables['msgboxCode'] = StringTrimLeft(variables['A_LoopField17'], 10)
        variables['msgboxCode'] = varTranspiler(variables['msgboxCode'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['cppCode'] += "print(" + variables['msgboxCode'] + ");" + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 8)== "msgbox, "):
        variables['msgboxCode'] = StringTrimLeft(variables['A_LoopField17'], 8)
        variables['cppCode'] += "print(std::string(" + Chr(34) + variables['msgboxCode'] + Chr(34) + "));" + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 1)== ";"):
        variables['str1234'] = StringTrimLeft(variables['A_LoopField17'], 1)
        variables['cppCode'] += "//" + variables['str1234'] + "\n"
        variables['lineDone'] = 1
    elif (SubStr(variables['A_LoopField17'] , -1)== "++"):
        variables['str123'] = Trim(variables['A_LoopField17'])
        variables['str123'] = StringTrimRight(variables['str123'], 2)
        variables['out'] = variables['str123'] + "++;"
        variables['cppCode'] += variables['out'] + "\n"
        variables['lineDone'] = 1
    elif (SubStr(variables['A_LoopField17'] , -1)== "--"):
        variables['str123'] = Trim(variables['A_LoopField17'])
        variables['str123'] = StringTrimRight(variables['str123'], 2)
        variables['out'] = variables['str123'] + "--;"
        variables['cppCode'] += variables['out'] + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 10)== "fileread, "):
        variables['filereadCommand'] = StringTrimLeft(variables['A_LoopField17'], 10)
        variables['filereadCommand1varname'] = StrSplit(variables['filereadCommand'] , ", " , 1)
        variables['filereadCommand2path'] = StrSplit(variables['filereadCommand'] , ", " , 2)
        variables['filereadCommand2path'] = StrReplace(variables['filereadCommand2path'] , "\\" , "\\\\")
        variables['filereadCommand2path'] = Trim(variables['transpileLowVariables'](variables['filereadCommand2path']))
        variables['filereadCommand1varname'] = Trim(variables['transpileVariables'](variables['filereadCommand1varname'] , variables['functionNames']))
        variables['cppCode'] += variables['filereadCommand1varname'] + " = FileRead(" + variables['filereadCommand2path'] + ")\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 12)== "fileappend, "):
        variables['fileAppendCommand'] = StringTrimLeft(variables['A_LoopField17'], 12)
        variables['fileAppendCommand1varname'] = StrSplit(variables['fileAppendCommand'] , ", " , 1)
        variables['fileAppendCommand2path'] = StrSplit(variables['fileAppendCommand'] , ", " , 2)
        variables['fileAppendCommand2path'] = StrReplace(variables['fileAppendCommand2path'] , "\\" , "\\\\")
        variables['fileAppendCommand1varname'] = Trim(variables['transpileLowVariables'](variables['fileAppendCommand1varname']))
        variables['fileAppendCommand2path'] = Trim(variables['transpileLowVariables'](variables['fileAppendCommand2path']))
        variables['cppCode'] += "FileAppend(" + variables['fileAppendCommand1varname'] + ", " + variables['fileAppendCommand2path'] + ")\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 12)== "filedelete, "):
        variables['fileDeleteCommand'] = StringTrimLeft(variables['A_LoopField17'], 12)
        variables['fileDeleteCommand2path'] = StrSplit(variables['fileDeleteCommand'] , ", " , 1)
        variables['fileDeleteCommand2path'] = StrReplace(variables['fileDeleteCommand2path'] , "\\" , "\\\\")
        variables['fileDeleteCommand2path'] = Trim(variables['transpileLowVariables'](variables['fileDeleteCommand2path']))
        variables['cppCode'] += "FileDelete(" + variables['fileDeleteCommand2path'] + ")\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 17)== StrLower("StringTrimRight, ")):
        variables['varr1'] = StrSplit(variables['A_LoopField17'] , "," , 2)
        variables['varr2'] = StrSplit(variables['A_LoopField17'] , "," , 3)
        variables['varr3'] = StrSplit(variables['A_LoopField17'] , "," , 4)
        variables['outt1'] = Trim(varTranspiler(variables['varr1'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts']))
        variables['outt2'] = Trim(varTranspiler(variables['varr2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts']))
        variables['outt3'] = Trim(varTranspiler(variables['varr3'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts']))
        variables['out'] = variables['outt1'] + " = " + "StringTrimRight(" + variables['outt2'] + ", " + variables['outt3'] + ");"
        variables['cppCode'] += variables['out'] + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 16)== StrLower("StringTrimLeft, ")):
        variables['varr1'] = StrSplit(variables['A_LoopField17'] , "," , 2)
        variables['varr2'] = StrSplit(variables['A_LoopField17'] , "," , 3)
        variables['varr3'] = StrSplit(variables['A_LoopField17'] , "," , 4)
        variables['outt1'] = Trim(varTranspiler(variables['varr1'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts']))
        variables['outt2'] = Trim(varTranspiler(variables['varr2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts']))
        variables['outt3'] = Trim(varTranspiler(variables['varr3'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts']))
        variables['out'] = variables['outt1'] + " = " + "StringTrimLeft(" + variables['outt2'] + ", " + variables['outt3'] + ");"
        variables['cppCode'] += variables['out'] + "\n"
        variables['lineDone'] = 1
    elif (variables['A_LoopField17'] == "main:"):
        variables['theMainFuncDec'] = 1
        variables['cppCode'] += "\nint main()\n{\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 5)== "func "):
        variables['funcName123'] = StringTrimLeft(variables['A_LoopField17'], 5)
        variables['removeNextCurlyBraceCpp'] = 1
        variables['funcName123'] = StrReplace(variables['funcName123'] , " str " , " std::string ")
        variables['funcName123'] = StrReplace(variables['funcName123'] , "(str " , "std::string ")
        variables['cppCode'] += "std::any " + variables['funcName123'] + "\n{\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 4)== "str "):
        variables['strVar'] = StringTrimLeft(variables['A_LoopField17'], 4)
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
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 1)== "["):
        variables['strVar'] = StringTrimLeft(variables['A_LoopField17'], 1)
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
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 5)== "char "):
        variables['varName123Temp'] = StringTrimLeft(variables['A_LoopField17'], 5)
        variables['varName'] = StrSplit(variables['varName123Temp'] , " " , 1)
        variables['lineDone'] = 1
        variables['strVar'] = StringTrimLeft(variables['A_LoopField17'], 5)
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
            variables['charVar1'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentTypeSplit'] , 1))
            variables['charVar2'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentTypeSplit'] , 2))
            variables['didItFoundTheChar'] = 0
            variables['cppCode'] += "const char* " + variables['charVar1'] + Chr(59) + "\n"
        else:
            variables['charVar1'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentTypeSplit'] , 1))
            variables['charVar2'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentTypeSplit'] , 2))
            variables['didItFoundTheChar'] = 0
            variables['cppCode'] += "const char* " + variables['charVar1'] + " " + variables['varAssignmentType'] + " " + variables['charVar2'] + Chr(59) + "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 4)== "int ")or(SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 5)== "int8 ")or(SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 6)== "int16 ")or(SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 6)== "int32 "):
        variables['lineDone'] = 1
        if (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 5)== "int8 "):
            variables['varName123Temp'] = StringTrimLeft(variables['A_LoopField17'], 5)
        elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 4)== "int "):
            variables['varName123Temp'] = StringTrimLeft(variables['A_LoopField17'], 4)
        else:
            variables['varName123Temp'] = StringTrimLeft(variables['A_LoopField17'], 6)
        variables['intType'] = Trim(StrSplit(variables['A_LoopField17'] , " " , 1)) + "_t"
        variables['varName'] = StrSplit(variables['varName123Temp'] , " " , 1)
        variables['allVarsInts'] += variables['varName'] + "\n"
        if (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 5)== "int8 "):
            variables['strVar'] = StringTrimLeft(variables['A_LoopField17'], 5)
        elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 4)== "int "):
            variables['strVar'] = StringTrimLeft(variables['A_LoopField17'], 4)
        else:
            variables['strVar'] = StringTrimLeft(variables['A_LoopField17'], 6)
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
            variables['charVar1'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentTypeSplit'] , 1))
            variables['charVar2'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentTypeSplit'] , 2))
            variables['charVar1'] = StrSplit(variables['charVar1'] , " " , 1)
            variables['charVar2'] = varTranspiler(variables['charVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            #MsgBox, % intType
            if (variables['intType'] == "int_t"):
                variables['intType'] = "int"
            variables['cppCode'] += variables['intType'] + " " + variables['charVar1'] + Chr(59) + "\n"
        else:
            variables['charVar1'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentTypeSplit'] , 1))
            variables['charVar2'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentTypeSplit'] , 2))
            variables['charVar1'] = StrSplit(variables['charVar1'] , " " , 1)
            variables['charVar2'] = varTranspiler(variables['charVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            #MsgBox, % intType
            if (variables['intType'] == "int_t"):
                variables['intType'] = "int"
            variables['cppCode'] += variables['intType'] + " " + variables['charVar1'] + " " + variables['varAssignmentType'] + " " + variables['charVar2'] + Chr(59) + "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 4)== "cat "):
        variables['lineDone'] = 1
        variables['strVar'] = StringTrimLeft(variables['A_LoopField17'], 4)
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
            variables['nameOfVar1'] = "variables[" + Chr(34) + variables['nameOfVar11'] + Chr(34) + " + std::string(variables[" + Chr(34) + variables['nameOfVar12'] + Chr(34) + "])]"
            variables['cppCode'] += variables['nameOfVar1'] + Chr(59) + "\n"
        else:
            variables['nameOfVar1'] = Trim(StrSplit(variables['strVar'] , " " , 1))
            variables['nameOfVarSplit'] = StrSplit(variables['strVar'] , " " , 2)
            variables['nameOfVar2'] = Trim(StrSplit(variables['strVar'] , str(variables['nameOfVarSplit']), 2))
            variables['nameOfVar2'] = varTranspiler(variables['nameOfVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            variables['nameOfVar11'] = Trim(StrSplit(variables['nameOfVar1'] , "%" , 1))
            variables['nameOfVar12'] = Trim(StrSplit(variables['nameOfVar1'] , "%" , 2))
            variables['nameOfVar1'] = "variables[" + Chr(34) + variables['nameOfVar11'] + Chr(34) + " + std::string(variables[" + Chr(34) + variables['nameOfVar12'] + Chr(34) + "])]"
            variables['cppCode'] += variables['nameOfVar1'] + " " + variables['varAssignmentType'] + " " + variables['nameOfVar2'] + Chr(59) + "\n"
        variables['lineDone'] = 1
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 4)== StrLower(variables['CheckIFandElsesss1']))or(SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 3)== StrLower(variables['CheckIFandElsesss2']))or(SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 5)== StrLower(variables['CheckIFandElsesss3']))or(SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 4)== StrLower(variables['CheckIFandElsesss4']))or(SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 9)== StrLower(variables['CheckIFandElsesss5']))or(SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 8)== StrLower(variables['CheckIFandElsesss6']))or(SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 10)== StrLower(variables['CheckIFandElsesss7']))or(SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 9)== StrLower(variables['CheckIFandElsesss8'])):
        variables['lineDone'] = 1
        if (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 4)== StrLower(variables['CheckIFandElsesss1'])):
            variables['CheckIFandElsesssNum'] = 4
            variables['CheckIFandElsesssNumNum'] = 1
        if (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 3)== StrLower(variables['CheckIFandElsesss2'])):
            variables['CheckIFandElsesssNum'] = 3
            variables['CheckIFandElsesssNumNum'] = 2
        if (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 5)== StrLower(variables['CheckIFandElsesss3'])):
            variables['CheckIFandElsesssNum'] = 5
            variables['CheckIFandElsesssNumNum'] = 3
        if (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 4)== StrLower(variables['CheckIFandElsesss4'])):
            variables['CheckIFandElsesssNum'] = 4
            variables['CheckIFandElsesssNumNum'] = 4
        if (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 9)== StrLower(variables['CheckIFandElsesss5'])):
            variables['CheckIFandElsesssNum'] = 9
            variables['CheckIFandElsesssNumNum'] = 5
        if (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 8)== StrLower(variables['CheckIFandElsesss6'])):
            variables['CheckIFandElsesssNum'] = 8
            variables['CheckIFandElsesssNumNum'] = 6
        if (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 10)== StrLower(variables['CheckIFandElsesss7'])):
            variables['CheckIFandElsesssNum'] = 10
            variables['CheckIFandElsesssNumNum'] = 7
        if (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 9)== StrLower(variables['CheckIFandElsesss8'])):
            variables['CheckIFandElsesssNum'] = 9
            variables['CheckIFandElsesssNumNum'] = 8
        variables['str123'] = StringTrimLeft(variables['A_LoopField17'], variables['CheckIFandElsesssNum'])
        variables['str123'] = StrReplace(variables['str123'] , "(" , " ( ")
        variables['str123'] = StrReplace(variables['str123'] , ")" , " ) ")
        variables['str123'] = StrReplace(variables['str123'] , "!" , " ! ")
        variables['str123'] = variables[f'CheckIFandElsesss{variables["CheckIFandElsesssNumNum"]}'] + Chr(32) + varTranspiler(variables['str123'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['str123'] = StrReplace(variables['str123'] , "( " , "(")
        variables['str123'] = StrReplace(variables['str123'] , " )" , ")")
        variables['str123'] = StrReplace(variables['str123'] , " ! " , "!")
        variables['str123'] = StrReplace(variables['str123'] , "std::string()" , "")
        variables['str123'] = StrReplace(variables['str123'] , "if " + Chr(40) + Chr(32), "if " + Chr(40))
        variables['out123'] = variables['str123']
        variables['cppCode'] += variables['out123'] + "\n"
    elif (StrLower(variables['A_LoopField17'])== "loop"):
        # infinity loops
        variables['haveWeEverUsedAloop'] = 1
        variables['lineDone'] = 1
        variables['var1'] = "for (int A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " = 1;; A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + "++)"
        variables['nothing'] = ""
        variables['AindexcharLengthStr'] = variables['nothing'] + str(variables['AindexcharLength']) + variables['nothing']
        variables['theFixTextLoopNL'] = "A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + Chr(34) + " = A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + ";"
        variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 1
        variables['pycodeLoopfixa'] += "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength']) + "\n"
        variables['pycodeLoopfixa1'] = "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength'])
        variables['AindexcharLength'] += 1
        variables['cppCode'] += variables['pycodeLoopfixa1'] + "\n" + variables['var1'] + "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 6)== "loop, ")and(SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 8) != "loop, % ")and(SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 7) != "loop % ")and(SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 11) != StrLower("Loop, Parse")):
        variables['str123'] = variables['A_LoopField17']
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
        variables['theFixTextLoopNL'] = "A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " = A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + ";"
        variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 1
        variables['pycodeLoopfixa'] += "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength']) + "\n"
        variables['pycodeLoopfixa1'] = "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength'])
        variables['AindexcharLength'] += 1
        variables['cppCode'] += variables['pycodeLoopfixa1'] + "\n" + variables['var1'] + "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 8)== "loop, % "):
        variables['str123'] = variables['A_LoopField17']
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
        variables['var1'] = "for A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " in range(1, " + variables['line'] + " + 1):"
        variables['nothing'] = ""
        variables['AindexcharLengthStr'] = variables['nothing'] + str(variables['AindexcharLength']) + variables['nothing']
        variables['theFixTextLoopNL'] = "A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " = A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + ";"
        variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 1
        variables['haveWeEverUsedAloop'] = 1
        variables['pycodeLoopfixa'] += "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength']) + "\n"
        variables['pycodeLoopfixa1'] = "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength'])
        variables['AindexcharLength'] += 1
        variables['cppCode'] += variables['pycodeLoopfixa1'] + "\n" + variables['var1'] + "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 13)== StrLower("Loop, Parse, ")):
        #std::vector<std::string> items = LoopParseFunc(variables["var1"], " ");
        variables['lineDone'] = 1
        variables['var1'] = variables['A_LoopField17']
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
        variables['var1out'] = variables['itemsOut'] + "\n" + "for (size_t A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " = 0; A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " < items" + str(variables['AindexcharLength']) + ".size(); A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + "++)"
        variables['nothing'] = ""
        variables['AindexcharLengthStr'] = variables['nothing'] + str(variables['AindexcharLength']) + variables['nothing']
        variables['theFixTextLoopLP'] = "A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " = A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + " + 1;" + "\n" + "std::string A" + Chr(95) + "LoopField" + str(variables['AindexcharLength']) + " = items" + str(variables['AindexcharLength']) + "[A" + Chr(95) + "Index" + str(variables['AindexcharLength']) + "];"
        variables['pycodeAcurlyBraceAddSomeVrasFixLP'] = 1
        variables['haveWeEverUsedAloop'] = 1
        variables['pycodeLoopfixa'] += "lp|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength']) + "\n"
        variables['pycodeLoopfixa1'] = "lp|itsaersdtgtgfergsdgfsegdfsedAA|" + str(variables['AindexcharLength'])
        variables['AindexcharLength'] += 1
        variables['cppCode'] += variables['pycodeLoopfixa1'] + "\n" + variables['var1out'] + "\n"
        variables['lineDone'] = 1
    elif (StrLower(variables['A_LoopField17'])== "break"):
        variables['cppCode'] += variables['A_LoopField17'] + ";\n"
        variables['lineDone'] = 1
    elif (StrLower(variables['A_LoopField17'])== "continue"):
        variables['cppCode'] += variables['A_LoopField17'] + ";\n"
        variables['lineDone'] = 1
    elif (StrLower(variables['A_LoopField17'])== "return")or(SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 7)== "return "):
        if (StrLower(variables['A_LoopField17'])== "return"):
            variables['cppCode'] += variables['A_LoopField17'] + ";\n"
            variables['lineDone'] = 1
        else:
            variables['varTranspiledReturn'] = StringTrimLeft(variables['A_LoopField17'], 7)
            variables['varTranspiledReturn'] = varTranspiler(variables['varTranspiledReturn'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            variables['cppCode'] += "return " + variables['varTranspiledReturn'] + ";\n"
            variables['lineDone'] = 1
    elif (InStr(variables['A_LoopField17'] , " := "))or(InStr(variables['A_LoopField17'] , " .= "))or(InStr(variables['A_LoopField17'] , " += "))or(InStr(variables['A_LoopField17'] , " -= "))or(InStr(variables['A_LoopField17'] , " *= "))or(InStr(variables['A_LoopField17'] , " /= "))and(variables['lineDone'] == 0):
        variables['lineDone'] = 1
        variables['strVar'] = variables['A_LoopField17']
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
    else:
        # this is THE else
        if (variables['removeNextCurlyBraceCpp']  != 1):
            variables['removeNextCurlyBraceCpp'] = 0
            if (variables['skipLeftCuleyForFuncPLS']  != 1):
                if (SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 1)== Chr(125)):
                    variables['cppCode'] += Chr(125) + "\n"
                else:
                    if (variables['pycodeAcurlyBraceAddSomeVrasFixLP'] == 1)and(SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 1)== Chr(123)):
                        variables['pycodeAcurlyBraceAddSomeVrasFixLP'] = 0
                        variables['cppCode'] += variables['A_LoopField17'] + "\n" + variables['theFixTextLoopLP'] + "\n"
                    else:
                        if (variables['pycodeAcurlyBraceAddSomeVrasFixNL'] == 1)and(SubStr(Trim(StrLower(variables['A_LoopField17'])), 1 , 1)== Chr(123)):
                            variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 0
                            variables['cppCode'] += variables['A_LoopField17'] + "\n" + variables['theFixTextLoopNL'] + "\n"
                        else:
                            variables['cppCode'] += variables['A_LoopField17'] + "\n"
            else:
                variables['skipLeftCuleyForFuncPLS'] = 0
        else:
            if (Trim(variables['A_LoopField17'])== "{")and(variables['removeNextCurlyBraceCpp'] == 1):
                variables['removeNextCurlyBraceCpp'] = 0
            else:
                variables['cppCode'] += variables['A_LoopField17'] + "\n"
variables['cppCode'] = StringTrimRight(variables['cppCode'], 1)
#s
if (variables['haveWeEverUsedAloop'] == 1):
    variables['pycodeLoopfixa'] = StringTrimRight(variables['pycodeLoopfixa'], 1)
    #OutputDebug, |%pycodeLoopfixa%|
    variables['AIndexLoopCurlyFix'] = 1
    items = LoopParseFunc(variables['pycodeLoopfixa'], "\n", "\r")
    for A_Index18, A_LoopField18 in enumerate(items, start=1):
        variables['A_Index18'] = A_Index18
        variables['A_LoopField18'] = A_LoopField18
        variables['str123'] = variables['A_LoopField18']
        variables['fixLoopLokingFor'] = variables['A_LoopField18']
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
            for A_Index19, A_LoopField19 in enumerate(items, start=1):
                variables['A_Index19'] = A_Index19
                variables['A_LoopField19'] = A_LoopField19
                #MsgBox, dsfgsdefgesrdg1
                #MsgBox, |%A_LoopField19%|`n|%fixLoopLokingFor%|
                if (InStr(variables['A_LoopField19'] , variables['fixLoopLokingFor']))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['fixLoopLokingForNum'] = 1
                    #MsgBox, do we came here 1
                if (InStr(variables['A_LoopField19'] , "for "))and(variables['weAreDoneHereCurly']  != 1)and(variables['insdeAnestedLoopBAD']  != 1)and(variables['fixLoopLokingForNum'] == 1):
                    variables['s'] = StrSplit(variables['A_LoopField19'] , "A" + Chr(95) + "Index" , 2)
                    variables['out1z'] = variables['s']
                    variables['s'] = StrSplit(variables['out1z'] , " " , 1)
                    variables['out1z'] = Trim(variables['s'])
                    #MsgBox, % out1z
                    #MsgBox, do we came here 2
                    variables['fixLoopLokingForNum'] = 0
                    variables['foundTheTopLoop'] += 1
                    variables['inTarget'] = 1
                    #MsgBox, % A_LoopField19
                    variables['dontSaveStr'] = 1
                    variables['ALoopField'] = variables['A_LoopField19']
                    variables['DeleayOneCuzOfLoopParse'] = 1
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField'] + "\n"
                if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField19'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['insideBracket'] = 1
                if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField19'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['netsedCurly'] += 1
                if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField19'] , Chr(125)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['netsedCurly'] -= 1
                    variables['readyToEnd'] = 1
                if (InStr(variables['A_LoopField19'] , "for "))and(variables['insdeAnestedLoopBAD']  != 1)and(variables['foundTheTopLoop'] >= 2):
                    variables['insdeAnestedLoopBAD'] = 1
                    variables['insideBracket1'] = 0
                    variables['netsedCurly1'] = 0
                if (variables['inTarget'] == 1):
                    variables['foundTheTopLoop'] += 1
                if (variables['insdeAnestedLoopBAD'] == 1):
                    if (InStr(variables['A_LoopField19'] , Chr(123))):
                        variables['insideBracket1'] = 1
                    if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField19'] , Chr(123))):
                        variables['netsedCurly1'] += 1
                    if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField19'] , Chr(125))):
                        variables['netsedCurly1'] -= 1
                        variables['readyToEnd1'] = 1
                    if (InStr(variables['A_LoopField19'] , Chr(125)))and(variables['readyToEnd1'] == 1)and(variables['netsedCurly1'] == 0)and(variables['insideBracket'] == 1):
                        #MsgBox, % A_LoopField19
                        variables['eldLoopNestedBADlol'] = 1
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField19'] + "\n"
                if (variables['inTarget'] == 1)and(variables['dontSaveStr']  != 1)and(variables['fixLoopLokingForNum']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['ALoopField'] = variables['A_LoopField19']
                    # Replace "A_Index" with or without a following digit with "A_Index" + out1z
                    variables['ALoopField'] = RegExReplace(variables['ALoopField'] , "A" + Chr(95) + "Index(?:\\d+)?" , "A" + Chr(95) + "Index" + variables['out1z'])
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField'] + "\n"
                if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField19'] , Chr(125)))and(variables['readyToEnd'] == 1)and(variables['netsedCurly'] == 0)and(variables['weAreDoneHereCurly'] == 0)and(variables['dontSaveStr']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    #MsgBox, % A_LoopField19
                    variables['weAreDoneHereCurly'] = 1
                    variables['inTarget'] = 0
                    variables['endBracketDOntPutThere'] = 1
                variables['dontSaveStr'] = 0
                if (variables['inTarget']  != 1)and(variables['endBracketDOntPutThere']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField19'] + "\n"
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
            for A_Index20, A_LoopField20 in enumerate(items, start=1):
                variables['A_Index20'] = A_Index20
                variables['A_LoopField20'] = A_LoopField20
                if (InStr(variables['A_LoopField20'] , variables['fixLoopLokingFor']))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['fixLoopLokingForNum'] = 1
                    #MsgBox, do we came here 3
                if (InStr(variables['A_LoopField20'] , "for "))and(variables['weAreDoneHereCurly']  != 1)and(variables['insdeAnestedLoopBAD']  != 1)and(variables['fixLoopLokingForNum'] == 1):
                    variables['s'] = StrSplit(variables['A_LoopField20'] , "A" + Chr(95) + "Index" , 2)
                    variables['out1z'] = variables['s']
                    variables['s'] = StrSplit(variables['out1z'] , " " , 1)
                    variables['out1z'] = Trim(variables['s'])
                    #MsgBox, % out1z
                    variables['fixLoopLokingForNum'] = 0
                    #MsgBox, do we came here 4
                    variables['foundTheTopLoop'] += 1
                    variables['inTarget'] = 1
                    #MsgBox, % A_LoopField20
                    variables['dontSaveStr'] = 1
                    variables['ALoopField'] = variables['A_LoopField20']
                    variables['DeleayOneCuzOfLoopParse'] = 1
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField'] + "\n"
                if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField20'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['insideBracket'] = 1
                if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField20'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['netsedCurly'] += 1
                if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField20'] , Chr(125)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['netsedCurly'] -= 1
                    variables['readyToEnd'] = 1
                if (InStr(variables['A_LoopField20'] , "for "))and(variables['insdeAnestedLoopBAD']  != 1)and(variables['foundTheTopLoop'] >= 2):
                    variables['insdeAnestedLoopBAD'] = 1
                    variables['insideBracket1'] = 0
                    variables['netsedCurly1'] = 0
                if (variables['inTarget'] == 1):
                    variables['foundTheTopLoop'] += 1
                if (variables['insdeAnestedLoopBAD'] == 1):
                    if (InStr(variables['A_LoopField20'] , Chr(123))):
                        variables['insideBracket1'] = 1
                    if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField20'] , Chr(123))):
                        variables['netsedCurly1'] += 1
                    if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField20'] , Chr(125))):
                        variables['netsedCurly1'] -= 1
                        variables['readyToEnd1'] = 1
                    if (InStr(variables['A_LoopField20'] , Chr(125)))and(variables['readyToEnd1'] == 1)and(variables['netsedCurly1'] == 0)and(variables['insideBracket'] == 1):
                        #MsgBox, % A_LoopField20
                        variables['eldLoopNestedBADlol'] = 1
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField20'] + "\n"
                if (variables['inTarget'] == 1)and(variables['dontSaveStr']  != 1)and(variables['fixLoopLokingForNum']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['ALoopField'] = variables['A_LoopField20']
                    # Replace "A_Index" with or without a following digit with "A_Index" + out1z
                    variables['ALoopField'] = RegExReplace(variables['ALoopField'] , "A" + Chr(95) + "Index(?:\\d+)?" , "A" + Chr(95) + "Index" + variables['out1z'])
                    # Replace "A_Index" with or without a following digit with "A_Index" + out1z
                    variables['ALoopField'] = RegExReplace(variables['ALoopField'] , "A" + Chr(95) + "LoopField(?:\\d+)?" , "A" + Chr(95) + "LoopField" + variables['out1z'])
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField'] + "\n"
                if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField20'] , Chr(125)))and(variables['readyToEnd'] == 1)and(variables['netsedCurly'] == 0)and(variables['weAreDoneHereCurly'] == 0)and(variables['dontSaveStr']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    #MsgBox, % A_LoopField20
                    variables['weAreDoneHereCurly'] = 1
                    variables['inTarget'] = 0
                    variables['endBracketDOntPutThere'] = 1
                variables['dontSaveStr'] = 0
                if (variables['inTarget']  != 1)and(variables['endBracketDOntPutThere']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField20'] + "\n"
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
    for A_Index21, A_LoopField21 in enumerate(items, start=1):
        variables['A_Index21'] = A_Index21
        variables['A_LoopField21'] = A_LoopField21
        variables['ignore'] = 0
        if (InStr(variables['A_LoopField21'] , "for ")):
            if (variables['hold'] == 1)and(variables['holdText'] == variables['A_LoopField21']):
                variables['ignore'] = 1
            else:
                variables['holdText'] = variables['A_LoopField21']
                variables['hold'] = 1
        if ( not (variables['ignore'])):
            variables['out4758686d86dgt8r754444444'] += variables['A_LoopField21'] + "\n"
    variables['out4758686d86dgt8r754444444'] = StringTrimRight(variables['out4758686d86dgt8r754444444'], 1)
    variables['cppCode'] = variables['out4758686d86dgt8r754444444']
variables['pyCodeOut1234565432'] = ""
items = LoopParseFunc(variables['cppCode'], "\n", "\r")
for A_Index22, A_LoopField22 in enumerate(items, start=1):
    variables['A_Index22'] = A_Index22
    variables['A_LoopField22'] = A_LoopField22
    variables['out'] = variables['A_LoopField22']
    if ( not (InStr(variables['out'] , "|itsaersdtgtgfergsdgfsegdfsedAA|"))):
        variables['pyCodeOut1234565432'] += variables['out'] + "\n"
variables['cppCode'] = StringTrimRight(variables['pyCodeOut1234565432'], 1)
for A_Index23 in range(1, variables['theIdNumOfThe34'] + 1):
    variables['A_Index23'] = A_Index23
    variables['cppCode'] = StrReplace(variables['cppCode'] , "ihuiuuhuuhtheidFor--asas-theuhturtyphoutr-" + Chr(65) + Chr(65) + str(variables['A_Index23']) + Chr(65) + Chr(65), "std::string(" + variables[f'theIdNumOfThe34theVar{variables["A_Index23"]}'] + ")")
variables['cppCodeFixCharRemoveStd'] = ""
items = LoopParseFunc(variables['cppCode'], "\n", "\r")
for A_Index24, A_LoopField24 in enumerate(items, start=1):
    variables['A_Index24'] = A_Index24
    variables['A_LoopField24'] = A_LoopField24
    if (SubStr(Trim(StrLower(variables['A_LoopField24'])), 1 , 12)== "const char* "):
        variables['cppCodeFixCharRemoveStd123'] = variables['A_LoopField24']
        variables['cppCodeFixCharRemoveStd123'] = StrReplace(variables['cppCodeFixCharRemoveStd123'] , "std::string(" , "")
        variables['cppCodeFixCharRemoveStd123'] = StrReplace(variables['cppCodeFixCharRemoveStd123'] , ")" , "")
        variables['cppCodeFixCharRemoveStd'] += variables['cppCodeFixCharRemoveStd123'] + "\n"
    else:
        variables['cppCodeFixCharRemoveStd'] += variables['A_LoopField24'] + "\n"
variables['cppCode'] = StringTrimRight(variables['cppCodeFixCharRemoveStd'], 1)
if (variables['theMainFuncDec'] == 0):
    variables['upCode'] = "\nint main()\n{\n"
variables['uperCode'] = "#include <iostream>\n#include <sstream>\n#include <vector>\n#include <unordered_map>\n#include <string>\n#include <any>\n#include <cstdint>\n#include <regex>\n#include <fstream>\n#include <filesystem>\n#include <cctype>\n#include <algorithm>\n#include <cmath>\n#include <limits>\n#include <chrono>\n\n// Define a map to store dynamic variables\n" + "// Create a map to hold variables\n    std::unordered_map<std::string, std::string> variables;\n"
if (InStr(variables['cppCode'] , "INT("))or(InStr(variables['cppCode'] , "INT (")):
    variables['uperCode'] = variables['uperCode'] + "\n// Convert std::string to int\nint INT(const std::string& str) {\n    std::istringstream iss(str);\n    int value;\n    iss >> value;\n    return value;\n}\n"
if (InStr(variables['cppCode'] , "STR("))or(InStr(variables['cppCode'] , "STR (")):
    variables['uperCode'] = variables['uperCode'] + "\n// Convert various types to std::string\nstd::string STR(int value) {\n    return std::to_string(value);\n}\n\nstd::string STR(float value) {\n    return std::to_string(value);\n}\n\nstd::string STR(double value) {\n    return std::to_string(value);\n}\n\nstd::string STR(size_t value) {\n    return std::to_string(value);\n}\n\nstd::string STR(bool value) {\n    return value ? " + Chr(34) + "1" + Chr(34) + " : " + Chr(34) + "0" + Chr(34) + ";\n}\n"
if (InStr(variables['cppCode'] , "FLOAT("))or(InStr(variables['cppCode'] , "FLOAT (")):
    variables['uperCode'] = variables['uperCode'] + "\n// Convert std::string to float\nfloat FLOAT(const std::string& str) {\n    std::istringstream iss(str);\n    float value;\n    iss >> value;\n    return value;\n}\n"
if (InStr(variables['cppCode'] , "InStr("))or(InStr(variables['cppCode'] , "InStr (")):
    variables['uperCode'] = variables['uperCode'] + "\n// Function to check if needle exists in haystack (std::string overload)\nbool InStr(const std::string& haystack, const std::string& needle) {\n    return haystack.find(needle) != std::string::npos;\n}\n"
if (InStr(variables['cppCode'] , "LoopParseFunc(")):
    variables['uperCode'] = variables['uperCode'] + "\n// Function to escape special characters for regex\nstd::string escapeRegex(const std::string& str) {\n    static const std::regex specialChars{R" + Chr(34) + "([-[\]{}()*+?.,\^$|#\s])" + Chr(34) + "};\n    return std::regex_replace(str, specialChars, R" + Chr(34) + "(\$&)" + Chr(34) + ");\n}\n\n// Function to split a string based on delimiters\nstd::vector<std::string> LoopParseFunc(const std::string& var, const std::string& delimiter1 = " + Chr(34) + "" + Chr(34) + ", const std::string& delimiter2 = " + Chr(34) + "" + Chr(34) + ") {\n    std::vector<std::string> items;\n    if (delimiter1.empty() && delimiter2.empty()) {\n        // If no delimiters are provided, return a list of characters\n        for (char c : var) {\n            items.push_back(std::string(1, c));\n        }\n    } else {\n        // Escape delimiters for regex\n        std::string escapedDelimiters = escapeRegex(delimiter1 + delimiter2);\n        // Construct the regular expression pattern for splitting the string\n        std::string pattern = " + Chr(34) + "[" + Chr(34) + " + escapedDelimiters + " + Chr(34) + "]+" + Chr(34) + ";\n        std::regex regexPattern(pattern);\n        std::sregex_token_iterator iter(var.begin(), var.end(), regexPattern, -1);\n        std::sregex_token_iterator end;\n        while (iter != end) {\n            items.push_back(*iter++);\n        }\n    }\n    return items;\n}\n"
if (InStr(variables['cppCode'] , "print("))or(InStr(variables['cppCode'] , "print (")):
    variables['uperCode'] = variables['uperCode'] + "\n// Print function that converts all types to string if needed\ntemplate <typename T>\nvoid print(const T& value) {\n    if constexpr (std::is_same_v<T, std::string>) {\n        std::cout << value << std::endl;\n    } else if constexpr (std::is_same_v<T, int>) {\n        std::cout << STR(value) << std::endl;\n    } else if constexpr (std::is_same_v<T, float>) {\n        std::cout << STR(value) << std::endl;\n    } else if constexpr (std::is_same_v<T, double>) {\n        std::cout << STR(value) << std::endl;\n    } else if constexpr (std::is_same_v<T, size_t>) {\n        std::cout << STR(value) << std::endl;\n    } else if constexpr (std::is_same_v<T, bool>) {\n        std::cout << STR(value) << std::endl;\n    } else {\n        std::cout << " + Chr(34) + "Unsupported type" + Chr(34) + " << std::endl;\n    }\n}\n"
if (InStr(variables['cppCode'] , "FileRead(")):
    variables['uperCode'] = variables['uperCode'] + "\nstd::string FileRead(const std::string& path) {\n    std::ifstream file;\n    std::filesystem::path full_path;\n\n    // Check if the file path is an absolute path\n    if (std::filesystem::path(path).is_absolute()) {\n        full_path = path;\n    } else {\n        // If it's not a full path, prepend the current working directory\n        full_path = std::filesystem::current_path() / path;\n    }\n\n    // Open the file\n    file.open(full_path);\n    if (!file.is_open()) {\n        throw std::runtime_error(" + Chr(34) + "Error: Could not open the file." + Chr(34) + ");\n    }\n\n    // Read the file content into a string\n    std::string content;\n    std::string line;\n    while (std::getline(file, line)) {\n        content += line + '" + Chr(92) + "n';\n    }\n\n    file.close();\n    return content;\n}\n"
if (InStr(variables['cppCode'] , "FileAppend(")):
    variables['uperCode'] = variables['uperCode'] + "\nbool FileAppend(const std::string& content, const std::string& path) {\n    std::ofstream file;\n\n    // Open the file in append mode\n    file.open(path, std::ios::app);\n\n    if (!file.is_open()) {\n        std::cerr << " + Chr(34) + "Error: Could not open the file for appending." + Chr(34) + " << std::endl;\n        return false;\n    }\n\n    // Append the content to the file\n    file << content;\n\n    // Close the file\n    file.close();\n\n    return true;\n}\n"
if (InStr(variables['cppCode'] , "FileDelete(")):
    variables['uperCode'] = variables['uperCode'] + "\nbool FileDelete(const std::string& path) {\n    std::filesystem::path file_path(path);\n\n    // Check if the file exists\n    if (!std::filesystem::exists(file_path)) {\n        std::cerr << " + Chr(34) + "Error: File does not exist." + Chr(34) + " << std::endl;\n        return false;\n    }\n\n    // Attempt to remove the file\n    if (!std::filesystem::remove(file_path)) {\n        std::cerr << " + Chr(34) + "Error: Failed to delete the file." + Chr(34) + " << std::endl;\n        return false;\n    }\n\n    return true;\n}\n"
#;;;;;;;;;;;;;;
if (InStr(variables['cppCode'] , "SubStr("))or(InStr(variables['cppCode'] , "SubStr (")):
    variables['uperCode'] = variables['uperCode'] + "\n// SubStr function to get a substring with optional length\nstd::string SubStr(const std::string& str, int startPos, int length = -1) {\n    std::string result;\n    size_t strLen = str.size();\n\n    // Handle negative starting positions\n    if (startPos < 0) {\n        startPos += strLen;\n        if (startPos < 0) startPos = 0;\n    } else {\n        if (startPos > static_cast<int>(strLen)) return " + Chr(34) + "" + Chr(34) + "; // Starting position beyond string length\n        startPos -= 1; // Convert to 0-based index\n    }\n\n    // Handle length\n    if (length < 0) {\n        length = strLen - startPos; // Length to end of string\n    } else if (startPos + length > static_cast<int>(strLen)) {\n        length = strLen - startPos; // Adjust length to fit within the string\n    }\n\n    // Extract substring\n    result = str.substr(startPos, length);\n    return result;\n}\n"
if (InStr(variables['cppCode'] , "Trim("))or(InStr(variables['cppCode'] , "Trim (")):
    variables['uperCode'] = variables['uperCode'] + "\n// Function to trim leading and trailing whitespace from a string\nstd::string Trim(const std::string &inputString) {\n    if (inputString.empty()) return " + Chr(34) + "" + Chr(34) + ";\n\n    size_t start = inputString.find_first_not_of(" + Chr(34) + " " + Chr(92) + "t" + Chr(92) + "n" + Chr(92) + "r" + Chr(92) + "f" + Chr(92) + "v" + Chr(34) + ");\n    size_t end = inputString.find_last_not_of(" + Chr(34) + " " + Chr(92) + "t" + Chr(92) + "n" + Chr(92) + "r" + Chr(92) + "f" + Chr(92) + "v" + Chr(34) + ");\n\n    return (start == std::string::npos) ? " + Chr(34) + "" + Chr(34) + " : inputString.substr(start, end - start + 1);\n}\n"
if (InStr(variables['cppCode'] , "StrReplace("))or(InStr(variables['cppCode'] , "StrReplace (")):
    variables['uperCode'] = variables['uperCode'] + "\n// Function to replace all occurrences of a substring with another substring\nstd::string StrReplace(const std::string &originalString, const std::string &find, const std::string &replaceWith) {\n    std::string result = originalString;\n    size_t pos = 0;\n\n    while ((pos = result.find(find, pos)) != std::string::npos) {\n        result.replace(pos, find.length(), replaceWith);\n        pos += replaceWith.length();\n    }\n\n    return result;\n}\n"
if (InStr(variables['cppCode'] , "StringTrimLeft("))or(InStr(variables['cppCode'] , "StringTrimLeft (")):
    variables['uperCode'] = variables['uperCode'] + "\n// Function to trim characters from the left of the string\nstd::string StringTrimLeft(const std::string &input, int numChars) {\n    return (numChars <= input.length()) ? input.substr(numChars) : input;\n}\n"
if (InStr(variables['cppCode'] , "StringTrimRight("))or(InStr(variables['cppCode'] , "StringTrimRight (")):
    variables['uperCode'] = variables['uperCode'] + "\n// Function to trim characters from the right of the string\nstd::string StringTrimRight(const std::string &input, int numChars) {\n    return (numChars <= input.length()) ? input.substr(0, input.length() - numChars) : input;\n}\n"
if (InStr(variables['cppCode'] , "StrLower("))or(InStr(variables['cppCode'] , "StrLower (")):
    variables['uperCode'] = variables['uperCode'] + "\n// Function to convert a string to lowercase\nstd::string StrLower(const std::string &string) {\n    std::string result = string;\n    std::transform(result.begin(), result.end(), result.begin(), ::tolower);\n    return result;\n}\n"
if (InStr(variables['cppCode'] , "RegExReplace("))or(InStr(variables['cppCode'] , "RegExReplace (")):
    variables['uperCode'] = variables['uperCode'] + "\n// Function to perform a regex replacement\nstd::string RegExReplace(const std::string &inputStr, const std::string &regexPattern, const std::string &replacement) {\n    std::regex regex(regexPattern);\n    return std::regex_replace(inputStr, regex, replacement);\n}\n"
if (InStr(variables['cppCode'] , "StrSplit("))or(InStr(variables['cppCode'] , "StrSplit (")):
    variables['uperCode'] = variables['uperCode'] + "\n// Function to split a string by a delimiter and return the nth part\nstd::string StrSplit(const std::string &inputStr, const std::string &delimiter, int num) {\n    size_t start = 0, end = 0, count = 0;\n\n    while ((end = inputStr.find(delimiter, start)) != std::string::npos) {\n        if (++count == num) {\n            return inputStr.substr(start, end - start);\n        }\n        start = end + delimiter.length();\n    }\n\n    if (count + 1 == num) {\n        return inputStr.substr(start);\n    }\n\n    return " + Chr(34) + "" + Chr(34) + ";\n}\n"
if (InStr(variables['cppCode'] , "Chr("))or(InStr(variables['cppCode'] , "Chr (")):
    variables['uperCode'] = variables['uperCode'] + "\n// Function to convert a number to a character\nstd::string Chr(int number) {\n    return (number >= 0 && number <= 0x10FFFF) ? std::string(1, static_cast<char>(number)) : " + Chr(34) + "" + Chr(34) + ";\n}\n"
if (InStr(variables['cppCode'] , "Mod("))or(InStr(variables['cppCode'] , "Mod (")):
    variables['uperCode'] = variables['uperCode'] + "\n// Custom Mod function\nint Mod(int dividend, int divisor) {\n    return dividend % divisor;\n}\n"
if (InStr(variables['cppCode'] , "Floor("))or(InStr(variables['cppCode'] , "Floor (")):
    variables['uperCode'] = variables['uperCode'] + "\ndouble Floor(double num) {\n    if (std::isnan(num)) {\n        return std::numeric_limits<double>::quiet_NaN();\n    }\n    return std::floor(num);\n}\n"
if (InStr(variables['cppCode'] , "A_TickCount("))or(InStr(variables['cppCode'] , "A_TickCount (")):
    variables['uperCode'] = variables['uperCode'] + "\nauto start_timestamp = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch()).count();\n\n// Function to calculate tick count in milliseconds\nstd::string A_TickCount() {\n    auto current_timestamp = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch()).count();\n    return std::to_string(current_timestamp - start_timestamp);\n}\n"
variables['downCode'] = "\nreturn 0;\n}"
variables['cppCode'] = variables['uperCode'] + variables['upCode'] + variables['cppCode'] + variables['downCode']
variables['cppCode'] = StrReplace(variables['cppCode'] , "std::string()" , "")
#MsgBox, % cppCode
variables['filePathOfCode'] = StringTrimRight(variables['filePathOfCode'], 4)
variables['filePathOfCode'] = variables['filePathOfCode'] + "cpp"
FileDelete("" + variables['filePathOfCode'] + "")
FileAppend("" + variables['cppCode'] + "", "" + variables['filePathOfCode'] + "")
