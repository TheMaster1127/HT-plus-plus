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

print(std::string("hello"));

return 0;
}