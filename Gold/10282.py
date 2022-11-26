'''
해킹
https://www.acmicpc.net/problem/10282
그래프 이론, 다익스트라
'''


import sys
import heapq

input = sys.stdin.readline

T = int(input())
def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] >= dist:
            for i in adj[now]:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(heap, (cost, i[0]))

for _ in range(T):
    n, d, c = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    distance = [1e9] * (n + 1)
    for _ in range(d):
        a, b, s = map(int, input().split())
        adj[b].append((a, s))
    dijkstra(c)
    count = 0
    max_distance = 0
    for i in distance:
        if i != 1e9:
            count += 1
            if i > max_distance:
                max_distance = i
    print(count, max_distance)

