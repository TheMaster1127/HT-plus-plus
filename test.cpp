#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <string>
#include <any>
#include <cstdint>
#include <regex>
#include <fstream>
#include <filesystem>
#include <cctype>
#include <algorithm>
#include <cmath>
#include <limits>
#include <chrono>

// Define a map to store dynamic variables
std::unordered_map<std::string, std::any> variables;

// Function to convert std::any to int
int convertToInt(const std::any& value) {
    if (value.type() == typeid(std::string)) {
        try {
            return std::stoi(std::any_cast<std::string>(value));
        } catch (const std::invalid_argument&) {
            return 0; // Return 0 if conversion fails
        }
    } else if (value.type() == typeid(int)) {
        return std::any_cast<int>(value);
    } else {
        return 0; // Return 0 for other types
    }
}

// Function to convert std::any to std::string
std::string convertToStr(const std::any& value) {
    if (value.type() == typeid(std::string)) {
        return std::any_cast<std::string>(value);
    } else if (value.type() == typeid(int)) {
        return std::to_string(std::any_cast<int>(value));
    } else if (value.type() == typeid(int8_t)) {
        return std::to_string(static_cast<int>(std::any_cast<int8_t>(value)));
    } else {
        return ""; // Return empty string for other types
    }
}

// Function to check if needle exists in haystack (std::string overload)
bool InStr(const std::string& haystack, const std::string& needle) {
    return haystack.find(needle) != std::string::npos;
}

// Function to escape special characters for regex
std::string escapeRegex(const std::string& str) {
    static const std::regex specialChars{R"([-[\]{}()*+?.,\^$|#\s])"};
    return std::regex_replace(str, specialChars, R"(\$&)");
}

// Function to split a string based on delimiters
std::vector<std::string> LoopParseFunc(const std::string& var, const std::string& delimiter1 = "", const std::string& delimiter2 = "") {
    std::vector<std::string> items;
    if (delimiter1.empty() && delimiter2.empty()) {
        // If no delimiters are provided, return a list of characters
        for (char c : var) {
            items.push_back(std::string(1, c));
        }
    } else {
        // Escape delimiters for regex
        std::string escapedDelimiters = escapeRegex(delimiter1 + delimiter2);
        // Construct the regular expression pattern for splitting the string
        std::string pattern = "[" + escapedDelimiters + "]+";
        std::regex regexPattern(pattern);
        std::sregex_token_iterator iter(var.begin(), var.end(), regexPattern, -1);
        std::sregex_token_iterator end;
        while (iter != end) {
            items.push_back(*iter++);
        }
    }
    return items;
}

// Function to print the value stored in std::any
void print(const std::any& value) {
    if (value.has_value()) {
        if (value.type() == typeid(std::string)) {
            std::cout << std::any_cast<std::string>(value) << std::endl;
        } else if (value.type() == typeid(int)) {
            std::cout << std::any_cast<int>(value) << std::endl;
        }
    } else {
        std::cout << "Value is not set" << std::endl;
    }
}

// Function to trim characters from the left of the string
std::string StringTrimLeft(const std::string &input, int numChars) {
    return (numChars <= input.length()) ? input.substr(numChars) : input;
}

// Function to trim characters from the right of the string
std::string StringTrimRight(const std::string &input, int numChars) {
    return (numChars <= input.length()) ? input.substr(0, input.length() - numChars) : input;
}

// Custom Mod function
int Mod(int dividend, int divisor) {
    return dividend % divisor;
}

double Floor(double num) {
    if (std::isnan(num)) {
        return std::numeric_limits<double>::quiet_NaN();
    }
    return std::floor(num);
}

auto start_timestamp = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch()).count();

// Function to calculate tick count in milliseconds
std::string A_TickCount() {
    auto current_timestamp = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch()).count();
    return std::to_string(current_timestamp - start_timestamp);
}

std::any aszdxfc()
{
return std::string("hello");
}
int main()
{
variables["StartTime"] = convertToInt ( A_TickCount ( ) ) ;
variables["var1"] = std::string("hello asdfdxg aesdf asdfg cdfxcgvhello asdfdxg aesdf asdfg cd");
for (int A_Index1 = 1; A_Index1<= 13; ++A_Index1)
{
variables["A_Index1"] = A_Index1;
variables["var1"] = convertToStr(variables["var1"]) + convertToStr(variables["var1"]) + convertToStr(variables["var1"]);
}
variables["numsss"] = 0;
std::vector<std::string> items2 = LoopParseFunc(convertToStr(variables["var1"]), std::string(" "));
for (size_t A_Index2 = 0; A_Index2 < items2.size(); A_Index2++)
{
variables["A_Index2"] = std::to_string(A_Index2 + 1);
variables["A_LoopField2"] = items2[A_Index2];
variables["numsss"] = convertToInt(variables["numsss"]) + 1;
if (InStr (convertToStr(variables["A_LoopField2"]) , std::string("sd")))
{
variables["AWSEDRF"] = variables["A_LoopField2"];
}
}
print(convertToStr(variables["numsss"]));
variables["asdfg"] = std::string("hello");
 variables["asdfg"] = StringTrimRight( convertToStr(variables["asdfg"]),  1);
 variables["asdfg"] = StringTrimLeft( convertToStr(variables["asdfg"]),  1);
print(convertToStr ( variables["asdfg"] ) );
variables["ElapsedTime"] = convertToInt ( A_TickCount ( ) ) - convertToInt(variables["StartTime"]);
variables["ms"] = variables["ElapsedTime"];
variables["hours"] = Floor ( convertToInt(variables["ms"]) / 3600000 ) ;
variables["ms"] = Mod ( convertToInt(variables["ms"]) , 3600000 ) ;
variables["minutes"] = Floor ( convertToInt(variables["ms"]) / 60000 ) ;
variables["ms"] = Mod ( convertToInt(variables["ms"]) , 60000 ) ;
variables["seconds"] = Floor ( convertToInt(variables["ms"]) / 1000 ) ;
variables["milliseconds"] = Mod ( convertToInt(variables["ms"]) , 1000 ) ;
variables["ElapsedTime123"] = convertToStr(variables["hours"]) + std::string("h ") + convertToStr(variables["minutes"]) + std::string("m ") + convertToStr(variables["seconds"]) + std::string("s ") + convertToStr(variables["milliseconds"]) + std::string("ms");
print(variables["ElapsedTime123"]);
return 0;
}