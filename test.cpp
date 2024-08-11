#include <cstdint>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <type_traits>
#include <vector>

// Forward declare OneIndexedArray template
template <typename T>
class OneIndexedArray;

#define OneIndexedArray_DEFINED

// Helper function to set the internal array's size as a string
template <typename T>
void setInternalArraySize(T& element, size_t size) {
    element = static_cast<T>(size);
}

// Specialization for std::string
template <>
void setInternalArraySize<std::string>(std::string& element, size_t size) {
    element = std::to_string(size);
}

// One-indexed dynamic array class
template <typename T>
class OneIndexedArray {
private:
    std::vector<T> internalArray;

public:
    OneIndexedArray() {
        internalArray.push_back(T{}); // Placeholder for element count
    }

    void add(const T& newElement) {
        internalArray.push_back(newElement);
        setInternalArraySize(internalArray[0], internalArray.size() - 1);
    }

    void setArray(const std::vector<T>& newArray) {
        internalArray.resize(newArray.size() + 1);
        std::copy(newArray.begin(), newArray.end(), internalArray.begin() + 1);
        setInternalArraySize(internalArray[0], newArray.size());
    }

    T& operator[](size_t index) {
        if (index >= internalArray.size()) {
            internalArray.resize(index + 1);
            setInternalArraySize(internalArray[0], internalArray.size() - 1);
        }
        return internalArray[index];
    }

    const T& operator[](size_t index) const {
        if (index >= internalArray.size()) {
            throw std::out_of_range("Index out of range");
        }
        return internalArray[index];
    }

    size_t size() const {
        return static_cast<size_t>(internalArray.size() - 1);
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
OneIndexedArray<std::string> arrSplit(const std::string& text, const std::string& delimiter) {
    OneIndexedArray<std::string> array;
    std::vector<std::string> words = split(text, delimiter);
    array.setArray(words);
    return array;
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

void testIntArray(OneIndexedArray<int> intArray, std::string secondParam)
{
print(intArray);
print(std::string("the secondParam is: ") + secondParam);
}
void testStrArray(OneIndexedArray<std::string> strArray, std::string secondParam)
{
print(strArray);
print(std::string("the secondParam is: ") + secondParam);
}
void testFloatArray(OneIndexedArray<float> floatArray, std::string secondParam)
{
print(floatArray);
print(std::string("the secondParam is: ") + secondParam);
}
// Simply label the main function since before we used other functions
int main(int argc, char* argv[])
{
OneIndexedArray<int> intArray;
OneIndexedArray<std::string> strArray;
OneIndexedArray<float> floatArray;
intArray.add(5);
strArray.add(std::string("hello"));
floatArray.add(3.14);
std::string secondParam = std::string("this is the secondParam");
testIntArray ( intArray , secondParam ) ;
testStrArray ( strArray , secondParam ) ;
testFloatArray ( floatArray , secondParam ) ;
return 0;
}