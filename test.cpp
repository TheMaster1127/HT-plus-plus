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

// Convert various types to std::string
std::string STR(int value) {
    return std::to_string(value);
}

std::string STR(float value) {
    return std::to_string(value);
}

std::string STR(double value) {
    return std::to_string(value);
}

std::string STR(size_t value) {
    return std::to_string(value);
}

std::string STR(bool value) {
    return value ? "1" : "0";
}

// Define OneIndexedArray
#define OneIndexedArray_DEFINED

// One-indexed dynamic array class
class OneIndexedArray {
private:
    std::vector<std::string> internalArray;

public:
    OneIndexedArray() {
        internalArray.push_back(""); // Placeholder for element count
    }

    void add(const std::string& newElement) {
        internalArray.push_back(newElement);
        internalArray[0] = std::to_string(internalArray.size() - 1);
    }

    void setArray(const std::vector<std::string>& newArray) {
        internalArray.resize(newArray.size() + 1);
        std::copy(newArray.begin(), newArray.end(), internalArray.begin() + 1);
        internalArray[0] = std::to_string(newArray.size());
    }

    std::string& operator[](size_t index) {
        if (index >= internalArray.size()) {
            internalArray.resize(index + 1);
            internalArray[0] = std::to_string(internalArray.size() - 1);
        }
        return internalArray[index];
    }

    const std::string& operator[](size_t index) const {
        if (index >= internalArray.size()) {
            throw std::out_of_range("Index out of range");
        }
        return internalArray[index];
    }

    size_t size() const {
        return internalArray.size() - 1;
    }
};

// Function to split text into words based on a delimiter
std::vector<std::string> split(const std::string& text, const std::string& delimiter) {
    std::vector<std::string> words;
    std::istringstream stream(text);
    std::string word;
    while (std::getline(stream, word, delimiter[0])) { // assuming single character delimiter
        words.push_back(word);
    }
    return words;
}

// Function to split text into a OneIndexedArray
OneIndexedArray arrSplit(const std::string& text, const std::string& delimiter) {
    OneIndexedArray array;
    std::vector<std::string> words = split(text, delimiter);
    array.setArray(words);
    return array;
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
        std::cout << std::to_string(value) << std::endl;
    } else if constexpr (std::is_same_v<T, float>) {
        std::cout << std::to_string(value) << std::endl;
    } else if constexpr (std::is_same_v<T, double>) {
        std::cout << std::to_string(value) << std::endl;
    } else if constexpr (std::is_same_v<T, size_t>) {
        std::cout << std::to_string(value) << std::endl;
    } else if constexpr (std::is_same_v<T, bool>) {
        std::cout << (value ? "1" : "0") << std::endl;
    }
    #ifdef OneIndexedArray_DEFINED
    else if constexpr (std::is_same_v<T, OneIndexedArray>) {
        for (size_t i = 1; i <= value.size(); ++i) {
            std::cout << value[i] << std::endl;
        }
    }
    #endif
    else {
        std::cout << "Unsupported type" << std::endl;
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

// Function to trim characters from the right of the string
std::string StringTrimRight(const std::string &input, int numChars) {
    return (numChars <= input.length()) ? input.substr(0, input.length() - numChars) : input;
}
std::string removeRepeatingWords(std::string text)
{
std::string out;
OneIndexedArray words = arrSplit ( text , std::string(" ") ) ;
words.add(std::string(" "));
std::vector<std::string> items1 = LoopParseFunc(text, std::string(" "));
for (size_t A_Index1 = 1; A_Index1 < items1.size() + 1; A_Index1++)
{
std::string A_LoopField1 = items1[A_Index1 - 1];
if (A_LoopField1!= words[A_Index1 + 1]) 
{
out += A_LoopField1 + std::string(" ");
}
}
out = StringTrimRight(out, 1);
return out;
}
int main()
{
std::string text = std::string("hello hello hello man man whats up up today today how are you you doing");
print(removeRepeatingWords ( text ) );
// how to use arrays in HT++
// declare the array
OneIndexedArray MyArray123;
// add an element to the array
MyArray123.add(std::string("6"));
// add an element to the array
MyArray123.add(std::string("6"));
// concatenate an element to the second element of the array array
MyArray123[2] += std::string("9");
// add an element to the array
MyArray123.add(std::string("6"));
// reassign an element in the array
MyArray123[3] = std::string("7");
print(std::string("the number of elements in the array MyArray123 is: ") + MyArray123[0]);
print(std::string("Here are all the elements in the array MyArray123"));
print(MyArray123);
// we can also do this
// declare a new array
std::string var123Text = std::string("some text whit spacses");
// split the string var123Text into an array using space as a delimiter
OneIndexedArray MyArray123456789 = arrSplit ( var123Text , std::string(" ") ) ;
print(std::string("the number of elements in the array MyArray123456789 is: ") + MyArray123456789[0]);
print(std::string("Here are all the elements in the array MyArray123456789"));
print(MyArray123456789);
std::string var1 = std::string("aersdgfw esrdtg wesvn");
std::vector<std::string> items2 = LoopParseFunc(var1, std::string(" "));
for (size_t A_Index2 = 1; A_Index2 < items2.size() + 1; A_Index2++)
{
std::string A_LoopField2 = items2[A_Index2 - 1];
print(A_LoopField2);
}
int num = 5;
const char* vasdf = "s";
variables["var" + STR(num)] = variables["var"] + std::string("10");
var1 = std::string("aesdfgdsawsdsfsagss");
variables["var1"] = std::string("ssdvdvds");
int va2r;
int var13 = 69;
va2r = var13;
// can only do one letter char
const char* var5 = "s";
int var = INT ( variables["var" + STR(num)] ) ;
int sadsfdx = 5;
sadsfdx++;
variables["wasedsa"] = std::string("5");
int sads = INT ( variables["wasedsa"] ) ;
variables["num"] = std::string("5");
variables["var" + std::string(variables["num"])] = std::string("hello");
print(variables["var5"]);
std::string filepath = std::string("testText.txt");
std::string text1234 = std::string("dzsfddz jskd jd cakjs a jsv\nsal sajvas");
FileAppend(text1234, filepath);
std::string text12346 = FileRead("testText.txt");
FileDelete(filepath);
for (int A_Index3 = 1;; A_Index3++)
{
if (A_Index3 == 5) 
{
break;
}
else
{
print(A_Index3);
}
}
int numLoop = 10;
for (int A_Index4 = 1; A_Index4<= numLoop; ++A_Index4)
{
if (A_Index4 == 5) 
{
break;
}
else
{
print(A_Index4);
}
}
for (int A_Index5 = 1; A_Index5<= 5; ++A_Index5)
{
if (A_Index5 == 5) 
{
break;
}
else
{
print(A_Index5);
}
}

return 0;
}