# Problem 1: First Non-Repeating Character
# Given a string, return the first non-repeating character in it and return its index.
# If it does not exist, return -1.

# Example:
# Input: s = "uday samsani"
# Output: ('u', 0)

def find_first_unique_character(string):
    char_dict = {}

    for char in string:
        if char == ' ':
            continue
        if char in char_dict.keys():
            char_dict[char] = char_dict[char]+1
        else:
            char_dict[char] = 1

    for index in range(len(string)):
        if char_dict[string[index]] == 1:
            return string[index], index
    return -1

def main():
    result = find_first_unique_character("uday samsani")
    if result != -1:
        print(f"The first non-repeating character is '{result[0]}' at index {result[1]}.")
    else:
        print("No non-repeating character found.")

if __name__ == '__main__':
    main()