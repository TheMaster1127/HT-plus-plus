#include <algorithm>
#include <array>
#include <atomic>
#include <cctype>
#include <chrono>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <memory>
#include <mutex>
#include <regex>
#include <sstream>
#include <stdexcept>
#include <string>
#include <thread>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#include <vector>

// Define a map to store dynamic variables
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

// Convert std::string to float
float FLOAT(const std::string& str) {
    std::istringstream iss(str);
    float value;
    iss >> value;
    return value;
}

// Function to check if needle exists in haystack (std::string overload)
bool InStr(const std::string& haystack, const std::string& needle) {
    return haystack.find(needle) != std::string::npos;
}

// Function to generate a random integer within a specified range [min, max]
int Random(int min, int max) {
    // Seed the random number generator with the current time
    std::srand(std::time(0));
    
    // Generate a random number within the specified range
    int range = max - min + 1;
    int randomNumber = std::rand() % range + min;
    
    return randomNumber;
}


// Function to sleep for a specified number of milliseconds
void Sleep(int milliseconds) {
    std::this_thread::sleep_for(std::chrono::milliseconds(milliseconds));
}


// Function to get input from the user, similar to Python's input() function
std::string input(const std::string& prompt) {
    std::string userInput;
    std::cout << prompt; // Display the prompt to the user
    std::getline(std::cin, userInput); // Get the entire line of input
    return userInput;
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
    else if constexpr (std::is_base_of_v<OneIndexedArray<std::string>, T>) {
        for (size_t i = 1; i <= value.size(); ++i) {
            std::cout << value[i] << std::endl;
        }
    } else if constexpr (std::is_base_of_v<OneIndexedArray<int>, T>) {
        for (size_t i = 1; i <= value.size(); ++i) {
            std::cout << std::to_string(value[i]) << std::endl;
        }
    } else if constexpr (std::is_base_of_v<OneIndexedArray<float>, T>) {
        for (size_t i = 1; i <= value.size(); ++i) {
            std::cout << std::to_string(value[i]) << std::endl;
        }
    } else if constexpr (std::is_base_of_v<OneIndexedArray<double>, T>) {
        for (size_t i = 1; i <= value.size(); ++i) {
            std::cout << std::to_string(value[i]) << std::endl;
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

size_t StrLen(const std::string& str) {
    return str.length();
}

int Asc(const std::string& str) {
    if (!str.empty()) {
        return static_cast<int>(str[0]);
    }
    return -1; // Return -1 if the string is empty
}

double Abs(double value) {
    return std::fabs(value);
}


double ACos(double value) {
    return std::acos(value);
}

double ATan(double value) {
    return std::atan(value);
}

double Ceil(double value) {
    return std::ceil(value);
}

double Cos(double angle) {
    return std::cos(angle);
}

double Exp(double value) {
    return std::exp(value);
}

double Ln(double value) {
    return std::log(value);
}

double Log(double value, double base) {
    return std::log(value) / std::log(base);
}

double Round(double value) {
    return std::round(value);
}

double Sin(double angle) {
    return std::sin(angle);
}

double Sqrt(double value) {
    return std::sqrt(value);
}

double Tan(double angle) {
    return std::tan(angle);
}

std::string SubStr(const std::string& str, int startPos, int length = -1) {
    std::string result;
    size_t strLen = str.size();

    // Handle negative starting positions
    if (startPos < 0) {
        startPos += strLen;
        if (startPos < 0) startPos = 0;
    } else {
        if (startPos > static_cast<int>(strLen)) return ""; // Starting position beyond string length
        startPos -= 1; // Convert to 0-based index
    }

    // Handle length
    if (length < 0) {
        length = strLen - startPos; // Length to end of string
    } else if (startPos + length > static_cast<int>(strLen)) {
        length = strLen - startPos; // Adjust length to fit within the string
    }

    // Extract substring
    result = str.substr(startPos, length);
    return result;
}

std::string Trim(const std::string &inputString) {
    if (inputString.empty()) return "";

    size_t start = inputString.find_first_not_of(" \t\n\r\f\v");
    size_t end = inputString.find_last_not_of(" \t\n\r\f\v");

    return (start == std::string::npos) ? "" : inputString.substr(start, end - start + 1);
}

std::string StrReplace(const std::string &originalString, const std::string &find, const std::string &replaceWith) {
    std::string result = originalString;
    size_t pos = 0;

    while ((pos = result.find(find, pos)) != std::string::npos) {
        result.replace(pos, find.length(), replaceWith);
        pos += replaceWith.length();
    }

    return result;
}

std::string StringTrimLeft(const std::string &input, int numChars) {
    return (numChars <= input.length()) ? input.substr(numChars) : input;
}

std::string StringTrimRight(const std::string &input, int numChars) {
    return (numChars <= input.length()) ? input.substr(0, input.length() - numChars) : input;
}

std::string StrLower(const std::string &string) {
    std::string result = string;
    std::transform(result.begin(), result.end(), result.begin(), ::tolower);
    return result;
}

std::string RegExReplace(const std::string &inputStr, const std::string &regexPattern, const std::string &replacement) {
    std::regex regex(regexPattern);
    return std::regex_replace(inputStr, regex, replacement);
}

std::string StrSplit(const std::string &inputStr, const std::string &delimiter, int num) {
    size_t start = 0, end = 0, count = 0;

    while ((end = inputStr.find(delimiter, start)) != std::string::npos) {
        if (++count == num) {
            return inputStr.substr(start, end - start);
        }
        start = end + delimiter.length();
    }

    if (count + 1 == num) {
        return inputStr.substr(start);
    }

    return "";
}

std::string Chr(int number) {
    return (number >= 0 && number <= 0x10FFFF) ? std::string(1, static_cast<char>(number)) : "";
}


int Mod(int dividend, int divisor) {
    return dividend % divisor;
}

double Floor(double num) {
    if (std::isnan(num)) {
        return std::numeric_limits<double>::quiet_NaN();
    }
    return std::floor(num);
}

std::string trim(const std::string& str) {
    auto start = str.begin();
    while (start != str.end() && std::isspace(*start)) {
        start++;
    }
    auto end = str.end();
    do {
        end--;
    } while (std::distance(start, end) > 0 && std::isspace(*end));
    return std::string(start, end + 1);
}

class JSONValue {
public:
    enum Type { Null, Boolean, Number, String, Array, Object };

    JSONValue() : type(Null) {}
    JSONValue(bool b) : type(Boolean), boolean_value(b) {}
    JSONValue(double n) : type(Number), number_value(n) {}
    JSONValue(const std::string& s) : type(String), string_value(s) {}
    JSONValue(const std::vector<JSONValue>& a) : type(Array), array_value(a) {}
    JSONValue(const std::map<std::string, JSONValue>& o) : type(Object), object_value(o) {}

    Type getType() const { return type; }
    bool isNull() const { return type == Null; }
    bool isBoolean() const { return type == Boolean; }
    bool isNumber() const { return type == Number; }
    bool isString() const { return type == String; }
    bool isArray() const { return type == Array; }
    bool isObject() const { return type == Object; }

    bool asBoolean() const { return boolean_value; }
    double asNumber() const { return number_value; }
    const std::string& asString() const { return string_value; }
    const std::vector<JSONValue>& asArray() const { return array_value; }
    const std::map<std::string, JSONValue>& asObject() const { return object_value; }

private:
    Type type;
    bool boolean_value;
    double number_value;
    std::string string_value;
    std::vector<JSONValue> array_value;
    std::map<std::string, JSONValue> object_value;
};

class JSONParser {
public:
    static JSONValue parse(const std::string& json) {
        size_t index = 0;
        return parseValue(json, index);
    }

private:
    static JSONValue parseValue(const std::string& json, size_t& index) {
        skipWhitespace(json, index);
        char c = json[index];
        if (c == '{') {
            return parseObject(json, index);
        } else if (c == '[') {
            return parseArray(json, index);
        } else if (c == '"') {
            return parseString(json, index);
        } else if (std::isdigit(c) || c == '-') {
            return parseNumber(json, index);
        } else if (c == 't' || c == 'f') {
            return parseBoolean(json, index);
        } else if (c == 'n') {
            return parseNull(json, index);
        }
        throw std::runtime_error("Invalid JSON");
    }

    static JSONValue parseObject(const std::string& json, size_t& index) {
        std::map<std::string, JSONValue> object;
        index++; // Skip '{'
        skipWhitespace(json, index);
        if (json[index] == '}') {
            index++;
            return JSONValue(object);
        }
        while (true) {
            std::string key = parseString(json, index).asString();
            skipWhitespace(json, index);
            if (json[index] != ':') throw std::runtime_error("Expected ':'");
            index++;
            JSONValue value = parseValue(json, index);
            object[key] = value;
            skipWhitespace(json, index);
            if (json[index] == '}') {
                index++;
                return JSONValue(object);
            }
            if (json[index] != ',') throw std::runtime_error("Expected ',' or '}'");
            index++;
            skipWhitespace(json, index);
        }
    }

    static JSONValue parseArray(const std::string& json, size_t& index) {
        std::vector<JSONValue> array;
        index++; // Skip '['
        skipWhitespace(json, index);
        if (json[index] == ']') {
            index++;
            return JSONValue(array);
        }
        while (true) {
            array.push_back(parseValue(json, index));
            skipWhitespace(json, index);
            if (json[index] == ']') {
                index++;
                return JSONValue(array);
            }
            if (json[index] != ',') throw std::runtime_error("Expected ',' or ']'");
            index++;
            skipWhitespace(json, index);
        }
    }

    static JSONValue parseString(const std::string& json, size_t& index) {
        index++; // Skip opening quote
        std::string result;
        while (json[index] != '"') {
            if (json[index] == '\\') {
                index++;
                switch (json[index]) {
                    case '"': result += '"'; break;
                    case '\\': result += '\\'; break;
                    case '/': result += '/'; break;
                    case 'b': result += '\b'; break;
                    case 'f': result += '\f'; break;
                    case 'n': result += '\n'; break;
                    case 'r': result += '\r'; break;
                    case 't': result += '\t'; break;
                    default: throw std::runtime_error("Invalid escape sequence");
                }
            } else {
                result += json[index];
            }
            index++;
        }
        index++; // Skip closing quote
        return JSONValue(result);
    }

    static JSONValue parseNumber(const std::string& json, size_t& index) {
        size_t start = index;
        while (std::isdigit(json[index]) || json[index] == '-' || json[index] == '.' || json[index] == 'e' || json[index] == 'E') {
            index++;
        }
        return JSONValue(std::stod(json.substr(start, index - start)));
    }

    static JSONValue parseBoolean(const std::string& json, size_t& index) {
        if (json.substr(index, 4) == "true") {
            index += 4;
            return JSONValue(true);
        } else if (json.substr(index, 5) == "false") {
            index += 5;
            return JSONValue(false);
        }
        throw std::runtime_error("Invalid boolean value");
    }

    static JSONValue parseNull(const std::string& json, size_t& index) {
        if (json.substr(index, 4) == "null") {
            index += 4;
            return JSONValue();
        }
        throw std::runtime_error("Invalid null value");
    }

    static void skipWhitespace(const std::string& json, size_t& index) {
        while (index < json.length() && std::isspace(json[index])) {
            index++;
        }
    }
};

std::string getDataFromJSON(const std::string& json_data, const std::string& json_path) {
    JSONValue root = JSONParser::parse(json_data);
    std::istringstream path_stream(json_path);
    std::string segment;
    JSONValue current = root;

    while (std::getline(path_stream, segment, '.')) {
        segment = trim(segment);
        
        size_t bracket_pos = segment.find('[');
        if (bracket_pos != std::string::npos) {
            std::string key = segment.substr(0, bracket_pos);
            size_t index = std::stoi(segment.substr(bracket_pos + 1, segment.find(']') - bracket_pos - 1));
            
            if (current.isObject() && current.asObject().find(key) != current.asObject().end()) {
                current = current.asObject().at(key);
                if (current.isArray() && index < current.asArray().size()) {
                    current = current.asArray()[index];
                } else {
                    return "Array index out of bounds";
                }
            } else {
                return "Key not found: " + key;
            }
        } else if (current.isObject() && current.asObject().find(segment) != current.asObject().end()) {
            current = current.asObject().at(segment);
        } else {
            return "Key not found: " + segment;
        }
    }

    if (current.isString()) return current.asString();
    if (current.isNumber()) {
        double num = current.asNumber();
        if (num == std::floor(num)) {
            // It's an integer
            return std::to_string(static_cast<long long>(num));
        } else {
            // It's a floating-point number
            return std::to_string(num);
        }
    }
    if (current.isBoolean()) return current.asBoolean() ? "true" : "false";
    if (current.isNull()) return "null";
    
    return "Unsupported value type";
}

// Function to get command-line parameters
std::string GetParams() {
    std::vector<std::string> params;
    for (int i = 1; i < __argc; ++i) {
        std::string arg = __argv[i];
        if (std::filesystem::exists(arg)) {
            arg = std::filesystem::absolute(arg).string();
        }
        params.push_back(arg);
    }
    std::string result;
    for (const auto& param : params) {
        result += param + "\n";
    }
    return result;
}

// Store the start time as a global variable
std::chrono::time_point<std::chrono::steady_clock> programStartTime = std::chrono::steady_clock::now();

// Function to get built-in variables
std::string BuildInVars(const std::string& varName) {
    auto now = std::chrono::system_clock::now();
    std::time_t currentTime = std::chrono::system_clock::to_time_t(now);
    std::tm* localTime = std::localtime(&currentTime);

    std::ostringstream oss;

    if (varName == "A_TickCount") {
        // Calculate milliseconds since program start
        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now() - programStartTime).count();
        if (duration > std::numeric_limits<int>::max()) {
            // Handle overflow case
            return "Value too large";
        } else {
            return std::to_string(static_cast<int>(duration));
        }
    } else if (varName == "A_Now") {
        oss << std::put_time(localTime, "%Y-%m-%d %H:%M:%S");
    } else if (varName == "A_YYYY") {
        oss << std::put_time(localTime, "%Y");
    } else if (varName == "A_MM") {
        oss << std::put_time(localTime, "%m");
    } else if (varName == "A_DD") {
        oss << std::put_time(localTime, "%d");
    } else if (varName == "A_MMMM") {
        oss << std::put_time(localTime, "%B");
    } else if (varName == "A_MMM") {
        oss << std::put_time(localTime, "%b");
    } else if (varName == "A_DDDD") {
        oss << std::put_time(localTime, "%A");
    } else if (varName == "A_DDD") {
        oss << std::put_time(localTime, "%a");
    } else if (varName == "A_Hour") {
        oss << std::put_time(localTime, "%H");
    } else if (varName == "A_Min") {
        oss << std::put_time(localTime, "%M");
    } else if (varName == "A_Sec") {
        oss << std::put_time(localTime, "%S");
    } else if (varName == "A_Space") {
        return " ";
    } else if (varName == "A_Tab") {
        return "\t";
    } else {
        return "";
    }
    return oss.str();
}

// Function to perform regex replacement
std::string RegExReplace(const std::string& inputStr, const std::string& regexPattern, const std::string& replacement) {
    std::regex re(regexPattern, std::regex_constants::ECMAScript | std::regex_constants::multiline);
    return std::regex_replace(inputStr, re, replacement);
}

// Function to run a system command
std::string RunCMD(const std::string& command) {
    std::array<char, 128> buffer;
    std::string result;
#if defined(_WIN32)
    std::unique_ptr<FILE, decltype(&_pclose)> pipe(_popen(command.c_str(), "r"), _pclose);
#else
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(command.c_str(), "r"), pclose);
#endif
    if (!pipe) {
        throw std::runtime_error("popen() failed!");
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }
    return result;
}

// Function to perform regex matching and return the match position
int RegExMatch(const std::string& haystack, const std::string& needleRegEx, std::string* outputVar = nullptr, int startingPos = 0) {
    if (haystack.empty() || needleRegEx.empty()) {
        return 0;
    }

    std::regex re(needleRegEx);
    std::smatch match;

    if (std::regex_search(haystack.begin() + startingPos, haystack.end(), match, re)) {
        if (outputVar != nullptr) {
            *outputVar = match.str(0);
        }
        return match.position(0) + 1; // To make it 1-based index
    }

    return 0;
}

void ExitApp() {
    std::cout << "Exiting application..." << std::endl;
    std::exit(0);
}

// Structure to store timer information
struct TimerInfo {
    std::function<void()> func;
    int interval_ms;
    bool active;
    std::chrono::steady_clock::time_point last_execution;
};

// Maps to store the timers and their states
std::map<std::string, TimerInfo> timers;
std::mutex mtx; // Mutex for synchronizing access to shared data
std::atomic<bool> should_exit(false); // Flag to signal the application to exit

void TimerManager() {
    while (!should_exit) {
        auto now = std::chrono::steady_clock::now();
        {
            std::lock_guard<std::mutex> lock(mtx);
            bool any_active_timers = false;
            for (auto& [name, timer] : timers) {
                if (timer.active) {
                    any_active_timers = true;
                    auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(now - timer.last_execution);
                    if (elapsed.count() >= timer.interval_ms) {
                        timer.func();
                        timer.last_execution = now;
                    }
                }
            }
            if (!any_active_timers) {
                should_exit = true;
            }
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(10)); // Sleep for a short period to reduce CPU usage
    }
}

// Global counter for unique timer names
static int timer_counter = 0;

void SetTimer(const std::function<void()>& func, const std::string& timeOrOnOff) {
    std::lock_guard<std::mutex> lock(mtx); // Lock for safe access to shared data

    // Create a unique identifier for the timer
    std::string name = "timer_" + std::to_string(timer_counter++);

    if (timeOrOnOff == "On") {
        timers[name] = {func, 10, true, std::chrono::steady_clock::now()};
    } else if (timeOrOnOff == "Off") {
        // Find the timer with the matching function and turn it off
        for (auto& [timer_name, timer] : timers) {
            if (timer.func.target_type() == func.target_type() && timer.active) {
                timer.active = false;
                break;
            }
        }
    } else {
        try {
            int interval_ms = std::stoi(timeOrOnOff);
            timers[name] = {func, interval_ms, true, std::chrono::steady_clock::now()};
        } catch (const std::invalid_argument&) {
            std::cerr << "Invalid interval value: " << timeOrOnOff << std::endl;
        }
    }
}

// Function to run a system command
std::string getDataFromAPIRunCMD(const std::string& command) {
    std::array<char, 128> buffer;
    std::string result;
#if defined(_WIN32)
    std::unique_ptr<FILE, decltype(&_pclose)> pipe(_popen(command.c_str(), "r"), _pclose);
#else
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(command.c_str(), "r"), pclose);
#endif
    if (!pipe) {
        throw std::runtime_error("popen() failed!");
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }
    return result;
}


// Function to fetch data from API
std::string getDataFromAPI(const std::string& url) {
    std::string command = "curl -s " + url;
    return getDataFromAPIRunCMD(command);
}

// Helper function to trim whitespace from both ends of a string
std::string trim(const std::string& str) {
    const std::string whitespace = " \t\n\r\f\v";
    size_t start = str.find_first_not_of(whitespace);
    if (start == std::string::npos) return "";
    size_t end = str.find_last_not_of(whitespace);
    return str.substr(start, end - start + 1);
}

