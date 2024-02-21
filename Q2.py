def replace_characters(input_str, k):
    replaced_str = ''
    last_seen = {}
    # sliding window techniques
    for i, char in enumerate(input_str):
        if char in last_seen and i - last_seen[char] <= k:
            replaced_str += '-'
        else:
            replaced_str += char
        last_seen[char] = i
    return replaced_str

# Test cases
if __name__ == "__main__":
    test_cases = [("abcdefaxc", 10), ("abcdefaxcqwertba", 10)]
    for input_str, k in test_cases:
        output_str = replace_characters(input_str, k)
        print(f"Input: {input_str} {k}")
        print(f"Output: {output_str}")
