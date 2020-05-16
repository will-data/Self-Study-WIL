def solution(n, costs):
    parent = {};
    rank = {}

    def make_set(v):
        parent[v] = v
        rank[v] = 0

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v, u):
        root1 = find(v)
        root2 = find(u)
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

    for v in range(n):
        make_set(v)

    costs.sort(key=lambda i: i[2])
    answer = 0

    for start, end, cost in costs:
        if find(start) != find(end):
            union(start, end)
            answer += cost

    return answer