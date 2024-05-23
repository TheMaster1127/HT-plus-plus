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
        if (variables['A_LoopField3'] == Chr(48)) or(variables['A_LoopField3'] == Chr(49)) or(variables['A_LoopField3'] == Chr(50)) or(variables['A_LoopField3'] == Chr(51)) or(variables['A_LoopField3'] == Chr(52)) or(variables['A_LoopField3'] == Chr(53)) or(variables['A_LoopField3'] == Chr(54)) or(variables['A_LoopField3'] == Chr(55)) or(variables['A_LoopField3'] == Chr(56)) or(variables['A_LoopField3'] == Chr(57)) or(variables['A_LoopField3'] == Chr(46)):
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
        variables['nameOfVarr111'] = "variables["  +  Chr(34) +  variables['nameOfVarr11']  +  Chr(34) +  " + convertToStr(variables["  +  Chr(34) +  variables['nameOfVarr12']  +  Chr(34) +  "])]"
        return variables['nameOfVarr111']
    items = LoopParseFunc(variables['allVarsChars'], "\n", "\r")
    for A_Index7, A_LoopField7 in enumerate(items, start=1):
        variables['A_Index7'] = A_Index7
        variables['A_LoopField7'] = A_LoopField7
        if (Trim(variables['varInVarTranspiler'])== Trim(variables['A_LoopField7'])):
            return "std::string("  +  variables['varInVarTranspiler']  +  ")"
    items = LoopParseFunc(variables['allVarsInts'], "\n", "\r")
    for A_Index8, A_LoopField8 in enumerate(items, start=1):
        variables['A_Index8'] = A_Index8
        variables['A_LoopField8'] = A_LoopField8
        if (Trim(variables['varInVarTranspiler'])== Trim(variables['A_LoopField8'])):
            return "std::any("  +  variables['varInVarTranspiler']  +  ")"
    items = LoopParseFunc(variables['funcNames'], "|")
    for A_Index9, A_LoopField9 in enumerate(items, start=1):
        variables['A_Index9'] = A_Index9
        variables['A_LoopField9'] = A_LoopField9
        if (Trim(variables['varInVarTranspiler'])== Trim(variables['A_LoopField9'])):
            return variables['varInVarTranspiler']
    if (varDetect(variables['varInVarTranspiler'])):
        return "variables["  +  Chr(34) +  variables['varInVarTranspiler']  +  Chr(34) +  "]"
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
                variables['varOut2out'] = "convertToInt("  +  variables['varOut2out']  +  ")"
            if (variables['lastType'] == "str"):
                variables['varOut2out'] = "convertToStr("  +  variables['varOut2out']  +  ")"
            variables['var123out'] += str(variables['varOut2out']) +  " "
            variables['typeMode'] = 0
        elif (variables['A_LoopField10']  != "int")and(variables['A_LoopField10']  != "str")and(variables['typeMode'] == 0):
            variables['varInVarTranspiler'] = Trim(variables['A_LoopField10'])
            variables['varOut2out'] = isVarAfuncOrWhat(variables['varInVarTranspiler'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
            variables['var123out'] += str(variables['varOut2out']) +  " "
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
variables['code'] = Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(104) +  Chr(101) +  Chr(108) +  Chr(108) +  Chr(111) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(104) +  Chr(101) +  Chr(108) +  Chr(108) +  Chr(111) +  Chr(32) +  Chr(109) +  Chr(97) +  Chr(110) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(49) +  Chr(50) +  Chr(51) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(49) +  Chr(50) +  Chr(51) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(54) +  Chr(10) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(49) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(53) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(54) +  Chr(10) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(50) +  Chr(50) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(34) +  Chr(104) +  Chr(101) +  Chr(108) +  Chr(108) +  Chr(111) +  Chr(34) +  Chr(10) +  Chr(99) +  Chr(104) +  Chr(97) +  Chr(114) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(50) +  Chr(91) +  Chr(54) +  Chr(93) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(34) +  Chr(104) +  Chr(101) +  Chr(108) +  Chr(108) +  Chr(111) +  Chr(34) +  Chr(10) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(56) +  Chr(32) +  Chr(104) +  Chr(101) +  Chr(108) +  Chr(108) +  Chr(111) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(53) +  Chr(10) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(49) +  Chr(54) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(50) +  Chr(51) +  Chr(52) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(49) +  Chr(53) +  Chr(48) +  Chr(48) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(37) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(50) +  Chr(51) +  Chr(52) +  Chr(10) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(50) +  Chr(51) +  Chr(52) +  Chr(53) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(50) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(34) +  Chr(34) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(49) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(34) +  Chr(32) +  Chr(34) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(32) +  Chr(104) +  Chr(101) +  Chr(108) +  Chr(108) +  Chr(111) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(37) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(50) +  Chr(51) +  Chr(52) +  Chr(53) +  Chr(10) +  Chr(10) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(95) +  Chr(49) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(53) +  Chr(10) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(95) +  Chr(50) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(49) +  Chr(10) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(95) +  Chr(52) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(34) +  Chr(97) +  Chr(119) +  Chr(115) +  Chr(100) +  Chr(101) +  Chr(102) +  Chr(103) +  Chr(104) +  Chr(34) +  Chr(10) +  Chr(99) +  Chr(97) +  Chr(116) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(95) +  Chr(37) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(95) +  Chr(50) +  Chr(37) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(95) +  Chr(52) +  Chr(10) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(37) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(95) +  Chr(37) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(95) +  Chr(50) +  Chr(37) +  Chr(10) +  Chr(10) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(57) +  Chr(57) +  Chr(57) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(95) +  Chr(37) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(95) +  Chr(50) +  Chr(37) +  Chr(10) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(83) +  Chr(83) +  Chr(83) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(57) +  Chr(57) +  Chr(57) +  Chr(10) +  Chr(99) +  Chr(97) +  Chr(116) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(37) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(83) +  Chr(83) +  Chr(83) +  Chr(37) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(95) +  Chr(37) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(95) +  Chr(50) +  Chr(37) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(37) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(37) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(83) +  Chr(83) +  Chr(83) +  Chr(37) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(37) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(57) +  Chr(57) +  Chr(57) +  Chr(10) +  Chr(10) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(107) +  Chr(97) +  Chr(114) +  Chr(49) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(49) +  Chr(48) +  Chr(10) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(107) +  Chr(97) +  Chr(114) +  Chr(50) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(50) +  Chr(48) +  Chr(10) +  Chr(10) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(107) +  Chr(97) +  Chr(114) +  Chr(49) +  Chr(32) +  Chr(62) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(107) +  Chr(97) +  Chr(114) +  Chr(50) +  Chr(41) +  Chr(10) +  Chr(123) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(107) +  Chr(97) +  Chr(114) +  Chr(49) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(98) +  Chr(105) +  Chr(103) +  Chr(103) +  Chr(101) +  Chr(114) +  Chr(10) +  Chr(125) +  Chr(10) +  Chr(101) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(107) +  Chr(97) +  Chr(114) +  Chr(49) +  Chr(32) +  Chr(60) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(107) +  Chr(97) +  Chr(114) +  Chr(50) +  Chr(41) +  Chr(10) +  Chr(123) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(37) +  Chr(32) +  Chr(34) +  Chr(107) +  Chr(97) +  Chr(114) +  Chr(50) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(98) +  Chr(105) +  Chr(103) +  Chr(103) +  Chr(101) +  Chr(114) +  Chr(34) +  Chr(10) +  Chr(125) +  Chr(10) +  Chr(101) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(10) +  Chr(123) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(37) +  Chr(32) +  Chr(34) +  Chr(107) +  Chr(97) +  Chr(114) +  Chr(50) +  Chr(32) +  Chr(97) +  Chr(110) +  Chr(100) +  Chr(32) +  Chr(107) +  Chr(97) +  Chr(114) +  Chr(49) +  Chr(32) +  Chr(97) +  Chr(114) +  Chr(101) +  Chr(32) +  Chr(101) +  Chr(113) +  Chr(117) +  Chr(97) +  Chr(108) +  Chr(34) +  Chr(10) +  Chr(125) +  Chr(10) +  Chr(10) +  Chr(76) +  Chr(111) +  Chr(111) +  Chr(112) +  Chr(44) +  Chr(32) +  Chr(53) +  Chr(10) +  Chr(123) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(37) +  Chr(32) +  Chr(65) +  Chr(95) +  Chr(73) +  Chr(110) +  Chr(100) +  Chr(101) +  Chr(120) +  Chr(10) +  Chr(125) +  Chr(10) +  Chr(10) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(50) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(53) +  Chr(10) +  Chr(76) +  Chr(111) +  Chr(111) +  Chr(112) +  Chr(10) +  Chr(123) +  Chr(10) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(50) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(50) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(49) +  Chr(10) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(50) +  Chr(32) +  Chr(62) +  Chr(32) +  Chr(50) +  Chr(48) +  Chr(41) +  Chr(10) +  Chr(123) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(37) +  Chr(32) +  Chr(34) +  Chr(98) +  Chr(114) +  Chr(101) +  Chr(97) +  Chr(107) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(97) +  Chr(116) +  Chr(32) +  Chr(34) +  Chr(32) +  Chr(46) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(32) +  Chr(65) +  Chr(95) +  Chr(73) +  Chr(110) +  Chr(100) +  Chr(101) +  Chr(120) +  Chr(10) +  Chr(98) +  Chr(114) +  Chr(101) +  Chr(97) +  Chr(107) +  Chr(10) +  Chr(125) +  Chr(10) +  Chr(125) +  Chr(10) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(37) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(114) +  Chr(50) +  Chr(10) +  Chr(10) +  Chr(10) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(106) +  Chr(104) +  Chr(103) +  Chr(105) +  Chr(117) +  Chr(111) +  Chr(32) +  Chr(58) +  Chr(61) +  Chr(32) +  Chr(34) +  Chr(97) +  Chr(115) +  Chr(119) +  Chr(97) +  Chr(101) +  Chr(115) +  Chr(114) +  Chr(100) +  Chr(102) +  Chr(32) +  Chr(119) +  Chr(101) +  Chr(114) +  Chr(115) +  Chr(102) +  Chr(100) +  Chr(102) +  Chr(119) +  Chr(101) +  Chr(115) +  Chr(102) +  Chr(32) +  Chr(100) +  Chr(119) +  Chr(101) +  Chr(32) +  Chr(115) +  Chr(114) +  Chr(102) +  Chr(119) +  Chr(32) +  Chr(97) +  Chr(101) +  Chr(115) +  Chr(102) +  Chr(103) +  Chr(32) +  Chr(101) +  Chr(115) +  Chr(102) +  Chr(100) +  Chr(103) +  Chr(32) +  Chr(119) +  Chr(97) +  Chr(101) +  Chr(115) +  Chr(102) +  Chr(103) +  Chr(96) +  Chr(110) +  Chr(119) +  Chr(101) +  Chr(115) +  Chr(102) +  Chr(100) +  Chr(103) +  Chr(96) +  Chr(114) +  Chr(101) +  Chr(115) +  Chr(114) +  Chr(100) +  Chr(102) +  Chr(103) +  Chr(102) +  Chr(104) +  Chr(103) +  Chr(96) +  Chr(110) +  Chr(119) +  Chr(97) +  Chr(101) +  Chr(115) +  Chr(114) +  Chr(102) +  Chr(100) +  Chr(103) +  Chr(96) +  Chr(110) +  Chr(119) +  Chr(101) +  Chr(114) +  Chr(115) +  Chr(100) +  Chr(116) +  Chr(103) +  Chr(102) +  Chr(34) +  Chr(10) +  Chr(10) +  Chr(76) +  Chr(111) +  Chr(111) +  Chr(112) +  Chr(44) +  Chr(32) +  Chr(80) +  Chr(97) +  Chr(114) +  Chr(115) +  Chr(101) +  Chr(44) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(106) +  Chr(104) +  Chr(103) +  Chr(105) +  Chr(117) +  Chr(111) +  Chr(44) +  Chr(32) +  Chr(96) +  Chr(110) +  Chr(44) +  Chr(32) +  Chr(96) +  Chr(114) +  Chr(10) +  Chr(123) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(37) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(65) +  Chr(95) +  Chr(73) +  Chr(110) +  Chr(100) +  Chr(101) +  Chr(120) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(37) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(32) +  Chr(65) +  Chr(95) +  Chr(76) +  Chr(111) +  Chr(111) +  Chr(112) +  Chr(70) +  Chr(105) +  Chr(101) +  Chr(108) +  Chr(100) +  Chr(10) +  Chr(125) +  Chr(10) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(45) +  Chr(10) +  Chr(10) +  Chr(76) +  Chr(111) +  Chr(111) +  Chr(112) +  Chr(44) +  Chr(32) +  Chr(80) +  Chr(97) +  Chr(114) +  Chr(115) +  Chr(101) +  Chr(44) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(106) +  Chr(104) +  Chr(103) +  Chr(105) +  Chr(117) +  Chr(111) +  Chr(44) +  Chr(32) +  Chr(34) +  Chr(32) +  Chr(34) +  Chr(10) +  Chr(123) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(37) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(65) +  Chr(95) +  Chr(73) +  Chr(110) +  Chr(100) +  Chr(101) +  Chr(120) +  Chr(10) +  Chr(109) +  Chr(115) +  Chr(103) +  Chr(98) +  Chr(111) +  Chr(120) +  Chr(44) +  Chr(32) +  Chr(37) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(32) +  Chr(65) +  Chr(95) +  Chr(76) +  Chr(111) +  Chr(111) +  Chr(112) +  Chr(70) +  Chr(105) +  Chr(101) +  Chr(108) +  Chr(100) +  Chr(10) +  Chr(125)
variables['codeTrimBeggining'] = ""
items = LoopParseFunc(variables['code'], "\n", "\r")
for A_Index11, A_LoopField11 in enumerate(items, start=1):
    variables['A_Index11'] = A_Index11
    variables['A_LoopField11'] = A_LoopField11
    variables['codeTrimBeggining'] += Trim(variables['A_LoopField11']) +  "\n"
variables['code'] = StringTrimRight(variables['codeTrimBeggining'], 1)
variables['HTpyCodeOUT754754'] = ""
variables['areWEinSome34sNum'] = 0
variables['theIdNumOfThe34'] = 0
items = LoopParseFunc(variables['code'])
for A_Index12, A_LoopField12 in enumerate(items, start=1):
    variables['A_Index12'] = A_Index12
    variables['A_LoopField12'] = A_LoopField12
    variables[f'theIdNumOfThe34theVar{variables["A_Index12"]}'] = Chr(34)
items = LoopParseFunc(variables['code'])
for A_Index13, A_LoopField13 in enumerate(items, start=1):
    variables['A_Index13'] = A_Index13
    variables['A_LoopField13'] = A_LoopField13
    if (variables['A_LoopField13'] == Chr(34)):
        variables['areWEinSome34sNum'] += 1
    if (variables['areWEinSome34sNum'] == 1):
        if (variables['A_LoopField13']  != Chr(34)):
            if (variables['A_LoopField13'] == Chr(96)):
                variables[f'theIdNumOfThe34theVar{variables["theIdNumOfThe34"]}'] += Chr(92)
            else:
                variables[f'theIdNumOfThe34theVar{variables["theIdNumOfThe34"]}'] += variables['A_LoopField13']
        else:
            variables['theIdNumOfThe34'] += 1
            variables['HTpyCodeOUT754754'] += "ihuiuuhuuhtheidFor--asas-theuhturtyphoutr-"  +  Chr(65) +  Chr(65) +  str(variables['theIdNumOfThe34']) +  Chr(65) +  Chr(65)
    if (variables['areWEinSome34sNum'] == 2)or(variables['areWEinSome34sNum'] == 0):
        if (variables['A_LoopField13']  != Chr(34)):
            variables['HTpyCodeOUT754754'] += variables['A_LoopField13']
        variables['areWEinSome34sNum'] = 0
variables['code'] = variables['HTpyCodeOUT754754']
for A_Index14 in range(1, variables['theIdNumOfThe34'] + 1):
    variables['A_Index14'] = A_Index14
    variables[f'theIdNumOfThe34theVar{variables["A_Index14"]}'] += Chr(34)
variables['allVarsChars'] = ""
variables['allVarsInts'] = ""
variables['funcNames'] = "InStr|convertToStr|convertToInt"
variables['cppCode'] = ""
items = LoopParseFunc(variables['code'], "\n", "\r")
for A_Index15, A_LoopField15 in enumerate(items, start=1):
    variables['A_Index15'] = A_Index15
    variables['A_LoopField15'] = A_LoopField15
    if (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 10)== "msgbox, % "):
        variables['msgboxCode'] = StringTrimLeft(variables['A_LoopField15'], 10)
        variables['msgboxCode'] = varTranspiler(variables['msgboxCode'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['cppCode'] += "print("  +  variables['msgboxCode']  +  ");"  +  "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 8)== "msgbox, "):
        variables['msgboxCode'] = StringTrimLeft(variables['A_LoopField15'], 8)
        variables['cppCode'] += "print(std::string("  +  Chr(34) +  variables['msgboxCode']  +  Chr(34) +  "));"  +  "\n"
    elif (SubStr(variables['A_LoopField15'] , -1)== "++"):
        variables['str123'] = Trim(variables['A_LoopField15'])
        variables['str123'] = StringTrimRight(variables['str123'], 2)
        variables['out'] = "variables["  +  Chr(34) +  variables['str123']  +  Chr(34) +  "] = convertToInt(variables["  +  Chr(34) +  variables['str123']  +  Chr(34) +  "]) + 1;"
        variables['cppCode'] += variables['out']  +  "\n"
    elif (SubStr(variables['A_LoopField15'] , -1)== "--"):
        variables['str123'] = Trim(variables['A_LoopField15'])
        variables['str123'] = StringTrimRight(variables['str123'], 2)
        variables['out'] = "variables["  +  Chr(34) +  variables['str123']  +  Chr(34) +  "] = convertToInt(variables["  +  Chr(34) +  variables['str123']  +  Chr(34) +  "]) - 1;"
        variables['cppCode'] += variables['out']  +  "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 4)== "int "):
        variables['intVar'] = StringTrimLeft(variables['A_LoopField15'], 4)
        variables['intVar'] = Trim(variables['intVar'])
        if (InStr(variables['intVar'] , " := ")):
            variables['varAssignmentType'] = "="
        if (InStr(variables['intVar'] , " += ")):
            variables['varAssignmentType'] = "+="
        if (InStr(variables['intVar'] , " .= ")):
            variables['varAssignmentType'] = "+="
        if (InStr(variables['intVar'] , " -= ")):
            variables['varAssignmentType'] = "-="
        if (InStr(variables['intVar'] , " *= ")):
            variables['varAssignmentType'] = "*="
        if (InStr(variables['intVar'] , " /= ")):
            variables['varAssignmentType'] = "/="
        variables['nameOfVar1'] = Trim(StrSplit(variables['intVar'] , " " , 1))
        variables['nameOfVarSplit'] = Trim(StrSplit(variables['intVar'] , " " , 2))
        variables['nameOfVar2'] = Trim(StrSplit(variables['intVar'] , variables['nameOfVarSplit'] , 2))
        variables['nameOfVar2'] = varTranspiler(variables['nameOfVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['cppCode'] += "variables["  +  Chr(34) +  variables['nameOfVar1']  +  Chr(34) +  "]"  +  " "  +  variables['varAssignmentType']  +  " "  +  variables['nameOfVar2']  +  Chr(59) +  "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 4)== "str "):
        variables['strVar'] = StringTrimLeft(variables['A_LoopField15'], 4)
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
        variables['nameOfVarSplit'] = Trim(StrSplit(variables['strVar'] , " " , 2))
        variables['nameOfVar2'] = Trim(StrSplit(variables['strVar'] , variables['nameOfVarSplit'] , 2))
        variables['nameOfVar2'] = varTranspiler(variables['nameOfVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['cppCode'] += "variables["  +  Chr(34) +  variables['nameOfVar1']  +  Chr(34) +  "]"  +  " "  +  variables['varAssignmentType']  +  " "  +  variables['nameOfVar2']  +  Chr(59) +  "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 5)== "char "):
        variables['varName123Temp'] = StringTrimLeft(variables['A_LoopField15'], 5)
        variables['varName'] = StrSplit(variables['varName123Temp'] , "[" , 1)
        variables['allVarsChars'] += Trim(variables['varName']) +  "\n"
        variables['strVar'] = StringTrimLeft(variables['A_LoopField15'], 5)
        variables['strVar'] = Trim(variables['strVar'])
        if (InStr(variables['strVar'] , " := ")):
            variables['varAssignmentTypeSplit'] = " := "
            variables['varAssignmentType'] = "="
        if (InStr(variables['strVar'] , " += ")):
            variables['varAssignmentTypeSplit'] = " += "
            variables['varAssignmentType'] = "+="
        if (InStr(variables['strVar'] , " .= ")):
            variables['varAssignmentTypeSplit'] = " .= "
            variables['varAssignmentType'] = "+="
        if (InStr(variables['strVar'] , " -= ")):
            variables['varAssignmentTypeSplit'] = " -= "
            variables['varAssignmentType'] = "-="
        if (InStr(variables['strVar'] , " *= ")):
            variables['varAssignmentTypeSplit'] = " *= "
            variables['varAssignmentType'] = "*="
        if (InStr(variables['strVar'] , " /= ")):
            variables['varAssignmentTypeSplit'] = " /= "
            variables['varAssignmentType'] = "/="
        variables['charVar1'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentTypeSplit'] , 1))
        variables['charVar2'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentTypeSplit'] , 2))
        variables['cppCode'] += "char "  +  variables['charVar1']  +  " "  +  variables['varAssignmentType']  +  " "  +  variables['charVar2']  +  Chr(59) +  "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 5)== "int8 ")or(SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 6)== "int16 ")or(SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 6)== "int32 ")or(SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 6)== "int64 "):
        if (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 5)== "int8 "):
            variables['varName123Temp'] = StringTrimLeft(variables['A_LoopField15'], 5)
        else:
            variables['varName123Temp'] = StringTrimLeft(variables['A_LoopField15'], 6)
        variables['intType'] = Trim(StrSplit(variables['A_LoopField15'] , " " , 1))  +  "_t"
        variables['varName'] = StrSplit(variables['varName123Temp'] , " " , 1)
        variables['allVarsInts'] += variables['varName']  +  "\n"
        if (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 5)== "int8 "):
            variables['strVar'] = StringTrimLeft(variables['A_LoopField15'], 5)
        else:
            variables['strVar'] = StringTrimLeft(variables['A_LoopField15'], 6)
        variables['strVar'] = Trim(variables['strVar'])
        if (InStr(variables['strVar'] , " := ")):
            variables['varAssignmentTypeSplit'] = " := "
            variables['varAssignmentType'] = "="
        if (InStr(variables['strVar'] , " += ")):
            variables['varAssignmentTypeSplit'] = " += "
            variables['varAssignmentType'] = "+="
        if (InStr(variables['strVar'] , " .= ")):
            variables['varAssignmentTypeSplit'] = " .= "
            variables['varAssignmentType'] = "+="
        if (InStr(variables['strVar'] , " -= ")):
            variables['varAssignmentTypeSplit'] = " -= "
            variables['varAssignmentType'] = "-="
        if (InStr(variables['strVar'] , " *= ")):
            variables['varAssignmentTypeSplit'] = " *= "
            variables['varAssignmentType'] = "*="
        if (InStr(variables['strVar'] , " /= ")):
            variables['varAssignmentTypeSplit'] = " /= "
            variables['varAssignmentType'] = "/="
        variables['charVar1'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentTypeSplit'] , 1))
        variables['charVar2'] = Trim(StrSplit(variables['strVar'] , variables['varAssignmentTypeSplit'] , 2))
        variables['charVar1'] = StrSplit(variables['charVar1'] , " " , 1)
        variables['cppCode'] += variables['intType']  +  " "  +  variables['charVar1']  +  " "  +  variables['varAssignmentType']  +  " "  +  variables['charVar2']  +  Chr(59) +  "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 4)== "cat "):
        variables['strVar'] = StringTrimLeft(variables['A_LoopField15'], 4)
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
        variables['nameOfVarSplit'] = Trim(StrSplit(variables['strVar'] , " " , 2))
        variables['nameOfVar2'] = Trim(StrSplit(variables['strVar'] , variables['nameOfVarSplit'] , 2))
        variables['nameOfVar2'] = varTranspiler(variables['nameOfVar2'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['nameOfVar11'] = Trim(StrSplit(variables['nameOfVar1'] , "%" , 1))
        variables['nameOfVar12'] = Trim(StrSplit(variables['nameOfVar1'] , "%" , 2))
        variables['nameOfVar1'] = "variables["  +  Chr(34) +  variables['nameOfVar11']  +  Chr(34) +  " + convertToStr(variables["  +  Chr(34) +  variables['nameOfVar12']  +  Chr(34) +  "])]"
        variables['cppCode'] += variables['nameOfVar1']  +  " "  +  variables['varAssignmentType']  +  " "  +  variables['nameOfVar2']  +  Chr(59) +  "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 4)== StrLower(variables['CheckIFandElsesss1'])) or(SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 3)== StrLower(variables['CheckIFandElsesss2'])) or(SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 5)== StrLower(variables['CheckIFandElsesss3'])) or(SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 4)== StrLower(variables['CheckIFandElsesss4'])) or(SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 9)== StrLower(variables['CheckIFandElsesss5'])) or(SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 8)== StrLower(variables['CheckIFandElsesss6'])) or(SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 10)== StrLower(variables['CheckIFandElsesss7'])) or(SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 9)== StrLower(variables['CheckIFandElsesss8'])):
        if (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 4)== StrLower(variables['CheckIFandElsesss1'])):
            variables['CheckIFandElsesssNum'] = 4
            variables['CheckIFandElsesssNumNum'] = 1
        if (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 3)== StrLower(variables['CheckIFandElsesss2'])):
            variables['CheckIFandElsesssNum'] = 3
            variables['CheckIFandElsesssNumNum'] = 2
        if (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 5)== StrLower(variables['CheckIFandElsesss3'])):
            variables['CheckIFandElsesssNum'] = 5
            variables['CheckIFandElsesssNumNum'] = 3
        if (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 4)== StrLower(variables['CheckIFandElsesss4'])):
            variables['CheckIFandElsesssNum'] = 4
            variables['CheckIFandElsesssNumNum'] = 4
        if (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 9)== StrLower(variables['CheckIFandElsesss5'])):
            variables['CheckIFandElsesssNum'] = 9
            variables['CheckIFandElsesssNumNum'] = 5
        if (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 8)== StrLower(variables['CheckIFandElsesss6'])):
            variables['CheckIFandElsesssNum'] = 8
            variables['CheckIFandElsesssNumNum'] = 6
        if (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 10)== StrLower(variables['CheckIFandElsesss7'])):
            variables['CheckIFandElsesssNum'] = 10
            variables['CheckIFandElsesssNumNum'] = 7
        if (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 9)== StrLower(variables['CheckIFandElsesss8'])):
            variables['CheckIFandElsesssNum'] = 9
            variables['CheckIFandElsesssNumNum'] = 8
        variables['str123'] = StringTrimLeft(variables['A_LoopField15'], variables['CheckIFandElsesssNum'])
        variables['str123'] = StrReplace(variables['str123'] , "(" , " ( ")
        variables['str123'] = StrReplace(variables['str123'] , ")" , " ) ")
        variables['str123'] = StrReplace(variables['str123'] , "!" , " ! ")
        variables['str123'] = variables[f'CheckIFandElsesss{variables["CheckIFandElsesssNumNum"]}']  +  Chr(32) +  varTranspiler(variables['str123'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['str123'] = StrReplace(variables['str123'] , "( " , "(")
        variables['str123'] = StrReplace(variables['str123'] , " )" , ")")
        variables['str123'] = StrReplace(variables['str123'] , " ! " , "!")
        variables['str123'] = StrReplace(variables['str123'] , "std::string()" , "")
        variables['str123'] = StrReplace(variables['str123'] , "if "  +  Chr(40) +  Chr(32), "if "  +  Chr(40))
        variables['out123'] = variables['str123']
        variables['cppCode'] += variables['out123']  +  "\n"
    elif (StrLower(variables['A_LoopField15'])== "loop"):
        # infinity loops
        variables['haveWeEverUsedAloop'] = 1
        variables['lineDone'] = 1
        variables['var1'] = "for (int A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  " = 1;; A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  "++)"
        variables['nothing'] = ""
        variables['AindexcharLengthStr'] = variables['nothing']  +  str(variables['AindexcharLength']) +  variables['nothing']
        variables['theFixTextLoopNL'] = "variables["  +  Chr(34) +  "A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  Chr(34) +  "] = A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  ";"
        variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 1
        variables['pycodeLoopfixa'] += "nl|itsaersdtgtgfergsdgfsegdfsedAA|"  +  str(variables['AindexcharLength']) +  "\n"
        variables['pycodeLoopfixa1'] = "nl|itsaersdtgtgfergsdgfsegdfsedAA|"  +  str(variables['AindexcharLength'])
        variables['AindexcharLength'] += 1
        variables['cppCode'] += variables['pycodeLoopfixa1']  +  "\n"  +  variables['var1']  +  "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 6)== "loop, ")and(SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 8) != "loop, % ")and(SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 7) != "loop % ")and(SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 11) != StrLower("Loop, Parse")):
        variables['str123'] = variables['A_LoopField15']
        #MsgBox, % str123
        variables['out2'] = StringTrimLeft(variables['str123'], 6)
        #MsgBox % out2
        #MsgBox, % out2
        variables['out2'] = Trim(variables['out2'])
        variables['myVar'] = variables['out2']
        variables['lineYGI'] = varTranspiler(variables['myVar'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['line'] = variables['lineYGI']
        variables['haveWeEverUsedAloop'] = 1
        #MsgBox, % line
        variables['var1'] = "for (int A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  " = 1; A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  "<= "  +  variables['line']  + "; ++A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  ")"
        variables['nothing'] = ""
        variables['AindexcharLengthStr'] = variables['nothing']  +  str(variables['AindexcharLength']) +  variables['nothing']
        variables['theFixTextLoopNL'] = "variables["  +  Chr(34) +  "A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  Chr(34) +  "] = A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  ";"
        variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 1
        variables['pycodeLoopfixa'] += "nl|itsaersdtgtgfergsdgfsegdfsedAA|"  +  str(variables['AindexcharLength']) +  "\n"
        variables['pycodeLoopfixa1'] = "nl|itsaersdtgtgfergsdgfsegdfsedAA|"  +  str(variables['AindexcharLength'])
        variables['AindexcharLength'] += 1
        variables['cppCode'] += variables['pycodeLoopfixa1']  +  "\n"  +  variables['var1']  +  "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 8)== "loop, % "):
        variables['str123'] = variables['A_LoopField15']
        #MsgBox, % str123
        variables['out2'] = StringTrimLeft(variables['str123'], 8)
        #MsgBox % out2
        #MsgBox, % out2
        variables['out2'] = Trim(variables['out2'])
        variables['myVar'] = variables['out2']
        variables['lineYGI'] = varTranspiler(variables['myVar'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['line'] = variables['lineYGI']
        #MsgBox, % line
        variables['var1'] = "for A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  " in range(1, "  +  variables['line']  +  " + 1):"
        variables['nothing'] = ""
        variables['AindexcharLengthStr'] = variables['nothing']  +  str(variables['AindexcharLength']) +  variables['nothing']
        variables['theFixTextLoopNL'] = "variables["  +  Chr(34) +  "A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  Chr(34) +  "] = A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  ";"
        variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 1
        variables['haveWeEverUsedAloop'] = 1
        variables['pycodeLoopfixa'] += "nl|itsaersdtgtgfergsdgfsegdfsedAA|"  +  str(variables['AindexcharLength']) +  "\n"
        variables['pycodeLoopfixa1'] = "nl|itsaersdtgtgfergsdgfsegdfsedAA|"  +  str(variables['AindexcharLength'])
        variables['AindexcharLength'] += 1
        variables['cppCode'] += variables['pycodeLoopfixa1']  +  "\n"  +  variables['var1']  +  "\n"
    elif (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 13)== StrLower("Loop, Parse, ")):
        #std::vector<std::string> items = LoopParseFunc(variables["var1"], " ");
        variables['var1'] = variables['A_LoopField15']
        variables['var1'] = Trim(variables['var1'])
        variables['var1'] = StringTrimLeft(variables['var1'], 13)
        variables['line1'] = Trim(StrSplit(variables['var1'] , "," , 1))
        variables['line1'] = varTranspiler(variables['line1'] , variables['funcNames'] , variables['allVarsChars'] , variables['allVarsInts'])
        variables['line2'] = ""
        variables['line3'] = ""
        variables['itemsOut'] = ""
        variables['line2'] = Trim(StrSplit(variables['var1'] , "," , 2))
        variables['line3'] = Trim(StrSplit(variables['var1'] , "," , 3))
        if (InStr(variables['var1'] , Chr(96) +  ",")):
            variables['line2'] = Chr(34) +  ","  +  Chr(34)
            variables['itemsOut'] = "std::vector<std::string> items"  +  str(variables['AindexcharLength']) +  " = LoopParseFunc(convertToStr("  +  variables['line1']  +  "), "  +  variables['line2']  +  ");"
        else:
            if (variables['line2'] == "")and(variables['line3'] == ""):
                # nothing so only each char
                variables['itemsOut'] = "std::vector<std::string> items"  +  str(variables['AindexcharLength']) +  " = LoopParseFunc(convertToStr("  +  variables['line1']  +  "));"
            if (variables['line2']  != "")and(variables['line3'] == ""):
                if (InStr(variables['line2'] , Chr(96))):
                    variables['line2'] = Chr(34) +  variables['line2']  +  Chr(34)
                variables['itemsOut'] = "std::vector<std::string> items"  +  str(variables['AindexcharLength']) +  " = LoopParseFunc(convertToStr("  +  variables['line1']  +  "), "  +  variables['line2']  +  ");"
            if (variables['line2']  != "")and(variables['line3']  != ""):
                if (InStr(variables['line2'] , Chr(96))):
                    variables['line2'] = Chr(34) +  variables['line2']  +  Chr(34)
                if (InStr(variables['line3'] , Chr(96))):
                    variables['line3'] = Chr(34) +  variables['line3']  +  Chr(34)
                variables['itemsOut'] = "std::vector<std::string> items"  +  str(variables['AindexcharLength']) +  " = LoopParseFunc(convertToStr("  +  variables['line1']  +  "), "  +  variables['line2']  +  ", "  +  variables['line3']  +  ");"
            variables['itemsOut'] = StrReplace(variables['itemsOut'] , Chr(96), Chr(92))
        #for (size_t A_Index1 = 0; A_Index1 < items.size(); A_Index1++)
        variables['var1out'] = variables['itemsOut']  +  "\n"  +  "for (size_t A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  " = 0; A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  " < items"  +  str(variables['AindexcharLength']) +  ".size(); A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  "++)"
        variables['nothing'] = ""
        variables['AindexcharLengthStr'] = variables['nothing']  +  str(variables['AindexcharLength']) +  variables['nothing']
        variables['theFixTextLoopLP'] = "variables["  +  Chr(34) +  "A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  Chr(34) +  "] = std::to_string(A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  " + 1);"  +  "\n"  +  "variables["  +  Chr(34) +  "A"  +  Chr(95) +  "LoopField"  +  str(variables['AindexcharLength']) +  Chr(34) +  "] = items"  +  str(variables['AindexcharLength']) +  "[A"  +  Chr(95) +  "Index"  +  str(variables['AindexcharLength']) +  "];"
        variables['pycodeAcurlyBraceAddSomeVrasFixLP'] = 1
        variables['haveWeEverUsedAloop'] = 1
        variables['pycodeLoopfixa'] += "lp|itsaersdtgtgfergsdgfsegdfsedAA|"  +  str(variables['AindexcharLength']) +  "\n"
        variables['pycodeLoopfixa1'] = "lp|itsaersdtgtgfergsdgfsegdfsedAA|"  +  str(variables['AindexcharLength'])
        variables['AindexcharLength'] += 1
        variables['cppCode'] += variables['pycodeLoopfixa1']  +  "\n"  +  variables['var1out']  +  "\n"
    elif (StrLower(variables['A_LoopField15'])== "break"):
        variables['cppCode'] += variables['A_LoopField15']  +  ";\n"
    else:
        # this is THE else
        if (variables['skipLeftCuleyForFuncPLS']  != 1):
            if (SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 1)== Chr(125)):
                variables['cppCode'] += Chr(125) +  "\n"
            else:
                if (variables['pycodeAcurlyBraceAddSomeVrasFixLP'] == 1)and(SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 1)== Chr(123)):
                    variables['pycodeAcurlyBraceAddSomeVrasFixLP'] = 0
                    variables['cppCode'] += variables['A_LoopField15']  +  "\n"  +  variables['theFixTextLoopLP']  +  "\n"
                else:
                    if (variables['pycodeAcurlyBraceAddSomeVrasFixNL'] == 1)and(SubStr(Trim(StrLower(variables['A_LoopField15'])) , 1 , 1)== Chr(123)):
                        variables['pycodeAcurlyBraceAddSomeVrasFixNL'] = 0
                        variables['cppCode'] += variables['A_LoopField15']  +  "\n"  +  variables['theFixTextLoopNL']  +  "\n"
                    else:
                        variables['cppCode'] += variables['A_LoopField15']  +  "\n"
        else:
            variables['skipLeftCuleyForFuncPLS'] = 0
