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

int main()
{
// Define a map to store dynamic variables
std::unordered_map<std::string, std::any> variables;

variables["var1"] = std::string("hello asdfdxg aesdf asdfg cdfxcgv");
std::vector<std::string> items1 = LoopParseFunc(convertToStr(variables["var1"]), std::string(" "));
for (size_t A_Index1 = 0; A_Index1 < items1.size(); A_Index1++)
{
variables["A_Index1"] = std::to_string(A_Index1 + 1);
variables["A_LoopField1"] = items1[A_Index1];
print(variables["A_LoopField1"]);
}
return 0;
}