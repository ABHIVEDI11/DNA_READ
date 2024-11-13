def find_repeating_patterns(data, length):
    # Initialize a dictionary to store patterns and their counts
    patterns = {}
    # Loop through the data string to extract patterns of the given length
    for i in range(len(data) - length + 1):
        # Extract a pattern of the specified length
        pattern = data[i:i + length]
        # If the pattern is already in the dictionary, increment its count
        if pattern in patterns:
            patterns[pattern] += 1
        # If the pattern is not in the dictionary, add it with a count of 1
        else:
            patterns[pattern] = 1
    # Filter only repeating patterns (patterns with a count greater than 1)
    repeating_patterns = {k: v for k, v in patterns.items() if v > 1}
    # Return the dictionary of repeating patterns
    return repeating_patterns

# Example data and length
data = "ACGTACGTACG"
length = 3

# Print the dictionary of repeating patterns
print(find_repeating_patterns(data, length))
