def sort_string_by_frequency(s):
    # Create a dictionary to store the frequency of each character
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    # Sort the characters by frequency
    sorted_chars = sorted(freq, key=freq.get, reverse=True)
    # Build the sorted string
    sorted_str = ''
    for c in sorted_chars:
        sorted_str += c * freq[c]
    return sorted_str

# Example usage
input_str = 'hello world'
output_str = sort_string_by_frequency(input_str)
print(output_str)  # Output: 'llloohe wrd'

input_str = 'tree'
output_str = sort_string_by_frequency(input_str)
print(output_str)  # Output: 'eetr'
