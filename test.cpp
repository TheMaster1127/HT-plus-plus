#include <chrono>
#include <cstdint>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <limits>
#include <sstream>
#include <string>
#include <type_traits>

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


int main(int argc, char* argv[])
{
print(std::string("Current local time: ") + BuildInVars("A_Now"));
print(std::string("Current year: ") + BuildInVars("A_YYYY"));
print(std::string("Current month: ") + BuildInVars("A_MM"));
print(std::string("Current day: ") + BuildInVars("A_DD"));
print(std::string("Full name of current month: ") + BuildInVars("A_MMMM"));
print(std::string("Abbreviated name of current month: ") + BuildInVars("A_MMM"));
print(std::string("Full name of current day: ") + BuildInVars("A_DDDD"));
print(std::string("Abbreviated name of current day: ") + BuildInVars("A_DDD"));
print(std::string("Current hour: ") + BuildInVars("A_Hour"));
print(std::string("Current minute: ") + BuildInVars("A_Min"));
print(std::string("Current second: ") + BuildInVars("A_Sec"));
print(std::string("Hello") + BuildInVars("A_Space") + std::string("man"));
print(std::string("|") + BuildInVars("A_Tab") + std::string("Hello man|"));
return 0;
}