// Helper function to convert string to lowercase
std::string toLower(const std::string& str) {
    std::string lowerStr = str;
    std::transform(lowerStr.begin(), lowerStr.end(), lowerStr.begin(), ::tolower);
    return lowerStr;
}

// Function to sort case-insensitively but ensure lowercase items come last
bool customSortCompare(const std::string& a, const std::string& b) {
    std::string lowerA = toLower(a);
    std::string lowerB = toLower(b);
    if (lowerA == lowerB) {
        // If case-insensitive equivalent, ensure lowercase items come last
        if (std::islower(a[0]) && std::isupper(b[0])) {
            return false; // a should come after b
        } else if (std::isupper(a[0]) && std::islower(b[0])) {
            return true; // a should come before b
        }
        return a < b; // Otherwise, sort lexicographically
    }
    return lowerA < lowerB;
}

// Function to remove exact duplicates (case-sensitive)
std::vector<std::string> removeExactDuplicates(const std::vector<std::string>& items) {
    std::unordered_set<std::string> seen;
    std::vector<std::string> uniqueItems;
    for (const auto& item : items) {
        if (seen.find(item) == seen.end()) {
            seen.insert(item);
            uniqueItems.push_back(item);
        }
    }
    return uniqueItems;
}

// Main sorting function
std::string SortLikeAHK(const std::string& input, const std::string& options) {
    std::string delimiter = "\n";
    bool caseInsensitive = options.find('C') != std::string::npos;
    bool unique = options.find('U') != std::string::npos;
    bool reverse = options.find('R') != std::string::npos;
    bool random = options.find("Random") != std::string::npos;
    bool numeric = options.find('N') != std::string::npos;

    // Custom delimiter
    if (options.find('D') != std::string::npos) {
        size_t delimiterPos = options.find('D') + 1;
        if (delimiterPos < options.size()) {
            delimiter = options.substr(delimiterPos, 1);
        }
    }

    // Split input by delimiter
    std::vector<std::string> items;
    std::stringstream ss(input);
    std::string item;
    while (std::getline(ss, item, delimiter[0])) {
        item = trim(item);  // Trim whitespace from each item
        if (!item.empty()) {
            items.push_back(item);
        }
    }

    // Sort items
    if (numeric) {
        std::sort(items.begin(), items.end(), [](const std::string& a, const std::string& b) {
            return std::stoi(a) < std::stoi(b);
        });
    } else {
        std::sort(items.begin(), items.end(), customSortCompare);
    }

    // Remove exact duplicates if needed
    if (unique) {
        items = removeExactDuplicates(items);
    }

    // Apply reverse order if needed
    if (reverse) {
        std::reverse(items.begin(), items.end());
    }

    // Separate uppercase and lowercase items
    std::vector<std::string> uppercaseItems;
    std::vector<std::string> lowercaseItems;
    
    for (const auto& item : items) {
        if (std::isupper(item[0])) {
            uppercaseItems.push_back(item);
        } else {
            lowercaseItems.push_back(item);
        }
    }

    // Combine sorted uppercase items with sorted lowercase items
    std::string result;
    for (const auto& item : uppercaseItems) {
        result += item;
        result += delimiter;
    }
    for (const auto& item : lowercaseItems) {
        result += item;
        if (&item != &lowercaseItems.back()) {
            result += delimiter;
        }
    }

    // Remove trailing delimiter if necessary
    if (!result.empty() && result.back() == delimiter[0]) {
        result.pop_back();
    }

    return result;
}


