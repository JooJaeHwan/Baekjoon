'''
알파벳 찾기
https://www.acmicpc.net/problem/10809
'''

import sys

from string import ascii_lowercase
input = sys.stdin.readline

alphabet_dict = {}
visited = [False] * 26
word = str(input().rstrip())

for i in ascii_lowercase:
	alphabet_dict[i] = -1
    

for idx, w in enumerate(word):
    if alphabet_dict[w] == -1:
        alphabet_dict[w] = idx
    else: continue

print(' '.join(map(str, alphabet_dict.values())))
