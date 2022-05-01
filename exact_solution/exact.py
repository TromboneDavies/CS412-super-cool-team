import itertools
import sys
import time

"""
    Name: Deven Sarma
"""


def main():
    nodes = int(input())
    start_node = input()
    num_edges = int((nodes * (nodes - 1)) / 2)  # calculate number of edges based on n nodes
    adj_list = {}
    permutation_list = set()  # list to contain all nodes except the start node in
    # order to compute permutations

    for _ in range(num_edges):
        u, v, w = [num for num in input().split()]
        w = int(w)
        # add u & v into adjacency list both ways to show undirected graph
        if u in adj_list:
            adj_list[u].append((v, w))
        else:
            adj_list[u] = [(v, w)]
        if v in adj_list:
            adj_list[v].append((u, w))
        else:
            adj_list[v] = [(u, w)]
        # if u & v aren't the start node, add them to the set
        if u != start_node:
            permutation_list.add(u)
        if v != start_node:
            permutation_list.add(v)
    
    start_time = time.time()
    cost, path = permute(adj_list, permutation_list, start_node)
    #cost, path = shortest_path(adj_list, all_permutations)
    end_time = time.time()
    print("Number of nodes: ", nodes)
    print("Shortest path:   ",cost)
    print("Path: ",path)
    print("Execution time excluding input: ",end_time-start_time)
    print()


def permute(adjacency_list, permutation_list, start_node):
    permutations = itertools.permutations(permutation_list)
    best_cost = sys.maxsize
    best_path = None

    for permutation in permutations:
        this_permutation = list(permutation)
        this_permutation.insert(0, start_node)  # add start_node to front of list
        this_permutation.append(start_node)     # add start_node to end of list
        this_cost = shortest_path(adjacency_list, this_permutation) # calculate cost of this_permutation
        if this_cost < best_cost:
            best_path = this_permutation
        best_cost = min(best_cost, this_cost)

    return best_cost, best_path

def shortest_path(adjacency_list, permutation):
    this_cost = 0
    start_node = permutation[0]
    for node in permutation[1:]:
        # look up cost from start_node to node
        tup = [item for item in adjacency_list[start_node] if node in item]
        this_cost += tup[0][1]
        start_node = node

    return this_cost

if __name__ == "__main__":
    main()
