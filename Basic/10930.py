'''
SHA-256
https://www.acmicpc.net/problem/10930
'''

import sys
import hashlib

input = sys.stdin.readline

data = input().strip()

print(hashlib.sha256(data.encode()).hexdigest())