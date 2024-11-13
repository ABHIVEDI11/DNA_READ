def find_alternating_patterns(data, pattern1, pattern2):
    # Initialize a list to store positions of alternating patterns
    alternating_positions = []
    # Set the expected pattern to pattern1 initially
    expected_pattern = pattern1
    i = 0
    # Loop through the data string to find alternating patterns
    while i <= len(data) - len(expected_pattern):
        # Check if the substring matches the expected pattern
        if data[i:i + len(expected_pattern)] == expected_pattern:
            alternating_positions.append(i)
            # Switch expected pattern for next iteration
            expected_pattern = pattern2 if expected_pattern == pattern1 else pattern1
            # Move index forward by the length of pattern1
            i += len(pattern1)
        else:
            break
    # Return the list of positions if there are more than one alternating patterns
    return alternating_positions if len(alternating_positions) > 1 else []

# Example data and patterns
data = "ABBAABBAAB"
pattern1 = "AB"
pattern2 = "BA"

# Print the list of positions where alternating patterns occur
print(find_alternating_patterns(data, pattern1, pattern2))
