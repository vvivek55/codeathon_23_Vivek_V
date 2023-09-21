def sort_array(arr):
    return sorted(arr)

# Test cases
test_cases = [
    ([100, 180, 260, 310, 40, 535, 695], [40, 100, 180, 260, 310, 535, 695]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
]

for i, (input_arr, expected_output) in enumerate(test_cases):
    result = sort_array(input_arr)
    assert result == expected_output, f"Test case {i + 1} failed: {result}"

# Performance Testing
import random
import time

large_input = [random.randint(1, 10000) for _ in range(50000)]

start_time = time.time()
sorted_large_input = sort_array(large_input)
end_time = time.time()

print(f"Sorting 50000 elements took {end_time - start_time:.4f} seconds.")

