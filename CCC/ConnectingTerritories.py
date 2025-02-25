import heapq

def yeah():
    R = int(input())
    C = int(input())
    M = int(input())
    if R > 10:
        R = 10
    if C > 10:
        C = 10
    def tCost(r, c):
        return ((c - 1) % M) + 1
    wheretogo = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1), (0, 1), 
                  (1, -1), (1, 0), (1, 1)]
    distance = [[float('inf')] * C for _ in range(R)]
    pq = []
    for c in range(C):
        cost = tCost(1, c + 1)
        distance[0][c] = cost
        heapq.heappush(pq, (cost, 0, c))
    while pq:
        cCost, r, c = heapq.heappop(pq)
        if r == R - 1:
            print(cCost)
            return
        for dr, dc in wheretogo:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                nCost = cCost + tCost(nr + 1, nc + 1)
                if nCost < distance[nr][nc]:
                    distance[nr][nc] = nCost
                    heapq.heappush(pq, (nCost, nr, nc))
    print(min(distance[R - 1]))

yeah()