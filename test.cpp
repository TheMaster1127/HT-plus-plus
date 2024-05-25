#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <unordered_map>
#include <string>
#include <any>
#include <cstdint>
#include <regex>
#include <fstream>
#include <filesystem>

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

std::string FileRead(const std::string& path) {
    std::ifstream file;
    std::filesystem::path full_path;

    // Check if the file path is an absolute path
    if (std::filesystem::path(path).is_absolute()) {
        full_path = path;
    } else {
        // If it's not a full path, prepend the current working directory
        full_path = std::filesystem::current_path() / path;
    }

    // Open the file
    file.open(full_path);
    if (!file.is_open()) {
        throw std::runtime_error("Error: Could not open the file.");
    }

    // Read the file content into a string
    std::string content;
    std::string line;
    while (std::getline(file, line)) {
        content += line + '\n';
    }

    file.close();
    return content;
}

bool FileAppend(const std::string& content, const std::string& path) {
    std::ofstream file;

    // Open the file in append mode
    file.open(path, std::ios::app);

    if (!file.is_open()) {
        std::cerr << "Error: Could not open the file for appending." << std::endl;
        return false;
    }

    // Append the content to the file
    file << content;

    // Close the file
    file.close();

    return true;
}

bool FileDelete(const std::string& path) {
    std::filesystem::path file_path(path);

    // Check if the file exists
    if (!std::filesystem::exists(file_path)) {
        std::cerr << "Error: File does not exist." << std::endl;
        return false;
    }

    // Attempt to remove the file
    if (!std::filesystem::remove(file_path)) {
        std::cerr << "Error: Failed to delete the file." << std::endl;
        return false;
    }

    return true;
}

int main()
{
// Define a map to store dynamic variables
std::unordered_map<std::string, std::any> variables;
print(std::string("hello"));
print(std::string("hello man"));
print(std::string("123"));
print(std::string("123 + 6"));
variables["var1"] = 5 + 6;
variables["var22"] = std::string("hello");
char var2[6] = "hello";
int8_t hello = 5;
int16_t var234 = 1500;
print(std::any(var234));
variables["var2345"] = convertToStr(std::string(var2)) + std::string("") + convertToStr(variables["var1"]) + std::string(" ") + convertToStr(std::any(hello));
print(variables["var2345"]);
variables["var_1"] = 5;
variables["var_2"] = 1;
variables["var_4"] = std::string("awsdefgh");
variables["var_" + convertToStr(variables["var_2"])] = variables["var_4"];
print(variables["var_" + convertToStr(variables["var_2"])]);
variables["var999"] = variables["var_" + convertToStr(variables["var_2"])];
variables["varSSS"] = 999;
variables["var" + convertToStr(variables["varSSS"])] = variables["var_" + convertToStr(variables["var_2"])];
print(variables["var" + convertToStr(variables["varSSS"])]);
print(variables["var999"]);
variables["kar1"] = 10;
variables["kar2"] = 20;
if (convertToInt(variables["kar1"]) > convertToInt(variables["kar2"])) 
{
print(std::string("kar1 is bigger"));
}
else if (convertToInt(variables["kar1"]) < convertToInt(variables["kar2"])) 
{
print(std::string("kar2 is bigger"));
}
else
{
print(std::string("kar2 and kar1 are equal"));
}
for (int A_Index1 = 1; A_Index1<= 5; ++A_Index1)
{
variables["A_Index1"] = A_Index1;
print(variables["A_Index1"]);
}
variables["varrrrrrr2"] = 5;
for (int A_Index2 = 1;; A_Index2++)
{
variables["A_Index2"] = A_Index2;
variables["varrrrrrr2"] = convertToInt(variables["varrrrrrr2"]) + 1;
if (convertToInt(variables["varrrrrrr2"]) > 20) 
{
print(std::string("breakint at ") + convertToStr(variables["A_Index2"]));
break;
}
}
print(variables["varrrrrrr2"]);
variables["varjhgiuo"] = std::string("aswaesrdf wersfdfwesf dwe srfw aesfg esfdg waesfg\nwesfdg\resrdfgfhg\nwaesrfdg\nwersdtgf");
std::vector<std::string> items3 = LoopParseFunc(convertToStr(variables["varjhgiuo"]), "\n", "\r");
for (size_t A_Index3 = 0; A_Index3 < items3.size(); A_Index3++)
{
variables["A_Index3"] = std::to_string(A_Index3 + 1);
variables["A_LoopField3"] = items3[A_Index3];
print(convertToInt(variables["A_Index3"]));
print(convertToStr(variables["A_LoopField3"]));
}
print(std::string("------------------------------"));
std::vector<std::string> items4 = LoopParseFunc(convertToStr(variables["varjhgiuo"]), std::string(" "));
for (size_t A_Index4 = 0; A_Index4 < items4.size(); A_Index4++)
{
variables["A_Index4"] = std::to_string(A_Index4 + 1);
variables["A_LoopField4"] = items4[A_Index4];
print(convertToInt(variables["A_Index4"]));
print(convertToStr(variables["A_LoopField4"]));
}
for (int A_Index5 = 1; A_Index5<= 5; ++A_Index5)
{
variables["A_Index5"] = A_Index5;
for (int A_Index6 = 1; A_Index6<= 5; ++A_Index6)
{
variables["A_Index6"] = A_Index6;
print(variables["A_Index6"]);
}
print(variables["A_Index5"]);
}
variables["var234565432345"] = FileRead("C:\\Users\\The_M\\OneDrive\\Desktop\\AutoHotKey Scripts\\Open Notepad\\Notepad Log\\Date-22-05-2024 Time-17-50-56-Notepad.txt");
print(variables["var234565432345"]);
FileAppend(std::string("hello123456789"), "man.txt");
FileAppend(std::string("hello123456789"), "man.txt");
FileAppend(std::string("\nhello123456789"), "man.txt");
variables["asdfsfsasdfx"] = FileRead("man.txt");
print(variables["asdfsfsasdfx"]);
FileAppend(std::string("hello123456789"), "man.txt");
FileDelete("man.txt");
return 0;
}