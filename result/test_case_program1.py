def test_sort_string_by_frequency():
    # Test sorting a string with repeated characters
    assert sort_string_by_frequency('aaabbbccc') == 'cccbbbaaa'

    # Test sorting a string with different frequencies of characters
    assert sort_string_by_frequency('ababab') == 'aaaabbb'

    # Test sorting an empty string
    assert sort_string_by_frequency('') == ''

    # Test sorting a string with a single character
    assert sort_string_by_frequency('a') == 'a'

    # Test sorting a string with all unique characters
    assert sort_string_by_frequency('abcdefg') == 'abcdefg'

    # Test sorting a string with spaces and punctuation
    assert sort_string_by_frequency('The quick brown fox jumps over the lazy dog.') == 'eeooorrttThhhiiiqckkbbwwnfxjmpsvlyadgu.'

test_sort_string_by_frequency()
