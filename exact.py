import itertools

def main():

    nodes = int(input())
    num_edges = int((nodes*(nodes-1))/2)
    adj_list = {}
    for _ in range(num_edges):
        u, v, w = [num for num in input().split()]
        w = int(w)
        if u in adj_list:
            adj_list[u].append((v, w))
        else:
            adj_list[u] = [(v, w)]

    print(adj_list)





if __name__ == "__main__":
    main()
