'''
거의 최단 경로
https://www.acmicpc.net/problem/5719
그래프 이론, 그래프 탐색, 다익스트라
'''



from collections import deque
import heapq
import sys

input = sys.stdin.readline

INF = sys.maxsize

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost and not dropped[now][i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))



def bfs():
    q = deque()
    q.append(end)
    while q:
        now = q.popleft()
        if now == start:
            continue
        for prev, cost in reverse_adj[now]:
            if distance[now] == (distance[prev] + cost) and not dropped[prev][now]:
                dropped[prev][now] = True
                q.append(prev)



while True:
    N, M = map(int, input().rstrip().split())
    if N == 0 and M == 0:
        break
    start, end = map(int, input().rstrip().split())
    adj = [[] for _ in range(N)]
    reverse_adj = [[] for _ in range(N)]
    
    for _ in range(M):
        x, y, cost = map(int, input().split())
        adj[x].append((y, cost))
        reverse_adj[y].append((x, cost))
    
    dropped = [[False] * (N) for _ in range(N)]
    distance = [INF] * (N)
    dijkstra()
    bfs()
    distance = [INF] * (N)
    dijkstra()
    if distance[end] != INF:
        print(distance[end])
    else:
        print(-1)