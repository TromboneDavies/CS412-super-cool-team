import itertools

def main():

    nodes = int(input())
    num_edges = int((nodes*(nodes-1))/2)
    adj_list = {}
    visited = {}
    for _ in range(num_edges):
        u, v, w = [num for num in input().split()]
        w = int(w)
        if u in adj_list:
            adj_list[u].append((v, w))
        else:
            adj_list[u] = [(v, w)]
        if v in adj_list:
            adj_list[v].append((u, w))
        else:
            adj_list[v] = [(u, w)]
        if u not in visited:
            visited[u] = "unmarked"
        if v not in visited:
            visited[v] = "unmarked"

    print(adj_list)
    print(visited)

    p = itertools.permutations(adj_list)
    # leave the start vertex out and place at the start and end
    for j in list(p):
        print(j)



if __name__ == "__main__":
    main()
