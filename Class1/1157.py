'''
단어 공부
https://www.acmicpc.net/problem/1157
'''

import sys


a = input().lower()
word_list = list(set(a))
cnt = [a.count(i) for i in word_list]
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper())



'''
Mississipi
-----
?
'''