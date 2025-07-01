from itertools import combinations
import os
import argparse

def get_unique_character_combinations(text):
    unique_characters = set(text)
    return combinations(unique_characters, 2)

def is_alternating(s):
    first, second = list(set(s))
    expected1 = ''.join(first if i % 2 == 0 else second for i in range(len(s)))
    expected2 = ''.join(second if i % 2 == 0 else first for i in range(len(s)))
    return s == expected1 or s == expected2

def get_longest_version(text):
    longest_versions = []
    max_length = 0
    
    for characters_to_include in get_unique_character_combinations(text):
        filtered = ''.join(c for c in text if c in characters_to_include)
        
        if not is_alternating(filtered):
            continue 
    
        if len(filtered) > max_length:
            longest_versions = [filtered]
            max_length = len(filtered)

        elif len(filtered) == max_length:
            longest_versions.append(filtered)

    if longest_versions: 
        return longest_versions
    
    return 0 


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('s', type=str, help='the string to process')
    args = parser.parse_args()

    longest = get_longest_version(args.s)

    if not longest:
        print(0)
    else:
        for version in longest:
            print(version)

if __name__ == '__main__':
    main() 
