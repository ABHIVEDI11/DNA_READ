def count_pattern_occurrences(data, pattern):
    # Initialize the count of pattern occurrences
    count = 0
    # Loop through the data string
    for i in range(len(data) - len(pattern) + 1):
        # Check if the substring matches the pattern
        if data[i:i + len(pattern)] == pattern:
            count += 1
    # Return the total count of occurrences
    return count

# Example data and pattern
data = "AABBCCDDAABB"
pattern = "AAB"

# Print the count of pattern occurrences
print(count_pattern_occurrences(data, pattern))
