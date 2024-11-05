#include <algorithm>
#include <array>
#include <atomic>
#include <cctype>
#include <chrono>
#include <cmath>
#include <cstdint>
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
#include <random>
#include <regex>
#include <sstream>
#include <stdexcept>
#include <string>
#include <system_error>
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

// Convert various types to std::string
std::string STR(long long value) {
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

// Function to find the position of needle in haystack (std::string overload)
int InStr(const std::string& haystack, const std::string& needle) {
    size_t pos = haystack.find(needle);
    return (pos != std::string::npos) ? static_cast<int>(pos) + 1 : 0;
}

int Random(int min, int max) {
    // Create a random device to seed the generator
    std::random_device rd;
    
    // Create a generator seeded with the random device
    std::mt19937 gen(rd());
    
    // Define a distribution within the specified range
    std::uniform_int_distribution<> dis(min, max);
    
    // Generate and return a random number within the specified range
    return dis(gen);
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
        return false;
    }

    // Attempt to remove the file
    if (!std::filesystem::remove(file_path)) {
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

// Define your custom ASin function
double ASin(double value) {
    // Ensure the value is within the valid range for asin
    if (value < -1.0 || value > 1.0) {
        std::cerr << "Error: Value out of range for arcsine function." << std::endl;
        return NAN;  // Return 'Not-a-Number' to indicate an error
    }

    return asin(value);  // Call the standard asin function
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

// Function that computes the logarithm with base 10
double Log(double value) {
    return std::log10(value);
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

            if (key.empty()) {
                // This is a direct array access
                if (current.isArray() && index < current.asArray().size()) {
                    current = current.asArray()[index];
                } else {
                    return "Array index out of bounds";
                }
            } else {
                // This is an object access followed by array access
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
        if (num == floor(num)) {
            return std::to_string(static_cast<long long>(num));
        } else {
            return std::to_string(num);
        }
    }
    if (current.isBoolean()) return current.asBoolean() ? "true" : "false";
    if (current.isNull()) return "null";

    return "Unsupported value type";
}

// Platform-specific handling for command-line arguments
#ifdef _WIN32
    #define ARGC __argc
    #define ARGV __argv
#else
    // On Linux/macOS, we need to declare these as extern variables.
    extern char **environ; // Ensure the declaration of `environ`
    int ARGC;
    char** ARGV;

    __attribute__((constructor)) void init_args(int argc, char* argv[], char* envp[]) {
        ARGC = argc;
        ARGV = argv;
    }
#endif

// Function to get command-line parameters
std::string GetParams() {
    std::vector<std::string> params;
    for (int i = 1; i < ARGC; ++i) {
        std::string arg = ARGV[i];
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

// Creates a directory if it does not exist
void FileCreateDir(const std::string& path) {
    try {
        // No need to handle existing directories; create_directory will not throw if it already exists
        std::filesystem::create_directory(path);
    } catch (const std::filesystem::filesystem_error&) {
        // Handle errors silently; do nothing if the directory already exists or other errors occur
    }
}

// Removes a directory if it exists
void FileRemoveDir(const std::string& path) {
    try {
        if (std::filesystem::exists(path) && std::filesystem::is_directory(path)) {
            std::filesystem::remove_all(path);
        }
    } catch (const std::filesystem::filesystem_error&) {
        // Handle errors silently; do nothing if the directory does not exist or other errors occur
    }
}

// Checks if a file or directory exists
bool FileExist(const std::string& path) {
    try {
        return std::filesystem::exists(path);
    } catch (const std::filesystem::filesystem_error&) {
        // Handle errors silently; return false if an error occurs
        return false;
    }
}

// Function to check if the operating system is Windows
bool isWindows() {
    #ifdef _WIN32
        return true;
    #else
        return false;
    #endif
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
isVarAnumKindaVar ( strrrrr ) ;
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
varDetect ( strrrrr ) ;
{
if (InStr (strrrrr , "-")) 
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
isVarAfuncOrWhat ( varInVarTranspiler , funcNames , allVarsChars , allVarsInts ) ;
{
if (InStr (varInVarTranspiler , "%")) 
{
nameOfVarr11 = Trim ( StrSplit ( varInVarTranspiler , "%" , 1 ) ) ;
nameOfVarr12 = Trim ( StrSplit ( varInVarTranspiler , "%" , 2 ) ) ;
if (SubStr (nameOfVarr12 , 1 , 1) == "[") 
{
nameOfVarr12 = StringTrimRight(nameOfVarr12, 1);
nameOfVarr12 = StringTrimLeft(nameOfVarr12, 1);
nameOfVarr111 = "variables[" + Chr ( 34 ) + nameOfVarr11 + Chr ( 34 ) + " + std::string(variables[" + Chr ( 34 ) + nameOfVarr12 + Chr ( 34 ) + "])]";
}
else
{
nameOfVarr111 = "variables[" + Chr ( 34 ) + nameOfVarr11 + Chr ( 34 ) + " + STR(" + nameOfVarr12 + ")]";
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
std::vector<std::string> items9 = LoopParseFunc(funcNames, "|");
for (size_t A_Index9 = 1; A_Index9 < items9.size() + 1; A_Index9++)
{
std::string A_LoopField9 = items9[A_Index9 - 1];
if (varInVarTranspiler == A_LoopField9) 
{
return varInVarTranspiler;
}
if (InStr (Trim (varInVarTranspiler) , A_LoopField9 + "(")) 
{
return varInVarTranspiler;
}
}
if (SubStr (varInVarTranspiler , 1 , 1) == "[") 
{
varInVarTranspiler = StringTrimLeft(varInVarTranspiler, 1);
varInVarTranspiler = StringTrimRight(varInVarTranspiler, 1);
return "variables[" + Chr ( 34 ) + varInVarTranspiler + Chr ( 34 ) + "]";
}
if (varDetect (varInVarTranspiler)) 
{
return varInVarTranspiler;
}
if (isVarAnumKindaVar (varInVarTranspiler)) 
{
return varInVarTranspiler;
}
if (varInVarTranspiler == ".") 
{
return "+";
}
if (varInVarTranspiler == "=") 
{
return "==";
}
if (varInVarTranspiler == "or") 
{
return "||";
}
if (varInVarTranspiler == "and") 
{
return "&&";
}
return varInVarTranspiler;
}
//;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
//;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
//;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
varTranspiler ( var123 , funcNames , allVarsChars , allVarsInts ) ;
{
var123out = "";
lastType = "";
typeMode = 0;
//MsgBox, % var123
var123 = StrReplace ( var123 , ") or (" , " || " ) ;
var123 = StrReplace ( var123 , ") || (" , " || " ) ;
var123 = StrReplace ( var123 , ") and (" , " && " ) ;
var123 = StrReplace ( var123 , ") && (" , " && " ) ;
var123 = StrReplace ( var123 , ")  or  (" , "  ||  " ) ;
var123 = StrReplace ( var123 , ")  ||  (" , "  ||  " ) ;
var123 = StrReplace ( var123 , ")  and  (" , "  &&  " ) ;
var123 = StrReplace ( var123 , ")  &&  (" , "  &&  " ) ;
var123 = StrReplace ( var123 , "," , " , " ) ;
var123 = StrReplace ( var123 , "(" , " ( " ) ;
var123 = StrReplace ( var123 , ")" , " ) " ) ;
std::vector<std::string> items10 = LoopParseFunc(var123, " ");
for (size_t A_Index10 = 1; A_Index10 < items10.size() + 1; A_Index10++)
{
std::string A_LoopField10 = items10[A_Index10 - 1];
if (A_LoopField10 == "int" || A_LoopField10 == "str") 
{
typeMode = 1;
lastType = Trim ( A_LoopField10 ) ;
}
if (A_LoopField10!= "int" && A_LoopField10!= "str" && typeMode == 1) 
{
varInVarTranspiler = Trim ( A_LoopField10 ) ;
varOut2out = isVarAfuncOrWhat ( varInVarTranspiler , funcNames , allVarsChars , allVarsInts ) ;
if (lastType == "int") 
{
varOut2out = "INT(" + varOut2out + ")";
}
if (lastType == "str") 
{
varOut2out = "std::string(" + varOut2out + ")";
}
var123out += std::string(() varOut2out ) + " ";
typeMode = 0;
}
else if (A_LoopField10!= "int" && A_LoopField10!= "str" && typeMode == 0) 
{
varInVarTranspiler = Trim ( A_LoopField10 ) ;
varOut2out = isVarAfuncOrWhat ( varInVarTranspiler , funcNames , allVarsChars , allVarsInts ) ;
var123out += std::string(() varOut2out ) + " ";
}
}
var123out = StringTrimRight(var123out, 1);
return var123out;
}
transpileLowVariables ( sstr ) ;
{
sstr = Trim ( sstr ) ;
outOftranspileVariablesOut = Chr ( 34 ) ;
if (InStr (sstr , Chr (37))) 
{
std::vector<std::string> items11 = LoopParseFunc(sstr, "%");
for (size_t A_Index11 = 1; A_Index11 < items11.size() + 1; A_Index11++)
{
std::string A_LoopField11 = items11[A_Index11 - 1];
if (Mod (A_Index11 , 2)) 
{
outOftranspileVariablesOut += A_LoopField11;
}
else
{
outOftranspileVariablesOut += Chr ( 34 ) + " + variables['" + A_LoopField11 + Chr ( 39 ) + Chr ( 93 ) + " + " + Chr ( 34 ) ;
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
CheckIFandElsesss1 = "if (";
CheckIFandElsesss2 = "if(";
CheckIFandElsesss3 = "if !(";
CheckIFandElsesss4 = "if!(";
CheckIFandElsesss5 = "else if (";
CheckIFandElsesss6 = "else if(";
CheckIFandElsesss7 = "else if !(";
CheckIFandElsesss8 = "else if!(";
CheckIFandElsesssNum = 0;
onceImportTime = 0;
weUseRandomAtLeastOnce = 0;
weEverUseVars = "";
haveWeEverUsedAloop = 0;
usedLib = "";
putEndPointFlask1Up = "";
putEndPointFlask2Down = "";
AindexcharLength = 1;
pycodeAcurlyBraceAddSomeVrasFixNL = 0;
pycodeAcurlyBraceAddSomeVrasFixLP = 0;
pycodeLoopfixa = "";
out = "";
HTpyCodeD1 = "";
skipLeftCuleyForFuncPLS = 0;
eavbnsalvbaslv = 0;
theMainFuncDec = 0;
upCode = "";
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
//MsgBox, % filePathOfCode
//code := FileRead(filePathOfCode)
code = FileRead(filePathOfCode);
//MsgBox, % code
}
if (A_Index12 == 2) 
{
print(A_LoopField12);
}
}
//MsgBox, % code
nothing = "";
code = StrReplace ( code , Chr ( 13 ) , nothing ) ;
codeTrimBeggining = "";
std::vector<std::string> items13 = LoopParseFunc(code, "\n", "\r");
for (size_t A_Index13 = 1; A_Index13 < items13.size() + 1; A_Index13++)
{
std::string A_LoopField13 = items13[A_Index13 - 1];
codeTrimBeggining += Trim ( A_LoopField13 ) + "\n";
}
code = StringTrimRight(codeTrimBeggining, 1);
HTpyCodeOUT754754 = "";
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
HTpyCodeOUT754754 += "ihuiuuhuuhtheidFor--asas-theuhturtyphoutr-" + Chr ( 65 ) + Chr ( 65 ) + std::string(() theIdNumOfThe34 ) + Chr ( 65 ) + Chr ( 65 ) ;
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
allVarsChars = "";
allVarsInts = "";
funcNames = "std::string|INT|STR|FLOAT|arrSplit|LoopParseFunc|InStr|Random|Sleep|input|print|FileRead|StrLower|FileAppend|FileDelete|StrLen|Asc|Abs|ACos|ASin|ATan|Ceil|Cos|Exp|Ln|Log|Round|Sin|Sqrt|Tan|SubStr|Trim|StrReplace|StringTrimLeft|StringTrimRight|StrSplit|Chr|Mod|Floor|getDataFromJSON|GetParams|BuildInVars|RegExReplace|RegExMatch|RunCMD|SetTimer|ExitApp|getDataFromAPI|SortLikeAHK|isWindows|FileCreateDir|FileRemoveDir|FileExist";
//"std::string|INT|STR|FLOAT|arrSplit|LoopParseFunc|InStr|Random|Sleep|input|print|FileRead|FileAppend|FileDelete|StrLen|Asc|Abs|ACos|ATan|Ceil|Cos|Exp|Ln|Log|Round|Sin|Sqrt|Tan|SubStr|Trim|StrReplace|StringTrimLeft|StringTrimRight|RegExReplace|StrSplit|Chr|Mod|Floor|getDataFromJSON|GetParams|BuildInVars|RegExReplace|RegExMatch|RunCMD|SetTimer|getDataFromAPI|SortLikeAHK"
//"input|int|chr|str|InStr|SubStr|Trim|StrReplace|StringTrimLeft|StringTrimRight|StrLower|RegExReplace|StrSplit|Chr|Mod|FileRead|FileAppend|FileDelete|GetParams|RunCMD|SortLikeAHK|BuildInVars|Floor|ExitApp|SetTimer|Abs|ACos|ASin|ATan|Ceil|Cos|Exp|Ln|Log|Round|Sin|Sqrt|Tan|RegExMatch|StrLen|Asc|getDataFromAPI|getDataFromJSON|float"
// func
std::vector<std::string> items17 = LoopParseFunc(code, "\n", "\r");
for (size_t A_Index17 = 1; A_Index17 < items17.size() + 1; A_Index17++)
{
std::string A_LoopField17 = items17[A_Index17 - 1];
if (SubStr (Trim (StrLower (A_LoopField17)) , 1 , 5) == "func ") 
{
funcName123 = StringTrimLeft(A_LoopField17, 5);
funcName123 = Trim ( StrSplit ( funcName123 , "(" , 1 ) ) ;
funcName123 = Trim ( StrSplit ( funcName123 , " " , 2 ) ) ;
funcNames += "|" + funcName123;
}
}
varAssignmentType = "=";
timer_thread = 0;
cppCode = "";
std::vector<std::string> items18 = LoopParseFunc(code, "\n", "\r");
for (size_t A_Index18 = 1; A_Index18 < items18.size() + 1; A_Index18++)
{
std::string A_LoopField18 = items18[A_Index18 - 1];
lineDone = 0;
if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 10) == "msgbox, % ") 
{
msgboxCode = StringTrimLeft(A_LoopField18, 10);
msgboxCode = varTranspiler ( msgboxCode , funcNames , allVarsChars , allVarsInts ) ;
cppCode += "print(" + msgboxCode + ");" + "\n";
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 8) == "msgbox, ") 
{
msgboxCode = StringTrimLeft(A_LoopField18, 8);
cppCode += "print(std::string(" + Chr ( 34 ) + msgboxCode + Chr ( 34 ) + "));" + "\n";
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 1) == ";") 
{
str1234 = StringTrimLeft(A_LoopField18, 1);
cppCode += "//" + str1234 + "\n";
lineDone = 1;
}
else if (SubStr (A_LoopField18 , -1) == "++") 
{
str123 = Trim ( A_LoopField18 ) ;
str123 = StringTrimRight(str123, 2);
out = str123 + "++;";
cppCode += out + "\n";
lineDone = 1;
}
else if (SubStr (A_LoopField18 , -1) == "--") 
{
str123 = Trim ( A_LoopField18 ) ;
str123 = StringTrimRight(str123, 2);
out = str123 + "--;";
cppCode += out + "\n";
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 6) == "sort, ") 
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
s = StrSplit ( str1 , "," , 1 ) ;
out1 = Trim ( s ) ;
s = StrSplit ( str1 , "," , 2 ) ;
out2 = Trim ( s ) ;
if (weHaveAcommaFixSortCommand == 1) 
{
out2 = out2 + Chr ( 44 ) ;
}
var1 = out1 + " = SortLikeAHK(" + out1 + ", " + Chr ( 34 ) + out2 + Chr ( 34 ) + ");";
lineDone = 1;
cppCode += var1 + "\n";
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 10) == "settimer, ") 
{
str1 = StringTrimLeft(A_LoopField18, 10);
str2 = Trim ( StrSplit ( str1 , "," , 1 ) ) ;
str3 = Trim ( StrSplit ( str1 , "," , 2 ) ) ;
if (str3 == "") 
{
str3 = Chr ( 34 ) + "10" + Chr ( 34 ) ;
}
else
{
if (StrLower (str3) == "on") 
{
str3 = Chr ( 34 ) + "On" + Chr ( 34 ) ;
}
else if (StrLower (str3) == "off") 
{
str3 = Chr ( 34 ) + "Off" + Chr ( 34 ) ;
}
else
{
if (RegExMatch (str3 , "^\\d+$")) 
{
str3 = Chr ( 34 ) + str3 + Chr ( 34 ) ;
}
else
{
str3 = "STR(" + str3 + ")";
}
}
}
out1 = "SetTimer(" + str2 + ", " + str3 + ");";
lineDone = 1;
cppCode += out1 + "\n";
}
else if (StrLower (A_LoopField18) == "settimers") 
{
lineDone = 1;
timer_thread++;
cppCode += "std::thread timer_thread" + std::string(() timer_thread ) + "(TimerManager);\n";
}
else if (StrLower (A_LoopField18) == "starttimers") 
{
lineDone = 1;
cppCode += "timer_thread" + std::string(() timer_thread ) + ".join(); // Wait for TimerManager to finish\nshould_exit = false; // Reset the exit flag for the new TimerManager thread\n";
}
else if (Trim (StrLower (A_LoopField18)) == "exitapp") 
{
lineDone = 1;
cppCode += "ExitApp();" + "\n";
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 7) == "gosub, ") 
{
//MsgBox, % A_LoopField18
sstr1 = A_LoopField18;
s = StrSplit ( sstr1 , "," , 2 ) ;
out1 = s;
out1 = Trim ( out1 ) ;
out2 = out1 + "();";
//MsgBox, % out2
lineDone = 1;
cppCode += out2 + "\n";
}
else if (A_LoopField18 == "Return") 
{
cppCode += "}" + "\n";
lineDone = 1;
}
else if (RegExReplace (A_LoopField18 , "^\\w+:$" , "")!= A_LoopField18 && Trim (SubStr (A_LoopField18 , 0)) == ":" && lineDone!= 1 && A_LoopField18!= "main:") 
{
//MsgBox, % A_LoopField18
out1 = A_LoopField18;
out1 = Trim ( out1 ) ;
out1 = StringTrimRight(out1, 1);
lineDone = 1;
cppCode += "void " + out1 + "()\n{\n";
//MsgBox, % out1
//~ MsgBox, % see
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 10) == "fileread, ") 
{
filereadCommand = StringTrimLeft(A_LoopField18, 10);
filereadCommand1varname = StrSplit ( filereadCommand , ", " , 1 ) ;
filereadCommand2path = StrSplit ( filereadCommand , ", " , 2 ) ;
filereadCommand2path = StrReplace ( filereadCommand2path , "\\" , "\\\\" ) ;
if (!(InStr (filereadCommand2path , "%"))) 
{
filereadCommand2path = Trim ( transpileLowVariables ( filereadCommand2path ) ) ;
}
else
{
filereadCommand2path = StrReplace ( filereadCommand2path , "%" , "" ) ;
}
cppCode += filereadCommand1varname + " = FileRead(" + filereadCommand2path + ");\n";
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 12) == "fileappend, ") 
{
fileAppendCommand = StringTrimLeft(A_LoopField18, 12);
fileAppendCommand1varname = StrSplit ( fileAppendCommand , ", " , 1 ) ;
fileAppendCommand2path = StrSplit ( fileAppendCommand , ", " , 2 ) ;
fileAppendCommand2path = StrReplace ( fileAppendCommand2path , "\\" , "\\\\" ) ;
if (!(InStr (fileAppendCommand2path , "%"))) 
{
fileAppendCommand2path = Trim ( transpileLowVariables ( fileAppendCommand2path ) ) ;
}
else
{
fileAppendCommand2path = StrReplace ( fileAppendCommand2path , "%" , "" ) ;
}
fileAppendCommand1varname = StrReplace ( fileAppendCommand1varname , "%" , "" ) ;
cppCode += "FileAppend(" + fileAppendCommand1varname + ", " + fileAppendCommand2path + ");\n";
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 12) == "filedelete, ") 
{
fileDeleteCommand = StringTrimLeft(A_LoopField18, 12);
fileDeleteCommand2path = StrSplit ( fileDeleteCommand , ", " , 1 ) ;
fileDeleteCommand2path = StrReplace ( fileDeleteCommand2path , "\\" , "\\\\" ) ;
if (!(InStr (fileDeleteCommand2path , "%"))) 
{
fileDeleteCommand2path = Trim ( transpileLowVariables ( fileDeleteCommand2path ) ) ;
}
else
{
fileDeleteCommand2path = StrReplace ( fileDeleteCommand2path , "%" , "" ) ;
}
cppCode += "FileDelete(" + fileDeleteCommand2path + ");\n";
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 15) == "filecreatedir, ") 
{
FileCreateDirCommand = StringTrimLeft(A_LoopField18, 15);
FileCreateDirCommand2path = StrSplit ( FileCreateDirCommand , ", " , 1 ) ;
FileCreateDirCommand2path = StrReplace ( FileCreateDirCommand2path , "\\" , "\\\\" ) ;
if (!(InStr (FileCreateDirCommand2path , "%"))) 
{
FileCreateDirCommand2path = Trim ( transpileLowVariables ( FileCreateDirCommand2path ) ) ;
}
else
{
FileCreateDirCommand2path = StrReplace ( FileCreateDirCommand2path , "%" , "" ) ;
}
cppCode += "FileCreateDir(" + FileCreateDirCommand2path + ");\n";
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 15) == "fileremovedir, ") 
{
FileRemoveDirCommand = StringTrimLeft(A_LoopField18, 15);
FileRemoveDirCommand2path = StrSplit ( FileRemoveDirCommand , ", " , 1 ) ;
FileRemoveDirCommand2path = StrReplace ( FileRemoveDirCommand2path , "\\" , "\\\\" ) ;
if (!(InStr (FileRemoveDirCommand2path , "%"))) 
{
FileRemoveDirCommand2path = Trim ( transpileLowVariables ( FileRemoveDirCommand2path ) ) ;
}
else
{
FileRemoveDirCommand2path = StrReplace ( FileRemoveDirCommand2path , "%" , "" ) ;
}
cppCode += "FileRemoveDir(" + FileRemoveDirCommand2path + ");\n";
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 17) == StrLower ("StringTrimRight, ")) 
{
varr1 = StrSplit ( A_LoopField18 , "," , 2 ) ;
varr2 = StrSplit ( A_LoopField18 , "," , 3 ) ;
varr3 = StrSplit ( A_LoopField18 , "," , 4 ) ;
outt1 = Trim ( varTranspiler ( varr1 , funcNames , allVarsChars , allVarsInts ) ) ;
outt2 = Trim ( varTranspiler ( varr2 , funcNames , allVarsChars , allVarsInts ) ) ;
outt3 = Trim ( varTranspiler ( varr3 , funcNames , allVarsChars , allVarsInts ) ) ;
out = outt1 + " = " + "StringTrimRight(" + outt2 + ", " + outt3 + ");";
cppCode += out + "\n";
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 8) == StrLower ("Random, ")) 
{
varr1 = StrSplit ( A_LoopField18 , "," , 2 ) ;
varr2 = StrSplit ( A_LoopField18 , "," , 3 ) ;
varr3 = StrSplit ( A_LoopField18 , "," , 4 ) ;
varr1 = StrReplace ( varr1 , "%" , "" ) ;
varr2 = StrReplace ( varr2 , "%" , "" ) ;
varr3 = StrReplace ( varr3 , "%" , "" ) ;
varr1 = StrReplace ( varr1 , "  " , " " ) ;
outt2 = Trim ( varTranspiler ( varr2 , funcNames , allVarsChars , allVarsInts ) ) ;
outt3 = Trim ( varTranspiler ( varr3 , funcNames , allVarsChars , allVarsInts ) ) ;
out = varr1 + " = " + "Random(" + outt2 + ", " + outt3 + ");";
cppCode += out + "\n";
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 7) == StrLower ("Sleep, ")) 
{
varr1 = StrSplit ( A_LoopField18 , "," , 2 ) ;
varr1 = StrReplace ( varr1 , "%" , "" ) ;
varr1 = StrReplace ( varr1 , "  " , " " ) ;
out = "Sleep(" + varr1 + ");";
cppCode += out + "\n";
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 16) == StrLower ("StringTrimLeft, ")) 
{
varr1 = StrSplit ( A_LoopField18 , "," , 2 ) ;
varr2 = StrSplit ( A_LoopField18 , "," , 3 ) ;
varr3 = StrSplit ( A_LoopField18 , "," , 4 ) ;
outt1 = Trim ( varTranspiler ( varr1 , funcNames , allVarsChars , allVarsInts ) ) ;
outt2 = Trim ( varTranspiler ( varr2 , funcNames , allVarsChars , allVarsInts ) ) ;
outt3 = Trim ( varTranspiler ( varr3 , funcNames , allVarsChars , allVarsInts ) ) ;
out = outt1 + " = " + "StringTrimLeft(" + outt2 + ", " + outt3 + ");";
cppCode += out + "\n";
lineDone = 1;
}
else if (A_LoopField18 == "main:") 
{
theMainFuncDec = 1;
cppCode += "\nint main(int argc, char* argv[])\n{\n";
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 5) == "func ") 
{
funcName123 = StringTrimLeft(A_LoopField18, 5);
removeNextCurlyBraceCpp = 1;
funcName123 = StrReplace ( funcName123 , "arr int" , "OneIndexedArray<int>" ) ;
funcName123 = StrReplace ( funcName123 , "arr str" , "OneIndexedArray<std::string>" ) ;
funcName123 = StrReplace ( funcName123 , "arr float" , "OneIndexedArray<float>" ) ;
funcName123 = StrReplace ( funcName123 , " str " , " std::string " ) ;
funcName123 = StrReplace ( funcName123 , "str " , "std::string " ) ;
funcName123 = StrReplace ( funcName123 , "(str " , "(std::string " ) ;
cppCode += funcName123 + "\n{\n";
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 4) == "str ") 
{
strVar = StringTrimLeft(A_LoopField18, 4);
strVar = Trim ( strVar ) ;
declareAvarNOvalue = 0;
if (InStr (strVar , " := ")) 
{
varAssignmentType = "=";
}
else if (InStr (strVar , " += ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " .= ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " -= ")) 
{
varAssignmentType = "-=";
}
else if (InStr (strVar , " *= ")) 
{
varAssignmentType = "*=";
}
else if (InStr (strVar , " /= ")) 
{
varAssignmentType = "/=";
}
else
{
declareAvarNOvalue = 1;
}
if (declareAvarNOvalue == 1) 
{
nameOfVar1 = Trim ( StrSplit ( strVar , " " , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , " " , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
cppCode += "std::string " + nameOfVar1 + Chr ( 59 ) + "\n";
}
else
{
nameOfVar1 = Trim ( StrSplit ( strVar , " " , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , " " , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
cppCode += "std::string " + nameOfVar1 + " " + varAssignmentType + " " + nameOfVar2 + Chr ( 59 ) + "\n";
}
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 8) == "arr str ") 
{
strVar = StringTrimLeft(A_LoopField18, 8);
strVar = Trim ( strVar ) ;
haveWeEverUsedArrays = 1;
declareAvarNOvalue = 0;
if (InStr (strVar , " := ")) 
{
varAssignmentType = "=";
}
else if (InStr (strVar , " += ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " .= ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " -= ")) 
{
varAssignmentType = "-=";
}
else if (InStr (strVar , " *= ")) 
{
varAssignmentType = "*=";
}
else if (InStr (strVar , " /= ")) 
{
varAssignmentType = "/=";
}
else
{
declareAvarNOvalue = 1;
}
// defalut type
arrType = "std::string";
if (declareAvarNOvalue == 1) 
{
nameOfVar1 = Trim ( StrSplit ( strVar , " " , 1 ) ) ;
cppCode += "OneIndexedArray<" + arrType + "> " + nameOfVar1 + Chr ( 59 ) + "\n";
}
else
{
nameOfVar1 = Trim ( StrSplit ( strVar , " " , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , " " , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar222223 = nameOfVar2;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
if (varAssignmentType == "+=") 
{
cppCode += nameOfVar1 + ".add(" + nameOfVar222223 + ")" + Chr ( 59 ) + "\n";
}
else
{
cppCode += "OneIndexedArray<" + arrType + "> " + nameOfVar1 + " " + varAssignmentType + " " + nameOfVar2 + Chr ( 59 ) + "\n";
}
}
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 8) == "arr int ") 
{
strVar = StringTrimLeft(A_LoopField18, 8);
strVar = Trim ( strVar ) ;
haveWeEverUsedArrays = 1;
declareAvarNOvalue = 0;
if (InStr (strVar , " := ")) 
{
varAssignmentType = "=";
}
else if (InStr (strVar , " += ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " .= ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " -= ")) 
{
varAssignmentType = "-=";
}
else if (InStr (strVar , " *= ")) 
{
varAssignmentType = "*=";
}
else if (InStr (strVar , " /= ")) 
{
varAssignmentType = "/=";
}
else
{
declareAvarNOvalue = 1;
}
// defalut type
arrType = "int";
if (declareAvarNOvalue == 1) 
{
nameOfVar1 = Trim ( StrSplit ( strVar , " " , 1 ) ) ;
cppCode += "OneIndexedArray<" + arrType + "> " + nameOfVar1 + Chr ( 59 ) + "\n";
}
else
{
nameOfVar1 = Trim ( StrSplit ( strVar , " " , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , " " , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar222223 = nameOfVar2;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
if (varAssignmentType == "+=") 
{
cppCode += nameOfVar1 + ".add(" + nameOfVar222223 + ")" + Chr ( 59 ) + "\n";
}
else
{
cppCode += "OneIndexedArray<" + arrType + "> " + nameOfVar1 + " " + varAssignmentType + " " + nameOfVar2 + Chr ( 59 ) + "\n";
}
}
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 10) == "arr float ") 
{
strVar = StringTrimLeft(A_LoopField18, 10);
strVar = Trim ( strVar ) ;
haveWeEverUsedArrays = 1;
declareAvarNOvalue = 0;
if (InStr (strVar , " := ")) 
{
varAssignmentType = "=";
}
else if (InStr (strVar , " += ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " .= ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " -= ")) 
{
varAssignmentType = "-=";
}
else if (InStr (strVar , " *= ")) 
{
varAssignmentType = "*=";
}
else if (InStr (strVar , " /= ")) 
{
varAssignmentType = "/=";
}
else
{
declareAvarNOvalue = 1;
}
// defalut type
arrType = "float";
if (declareAvarNOvalue == 1) 
{
nameOfVar1 = Trim ( StrSplit ( strVar , " " , 1 ) ) ;
cppCode += "OneIndexedArray<" + arrType + "> " + nameOfVar1 + Chr ( 59 ) + "\n";
}
else
{
nameOfVar1 = Trim ( StrSplit ( strVar , " " , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , " " , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar222223 = nameOfVar2;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
if (varAssignmentType == "+=") 
{
cppCode += nameOfVar1 + ".add(" + nameOfVar222223 + ")" + Chr ( 59 ) + "\n";
}
else
{
cppCode += "OneIndexedArray<" + arrType + "> " + nameOfVar1 + " " + varAssignmentType + " " + nameOfVar2 + Chr ( 59 ) + "\n";
}
}
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 4) == "arr ") 
{
strVar = StringTrimLeft(A_LoopField18, 4);
strVar = Trim ( strVar ) ;
haveWeEverUsedArrays = 1;
declareAvarNOvalue = 0;
if (InStr (strVar , " := ")) 
{
varAssignmentType = "=";
}
else if (InStr (strVar , " += ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " .= ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " -= ")) 
{
varAssignmentType = "-=";
}
else if (InStr (strVar , " *= ")) 
{
varAssignmentType = "*=";
}
else if (InStr (strVar , " /= ")) 
{
varAssignmentType = "/=";
}
else
{
declareAvarNOvalue = 1;
}
// defalut type
arrType = "std::string";
if (declareAvarNOvalue == 1) 
{
nameOfVar1 = Trim ( StrSplit ( strVar , " " , 1 ) ) ;
cppCode += "OneIndexedArray<" + arrType + "> " + nameOfVar1 + Chr ( 59 ) + "\n";
}
else
{
nameOfVar1 = Trim ( StrSplit ( strVar , " " , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , " " , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar222223 = nameOfVar2;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
if (varAssignmentType == "+=") 
{
cppCode += nameOfVar1 + ".add(" + nameOfVar222223 + ")" + Chr ( 59 ) + "\n";
}
else
{
cppCode += "OneIndexedArray<" + arrType + "> " + nameOfVar1 + " " + varAssignmentType + " " + nameOfVar2 + Chr ( 59 ) + "\n";
}
}
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 1) == "[") 
{
strVar = StringTrimLeft(A_LoopField18, 1);
strVar = Trim ( strVar ) ;
declareAvarNOvalue = 0;
if (InStr (strVar , " := ")) 
{
varAssignmentType = "=";
}
else if (InStr (strVar , " += ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " .= ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " -= ")) 
{
varAssignmentType = "-=";
}
else if (InStr (strVar , " *= ")) 
{
varAssignmentType = "*=";
}
else if (InStr (strVar , " /= ")) 
{
varAssignmentType = "/=";
}
else
{
declareAvarNOvalue = 1;
}
if (declareAvarNOvalue == 1) 
{
nameOfVar1 = Trim ( StrSplit ( strVar , " " , 1 ) ) ;
nameOfVar1 = StringTrimRight(nameOfVar1, 1);
nameOfVarSplit = StrSplit ( strVar , " " , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
cppCode += "variables[" + Chr ( 34 ) + nameOfVar1 + Chr ( 34 ) + "]" + Chr ( 59 ) + "\n";
}
else
{
nameOfVar1 = Trim ( StrSplit ( strVar , " " , 1 ) ) ;
nameOfVar1 = StringTrimRight(nameOfVar1, 1);
nameOfVarSplit = StrSplit ( strVar , " " , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
cppCode += "variables[" + Chr ( 34 ) + nameOfVar1 + Chr ( 34 ) + "] " + varAssignmentType + " " + nameOfVar2 + Chr ( 59 ) + "\n";
}
lineDone = 1;
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 5) == "char ") 
{
varName123Temp = StringTrimLeft(A_LoopField18, 5);
varName = StrSplit ( varName123Temp , " " , 1 ) ;
lineDone = 1;
strVar = StringTrimLeft(A_LoopField18, 5);
strVar = Trim ( strVar ) ;
declareAvarNOvalue = 0;
if (InStr (strVar , " := ")) 
{
varAssignmentType = "=";
}
else if (InStr (strVar , " += ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " .= ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " -= ")) 
{
varAssignmentType = "-=";
}
else if (InStr (strVar , " *= ")) 
{
varAssignmentType = "*=";
}
else if (InStr (strVar , " /= ")) 
{
varAssignmentType = "/=";
}
else
{
declareAvarNOvalue = 1;
}
if (declareAvarNOvalue == 1) 
{
charVar1 = Trim ( StrSplit ( strVar , ":=" , 1 ) ) ;
didItFoundTheChar = 0;
cppCode += "const char* " + charVar1 + Chr ( 59 ) + "\n";
}
else
{
charVar1 = Trim ( StrSplit ( strVar , ":=" , 1 ) ) ;
charVar2 = Trim ( StrSplit ( strVar , ":=" , 2 ) ) ;
didItFoundTheChar = 0;
cppCode += "const char* " + charVar1 + " " + varAssignmentType + " " + charVar2 + Chr ( 59 ) + "\n";
}
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 4) == "int " || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 5) == "int8 " || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 6) == "int16 " || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 6) == "int32 " || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 6) == "int64 ") 
{
lineDone = 1;
if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 5) == "int8 ") 
{
varName123Temp = StringTrimLeft(A_LoopField18, 5);
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 4) == "int ") 
{
varName123Temp = StringTrimLeft(A_LoopField18, 4);
}
else
{
varName123Temp = StringTrimLeft(A_LoopField18, 6);
}
intType = Trim ( StrSplit ( A_LoopField18 , " " , 1 ) ) + "_t";
varName = StrSplit ( varName123Temp , " " , 1 ) ;
allVarsInts += varName + "\n";
if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 5) == "int8 ") 
{
strVar = StringTrimLeft(A_LoopField18, 5);
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 4) == "int ") 
{
strVar = StringTrimLeft(A_LoopField18, 4);
}
else
{
strVar = StringTrimLeft(A_LoopField18, 6);
}
strVar = Trim ( strVar ) ;
declareAvarNOvalue = 0;
if (InStr (strVar , " := ")) 
{
varAssignmentType = "=";
}
else if (InStr (strVar , " += ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " .= ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " -= ")) 
{
varAssignmentType = "-=";
}
else if (InStr (strVar , " *= ")) 
{
varAssignmentType = "*=";
}
else if (InStr (strVar , " /= ")) 
{
varAssignmentType = "/=";
}
else
{
declareAvarNOvalue = 1;
}
if (declareAvarNOvalue == 1) 
{
charVar1 = Trim ( StrSplit ( strVar , varAssignmentType , 1 ) ) ;
charVar2 = Trim ( StrSplit ( strVar , varAssignmentType , 2 ) ) ;
charVar1 = StrSplit ( charVar1 , " " , 1 ) ;
charVar2 = varTranspiler ( charVar2 , funcNames , allVarsChars , allVarsInts ) ;
//MsgBox, % intType
if (intType == "int_t") 
{
intType = "int";
}
if (intType == "int64_t") 
{
intType = "long long";
}
cppCode += intType + " " + charVar1 + Chr ( 59 ) + "\n";
}
else
{
charVar1 = Trim ( StrSplit ( strVar , varAssignmentType , 1 ) ) ;
charVar2 = Trim ( StrSplit ( strVar , varAssignmentType , 2 ) ) ;
charVar1 = StrSplit ( charVar1 , " " , 1 ) ;
charVar2 = varTranspiler ( charVar2 , funcNames , allVarsChars , allVarsInts ) ;
//MsgBox, % intType
if (intType == "int_t") 
{
intType = "int";
}
if (intType == "int64_t") 
{
intType = "long long";
}
cppCode += intType + " " + charVar1 + " " + varAssignmentType + " " + charVar2 + Chr ( 59 ) + "\n";
}
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 6) == "float ") 
{
lineDone = 1;
varName123Temp = StringTrimLeft(A_LoopField18, 6);
varName = StrSplit ( varName123Temp , " " , 1 ) ;
strVar = StringTrimLeft(A_LoopField18, 6);
strVar = Trim ( strVar ) ;
declareAvarNOvalue = 0;
if (InStr (strVar , " := ")) 
{
varAssignmentType = "=";
}
else if (InStr (strVar , " += ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " .= ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " -= ")) 
{
varAssignmentType = "-=";
}
else if (InStr (strVar , " *= ")) 
{
varAssignmentType = "*=";
}
else if (InStr (strVar , " /= ")) 
{
varAssignmentType = "/=";
}
else
{
declareAvarNOvalue = 1;
}
if (declareAvarNOvalue == 1) 
{
charVar1 = Trim ( StrSplit ( strVar , varAssignmentType , 1 ) ) ;
charVar2 = Trim ( StrSplit ( strVar , varAssignmentType , 2 ) ) ;
charVar1 = StrSplit ( charVar1 , " " , 1 ) ;
charVar2 = varTranspiler ( charVar2 , funcNames , allVarsChars , allVarsInts ) ;
//MsgBox, % intType
cppCode += "float" + " " + charVar1 + Chr ( 59 ) + "\n";
}
else
{
charVar1 = Trim ( StrSplit ( strVar , varAssignmentType , 1 ) ) ;
charVar2 = Trim ( StrSplit ( strVar , varAssignmentType , 2 ) ) ;
charVar1 = StrSplit ( charVar1 , " " , 1 ) ;
charVar2 = varTranspiler ( charVar2 , funcNames , allVarsChars , allVarsInts ) ;
//MsgBox, % intType
cppCode += "float" + " " + charVar1 + " " + varAssignmentType + " " + charVar2 + Chr ( 59 ) + "\n";
}
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 5) == "bool ") 
{
lineDone = 1;
varName123Temp = StringTrimLeft(A_LoopField18, 5);
varName = StrSplit ( varName123Temp , " " , 1 ) ;
strVar = StringTrimLeft(A_LoopField18, 5);
strVar = Trim ( strVar ) ;
declareAvarNOvalue = 0;
if (InStr (strVar , " := ")) 
{
varAssignmentType = "=";
}
else if (InStr (strVar , " += ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " .= ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " -= ")) 
{
varAssignmentType = "-=";
}
else if (InStr (strVar , " *= ")) 
{
varAssignmentType = "*=";
}
else if (InStr (strVar , " /= ")) 
{
varAssignmentType = "/=";
}
else
{
declareAvarNOvalue = 1;
}
if (declareAvarNOvalue == 1) 
{
charVar1 = Trim ( StrSplit ( strVar , varAssignmentType , 1 ) ) ;
charVar2 = Trim ( StrSplit ( strVar , varAssignmentType , 2 ) ) ;
charVar1 = StrSplit ( charVar1 , " " , 1 ) ;
charVar2 = varTranspiler ( charVar2 , funcNames , allVarsChars , allVarsInts ) ;
//MsgBox, % intType
cppCode += "bool" + " " + charVar1 + Chr ( 59 ) + "\n";
}
else
{
charVar1 = Trim ( StrSplit ( strVar , varAssignmentType , 1 ) ) ;
charVar2 = Trim ( StrSplit ( strVar , varAssignmentType , 2 ) ) ;
charVar1 = StrSplit ( charVar1 , " " , 1 ) ;
charVar2 = varTranspiler ( charVar2 , funcNames , allVarsChars , allVarsInts ) ;
//MsgBox, % intType
cppCode += "bool" + " " + charVar1 + " " + varAssignmentType + " " + charVar2 + Chr ( 59 ) + "\n";
}
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 4) == "cat ") 
{
lineDone = 1;
strVar = StringTrimLeft(A_LoopField18, 4);
strVar = Trim ( strVar ) ;
declareAvarNOvalue = 0;
if (InStr (strVar , " := ")) 
{
varAssignmentType = "=";
}
else if (InStr (strVar , " += ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " .= ")) 
{
varAssignmentType = "+=";
}
else if (InStr (strVar , " -= ")) 
{
varAssignmentType = "-=";
}
else if (InStr (strVar , " *= ")) 
{
varAssignmentType = "*=";
}
else if (InStr (strVar , " /= ")) 
{
varAssignmentType = "/=";
}
else
{
declareAvarNOvalue = 1;
}
if (declareAvarNOvalue == 1) 
{
nameOfVar1 = Trim ( StrSplit ( strVar , " " , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , " " , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
nameOfVar11 = Trim ( StrSplit ( nameOfVar1 , "%" , 1 ) ) ;
nameOfVar12 = Trim ( StrSplit ( nameOfVar1 , "%" , 2 ) ) ;
if (SubStr (nameOfVar12 , 1 , 1) == "[") 
{
nameOfVar12 = StringTrimRight(nameOfVar12, 1);
nameOfVar12 = StringTrimLeft(nameOfVar12, 1);
nameOfVar1 = "variables[" + Chr ( 34 ) + nameOfVar11 + Chr ( 34 ) + " + std::string(variables[" + Chr ( 34 ) + nameOfVar12 + Chr ( 34 ) + "])]";
}
else
{
nameOfVar1 = "variables[" + Chr ( 34 ) + nameOfVar11 + Chr ( 34 ) + " + STR(" + nameOfVar12 + ")]";
}
cppCode += nameOfVar1 + Chr ( 59 ) + "\n";
}
else
{
nameOfVar1 = Trim ( StrSplit ( strVar , " " , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , " " , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
nameOfVar11 = Trim ( StrSplit ( nameOfVar1 , "%" , 1 ) ) ;
nameOfVar12 = Trim ( StrSplit ( nameOfVar1 , "%" , 2 ) ) ;
if (SubStr (nameOfVar12 , 1 , 1) == "[") 
{
nameOfVar12 = StringTrimRight(nameOfVar12, 1);
nameOfVar12 = StringTrimLeft(nameOfVar12, 1);
nameOfVar1 = "variables[" + Chr ( 34 ) + nameOfVar11 + Chr ( 34 ) + " + std::string(variables[" + Chr ( 34 ) + nameOfVar12 + Chr ( 34 ) + "])]";
}
else
{
nameOfVar1 = "variables[" + Chr ( 34 ) + nameOfVar11 + Chr ( 34 ) + " + STR(" + nameOfVar12 + ")]";
}
cppCode += nameOfVar1 + " " + varAssignmentType + " " + nameOfVar2 + Chr ( 59 ) + "\n";
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
str123 = StrReplace ( str123 , "(" , " ( " ) ;
str123 = StrReplace ( str123 , ")" , " ) " ) ;
str123 = StrReplace ( str123 , "!" , " ! " ) ;
str123 = variables["CheckIFandElsesss" + STR(CheckIFandElsesssNumNum)] + Chr ( 32 ) + varTranspiler ( str123 , funcNames , allVarsChars , allVarsInts ) ;
str123 = StrReplace ( str123 , "( " , "(" ) ;
str123 = StrReplace ( str123 , " )" , ")" ) ;
str123 = StrReplace ( str123 , " ! " , "!" ) ;
str123 = StrReplace ( str123 , "" , "" ) ;
str123 = StrReplace ( str123 , "if " + Chr ( 40 ) + Chr ( 32 ) , "if " + Chr ( 40 ) ) ;
str123 = StrReplace ( str123 , "!==" , "!=" ) ;
out123 = str123;
cppCode += out123 + "\n";
}
else if (StrLower (A_LoopField18) == "loop") 
{
// infinity loops
haveWeEverUsedAloop = 1;
lineDone = 1;
var1 = "for (int A" + Chr ( 95 ) + "Index" + std::string(() AindexcharLength ) + " = 1;; A" + Chr ( 95 ) + "Index" + std::string(() AindexcharLength ) + "++)";
nothing = "";
AindexcharLengthStr = nothing + std::string(() AindexcharLength ) + nothing;
pycodeAcurlyBraceAddSomeVrasFixNL = 1;
pycodeLoopfixa += "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + std::string(() AindexcharLength ) + "\n";
pycodeLoopfixa1 = "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + std::string(() AindexcharLength ) ;
AindexcharLength++;
cppCode += pycodeLoopfixa1 + "\n" + var1 + "\n";
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 6) == "loop, " && SubStr (Trim (StrLower (A_LoopField18)) , 1 , 8)!= "loop, % " && SubStr (Trim (StrLower (A_LoopField18)) , 1 , 7)!= "loop % " && SubStr (Trim (StrLower (A_LoopField18)) , 1 , 11)!= StrLower ("Loop, Parse")) 
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
var1 = "for (int A" + Chr ( 95 ) + "Index" + std::string(() AindexcharLength ) + " = 1; A" + Chr ( 95 ) + "Index" + std::string(() AindexcharLength ) + "<= " + line + "; ++A" + Chr ( 95 ) + "Index" + std::string(() AindexcharLength ) + ")";
nothing = "";
AindexcharLengthStr = nothing + std::string(() AindexcharLength ) + nothing;
pycodeAcurlyBraceAddSomeVrasFixNL = 1;
pycodeLoopfixa += "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + std::string(() AindexcharLength ) + "\n";
pycodeLoopfixa1 = "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + std::string(() AindexcharLength ) ;
AindexcharLength++;
cppCode += pycodeLoopfixa1 + "\n" + var1 + "\n";
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 8) == "loop, % ") 
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
var1 = "for (int A" + Chr ( 95 ) + "Index" + std::string(() AindexcharLength ) + " = 1; A" + Chr ( 95 ) + "Index" + std::string(() AindexcharLength ) + "<= " + line + "; ++A" + Chr ( 95 ) + "Index" + std::string(() AindexcharLength ) + ")";
nothing = "";
AindexcharLengthStr = nothing + std::string(() AindexcharLength ) + nothing;
pycodeAcurlyBraceAddSomeVrasFixNL = 1;
haveWeEverUsedAloop = 1;
pycodeLoopfixa += "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + std::string(() AindexcharLength ) + "\n";
pycodeLoopfixa1 = "nl|itsaersdtgtgfergsdgfsegdfsedAA|" + std::string(() AindexcharLength ) ;
AindexcharLength++;
cppCode += pycodeLoopfixa1 + "\n" + var1 + "\n";
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 1 , 13) == StrLower ("Loop, Parse, ")) 
{
//std::vector<std::string> items = LoopParseFunc(variables["var1"], " ");
lineDone = 1;
var1 = A_LoopField18;
var1 = Trim ( var1 ) ;
var1 = StringTrimLeft(var1, 13);
line1 = Trim ( StrSplit ( var1 , "," , 1 ) ) ;
line1 = varTranspiler ( line1 , funcNames , allVarsChars , allVarsInts ) ;
line2 = "";
line3 = "";
itemsOut = "";
line2 = Trim ( StrSplit ( var1 , "," , 2 ) ) ;
line3 = Trim ( StrSplit ( var1 , "," , 3 ) ) ;
if (InStr (var1 , Chr (96) + ",")) 
{
line2 = Chr ( 34 ) + "," + Chr ( 34 ) ;
itemsOut = "std::vector<std::string> items" + std::string(() AindexcharLength ) + " = LoopParseFunc(" + line1 + ", " + line2 + ");";
}
else
{
if (line2 == "" && line3 == "") 
{
// nothing so only each char
itemsOut = "std::vector<std::string> items" + std::string(() AindexcharLength ) + " = LoopParseFunc(" + line1 + ");";
}
if (line2!= "" && line3 == "") 
{
if (InStr (line2 , Chr (96))) 
{
line2 = Chr ( 34 ) + line2 + Chr ( 34 ) ;
}
itemsOut = "std::vector<std::string> items" + std::string(() AindexcharLength ) + " = LoopParseFunc(" + line1 + ", " + line2 + ");";
}
if (line2!= "" && line3!= "") 
{
if (InStr (line2 , Chr (96))) 
{
line2 = Chr ( 34 ) + line2 + Chr ( 34 ) ;
}
if (InStr (line3 , Chr (96))) 
{
line3 = Chr ( 34 ) + line3 + Chr ( 34 ) ;
}
itemsOut = "std::vector<std::string> items" + std::string(() AindexcharLength ) + " = LoopParseFunc(" + line1 + ", " + line2 + ", " + line3 + ");";
}
itemsOut = StrReplace ( itemsOut , Chr ( 96 ) , Chr ( 92 ) ) ;
}
//for (size_t A_Index1 = 0; A_Index1 < items.size(); A_Index1++)
var1out = itemsOut + "\n" + "for (size_t A" + Chr ( 95 ) + "Index" + std::string(() AindexcharLength ) + " = 1; A" + Chr ( 95 ) + "Index" + std::string(() AindexcharLength ) + " < items" + std::string(() AindexcharLength ) + ".size() + 1; A" + Chr ( 95 ) + "Index" + std::string(() AindexcharLength ) + "++)";
nothing = "";
AindexcharLengthStr = nothing + std::string(() AindexcharLength ) + nothing;
theFixTextLoopLP = "std::string A" + Chr ( 95 ) + "LoopField" + std::string(() AindexcharLength ) + " = items" + std::string(() AindexcharLength ) + "[A" + Chr ( 95 ) + "Index" + std::string(() AindexcharLength ) + " - 1];";
pycodeAcurlyBraceAddSomeVrasFixLP = 1;
haveWeEverUsedAloop = 1;
pycodeLoopfixa += "lp|itsaersdtgtgfergsdgfsegdfsedAA|" + std::string(() AindexcharLength ) + "\n";
pycodeLoopfixa1 = "lp|itsaersdtgtgfergsdgfsegdfsedAA|" + std::string(() AindexcharLength ) ;
AindexcharLength++;
cppCode += pycodeLoopfixa1 + "\n" + var1out + "\n";
lineDone = 1;
}
else if (StrLower (A_LoopField18) == "break") 
{
cppCode += A_LoopField18 + ";\n";
lineDone = 1;
}
else if (StrLower (A_LoopField18) == "continue") 
{
cppCode += A_LoopField18 + ";\n";
lineDone = 1;
}
else if (StrLower (A_LoopField18) == "return" || SubStr (Trim (StrLower (A_LoopField18)) , 1 , 7) == "return ") 
{
if (StrLower (A_LoopField18) == "return") 
{
cppCode += A_LoopField18 + ";\n";
lineDone = 1;
}
else
{
varTranspiledReturn = StringTrimLeft(A_LoopField18, 7);
varTranspiledReturn = varTranspiler ( varTranspiledReturn , funcNames , allVarsChars , allVarsInts ) ;
cppCode += "return " + varTranspiledReturn + ";\n";
lineDone = 1;
}
}
else if (InStr (A_LoopField18 , " := ") || InStr (A_LoopField18 , " .= ") || InStr (A_LoopField18 , " += ") || InStr (A_LoopField18 , " -= ") || InStr (A_LoopField18 , " *= ") || InStr (A_LoopField18 , " /= ") && lineDone == 0) 
{
lineDone = 1;
strVar = A_LoopField18;
strVar = Trim ( strVar ) ;
if (InStr (strVar , " := ")) 
{
varAssignmentType = "=";
}
if (InStr (strVar , " += ")) 
{
varAssignmentType = "+=";
}
if (InStr (strVar , " .= ")) 
{
varAssignmentType = "+=";
}
if (InStr (strVar , " -= ")) 
{
varAssignmentType = "-=";
}
if (InStr (strVar , " *= ")) 
{
varAssignmentType = "*=";
}
if (InStr (strVar , " /= ")) 
{
varAssignmentType = "/=";
}
nameOfVar1 = Trim ( StrSplit ( strVar , " " , 1 ) ) ;
nameOfVarSplit = StrSplit ( strVar , " " , 2 ) ;
nameOfVar2 = Trim ( StrSplit ( strVar , std::string(() nameOfVarSplit ) , 2 ) ) ;
nameOfVar2 = varTranspiler ( nameOfVar2 , funcNames , allVarsChars , allVarsInts ) ;
cppCode += nameOfVar1 + " " + varAssignmentType + " " + nameOfVar2 + Chr ( 59 ) + "\n";
}
else if (SubStr (Trim (StrLower (A_LoopField18)) , 0) == Chr (41) && lineDone == 0) 
{
str123 = A_LoopField18;
FuncNameWhatIsIt = StrSplit ( str123 , "(" , 1 ) ;
std::vector<std::string> items19 = LoopParseFunc(FuncNameWhatIsIt);
for (size_t A_Index19 = 1; A_Index19 < items19.size() + 1; A_Index19++)
{
std::string A_LoopField19 = items19[A_Index19 - 1];
str123 = StringTrimLeft(str123, 1);
}
outVarTransiled = varTranspiler ( str123 , funcNames , allVarsChars , allVarsInts ) ;
out = FuncNameWhatIsIt + outVarTransiled;
lineDone = 1;
cppCode += out + ";\n";
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
cppCode += Chr ( 125 ) + "\n";
}
else
{
if (pycodeAcurlyBraceAddSomeVrasFixLP == 1 && SubStr (Trim (StrLower (A_LoopField18)) , 1 , 1) == Chr (123)) 
{
pycodeAcurlyBraceAddSomeVrasFixLP = 0;
cppCode += A_LoopField18 + "\n" + theFixTextLoopLP + "\n";
}
else
{
if (pycodeAcurlyBraceAddSomeVrasFixNL == 1 && SubStr (Trim (StrLower (A_LoopField18)) , 1 , 1) == Chr (123)) 
{
pycodeAcurlyBraceAddSomeVrasFixNL = 0;
cppCode += A_LoopField18 + "\n" + "\n";
}
else
{
cppCode += A_LoopField18 + "\n";
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
if (Trim (A_LoopField18) == "{" && removeNextCurlyBraceCpp == 1) 
{
removeNextCurlyBraceCpp = 0;
}
else
{
cppCode += A_LoopField18 + "\n";
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
std::vector<std::string> items20 = LoopParseFunc(pycodeLoopfixa, "\n", "\r");
for (size_t A_Index20 = 1; A_Index20 < items20.size() + 1; A_Index20++)
{
std::string A_LoopField20 = items20[A_Index20 - 1];
str123 = A_LoopField20;
fixLoopLokingFor = A_LoopField20;
fixLoopLokingForfound = 1;
out1 = StrSplit ( str123 , "|" , 1 ) ;
out2 = StrSplit ( str123 , "|" , 3 ) ;
//OutputDebug, |%out1%|
//OutputDebug, |%out2%|
wasAtanyIfsElseAddAIndexLoopCurlyFix = 0;
if (out1 == "nl") 
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
out4758686d86d86d86578991a%AIndexLoopCurlyFix% = "";
std::vector<std::string> items21 = LoopParseFunc(cppCode, "\n", "\r");
for (size_t A_Index21 = 1; A_Index21 < items21.size() + 1; A_Index21++)
{
std::string A_LoopField21 = items21[A_Index21 - 1];
//MsgBox, dsfgsdefgesrdg1
//MsgBox, |%A_LoopField21%|`n|%fixLoopLokingFor%|
if (InStr (A_LoopField21 , fixLoopLokingFor) && insdeAnestedLoopBAD!= 1) 
{
fixLoopLokingForNum = 1;
//MsgBox, do we came here 1
}
if (InStr (A_LoopField21 , "for ") && weAreDoneHereCurly!= 1 && insdeAnestedLoopBAD!= 1 && fixLoopLokingForNum == 1) 
{
s = StrSplit ( A_LoopField21 , "A" + Chr ( 95 ) + "Index" , 2 ) ;
out1z = s;
s = StrSplit ( out1z , " " , 1 ) ;
out1z = Trim ( s ) ;
//MsgBox, % out1z
//MsgBox, do we came here 2
fixLoopLokingForNum = 0;
foundTheTopLoop++;
inTarget = 1;
//MsgBox, % A_LoopField21
dontSaveStr = 1;
ALoopField = A_LoopField21;
//ALoopField := StrReplace(ALoopField, "for (/* Loop parse */", "for (/* Loop parse */ /* From AHK */")
DeleayOneCuzOfLoopParse = 1;
out4758686d86d86d86578991a%AIndexLoopCurlyFix% += ALoopField + "\n";
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
if (InStr (A_LoopField21 , "for ") && insdeAnestedLoopBAD!= 1 && foundTheTopLoop >= 2) 
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
//out4758686d86d86d86578991a%AIndexLoopCurlyFix% .= A_LoopField21 . "\n"
}
out4758686d86d86d86578991a%AIndexLoopCurlyFix% += A_LoopField21 + "\n";
}
if (inTarget == 1 && dontSaveStr!= 1 && fixLoopLokingForNum!= 1 && insdeAnestedLoopBAD!= 1) 
{
ALoopField = A_LoopField21;
// Replace "A_Index" with or without a following digit with "A_Index" + out1z
ALoopField = RegExReplace ( ALoopField , "A" + Chr ( 95 ) + "Index(?:\\d+)?" , "A" + Chr ( 95 ) + "Index" + out1z ) ;
//ALoopField := StrReplace(ALoopField, "A_LoopField", "A_LoopField" . AIndexLoopCurlyFix)
out4758686d86d86d86578991a%AIndexLoopCurlyFix% += ALoopField + "\n";
}
if (inTarget == 1 && InStr (A_LoopField21 , Chr (125)) && readyToEnd == 1 && netsedCurly == 0 && weAreDoneHereCurly == 0 && dontSaveStr!= 1 && insdeAnestedLoopBAD!= 1) 
{
//MsgBox, % A_LoopField21
weAreDoneHereCurly = 1;
inTarget = 0;
endBracketDOntPutThere = 1;
//out4758686d86d86d86578991a%AIndexLoopCurlyFix% .= A_LoopField21 . "\n"
}
dontSaveStr = 0;
if (inTarget!= 1 && endBracketDOntPutThere!= 1 && insdeAnestedLoopBAD!= 1) 
{
out4758686d86d86d86578991a%AIndexLoopCurlyFix% += A_LoopField21 + "\n";
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
out4758686d86d86d86578991a%AIndexLoopCurlyFix% = "";
std::vector<std::string> items22 = LoopParseFunc(cppCode, "\n", "\r");
for (size_t A_Index22 = 1; A_Index22 < items22.size() + 1; A_Index22++)
{
std::string A_LoopField22 = items22[A_Index22 - 1];
if (InStr (A_LoopField22 , fixLoopLokingFor) && insdeAnestedLoopBAD!= 1) 
{
fixLoopLokingForNum = 1;
//MsgBox, do we came here 3
}
if (InStr (A_LoopField22 , "for ") && weAreDoneHereCurly!= 1 && insdeAnestedLoopBAD!= 1 && fixLoopLokingForNum == 1) 
{
s = StrSplit ( A_LoopField22 , "A" + Chr ( 95 ) + "Index" , 2 ) ;
out1z = s;
s = StrSplit ( out1z , " " , 1 ) ;
out1z = Trim ( s ) ;
//MsgBox, % out1z
fixLoopLokingForNum = 0;
//MsgBox, do we came here 4
foundTheTopLoop++;
inTarget = 1;
//MsgBox, % A_LoopField22
dontSaveStr = 1;
ALoopField = A_LoopField22;
//ALoopField := StrReplace(ALoopField, "for (/* Loop parse */", "for (/* Loop parse */ /* From AHK */")
DeleayOneCuzOfLoopParse = 1;
out4758686d86d86d86578991a%AIndexLoopCurlyFix% += ALoopField + "\n";
}
if (inTarget == 1 && InStr (A_LoopField22 , Chr (123)) && insdeAnestedLoopBAD!= 1) 
{
insideBracket = 1;
}
if (insideBracket == 1 && InStr (A_LoopField22 , Chr (123)) && insdeAnestedLoopBAD!= 1) 
{
netsedCurly++;
}
if (insideBracket == 1 && InStr (A_LoopField22 , Chr (125)) && insdeAnestedLoopBAD!= 1) 
{
netsedCurly--;
readyToEnd = 1;
}
if (InStr (A_LoopField22 , "for ") && insdeAnestedLoopBAD!= 1 && foundTheTopLoop >= 2) 
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
if (InStr (A_LoopField22 , Chr (123))) 
{
insideBracket1 = 1;
}
if (insideBracket1 == 1 && InStr (A_LoopField22 , Chr (123))) 
{
netsedCurly1++;
}
if (insideBracket1 == 1 && InStr (A_LoopField22 , Chr (125))) 
{
netsedCurly1--;
readyToEnd1 = 1;
}
if (InStr (A_LoopField22 , Chr (125)) && readyToEnd1 == 1 && netsedCurly1 == 0 && insideBracket == 1) 
{
//MsgBox, % A_LoopField22
eldLoopNestedBADlol = 1;
//out4758686d86d86d86578991a%AIndexLoopCurlyFix% .= A_LoopField22 . "\n"
}
out4758686d86d86d86578991a%AIndexLoopCurlyFix% += A_LoopField22 + "\n";
}
if (inTarget == 1 && dontSaveStr!= 1 && fixLoopLokingForNum!= 1 && insdeAnestedLoopBAD!= 1) 
{
ALoopField = A_LoopField22;
// Replace "A_Index" with or without a following digit with "A_Index" + out1z
ALoopField = RegExReplace ( ALoopField , "A" + Chr ( 95 ) + "Index(?:\\d+)?" , "A" + Chr ( 95 ) + "Index" + out1z ) ;
// Replace "A_Index" with or without a following digit with "A_Index" + out1z
ALoopField = RegExReplace ( ALoopField , "A" + Chr ( 95 ) + "LoopField(?:\\d+)?" , "A" + Chr ( 95 ) + "LoopField" + out1z ) ;
out4758686d86d86d86578991a%AIndexLoopCurlyFix% += ALoopField + "\n";
}
if (inTarget == 1 && InStr (A_LoopField22 , Chr (125)) && readyToEnd == 1 && netsedCurly == 0 && weAreDoneHereCurly == 0 && dontSaveStr!= 1 && insdeAnestedLoopBAD!= 1) 
{
//MsgBox, % A_LoopField22
weAreDoneHereCurly = 1;
inTarget = 0;
endBracketDOntPutThere = 1;
//out4758686d86d86d86578991a%AIndexLoopCurlyFix% .= A_LoopField22 . "\n"
}
dontSaveStr = 0;
if (inTarget!= 1 && endBracketDOntPutThere!= 1 && insdeAnestedLoopBAD!= 1) 
{
out4758686d86d86d86578991a%AIndexLoopCurlyFix% += A_LoopField22 + "\n";
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
out4758686d86dgt8r754444444 = "";
hold = 0;
std::vector<std::string> items23 = LoopParseFunc(cppCode, "\n", "\r");
for (size_t A_Index23 = 1; A_Index23 < items23.size() + 1; A_Index23++)
{
std::string A_LoopField23 = items23[A_Index23 - 1];
ignore = 0;
if (InStr (A_LoopField23 , "for ")) 
{
if (hold == 1 && holdText == A_LoopField23) 
{
ignore = 1;
}
else
{
holdText = A_LoopField23;
hold = 1;
}
}
if (!(ignore)) 
{
out4758686d86dgt8r754444444 += A_LoopField23 + "\n";
}
}
out4758686d86dgt8r754444444 = StringTrimRight(out4758686d86dgt8r754444444, 1);
cppCode = out4758686d86dgt8r754444444;
}
pyCodeOut1234565432 = "";
std::vector<std::string> items24 = LoopParseFunc(cppCode, "\n", "\r");
for (size_t A_Index24 = 1; A_Index24 < items24.size() + 1; A_Index24++)
{
std::string A_LoopField24 = items24[A_Index24 - 1];
out = A_LoopField24;
if (!(InStr (out , "|itsaersdtgtgfergsdgfsegdfsedAA|"))) 
{
pyCodeOut1234565432 += out + "\n";
}
}
cppCode = StringTrimRight(pyCodeOut1234565432, 1);
cppCodeOutOneLastFixFixFIX = "";
std::vector<std::string> items25 = LoopParseFunc(cppCode, " ");
for (size_t A_Index25 = 1; A_Index25 < items25.size() + 1; A_Index25++)
{
std::string A_LoopField25 = items25[A_Index25 - 1];
sstr1 = A_LoopField25;
sstr1 = StrReplace ( sstr1 , "A_TickCount" , "BuildInVars(" + Chr ( 34 ) + "A_TickCount" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "A_Now" , "BuildInVars(" + Chr ( 34 ) + "A_Now" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "A_YYYY" , "BuildInVars(" + Chr ( 34 ) + "A_YYYY" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "A_MMMM" , "BuildInVars(" + Chr ( 34 ) + "A_MMMM" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "A_MMM" , "BuildInVars(" + Chr ( 34 ) + "A_MMM" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "A_MM" , "BuildInVars(" + Chr ( 34 ) + "A_MM" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "A_DDDD" , "BuildInVars(" + Chr ( 34 ) + "A_DDDD" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "A_DDD" , "BuildInVars(" + Chr ( 34 ) + "A_DDD" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "A_DD" , "BuildInVars(" + Chr ( 34 ) + "A_DD" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "A_Hour" , "BuildInVars(" + Chr ( 34 ) + "A_Hour" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "A_Min" , "BuildInVars(" + Chr ( 34 ) + "A_Min" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "A_Sec" , "BuildInVars(" + Chr ( 34 ) + "A_Sec" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "A_Space" , "BuildInVars(" + Chr ( 34 ) + "A_Space" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "A_Tab" , "BuildInVars(" + Chr ( 34 ) + "A_Tab" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "BuildInVars(" + Chr ( 34 ) + "BuildInVars(" + Chr ( 34 ) + "A_DD" + Chr ( 34 ) + ")D" + Chr ( 34 ) + ")" , "BuildInVars(" + Chr ( 34 ) + "A_DDD" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "BuildInVars(" + Chr ( 34 ) + "BuildInVars(" + Chr ( 34 ) + "BuildInVars(" + Chr ( 34 ) + "A_DD" + Chr ( 34 ) + ")D" + Chr ( 34 ) + ")D" + Chr ( 34 ) + ")" , "BuildInVars(" + Chr ( 34 ) + "A_DDDD" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "BuildInVars(" + Chr ( 34 ) + "BuildInVars(" + Chr ( 34 ) + "A_DDD" + Chr ( 34 ) + ")D" + Chr ( 34 ) + ")" , "BuildInVars(" + Chr ( 34 ) + "A_DDDD" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "BuildInVars(" + Chr ( 34 ) + "BuildInVars(" + Chr ( 34 ) + "A_MM" + Chr ( 34 ) + ")M" + Chr ( 34 ) + ")" , "BuildInVars(" + Chr ( 34 ) + "A_MMM" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "BuildInVars(" + Chr ( 34 ) + "BuildInVars(" + Chr ( 34 ) + "BuildInVars(" + Chr ( 34 ) + "A_MM" + Chr ( 34 ) + ")M" + Chr ( 34 ) + ")M" + Chr ( 34 ) + ")" , "BuildInVars(" + Chr ( 34 ) + "A_MMMM" + Chr ( 34 ) + ")" ) ;
sstr1 = StrReplace ( sstr1 , "BuildInVars(" + Chr ( 34 ) + "BuildInVars(" + Chr ( 34 ) + "A_MMM" + Chr ( 34 ) + ")M" + Chr ( 34 ) + ")" , "BuildInVars(" + Chr ( 34 ) + "A_MMMM" + Chr ( 34 ) + ")" ) ;
cppCodeOutOneLastFixFixFIX += sstr1 + " ";
}
cppCode = StringTrimRight(cppCodeOutOneLastFixFixFIX, 1);
for (int A_Index26 = 1; A_Index26<= theIdNumOfThe34; ++A_Index26)
{
cppCode = StrReplace ( cppCode , "ihuiuuhuuhtheidFor--asas-theuhturtyphoutr-" + Chr ( 65 ) + Chr ( 65 ) + std::string(() A_Index26 ) + Chr ( 65 ) + Chr ( 65 ) , "" + variables["theIdNumOfThe34theVar" + STR(A_Index26)] + "" ) ;
}
cppCodeFixCharRemoveStd = "";
std::vector<std::string> items27 = LoopParseFunc(cppCode, "\n", "\r");
for (size_t A_Index27 = 1; A_Index27 < items27.size() + 1; A_Index27++)
{
std::string A_LoopField27 = items27[A_Index27 - 1];
if (SubStr (Trim (StrLower (A_LoopField27)) , 1 , 12) == "const char* ") 
{
cppCodeFixCharRemoveStd123 = A_LoopField27;
cppCodeFixCharRemoveStd123 = StrReplace ( cppCodeFixCharRemoveStd123 , "std::string(" , "" ) ;
cppCodeFixCharRemoveStd123 = StrReplace ( cppCodeFixCharRemoveStd123 , ")" , "" ) ;
cppCodeFixCharRemoveStd += cppCodeFixCharRemoveStd123 + "\n";
}
else
{
cppCodeFixCharRemoveStd += A_LoopField27 + "\n";
}
}
cppCode = StringTrimRight(cppCodeFixCharRemoveStd, 1);
if (theMainFuncDec == 0) 
{
upCode = "\nint main(int argc, char* argv[])\n{\n";
}
uperCode = "";
uperCodeLibs = "";
uperCodeLibs += "#include <iostream>\n#include <sstream>\n#include <string>\n#include <cstdint>\n";
if (InStr (cppCode , "variables[")) 
{
uperCodeLibs += "\n#include <unordered_map>\n#include <string>\n";
uperCode = uperCode + "\n// Define a map to store dynamic variables\n    std::unordered_map<std::string, std::string> variables;\n";
}
if (haveWeEverUsedArrays == 1) 
{
uperCodeLibs += "\n#include <vector>\n#include <string>\n#include <sstream>\n#include <stdexcept>\n";
uperCode = uperCode + "\n// Forward declare OneIndexedArray template\ntemplate <typename T>\nclass OneIndexedArray;\n\n#define OneIndexedArray_DEFINED\n\n// Helper function to set the internal array's size as a string\ntemplate <typename T>\nvoid setInternalArraySize(T& element, size_t size) {\n    element = static_cast<T>(size);\n}\n\n// Specialization for std::string\ntemplate <>\nvoid setInternalArraySize<std::string>(std::string& element, size_t size) {\n    element = std::to_string(size);\n}\n\n// One-indexed dynamic array class\ntemplate <typename T>\nclass OneIndexedArray {\nprivate:\n    std::vector<T> internalArray;\n\npublic:\n    OneIndexedArray() {\n        internalArray.push_back(T{}); // Placeholder for element count\n    }\n\n    void add(const T& newElement) {\n        internalArray.push_back(newElement);\n        setInternalArraySize(internalArray[0], internalArray.size() - 1);\n    }\n\n    void setArray(const std::vector<T>& newArray) {\n        internalArray.resize(newArray.size() + 1);\n        std::copy(newArray.begin(), newArray.end(), internalArray.begin() + 1);\n        setInternalArraySize(internalArray[0], newArray.size());\n    }\n\n    T& operator[](size_t index) {\n        if (index >= internalArray.size()) {\n            internalArray.resize(index + 1);\n            setInternalArraySize(internalArray[0], internalArray.size() - 1);\n        }\n        return internalArray[index];\n    }\n\n    const T& operator[](size_t index) const {\n        if (index >= internalArray.size()) {\n            throw std::out_of_range(" + Chr ( 34 ) + "Index out of range" + Chr ( 34 ) + ");\n        }\n        return internalArray[index];\n    }\n\n    size_t size() const {\n        return static_cast<size_t>(internalArray.size() - 1);\n    }\n    void pop_back() {\n        if (size() " + Chr ( 62 ) + " 0) {\n            internalArray.pop_back(); // Remove last element\n            setInternalArraySize(internalArray[0], internalArray.size() - 1); // Update size\n        }\n    }\n};\n\n// Function to split text into words based on a delimiter\nstd::vector<std::string> split(const std::string& text, const std::string& delimiter) {\n    std::vector<std::string> words;\n    std::istringstream stream(text);\n    std::string word;\n    while (std::getline(stream, word, delimiter[0])) { // assuming single character delimiter\n        words.push_back(word);\n    }\n    return words;\n}\n\n// Function to split text into a OneIndexedArray\nOneIndexedArray<std::string> arrSplit(const std::string& text, const std::string& delimiter) {\n    OneIndexedArray<std::string> array;\n    std::vector<std::string> words = split(text, delimiter);\n    array.setArray(words);\n    return array;\n}\n";
}
if (InStr (cppCode , "INT(") || InStr (cppCode , "INT (")) 
{
uperCodeLibs += "\n#include <string>\n#include <sstream>\n";
uperCode = uperCode + "\n// Convert std::string to int\nint INT(const std::string& str) {\n    std::istringstream iss(str);\n    int value;\n    iss >> value;\n    return value;\n}\n";
}
if (InStr (cppCode , "STR(") || InStr (cppCode , "STR (")) 
{
uperCodeLibs += "\n#include <string>\n#include <string>\n";
uperCode = uperCode + "\n// Convert various types to std::string\nstd::string STR(int value) {\n    return std::to_string(value);\n}\n\n// Convert various types to std::string\nstd::string STR(long long value) {\n    return std::to_string(value);\n}\n\nstd::string STR(float value) {\n    return std::to_string(value);\n}\n\nstd::string STR(double value) {\n    return std::to_string(value);\n}\n\nstd::string STR(size_t value) {\n    return std::to_string(value);\n}\n\nstd::string STR(bool value) {\n    return value ? " + Chr ( 34 ) + "1" + Chr ( 34 ) + " : " + Chr ( 34 ) + "0" + Chr ( 34 ) + ";\n}\n";
}
if (InStr (cppCode , "FLOAT(") || InStr (cppCode , "FLOAT (")) 
{
uperCodeLibs += "\n#include <string>\n#include <sstream>\n";
uperCode = uperCode + "\n// Convert std::string to float\nfloat FLOAT(const std::string& str) {\n    std::istringstream iss(str);\n    float value;\n    iss >> value;\n    return value;\n}\n";
}
if (InStr (cppCode , "InStr(") || InStr (cppCode , "InStr (")) 
{
uperCodeLibs += "\n#include <string>\n";
uperCode = uperCode + "\n// Function to find the position of needle in haystack (std::string overload)\nint InStr(const std::string& haystack, const std::string& needle) {\n    size_t pos = haystack.find(needle);\n    return (pos != std::string::npos) ? static_cast<int>(pos) + 1 : 0;\n}\n";
}
if (InStr (cppCode , "Random(") || InStr (cppCode , "Random (")) 
{
uperCodeLibs += "\n#include <cstdlib>\n#include <ctime>\n#include <random>\n";
uperCode = uperCode + "\nint Random(int min, int max) {\n    // Create a random device to seed the generator\n    std::random_device rd;\n    \n    // Create a generator seeded with the random device\n    std::mt19937 gen(rd());\n    \n    // Define a distribution within the specified range\n    std::uniform_int_distribution<> dis(min, max);\n    \n    // Generate and return a random number within the specified range\n    return dis(gen);\n}\n";
}
if (InStr (cppCode , "Sleep(") || InStr (cppCode , "Sleep (")) 
{
uperCodeLibs += "\n#include <thread>\n#include <chrono>\n";
uperCode = uperCode + "\n// Function to sleep for a specified number of milliseconds\nvoid Sleep(int milliseconds) {\n    std::this_thread::sleep_for(std::chrono::milliseconds(milliseconds));\n}\n\n";
}
if (InStr (cppCode , "input(") || InStr (cppCode , "input (")) 
{
uperCodeLibs += "\n#include <iostream>\n#include <string>\n";
uperCode = uperCode + "\n// Function to get input from the user, similar to Python's input() function\nstd::string input(const std::string& prompt) {\n    std::string userInput;\n    std::cout << prompt; // Display the prompt to the user\n    std::getline(std::cin, userInput); // Get the entire line of input\n    return userInput;\n}\n\n";
}
if (InStr (cppCode , "LoopParseFunc(") || InStr (cppCode , "LoopParseFunc (")) 
{
uperCodeLibs += "\n#include <vector>\n#include <string>\n#include <regex>\n";
uperCode = uperCode + "\n// Function to escape special characters for regex\nstd::string escapeRegex(const std::string& str) {\n    static const std::regex specialChars{R" + Chr ( 34 ) + "([-[" + Chr ( 92 ) + "]{}()*+?.," + Chr ( 92 ) + "^$|#" + Chr ( 92 ) + "s])" + Chr ( 34 ) + "};\n    return std::regex_replace(str, specialChars, R" + Chr ( 34 ) + "(" + Chr ( 92 ) + "$&)" + Chr ( 34 ) + ");\n}\n\n// Function to split a string based on delimiters\nstd::vector<std::string> LoopParseFunc(const std::string& var, const std::string& delimiter1 = " + Chr ( 34 ) + "" + Chr ( 34 ) + ", const std::string& delimiter2 = " + Chr ( 34 ) + "" + Chr ( 34 ) + ") {\n    std::vector<std::string> items;\n    if (delimiter1.empty() && delimiter2.empty()) {\n        // If no delimiters are provided, return a list of characters\n        for (char c : var) {\n            items.push_back(std::string(1, c));\n        }\n    } else {\n        // Escape delimiters for regex\n        std::string escapedDelimiters = escapeRegex(delimiter1 + delimiter2);\n        // Construct the regular expression pattern for splitting the string\n        std::string pattern = " + Chr ( 34 ) + "[" + Chr ( 34 ) + " + escapedDelimiters + " + Chr ( 34 ) + "]+" + Chr ( 34 ) + ";\n        std::regex regexPattern(pattern);\n        std::sregex_token_iterator iter(var.begin(), var.end(), regexPattern, -1);\n        std::sregex_token_iterator end;\n        while (iter != end) {\n            items.push_back(*iter++);\n        }\n    }\n    return items;\n}\n";
}
if (InStr (cppCode , "print(") || InStr (cppCode , "print (")) 
{
uperCodeLibs += "\n#include <iostream>\n#include <string>\n#include <type_traits>\n";
uperCode = uperCode + "\n// Print function that converts all types to string if needed\ntemplate <typename T>\nvoid print(const T& value) {\n    if constexpr (std::is_same_v<T, std::string>) {\n        std::cout << value << std::endl;\n    } else if constexpr (std::is_same_v<T, int>) {\n        std::cout << std::to_string(value) << std::endl;\n    } else if constexpr (std::is_same_v<T, float>) {\n        std::cout << std::to_string(value) << std::endl;\n    } else if constexpr (std::is_same_v<T, double>) {\n        std::cout << std::to_string(value) << std::endl;\n    } else if constexpr (std::is_same_v<T, size_t>) {\n        std::cout << std::to_string(value) << std::endl;\n    } else if constexpr (std::is_same_v<T, bool>) {\n        std::cout << (value ? " + Chr ( 34 ) + "1" + Chr ( 34 ) + " : " + Chr ( 34 ) + "0" + Chr ( 34 ) + ") << std::endl;\n    } \n    #ifdef OneIndexedArray_DEFINED\n    else if constexpr (std::is_base_of_v<OneIndexedArray<std::string>, T>) {\n        for (size_t i = 1; i <= value.size(); ++i) {\n            std::cout << value[i] << std::endl;\n        }\n    } else if constexpr (std::is_base_of_v<OneIndexedArray<int>, T>) {\n        for (size_t i = 1; i <= value.size(); ++i) {\n            std::cout << std::to_string(value[i]) << std::endl;\n        }\n    } else if constexpr (std::is_base_of_v<OneIndexedArray<float>, T>) {\n        for (size_t i = 1; i <= value.size(); ++i) {\n            std::cout << std::to_string(value[i]) << std::endl;\n        }\n    } else if constexpr (std::is_base_of_v<OneIndexedArray<double>, T>) {\n        for (size_t i = 1; i <= value.size(); ++i) {\n            std::cout << std::to_string(value[i]) << std::endl;\n        }\n    }\n    #endif\n    else {\n        std::cout << " + Chr ( 34 ) + "Unsupported type" + Chr ( 34 ) + " << std::endl;\n    }\n}\n";
}
if (InStr (cppCode , "FileRead(") || InStr (cppCode , "FileRead (")) 
{
uperCodeLibs += "\n#include <fstream>\n#include <string>\n#include <filesystem>\n#include <stdexcept>\n";
uperCode = uperCode + "\nstd::string FileRead(const std::string& path) {\n    std::ifstream file;\n    std::filesystem::path full_path;\n\n    // Check if the file path is an absolute path\n    if (std::filesystem::path(path).is_absolute()) {\n        full_path = path;\n    } else {\n        // If it's not a full path, prepend the current working directory\n        full_path = std::filesystem::current_path() / path;\n    }\n\n    // Open the file\n    file.open(full_path);\n    if (!file.is_open()) {\n        throw std::runtime_error(" + Chr ( 34 ) + "Error: Could not open the file." + Chr ( 34 ) + ");\n    }\n\n    // Read the file content into a string\n    std::string content;\n    std::string line;\n    while (std::getline(file, line)) {\n        content += line + '" + Chr ( 92 ) + "n';\n    }\n\n    file.close();\n    return content;\n}\n";
}
if (InStr (cppCode , "FileAppend(") || InStr (cppCode , "FileAppend (")) 
{
uperCodeLibs += "\n#include <fstream>\n#include <iostream>\n#include <string>\n";
uperCode = uperCode + "\nbool FileAppend(const std::string& content, const std::string& path) {\n    std::ofstream file;\n\n    // Open the file in append mode\n    file.open(path, std::ios::app);\n\n    if (!file.is_open()) {\n        std::cerr << " + Chr ( 34 ) + "Error: Could not open the file for appending." + Chr ( 34 ) + " << std::endl;\n        return false;\n    }\n\n    // Append the content to the file\n    file << content;\n\n    // Close the file\n    file.close();\n\n    return true;\n}\n\n";
}
if (InStr (cppCode , "FileDelete(") || InStr (cppCode , "FileDelete (")) 
{
uperCodeLibs += "\n#include <filesystem>\n#include <iostream>\n#include <string>\n";
uperCode = uperCode + "\nbool FileDelete(const std::string& path) {\n    std::filesystem::path file_path(path);\n\n    // Check if the file exists\n    if (!std::filesystem::exists(file_path)) {\n        return false;\n    }\n\n    // Attempt to remove the file\n    if (!std::filesystem::remove(file_path)) {\n        return false;\n    }\n\n    return true;\n}\n";
}
if (InStr (cppCode , "StrLen(") || InStr (cppCode , "StrLen (")) 
{
uperCodeLibs += "\n#include <string>\n";
uperCode = uperCode + "\nsize_t StrLen(const std::string& str) {\n    return str.length();\n}\n";
}
if (InStr (cppCode , "Asc(") || InStr (cppCode , "Asc (")) 
{
uperCodeLibs += "\n#include <string>\n";
uperCode = uperCode + "\nint Asc(const std::string& str) {\n    if (!str.empty()) {\n        return static_cast<int>(str[0]);\n    }\n    return -1; // Return -1 if the string is empty\n}\n";
}
if (InStr (cppCode , "Abs(") || InStr (cppCode , "Abs (")) 
{
uperCodeLibs += "\n#include <cmath>\n";
uperCode = uperCode + "\ndouble Abs(double value) {\n    return std::fabs(value);\n}\n\n";
}
if (InStr (cppCode , "ACos(") || InStr (cppCode , "ACos (")) 
{
uperCodeLibs += "\n#include <cmath>\n";
uperCode = uperCode + "\ndouble ACos(double value) {\n    return std::acos(value);\n}\n";
}
if (InStr (cppCode , "ASin(") || InStr (cppCode , "ASin (")) 
{
uperCodeLibs += "\n#include <cmath>\n";
uperCode = uperCode + "\n// Define your custom ASin function\ndouble ASin(double value) {\n    // Ensure the value is within the valid range for asin\n    if (value < -1.0 || value > 1.0) {\n        std::cerr << " + Chr ( 34 ) + "Error: Value out of range for arcsine function." + Chr ( 34 ) + " << std::endl;\n        return NAN;  // Return 'Not-a-Number' to indicate an error\n    }\n\n    return asin(value);  // Call the standard asin function\n}\n";
}
if (InStr (cppCode , "ATan(") || InStr (cppCode , "ATan (")) 
{
uperCodeLibs += "\n#include <cmath>\n";
uperCode = uperCode + "\ndouble ATan(double value) {\n    return std::atan(value);\n}\n";
}
if (InStr (cppCode , "Ceil(") || InStr (cppCode , "Ceil (")) 
{
uperCodeLibs += "\n#include <cmath>\n";
uperCode = uperCode + "\ndouble Ceil(double value) {\n    return std::ceil(value);\n}\n";
}
if (InStr (cppCode , "Cos(") || InStr (cppCode , "Cos (")) 
{
uperCodeLibs += "\n#include <cmath>\n";
uperCode = uperCode + "\ndouble Cos(double angle) {\n    return std::cos(angle);\n}\n";
}
if (InStr (cppCode , "Exp(") || InStr (cppCode , "Exp (")) 
{
uperCodeLibs += "\n#include <cmath>\n";
uperCode = uperCode + "\ndouble Exp(double value) {\n    return std::exp(value);\n}\n";
}
if (InStr (cppCode , "Ln(") || InStr (cppCode , "Ln (")) 
{
uperCodeLibs += "\n#include <cmath>\n";
uperCode = uperCode + "\ndouble Ln(double value) {\n    return std::log(value);\n}\n";
}
if (InStr (cppCode , "Log(") || InStr (cppCode , "Log (")) 
{
uperCodeLibs += "\n#include <cmath>\n";
uperCode = uperCode + "\n// Function that computes the logarithm with base 10\ndouble Log(double value) {\n    return std::log10(value);\n}\n";
}
if (InStr (cppCode , "Round(") || InStr (cppCode , "Round (")) 
{
uperCodeLibs += "\n#include <cmath>\n";
uperCode = uperCode + "\ndouble Round(double value) {\n    return std::round(value);\n}\n";
}
if (InStr (cppCode , "Sin(") || InStr (cppCode , "Sin (")) 
{
uperCodeLibs += "\n#include <cmath>\n";
uperCode = uperCode + "\ndouble Sin(double angle) {\n    return std::sin(angle);\n}\n";
}
if (InStr (cppCode , "Sqrt(") || InStr (cppCode , "Sqrt (")) 
{
uperCodeLibs += "\n#include <cmath>\n";
uperCode = uperCode + "\ndouble Sqrt(double value) {\n    return std::sqrt(value);\n}\n";
}
if (InStr (cppCode , "Tan(") || InStr (cppCode , "Tan (")) 
{
uperCodeLibs += "\n#include <cmath>\n";
uperCode = uperCode + "\ndouble Tan(double angle) {\n    return std::tan(angle);\n}\n";
}
if (InStr (cppCode , "SubStr(") || InStr (cppCode , "SubStr (")) 
{
uperCodeLibs += "\n#include <string>\n";
uperCode = uperCode + "\nstd::string SubStr(const std::string& str, int startPos, int length = -1) {\n    std::string result;\n    size_t strLen = str.size();\n\n    // Handle negative starting positions\n    if (startPos < 0) {\n        startPos += strLen;\n        if (startPos < 0) startPos = 0;\n    } else {\n        if (startPos > static_cast<int>(strLen)) return " + Chr ( 34 ) + "" + Chr ( 34 ) + "; // Starting position beyond string length\n        startPos -= 1; // Convert to 0-based index\n    }\n\n    // Handle length\n    if (length < 0) {\n        length = strLen - startPos; // Length to end of string\n    } else if (startPos + length > static_cast<int>(strLen)) {\n        length = strLen - startPos; // Adjust length to fit within the string\n    }\n\n    // Extract substring\n    result = str.substr(startPos, length);\n    return result;\n}\n";
}
if (InStr (cppCode , "Trim(") || InStr (cppCode , "Trim (")) 
{
uperCodeLibs += "\n#include <string>\n";
uperCode = uperCode + "\nstd::string Trim(const std::string &inputString) {\n    if (inputString.empty()) return " + Chr ( 34 ) + "" + Chr ( 34 ) + ";\n\n    size_t start = inputString.find_first_not_of(" + Chr ( 34 ) + " " + Chr ( 92 ) + "t" + Chr ( 92 ) + "n" + Chr ( 92 ) + "r" + Chr ( 92 ) + "f" + Chr ( 92 ) + "v" + Chr ( 34 ) + ");\n    size_t end = inputString.find_last_not_of(" + Chr ( 34 ) + " " + Chr ( 92 ) + "t" + Chr ( 92 ) + "n" + Chr ( 92 ) + "r" + Chr ( 92 ) + "f" + Chr ( 92 ) + "v" + Chr ( 34 ) + ");\n\n    return (start == std::string::npos) ? " + Chr ( 34 ) + "" + Chr ( 34 ) + " : inputString.substr(start, end - start + 1);\n}\n";
}
if (InStr (cppCode , "StrReplace(") || InStr (cppCode , "StrReplace (")) 
{
uperCodeLibs += "\n#include <string>\n";
uperCode = uperCode + "\nstd::string StrReplace(const std::string &originalString, const std::string &find, const std::string &replaceWith) {\n    std::string result = originalString;\n    size_t pos = 0;\n\n    while ((pos = result.find(find, pos)) != std::string::npos) {\n        result.replace(pos, find.length(), replaceWith);\n        pos += replaceWith.length();\n    }\n\n    return result;\n}\n";
}
if (InStr (cppCode , "StringTrimLeft(") || InStr (cppCode , "StringTrimLeft (")) 
{
uperCodeLibs += "\n#include <string>\n";
uperCode = uperCode + "\nstd::string StringTrimLeft(const std::string &input, int numChars) {\n    return (numChars <= input.length()) ? input.substr(numChars) : input;\n}\n";
}
if (InStr (cppCode , "StringTrimRight(") || InStr (cppCode , "StringTrimRight (")) 
{
uperCodeLibs += "\n#include <string>\n";
uperCode = uperCode + "\nstd::string StringTrimRight(const std::string &input, int numChars) {\n    return (numChars <= input.length()) ? input.substr(0, input.length() - numChars) : input;\n}\n";
}
if (InStr (cppCode , "StrLower(") || InStr (cppCode , "StrLower (")) 
{
uperCodeLibs += "\n#include <algorithm>\n#include <cctype>\n#include <string>\n";
uperCode = uperCode + "\nstd::string StrLower(const std::string &string) {\n    std::string result = string;\n    std::transform(result.begin(), result.end(), result.begin(), ::tolower);\n    return result;\n}\n";
}
if (InStr (cppCode , "StrSplit(") || InStr (cppCode , "StrSplit (")) 
{
uperCodeLibs += "\n#include <string>\n";
uperCode = uperCode + "\nstd::string StrSplit(const std::string &inputStr, const std::string &delimiter, int num) {\n    size_t start = 0, end = 0, count = 0;\n\n    while ((end = inputStr.find(delimiter, start)) != std::string::npos) {\n        if (++count == num) {\n            return inputStr.substr(start, end - start);\n        }\n        start = end + delimiter.length();\n    }\n\n    if (count + 1 == num) {\n        return inputStr.substr(start);\n    }\n\n    return " + Chr ( 34 ) + "" + Chr ( 34 ) + ";\n}\n";
}
if (InStr (cppCode , "Chr(") || InStr (cppCode , "Chr (")) 
{
uperCodeLibs += "\n#include <string>\n";
uperCode = uperCode + "\nstd::string Chr(int number) {\n    return (number >= 0 && number <= 0x10FFFF) ? std::string(1, static_cast<char>(number)) : " + Chr ( 34 ) + "" + Chr ( 34 ) + ";\n}\n\n";
}
if (InStr (cppCode , "Mod(") || InStr (cppCode , "Mod (")) 
{
uperCodeLibs += "\n#include <string>\n";
uperCode = uperCode + "\nint Mod(int dividend, int divisor) {\n    return dividend % divisor;\n}\n";
}
if (InStr (cppCode , "Floor(") || InStr (cppCode , "Floor (")) 
{
uperCodeLibs += "\n#include <cmath>\n#include <limits>\n";
uperCode = uperCode + "\ndouble Floor(double num) {\n    if (std::isnan(num)) {\n        return std::numeric_limits<double>::quiet_NaN();\n    }\n    return std::floor(num);\n}\n";
}
if (InStr (cppCode , "getDataFromJSON(") || InStr (cppCode , "getDataFromJSON (")) 
{
uperCodeLibs += "\n#include <string>\n#include <vector>\n#include <map>\n#include <sstream>\n#include <iomanip>\n#include <stdexcept>\n#include <cctype>\n#include <chrono>\n#include <cmath>\n";
uperCode = uperCode + "\nstd::string trim(const std::string& str) {\n    auto start = str.begin();\n    while (start != str.end() && std::isspace(*start)) {\n        start++;\n    }\n    auto end = str.end();\n    do {\n        end--;\n    } while (std::distance(start, end) > 0 && std::isspace(*end));\n    return std::string(start, end + 1);\n}\n\nclass JSONValue {\npublic:\n    enum Type { Null, Boolean, Number, String, Array, Object };\n\n    JSONValue() : type(Null) {}\n    JSONValue(bool b) : type(Boolean), boolean_value(b) {}\n    JSONValue(double n) : type(Number), number_value(n) {}\n    JSONValue(const std::string& s) : type(String), string_value(s) {}\n    JSONValue(const std::vector<JSONValue>& a) : type(Array), array_value(a) {}\n    JSONValue(const std::map<std::string, JSONValue>& o) : type(Object), object_value(o) {}\n\n    Type getType() const { return type; }\n    bool isNull() const { return type == Null; }\n    bool isBoolean() const { return type == Boolean; }\n    bool isNumber() const { return type == Number; }\n    bool isString() const { return type == String; }\n    bool isArray() const { return type == Array; }\n    bool isObject() const { return type == Object; }\n\n    bool asBoolean() const { return boolean_value; }\n    double asNumber() const { return number_value; }\n    const std::string& asString() const { return string_value; }\n    const std::vector<JSONValue>& asArray() const { return array_value; }\n    const std::map<std::string, JSONValue>& asObject() const { return object_value; }\n\nprivate:\n    Type type;\n    bool boolean_value;\n    double number_value;\n    std::string string_value;\n    std::vector<JSONValue> array_value;\n    std::map<std::string, JSONValue> object_value;\n};\n\nclass JSONParser {\npublic:\n    static JSONValue parse(const std::string& json) {\n        size_t index = 0;\n        return parseValue(json, index);\n    }\n\nprivate:\n    static JSONValue parseValue(const std::string& json, size_t& index) {\n        skipWhitespace(json, index);\n        char c = json[index];\n        if (c == '{') {\n            return parseObject(json, index);\n        } else if (c == '[') {\n            return parseArray(json, index);\n        } else if (c == '" + Chr ( 34 ) + "') {\n            return parseString(json, index);\n        } else if (std::isdigit(c) || c == '-') {\n            return parseNumber(json, index);\n        } else if (c == 't' || c == 'f') {\n            return parseBoolean(json, index);\n        } else if (c == 'n') {\n            return parseNull(json, index);\n        }\n        throw std::runtime_error(" + Chr ( 34 ) + "Invalid JSON" + Chr ( 34 ) + ");\n    }\n\n    static JSONValue parseObject(const std::string& json, size_t& index) {\n        std::map<std::string, JSONValue> object;\n        index++; // Skip '{'\n        skipWhitespace(json, index);\n        if (json[index] == '}') {\n            index++;\n            return JSONValue(object);\n        }\n        while (true) {\n            std::string key = parseString(json, index).asString();\n            skipWhitespace(json, index);\n            if (json[index] != ':') throw std::runtime_error(" + Chr ( 34 ) + "Expected ':'" + Chr ( 34 ) + ");\n            index++;\n            JSONValue value = parseValue(json, index);\n            object[key] = value;\n            skipWhitespace(json, index);\n            if (json[index] == '}') {\n                index++;\n                return JSONValue(object);\n            }\n            if (json[index] != ',') throw std::runtime_error(" + Chr ( 34 ) + "Expected ',' or '}'" + Chr ( 34 ) + ");\n            index++;\n            skipWhitespace(json, index);\n        }\n    }\n\n    static JSONValue parseArray(const std::string& json, size_t& index) {\n        std::vector<JSONValue> array;\n        index++; // Skip '['\n        skipWhitespace(json, index);\n        if (json[index] == ']') {\n            index++;\n            return JSONValue(array);\n        }\n        while (true) {\n            array.push_back(parseValue(json, index));\n            skipWhitespace(json, index);\n            if (json[index] == ']') {\n                index++;\n                return JSONValue(array);\n            }\n            if (json[index] != ',') throw std::runtime_error(" + Chr ( 34 ) + "Expected ',' or ']'" + Chr ( 34 ) + ");\n            index++;\n            skipWhitespace(json, index);\n        }\n    }\n\n    static JSONValue parseString(const std::string& json, size_t& index) {\n        index++; // Skip opening quote\n        std::string result;\n        while (json[index] != '" + Chr ( 34 ) + "') {\n            if (json[index] == '" + Chr ( 92 ) + "" + Chr ( 92 ) + "') {\n                index++;\n                switch (json[index]) {\n                    case '" + Chr ( 34 ) + "': result += '" + Chr ( 34 ) + "'; break;\n                    case '" + Chr ( 92 ) + "" + Chr ( 92 ) + "': result += '" + Chr ( 92 ) + "" + Chr ( 92 ) + "'; break;\n                    case '/': result += '/'; break;\n                    case 'b': result += '" + Chr ( 92 ) + "b'; break;\n                    case 'f': result += '" + Chr ( 92 ) + "f'; break;\n                    case 'n': result += '" + Chr ( 92 ) + "n'; break;\n                    case 'r': result += '" + Chr ( 92 ) + "r'; break;\n                    case 't': result += '" + Chr ( 92 ) + "t'; break;\n                    default: throw std::runtime_error(" + Chr ( 34 ) + "Invalid escape sequence" + Chr ( 34 ) + ");\n                }\n            } else {\n                result += json[index];\n            }\n            index++;\n        }\n        index++; // Skip closing quote\n        return JSONValue(result);\n    }\n\n    static JSONValue parseNumber(const std::string& json, size_t& index) {\n        size_t start = index;\n        while (std::isdigit(json[index]) || json[index] == '-' || json[index] == '.' || json[index] == 'e' || json[index] == 'E') {\n            index++;\n        }\n        return JSONValue(std::stod(json.substr(start, index - start)));\n    }\n\n    static JSONValue parseBoolean(const std::string& json, size_t& index) {\n        if (json.substr(index, 4) == " + Chr ( 34 ) + "true" + Chr ( 34 ) + ") {\n            index += 4;\n            return JSONValue(true);\n        } else if (json.substr(index, 5) == " + Chr ( 34 ) + "false" + Chr ( 34 ) + ") {\n            index += 5;\n            return JSONValue(false);\n        }\n        throw std::runtime_error(" + Chr ( 34 ) + "Invalid boolean value" + Chr ( 34 ) + ");\n    }\n\n    static JSONValue parseNull(const std::string& json, size_t& index) {\n        if (json.substr(index, 4) == " + Chr ( 34 ) + "null" + Chr ( 34 ) + ") {\n            index += 4;\n            return JSONValue();\n        }\n        throw std::runtime_error(" + Chr ( 34 ) + "Invalid null value" + Chr ( 34 ) + ");\n    }\n\n    static void skipWhitespace(const std::string& json, size_t& index) {\n        while (index < json.length() && std::isspace(json[index])) {\n            index++;\n        }\n    }\n};\n\nstd::string getDataFromJSON(const std::string& json_data, const std::string& json_path) {\n    JSONValue root = JSONParser::parse(json_data);\n    std::istringstream path_stream(json_path);\n    std::string segment;\n    JSONValue current = root;\n\n    while (std::getline(path_stream, segment, '.')) {\n        segment = trim(segment);\n\n        size_t bracket_pos = segment.find('[');\n        if (bracket_pos != std::string::npos) {\n            std::string key = segment.substr(0, bracket_pos);\n            size_t index = std::stoi(segment.substr(bracket_pos + 1, segment.find(']') - bracket_pos - 1));\n\n            if (key.empty()) {\n                // This is a direct array access\n                if (current.isArray() && index < current.asArray().size()) {\n                    current = current.asArray()[index];\n                } else {\n                    return " + Chr ( 34 ) + "Array index out of bounds" + Chr ( 34 ) + ";\n                }\n            } else {\n                // This is an object access followed by array access\n                if (current.isObject() && current.asObject().find(key) != current.asObject().end()) {\n                    current = current.asObject().at(key);\n                    if (current.isArray() && index < current.asArray().size()) {\n                        current = current.asArray()[index];\n                    } else {\n                        return " + Chr ( 34 ) + "Array index out of bounds" + Chr ( 34 ) + ";\n                    }\n                } else {\n                    return " + Chr ( 34 ) + "Key not found: " + Chr ( 34 ) + " + key;\n                }\n            }\n        } else if (current.isObject() && current.asObject().find(segment) != current.asObject().end()) {\n            current = current.asObject().at(segment);\n        } else {\n            return " + Chr ( 34 ) + "Key not found: " + Chr ( 34 ) + " + segment;\n        }\n    }\n\n    if (current.isString()) return current.asString();\n    if (current.isNumber()) {\n        double num = current.asNumber();\n        if (num == floor(num)) {\n            return std::to_string(static_cast<long long>(num));\n        } else {\n            return std::to_string(num);\n        }\n    }\n    if (current.isBoolean()) return current.asBoolean() ? " + Chr ( 34 ) + "true" + Chr ( 34 ) + " : " + Chr ( 34 ) + "false" + Chr ( 34 ) + ";\n    if (current.isNull()) return " + Chr ( 34 ) + "null" + Chr ( 34 ) + ";\n\n    return " + Chr ( 34 ) + "Unsupported value type" + Chr ( 34 ) + ";\n}\n";
}
if (InStr (cppCode , "GetParams(") || InStr (cppCode , "GetParams (")) 
{
uperCodeLibs += "\n#include <iostream>\n#include <vector>\n#include <string>\n#include <filesystem>\n";
uperCode = uperCode + "\n// Platform-specific handling for command-line arguments\n#ifdef _WIN32\n    #define ARGC __argc\n    #define ARGV __argv\n#else\n    // On Linux/macOS, we need to declare these as extern variables.\n    extern char **environ; // Ensure the declaration of " + Chr ( 96 ) + "environ" + Chr ( 96 ) + "\n    int ARGC;\n    char** ARGV;\n\n    __attribute__((constructor)) void init_args(int argc, char* argv[], char* envp[]) {\n        ARGC = argc;\n        ARGV = argv;\n    }\n#endif\n\n// Function to get command-line parameters\nstd::string GetParams() {\n    std::vector<std::string> params;\n    for (int i = 1; i < ARGC; ++i) {\n        std::string arg = ARGV[i];\n        if (std::filesystem::exists(arg)) {\n            arg = std::filesystem::absolute(arg).string();\n        }\n        params.push_back(arg);\n    }\n    std::string result;\n    for (const auto& param : params) {\n        result += param + " + Chr ( 34 ) + "" + Chr ( 92 ) + "n" + Chr ( 34 ) + ";\n    }\n    return result;\n}\n";
}
if (InStr (cppCode , "BuildInVars(") || InStr (cppCode , "BuildInVars (")) 
{
uperCodeLibs += "\n#include <iostream>\n#include <chrono>\n#include <ctime>\n#include <sstream>\n#include <iomanip>\n#include <string>\n#include <limits>\n";
uperCode = uperCode + "\n// Store the start time as a global variable\nstd::chrono::time_point<std::chrono::steady_clock> programStartTime = std::chrono::steady_clock::now();\n\n// Function to get built-in variables\nstd::string BuildInVars(const std::string& varName) {\n    auto now = std::chrono::system_clock::now();\n    std::time_t currentTime = std::chrono::system_clock::to_time_t(now);\n    std::tm* localTime = std::localtime(&currentTime);\n\n    std::ostringstream oss;\n\n    if (varName == " + Chr ( 34 ) + "A_TickCount" + Chr ( 34 ) + ") {\n        // Calculate milliseconds since program start\n        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now() - programStartTime).count();\n        if (duration > std::numeric_limits<int>::max()) {\n            // Handle overflow case\n            return " + Chr ( 34 ) + "Value too large" + Chr ( 34 ) + ";\n        } else {\n            return std::to_string(static_cast<int>(duration));\n        }\n    } else if (varName == " + Chr ( 34 ) + "A_Now" + Chr ( 34 ) + ") {\n        oss << std::put_time(localTime, " + Chr ( 34 ) + "%Y-%m-%d %H:%M:%S" + Chr ( 34 ) + ");\n    } else if (varName == " + Chr ( 34 ) + "A_YYYY" + Chr ( 34 ) + ") {\n        oss << std::put_time(localTime, " + Chr ( 34 ) + "%Y" + Chr ( 34 ) + ");\n    } else if (varName == " + Chr ( 34 ) + "A_MM" + Chr ( 34 ) + ") {\n        oss << std::put_time(localTime, " + Chr ( 34 ) + "%m" + Chr ( 34 ) + ");\n    } else if (varName == " + Chr ( 34 ) + "A_DD" + Chr ( 34 ) + ") {\n        oss << std::put_time(localTime, " + Chr ( 34 ) + "%d" + Chr ( 34 ) + ");\n    } else if (varName == " + Chr ( 34 ) + "A_MMMM" + Chr ( 34 ) + ") {\n        oss << std::put_time(localTime, " + Chr ( 34 ) + "%B" + Chr ( 34 ) + ");\n    } else if (varName == " + Chr ( 34 ) + "A_MMM" + Chr ( 34 ) + ") {\n        oss << std::put_time(localTime, " + Chr ( 34 ) + "%b" + Chr ( 34 ) + ");\n    } else if (varName == " + Chr ( 34 ) + "A_DDDD" + Chr ( 34 ) + ") {\n        oss << std::put_time(localTime, " + Chr ( 34 ) + "%A" + Chr ( 34 ) + ");\n    } else if (varName == " + Chr ( 34 ) + "A_DDD" + Chr ( 34 ) + ") {\n        oss << std::put_time(localTime, " + Chr ( 34 ) + "%a" + Chr ( 34 ) + ");\n    } else if (varName == " + Chr ( 34 ) + "A_Hour" + Chr ( 34 ) + ") {\n        oss << std::put_time(localTime, " + Chr ( 34 ) + "%H" + Chr ( 34 ) + ");\n    } else if (varName == " + Chr ( 34 ) + "A_Min" + Chr ( 34 ) + ") {\n        oss << std::put_time(localTime, " + Chr ( 34 ) + "%M" + Chr ( 34 ) + ");\n    } else if (varName == " + Chr ( 34 ) + "A_Sec" + Chr ( 34 ) + ") {\n        oss << std::put_time(localTime, " + Chr ( 34 ) + "%S" + Chr ( 34 ) + ");\n    } else if (varName == " + Chr ( 34 ) + "A_Space" + Chr ( 34 ) + ") {\n        return " + Chr ( 34 ) + " " + Chr ( 34 ) + ";\n    } else if (varName == " + Chr ( 34 ) + "A_Tab" + Chr ( 34 ) + ") {\n        return " + Chr ( 34 ) + "" + Chr ( 92 ) + "t" + Chr ( 34 ) + ";\n    } else {\n        return " + Chr ( 34 ) + "" + Chr ( 34 ) + ";\n    }\n    return oss.str();\n}\n";
}
if (InStr (cppCode , "RegExReplace(") || InStr (cppCode , "RegExReplace (")) 
{
uperCodeLibs += "\n#include <string>\n#include <regex>\n#include <iostream>\n";
uperCode = uperCode + "\n// Function to perform regex replacement\nstd::string RegExReplace(const std::string& inputStr, const std::string& regexPattern, const std::string& replacement) {\n    std::regex re(regexPattern, std::regex_constants::ECMAScript | std::regex_constants::multiline);\n    return std::regex_replace(inputStr, re, replacement);\n}\n";
}
if (InStr (cppCode , "RunCMD(") || InStr (cppCode , "RunCMD (")) 
{
uperCodeLibs += "\n#include <iostream>\n#include <stdexcept>\n#include <string>\n#include <array>\n#include <memory>\n#include <cstdio>\n";
uperCode = uperCode + "\n// Function to run a system command\nstd::string RunCMD(const std::string& command) {\n    std::array<char, 128> buffer;\n    std::string result;\n#if defined(_WIN32)\n    std::unique_ptr<FILE, decltype(&_pclose)> pipe(_popen(command.c_str(), " + Chr ( 34 ) + "r" + Chr ( 34 ) + "), _pclose);\n#else\n    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(command.c_str(), " + Chr ( 34 ) + "r" + Chr ( 34 ) + "), pclose);\n#endif\n    if (!pipe) {\n        throw std::runtime_error(" + Chr ( 34 ) + "popen() failed!" + Chr ( 34 ) + ");\n    }\n    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {\n        result += buffer.data();\n    }\n    return result;\n}\n";
}
if (InStr (cppCode , "RegExMatch(") || InStr (cppCode , "RegExMatch (")) 
{
uperCodeLibs += "\n#include <iostream>\n#include <string>\n#include <regex>\n";
uperCode = uperCode + "\n// Function to perform regex matching and return the match position\nint RegExMatch(const std::string& haystack, const std::string& needleRegEx, std::string* outputVar = nullptr, int startingPos = 0) {\n    if (haystack.empty() || needleRegEx.empty()) {\n        return 0;\n    }\n\n    std::regex re(needleRegEx);\n    std::smatch match;\n\n    if (std::regex_search(haystack.begin() + startingPos, haystack.end(), match, re)) {\n        if (outputVar != nullptr) {\n            *outputVar = match.str(0);\n        }\n        return match.position(0) + 1; // To make it 1-based index\n    }\n\n    return 0;\n}\n";
}
if (InStr (cppCode , "ExitApp(") || InStr (cppCode , "ExitApp (")) 
{
uperCodeLibs += "\n#include <iostream>\n#include <cstdlib>\n";
uperCode = uperCode + "\nvoid ExitApp() {\n    std::exit(0);\n}\n";
}
if (InStr (cppCode , "SetTimer(") || InStr (cppCode , "SetTimer (")) 
{
uperCodeLibs += "\n#include <iostream>\n#include <map>\n#include <functional>\n#include <chrono>\n#include <mutex>\n#include <string>\n#include <sstream>\n#include <atomic>\n#include <thread>\n";
uperCode = uperCode + "\n// Structure to store timer information\nstruct TimerInfo {\n    std::function<void()> func;\n    int interval_ms;\n    bool active;\n    std::chrono::steady_clock::time_point last_execution;\n};\n\n// Maps to store the timers and their states\nstd::map<std::string, TimerInfo> timers;\nstd::mutex mtx; // Mutex for synchronizing access to shared data\nstd::atomic<bool> should_exit(false); // Flag to signal the application to exit\n\nvoid TimerManager() {\n    while (!should_exit) {\n        auto now = std::chrono::steady_clock::now();\n        {\n            std::lock_guard<std::mutex> lock(mtx);\n            bool any_active_timers = false;\n            for (auto& [name, timer] : timers) {\n                if (timer.active) {\n                    any_active_timers = true;\n                    auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(now - timer.last_execution);\n                    if (elapsed.count() >= timer.interval_ms) {\n                        timer.func();\n                        timer.last_execution = now;\n                    }\n                }\n            }\n            if (!any_active_timers) {\n                should_exit = true;\n            }\n        }\n        std::this_thread::sleep_for(std::chrono::milliseconds(10)); // Sleep for a short period to reduce CPU usage\n    }\n}\n\n// Global counter for unique timer names\nstatic int timer_counter = 0;\n\nvoid SetTimer(const std::function<void()>& func, const std::string& timeOrOnOff) {\n    std::lock_guard<std::mutex> lock(mtx); // Lock for safe access to shared data\n\n    // Create a unique identifier for the timer\n    std::string name = " + Chr ( 34 ) + "timer_" + Chr ( 34 ) + " + std::to_string(timer_counter++);\n\n    if (timeOrOnOff == " + Chr ( 34 ) + "On" + Chr ( 34 ) + ") {\n        timers[name] = {func, 10, true, std::chrono::steady_clock::now()};\n    } else if (timeOrOnOff == " + Chr ( 34 ) + "Off" + Chr ( 34 ) + ") {\n        // Find the timer with the matching function and turn it off\n        for (auto& [timer_name, timer] : timers) {\n            if (timer.func.target_type() == func.target_type() && timer.active) {\n                timer.active = false;\n                break;\n            }\n        }\n    } else {\n        try {\n            int interval_ms = std::stoi(timeOrOnOff);\n            timers[name] = {func, interval_ms, true, std::chrono::steady_clock::now()};\n        } catch (const std::invalid_argument&) {\n            std::cerr << " + Chr ( 34 ) + "Invalid interval value: " + Chr ( 34 ) + " << timeOrOnOff << std::endl;\n        }\n    }\n}\n";
}
if (InStr (cppCode , "getDataFromAPI(") || InStr (cppCode , "getDataFromAPI (")) 
{
uperCodeLibs += "\n#include <string>\n#include <array>\n#include <memory>\n#include <stdexcept>\n#include <cstdio>\n";
uperCode = uperCode + "\n// Function to run a system command\nstd::string getDataFromAPIRunCMD(const std::string& command) {\n    std::array<char, 128> buffer;\n    std::string result;\n#if defined(_WIN32)\n    std::unique_ptr<FILE, decltype(&_pclose)> pipe(_popen(command.c_str(), " + Chr ( 34 ) + "r" + Chr ( 34 ) + "), _pclose);\n#else\n    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(command.c_str(), " + Chr ( 34 ) + "r" + Chr ( 34 ) + "), pclose);\n#endif\n    if (!pipe) {\n        throw std::runtime_error(" + Chr ( 34 ) + "popen() failed!" + Chr ( 34 ) + ");\n    }\n    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {\n        result += buffer.data();\n    }\n    return result;\n}\n\n\n// Function to fetch data from API\nstd::string getDataFromAPI(const std::string& url) {\n    std::string command = " + Chr ( 34 ) + "curl -s " + Chr ( 34 ) + " + url;\n    return getDataFromAPIRunCMD(command);\n}\n";
}
if (InStr (cppCode , "FileCreateDir(") || InStr (cppCode , "FileCreateDir (")) 
{
uperCodeLibs += "\n#include <filesystem>\n#include <system_error>\n";
uperCode = uperCode + "\n// Creates a directory if it does not exist\nvoid FileCreateDir(const std::string& path) {\n    try {\n        // No need to handle existing directories; create_directory will not throw if it already exists\n        std::filesystem::create_directory(path);\n    } catch (const std::filesystem::filesystem_error&) {\n        // Handle errors silently; do nothing if the directory already exists or other errors occur\n    }\n}\n";
}
if (InStr (cppCode , "FileRemoveDir(") || InStr (cppCode , "FileRemoveDir (")) 
{
uperCodeLibs += "\n#include <filesystem>\n#include <system_error>\n";
uperCode = uperCode + "\n// Removes a directory if it exists\nvoid FileRemoveDir(const std::string& path) {\n    try {\n        if (std::filesystem::exists(path) && std::filesystem::is_directory(path)) {\n            std::filesystem::remove_all(path);\n        }\n    } catch (const std::filesystem::filesystem_error&) {\n        // Handle errors silently; do nothing if the directory does not exist or other errors occur\n    }\n}\n";
}
if (InStr (cppCode , "FileExist(") || InStr (cppCode , "FileExist (")) 
{
uperCodeLibs += "\n#include <filesystem>\n#include <system_error>\n";
uperCode = uperCode + "\n// Checks if a file or directory exists\nbool FileExist(const std::string& path) {\n    try {\n        return std::filesystem::exists(path);\n    } catch (const std::filesystem::filesystem_error&) {\n        // Handle errors silently; return false if an error occurs\n        return false;\n    }\n}\n";
}
if (InStr (cppCode , "isWindows(") || InStr (cppCode , "isWindows (")) 
{
uperCodeLibs += "\n#include <iostream>\n";
uperCode = uperCode + "\n// Function to check if the operating system is Windows\nbool isWindows() {\n    #ifdef _WIN32\n        return true;\n    #else\n        return false;\n    #endif\n}\n";
}
if (InStr (cppCode , "SortLikeAHK(") || InStr (cppCode , "SortLikeAHK (")) 
{
uperCodeLibs += "\n#include <string>\n#include <vector>\n#include <algorithm>\n#include <sstream>\n#include <unordered_set>\n#include <cctype>\n";
uperCode = uperCode + "\n// Helper function to trim whitespace from both ends of a string\nstd::string trim(const std::string& str) {\n    const std::string whitespace = " + Chr ( 34 ) + " " + Chr ( 92 ) + "t" + Chr ( 92 ) + "n" + Chr ( 92 ) + "r" + Chr ( 92 ) + "f" + Chr ( 92 ) + "v" + Chr ( 34 ) + ";\n    size_t start = str.find_first_not_of(whitespace);\n    if (start == std::string::npos) return " + Chr ( 34 ) + "" + Chr ( 34 ) + ";\n    size_t end = str.find_last_not_of(whitespace);\n    return str.substr(start, end - start + 1);\n}\n\n// Helper function to convert string to lowercase\nstd::string toLower(const std::string& str) {\n    std::string lowerStr = str;\n    std::transform(lowerStr.begin(), lowerStr.end(), lowerStr.begin(), ::tolower);\n    return lowerStr;\n}\n\n// Function to sort case-insensitively but ensure lowercase items come last\nbool customSortCompare(const std::string& a, const std::string& b) {\n    std::string lowerA = toLower(a);\n    std::string lowerB = toLower(b);\n    if (lowerA == lowerB) {\n        // If case-insensitive equivalent, ensure lowercase items come last\n        if (std::islower(a[0]) && std::isupper(b[0])) {\n            return false; // a should come after b\n        } else if (std::isupper(a[0]) && std::islower(b[0])) {\n            return true; // a should come before b\n        }\n        return a < b; // Otherwise, sort lexicographically\n    }\n    return lowerA < lowerB;\n}\n\n// Function to remove exact duplicates (case-sensitive)\nstd::vector<std::string> removeExactDuplicates(const std::vector<std::string>& items) {\n    std::unordered_set<std::string> seen;\n    std::vector<std::string> uniqueItems;\n    for (const auto& item : items) {\n        if (seen.find(item) == seen.end()) {\n            seen.insert(item);\n            uniqueItems.push_back(item);\n        }\n    }\n    return uniqueItems;\n}\n\n// Main sorting function\nstd::string SortLikeAHK(const std::string& input, const std::string& options) {\n    std::string delimiter = " + Chr ( 34 ) + "" + Chr ( 92 ) + "n" + Chr ( 34 ) + ";\n    bool caseInsensitive = options.find('C') != std::string::npos;\n    bool unique = options.find('U') != std::string::npos;\n    bool reverse = options.find('R') != std::string::npos;\n    bool random = options.find(" + Chr ( 34 ) + "Random" + Chr ( 34 ) + ") != std::string::npos;\n    bool numeric = options.find('N') != std::string::npos;\n\n    // Custom delimiter\n    if (options.find('D') != std::string::npos) {\n        size_t delimiterPos = options.find('D') + 1;\n        if (delimiterPos < options.size()) {\n            delimiter = options.substr(delimiterPos, 1);\n        }\n    }\n\n    // Split input by delimiter\n    std::vector<std::string> items;\n    std::stringstream ss(input);\n    std::string item;\n    while (std::getline(ss, item, delimiter[0])) {\n        item = trim(item);  // Trim whitespace from each item\n        if (!item.empty()) {\n            items.push_back(item);\n        }\n    }\n\n    // Sort items\n    if (numeric) {\n        std::sort(items.begin(), items.end(), [](const std::string& a, const std::string& b) {\n            return std::stoi(a) < std::stoi(b);\n        });\n    } else {\n        std::sort(items.begin(), items.end(), customSortCompare);\n    }\n\n    // Remove exact duplicates if needed\n    if (unique) {\n        items = removeExactDuplicates(items);\n    }\n\n    // Apply reverse order if needed\n    if (reverse) {\n        std::reverse(items.begin(), items.end());\n    }\n\n    // Separate uppercase and lowercase items\n    std::vector<std::string> uppercaseItems;\n    std::vector<std::string> lowercaseItems;\n    \n    for (const auto& item : items) {\n        if (std::isupper(item[0])) {\n            uppercaseItems.push_back(item);\n        } else {\n            lowercaseItems.push_back(item);\n        }\n    }\n\n    // Combine sorted uppercase items with sorted lowercase items\n    std::string result;\n    for (const auto& item : uppercaseItems) {\n        result += item;\n        result += delimiter;\n    }\n    for (const auto& item : lowercaseItems) {\n        result += item;\n        if (&item != &lowercaseItems.back()) {\n            result += delimiter;\n        }\n    }\n\n    // Remove trailing delimiter if necessary\n    if (!result.empty() && result.back() == delimiter[0]) {\n        result.pop_back();\n    }\n\n    return result;\n}\n";
}
uperCodeLibs = SortLikeAHK(uperCodeLibs, "U");
downCode = "\nreturn 0;\n}";
cppCode = uperCodeLibs + "\n" + uperCode + "\n" + upCode + cppCode + downCode;
cppCode = StrReplace ( cppCode , "" , "" ) ;
//MsgBox, % cppCode
filePathOfCode = StringTrimRight(filePathOfCode, 4);
filePathOfCode = filePathOfCode + "cpp";
FileDelete(filePathOfCode);
FileAppend(cppCode, filePathOfCode);

return 0;
}