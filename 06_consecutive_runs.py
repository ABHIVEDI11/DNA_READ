def find_consecutive_runs(data, pattern):
    # Initialize an empty list to store runs
    runs = []
    # Initialize index variable
    i = 0
    # Loop through the data
    '''At the beginning of the loop, i is initialized to 0.
    The condition i < len(data) is checked.
    If i is less than the length of the data string, the loop body executes.
    If i is equal to or greater than the length of the data string, the loop terminates.'''
    while i < len(data):
        # Check if the substring matches the pattern
        if data[i:i + len(pattern)] == pattern:
            # Store the start of the run
            run_start = i
            # Move index forward as long as the pattern matches
            while i < len(data) and data[i:i + len(pattern)] == pattern:
                i += len(pattern)
            # Append the start and end of the run to the list
            runs.append((run_start, i - 1))  # Corrected end index to i - 1
        else:
            # Move to the next character if no match
            i += 1
    return runs

# Example data and pattern
data = "AAABBBCCCAAABBB"
pattern = "AAA"

# Print the runs of the pattern in the data
print(find_consecutive_runs(data, pattern))
