#1. Brute Force Approach
#Idea: Split the string into words using spaces, then find the last word and return its length.
def length_of_last_word_brute_force(s):
    words = s.split()  # Split by spaces
    return len(words[-1]) if words else 0

# Time: 
# O(n) — Single traversal from the end.
# Space: 
# O(1) — No additional space used.


# 2. Using Reverse Traversal
# Idea: Traverse the string from the end, skipping trailing spaces and counting characters until the first space after a word is found.
def length_of_last_word_reverse(s):
    i = len(s) - 1
    length = 0

    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1

    # Count characters in the last word
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    return length

# Time: 
# O(n) — Traverses the string once.
# Space: 
# O(1) — Constant space used.


# 3. Using rstrip and split
# Idea: Remove trailing spaces with rstrip and then split the string.
def length_of_last_word_split(s):
    return len(s.rstrip().split()[-1])


# Time: 
# O(n) — Removing trailing spaces and splitting.
# Space: 
# O(k) — Temporary space for the split list.

                      
# 4. Optimal Approach with String Manipulation
# Idea: Use rstrip to remove trailing spaces and then traverse from the end to count the last word's length.
def length_of_last_word_optimal(s):
    s = s.rstrip()  # Remove trailing spaces
    length = 0
    for char in reversed(s):
        if char == ' ':
            break
        length += 1
    return length


# Time: 
# O(n) — Single traversal from the end.
# Space: 
# O(1) — No additional space used.


# 5. Using Regular Expressions
# Idea: Use regex to extract the last word.
import re

def length_of_last_word_regex(s):
    match = re.findall(r'\b\w+\b', s)
    return len(match[-1]) if match else 0

# Time: 
# O(n) — Depends on regex parsing.
# Space: 
# O(k) — Space for the list of matches.


# Preferred Solution
# The reverse traversal approach is often preferred as it is both time-efficient and space-efficient, making it suitable for scenarios with large strings.