variables['cppCode'] = StringTrimRight(variables['cppCode'], 1)
#s
if (variables['haveWeEverUsedAloop'] == 1):
    variables['pycodeLoopfixa'] = StringTrimRight(variables['pycodeLoopfixa'], 1)
    #OutputDebug, |%pycodeLoopfixa%|
    variables['AIndexLoopCurlyFix'] = 1
    items = LoopParseFunc(variables['pycodeLoopfixa'], "\n", "\r")
    for A_Index16, A_LoopField16 in enumerate(items, start=1):
        variables['A_Index16'] = A_Index16
        variables['A_LoopField16'] = A_LoopField16
        variables['str123'] = variables['A_LoopField16']
        variables['fixLoopLokingFor'] = variables['A_LoopField16']
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
            for A_Index17, A_LoopField17 in enumerate(items, start=1):
                variables['A_Index17'] = A_Index17
                variables['A_LoopField17'] = A_LoopField17
                #MsgBox, dsfgsdefgesrdg1
                #MsgBox, |%A_LoopField17%|`n|%fixLoopLokingFor%|
                if (InStr(variables['A_LoopField17'] , variables['fixLoopLokingFor'])) and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['fixLoopLokingForNum'] = 1
                    #MsgBox, do we came here 1
                if (InStr(variables['A_LoopField17'] , "for ")) and(variables['weAreDoneHereCurly']  != 1)and(variables['insdeAnestedLoopBAD']  != 1)and(variables['fixLoopLokingForNum'] == 1):
                    variables['s'] = StrSplit(variables['A_LoopField17'] , "A"  +  Chr(95) +  "Index" , 2)
                    variables['out1z'] = variables['s']
                    variables['s'] = StrSplit(variables['out1z'] , " " , 1)
                    variables['out1z'] = Trim(variables['s'])
                    #MsgBox, % out1z
                    #MsgBox, do we came here 2
                    variables['fixLoopLokingForNum'] = 0
                    variables['foundTheTopLoop'] += 1
                    variables['inTarget'] = 1
                    #MsgBox, % A_LoopField17
                    variables['dontSaveStr'] = 1
                    variables['ALoopField'] = variables['A_LoopField17']
                    variables['DeleayOneCuzOfLoopParse'] = 1
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField']  +  "\n"
                if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField17'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['insideBracket'] = 1
                if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField17'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['netsedCurly'] += 1
                if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField17'] , Chr(125)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['netsedCurly'] -= 1
                    variables['readyToEnd'] = 1
                if (InStr(variables['A_LoopField17'] , "for ")) and(variables['insdeAnestedLoopBAD']  != 1)and(variables['foundTheTopLoop'] >= 2):
                    variables['insdeAnestedLoopBAD'] = 1
                    variables['insideBracket1'] = 0
                    variables['netsedCurly1'] = 0
                if (variables['inTarget'] == 1):
                    variables['foundTheTopLoop'] += 1
                if (variables['insdeAnestedLoopBAD'] == 1):
                    if (InStr(variables['A_LoopField17'] , Chr(123))):
                        variables['insideBracket1'] = 1
                    if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField17'] , Chr(123))):
                        variables['netsedCurly1'] += 1
                    if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField17'] , Chr(125))):
                        variables['netsedCurly1'] -= 1
                        variables['readyToEnd1'] = 1
                    if (InStr(variables['A_LoopField17'] , Chr(125)))and(variables['readyToEnd1'] == 1)and(variables['netsedCurly1'] == 0)and(variables['insideBracket'] == 1):
                        #MsgBox, % A_LoopField17
                        variables['eldLoopNestedBADlol'] = 1
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField17']  +  "\n"
                if (variables['inTarget'] == 1)and(variables['dontSaveStr']  != 1)and(variables['fixLoopLokingForNum']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['ALoopField'] = variables['A_LoopField17']
                    # Replace "A_Index" with or without a following digit with "A_Index" + out1z
                    variables['ALoopField'] = RegExReplace(variables['ALoopField'] , "A"  +  Chr(95) +  "Index(?:\\d+)?" , "A"  +  Chr(95) +  "Index"  +  variables['out1z'])
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField']  +  "\n"
                if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField17'] , Chr(125)))and(variables['readyToEnd'] == 1)and(variables['netsedCurly'] == 0)and(variables['weAreDoneHereCurly'] == 0)and(variables['dontSaveStr']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    #MsgBox, % A_LoopField17
                    variables['weAreDoneHereCurly'] = 1
                    variables['inTarget'] = 0
                    variables['endBracketDOntPutThere'] = 1
                variables['dontSaveStr'] = 0
                if (variables['inTarget']  != 1)and(variables['endBracketDOntPutThere']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField17']  +  "\n"
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
            for A_Index18, A_LoopField18 in enumerate(items, start=1):
                variables['A_Index18'] = A_Index18
                variables['A_LoopField18'] = A_LoopField18
                if (InStr(variables['A_LoopField18'] , variables['fixLoopLokingFor'])) and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['fixLoopLokingForNum'] = 1
                    #MsgBox, do we came here 3
                if (InStr(variables['A_LoopField18'] , "for ")) and(variables['weAreDoneHereCurly']  != 1)and(variables['insdeAnestedLoopBAD']  != 1)and(variables['fixLoopLokingForNum'] == 1):
                    variables['s'] = StrSplit(variables['A_LoopField18'] , "A"  +  Chr(95) +  "Index" , 2)
                    variables['out1z'] = variables['s']
                    variables['s'] = StrSplit(variables['out1z'] , " " , 1)
                    variables['out1z'] = Trim(variables['s'])
                    #MsgBox, % out1z
                    variables['fixLoopLokingForNum'] = 0
                    #MsgBox, do we came here 4
                    variables['foundTheTopLoop'] += 1
                    variables['inTarget'] = 1
                    #MsgBox, % A_LoopField18
                    variables['dontSaveStr'] = 1
                    variables['ALoopField'] = variables['A_LoopField18']
                    variables['DeleayOneCuzOfLoopParse'] = 1
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField']  +  "\n"
                if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField18'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['insideBracket'] = 1
                if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField18'] , Chr(123)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['netsedCurly'] += 1
                if (variables['insideBracket'] == 1)and(InStr(variables['A_LoopField18'] , Chr(125)))and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['netsedCurly'] -= 1
                    variables['readyToEnd'] = 1
                if (InStr(variables['A_LoopField18'] , "for ")) and(variables['insdeAnestedLoopBAD']  != 1)and(variables['foundTheTopLoop'] >= 2):
                    variables['insdeAnestedLoopBAD'] = 1
                    variables['insideBracket1'] = 0
                    variables['netsedCurly1'] = 0
                if (variables['inTarget'] == 1):
                    variables['foundTheTopLoop'] += 1
                if (variables['insdeAnestedLoopBAD'] == 1):
                    if (InStr(variables['A_LoopField18'] , Chr(123))):
                        variables['insideBracket1'] = 1
                    if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField18'] , Chr(123))):
                        variables['netsedCurly1'] += 1
                    if (variables['insideBracket1'] == 1)and(InStr(variables['A_LoopField18'] , Chr(125))):
                        variables['netsedCurly1'] -= 1
                        variables['readyToEnd1'] = 1
                    if (InStr(variables['A_LoopField18'] , Chr(125)))and(variables['readyToEnd1'] == 1)and(variables['netsedCurly1'] == 0)and(variables['insideBracket'] == 1):
                        #MsgBox, % A_LoopField18
                        variables['eldLoopNestedBADlol'] = 1
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField18']  +  "\n"
                if (variables['inTarget'] == 1)and(variables['dontSaveStr']  != 1)and(variables['fixLoopLokingForNum']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    variables['ALoopField'] = variables['A_LoopField18']
                    # Replace "A_Index" with or without a following digit with "A_Index" + out1z
                    variables['ALoopField'] = RegExReplace(variables['ALoopField'] , "A"  +  Chr(95) +  "Index(?:\\d+)?" , "A"  +  Chr(95) +  "Index"  +  variables['out1z'])
                    # Replace "A_Index" with or without a following digit with "A_Index" + out1z
                    variables['ALoopField'] = RegExReplace(variables['ALoopField'] , "A"  +  Chr(95) +  "LoopField(?:\\d+)?" , "A"  +  Chr(95) +  "LoopField"  +  variables['out1z'])
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['ALoopField']  +  "\n"
                if (variables['inTarget'] == 1)and(InStr(variables['A_LoopField18'] , Chr(125)))and(variables['readyToEnd'] == 1)and(variables['netsedCurly'] == 0)and(variables['weAreDoneHereCurly'] == 0)and(variables['dontSaveStr']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    #MsgBox, % A_LoopField18
                    variables['weAreDoneHereCurly'] = 1
                    variables['inTarget'] = 0
                    variables['endBracketDOntPutThere'] = 1
                variables['dontSaveStr'] = 0
                if (variables['inTarget']  != 1)and(variables['endBracketDOntPutThere']  != 1)and(variables['insdeAnestedLoopBAD']  != 1):
                    variables[f'out4758686d86d86d86578991a{variables["AIndexLoopCurlyFix"]}'] += variables['A_LoopField18']  +  "\n"
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
    for A_Index19, A_LoopField19 in enumerate(items, start=1):
        variables['A_Index19'] = A_Index19
        variables['A_LoopField19'] = A_LoopField19
        variables['ignore'] = 0
        if (InStr(variables['A_LoopField19'] , "for ")):
            if (variables['hold'] == 1)and(variables['holdText'] == variables['A_LoopField19']):
                variables['ignore'] = 1
            else:
                variables['holdText'] = variables['A_LoopField19']
                variables['hold'] = 1
        if ( not (variables['ignore'])):
            variables['out4758686d86dgt8r754444444'] += variables['A_LoopField19']  +  "\n"
    variables['out4758686d86dgt8r754444444'] = StringTrimRight(variables['out4758686d86dgt8r754444444'], 1)
    variables['cppCode'] = variables['out4758686d86dgt8r754444444']
variables['pyCodeOut1234565432'] = ""
items = LoopParseFunc(variables['cppCode'], "\n", "\r")
for A_Index20, A_LoopField20 in enumerate(items, start=1):
    variables['A_Index20'] = A_Index20
    variables['A_LoopField20'] = A_LoopField20
    variables['out'] = variables['A_LoopField20']
    if ( not (InStr(variables['out'] , "|itsaersdtgtgfergsdgfsegdfsedAA|"))):
        variables['pyCodeOut1234565432'] += variables['out']  +  "\n"
variables['cppCode'] = StringTrimRight(variables['pyCodeOut1234565432'], 1)
for A_Index21 in range(1, variables['theIdNumOfThe34'] + 1):
    variables['A_Index21'] = A_Index21
    variables['cppCode'] = StrReplace(variables['cppCode'] , "ihuiuuhuuhtheidFor--asas-theuhturtyphoutr-"  +  Chr(65) +  Chr(65) +  str(variables['A_Index21']) +  Chr(65) +  Chr(65), "std::string("  +  variables[f'theIdNumOfThe34theVar{variables["A_Index21"]}']  +  ")")
variables['cppCodeFixCharRemoveStd'] = ""
items = LoopParseFunc(variables['cppCode'], "\n", "\r")
for A_Index22, A_LoopField22 in enumerate(items, start=1):
    variables['A_Index22'] = A_Index22
    variables['A_LoopField22'] = A_LoopField22
    if (SubStr(Trim(StrLower(variables['A_LoopField22'])) , 1 , 5)== "char "):
        variables['cppCodeFixCharRemoveStd123'] = variables['A_LoopField22']
        variables['cppCodeFixCharRemoveStd123'] = StrReplace(variables['cppCodeFixCharRemoveStd123'] , "std::string(" , "")
        variables['cppCodeFixCharRemoveStd123'] = StrReplace(variables['cppCodeFixCharRemoveStd123'] , ")" , "")
        variables['cppCodeFixCharRemoveStd'] += variables['cppCodeFixCharRemoveStd123']  +  "\n"
    else:
        variables['cppCodeFixCharRemoveStd'] += variables['A_LoopField22']  +  "\n"
variables['cppCode'] = StringTrimRight(variables['cppCodeFixCharRemoveStd'], 1)
variables['upCode'] = "\nint main()\n{\n"
if (InStr(variables['cppCode'] , "variables[")):
    variables['upCode'] = variables['upCode']  +  "// Define a map to store dynamic variables\n"  +  "std::unordered_map<std::string, std::any> variables;\n"
variables['uperCode'] = "#include <iostream>\n#include <sstream>\n#include <vector>\n#include <map>\n#include <unordered_map>\n#include <string>\n#include <any>\n#include <cstdint>\n#include <regex>\n"
variables['uperCode'] = variables['uperCode']  +  Chr(10) +  Chr(47) +  Chr(47) +  Chr(32) +  Chr(70) +  Chr(117) +  Chr(110) +  Chr(99) +  Chr(116) +  Chr(105) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(118) +  Chr(101) +  Chr(114) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(97) +  Chr(110) +  Chr(121) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(10) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(118) +  Chr(101) +  Chr(114) +  Chr(116) +  Chr(84) +  Chr(111) +  Chr(73) +  Chr(110) +  Chr(116) +  Chr(40) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(115) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(97) +  Chr(110) +  Chr(121) +  Chr(38) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(46) +  Chr(116) +  Chr(121) +  Chr(112) +  Chr(101) +  Chr(40) +  Chr(41) +  Chr(32) +  Chr(61) +  Chr(61) +  Chr(32) +  Chr(116) +  Chr(121) +  Chr(112) +  Chr(101) +  Chr(105) +  Chr(100) +  Chr(40) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(41) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(116) +  Chr(114) +  Chr(121) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(111) +  Chr(105) +  Chr(40) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(97) +  Chr(110) +  Chr(121) +  Chr(95) +  Chr(99) +  Chr(97) +  Chr(115) +  Chr(116) +  Chr(60) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(62) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(41) +  Chr(41) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(32) +  Chr(99) +  Chr(97) +  Chr(116) +  Chr(99) +  Chr(104) +  Chr(32) +  Chr(40) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(115) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(105) +  Chr(110) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(105) +  Chr(100) +  Chr(95) +  Chr(97) +  Chr(114) +  Chr(103) +  Chr(117) +  Chr(109) +  Chr(101) +  Chr(110) +  Chr(116) +  Chr(38) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(48) +  Chr(59) +  Chr(32) +  Chr(47) +  Chr(47) +  Chr(32) +  Chr(82) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(48) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(118) +  Chr(101) +  Chr(114) +  Chr(115) +  Chr(105) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(102) +  Chr(97) +  Chr(105) +  Chr(108) +  Chr(115) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(32) +  Chr(101) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(46) +  Chr(116) +  Chr(121) +  Chr(112) +  Chr(101) +  Chr(40) +  Chr(41) +  Chr(32) +  Chr(61) +  Chr(61) +  Chr(32) +  Chr(116) +  Chr(121) +  Chr(112) +  Chr(101) +  Chr(105) +  Chr(100) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(41) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(97) +  Chr(110) +  Chr(121) +  Chr(95) +  Chr(99) +  Chr(97) +  Chr(115) +  Chr(116) +  Chr(60) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(62) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(41) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(32) +  Chr(101) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(48) +  Chr(59) +  Chr(32) +  Chr(47) +  Chr(47) +  Chr(32) +  Chr(82) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(48) +  Chr(32) +  Chr(102) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(111) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(114) +  Chr(32) +  Chr(116) +  Chr(121) +  Chr(112) +  Chr(101) +  Chr(115) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(10) +  Chr(125) +  Chr(10) +  Chr(10) +  Chr(47) +  Chr(47) +  Chr(32) +  Chr(70) +  Chr(117) +  Chr(110) +  Chr(99) +  Chr(116) +  Chr(105) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(118) +  Chr(101) +  Chr(114) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(97) +  Chr(110) +  Chr(121) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(10) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(118) +  Chr(101) +  Chr(114) +  Chr(116) +  Chr(84) +  Chr(111) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(40) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(115) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(97) +  Chr(110) +  Chr(121) +  Chr(38) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(46) +  Chr(116) +  Chr(121) +  Chr(112) +  Chr(101) +  Chr(40) +  Chr(41) +  Chr(32) +  Chr(61) +  Chr(61) +  Chr(32) +  Chr(116) +  Chr(121) +  Chr(112) +  Chr(101) +  Chr(105) +  Chr(100) +  Chr(40) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(41) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(97) +  Chr(110) +  Chr(121) +  Chr(95) +  Chr(99) +  Chr(97) +  Chr(115) +  Chr(116) +  Chr(60) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(62) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(41) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(32) +  Chr(101) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(46) +  Chr(116) +  Chr(121) +  Chr(112) +  Chr(101) +  Chr(40) +  Chr(41) +  Chr(32) +  Chr(61) +  Chr(61) +  Chr(32) +  Chr(116) +  Chr(121) +  Chr(112) +  Chr(101) +  Chr(105) +  Chr(100) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(41) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(116) +  Chr(111) +  Chr(95) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(40) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(97) +  Chr(110) +  Chr(121) +  Chr(95) +  Chr(99) +  Chr(97) +  Chr(115) +  Chr(116) +  Chr(60) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(62) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(41) +  Chr(41) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(32) +  Chr(101) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(46) +  Chr(116) +  Chr(121) +  Chr(112) +  Chr(101) +  Chr(40) +  Chr(41) +  Chr(32) +  Chr(61) +  Chr(61) +  Chr(32) +  Chr(116) +  Chr(121) +  Chr(112) +  Chr(101) +  Chr(105) +  Chr(100) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(56) +  Chr(95) +  Chr(116) +  Chr(41) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(116) +  Chr(111) +  Chr(95) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(40) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(116) +  Chr(105) +  Chr(99) +  Chr(95) +  Chr(99) +  Chr(97) +  Chr(115) +  Chr(116) +  Chr(60) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(62) +  Chr(40) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(97) +  Chr(110) +  Chr(121) +  Chr(95) +  Chr(99) +  Chr(97) +  Chr(115) +  Chr(116) +  Chr(60) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(56) +  Chr(95) +  Chr(116) +  Chr(62) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(41) +  Chr(41) +  Chr(41) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(32) +  Chr(101) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(34) +  Chr(34) +  Chr(59) +  Chr(32) +  Chr(47) +  Chr(47) +  Chr(32) +  Chr(82) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(101) +  Chr(109) +  Chr(112) +  Chr(116) +  Chr(121) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(102) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(111) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(114) +  Chr(32) +  Chr(116) +  Chr(121) +  Chr(112) +  Chr(101) +  Chr(115) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(10) +  Chr(125) +  Chr(10) +  Chr(10) +  Chr(47) +  Chr(47) +  Chr(32) +  Chr(70) +  Chr(117) +  Chr(110) +  Chr(99) +  Chr(116) +  Chr(105) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(99) +  Chr(104) +  Chr(101) +  Chr(99) +  Chr(107) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(110) +  Chr(101) +  Chr(101) +  Chr(100) +  Chr(108) +  Chr(101) +  Chr(32) +  Chr(101) +  Chr(120) +  Chr(105) +  Chr(115) +  Chr(116) +  Chr(115) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(32) +  Chr(104) +  Chr(97) +  Chr(121) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(99) +  Chr(107) +  Chr(32) +  Chr(40) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(111) +  Chr(118) +  Chr(101) +  Chr(114) +  Chr(108) +  Chr(111) +  Chr(97) +  Chr(100) +  Chr(41) +  Chr(10) +  Chr(98) +  Chr(111) +  Chr(111) +  Chr(108) +  Chr(32) +  Chr(73) +  Chr(110) +  Chr(83) +  Chr(116) +  Chr(114) +  Chr(40) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(115) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(38) +  Chr(32) +  Chr(104) +  Chr(97) +  Chr(121) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(99) +  Chr(107) +  Chr(44) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(115) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(38) +  Chr(32) +  Chr(110) +  Chr(101) +  Chr(101) +  Chr(100) +  Chr(108) +  Chr(101) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(104) +  Chr(97) +  Chr(121) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(99) +  Chr(107) +  Chr(46) +  Chr(102) +  Chr(105) +  Chr(110) +  Chr(100) +  Chr(40) +  Chr(110) +  Chr(101) +  Chr(101) +  Chr(100) +  Chr(108) +  Chr(101) +  Chr(41) +  Chr(32) +  Chr(33) +  Chr(61) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(58) +  Chr(58) +  Chr(110) +  Chr(112) +  Chr(111) +  Chr(115) +  Chr(59) +  Chr(10) +  Chr(125) +  Chr(10) +  Chr(10)
variables['uperCode'] = variables['uperCode']  +  Chr(10) +  Chr(47) +  Chr(47) +  Chr(32) +  Chr(70) +  Chr(117) +  Chr(110) +  Chr(99) +  Chr(116) +  Chr(105) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(101) +  Chr(115) +  Chr(99) +  Chr(97) +  Chr(112) +  Chr(101) +  Chr(32) +  Chr(115) +  Chr(112) +  Chr(101) +  Chr(99) +  Chr(105) +  Chr(97) +  Chr(108) +  Chr(32) +  Chr(99) +  Chr(104) +  Chr(97) +  Chr(114) +  Chr(97) +  Chr(99) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(115) +  Chr(32) +  Chr(102) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(101) +  Chr(120) +  Chr(10) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(101) +  Chr(115) +  Chr(99) +  Chr(97) +  Chr(112) +  Chr(101) +  Chr(82) +  Chr(101) +  Chr(103) +  Chr(101) +  Chr(120) +  Chr(40) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(115) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(38) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(97) +  Chr(116) +  Chr(105) +  Chr(99) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(115) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(101) +  Chr(120) +  Chr(32) +  Chr(115) +  Chr(112) +  Chr(101) +  Chr(99) +  Chr(105) +  Chr(97) +  Chr(108) +  Chr(67) +  Chr(104) +  Chr(97) +  Chr(114) +  Chr(115) +  Chr(123) +  Chr(82) +  Chr(34) +  Chr(40) +  Chr(91) +  Chr(45) +  Chr(91) +  Chr(92) +  Chr(93) +  Chr(123) +  Chr(125) +  Chr(40) +  Chr(41) +  Chr(42) +  Chr(43) +  Chr(63) +  Chr(46) +  Chr(44) +  Chr(92) +  Chr(94) +  Chr(36) +  Chr(124) +  Chr(35) +  Chr(92) +  Chr(115) +  Chr(93) +  Chr(41) +  Chr(34) +  Chr(125) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(101) +  Chr(120) +  Chr(95) +  Chr(114) +  Chr(101) +  Chr(112) +  Chr(108) +  Chr(97) +  Chr(99) +  Chr(101) +  Chr(40) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(44) +  Chr(32) +  Chr(115) +  Chr(112) +  Chr(101) +  Chr(99) +  Chr(105) +  Chr(97) +  Chr(108) +  Chr(67) +  Chr(104) +  Chr(97) +  Chr(114) +  Chr(115) +  Chr(44) +  Chr(32) +  Chr(82) +  Chr(34) +  Chr(40) +  Chr(92) +  Chr(36) +  Chr(38) +  Chr(41) +  Chr(34) +  Chr(41) +  Chr(59) +  Chr(10) +  Chr(125) +  Chr(10) +  Chr(10) +  Chr(47) +  Chr(47) +  Chr(32) +  Chr(70) +  Chr(117) +  Chr(110) +  Chr(99) +  Chr(116) +  Chr(105) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(115) +  Chr(112) +  Chr(108) +  Chr(105) +  Chr(116) +  Chr(32) +  Chr(97) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(98) +  Chr(97) +  Chr(115) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(115) +  Chr(10) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(118) +  Chr(101) +  Chr(99) +  Chr(116) +  Chr(111) +  Chr(114) +  Chr(60) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(62) +  Chr(32) +  Chr(76) +  Chr(111) +  Chr(111) +  Chr(112) +  Chr(80) +  Chr(97) +  Chr(114) +  Chr(115) +  Chr(101) +  Chr(70) +  Chr(117) +  Chr(110) +  Chr(99) +  Chr(40) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(115) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(38) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(44) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(115) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(38) +  Chr(32) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(49) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(34) +  Chr(34) +  Chr(44) +  Chr(32) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(115) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(38) +  Chr(32) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(50) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(34) +  Chr(34) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(118) +  Chr(101) +  Chr(99) +  Chr(116) +  Chr(111) +  Chr(114) +  Chr(60) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(62) +  Chr(32) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(109) +  Chr(115) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(40) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(49) +  Chr(46) +  Chr(101) +  Chr(109) +  Chr(112) +  Chr(116) +  Chr(121) +  Chr(40) +  Chr(41) +  Chr(32) +  Chr(38) +  Chr(38) +  Chr(32) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(50) +  Chr(46) +  Chr(101) +  Chr(109) +  Chr(112) +  Chr(116) +  Chr(121) +  Chr(40) +  Chr(41) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(47) +  Chr(47) +  Chr(32) +  Chr(73) +  Chr(102) +  Chr(32) +  Chr(110) +  Chr(111) +  Chr(32) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(115) +  Chr(32) +  Chr(97) +  Chr(114) +  Chr(101) +  Chr(32) +  Chr(112) +  Chr(114) +  Chr(111) +  Chr(118) +  Chr(105) +  Chr(100) +  Chr(101) +  Chr(100) +  Chr(44) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(97) +  Chr(32) +  Chr(108) +  Chr(105) +  Chr(115) +  Chr(116) +  Chr(32) +  Chr(111) +  Chr(102) +  Chr(32) +  Chr(99) +  Chr(104) +  Chr(97) +  Chr(114) +  Chr(97) +  Chr(99) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(115) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(102) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(40) +  Chr(99) +  Chr(104) +  Chr(97) +  Chr(114) +  Chr(32) +  Chr(99) +  Chr(32) +  Chr(58) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(109) +  Chr(115) +  Chr(46) +  Chr(112) +  Chr(117) +  Chr(115) +  Chr(104) +  Chr(95) +  Chr(98) +  Chr(97) +  Chr(99) +  Chr(107) +  Chr(40) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(40) +  Chr(49) +  Chr(44) +  Chr(32) +  Chr(99) +  Chr(41) +  Chr(41) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(32) +  Chr(101) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(47) +  Chr(47) +  Chr(32) +  Chr(69) +  Chr(115) +  Chr(99) +  Chr(97) +  Chr(112) +  Chr(101) +  Chr(32) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(115) +  Chr(32) +  Chr(102) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(101) +  Chr(120) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(101) +  Chr(115) +  Chr(99) +  Chr(97) +  Chr(112) +  Chr(101) +  Chr(100) +  Chr(68) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(115) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(101) +  Chr(115) +  Chr(99) +  Chr(97) +  Chr(112) +  Chr(101) +  Chr(82) +  Chr(101) +  Chr(103) +  Chr(101) +  Chr(120) +  Chr(40) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(49) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(100) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(50) +  Chr(41) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(47) +  Chr(47) +  Chr(32) +  Chr(67) +  Chr(111) +  Chr(110) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(117) +  Chr(99) +  Chr(116) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(117) +  Chr(108) +  Chr(97) +  Chr(114) +  Chr(32) +  Chr(101) +  Chr(120) +  Chr(112) +  Chr(114) +  Chr(101) +  Chr(115) +  Chr(115) +  Chr(105) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(112) +  Chr(97) +  Chr(116) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(102) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(115) +  Chr(112) +  Chr(108) +  Chr(105) +  Chr(116) +  Chr(116) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(32) +  Chr(112) +  Chr(97) +  Chr(116) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(61) +  Chr(32) +  Chr(34) +  Chr(91) +  Chr(34) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(101) +  Chr(115) +  Chr(99) +  Chr(97) +  Chr(112) +  Chr(101) +  Chr(100) +  Chr(68) +  Chr(101) +  Chr(108) +  Chr(105) +  Chr(109) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(115) +  Chr(32) +  Chr(43) +  Chr(32) +  Chr(34) +  Chr(93) +  Chr(43) +  Chr(34) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(101) +  Chr(120) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(101) +  Chr(120) +  Chr(80) +  Chr(97) +  Chr(116) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(110) +  Chr(40) +  Chr(112) +  Chr(97) +  Chr(116) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(110) +  Chr(41) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(101) +  Chr(120) +  Chr(95) +  Chr(116) +  Chr(111) +  Chr(107) +  Chr(101) +  Chr(110) +  Chr(95) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(97) +  Chr(116) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(46) +  Chr(98) +  Chr(101) +  Chr(103) +  Chr(105) +  Chr(110) +  Chr(40) +  Chr(41) +  Chr(44) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(114) +  Chr(46) +  Chr(101) +  Chr(110) +  Chr(100) +  Chr(40) +  Chr(41) +  Chr(44) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(101) +  Chr(120) +  Chr(80) +  Chr(97) +  Chr(116) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(110) +  Chr(44) +  Chr(32) +  Chr(45) +  Chr(49) +  Chr(41) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(114) +  Chr(101) +  Chr(103) +  Chr(101) +  Chr(120) +  Chr(95) +  Chr(116) +  Chr(111) +  Chr(107) +  Chr(101) +  Chr(110) +  Chr(95) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(97) +  Chr(116) +  Chr(111) +  Chr(114) +  Chr(32) +  Chr(101) +  Chr(110) +  Chr(100) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(119) +  Chr(104) +  Chr(105) +  Chr(108) +  Chr(101) +  Chr(32) +  Chr(40) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(32) +  Chr(33) +  Chr(61) +  Chr(32) +  Chr(101) +  Chr(110) +  Chr(100) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(109) +  Chr(115) +  Chr(46) +  Chr(112) +  Chr(117) +  Chr(115) +  Chr(104) +  Chr(95) +  Chr(98) +  Chr(97) +  Chr(99) +  Chr(107) +  Chr(40) +  Chr(42) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(114) +  Chr(43) +  Chr(43) +  Chr(41) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(114) +  Chr(101) +  Chr(116) +  Chr(117) +  Chr(114) +  Chr(110) +  Chr(32) +  Chr(105) +  Chr(116) +  Chr(101) +  Chr(109) +  Chr(115) +  Chr(59) +  Chr(10) +  Chr(125) +  Chr(10)
if (InStr(variables['cppCode'] , "print(std::string")):
    variables['uperCode'] = variables['uperCode']  +  Chr(10) +  Chr(47) +  Chr(47) +  Chr(32) +  Chr(70) +  Chr(117) +  Chr(110) +  Chr(99) +  Chr(116) +  Chr(105) +  Chr(111) +  Chr(110) +  Chr(32) +  Chr(116) +  Chr(111) +  Chr(32) +  Chr(112) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(32) +  Chr(116) +  Chr(104) +  Chr(101) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(111) +  Chr(114) +  Chr(101) +  Chr(100) +  Chr(32) +  Chr(105) +  Chr(110) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(97) +  Chr(110) +  Chr(121) +  Chr(10) +  Chr(118) +  Chr(111) +  Chr(105) +  Chr(100) +  Chr(32) +  Chr(112) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(40) +  Chr(99) +  Chr(111) +  Chr(110) +  Chr(115) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(97) +  Chr(110) +  Chr(121) +  Chr(38) +  Chr(32) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(46) +  Chr(104) +  Chr(97) +  Chr(115) +  Chr(95) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(40) +  Chr(41) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(46) +  Chr(116) +  Chr(121) +  Chr(112) +  Chr(101) +  Chr(40) +  Chr(41) +  Chr(32) +  Chr(61) +  Chr(61) +  Chr(32) +  Chr(116) +  Chr(121) +  Chr(112) +  Chr(101) +  Chr(105) +  Chr(100) +  Chr(40) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(41) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(99) +  Chr(111) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(60) +  Chr(60) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(97) +  Chr(110) +  Chr(121) +  Chr(95) +  Chr(99) +  Chr(97) +  Chr(115) +  Chr(116) +  Chr(60) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(115) +  Chr(116) +  Chr(114) +  Chr(105) +  Chr(110) +  Chr(103) +  Chr(62) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(41) +  Chr(32) +  Chr(60) +  Chr(60) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(101) +  Chr(110) +  Chr(100) +  Chr(108) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(32) +  Chr(101) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(32) +  Chr(105) +  Chr(102) +  Chr(32) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(46) +  Chr(116) +  Chr(121) +  Chr(112) +  Chr(101) +  Chr(40) +  Chr(41) +  Chr(32) +  Chr(61) +  Chr(61) +  Chr(32) +  Chr(116) +  Chr(121) +  Chr(112) +  Chr(101) +  Chr(105) +  Chr(100) +  Chr(40) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(41) +  Chr(41) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(99) +  Chr(111) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(60) +  Chr(60) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(97) +  Chr(110) +  Chr(121) +  Chr(95) +  Chr(99) +  Chr(97) +  Chr(115) +  Chr(116) +  Chr(60) +  Chr(105) +  Chr(110) +  Chr(116) +  Chr(62) +  Chr(40) +  Chr(118) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(41) +  Chr(32) +  Chr(60) +  Chr(60) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(101) +  Chr(110) +  Chr(100) +  Chr(108) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(32) +  Chr(101) +  Chr(108) +  Chr(115) +  Chr(101) +  Chr(32) +  Chr(123) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(99) +  Chr(111) +  Chr(117) +  Chr(116) +  Chr(32) +  Chr(60) +  Chr(60) +  Chr(32) +  Chr(34) +  Chr(86) +  Chr(97) +  Chr(108) +  Chr(117) +  Chr(101) +  Chr(32) +  Chr(105) +  Chr(115) +  Chr(32) +  Chr(110) +  Chr(111) +  Chr(116) +  Chr(32) +  Chr(115) +  Chr(101) +  Chr(116) +  Chr(34) +  Chr(32) +  Chr(60) +  Chr(60) +  Chr(32) +  Chr(115) +  Chr(116) +  Chr(100) +  Chr(58) +  Chr(58) +  Chr(101) +  Chr(110) +  Chr(100) +  Chr(108) +  Chr(59) +  Chr(10) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(32) +  Chr(125) +  Chr(10) +  Chr(125) +  Chr(10)
variables['downCode'] = "\nreturn 0;\n}"
variables['cppCode'] = variables['uperCode']  +  variables['upCode']  +  variables['cppCode']  +  variables['downCode']
print(variables['cppCode'])

