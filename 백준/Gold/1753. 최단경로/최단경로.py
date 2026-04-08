import sys
input = sys.stdin.readline

from heapq import heappush, heappop

def dijkstra():

    mins = [float('inf') for _ in range(V+1)]
    mins[START] = 0
    pq = [(0, START)]

    while pq:
        dist, node = heappop(pq) # 누적 거리, 대상 노드
        if dist > mins[node]: # 볼 필요 없는 애면 continue
            continue

        for edge in edges[node]:
            edge_dist, edge_dest = edge
            sum_dist = dist + edge_dist

            if mins[edge_dest] <= sum_dist:
                continue

            mins[edge_dest] = sum_dist
            heappush(pq, (sum_dist, edge_dest))

    return mins



V, E = map(int, input().split())
START = int(input())  # 시작 정점
edges = [[] for _ in range(V+1)]

for line in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((w, v))

result = dijkstra()

for i in range(1, V + 1):
    if result[i] == float('inf'):
        print("INF")
    else:
        print(result[i])