def find_substring_positions(data, pattern):
    # Initialize an empty list to store positions
    positions = []
    # Loop through the data to find matching positions
    for i in range(len(data) - len(pattern) + 1):
        # Check if the substring matches the pattern
        if data[i:i + len(pattern)] == pattern:
            # If match is found, add the position to the list
            positions.append(i)
    return positions

# Example data and pattern
data = "ACGTACGTACG"
pattern = "CGT"

# Print the positions of the pattern in the data
print(find_substring_positions(data, pattern))
