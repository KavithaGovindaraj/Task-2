
#1)

def count_vowels(string):
    # Convert the string to lowercase to handle both uppercase and lowercase vowels
    string = string.lower()
    
    # Initialize counts for each vowel
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0
    
    # Total count of all vowels
    total_vowels = 0
    
    # Iterate through each character in the string
    for char in string:
        if char == 'a':
            count_a += 1
            total_vowels += 1
        elif char == 'e':
            count_e += 1
            total_vowels += 1
        elif char == 'i':
            count_i += 1
            total_vowels += 1
        elif char == 'o':
            count_o += 1
            total_vowels += 1
        elif char == 'u':
            count_u += 1
            total_vowels += 1
    
    # Print the counts of each vowel
    print("Count of each vowel:")
    print(f"A: {count_a}")
    print(f"E: {count_e}")
    print(f"I: {count_i}")
    print(f"O: {count_o}")
    print(f"U: {count_u}")
    
    # Print the total number of vowels
    print(f"Total number of vowels: {total_vowels}")

# usage:1
string = "Guvi Geeks Network Private limited"
count_vowels(string)


#Output:


#Count of each vowel:
#A: 1
#E: 5
#I: 4
#O: 1
#U: 1
#Total number of vowels: 12



#2)

# Number of rows in the pyramid (can be adjusted as needed)
num_rows = 20  # We'll create a pyramid with 20 rows

# Outer loop for each row of the pyramid
for i in range(1, num_rows + 1):
    # Print spaces for alignment
    print(' ' * (num_rows - i), end='')
    
    # Inner loop to print numbers for the current row
    current_number = 1
    for j in range(1, i + 1):
        print(f'{current_number:2} ', end='')
        current_number += 1
    
    # Move to the next line after printing all numbers in the current row
    print()



# Output:

#                    1
#                   1  2
#                  1  2  3
#                 1  2  3  4
#                1  2  3  4  5
#               1  2  3  4  5  6
#              1  2  3  4  5  6  7
#             1  2  3  4  5  6  7  8
#            1  2  3  4  5  6  7  8  9
#           1  2  3  4  5  6  7  8  9 10
#          1  2  3  4  5  6  7  8  9 10 11
#         1  2  3  4  5  6  7  8  9 10 11 12
#        1  2  3  4  5  6  7  8  9 10 11 12 13
#       1  2  3  4  5  6  7  8  9 10 11 12 13 14
#      1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
#     1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
#    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17
#   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18
#  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
# 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20


#3)


def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    filtered_string = ""

    for char in input_string:
        if char not in vowels:
            filtered_string += char

    return filtered_string

input_string = "Hello, this is a sample string with vowels."
result = remove_vowels(input_string)
print("Original string:", input_string)
print("String with vowels removed:", result)

#Output:

#Original string: Hello, this is a sample string with vowels.
#String with vowels removed: Hll, ths s  smpl strng wth vwls.


#4)

def count_unique_characters(input_string):
    # Use a set to store unique characters:
    unique_chars = set()

    # Iterate through each character in the input string:
    for char in input_string:
        unique_chars.add(char)

    # Return the number of unique characters:
    return len(unique_chars)

#  usage:
input_string = "Hello, World!"
unique_count = count_unique_characters(input_string)
print(f"Input string: '{input_string}'")
print(f"Number of unique characters: {unique_count}")


#Output:

#Input string: 'Hello, World!'
#Number of unique characters: 10


#5)

def is_palindrome(input_string):
    # Remove spaces and convert to lowercase
    processed_string = input_string.replace(" ", "").lower()
    
    # Check if the processed string is equal to its reverse
    return processed_string == processed_string[::-1]

# Example usage:
input_string1 = "Madam"
input_string2 = "Hello"
input_string3 = "A man a plan a canal Panama"

print(f"Is '{input_string1}' a palindrome? {is_palindrome(input_string1)}")
print(f"Is '{input_string2}' a palindrome? {is_palindrome(input_string2)}")
print(f"Is '{input_string3}' a palindrome? {is_palindrome(input_string3)}")

#Output:

#Is 'Madam' a palindrome? True
#Is 'Hello' a palindrome? False
#Is 'A man a plan a canal Panama' a palindrome? True



#6)

def longest_common_substring(str1, str2):
    # Initialize variables to store the length of the longest common substring and its ending position
    max_length = 0
    end_position = 0
    
    # Initialize a 2D list to store lengths of longest common suffixes of substrings
    # dp[i][j] will store the length of longest common substring ending at str1[i-1] and str2[j-1]
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    # Fill the dp array
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_position = i  # or j, since both are the same in this case
            else:
                dp[i][j] = 0  # reset to zero for non-matching characters
    
    # Extract the longest common substring from str1
    longest_substring = str1[end_position - max_length : end_position]
    
    return longest_substring

# Example usage:
str1 = "abcdef"
str2 = "abdf"

longest_substring = longest_common_substring(str1, str2)
print(f"The longest common substring between '{str1}' and '{str2}' is '{longest_substring}'")



#Output:
#The longest common substring between 'abcdef' and 'abdf' is 'ab'


#7)


def most_frequent_char(input_string):
    # Remove whitespace from the string
    input_string = input_string.replace(" ", "")
    
    # Create a dictionary to keep track of character frequencies
    char_count = {}
    
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the character with the maximum frequency
    most_frequent = max(char_count, key=char_count.get)
    
    return most_frequent

# Example usage:
input_string = "example string with some characters"
print("The most frequent character is:", most_frequent_char(input_string))


#Output:
#The most frequent character is: e


#8)

def are_anagrams(string1, string2):
    # Remove whitespace and convert to lowercase
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    
    # Check if the sorted characters of both strings are the same
    return sorted(string1) == sorted(string2)

# Example usage:
string1 = "Listen"
string2 = "Silent"
print(are_anagrams(string1, string2))  

string1 = "Hello"
string2 = "World"
print(are_anagrams(string1, string2)) 


#Output:
#True
#False

#9)


def count_words(input_string):
    # Split the string into words based on whitespace
    words = input_string.split()
    
    # Return the number of words
    return len(words)

# Example usage:
input_string = "This is an example string with several words."
print("Number of words:", count_words(input_string)) 


#Output:
#Number of words: 8
