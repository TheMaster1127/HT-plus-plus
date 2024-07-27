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
// Create a map to hold variables
    std::unordered_map<std::string, std::string> variables;

// Convert std::string to int
int INT(const std::string& str) {
    std::istringstream iss(str);
    int value;
    iss >> value;
    return value;
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

// Print function that converts all types to string if needed
template <typename T>
void print(const T& value) {
    if constexpr (std::is_same_v<T, std::string>) {
        std::cout << value << std::endl;
    } else if constexpr (std::is_same_v<T, int>) {
        std::cout << STR(value) << std::endl;
    } else if constexpr (std::is_same_v<T, float>) {
        std::cout << STR(value) << std::endl;
    } else if constexpr (std::is_same_v<T, double>) {
        std::cout << STR(value) << std::endl;
    } else if constexpr (std::is_same_v<T, size_t>) {
        std::cout << STR(value) << std::endl;
    } else if constexpr (std::is_same_v<T, bool>) {
        std::cout << STR(value) << std::endl;
    } else {
        std::cout << "Unsupported type" << std::endl;
    }
}

std::any hello(int var5)
{
return var5;
}
int main()
{
std::string var1 = std::string("aersdgfw esrdtg wesvn");
std::vector<std::string> items1 = LoopParseFunc(var1, std::string(" "));
for (size_t A_Index1 = 0; A_Index1 < items1.size(); A_Index1++)
{
A_Index1 = A_Index1 + 1;
std::string A_LoopField1 = items1[A_Index1];
print(A_LoopField1);
}
int num = 5;
const char* vasdf = "s";
variables["var" + std::string(variables["num"])] = variables["var"] + std::string("10");
var1 = std::string("aesdfgdsawsdsfsagss");
variables["var1"] = std::string("ssdvdvds");
int va2r = ;
int var13 = 69;
va2r = var13;
// can only do one letter char
const char* var5 = "s";
int var = INT ( variables["var" + std::string(variables["num"])] ) ;
int sadsfdx = 5;
sadsfdx++;
variables["wasedsa"] = std::string("5");
int sads = INT ( variables["wasedsa"] ) ;
return 0;
}