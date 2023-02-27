"""
solution for
    https://leetcode.com/problems/substring-with-concatenation-of-all-words/

    Heavy use of Generators, nearly a one liner
"""
from itertools import permutations
from re import compile

def main():
    words = ["bar","foo","the"]
    s = "barfoofoobarthefoobarman"
    # Sadly, due to the possibility of returning <None> for <regex.search(STRING)>, there is now one liner with generator syntax possible
    matches = (compile("".join(perm)).search(s) for perm in permutations(words, len(words)))
    print(list(match.start() for match in matches if match)) 
    
#   Per line verison
#    perms = permutations(words, len(words))
#    perms = ("".join(perm) for perm in perms)
#    gen_idx = (re.compile(perm).search(s) for perm in perms) 
#    start_idx = (match.start() for match in gen_idx if match)


if __name__ == "__main__":
    main()
