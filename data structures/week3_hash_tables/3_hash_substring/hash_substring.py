# python3

from random import randint
p = 10**9 + 7
x = randint(1, p-1)

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_hash(s):
    result = 0
    ex = 1
    for ch in s:
        result = (result + ex * ord(ch)) % p
        ex = (ex * x) % p
    return result

def precompute_hashes(text, pattern_length):
    hashes = [0] * (len(text) - pattern_length + 1)
    hashes[-1] = get_hash(text[len(text)-pattern_length:len(text)])
    power = (x ** pattern_length) % p
    for i in range(len(hashes) - 2, -1, -1):
        hashes[i] = (x * hashes[i+1] + ord(text[i]) - power * ord(text[i+pattern_length])) % p
    return hashes

def get_occurrences(pattern, text):
    occurrences = []
    hashes = precompute_hashes(text, len(pattern))
    pattern_hash = get_hash(pattern)
    for i in range(len(hashes)):
        if hashes[i] == pattern_hash and text[i:i+len(pattern)] == pattern:
            occurrences.append(i)
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