int main(int argc, char* argv[])
{
// HT++
isVarAnumKindaVar(strrrrr)
{
strLettersStart = 48;
for (int A_Index1 = 1; A_Index1<= 10; ++A_Index1)
{
if (InStr (strrrrr , Chr (strLettersStart))) 
{
return true;
}
strLettersStart++;
}
return false;
}
varDetect(strrrrr)
{
if (InStr (strrrrr , std::string("-"))) 
{
return false;
}
numFixhsidhkcjzdls = 0;
std::vector<std::string> items2 = LoopParseFunc(strrrrr);
for (size_t A_Index2 = 1; A_Index2 < items2.size() + 1; A_Index2++)
{
std::string A_LoopField2 = items2[A_Index2 - 1];
numFixhsidhkcjzdls++;
}
numFixhsidhkcjzdls22 = 0;
std::vector<std::string> items3 = LoopParseFunc(strrrrr);
for (size_t A_Index3 = 1; A_Index3 < items3.size() + 1; A_Index3++)
{
std::string A_LoopField3 = items3[A_Index3 - 1];
if (A_LoopField3 == Chr (48) || A_LoopField3 == Chr (49) || A_LoopField3 == Chr (50) || A_LoopField3 == Chr (51) || A_LoopField3 == Chr (52) || A_LoopField3 == Chr (53) || A_LoopField3 == Chr (54) || A_LoopField3 == Chr (55) || A_LoopField3 == Chr (56) || A_LoopField3 == Chr (57) || A_LoopField3 == Chr (46)) 
{
numFixhsidhkcjzdls22++;
}
}
if (numFixhsidhkcjzdls == numFixhsidhkcjzdls22) 
{
return false;
}
strLettersStart = 97;
for (int A_Index4 = 1; A_Index4<= 26; ++A_Index4)
{
if (InStr (strrrrr , Chr (strLettersStart))) 
{
return true;
}
strLettersStart++;
}
strLettersStart = 65;
for (int A_Index5 = 1; A_Index5<= 26; ++A_Index5)
{
if (InStr (strrrrr , Chr (strLettersStart))) 
{
return true;
}
strLettersStart++;
}
strLettersStart = 48;
for (int A_Index6 = 1; A_Index6<= 10; ++A_Index6)
{
if (InStr (strrrrr , Chr (strLettersStart))) 
{
return true;
}
strLettersStart++;
}
if (InStr (strrrrr , Chr (95))) 
{
return true;
}
if (InStr (strrrrr , Chr (37))) 
{
return true;
}
return false;
}
isVarAfuncOrWhat(varInVarTranspiler, funcNames, allVarsChars, allVarsInts)
{
if (InStr (varInVarTranspiler , std::string("%"))) 
{
nameOfVarr11 = Trim ( StrSplit ( varInVarTranspiler , std::string("%") , 1 ) ) ;
nameOfVarr12 = Trim ( StrSplit ( varInVarTranspiler , std::string("%") , 2 ) ) ;
if (SubStr (nameOfVarr12 , 1 , 1) == std::string("[")) 
{
nameOfVarr12 = StringTrimRight(nameOfVarr12, 1);
nameOfVarr12 = StringTrimLeft(nameOfVarr12, 1);
nameOfVarr111 = std::string("variables[") + Chr ( 34 ) + nameOfVarr11 + Chr ( 34 ) + std::string(" + std::string(variables[") + Chr ( 34 ) + nameOfVarr12 + Chr ( 34 ) + std::string("])]");
}
else
{
nameOfVarr111 = std::string("variables[") + Chr ( 34 ) + nameOfVarr11 + Chr ( 34 ) + std::string(" + STR(") + nameOfVarr12 + std::string(")]");
}
return nameOfVarr111;
}
std::vector<std::string> items7 = LoopParseFunc(allVarsChars, "\n", "\r");
for (size_t A_Index7 = 1; A_Index7 < items7.size() + 1; A_Index7++)
{
std::string A_LoopField7 = items7[A_Index7 - 1];
if (Trim (varInVarTranspiler) == Trim (A_LoopField7)) 
{
return varInVarTranspiler;
}
}
std::vector<std::string> items8 = LoopParseFunc(allVarsInts, "\n", "\r");
for (size_t A_Index8 = 1; A_Index8 < items8.size() + 1; A_Index8++)
{
std::string A_LoopField8 = items8[A_Index8 - 1];
if (Trim (varInVarTranspiler) == Trim (A_LoopField8)) 
{
return varInVarTranspiler;
}
}
std::vector<std::string> items9 = LoopParseFunc(funcNames, std::string("|"));
for (size_t A_Index9 = 1; A_Index9 < items9.size() + 1; A_Index9++)
{
std::string A_LoopField9 = items9[A_Index9 - 1];
if (varInVarTranspiler == A_LoopField9) 
{
return varInVarTranspiler;
}
if (InStr (Trim (varInVarTranspiler) , A_LoopField9 + std::string("("))) 
{
return varInVarTranspiler;
}
}
if (SubStr (varInVarTranspiler , 1 , 1) == std::string("[")) 
{
varInVarTranspiler = StringTrimLeft(varInVarTranspiler, 1);
varInVarTranspiler = StringTrimRight(varInVarTranspiler, 1);
return std::string("variables[") + Chr ( 34 ) + varInVarTranspiler + Chr ( 34 ) + std::string("]");
}
if (varDetect (varInVarTranspiler)) 
{
return varInVarTranspiler;
}
if (isVarAnumKindaVar (varInVarTranspiler)) 
{
return varInVarTranspiler;
}
if (varInVarTranspiler == std::string(".")) 
{
return std::string("+");
}
if (varInVarTranspiler == std::string("=")) 
{
return std::string("==");
}
if (varInVarTranspiler == std::string("or")) 
{
return std::string("||");
}
if (varInVarTranspiler == std::string("and")) 
{
return std::string("&&");
}
return varInVarTranspiler;
}
//;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
//;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
//;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
varTranspiler(var123, funcNames, allVarsChars, allVarsInts)
{
var123out = std::string("");
lastType = std::string("");
typeMode = 0;
print(var123);
var123 = StrReplace ( var123 , std::string(") or (") , std::string(" || ") ) ;
var123 = StrReplace ( var123 , std::string(") || (") , std::string(" || ") ) ;
var123 = StrReplace ( var123 , std::string(") and (") , std::string(" && ") ) ;
var123 = StrReplace ( var123 , std::string(") && (") , std::string(" && ") ) ;
var123 = StrReplace ( var123 , std::string(")  or  (") , std::string("  ||  ") ) ;
var123 = StrReplace ( var123 , std::string(")  ||  (") , std::string("  ||  ") ) ;
var123 = StrReplace ( var123 , std::string(")  and  (") , std::string("  &&  ") ) ;
var123 = StrReplace ( var123 , std::string(")  &&  (") , std::string("  &&  ") ) ;
var123 = StrReplace ( var123 , std::string(",") , std::string(" , ") ) ;
var123 = StrReplace ( var123 , std::string("(") , std::string(" ( ") ) ;
var123 = StrReplace ( var123 , std::string(")") , std::string(" ) ") ) ;
std::vector<std::string> items10 = LoopParseFunc(var123, std::string(" "));
for (size_t A_Index10 = 1; A_Index10 < items10.size() + 1; A_Index10++)
{
std::string A_LoopField10 = items10[A_Index10 - 1];
if (A_LoopField10 == std::string("int") || A_LoopField10 == std::string("str")) 
{
typeMode = 1;
lastType = Trim ( A_LoopField10 ) ;
}
if (A_LoopField10!= std::string("int") && A_LoopField10!= std::string("str") && typeMode == 1) 
{
varInVarTranspiler = Trim ( A_LoopField10 ) ;
varOut2out = isVarAfuncOrWhat ( varInVarTranspiler , funcNames , allVarsChars , allVarsInts ) ;
if (lastType == std::string("int")) 
{
varOut2out = std::string("INT(") + varOut2out + std::string(")");
}
if (lastType == std::string("str")) 
{
varOut2out = std::string("std::string(") + varOut2out + std::string(")");
}
var123out += std::string(() varOut2out ) + std::string(" ");
typeMode = 0;
}
else if (A_LoopField10!= std::string("int") && A_LoopField10!= std::string("str") && typeMode == 0) 
{
varInVarTranspiler = Trim ( A_LoopField10 ) ;
varOut2out = isVarAfuncOrWhat ( varInVarTranspiler , funcNames , allVarsChars , allVarsInts ) ;
var123out += std::string(() varOut2out ) + std::string(" ");
}
}
var123out = StringTrimRight(var123out, 1);
return var123out;
}
transpileLowVariables(sstr)
{
sstr = Trim ( sstr ) ;
outOftranspileVariablesOut = Chr ( 34 ) ;
if (InStr (sstr , Chr (37))) 
{
std::vector<std::string> items11 = LoopParseFunc(sstr, std::string("%"));
for (size_t A_Index11 = 1; A_Index11 < items11.size() + 1; A_Index11++)
{
std::string A_LoopField11 = items11[A_Index11 - 1];
if (Mod (A_Index11 , 2)) 
{
outOftranspileVariablesOut += A_LoopField11;
}
else
{
outOftranspileVariablesOut += Chr ( 34 ) + std::string(" + variables['") + A_LoopField11 + Chr ( 39 ) + Chr ( 93 ) + std::string(" + ") + Chr ( 34 ) ;
}
}
}
else
{
sstr = Chr ( 34 ) + sstr + Chr ( 34 ) ;
return sstr;
}
outOftranspileVariablesOut = outOftranspileVariablesOut + Chr ( 34 ) ;
return outOftranspileVariablesOut;
}
CheckIFandElsesss1 = std::string("if (");
CheckIFandElsesss2 = std::string("if(");
CheckIFandElsesss3 = std::string("if !(");
CheckIFandElsesss4 = std::string("if!(");
CheckIFandElsesss5 = std::string("else if (");
CheckIFandElsesss6 = std::string("else if(");
CheckIFandElsesss7 = std::string("else if !(");
CheckIFandElsesss8 = std::string("else if!(");
CheckIFandElsesssNum = 0;
onceImportTime = 0;
weUseRandomAtLeastOnce = 0;
weEverUseVars = std::string("");
haveWeEverUsedAloop = 0;
usedLib = std::string("");
putEndPointFlask1Up = std::string("");
putEndPointFlask2Down = std::string("");
AindexcharLength = 1;
pycodeAcurlyBraceAddSomeVrasFixNL = 0;
pycodeAcurlyBraceAddSomeVrasFixLP = 0;
pycodeLoopfixa = std::string("");
out = std::string("");
HTpyCodeD1 = std::string("");
skipLeftCuleyForFuncPLS = 0;
eavbnsalvbaslv = 0;
theMainFuncDec = 0;
upCode = std::string("");
removeNextCurlyBraceCpp = 0;
params = GetParams ( ) ;
std::vector<std::string> items12 = LoopParseFunc(params, "\n", "\r");
for (size_t A_Index12 = 1; A_Index12 < items12.size() + 1; A_Index12++)
{
std::string A_LoopField12 = items12[A_Index12 - 1];
if (A_Index12 == 1) 
{
print(A_LoopField12);
filePathOfCode = A_LoopField12;
//code := FileRead(filePathOfCode)
std::string code = FileRead(filePathOfCode);
}
if (A_Index12 == 2) 
{
print(A_LoopField12);
}
}
//MsgBox, % code
nothing = std::string("");
code = StrReplace ( code , Chr ( 13 ) , nothing ) ;
codeTrimBeggining = std::string("");
std::vector<std::string> items13 = LoopParseFunc(code, "\n", "\r");
for (size_t A_Index13 = 1; A_Index13 < items13.size() + 1; A_Index13++)
{
std::string A_LoopField13 = items13[A_Index13 - 1];
codeTrimBeggining += Trim ( A_LoopField13 ) + std::string("\n");
}
code = StringTrimRight(codeTrimBeggining, 1);
HTpyCodeOUT754754 = std::string("");
areWEinSome34sNum = 0;
theIdNumOfThe34 = 0;
std::vector<std::string> items14 = LoopParseFunc(code);
for (size_t A_Index14 = 1; A_Index14 < items14.size() + 1; A_Index14++)
{
std::string A_LoopField14 = items14[A_Index14 - 1];
theIdNumOfThe34theVar%A_Index14% = Chr ( 34 ) ;
}
std::vector<std::string> items15 = LoopParseFunc(code);
for (size_t A_Index15 = 1; A_Index15 < items15.size() + 1; A_Index15++)
{
std::string A_LoopField15 = items15[A_Index15 - 1];
if (A_LoopField15 == Chr (34)) 
{
areWEinSome34sNum++;
}
if (areWEinSome34sNum == 1) 
{
if (A_LoopField15!= Chr (34)) 
{
if (A_LoopField15 == Chr (96)) 
{
theIdNumOfThe34theVar%theIdNumOfThe34% += Chr ( 92 ) ;
}
else
{
theIdNumOfThe34theVar%theIdNumOfThe34% += A_LoopField15;
}
}
else
{
theIdNumOfThe34++;
HTpyCodeOUT754754 += std::string("ihuiuuhuuhtheidFor--asas-theuhturtyphoutr-") + Chr ( 65 ) + Chr ( 65 ) + std::string(() theIdNumOfThe34 ) + Chr ( 65 ) + Chr ( 65 ) ;
}
}
if (areWEinSome34sNum == 2 || areWEinSome34sNum == 0) 
{
if (A_LoopField15!= Chr (34)) 
{
HTpyCodeOUT754754 += A_LoopField15;
}
areWEinSome34sNum = 0;
}
}
code = HTpyCodeOUT754754;
for (int A_Index16 = 1; A_Index16<= theIdNumOfThe34; ++A_Index16)
{
theIdNumOfThe34theVar%A_Index16% += Chr ( 34 ) ;
}
haveWeEverUsedArrays = 0;
allVarsChars = std::string("");
allVarsInts = std::string("");
funcNames = std::string("std::string|INT|STR|FLOAT|arrSplit|LoopParseFunc|InStr|Random|Sleep|input|print|FileRead|StrLower|FileAppend|FileDelete|StrLen|Asc|Abs|ACos|ATan|Ceil|Cos|Exp|Ln|Log|Round|Sin|Sqrt|Tan|SubStr|Trim|StrReplace|StringTrimLeft|StringTrimRight|RegExReplace|StrSplit|Chr|Mod|Floor|getDataFromJSON|GetParams|BuildInVars|RegExReplace|RegExMatch|RunCMD|SetTimer|ExitApp|getDataFromAPI|SortLikeAHK");
//std::string("std::string|INT|STR|FLOAT|arrSplit|LoopParseFunc|InStr|Random|Sleep|input|print|FileRead|FileAppend|FileDelete|StrLen|Asc|Abs|ACos|ATan|Ceil|Cos|Exp|Ln|Log|Round|Sin|Sqrt|Tan|SubStr|Trim|StrReplace|StringTrimLeft|StringTrimRight|RegExReplace|StrSplit|Chr|Mod|Floor|getDataFromJSON|GetParams|BuildInVars|RegExReplace|RegExMatch|RunCMD|SetTimer|getDataFromAPI|SortLikeAHK")
//std::string("input|int|chr|str|InStr|SubStr|Trim|StrReplace|StringTrimLeft|StringTrimRight|StrLower|RegExReplace|StrSplit|Chr|Mod|FileRead|FileAppend|FileDelete|GetParams|RunCMD|SortLikeAHK|BuildInVars|Floor|ExitApp|SetTimer|Abs|ACos|ASin|ATan|Ceil|Cos|Exp|Ln|Log|Round|Sin|Sqrt|Tan|RegExMatch|StrLen|Asc|getDataFromAPI|getDataFromJSON|float")
// func
std::vector<std::string> items17 = LoopParseFunc(code, "\n", "\r");
for (size_t A_Index17 = 1; A_Index17 < items17.size() + 1; A_Index17++)
{
std::string A_LoopField17 = items17[A_Index17 - 1];
if (SubStr (Trim (StrLower (A_LoopField17)) , 1 , 5) == std::string("func ")) 
{
funcName123 = StringTrimLeft(A_LoopField17, 5);
funcName123 = Trim ( StrSplit ( funcName123 , std::string("(") , 1 ) ) ;
funcName123 = Trim ( StrSplit ( funcName123 , std::string(" ") , 2 ) ) ;
funcNames += std::string("|") + funcName123;
}
}
varAssignmentType = std::string("=");
timer_thread = 0;
cppCode = std::string("");
std::vector<std::string> items18 = LoopParseFunc(code, "\n", "\r");
for (size_t A_Index18 = 1; A_Index18 < items18.size() + 1; A_Index18++)
{
std::string A_LoopField18 = items18[A_Index18 - 1];
lineDone = 0;
if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 10) == std::string("msgbox, % ")) 
{
msgboxCode = StringTrimLeft(A_LoopField18, 10);
msgboxCode = varTranspiler ( msgboxCode , funcNames , allVarsChars , allVarsInts ) ;
cppCode += std::string("print(") + msgboxCode + std::string(");") + std::string("\n");
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 8) == std::string("msgbox, ")) 
{
msgboxCode = StringTrimLeft(A_LoopField18, 8);
cppCode += std::string("print(std::string(") + Chr ( 34 ) + msgboxCode + Chr ( 34 ) + std::string("));") + std::string("\n");
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 1) == std::string(";")) 
{
str1234 = StringTrimLeft(A_LoopField18, 1);
cppCode += std::string("//") + str1234 + std::string("\n");
lineDone = 1;
}
else if (SubStr (A_LoopField18 , -1) == std::string("++")) 
{
str123 = Trim ( A_LoopField18 ) ;
str123 = StringTrimRight(str123, 2);
out = str123 + std::string("++;");
cppCode += out + std::string("\n");
lineDone = 1;
}
else if (SubStr (A_LoopField18 , -1) == std::string("--")) 
{
str123 = Trim ( A_LoopField18 ) ;
str123 = StringTrimRight(str123, 2);
out = str123 + std::string("--;");
cppCode += out + std::string("\n");
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 6) == std::string("sort, ")) 
{
str1 = StringTrimLeft(A_LoopField18, 6);
str1 = Trim ( str1 ) ;
weHaveAcommaFixSortCommand = 0;
if (SubStr (str1 , 0) == Chr (44)) 
{
//MsgBox, comma YES
str1 = StringTrimRight(str1, 1);
weHaveAcommaFixSortCommand = 1;
}
else
{
//MsgBox, comma NO
gg = 0;
}
s = StrSplit ( str1 , std::string(",") , 1 ) ;
out1 = Trim ( s ) ;
s = StrSplit ( str1 , std::string(",") , 2 ) ;
out2 = Trim ( s ) ;
if (weHaveAcommaFixSortCommand == 1) 
{
out2 = out2 + Chr ( 44 ) ;
}
var1 = out1 + std::string(" = SortLikeAHK(") + out1 + std::string(", ") + Chr ( 34 ) + out2 + Chr ( 34 ) + std::string(")");
lineDone = 1;
cppCode += var1 + std::string("\n");
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 10) == std::string("settimer, ")) 
{
str1 = StringTrimLeft(A_LoopField18, 10);
str2 = Trim ( StrSplit ( str1 , std::string(",") , 1 ) ) ;
str3 = Trim ( StrSplit ( str1 , std::string(",") , 2 ) ) ;
if (str3 == std::string("")) 
{
str3 = Chr ( 34 ) + std::string("10") + Chr ( 34 ) ;
}
else
{
if (StrLower (str3) == std::string("on")) 
{
str3 = Chr ( 34 ) + std::string("On") + Chr ( 34 ) ;
}
else if (StrLower (str3) == std::string("off")) 
{
str3 = Chr ( 34 ) + std::string("Off") + Chr ( 34 ) ;
}
else
{
if (RegExMatch (str3 , std::string("^\\d+$"))) 
{
str3 = Chr ( 34 ) + str3 + Chr ( 34 ) ;
}
else
{
str3 = std::string("STR(") + str3 + std::string(")");
}
}
}
out1 = std::string("SetTimer(") + str2 + std::string(", ") + str3 + std::string(");");
lineDone = 1;
cppCode += out1 + std::string("\n");
}
else if (StrLower (A_LoopField18) == std::string("settimers")) 
{
lineDone = 1;
timer_thread++;
cppCode += std::string("std::thread timer_thread") + std::string(() timer_thread ) + std::string("(TimerManager);\n");
}
else if (StrLower (A_LoopField18) == std::string("starttimers")) 
{
lineDone = 1;
cppCode += std::string("timer_thread") + std::string(() timer_thread ) + std::string(".join(); // Wait for TimerManager to finish\nshould_exit = false; // Reset the exit flag for the new TimerManager thread\n");
}
else if (Trim (StrLower (A_LoopField18)) == std::string("exitapp")) 
{
lineDone = 1;
cppCode += std::string("ExitApp();") + std::string("\n");
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 7) == std::string("gosub, ")) 
{
//MsgBox, % A_LoopField18
sstr1 = A_LoopField18;
s = StrSplit ( sstr1 , std::string(",") , 2 ) ;
out1 = s;
out1 = Trim ( out1 ) ;
out2 = out1 + std::string("();");
//MsgBox, % out2
lineDone = 1;
cppCode += out2 + std::string("\n");
}
else if (A_LoopField18 == std::string("Return")) 
{
cppCode += std::string("}") + std::string("\n");
lineDone = 1;
}
else if (RegExReplace (A_LoopField18 , std::string("^\\w+:$") , std::string(""))!= A_LoopField18 && Trim (SubStr (A_LoopField18 , 0)) == std::string(":") && lineDone!= 1 && A_LoopField18!= std::string("main:")) 
{
//MsgBox, % A_LoopField18
out1 = A_LoopField18;
out1 = Trim ( out1 ) ;
out1 = StringTrimRight(out1, 1);
lineDone = 1;
cppCode += std::string("void ") + out1 + std::string("()\n{\n");
//MsgBox, % out1
//~ MsgBox, % see
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 10) == std::string("fileread, ")) 
{
filereadCommand = StringTrimLeft(A_LoopField18, 10);
filereadCommand1varname = StrSplit ( filereadCommand , std::string(", ") , 1 ) ;
filereadCommand2path = StrSplit ( filereadCommand , std::string(", ") , 2 ) ;
filereadCommand2path = StrReplace ( filereadCommand2path , std::string("\\") , std::string("\\\\") ) ;
if (!(InStr (filereadCommand2path , std::string("%")))) 
{
filereadCommand2path = Trim ( transpileLowVariables ( filereadCommand2path ) ) ;
}
else
{
filereadCommand2path = StrReplace ( filereadCommand2path , std::string("%") , std::string("") ) ;
}
cppCode += std::string("std::string ") + filereadCommand1varname + std::string(" = FileRead(") + filereadCommand2path + std::string(");\n");
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 12) == std::string("fileappend, ")) 
{
fileAppendCommand = StringTrimLeft(A_LoopField18, 12);
fileAppendCommand1varname = StrSplit ( fileAppendCommand , std::string(", ") , 1 ) ;
fileAppendCommand2path = StrSplit ( fileAppendCommand , std::string(", ") , 2 ) ;
fileAppendCommand2path = StrReplace ( fileAppendCommand2path , std::string("\\") , std::string("\\\\") ) ;
if (!(InStr (fileAppendCommand2path , std::string("%")))) 
{
fileAppendCommand2path = Trim ( transpileLowVariables ( fileAppendCommand2path ) ) ;
}
else
{
fileAppendCommand2path = StrReplace ( fileAppendCommand2path , std::string("%") , std::string("") ) ;
}
fileAppendCommand1varname = StrReplace ( fileAppendCommand1varname , std::string("%") , std::string("") ) ;
cppCode += std::string("FileAppend(") + fileAppendCommand1varname + std::string(", ") + fileAppendCommand2path + std::string(");\n");
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 12) == std::string("filedelete, ")) 
{
fileDeleteCommand = StringTrimLeft(A_LoopField18, 12);
fileDeleteCommand2path = StrSplit ( fileDeleteCommand , std::string(", ") , 1 ) ;
fileDeleteCommand2path = StrReplace ( fileDeleteCommand2path , std::string("\\") , std::string("\\\\") ) ;
if (!(InStr (fileDeleteCommand2path , std::string("%")))) 
{
fileDeleteCommand2path = Trim ( transpileLowVariables ( fileDeleteCommand2path ) ) ;
}
else
{
fileDeleteCommand2path = StrReplace ( fileDeleteCommand2path , std::string("%") , std::string("") ) ;
}
cppCode += std::string("FileDelete(") + fileDeleteCommand2path + std::string(");\n");
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 17) == StrLower (std::string("StringTrimRight, "))) 
{
varr1 = StrSplit ( A_LoopField18 , std::string(",") , 2 ) ;
varr2 = StrSplit ( A_LoopField18 , std::string(",") , 3 ) ;
varr3 = StrSplit ( A_LoopField18 , std::string(",") , 4 ) ;
outt1 = Trim ( varTranspiler ( varr1 , funcNames , allVarsChars , allVarsInts ) ) ;
outt2 = Trim ( varTranspiler ( varr2 , funcNames , allVarsChars , allVarsInts ) ) ;
outt3 = Trim ( varTranspiler ( varr3 , funcNames , allVarsChars , allVarsInts ) ) ;
out = outt1 + std::string(" = ") + std::string("StringTrimRight(") + outt2 + std::string(", ") + outt3 + std::string(");");
cppCode += out + std::string("\n");
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 8) == StrLower (std::string("Random, "))) 
{
varr1 = StrSplit ( A_LoopField18 , std::string(",") , 2 ) ;
varr2 = StrSplit ( A_LoopField18 , std::string(",") , 3 ) ;
varr3 = StrSplit ( A_LoopField18 , std::string(",") , 4 ) ;
varr1 = StrReplace ( varr1 , std::string("%") , std::string("") ) ;
varr2 = StrReplace ( varr2 , std::string("%") , std::string("") ) ;
varr3 = StrReplace ( varr3 , std::string("%") , std::string("") ) ;
varr1 = std::string("int ") + varr1;
varr1 = StrReplace ( varr1 , std::string("  ") , std::string(" ") ) ;
outt2 = Trim ( varTranspiler ( varr2 , funcNames , allVarsChars , allVarsInts ) ) ;
outt3 = Trim ( varTranspiler ( varr3 , funcNames , allVarsChars , allVarsInts ) ) ;
out = varr1 + std::string(" = ") + std::string("Random(") + outt2 + std::string(", ") + outt3 + std::string(");");
cppCode += out + std::string("\n");
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 7) == StrLower (std::string("Sleep, "))) 
{
varr1 = StrSplit ( A_LoopField18 , std::string(",") , 2 ) ;
varr1 = StrReplace ( varr1 , std::string("%") , std::string("") ) ;
varr1 = StrReplace ( varr1 , std::string("  ") , std::string(" ") ) ;
out = std::string("Sleep(") + varr1 + std::string(");");
cppCode += out + std::string("\n");
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 16) == StrLower (std::string("StringTrimLeft, "))) 
{
varr1 = StrSplit ( A_LoopField18 , std::string(",") , 2 ) ;
varr2 = StrSplit ( A_LoopField18 , std::string(",") , 3 ) ;
varr3 = StrSplit ( A_LoopField18 , std::string(",") , 4 ) ;
outt1 = Trim ( varTranspiler ( varr1 , funcNames , allVarsChars , allVarsInts ) ) ;
outt2 = Trim ( varTranspiler ( varr2 , funcNames , allVarsChars , allVarsInts ) ) ;
outt3 = Trim ( varTranspiler ( varr3 , funcNames , allVarsChars , allVarsInts ) ) ;
out = outt1 + std::string(" = ") + std::string("StringTrimLeft(") + outt2 + std::string(", ") + outt3 + std::string(");");
cppCode += out + std::string("\n");
lineDone = 1;
}
else if (A_LoopField18 == std::string("main:")) 
{
theMainFuncDec = 1;
cppCode += std::string("\nint main(int argc, char* argv[])\n{\n");
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 5) == std::string("func ")) 
{
funcName123 = StringTrimLeft(A_LoopField18, 5);
removeNextCurlyBraceCpp = 1;
funcName123 = StrReplace ( funcName123 , std::string(" str ") , std::string(" std::string ") ) ;
funcName123 = StrReplace ( funcName123 , std::string("str ") , std::string("std::string ") ) ;
funcName123 = StrReplace ( funcName123 , std::string("(str ") , std::string("(std::string ") ) ;
cppCode += funcName123 + std::string("\n{\n");
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 4) == std::string("str ")) 
{
strVar = StringTrimLeft(A_LoopField18, 4);
strVar = Trim ( strVar ) ;
declareAvarNOvalue = 0;
if (InStr (strVar , std::string(" := "))) 
{
varAssignmentType = std::string("=");
}
else if (InStr (strVar , std::string(" += "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" .= "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" -= "))) 
{
varAssignmentType = std::string("-=");
}
else if (InStr (strVar , std::string(" *= "))) 
{
varAssignmentType = std::string("*=");
}
else if (InStr (strVar , std::string(" /= "))) 
{
varAssignmentType = std::string("/=");
}
else
{
declareAvarNOvalue = 1;
}
if (declareAvarNOvalue == 1) 
{
nameOfVar1 = Trim ( StrSplit ( strVar , std::string(" ") , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , std::string(" ") , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
cppCode += std::string("std::string ") + nameOfVar1 + Chr ( 59 ) + std::string("\n");
}
else
{
nameOfVar1 = Trim ( StrSplit ( strVar , std::string(" ") , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , std::string(" ") , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
cppCode += std::string("std::string ") + nameOfVar1 + std::string(" ") + varAssignmentType + std::string(" ") + nameOfVar2 + Chr ( 59 ) + std::string("\n");
}
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 8) == std::string("arr str ")) 
{
strVar = StringTrimLeft(A_LoopField18, 8);
strVar = Trim ( strVar ) ;
haveWeEverUsedArrays = 1;
declareAvarNOvalue = 0;
if (InStr (strVar , std::string(" := "))) 
{
varAssignmentType = std::string("=");
}
else if (InStr (strVar , std::string(" += "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" .= "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" -= "))) 
{
varAssignmentType = std::string("-=");
}
else if (InStr (strVar , std::string(" *= "))) 
{
varAssignmentType = std::string("*=");
}
else if (InStr (strVar , std::string(" /= "))) 
{
varAssignmentType = std::string("/=");
}
else
{
declareAvarNOvalue = 1;
}
// defalut type
arrType = std::string("std::string");
if (declareAvarNOvalue == 1) 
{
nameOfVar1 = Trim ( StrSplit ( strVar , std::string(" ") , 1 ) ) ;
cppCode += std::string("OneIndexedArray<") + arrType + std::string("> ") + nameOfVar1 + Chr ( 59 ) + std::string("\n");
}
else
{
nameOfVar1 = Trim ( StrSplit ( strVar , std::string(" ") , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , std::string(" ") , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar222223 = nameOfVar2;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
if (varAssignmentType == std::string("+=")) 
{
cppCode += nameOfVar1 + std::string(".add(") + nameOfVar222223 + std::string(")") + Chr ( 59 ) + std::string("\n");
}
else
{
cppCode += std::string("OneIndexedArray<") + arrType + std::string("> ") + nameOfVar1 + std::string(" ") + varAssignmentType + std::string(" ") + nameOfVar2 + Chr ( 59 ) + std::string("\n");
}
}
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 8) == std::string("arr int ")) 
{
strVar = StringTrimLeft(A_LoopField18, 8);
strVar = Trim ( strVar ) ;
haveWeEverUsedArrays = 1;
declareAvarNOvalue = 0;
if (InStr (strVar , std::string(" := "))) 
{
varAssignmentType = std::string("=");
}
else if (InStr (strVar , std::string(" += "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" .= "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" -= "))) 
{
varAssignmentType = std::string("-=");
}
else if (InStr (strVar , std::string(" *= "))) 
{
varAssignmentType = std::string("*=");
}
else if (InStr (strVar , std::string(" /= "))) 
{
varAssignmentType = std::string("/=");
}
else
{
declareAvarNOvalue = 1;
}
// defalut type
arrType = std::string("int");
if (declareAvarNOvalue == 1) 
{
nameOfVar1 = Trim ( StrSplit ( strVar , std::string(" ") , 1 ) ) ;
cppCode += std::string("OneIndexedArray<") + arrType + std::string("> ") + nameOfVar1 + Chr ( 59 ) + std::string("\n");
}
else
{
nameOfVar1 = Trim ( StrSplit ( strVar , std::string(" ") , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , std::string(" ") , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar222223 = nameOfVar2;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
if (varAssignmentType == std::string("+=")) 
{
cppCode += nameOfVar1 + std::string(".add(") + nameOfVar222223 + std::string(")") + Chr ( 59 ) + std::string("\n");
}
else
{
cppCode += std::string("OneIndexedArray<") + arrType + std::string("> ") + nameOfVar1 + std::string(" ") + varAssignmentType + std::string(" ") + nameOfVar2 + Chr ( 59 ) + std::string("\n");
}
}
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 10) == std::string("arr float ")) 
{
strVar = StringTrimLeft(A_LoopField18, 10);
strVar = Trim ( strVar ) ;
haveWeEverUsedArrays = 1;
declareAvarNOvalue = 0;
if (InStr (strVar , std::string(" := "))) 
{
varAssignmentType = std::string("=");
}
else if (InStr (strVar , std::string(" += "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" .= "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" -= "))) 
{
varAssignmentType = std::string("-=");
}
else if (InStr (strVar , std::string(" *= "))) 
{
varAssignmentType = std::string("*=");
}
else if (InStr (strVar , std::string(" /= "))) 
{
varAssignmentType = std::string("/=");
}
else
{
declareAvarNOvalue = 1;
}
// defalut type
arrType = std::string("float");
if (declareAvarNOvalue == 1) 
{
nameOfVar1 = Trim ( StrSplit ( strVar , std::string(" ") , 1 ) ) ;
cppCode += std::string("OneIndexedArray<") + arrType + std::string("> ") + nameOfVar1 + Chr ( 59 ) + std::string("\n");
}
else
{
nameOfVar1 = Trim ( StrSplit ( strVar , std::string(" ") , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , std::string(" ") , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar222223 = nameOfVar2;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
if (varAssignmentType == std::string("+=")) 
{
cppCode += nameOfVar1 + std::string(".add(") + nameOfVar222223 + std::string(")") + Chr ( 59 ) + std::string("\n");
}
else
{
cppCode += std::string("OneIndexedArray<") + arrType + std::string("> ") + nameOfVar1 + std::string(" ") + varAssignmentType + std::string(" ") + nameOfVar2 + Chr ( 59 ) + std::string("\n");
}
}
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 4) == std::string("arr ")) 
{
strVar = StringTrimLeft(A_LoopField18, 4);
strVar = Trim ( strVar ) ;
haveWeEverUsedArrays = 1;
declareAvarNOvalue = 0;
if (InStr (strVar , std::string(" := "))) 
{
varAssignmentType = std::string("=");
}
else if (InStr (strVar , std::string(" += "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" .= "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" -= "))) 
{
varAssignmentType = std::string("-=");
}
else if (InStr (strVar , std::string(" *= "))) 
{
varAssignmentType = std::string("*=");
}
else if (InStr (strVar , std::string(" /= "))) 
{
varAssignmentType = std::string("/=");
}
else
{
declareAvarNOvalue = 1;
}
// defalut type
arrType = std::string("std::string");
if (declareAvarNOvalue == 1) 
{
nameOfVar1 = Trim ( StrSplit ( strVar , std::string(" ") , 1 ) ) ;
cppCode += std::string("OneIndexedArray<") + arrType + std::string("> ") + nameOfVar1 + Chr ( 59 ) + std::string("\n");
}
else
{
nameOfVar1 = Trim ( StrSplit ( strVar , std::string(" ") , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , std::string(" ") , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar222223 = nameOfVar2;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
if (varAssignmentType == std::string("+=")) 
{
cppCode += nameOfVar1 + std::string(".add(") + nameOfVar222223 + std::string(")") + Chr ( 59 ) + std::string("\n");
}
else
{
cppCode += std::string("OneIndexedArray<") + arrType + std::string("> ") + nameOfVar1 + std::string(" ") + varAssignmentType + std::string(" ") + nameOfVar2 + Chr ( 59 ) + std::string("\n");
}
}
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 1) == std::string("[")) 
{
strVar = StringTrimLeft(A_LoopField18, 1);
strVar = Trim ( strVar ) ;
declareAvarNOvalue = 0;
if (InStr (strVar , std::string(" := "))) 
{
varAssignmentType = std::string("=");
}
else if (InStr (strVar , std::string(" += "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" .= "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" -= "))) 
{
varAssignmentType = std::string("-=");
}
else if (InStr (strVar , std::string(" *= "))) 
{
varAssignmentType = std::string("*=");
}
else if (InStr (strVar , std::string(" /= "))) 
{
varAssignmentType = std::string("/=");
}
else
{
declareAvarNOvalue = 1;
}
if (declareAvarNOvalue == 1) 
{
nameOfVar1 = Trim ( StrSplit ( strVar , std::string(" ") , 1 ) ) ;
nameOfVar1 = StringTrimRight(nameOfVar1, 1);
nameOfVarSplit = StrSplit ( strVar , std::string(" ") , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
cppCode += std::string("variables[") + Chr ( 34 ) + nameOfVar1 + Chr ( 34 ) + std::string("]") + Chr ( 59 ) + std::string("\n");
}
else
{
nameOfVar1 = Trim ( StrSplit ( strVar , std::string(" ") , 1 ) ) ;
nameOfVar1 = StringTrimRight(nameOfVar1, 1);
nameOfVarSplit = StrSplit ( strVar , std::string(" ") , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
cppCode += std::string("variables[") + Chr ( 34 ) + nameOfVar1 + Chr ( 34 ) + std::string("] ") + varAssignmentType + std::string(" ") + nameOfVar2 + Chr ( 59 ) + std::string("\n");
}
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 5) == std::string("char ")) 
{
varName123Temp = StringTrimLeft(A_LoopField18, 5);
varName = StrSplit ( varName123Temp , std::string(" ") , 1 ) ;
lineDone = 1;
strVar = StringTrimLeft(A_LoopField18, 5);
strVar = Trim ( strVar ) ;
declareAvarNOvalue = 0;
if (InStr (strVar , std::string(" := "))) 
{
varAssignmentType = std::string("=");
}
else if (InStr (strVar , std::string(" += "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" .= "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" -= "))) 
{
varAssignmentType = std::string("-=");
}
else if (InStr (strVar , std::string(" *= "))) 
{
varAssignmentType = std::string("*=");
}
else if (InStr (strVar , std::string(" /= "))) 
{
varAssignmentType = std::string("/=");
}
else
{
declareAvarNOvalue = 1;
}
if (declareAvarNOvalue == 1) 
{
charVar1 = Trim ( StrSplit ( strVar , std::string(":=") , 1 ) ) ;
didItFoundTheChar = 0;
cppCode += std::string("const char* ") + charVar1 + Chr ( 59 ) + std::string("\n");
}
else
{
charVar1 = Trim ( StrSplit ( strVar , std::string(":=") , 1 ) ) ;
charVar2 = Trim ( StrSplit ( strVar , std::string(":=") , 2 ) ) ;
didItFoundTheChar = 0;
cppCode += std::string("const char* ") + charVar1 + std::string(" ") + varAssignmentType + std::string(" ") + charVar2 + Chr ( 59 ) + std::string("\n");
}
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 4) == std::string("int ") || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 5) == std::string("int8 ") || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 6) == std::string("int16 ") || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 6) == std::string("int32 ") || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 6) == std::string("int64 ")) 
{
lineDone = 1;
if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 5) == std::string("int8 ")) 
{
varName123Temp = StringTrimLeft(A_LoopField18, 5);
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 4) == std::string("int ")) 
{
varName123Temp = StringTrimLeft(A_LoopField18, 4);
}
else
{
varName123Temp = StringTrimLeft(A_LoopField18, 6);
}
intType = Trim ( StrSplit ( A_LoopField18 , std::string(" ") , 1 ) ) + std::string("_t");
varName = StrSplit ( varName123Temp , std::string(" ") , 1 ) ;
allVarsInts += varName + std::string("\n");
if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 5) == std::string("int8 ")) 
{
strVar = StringTrimLeft(A_LoopField18, 5);
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 4) == std::string("int ")) 
{
strVar = StringTrimLeft(A_LoopField18, 4);
}
else
{
strVar = StringTrimLeft(A_LoopField18, 6);
}
strVar = Trim ( strVar ) ;
declareAvarNOvalue = 0;
if (InStr (strVar , std::string(" := "))) 
{
varAssignmentType = std::string("=");
}
else if (InStr (strVar , std::string(" += "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" .= "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" -= "))) 
{
varAssignmentType = std::string("-=");
}
else if (InStr (strVar , std::string(" *= "))) 
{
varAssignmentType = std::string("*=");
}
else if (InStr (strVar , std::string(" /= "))) 
{
varAssignmentType = std::string("/=");
}
else
{
declareAvarNOvalue = 1;
}
if (declareAvarNOvalue == 1) 
{
charVar1 = Trim ( StrSplit ( strVar , varAssignmentType , 1 ) ) ;
charVar2 = Trim ( StrSplit ( strVar , varAssignmentType , 2 ) ) ;
charVar1 = StrSplit ( charVar1 , std::string(" ") , 1 ) ;
charVar2 = varTranspiler ( charVar2 , funcNames , allVarsChars , allVarsInts ) ;
//MsgBox, % intType
if (intType == std::string("int_t")) 
{
intType = std::string("int");
}
if (intType == std::string("int64_t")) 
{
intType = std::string("long long");
}
cppCode += intType + std::string(" ") + charVar1 + Chr ( 59 ) + std::string("\n");
}
else
{
charVar1 = Trim ( StrSplit ( strVar , varAssignmentType , 1 ) ) ;
charVar2 = Trim ( StrSplit ( strVar , varAssignmentType , 2 ) ) ;
charVar1 = StrSplit ( charVar1 , std::string(" ") , 1 ) ;
charVar2 = varTranspiler ( charVar2 , funcNames , allVarsChars , allVarsInts ) ;
//MsgBox, % intType
if (intType == std::string("int_t")) 
{
intType = std::string("int");
}
if (intType == std::string("int64_t")) 
{
intType = std::string("long long");
}
cppCode += intType + std::string(" ") + charVar1 + std::string(" ") + varAssignmentType + std::string(" ") + charVar2 + Chr ( 59 ) + std::string("\n");
}
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 4) == std::string("cat ")) 
{
lineDone = 1;
strVar = StringTrimLeft(A_LoopField18, 4);
strVar = Trim ( strVar ) ;
declareAvarNOvalue = 0;
if (InStr (strVar , std::string(" := "))) 
{
varAssignmentType = std::string("=");
}
else if (InStr (strVar , std::string(" += "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" .= "))) 
{
varAssignmentType = std::string("+=");
}
else if (InStr (strVar , std::string(" -= "))) 
{
varAssignmentType = std::string("-=");
}
else if (InStr (strVar , std::string(" *= "))) 
{
varAssignmentType = std::string("*=");
}
else if (InStr (strVar , std::string(" /= "))) 
{
varAssignmentType = std::string("/=");
}
else
{
declareAvarNOvalue = 1;
}
if (declareAvarNOvalue == 1) 
{
nameOfVar1 = Trim ( StrSplit ( strVar , std::string(" ") , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , std::string(" ") , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
nameOfVar11 = Trim ( StrSplit ( nameOfVar1 , std::string("%") , 1 ) ) ;
nameOfVar12 = Trim ( StrSplit ( nameOfVar1 , std::string("%") , 2 ) ) ;
if (SubStr (nameOfVar12 , 1 , 1) == std::string("[")) 
{
nameOfVar12 = StringTrimRight(nameOfVar12, 1);
nameOfVar12 = StringTrimLeft(nameOfVar12, 1);
nameOfVar1 = std::string("variables[") + Chr ( 34 ) + nameOfVar11 + Chr ( 34 ) + std::string(" + std::string(variables[") + Chr ( 34 ) + nameOfVar12 + Chr ( 34 ) + std::string("])]");
}
else
{
nameOfVar1 = std::string("variables[") + Chr ( 34 ) + nameOfVar11 + Chr ( 34 ) + std::string(" + STR(") + nameOfVar12 + std::string(")]");
}
cppCode += nameOfVar1 + Chr ( 59 ) + std::string("\n");
}
else
{
nameOfVar1 = Trim ( StrSplit ( strVar , std::string(" ") , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , std::string(" ") , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
nameOfVar11 = Trim ( StrSplit ( nameOfVar1 , std::string("%") , 1 ) ) ;
nameOfVar12 = Trim ( StrSplit ( nameOfVar1 , std::string("%") , 2 ) ) ;
if (SubStr (nameOfVar12 , 1 , 1) == std::string("[")) 
{
nameOfVar12 = StringTrimRight(nameOfVar12, 1);
nameOfVar12 = StringTrimLeft(nameOfVar12, 1);
nameOfVar1 = std::string("variables[") + Chr ( 34 ) + nameOfVar11 + Chr ( 34 ) + std::string(" + std::string(variables[") + Chr ( 34 ) + nameOfVar12 + Chr ( 34 ) + std::string("])]");
}
else
{
nameOfVar1 = std::string("variables[") + Chr ( 34 ) + nameOfVar11 + Chr ( 34 ) + std::string(" + STR(") + nameOfVar12 + std::string(")]");
}
cppCode += nameOfVar1 + std::string(" ") + varAssignmentType + std::string(" ") + nameOfVar2 + Chr ( 59 ) + std::string("\n");
}
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 4) == StrLower (CheckIFandElsesss1) || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 3) == StrLower (CheckIFandElsesss2) || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 5) == StrLower (CheckIFandElsesss3) || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 4) == StrLower (CheckIFandElsesss4) || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 9) == StrLower (CheckIFandElsesss5) || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 8) == StrLower (CheckIFandElsesss6) || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 10) == StrLower (CheckIFandElsesss7) || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 9) == StrLower (CheckIFandElsesss8)) 
{
lineDone = 1;
if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 4) == StrLower (CheckIFandElsesss1)) 
{
CheckIFandElsesssNum = 4;
CheckIFandElsesssNumNum = 1;
}
if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 3) == StrLower (CheckIFandElsesss2)) 
{
CheckIFandElsesssNum = 3;
CheckIFandElsesssNumNum = 2;
}
if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 5) == StrLower (CheckIFandElsesss3)) 
{
CheckIFandElsesssNum = 5;
CheckIFandElsesssNumNum = 3;
}
if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 4) == StrLower (CheckIFandElsesss4)) 
{
CheckIFandElsesssNum = 4;
CheckIFandElsesssNumNum = 4;
}
if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 9) == StrLower (CheckIFandElsesss5)) 
{
CheckIFandElsesssNum = 9;
CheckIFandElsesssNumNum = 5;
}
if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 8) == StrLower (CheckIFandElsesss6)) 
{
CheckIFandElsesssNum = 8;
CheckIFandElsesssNumNum = 6;
}
if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 10) == StrLower (CheckIFandElsesss7)) 
{
CheckIFandElsesssNum = 10;
CheckIFandElsesssNumNum = 7;
}
if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 9) == StrLower (CheckIFandElsesss8)) 
{
CheckIFandElsesssNum = 9;
CheckIFandElsesssNumNum = 8;
}
str123 = StringTrimLeft(A_LoopField18, CheckIFandElsesssNum);
str123 = StrReplace ( str123 , std::string("(") , std::string(" ( ") ) ;
str123 = StrReplace ( str123 , std::string(")") , std::string(" ) ") ) ;
str123 = StrReplace ( str123 , std::string("!") , std::string(" ! ") ) ;
str123 = variables["CheckIFandElsesss" + STR(CheckIFandElsesssNumNum)] + Chr ( 32 ) + varTranspiler ( str123 , funcNames , allVarsChars , allVarsInts ) ;
str123 = StrReplace ( str123 , std::string("( ") , std::string("(") ) ;
str123 = StrReplace ( str123 , std::string(" )") , std::string(")") ) ;
str123 = StrReplace ( str123 , std::string(" ! ") , std::string("!") ) ;
str123 = StrReplace ( str123 , std::string("") , std::string("") ) ;
str123 = StrReplace ( str123 , std::string("if ") + Chr ( 40 ) + Chr ( 32 ) , std::string("if ") + Chr ( 40 ) ) ;
str123 = StrReplace ( str123 , std::string("!==") , std::string("!=") ) ;
out123 = str123;
cppCode += out123 + std::string("\n");
}
else if (StrLower (A_LoopField18) == std::string("loop")) 
{
// infinity loops
haveWeEverUsedAloop = 1;
lineDone = 1;
var1 = std::string("for (int A") + Chr ( 95 ) + std::string("Index") + std::string(() AindexcharLength ) + std::string(" = 1;; A") + Chr ( 95 ) + std::string("Index") + std::string(() AindexcharLength ) + std::string("++)");
nothing = std::string("");
AindexcharLengthStr = nothing + std::string(() AindexcharLength ) + nothing;
pycodeAcurlyBraceAddSomeVrasFixNL = 1;
pycodeLoopfixa += std::string("nl|itsaersdtgtgfergsdgfsegdfsedAA|") + std::string(() AindexcharLength ) + std::string("\n");
pycodeLoopfixa1 = std::string("nl|itsaersdtgtgfergsdgfsegdfsedAA|") + std::string(() AindexcharLength ) ;
AindexcharLength++;
cppCode += pycodeLoopfixa1 + std::string("\n") + var1 + std::string("\n");
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 6) == std::string("loop, ") && SubStr (Trim (StrLower (A_LoopField18)) , 1 , 8)!= std::string("loop, % ") && SubStr (Trim (StrLower (A_LoopField18)) , 1 , 7)!= std::string("loop % ") && SubStr (Trim (StrLower (A_LoopField18)) , 1 , 11)!= StrLower (std::string("Loop, Parse"))) 
{
str123 = A_LoopField18;
//MsgBox, % str123
out2 = StringTrimLeft(str123, 6);
//MsgBox % out2
//MsgBox, % out2
out2 = Trim ( out2 ) ;
lineDone = 1;
myVar = out2;
lineYGI = varTranspiler ( myVar , funcNames , allVarsChars , allVarsInts ) ;
line = lineYGI;
haveWeEverUsedAloop = 1;
//MsgBox, % line
var1 = std::string("for (int A") + Chr ( 95 ) + std::string("Index") + std::string(() AindexcharLength ) + std::string(" = 1; A") + Chr ( 95 ) + std::string("Index") + std::string(() AindexcharLength ) + std::string("<= ") + line + std::string("; ++A") + Chr ( 95 ) + std::string("Index") + std::string(() AindexcharLength ) + std::string(")");
nothing = std::string("");
AindexcharLengthStr = nothing + std::string(() AindexcharLength ) + nothing;
pycodeAcurlyBraceAddSomeVrasFixNL = 1;
pycodeLoopfixa += std::string("nl|itsaersdtgtgfergsdgfsegdfsedAA|") + std::string(() AindexcharLength ) + std::string("\n");
pycodeLoopfixa1 = std::string("nl|itsaersdtgtgfergsdgfsegdfsedAA|") + std::string(() AindexcharLength ) ;
AindexcharLength++;
cppCode += pycodeLoopfixa1 + std::string("\n") + var1 + std::string("\n");
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 8) == std::string("loop, % ")) 
{
str123 = A_LoopField18;
//MsgBox, % str123
lineDone = 1;
out2 = StringTrimLeft(str123, 8);
//MsgBox % out2
//MsgBox, % out2
out2 = Trim ( out2 ) ;
myVar = out2;
lineYGI = varTranspiler ( myVar , funcNames , allVarsChars , allVarsInts ) ;
line = lineYGI;
//MsgBox, % line
var1 = std::string("for (int A") + Chr ( 95 ) + std::string("Index") + std::string(() AindexcharLength ) + std::string(" = 1; A") + Chr ( 95 ) + std::string("Index") + std::string(() AindexcharLength ) + std::string("<= ") + line + std::string("; ++A") + Chr ( 95 ) + std::string("Index") + std::string(() AindexcharLength ) + std::string(")");
nothing = std::string("");
AindexcharLengthStr = nothing + std::string(() AindexcharLength ) + nothing;
pycodeAcurlyBraceAddSomeVrasFixNL = 1;
haveWeEverUsedAloop = 1;
pycodeLoopfixa += std::string("nl|itsaersdtgtgfergsdgfsegdfsedAA|") + std::string(() AindexcharLength ) + std::string("\n");
pycodeLoopfixa1 = std::string("nl|itsaersdtgtgfergsdgfsegdfsedAA|") + std::string(() AindexcharLength ) ;
AindexcharLength++;
cppCode += pycodeLoopfixa1 + std::string("\n") + var1 + std::string("\n");
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 13) == StrLower (std::string("Loop, Parse, "))) 
{
//std::vector<std::string> items = LoopParseFunc(variables[std::string("var1")], std::string(" "));
lineDone = 1;
var1 = A_LoopField18;
var1 = Trim ( var1 ) ;
var1 = StringTrimLeft(var1, 13);
line1 = Trim ( StrSplit ( var1 , std::string(",") , 1 ) ) ;
line1 = varTranspiler ( line1 , funcNames , allVarsChars , allVarsInts ) ;
line2 = std::string("");
line3 = std::string("");
itemsOut = std::string("");
line2 = Trim ( StrSplit ( var1 , std::string(",") , 2 ) ) ;
line3 = Trim ( StrSplit ( var1 , std::string(",") , 3 ) ) ;
if (InStr (var1 , Chr (96) + std::string(","))) 
{
line2 = Chr ( 34 ) + std::string(",") + Chr ( 34 ) ;
itemsOut = std::string("std::vector<std::string> items") + std::string(() AindexcharLength ) + std::string(" = LoopParseFunc(") + line1 + std::string(", ") + line2 + std::string(");");
}
else
{
if (line2 == std::string("") && line3 == std::string("")) 
{
// nothing so only each char
itemsOut = std::string("std::vector<std::string> items") + std::string(() AindexcharLength ) + std::string(" = LoopParseFunc(") + line1 + std::string(");");
}
if (line2!= std::string("") && line3 == std::string("")) 
{
if (InStr (line2 , Chr (96))) 
{
line2 = Chr ( 34 ) + line2 + Chr ( 34 ) ;
}
itemsOut = std::string("std::vector<std::string> items") + std::string(() AindexcharLength ) + std::string(" = LoopParseFunc(") + line1 + std::string(", ") + line2 + std::string(");");
}
if (line2!= std::string("") && line3!= std::string("")) 
{
if (InStr (line2 , Chr (96))) 
{
line2 = Chr ( 34 ) + line2 + Chr ( 34 ) ;
}
if (InStr (line3 , Chr (96))) 
{
line3 = Chr ( 34 ) + line3 + Chr ( 34 ) ;
}
itemsOut = std::string("std::vector<std::string> items") + std::string(() AindexcharLength ) + std::string(" = LoopParseFunc(") + line1 + std::string(", ") + line2 + std::string(", ") + line3 + std::string(");");
}
itemsOut = StrReplace ( itemsOut , Chr ( 96 ) , Chr ( 92 ) ) ;
}
//for (size_t A_Index1 = 0; A_Index1 < items.size(); A_Index1++)
var1out = itemsOut + std::string("\n") + std::string("for (size_t A") + Chr ( 95 ) + std::string("Index") + std::string(() AindexcharLength ) + std::string(" = 1; A") + Chr ( 95 ) + std::string("Index") + std::string(() AindexcharLength ) + std::string(" < items") + std::string(() AindexcharLength ) + std::string(".size() + 1; A") + Chr ( 95 ) + std::string("Index") + std::string(() AindexcharLength ) + std::string("++)");
nothing = std::string("");
AindexcharLengthStr = nothing + std::string(() AindexcharLength ) + nothing;
theFixTextLoopLP = std::string("std::string A") + Chr ( 95 ) + std::string("LoopField") + std::string(() AindexcharLength ) + std::string(" = items") + std::string(() AindexcharLength ) + std::string("[A") + Chr ( 95 ) + std::string("Index") + std::string(() AindexcharLength ) + std::string(" - 1];");
pycodeAcurlyBraceAddSomeVrasFixLP = 1;
haveWeEverUsedAloop = 1;
pycodeLoopfixa += std::string("lp|itsaersdtgtgfergsdgfsegdfsedAA|") + std::string(() AindexcharLength ) + std::string("\n");
pycodeLoopfixa1 = std::string("lp|itsaersdtgtgfergsdgfsegdfsedAA|") + std::string(() AindexcharLength ) ;
AindexcharLength++;
cppCode += pycodeLoopfixa1 + std::string("\n") + var1out + std::string("\n");
lineDone = 1;
}
else if (StrLower (A_LoopField18) == std::string("break")) 
{
cppCode += A_LoopField18 + std::string(";\n");
lineDone = 1;
}
else if (StrLower (A_LoopField18) == std::string("continue")) 
{
cppCode += A_LoopField18 + std::string(";\n");
lineDone = 1;
}
else if (StrLower (A_LoopField18) == std::string("return") || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 7) == std::string("return ")) 
{
if (StrLower (A_LoopField18) == std::string("return")) 
{
cppCode += A_LoopField18 + std::string(";\n");
lineDone = 1;
}
else
{
varTranspiledReturn = StringTrimLeft(A_LoopField18, 7);
varTranspiledReturn = varTranspiler ( varTranspiledReturn , funcNames , allVarsChars , allVarsInts ) ;
cppCode += std::string("return ") + varTranspiledReturn + std::string(";\n");
lineDone = 1;
}
}
else if (InStr (A_LoopField18 , std::string(" := ")) || InStr (A_LoopField18 , std::string(" .= ")) || InStr (A_LoopField18 , std::string(" += ")) || InStr (A_LoopField18 , std::string(" -= ")) || InStr (A_LoopField18 , std::string(" *= ")) || InStr (A_LoopField18 , std::string(" /= ")) && lineDone == 0) 
{
lineDone = 1;
strVar = A_LoopField18;
strVar = Trim ( strVar ) ;
if (InStr (strVar , std::string(" := "))) 
{
varAssignmentType = std::string("=");
}
if (InStr (strVar , std::string(" += "))) 
{
varAssignmentType = std::string("+=");
}
if (InStr (strVar , std::string(" .= "))) 
{
varAssignmentType = std::string("+=");
}
if (InStr (strVar , std::string(" -= "))) 
{
varAssignmentType = std::string("-=");
}
if (InStr (strVar , std::string(" *= "))) 
{
varAssignmentType = std::string("*=");
}
if (InStr (strVar , std::string(" /= "))) 
{
varAssignmentType = std::string("/=");
}
nameOfVar1 = Trim ( StrSplit ( strVar , std::string(" ") , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , std::string(" ") , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
cppCode += nameOfVar1 + std::string(" ") + varAssignmentType + std::string(" ") + nameOfVar2 + Chr ( 59 ) + std::string("\n");
}
else
{
// this is THE else
if (removeNextCurlyBraceCpp!= 1) 
{
removeNextCurlyBraceCpp = 0;
if (skipLeftCuleyForFuncPLS!= 1) 
{
if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 1) == Chr (125)) 
{
cppCode += Chr ( 125 ) + std::string("\n");
}
else
{
if (pycodeAcurlyBraceAddSomeVrasFixLP == 1 && SubStr (Trim (StrLower (A_LoopField18)) , 1 , 1) == Chr (123)) 
{
pycodeAcurlyBraceAddSomeVrasFixLP = 0;
cppCode += A_LoopField18 + std::string("\n") + theFixTextLoopLP + std::string("\n");
}
else
{
if (pycodeAcurlyBraceAddSomeVrasFixNL == 1 && SubStr (Trim (StrLower (A_LoopField18)) , 1 , 1) == Chr (123)) 
{
pycodeAcurlyBraceAddSomeVrasFixNL = 0;
cppCode += A_LoopField18 + std::string("\n") + std::string("\n");
}
else
{
cppCode += A_LoopField18 + std::string("\n");
}
}
}
}
else
{
skipLeftCuleyForFuncPLS = 0;
}
}
else
{
if (Trim (A_LoopField18) == std::string("{") && removeNextCurlyBraceCpp == 1) 
{
removeNextCurlyBraceCpp = 0;
}
else
{
cppCode += A_LoopField18 + std::string("\n");
}
}
}
}
cppCode = StringTrimRight(cppCode, 1);
// cat int var% int num1% := cat str string% int num1%
//s
if (haveWeEverUsedAloop == 1) 
{
pycodeLoopfixa = StringTrimRight(pycodeLoopfixa, 1);
//OutputDebug, |%pycodeLoopfixa%|
AIndexLoopCurlyFix = 1;
std::vector<std::string> items19 = LoopParseFunc(pycodeLoopfixa, "\n", "\r");
for (size_t A_Index19 = 1; A_Index19 < items19.size() + 1; A_Index19++)
{
std::string A_LoopField19 = items19[A_Index19 - 1];
str123 = A_LoopField19;
fixLoopLokingFor = A_LoopField19;
fixLoopLokingForfound = 1;
out1 = StrSplit ( str123 , std::string("|") , 1 ) ;
out2 = StrSplit ( str123 , std::string("|") , 3 ) ;
//OutputDebug, |%out1%|
//OutputDebug, |%out2%|
wasAtanyIfsElseAddAIndexLoopCurlyFix = 0;
if (out1 == std::string("nl")) 
{
inTarget = 0;
insideBracket = 0;
netsedCurly = 0;
eldLoopNestedBADlol = 0;
readyToEnd = 0;
endBracketDOntPutThere = 0;
dontSaveStr = 0;
weAreDoneHereCurly = 0;
DeleayOneCuzOfLoopParse = 0;
fixLoopLokingForNum = 0;
insdeAnestedLoopBAD = 0;
foundTheTopLoop = 0;
out4758686d86d86d86578991a%AIndexLoopCurlyFix% = std::string("");
std::vector<std::string> items20 = LoopParseFunc(cppCode, "\n", "\r");
for (size_t A_Index20 = 1; A_Index20 < items20.size() + 1; A_Index20++)
{
std::string A_LoopField20 = items20[A_Index20 - 1];
//MsgBox, dsfgsdefgesrdg1
//MsgBox, |%A_LoopField20%|`n|%fixLoopLokingFor%|
if (InStr (A_LoopField20 , fixLoopLokingFor) && insdeAnestedLoopBAD!= 1) 
{
fixLoopLokingForNum = 1;
//MsgBox, do we came here 1
}
if (InStr (A_LoopField20 , std::string("for ")) && weAreDoneHereCurly!= 1 && insdeAnestedLoopBAD!= 1 && fixLoopLokingForNum == 1) 
{
s = StrSplit ( A_LoopField20 , std::string("A") + Chr ( 95 ) + std::string("Index") , 2 ) ;
out1z = s;
s = StrSplit ( out1z , std::string(" ") , 1 ) ;
out1z = Trim ( s ) ;
//MsgBox, % out1z
//MsgBox, do we came here 2
fixLoopLokingForNum = 0;
foundTheTopLoop++;
inTarget = 1;
//MsgBox, % A_LoopField20
dontSaveStr = 1;
ALoopField = A_LoopField20;
//ALoopField := StrReplace(ALoopField, std::string("for (/* Loop parse */"), std::string("for (/* Loop parse */ /* From AHK */"))
DeleayOneCuzOfLoopParse = 1;
out4758686d86d86d86578991a%AIndexLoopCurlyFix% += ALoopField + std::string("\n");
}
if (inTarget == 1 && InStr (A_LoopField20 , Chr (123)) && insdeAnestedLoopBAD!= 1) 
{
insideBracket = 1;
}
if (insideBracket == 1 && InStr (A_LoopField20 , Chr (123)) && insdeAnestedLoopBAD!= 1) 
{
netsedCurly++;
}
if (insideBracket == 1 && InStr (A_LoopField20 , Chr (125)) && insdeAnestedLoopBAD!= 1) 
{
netsedCurly--;
readyToEnd = 1;
}
if (InStr (A_LoopField20 , std::string("for ")) && insdeAnestedLoopBAD!= 1 && foundTheTopLoop >= 2) 
{
insdeAnestedLoopBAD = 1;
insideBracket1 = 0;
netsedCurly1 = 0;
}
if (inTarget == 1) 
{
foundTheTopLoop++;
}
if (insdeAnestedLoopBAD == 1) 
{
if (InStr (A_LoopField20 , Chr (123))) 
{
insideBracket1 = 1;
}
if (insideBracket1 == 1 && InStr (A_LoopField20 , Chr (123))) 
{
netsedCurly1++;
}
if (insideBracket1 == 1 && InStr (A_LoopField20 , Chr (125))) 
{
netsedCurly1--;
readyToEnd1 = 1;
}
if (InStr (A_LoopField20 , Chr (125)) && readyToEnd1 == 1 && netsedCurly1 == 0 && insideBracket == 1) 
{
//MsgBox, % A_LoopField20
eldLoopNestedBADlol = 1;
//out4758686d86d86d86578991a%AIndexLoopCurlyFix% .= A_LoopField20 . std::string("\n")
}
out4758686d86d86d86578991a%AIndexLoopCurlyFix% += A_LoopField20 + std::string("\n");
}
if (inTarget == 1 && dontSaveStr!= 1 && fixLoopLokingForNum!= 1 && insdeAnestedLoopBAD!= 1) 
{
ALoopField = A_LoopField20;
// Replace std::string("A_Index") with or without a following digit with std::string("A_Index") + out1z
ALoopField = RegExReplace ( ALoopField , std::string("A") + Chr ( 95 ) + std::string("Index(?:\\d+)?") , std::string("A") + Chr ( 95 ) + std::string("Index") + out1z ) ;
//ALoopField := StrReplace(ALoopField, std::string("A_LoopField"), std::string("A_LoopField") . AIndexLoopCurlyFix)
out4758686d86d86d86578991a%AIndexLoopCurlyFix% += ALoopField + std::string("\n");
}
if (inTarget == 1 && InStr (A_LoopField20 , Chr (125)) && readyToEnd == 1 && netsedCurly == 0 && weAreDoneHereCurly == 0 && dontSaveStr!= 1 && insdeAnestedLoopBAD!= 1) 
{
//MsgBox, % A_LoopField20
weAreDoneHereCurly = 1;
inTarget = 0;
endBracketDOntPutThere = 1;
//out4758686d86d86d86578991a%AIndexLoopCurlyFix% .= A_LoopField20 . std::string("\n")
}
dontSaveStr = 0;
if (inTarget!= 1 && endBracketDOntPutThere!= 1 && insdeAnestedLoopBAD!= 1) 
{
out4758686d86d86d86578991a%AIndexLoopCurlyFix% += A_LoopField20 + std::string("\n");
}
endBracketDOntPutThere = 0;
if (eldLoopNestedBADlol == 1) 
{
insdeAnestedLoopBAD = 0;
}
}
strstysrstsytTRIMHELP = variables["out4758686d86d86d86578991a" + STR(AIndexLoopCurlyFix)];
strstysrstsytTRIMHELP = StringTrimRight(strstysrstsytTRIMHELP, 1);
//MsgBox, % out4758686d86d86d86578991a%AIndexLoopCurlyFix%
cppCode = strstysrstsytTRIMHELP;
//MsgBox, % jsCode
wasAtanyIfsElseAddAIndexLoopCurlyFix = 1;
}
else
{
inTarget = 0;
insideBracket = 0;
netsedCurly = 0;
eldLoopNestedBADlol = 0;
readyToEnd = 0;
endBracketDOntPutThere = 0;
dontSaveStr = 0;
weAreDoneHereCurly = 0;
DeleayOneCuzOfLoopParse = 0;
fixLoopLokingForNum = 0;
insdeAnestedLoopBAD = 0;
foundTheTopLoop = 0;
out4758686d86d86d86578991a%AIndexLoopCurlyFix% = std::string("");
std::vector<std::string> items21 = LoopParseFunc(cppCode, "\n", "\r");
for (size_t A_Index21 = 1; A_Index21 < items21.size() + 1; A_Index21++)
{
std::string A_LoopField21 = items21[A_Index21 - 1];
if (InStr (A_LoopField21 , fixLoopLokingFor) && insdeAnestedLoopBAD!= 1) 
{
fixLoopLokingForNum = 1;
//MsgBox, do we came here 3
}
if (InStr (A_LoopField21 , std::string("for ")) && weAreDoneHereCurly!= 1 && insdeAnestedLoopBAD!= 1 && fixLoopLokingForNum == 1) 
{
s = StrSplit ( A_LoopField21 , std::string("A") + Chr ( 95 ) + std::string("Index") , 2 ) ;
out1z = s;
s = StrSplit ( out1z , std::string(" ") , 1 ) ;
out1z = Trim ( s ) ;
//MsgBox, % out1z
fixLoopLokingForNum = 0;
//MsgBox, do we came here 4
foundTheTopLoop++;
inTarget = 1;
//MsgBox, % A_LoopField21
dontSaveStr = 1;
ALoopField = A_LoopField21;
//ALoopField := StrReplace(ALoopField, std::string("for (/* Loop parse */"), std::string("for (/* Loop parse */ /* From AHK */"))
DeleayOneCuzOfLoopParse = 1;
out4758686d86d86d86578991a%AIndexLoopCurlyFix% += ALoopField + std::string("\n");
}
if (inTarget == 1 && InStr (A_LoopField21 , Chr (123)) && insdeAnestedLoopBAD!= 1) 
{
insideBracket = 1;
}
if (insideBracket == 1 && InStr (A_LoopField21 , Chr (123)) && insdeAnestedLoopBAD!= 1) 
{
netsedCurly++;
}
if (insideBracket == 1 && InStr (A_LoopField21 , Chr (125)) && insdeAnestedLoopBAD!= 1) 
{
netsedCurly--;
readyToEnd = 1;
}
if (InStr (A_LoopField21 , std::string("for ")) && insdeAnestedLoopBAD!= 1 && foundTheTopLoop >= 2) 
{
insdeAnestedLoopBAD = 1;
insideBracket1 = 0;
netsedCurly1 = 0;
}
if (inTarget == 1) 
{
foundTheTopLoop++;
}
if (insdeAnestedLoopBAD == 1) 
{
if (InStr (A_LoopField21 , Chr (123))) 
{
insideBracket1 = 1;
}
if (insideBracket1 == 1 && InStr (A_LoopField21 , Chr (123))) 
{
netsedCurly1++;
}
if (insideBracket1 == 1 && InStr (A_LoopField21 , Chr (125))) 
{
netsedCurly1--;
readyToEnd1 = 1;
}
if (InStr (A_LoopField21 , Chr (125)) && readyToEnd1 == 1 && netsedCurly1 == 0 && insideBracket == 1) 
{
//MsgBox, % A_LoopField21
eldLoopNestedBADlol = 1;
//out4758686d86d86d86578991a%AIndexLoopCurlyFix% .= A_LoopField21 . std::string("\n")
}
out4758686d86d86d86578991a%AIndexLoopCurlyFix% += A_LoopField21 + std::string("\n");
}
if (inTarget == 1 && dontSaveStr!= 1 && fixLoopLokingForNum!= 1 && insdeAnestedLoopBAD!= 1) 
{
ALoopField = A_LoopField21;
// Replace std::string("A_Index") with or without a following digit with std::string("A_Index") + out1z
ALoopField = RegExReplace ( ALoopField , std::string("A") + Chr ( 95 ) + std::string("Index(?:\\d+)?") , std::string("A") + Chr ( 95 ) + std::string("Index") + out1z ) ;
// Replace std::string("A_Index") with or without a following digit with std::string("A_Index") + out1z
ALoopField = RegExReplace ( ALoopField , std::string("A") + Chr ( 95 ) + std::string("LoopField(?:\\d+)?") , std::string("A") + Chr ( 95 ) + std::string("LoopField") + out1z ) ;
out4758686d86d86d86578991a%AIndexLoopCurlyFix% += ALoopField + std::string("\n");
}
if (inTarget == 1 && InStr (A_LoopField21 , Chr (125)) && readyToEnd == 1 && netsedCurly == 0 && weAreDoneHereCurly == 0 && dontSaveStr!= 1 && insdeAnestedLoopBAD!= 1) 
{
//MsgBox, % A_LoopField21
weAreDoneHereCurly = 1;
inTarget = 0;
endBracketDOntPutThere = 1;
//out4758686d86d86d86578991a%AIndexLoopCurlyFix% .= A_LoopField21 . std::string("\n")
}
dontSaveStr = 0;
if (inTarget!= 1 && endBracketDOntPutThere!= 1 && insdeAnestedLoopBAD!= 1) 
{
out4758686d86d86d86578991a%AIndexLoopCurlyFix% += A_LoopField21 + std::string("\n");
}
endBracketDOntPutThere = 0;
if (eldLoopNestedBADlol == 1) 
{
insdeAnestedLoopBAD = 0;
}
}
strstysrstsytTRIMHELP = variables["out4758686d86d86d86578991a" + STR(AIndexLoopCurlyFix)];
strstysrstsytTRIMHELP = StringTrimRight(strstysrstsytTRIMHELP, 1);
//MsgBox, % out4758686d86d86d86578991a%AIndexLoopCurlyFix%
cppCode = strstysrstsytTRIMHELP;
//MsgBox, % jsCode
wasAtanyIfsElseAddAIndexLoopCurlyFix = 1;
}
if (wasAtanyIfsElseAddAIndexLoopCurlyFix == 1) 
{
AIndexLoopCurlyFix++;
wasAtanyIfsElseAddAIndexLoopCurlyFix = 0;
}
}
out4758686d86dgt8r754444444 = std::string("");
hold = 0;
std::vector<std::string> items22 = LoopParseFunc(cppCode, "\n", "\r");
for (size_t A_Index22 = 1; A_Index22 < items22.size() + 1; A_Index22++)
{
std::string A_LoopField22 = items22[A_Index22 - 1];
ignore = 0;
if (InStr (A_LoopField22 , std::string("for "))) 
{
if (hold == 1 && holdText == A_LoopField22) 
{
ignore = 1;
}
else
{
holdText = A_LoopField22;
hold = 1;
}
}
if (!(ignore)) 
{
out4758686d86dgt8r754444444 += A_LoopField22 + std::string("\n");
}
}
out4758686d86dgt8r754444444 = StringTrimRight(out4758686d86dgt8r754444444, 1);
cppCode = out4758686d86dgt8r754444444;
}
pyCodeOut1234565432 = std::string("");
std::vector<std::string> items23 = LoopParseFunc(cppCode, "\n", "\r");
for (size_t A_Index23 = 1; A_Index23 < items23.size() + 1; A_Index23++)
{
std::string A_LoopField23 = items23[A_Index23 - 1];
out = A_LoopField23;
if (!(InStr (out , std::string("|itsaersdtgtgfergsdgfsegdfsedAA|")))) 
{
pyCodeOut1234565432 += out + std::string("\n");
}
}
cppCode = StringTrimRight(pyCodeOut1234565432, 1);
cppCodeOutOneLastFixFixFIX = std::string("");
std::vector<std::string> items24 = LoopParseFunc(cppCode, std::string(" "));
for (size_t A_Index24 = 1; A_Index24 < items24.size() + 1; A_Index24++)
{
std::string A_LoopField24 = items24[A_Index24 - 1];
sstr1 = A_LoopField24;
sstr1 = StrReplace ( sstr1 , std::string("A_TickCount") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_TickCount") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("A_Now") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_Now") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("A_YYYY") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_YYYY") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("A_MMMM") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_MMMM") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("A_MMM") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_MMM") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("A_MM") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_MM") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("A_DDDD") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_DDDD") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("A_DDD") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_DDD") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("A_DD") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_DD") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("A_Hour") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_Hour") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("A_Min") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_Min") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("A_Sec") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_Sec") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("A_Space") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_Space") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("A_Tab") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_Tab") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("BuildInVars(") + Chr ( 34 ) + std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_DD") + Chr ( 34 ) + std::string(")D") + Chr ( 34 ) + std::string(")") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_DDD") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("BuildInVars(") + Chr ( 34 ) + std::string("BuildInVars(") + Chr ( 34 ) + std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_DD") + Chr ( 34 ) + std::string(")D") + Chr ( 34 ) + std::string(")D") + Chr ( 34 ) + std::string(")") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_DDDD") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("BuildInVars(") + Chr ( 34 ) + std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_DDD") + Chr ( 34 ) + std::string(")D") + Chr ( 34 ) + std::string(")") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_DDDD") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("BuildInVars(") + Chr ( 34 ) + std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_MM") + Chr ( 34 ) + std::string(")M") + Chr ( 34 ) + std::string(")") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_MMM") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("BuildInVars(") + Chr ( 34 ) + std::string("BuildInVars(") + Chr ( 34 ) + std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_MM") + Chr ( 34 ) + std::string(")M") + Chr ( 34 ) + std::string(")M") + Chr ( 34 ) + std::string(")") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_MMMM") + Chr ( 34 ) + std::string(")") ) ;
sstr1 = StrReplace ( sstr1 , std::string("BuildInVars(") + Chr ( 34 ) + std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_MMM") + Chr ( 34 ) + std::string(")M") + Chr ( 34 ) + std::string(")") , std::string("BuildInVars(") + Chr ( 34 ) + std::string("A_MMMM") + Chr ( 34 ) + std::string(")") ) ;
cppCodeOutOneLastFixFixFIX += sstr1 + std::string(" ");
}
cppCode = StringTrimRight(cppCodeOutOneLastFixFixFIX, 1);
for (int A_Index25 = 1; A_Index25<= theIdNumOfThe34; ++A_Index25)
{
cppCode = StrReplace ( cppCode , std::string("ihuiuuhuuhtheidFor--asas-theuhturtyphoutr-") + Chr ( 65 ) + Chr ( 65 ) + std::string(() A_Index25 ) + Chr ( 65 ) + Chr ( 65 ) , std::string("std::string(") + variables["theIdNumOfThe34theVar" + STR(A_Index25)] + std::string(")") ) ;
}
cppCodeFixCharRemoveStd = std::string("");
std::vector<std::string> items26 = LoopParseFunc(cppCode, "\n", "\r");
for (size_t A_Index26 = 1; A_Index26 < items26.size() + 1; A_Index26++)
{
std::string A_LoopField26 = items26[A_Index26 - 1];
if (SubStr (Trim (StrLower (A_LoopField26)) , 1 , 12) == std::string("const char* ")) 
{
cppCodeFixCharRemoveStd123 = A_LoopField26;
cppCodeFixCharRemoveStd123 = StrReplace ( cppCodeFixCharRemoveStd123 , std::string("std::string(") , std::string("") ) ;
cppCodeFixCharRemoveStd123 = StrReplace ( cppCodeFixCharRemoveStd123 , std::string(")") , std::string("") ) ;
cppCodeFixCharRemoveStd += cppCodeFixCharRemoveStd123 + std::string("\n");
}
else
{
cppCodeFixCharRemoveStd += A_LoopField26 + std::string("\n");
}
}
cppCode = StringTrimRight(cppCodeFixCharRemoveStd, 1);
if (theMainFuncDec == 0) 
{
upCode = std::string("\nint main(int argc, char* argv[])\n{\n");
}
uperCode = std::string("");
uperCodeLibs = std::string("");
uperCodeLibs += std::string("#include <iostream>\n#include <sstream>\n#include <string>\n");
if (InStr (cppCode , std::string("variables["))) 
{
uperCodeLibs += std::string("\n#include <unordered_map>\n#include <string>\n");
uperCode = uperCode + std::string("\n// Define a map to store dynamic variables\n    std::unordered_map<std::string, std::string> variables;\n");
}
if (haveWeEverUsedArrays == 1) 
{
uperCodeLibs += std::string("\n#include <vector>\n#include <string>\n#include <sstream>\n#include <stdexcept>\n");
uperCode = uperCode + std::string("\n// Forward declare OneIndexedArray template\ntemplate <typename T>\nclass OneIndexedArray;\n\n#define OneIndexedArray_DEFINED\n\n// Helper function to set the internal array's size as a string\ntemplate <typename T>\nvoid setInternalArraySize(T& element, size_t size) {\n    element = static_cast<T>(size);\n}\n\n// Specialization for std::string\ntemplate <>\nvoid setInternalArraySize<std::string>(std::string& element, size_t size) {\n    element = std::to_string(size);\n}\n\n// One-indexed dynamic array class\ntemplate <typename T>\nclass OneIndexedArray {\nprivate:\n    std::vector<T> internalArray;\n\npublic:\n    OneIndexedArray() {\n        internalArray.push_back(T{}); // Placeholder for element count\n    }\n\n    void add(const T& newElement) {\n        internalArray.push_back(newElement);\n        setInternalArraySize(internalArray[0], internalArray.size() - 1);\n    }\n\n    void setArray(const std::vector<T>& newArray) {\n        internalArray.resize(newArray.size() + 1);\n        std::copy(newArray.begin(), newArray.end(), internalArray.begin() + 1);\n        setInternalArraySize(internalArray[0], newArray.size());\n    }\n\n    T& operator[](size_t index) {\n        if (index >= internalArray.size()) {\n            internalArray.resize(index + 1);\n            setInternalArraySize(internalArray[0], internalArray.size() - 1);\n        }\n        return internalArray[index];\n    }\n\n    const T& operator[](size_t index) const {\n        if (index >= internalArray.size()) {\n            throw std::out_of_range(") + Chr ( 34 ) + std::string("Index out of range") + Chr ( 34 ) + std::string(");\n        }\n        return internalArray[index];\n    }\n\n    size_t size() const {\n        return static_cast<size_t>(internalArray.size() - 1);\n    }\n};\n\n// Function to split text into words based on a delimiter\nstd::vector<std::string> split(const std::string& text, const std::string& delimiter) {\n    std::vector<std::string> words;\n    std::istringstream stream(text);\n    std::string word;\n    while (std::getline(stream, word, delimiter[0])) { // assuming single character delimiter\n        words.push_back(word);\n    }\n    return words;\n}\n\n// Function to split text into a OneIndexedArray\nOneIndexedArray<std::string> arrSplit(const std::string& text, const std::string& delimiter) {\n    OneIndexedArray<std::string> array;\n    std::vector<std::string> words = split(text, delimiter);\n    array.setArray(words);\n    return array;\n}\n");
}
if (InStr (cppCode , std::string("INT(")) || InStr (cppCode , std::string("INT ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n#include <sstream>\n");
uperCode = uperCode + std::string("\n// Convert std::string to int\nint INT(const std::string& str) {\n    std::istringstream iss(str);\n    int value;\n    iss >> value;\n    return value;\n}\n");
}
if (InStr (cppCode , std::string("STR(")) || InStr (cppCode , std::string("STR ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n#include <string>\n");
uperCode = uperCode + std::string("\n// Convert various types to std::string\nstd::string STR(int value) {\n    return std::to_string(value);\n}\n\nstd::string STR(float value) {\n    return std::to_string(value);\n}\n\nstd::string STR(double value) {\n    return std::to_string(value);\n}\n\nstd::string STR(size_t value) {\n    return std::to_string(value);\n}\n\nstd::string STR(bool value) {\n    return value ? ") + Chr ( 34 ) + std::string("1") + Chr ( 34 ) + std::string(" : ") + Chr ( 34 ) + std::string("0") + Chr ( 34 ) + std::string(";\n}\n");
}
if (InStr (cppCode , std::string("FLOAT(")) || InStr (cppCode , std::string("FLOAT ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n#include <sstream>\n");
uperCode = uperCode + std::string("\n// Convert std::string to float\nfloat FLOAT(const std::string& str) {\n    std::istringstream iss(str);\n    float value;\n    iss >> value;\n    return value;\n}\n");
}
if (InStr (cppCode , std::string("InStr(")) || InStr (cppCode , std::string("InStr ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n");
uperCode = uperCode + std::string("\n// Function to check if needle exists in haystack (std::string overload)\nbool InStr(const std::string& haystack, const std::string& needle) {\n    return haystack.find(needle) != std::string::npos;\n}\n");
}
if (InStr (cppCode , std::string("Random(")) || InStr (cppCode , std::string("Random ("))) 
{
uperCodeLibs += std::string("\n#include <cstdlib>\n#include <ctime>\n");
uperCode = uperCode + std::string("\n// Function to generate a random integer within a specified range [min, max]\nint Random(int min, int max) {\n    // Seed the random number generator with the current time\n    std::srand(std::time(0));\n    \n    // Generate a random number within the specified range\n    int range = max - min + 1;\n    int randomNumber = std::rand() % range + min;\n    \n    return randomNumber;\n}\n\n");
}
if (InStr (cppCode , std::string("Sleep(")) || InStr (cppCode , std::string("Sleep ("))) 
{
uperCodeLibs += std::string("\n#include <thread>\n#include <chrono>\n");
uperCode = uperCode + std::string("\n// Function to sleep for a specified number of milliseconds\nvoid Sleep(int milliseconds) {\n    std::this_thread::sleep_for(std::chrono::milliseconds(milliseconds));\n}\n\n");
}
if (InStr (cppCode , std::string("input(")) || InStr (cppCode , std::string("input ("))) 
{
uperCodeLibs += std::string("\n#include <iostream>\n#include <string>\n");
uperCode = uperCode + std::string("\n// Function to get input from the user, similar to Python's input() function\nstd::string input(const std::string& prompt) {\n    std::string userInput;\n    std::cout << prompt; // Display the prompt to the user\n    std::getline(std::cin, userInput); // Get the entire line of input\n    return userInput;\n}\n\n");
}
if (InStr (cppCode , std::string("LoopParseFunc(")) || InStr (cppCode , std::string("LoopParseFunc ("))) 
{
uperCodeLibs += std::string("\n#include <vector>\n#include <string>\n#include <regex>\n");
uperCode = uperCode + std::string("\n// Function to escape special characters for regex\nstd::string escapeRegex(const std::string& str) {\n    static const std::regex specialChars{R") + Chr ( 34 ) + std::string("([-[") + Chr ( 92 ) + std::string("]{}()*+?.,") + Chr ( 92 ) + std::string("^$|#") + Chr ( 92 ) + std::string("s])") + Chr ( 34 ) + std::string("};\n    return std::regex_replace(str, specialChars, R") + Chr ( 34 ) + std::string("(") + Chr ( 92 ) + std::string("$&)") + Chr ( 34 ) + std::string(");\n}\n\n// Function to split a string based on delimiters\nstd::vector<std::string> LoopParseFunc(const std::string& var, const std::string& delimiter1 = ") + Chr ( 34 ) + std::string("") + Chr ( 34 ) + std::string(", const std::string& delimiter2 = ") + Chr ( 34 ) + std::string("") + Chr ( 34 ) + std::string(") {\n    std::vector<std::string> items;\n    if (delimiter1.empty() && delimiter2.empty()) {\n        // If no delimiters are provided, return a list of characters\n        for (char c : var) {\n            items.push_back(std::string(1, c));\n        }\n    } else {\n        // Escape delimiters for regex\n        std::string escapedDelimiters = escapeRegex(delimiter1 + delimiter2);\n        // Construct the regular expression pattern for splitting the string\n        std::string pattern = ") + Chr ( 34 ) + std::string("[") + Chr ( 34 ) + std::string(" + escapedDelimiters + ") + Chr ( 34 ) + std::string("]+") + Chr ( 34 ) + std::string(";\n        std::regex regexPattern(pattern);\n        std::sregex_token_iterator iter(var.begin(), var.end(), regexPattern, -1);\n        std::sregex_token_iterator end;\n        while (iter != end) {\n            items.push_back(*iter++);\n        }\n    }\n    return items;\n}\n");
}
if (InStr (cppCode , std::string("print(")) || InStr (cppCode , std::string("print ("))) 
{
uperCodeLibs += std::string("\n#include <iostream>\n#include <string>\n#include <type_traits>\n");
uperCode = uperCode + std::string("\n// Print function that converts all types to string if needed\ntemplate <typename T>\nvoid print(const T& value) {\n    if constexpr (std::is_same_v<T, std::string>) {\n        std::cout << value << std::endl;\n    } else if constexpr (std::is_same_v<T, int>) {\n        std::cout << std::to_string(value) << std::endl;\n    } else if constexpr (std::is_same_v<T, float>) {\n        std::cout << std::to_string(value) << std::endl;\n    } else if constexpr (std::is_same_v<T, double>) {\n        std::cout << std::to_string(value) << std::endl;\n    } else if constexpr (std::is_same_v<T, size_t>) {\n        std::cout << std::to_string(value) << std::endl;\n    } else if constexpr (std::is_same_v<T, bool>) {\n        std::cout << (value ? ") + Chr ( 34 ) + std::string("1") + Chr ( 34 ) + std::string(" : ") + Chr ( 34 ) + std::string("0") + Chr ( 34 ) + std::string(") << std::endl;\n    } \n    #ifdef OneIndexedArray_DEFINED\n    else if constexpr (std::is_base_of_v<OneIndexedArray<std::string>, T>) {\n        for (size_t i = 1; i <= value.size(); ++i) {\n            std::cout << value[i] << std::endl;\n        }\n    } else if constexpr (std::is_base_of_v<OneIndexedArray<int>, T>) {\n        for (size_t i = 1; i <= value.size(); ++i) {\n            std::cout << std::to_string(value[i]) << std::endl;\n        }\n    } else if constexpr (std::is_base_of_v<OneIndexedArray<float>, T>) {\n        for (size_t i = 1; i <= value.size(); ++i) {\n            std::cout << std::to_string(value[i]) << std::endl;\n        }\n    } else if constexpr (std::is_base_of_v<OneIndexedArray<double>, T>) {\n        for (size_t i = 1; i <= value.size(); ++i) {\n            std::cout << std::to_string(value[i]) << std::endl;\n        }\n    }\n    #endif\n    else {\n        std::cout << ") + Chr ( 34 ) + std::string("Unsupported type") + Chr ( 34 ) + std::string(" << std::endl;\n    }\n}\n");
}
if (InStr (cppCode , std::string("FileRead(")) || InStr (cppCode , std::string("FileRead ("))) 
{
uperCodeLibs += std::string("\n#include <fstream>\n#include <string>\n#include <filesystem>\n#include <stdexcept>\n");
uperCode = uperCode + std::string("\nstd::string FileRead(const std::string& path) {\n    std::ifstream file;\n    std::filesystem::path full_path;\n\n    // Check if the file path is an absolute path\n    if (std::filesystem::path(path).is_absolute()) {\n        full_path = path;\n    } else {\n        // If it's not a full path, prepend the current working directory\n        full_path = std::filesystem::current_path() / path;\n    }\n\n    // Open the file\n    file.open(full_path);\n    if (!file.is_open()) {\n        throw std::runtime_error(") + Chr ( 34 ) + std::string("Error: Could not open the file.") + Chr ( 34 ) + std::string(");\n    }\n\n    // Read the file content into a string\n    std::string content;\n    std::string line;\n    while (std::getline(file, line)) {\n        content += line + '") + Chr ( 92 ) + std::string("n';\n    }\n\n    file.close();\n    return content;\n}\n");
}
if (InStr (cppCode , std::string("FileAppend(")) || InStr (cppCode , std::string("FileAppend ("))) 
{
uperCodeLibs += std::string("\n#include <fstream>\n#include <iostream>\n#include <string>\n");
uperCode = uperCode + std::string("\nbool FileAppend(const std::string& content, const std::string& path) {\n    std::ofstream file;\n\n    // Open the file in append mode\n    file.open(path, std::ios::app);\n\n    if (!file.is_open()) {\n        std::cerr << ") + Chr ( 34 ) + std::string("Error: Could not open the file for appending.") + Chr ( 34 ) + std::string(" << std::endl;\n        return false;\n    }\n\n    // Append the content to the file\n    file << content;\n\n    // Close the file\n    file.close();\n\n    return true;\n}\n\n");
}
if (InStr (cppCode , std::string("FileDelete(")) || InStr (cppCode , std::string("FileDelete ("))) 
{
uperCodeLibs += std::string("\n#include <filesystem>\n#include <iostream>\n#include <string>\n");
uperCode = uperCode + std::string("\nbool FileDelete(const std::string& path) {\n    std::filesystem::path file_path(path);\n\n    // Check if the file exists\n    if (!std::filesystem::exists(file_path)) {\n        std::cerr << ") + Chr ( 34 ) + std::string("Error: File does not exist.") + Chr ( 34 ) + std::string(" << std::endl;\n        return false;\n    }\n\n    // Attempt to remove the file\n    if (!std::filesystem::remove(file_path)) {\n        std::cerr << ") + Chr ( 34 ) + std::string("Error: Failed to delete the file.") + Chr ( 34 ) + std::string(" << std::endl;\n        return false;\n    }\n\n    return true;\n}\n");
}
if (InStr (cppCode , std::string("StrLen(")) || InStr (cppCode , std::string("StrLen ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n");
uperCode = uperCode + std::string("\nsize_t StrLen(const std::string& str) {\n    return str.length();\n}\n");
}
if (InStr (cppCode , std::string("Asc(")) || InStr (cppCode , std::string("Asc ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n");
uperCode = uperCode + std::string("\nint Asc(const std::string& str) {\n    if (!str.empty()) {\n        return static_cast<int>(str[0]);\n    }\n    return -1; // Return -1 if the string is empty\n}\n");
}
if (InStr (cppCode , std::string("Abs(")) || InStr (cppCode , std::string("Abs ("))) 
{
uperCodeLibs += std::string("\n#include <cmath>\n");
uperCode = uperCode + std::string("\ndouble Abs(double value) {\n    return std::fabs(value);\n}\n\n");
}
if (InStr (cppCode , std::string("ACos(")) || InStr (cppCode , std::string("ACos ("))) 
{
uperCodeLibs += std::string("\n#include <cmath>\n");
uperCode = uperCode + std::string("\ndouble ACos(double value) {\n    return std::acos(value);\n}\n");
}
if (InStr (cppCode , std::string("ATan(")) || InStr (cppCode , std::string("ATan ("))) 
{
uperCodeLibs += std::string("\n#include <cmath>\n");
uperCode = uperCode + std::string("\ndouble ATan(double value) {\n    return std::atan(value);\n}\n");
}
if (InStr (cppCode , std::string("Ceil(")) || InStr (cppCode , std::string("Ceil ("))) 
{
uperCodeLibs += std::string("\n#include <cmath>\n");
uperCode = uperCode + std::string("\ndouble Ceil(double value) {\n    return std::ceil(value);\n}\n");
}
if (InStr (cppCode , std::string("Cos(")) || InStr (cppCode , std::string("Cos ("))) 
{
uperCodeLibs += std::string("\n#include <cmath>\n");
uperCode = uperCode + std::string("\ndouble Cos(double angle) {\n    return std::cos(angle);\n}\n");
}
if (InStr (cppCode , std::string("Exp(")) || InStr (cppCode , std::string("Exp ("))) 
{
uperCodeLibs += std::string("\n#include <cmath>\n");
uperCode = uperCode + std::string("\ndouble Exp(double value) {\n    return std::exp(value);\n}\n");
}
if (InStr (cppCode , std::string("Ln(")) || InStr (cppCode , std::string("Ln ("))) 
{
uperCodeLibs += std::string("\n#include <cmath>\n");
uperCode = uperCode + std::string("\ndouble Ln(double value) {\n    return std::log(value);\n}\n");
}
if (InStr (cppCode , std::string("Log(")) || InStr (cppCode , std::string("Log ("))) 
{
uperCodeLibs += std::string("\n#include <cmath>\n");
uperCode = uperCode + std::string("\ndouble Log(double value, double base) {\n    return std::log(value) / std::log(base);\n}\n");
}
if (InStr (cppCode , std::string("Round(")) || InStr (cppCode , std::string("Round ("))) 
{
uperCodeLibs += std::string("\n#include <cmath>\n");
uperCode = uperCode + std::string("\ndouble Round(double value) {\n    return std::round(value);\n}\n");
}
if (InStr (cppCode , std::string("Sin(")) || InStr (cppCode , std::string("Sin ("))) 
{
uperCodeLibs += std::string("\n#include <cmath>\n");
uperCode = uperCode + std::string("\ndouble Sin(double angle) {\n    return std::sin(angle);\n}\n");
}
if (InStr (cppCode , std::string("Sqrt(")) || InStr (cppCode , std::string("Sqrt ("))) 
{
uperCodeLibs += std::string("\n#include <cmath>\n");
uperCode = uperCode + std::string("\ndouble Sqrt(double value) {\n    return std::sqrt(value);\n}\n");
}
if (InStr (cppCode , std::string("Tan(")) || InStr (cppCode , std::string("Tan ("))) 
{
uperCodeLibs += std::string("\n#include <cmath>\n");
uperCode = uperCode + std::string("\ndouble Tan(double angle) {\n    return std::tan(angle);\n}\n");
}
if (InStr (cppCode , std::string("SubStr(")) || InStr (cppCode , std::string("SubStr ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n");
uperCode = uperCode + std::string("\nstd::string SubStr(const std::string& str, int startPos, int length = -1) {\n    std::string result;\n    size_t strLen = str.size();\n\n    // Handle negative starting positions\n    if (startPos < 0) {\n        startPos += strLen;\n        if (startPos < 0) startPos = 0;\n    } else {\n        if (startPos > static_cast<int>(strLen)) return ") + Chr ( 34 ) + std::string("") + Chr ( 34 ) + std::string("; // Starting position beyond string length\n        startPos -= 1; // Convert to 0-based index\n    }\n\n    // Handle length\n    if (length < 0) {\n        length = strLen - startPos; // Length to end of string\n    } else if (startPos + length > static_cast<int>(strLen)) {\n        length = strLen - startPos; // Adjust length to fit within the string\n    }\n\n    // Extract substring\n    result = str.substr(startPos, length);\n    return result;\n}\n");
}
if (InStr (cppCode , std::string("Trim(")) || InStr (cppCode , std::string("Trim ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n");
uperCode = uperCode + std::string("\nstd::string Trim(const std::string &inputString) {\n    if (inputString.empty()) return ") + Chr ( 34 ) + std::string("") + Chr ( 34 ) + std::string(";\n\n    size_t start = inputString.find_first_not_of(") + Chr ( 34 ) + std::string(" ") + Chr ( 92 ) + std::string("t") + Chr ( 92 ) + std::string("n") + Chr ( 92 ) + std::string("r") + Chr ( 92 ) + std::string("f") + Chr ( 92 ) + std::string("v") + Chr ( 34 ) + std::string(");\n    size_t end = inputString.find_last_not_of(") + Chr ( 34 ) + std::string(" ") + Chr ( 92 ) + std::string("t") + Chr ( 92 ) + std::string("n") + Chr ( 92 ) + std::string("r") + Chr ( 92 ) + std::string("f") + Chr ( 92 ) + std::string("v") + Chr ( 34 ) + std::string(");\n\n    return (start == std::string::npos) ? ") + Chr ( 34 ) + std::string("") + Chr ( 34 ) + std::string(" : inputString.substr(start, end - start + 1);\n}\n");
}
if (InStr (cppCode , std::string("StrReplace(")) || InStr (cppCode , std::string("StrReplace ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n");
uperCode = uperCode + std::string("\nstd::string StrReplace(const std::string &originalString, const std::string &find, const std::string &replaceWith) {\n    std::string result = originalString;\n    size_t pos = 0;\n\n    while ((pos = result.find(find, pos)) != std::string::npos) {\n        result.replace(pos, find.length(), replaceWith);\n        pos += replaceWith.length();\n    }\n\n    return result;\n}\n");
}
if (InStr (cppCode , std::string("StringTrimLeft(")) || InStr (cppCode , std::string("StringTrimLeft ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n");
uperCode = uperCode + std::string("\nstd::string StringTrimLeft(const std::string &input, int numChars) {\n    return (numChars <= input.length()) ? input.substr(numChars) : input;\n}\n");
}
if (InStr (cppCode , std::string("StringTrimRight(")) || InStr (cppCode , std::string("StringTrimRight ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n");
uperCode = uperCode + std::string("\nstd::string StringTrimRight(const std::string &input, int numChars) {\n    return (numChars <= input.length()) ? input.substr(0, input.length() - numChars) : input;\n}\n");
}
if (InStr (cppCode , std::string("StrLower(")) || InStr (cppCode , std::string("StrLower ("))) 
{
uperCodeLibs += std::string("\n#include <algorithm>\n#include <cctype>\n#include <string>\n");
uperCode = uperCode + std::string("\nstd::string StrLower(const std::string &string) {\n    std::string result = string;\n    std::transform(result.begin(), result.end(), result.begin(), ::tolower);\n    return result;\n}\n");
}
if (InStr (cppCode , std::string("RegExReplace(")) || InStr (cppCode , std::string("RegExReplace ("))) 
{
uperCodeLibs += std::string("\n#include <regex>\n#include <string>\n");
uperCode = uperCode + std::string("\nstd::string RegExReplace(const std::string &inputStr, const std::string &regexPattern, const std::string &replacement) {\n    std::regex regex(regexPattern);\n    return std::regex_replace(inputStr, regex, replacement);\n}\n");
}
if (InStr (cppCode , std::string("StrSplit(")) || InStr (cppCode , std::string("StrSplit ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n");
uperCode = uperCode + std::string("\nstd::string StrSplit(const std::string &inputStr, const std::string &delimiter, int num) {\n    size_t start = 0, end = 0, count = 0;\n\n    while ((end = inputStr.find(delimiter, start)) != std::string::npos) {\n        if (++count == num) {\n            return inputStr.substr(start, end - start);\n        }\n        start = end + delimiter.length();\n    }\n\n    if (count + 1 == num) {\n        return inputStr.substr(start);\n    }\n\n    return ") + Chr ( 34 ) + std::string("") + Chr ( 34 ) + std::string(";\n}\n");
}
if (InStr (cppCode , std::string("Chr(")) || InStr (cppCode , std::string("Chr ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n");
uperCode = uperCode + std::string("\nstd::string Chr(int number) {\n    return (number >= 0 && number <= 0x10FFFF) ? std::string(1, static_cast<char>(number)) : ") + Chr ( 34 ) + std::string("") + Chr ( 34 ) + std::string(";\n}\n\n");
}
if (InStr (cppCode , std::string("Mod(")) || InStr (cppCode , std::string("Mod ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n");
uperCode = uperCode + std::string("\nint Mod(int dividend, int divisor) {\n    return dividend % divisor;\n}\n");
}
if (InStr (cppCode , std::string("Floor(")) || InStr (cppCode , std::string("Floor ("))) 
{
uperCodeLibs += std::string("\n#include <cmath>\n#include <limits>\n");
uperCode = uperCode + std::string("\ndouble Floor(double num) {\n    if (std::isnan(num)) {\n        return std::numeric_limits<double>::quiet_NaN();\n    }\n    return std::floor(num);\n}\n");
}
if (InStr (cppCode , std::string("getDataFromJSON(")) || InStr (cppCode , std::string("getDataFromJSON ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n#include <vector>\n#include <map>\n#include <sstream>\n#include <iomanip>\n#include <stdexcept>\n#include <cctype>\n#include <chrono>\n");
uperCode = uperCode + std::string("\nstd::string trim(const std::string& str) {\n    auto start = str.begin();\n    while (start != str.end() && std::isspace(*start)) {\n        start++;\n    }\n    auto end = str.end();\n    do {\n        end--;\n    } while (std::distance(start, end) > 0 && std::isspace(*end));\n    return std::string(start, end + 1);\n}\n\nclass JSONValue {\npublic:\n    enum Type { Null, Boolean, Number, String, Array, Object };\n\n    JSONValue() : type(Null) {}\n    JSONValue(bool b) : type(Boolean), boolean_value(b) {}\n    JSONValue(double n) : type(Number), number_value(n) {}\n    JSONValue(const std::string& s) : type(String), string_value(s) {}\n    JSONValue(const std::vector<JSONValue>& a) : type(Array), array_value(a) {}\n    JSONValue(const std::map<std::string, JSONValue>& o) : type(Object), object_value(o) {}\n\n    Type getType() const { return type; }\n    bool isNull() const { return type == Null; }\n    bool isBoolean() const { return type == Boolean; }\n    bool isNumber() const { return type == Number; }\n    bool isString() const { return type == String; }\n    bool isArray() const { return type == Array; }\n    bool isObject() const { return type == Object; }\n\n    bool asBoolean() const { return boolean_value; }\n    double asNumber() const { return number_value; }\n    const std::string& asString() const { return string_value; }\n    const std::vector<JSONValue>& asArray() const { return array_value; }\n    const std::map<std::string, JSONValue>& asObject() const { return object_value; }\n\nprivate:\n    Type type;\n    bool boolean_value;\n    double number_value;\n    std::string string_value;\n    std::vector<JSONValue> array_value;\n    std::map<std::string, JSONValue> object_value;\n};\n\nclass JSONParser {\npublic:\n    static JSONValue parse(const std::string& json) {\n        size_t index = 0;\n        return parseValue(json, index);\n    }\n\nprivate:\n    static JSONValue parseValue(const std::string& json, size_t& index) {\n        skipWhitespace(json, index);\n        char c = json[index];\n        if (c == '{') {\n            return parseObject(json, index);\n        } else if (c == '[') {\n            return parseArray(json, index);\n        } else if (c == '") + Chr ( 34 ) + std::string("') {\n            return parseString(json, index);\n        } else if (std::isdigit(c) || c == '-') {\n            return parseNumber(json, index);\n        } else if (c == 't' || c == 'f') {\n            return parseBoolean(json, index);\n        } else if (c == 'n') {\n            return parseNull(json, index);\n        }\n        throw std::runtime_error(") + Chr ( 34 ) + std::string("Invalid JSON") + Chr ( 34 ) + std::string(");\n    }\n\n    static JSONValue parseObject(const std::string& json, size_t& index) {\n        std::map<std::string, JSONValue> object;\n        index++; // Skip '{'\n        skipWhitespace(json, index);\n        if (json[index] == '}') {\n            index++;\n            return JSONValue(object);\n        }\n        while (true) {\n            std::string key = parseString(json, index).asString();\n            skipWhitespace(json, index);\n            if (json[index] != ':') throw std::runtime_error(") + Chr ( 34 ) + std::string("Expected ':'") + Chr ( 34 ) + std::string(");\n            index++;\n            JSONValue value = parseValue(json, index);\n            object[key] = value;\n            skipWhitespace(json, index);\n            if (json[index] == '}') {\n                index++;\n                return JSONValue(object);\n            }\n            if (json[index] != ',') throw std::runtime_error(") + Chr ( 34 ) + std::string("Expected ',' or '}'") + Chr ( 34 ) + std::string(");\n            index++;\n            skipWhitespace(json, index);\n        }\n    }\n\n    static JSONValue parseArray(const std::string& json, size_t& index) {\n        std::vector<JSONValue> array;\n        index++; // Skip '['\n        skipWhitespace(json, index);\n        if (json[index] == ']') {\n            index++;\n            return JSONValue(array);\n        }\n        while (true) {\n            array.push_back(parseValue(json, index));\n            skipWhitespace(json, index);\n            if (json[index] == ']') {\n                index++;\n                return JSONValue(array);\n            }\n            if (json[index] != ',') throw std::runtime_error(") + Chr ( 34 ) + std::string("Expected ',' or ']'") + Chr ( 34 ) + std::string(");\n            index++;\n            skipWhitespace(json, index);\n        }\n    }\n\n    static JSONValue parseString(const std::string& json, size_t& index) {\n        index++; // Skip opening quote\n        std::string result;\n        while (json[index] != '") + Chr ( 34 ) + std::string("') {\n            if (json[index] == '") + Chr ( 92 ) + std::string("") + Chr ( 92 ) + std::string("') {\n                index++;\n                switch (json[index]) {\n                    case '") + Chr ( 34 ) + std::string("': result += '") + Chr ( 34 ) + std::string("'; break;\n                    case '") + Chr ( 92 ) + std::string("") + Chr ( 92 ) + std::string("': result += '") + Chr ( 92 ) + std::string("") + Chr ( 92 ) + std::string("'; break;\n                    case '/': result += '/'; break;\n                    case 'b': result += '") + Chr ( 92 ) + std::string("b'; break;\n                    case 'f': result += '") + Chr ( 92 ) + std::string("f'; break;\n                    case 'n': result += '") + Chr ( 92 ) + std::string("n'; break;\n                    case 'r': result += '") + Chr ( 92 ) + std::string("r'; break;\n                    case 't': result += '") + Chr ( 92 ) + std::string("t'; break;\n                    default: throw std::runtime_error(") + Chr ( 34 ) + std::string("Invalid escape sequence") + Chr ( 34 ) + std::string(");\n                }\n            } else {\n                result += json[index];\n            }\n            index++;\n        }\n        index++; // Skip closing quote\n        return JSONValue(result);\n    }\n\n    static JSONValue parseNumber(const std::string& json, size_t& index) {\n        size_t start = index;\n        while (std::isdigit(json[index]) || json[index] == '-' || json[index] == '.' || json[index] == 'e' || json[index] == 'E') {\n            index++;\n        }\n        return JSONValue(std::stod(json.substr(start, index - start)));\n    }\n\n    static JSONValue parseBoolean(const std::string& json, size_t& index) {\n        if (json.substr(index, 4) == ") + Chr ( 34 ) + std::string("true") + Chr ( 34 ) + std::string(") {\n            index += 4;\n            return JSONValue(true);\n        } else if (json.substr(index, 5) == ") + Chr ( 34 ) + std::string("false") + Chr ( 34 ) + std::string(") {\n            index += 5;\n            return JSONValue(false);\n        }\n        throw std::runtime_error(") + Chr ( 34 ) + std::string("Invalid boolean value") + Chr ( 34 ) + std::string(");\n    }\n\n    static JSONValue parseNull(const std::string& json, size_t& index) {\n        if (json.substr(index, 4) == ") + Chr ( 34 ) + std::string("null") + Chr ( 34 ) + std::string(") {\n            index += 4;\n            return JSONValue();\n        }\n        throw std::runtime_error(") + Chr ( 34 ) + std::string("Invalid null value") + Chr ( 34 ) + std::string(");\n    }\n\n    static void skipWhitespace(const std::string& json, size_t& index) {\n        while (index < json.length() && std::isspace(json[index])) {\n            index++;\n        }\n    }\n};\n\nstd::string getDataFromJSON(const std::string& json_data, const std::string& json_path) {\n    JSONValue root = JSONParser::parse(json_data);\n    std::istringstream path_stream(json_path);\n    std::string segment;\n    JSONValue current = root;\n\n    while (std::getline(path_stream, segment, '.')) {\n        segment = trim(segment);\n        \n        size_t bracket_pos = segment.find('[');\n        if (bracket_pos != std::string::npos) {\n            std::string key = segment.substr(0, bracket_pos);\n            size_t index = std::stoi(segment.substr(bracket_pos + 1, segment.find(']') - bracket_pos - 1));\n            \n            if (current.isObject() && current.asObject().find(key) != current.asObject().end()) {\n                current = current.asObject().at(key);\n                if (current.isArray() && index < current.asArray().size()) {\n                    current = current.asArray()[index];\n                } else {\n                    return ") + Chr ( 34 ) + std::string("Array index out of bounds") + Chr ( 34 ) + std::string(";\n                }\n            } else {\n                return ") + Chr ( 34 ) + std::string("Key not found: ") + Chr ( 34 ) + std::string(" + key;\n            }\n        } else if (current.isObject() && current.asObject().find(segment) != current.asObject().end()) {\n            current = current.asObject().at(segment);\n        } else {\n            return ") + Chr ( 34 ) + std::string("Key not found: ") + Chr ( 34 ) + std::string(" + segment;\n        }\n    }\n\n    if (current.isString()) return current.asString();\n    if (current.isNumber()) {\n        double num = current.asNumber();\n        if (num == std::floor(num)) {\n            // It's an integer\n            return std::to_string(static_cast<long long>(num));\n        } else {\n            // It's a floating-point number\n            return std::to_string(num);\n        }\n    }\n    if (current.isBoolean()) return current.asBoolean() ? ") + Chr ( 34 ) + std::string("true") + Chr ( 34 ) + std::string(" : ") + Chr ( 34 ) + std::string("false") + Chr ( 34 ) + std::string(";\n    if (current.isNull()) return ") + Chr ( 34 ) + std::string("null") + Chr ( 34 ) + std::string(";\n    \n    return ") + Chr ( 34 ) + std::string("Unsupported value type") + Chr ( 34 ) + std::string(";\n}\n");
}
if (InStr (cppCode , std::string("GetParams(")) || InStr (cppCode , std::string("GetParams ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n#include <vector>\n#include <filesystem>\n");
uperCode = uperCode + std::string("\n// Function to get command-line parameters\nstd::string GetParams() {\n    std::vector<std::string> params;\n    for (int i = 1; i < __argc; ++i) {\n        std::string arg = __argv[i];\n        if (std::filesystem::exists(arg)) {\n            arg = std::filesystem::absolute(arg).string();\n        }\n        params.push_back(arg);\n    }\n    std::string result;\n    for (const auto& param : params) {\n        result += param + ") + Chr ( 34 ) + std::string("") + Chr ( 92 ) + std::string("n") + Chr ( 34 ) + std::string(";\n    }\n    return result;\n}\n");
}
if (InStr (cppCode , std::string("BuildInVars(")) || InStr (cppCode , std::string("BuildInVars ("))) 
{
uperCodeLibs += std::string("\n#include <iostream>\n#include <chrono>\n#include <ctime>\n#include <sstream>\n#include <iomanip>\n#include <string>\n#include <limits>\n");
uperCode = uperCode + std::string("\n// Store the start time as a global variable\nstd::chrono::time_point<std::chrono::steady_clock> programStartTime = std::chrono::steady_clock::now();\n\n// Function to get built-in variables\nstd::string BuildInVars(const std::string& varName) {\n    auto now = std::chrono::system_clock::now();\n    std::time_t currentTime = std::chrono::system_clock::to_time_t(now);\n    std::tm* localTime = std::localtime(&currentTime);\n\n    std::ostringstream oss;\n\n    if (varName == ") + Chr ( 34 ) + std::string("A_TickCount") + Chr ( 34 ) + std::string(") {\n        // Calculate milliseconds since program start\n        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now() - programStartTime).count();\n        if (duration > std::numeric_limits<int>::max()) {\n            // Handle overflow case\n            return ") + Chr ( 34 ) + std::string("Value too large") + Chr ( 34 ) + std::string(";\n        } else {\n            return std::to_string(static_cast<int>(duration));\n        }\n    } else if (varName == ") + Chr ( 34 ) + std::string("A_Now") + Chr ( 34 ) + std::string(") {\n        oss << std::put_time(localTime, ") + Chr ( 34 ) + std::string("%Y-%m-%d %H:%M:%S") + Chr ( 34 ) + std::string(");\n    } else if (varName == ") + Chr ( 34 ) + std::string("A_YYYY") + Chr ( 34 ) + std::string(") {\n        oss << std::put_time(localTime, ") + Chr ( 34 ) + std::string("%Y") + Chr ( 34 ) + std::string(");\n    } else if (varName == ") + Chr ( 34 ) + std::string("A_MM") + Chr ( 34 ) + std::string(") {\n        oss << std::put_time(localTime, ") + Chr ( 34 ) + std::string("%m") + Chr ( 34 ) + std::string(");\n    } else if (varName == ") + Chr ( 34 ) + std::string("A_DD") + Chr ( 34 ) + std::string(") {\n        oss << std::put_time(localTime, ") + Chr ( 34 ) + std::string("%d") + Chr ( 34 ) + std::string(");\n    } else if (varName == ") + Chr ( 34 ) + std::string("A_MMMM") + Chr ( 34 ) + std::string(") {\n        oss << std::put_time(localTime, ") + Chr ( 34 ) + std::string("%B") + Chr ( 34 ) + std::string(");\n    } else if (varName == ") + Chr ( 34 ) + std::string("A_MMM") + Chr ( 34 ) + std::string(") {\n        oss << std::put_time(localTime, ") + Chr ( 34 ) + std::string("%b") + Chr ( 34 ) + std::string(");\n    } else if (varName == ") + Chr ( 34 ) + std::string("A_DDDD") + Chr ( 34 ) + std::string(") {\n        oss << std::put_time(localTime, ") + Chr ( 34 ) + std::string("%A") + Chr ( 34 ) + std::string(");\n    } else if (varName == ") + Chr ( 34 ) + std::string("A_DDD") + Chr ( 34 ) + std::string(") {\n        oss << std::put_time(localTime, ") + Chr ( 34 ) + std::string("%a") + Chr ( 34 ) + std::string(");\n    } else if (varName == ") + Chr ( 34 ) + std::string("A_Hour") + Chr ( 34 ) + std::string(") {\n        oss << std::put_time(localTime, ") + Chr ( 34 ) + std::string("%H") + Chr ( 34 ) + std::string(");\n    } else if (varName == ") + Chr ( 34 ) + std::string("A_Min") + Chr ( 34 ) + std::string(") {\n        oss << std::put_time(localTime, ") + Chr ( 34 ) + std::string("%M") + Chr ( 34 ) + std::string(");\n    } else if (varName == ") + Chr ( 34 ) + std::string("A_Sec") + Chr ( 34 ) + std::string(") {\n        oss << std::put_time(localTime, ") + Chr ( 34 ) + std::string("%S") + Chr ( 34 ) + std::string(");\n    } else if (varName == ") + Chr ( 34 ) + std::string("A_Space") + Chr ( 34 ) + std::string(") {\n        return ") + Chr ( 34 ) + std::string(" ") + Chr ( 34 ) + std::string(";\n    } else if (varName == ") + Chr ( 34 ) + std::string("A_Tab") + Chr ( 34 ) + std::string(") {\n        return ") + Chr ( 34 ) + std::string("") + Chr ( 92 ) + std::string("t") + Chr ( 34 ) + std::string(";\n    } else {\n        return ") + Chr ( 34 ) + std::string("") + Chr ( 34 ) + std::string(";\n    }\n    return oss.str();\n}\n");
}
if (InStr (cppCode , std::string("RegExReplace(")) || InStr (cppCode , std::string("RegExReplace ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n#include <regex>\n#include <iostream>\n");
uperCode = uperCode + std::string("\n// Function to perform regex replacement\nstd::string RegExReplace(const std::string& inputStr, const std::string& regexPattern, const std::string& replacement) {\n    std::regex re(regexPattern, std::regex_constants::ECMAScript | std::regex_constants::multiline);\n    return std::regex_replace(inputStr, re, replacement);\n}\n");
}
if (InStr (cppCode , std::string("RunCMD(")) || InStr (cppCode , std::string("RunCMD ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n#include <array>\n#include <memory>\n#include <stdexcept>\n#include <cstdio>\n");
uperCode = uperCode + std::string("\n// Function to run a system command\nstd::string RunCMD(const std::string& command) {\n    std::array<char, 128> buffer;\n    std::string result;\n#if defined(_WIN32)\n    std::unique_ptr<FILE, decltype(&_pclose)> pipe(_popen(command.c_str(), ") + Chr ( 34 ) + std::string("r") + Chr ( 34 ) + std::string("), _pclose);\n#else\n    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(command.c_str(), ") + Chr ( 34 ) + std::string("r") + Chr ( 34 ) + std::string("), pclose);\n#endif\n    if (!pipe) {\n        throw std::runtime_error(") + Chr ( 34 ) + std::string("popen() failed!") + Chr ( 34 ) + std::string(");\n    }\n    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {\n        result += buffer.data();\n    }\n    return result;\n}\n");
}
if (InStr (cppCode , std::string("RegExMatch(")) || InStr (cppCode , std::string("RegExMatch ("))) 
{
uperCodeLibs += std::string("\n#include <iostream>\n#include <string>\n#include <regex>\n");
uperCode = uperCode + std::string("\n// Function to perform regex matching and return the match position\nint RegExMatch(const std::string& haystack, const std::string& needleRegEx, std::string* outputVar = nullptr, int startingPos = 0) {\n    if (haystack.empty() || needleRegEx.empty()) {\n        return 0;\n    }\n\n    std::regex re(needleRegEx);\n    std::smatch match;\n\n    if (std::regex_search(haystack.begin() + startingPos, haystack.end(), match, re)) {\n        if (outputVar != nullptr) {\n            *outputVar = match.str(0);\n        }\n        return match.position(0) + 1; // To make it 1-based index\n    }\n\n    return 0;\n}\n");
}
if (InStr (cppCode , std::string("ExitApp(")) || InStr (cppCode , std::string("ExitApp ("))) 
{
uperCodeLibs += std::string("\n#include <iostream>\n#include <cstdlib>\n");
uperCode = uperCode + std::string("\nvoid ExitApp() {\n    std::cout << ") + Chr ( 34 ) + std::string("Exiting application...") + Chr ( 34 ) + std::string(" << std::endl;\n    std::exit(0);\n}\n");
}
if (InStr (cppCode , std::string("SetTimer(")) || InStr (cppCode , std::string("SetTimer ("))) 
{
uperCodeLibs += std::string("\n#include <iostream>\n#include <map>\n#include <functional>\n#include <chrono>\n#include <mutex>\n#include <string>\n#include <sstream>\n#include <atomic>\n#include <thread>\n");
uperCode = uperCode + std::string("\n// Structure to store timer information\nstruct TimerInfo {\n    std::function<void()> func;\n    int interval_ms;\n    bool active;\n    std::chrono::steady_clock::time_point last_execution;\n};\n\n// Maps to store the timers and their states\nstd::map<std::string, TimerInfo> timers;\nstd::mutex mtx; // Mutex for synchronizing access to shared data\nstd::atomic<bool> should_exit(false); // Flag to signal the application to exit\n\nvoid TimerManager() {\n    while (!should_exit) {\n        auto now = std::chrono::steady_clock::now();\n        {\n            std::lock_guard<std::mutex> lock(mtx);\n            bool any_active_timers = false;\n            for (auto& [name, timer] : timers) {\n                if (timer.active) {\n                    any_active_timers = true;\n                    auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(now - timer.last_execution);\n                    if (elapsed.count() >= timer.interval_ms) {\n                        timer.func();\n                        timer.last_execution = now;\n                    }\n                }\n            }\n            if (!any_active_timers) {\n                should_exit = true;\n            }\n        }\n        std::this_thread::sleep_for(std::chrono::milliseconds(10)); // Sleep for a short period to reduce CPU usage\n    }\n}\n\n// Global counter for unique timer names\nstatic int timer_counter = 0;\n\nvoid SetTimer(const std::function<void()>& func, const std::string& timeOrOnOff) {\n    std::lock_guard<std::mutex> lock(mtx); // Lock for safe access to shared data\n\n    // Create a unique identifier for the timer\n    std::string name = ") + Chr ( 34 ) + std::string("timer_") + Chr ( 34 ) + std::string(" + std::to_string(timer_counter++);\n\n    if (timeOrOnOff == ") + Chr ( 34 ) + std::string("On") + Chr ( 34 ) + std::string(") {\n        timers[name] = {func, 10, true, std::chrono::steady_clock::now()};\n    } else if (timeOrOnOff == ") + Chr ( 34 ) + std::string("Off") + Chr ( 34 ) + std::string(") {\n        // Find the timer with the matching function and turn it off\n        for (auto& [timer_name, timer] : timers) {\n            if (timer.func.target_type() == func.target_type() && timer.active) {\n                timer.active = false;\n                break;\n            }\n        }\n    } else {\n        try {\n            int interval_ms = std::stoi(timeOrOnOff);\n            timers[name] = {func, interval_ms, true, std::chrono::steady_clock::now()};\n        } catch (const std::invalid_argument&) {\n            std::cerr << ") + Chr ( 34 ) + std::string("Invalid interval value: ") + Chr ( 34 ) + std::string(" << timeOrOnOff << std::endl;\n        }\n    }\n}\n");
}
if (InStr (cppCode , std::string("getDataFromAPI(")) || InStr (cppCode , std::string("getDataFromAPI ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n#include <array>\n#include <memory>\n#include <stdexcept>\n#include <cstdio>\n");
uperCode = uperCode + std::string("\n// Function to run a system command\nstd::string getDataFromAPIRunCMD(const std::string& command) {\n    std::array<char, 128> buffer;\n    std::string result;\n#if defined(_WIN32)\n    std::unique_ptr<FILE, decltype(&_pclose)> pipe(_popen(command.c_str(), ") + Chr ( 34 ) + std::string("r") + Chr ( 34 ) + std::string("), _pclose);\n#else\n    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(command.c_str(), ") + Chr ( 34 ) + std::string("r") + Chr ( 34 ) + std::string("), pclose);\n#endif\n    if (!pipe) {\n        throw std::runtime_error(") + Chr ( 34 ) + std::string("popen() failed!") + Chr ( 34 ) + std::string(");\n    }\n    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {\n        result += buffer.data();\n    }\n    return result;\n}\n\n\n// Function to fetch data from API\nstd::string getDataFromAPI(const std::string& url) {\n    std::string command = ") + Chr ( 34 ) + std::string("curl -s ") + Chr ( 34 ) + std::string(" + url;\n    return getDataFromAPIRunCMD(command);\n}\n");
}
if (InStr (cppCode , std::string("SortLikeAHK(")) || InStr (cppCode , std::string("SortLikeAHK ("))) 
{
uperCodeLibs += std::string("\n#include <string>\n#include <vector>\n#include <algorithm>\n#include <sstream>\n#include <unordered_set>\n#include <cctype>\n");
uperCode = uperCode + std::string("\n// Helper function to trim whitespace from both ends of a string\nstd::string trim(const std::string& str) {\n    const std::string whitespace = ") + Chr ( 34 ) + std::string(" ") + Chr ( 92 ) + std::string("t") + Chr ( 92 ) + std::string("n") + Chr ( 92 ) + std::string("r") + Chr ( 92 ) + std::string("f") + Chr ( 92 ) + std::string("v") + Chr ( 34 ) + std::string(";\n    size_t start = str.find_first_not_of(whitespace);\n    if (start == std::string::npos) return ") + Chr ( 34 ) + std::string("") + Chr ( 34 ) + std::string(";\n    size_t end = str.find_last_not_of(whitespace);\n    return str.substr(start, end - start + 1);\n}\n\n// Helper function to convert string to lowercase\nstd::string toLower(const std::string& str) {\n    std::string lowerStr = str;\n    std::transform(lowerStr.begin(), lowerStr.end(), lowerStr.begin(), ::tolower);\n    return lowerStr;\n}\n\n// Function to sort case-insensitively but ensure lowercase items come last\nbool customSortCompare(const std::string& a, const std::string& b) {\n    std::string lowerA = toLower(a);\n    std::string lowerB = toLower(b);\n    if (lowerA == lowerB) {\n        // If case-insensitive equivalent, ensure lowercase items come last\n        if (std::islower(a[0]) && std::isupper(b[0])) {\n            return false; // a should come after b\n        } else if (std::isupper(a[0]) && std::islower(b[0])) {\n            return true; // a should come before b\n        }\n        return a < b; // Otherwise, sort lexicographically\n    }\n    return lowerA < lowerB;\n}\n\n// Function to remove exact duplicates (case-sensitive)\nstd::vector<std::string> removeExactDuplicates(const std::vector<std::string>& items) {\n    std::unordered_set<std::string> seen;\n    std::vector<std::string> uniqueItems;\n    for (const auto& item : items) {\n        if (seen.find(item) == seen.end()) {\n            seen.insert(item);\n            uniqueItems.push_back(item);\n        }\n    }\n    return uniqueItems;\n}\n\n// Main sorting function\nstd::string SortLikeAHK(const std::string& input, const std::string& options) {\n    std::string delimiter = ") + Chr ( 34 ) + std::string("") + Chr ( 92 ) + std::string("n") + Chr ( 34 ) + std::string(";\n    bool caseInsensitive = options.find('C') != std::string::npos;\n    bool unique = options.find('U') != std::string::npos;\n    bool reverse = options.find('R') != std::string::npos;\n    bool random = options.find(") + Chr ( 34 ) + std::string("Random") + Chr ( 34 ) + std::string(") != std::string::npos;\n    bool numeric = options.find('N') != std::string::npos;\n\n    // Custom delimiter\n    if (options.find('D') != std::string::npos) {\n        size_t delimiterPos = options.find('D') + 1;\n        if (delimiterPos < options.size()) {\n            delimiter = options.substr(delimiterPos, 1);\n        }\n    }\n\n    // Split input by delimiter\n    std::vector<std::string> items;\n    std::stringstream ss(input);\n    std::string item;\n    while (std::getline(ss, item, delimiter[0])) {\n        item = trim(item);  // Trim whitespace from each item\n        if (!item.empty()) {\n            items.push_back(item);\n        }\n    }\n\n    // Sort items\n    if (numeric) {\n        std::sort(items.begin(), items.end(), [](const std::string& a, const std::string& b) {\n            return std::stoi(a) < std::stoi(b);\n        });\n    } else {\n        std::sort(items.begin(), items.end(), customSortCompare);\n    }\n\n    // Remove exact duplicates if needed\n    if (unique) {\n        items = removeExactDuplicates(items);\n    }\n\n    // Apply reverse order if needed\n    if (reverse) {\n        std::reverse(items.begin(), items.end());\n    }\n\n    // Separate uppercase and lowercase items\n    std::vector<std::string> uppercaseItems;\n    std::vector<std::string> lowercaseItems;\n    \n    for (const auto& item : items) {\n        if (std::isupper(item[0])) {\n            uppercaseItems.push_back(item);\n        } else {\n            lowercaseItems.push_back(item);\n        }\n    }\n\n    // Combine sorted uppercase items with sorted lowercase items\n    std::string result;\n    for (const auto& item : uppercaseItems) {\n        result += item;\n        result += delimiter;\n    }\n    for (const auto& item : lowercaseItems) {\n        result += item;\n        if (&item != &lowercaseItems.back()) {\n            result += delimiter;\n        }\n    }\n\n    // Remove trailing delimiter if necessary\n    if (!result.empty() && result.back() == delimiter[0]) {\n        result.pop_back();\n    }\n\n    return result;\n}\n");
}
uperCodeLibs = SortLikeAHK(uperCodeLibs, "U")
downCode = std::string("\nreturn 0;\n}");
cppCode = uperCodeLibs + std::string("\n") + uperCode + std::string("\n") + upCode + cppCode + downCode;
cppCode = StrReplace ( cppCode , std::string("") , std::string("") ) ;
//MsgBox, % cppCode
filePathOfCode = StringTrimRight(filePathOfCode, 4);
filePathOfCode = filePathOfCode + std::string("cpp");
FileDelete(filePathOfCode);
FileAppend(cppCode, filePathOfCode);

return 0;
}