def find_palindromic_patterns(data, length):
    # Initialize a list to store palindromic patterns
    palindromic_patterns = []
    # Loop through the data string to extract patterns of the given length
    for i in range(len(data) - length + 1):
        # Extract a pattern of the specified length
        pattern = data[i:i + length]
        # Check if the pattern is a palindrome
        if pattern == pattern[::-1]:
            # If it's a palindrome, add it to the list
            palindromic_patterns.append(pattern)
    # Return the list of palindromic patterns
    return palindromic_patterns

# Example data and length
data = "AGCTTCTGAATAGTG"
length = 3

# Print the list of palindromic patterns
print(f"Palindromic Patterns: {find_palindromic_patterns(data, length)}")
