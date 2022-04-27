import random
import itertools
from math import sqrt
import time

def main():
    # concept: ant colony optimization (ACO)
    #  FOR EACH ANT:
    #   1. probabilistically select an edge based on the weight and pheromones levels
    #   2. travel to that path, adding pheromones to the edge
    #      - traveling down a path takes time, so an ant might be skipped in a round
    #        due to it traveling to a node during that time
    #   3. repeat until no more nodes are possible, and return home
    # place ants randomly and allow them to follow this structure. decrease pheromones slightly
    # for each round.                                       

    # constants
    num_ants = 1000
    pheromone_increase = 1.0
    pheromone_dissapate = 3/10 # bigger is faster

    # get user input to build graph
    adj = {}
    nodes = set()
    max_weight = 0
    for _ in range(int(input())):
        u, v, w = input().split()
        w = int(w)
        adj[(u,v)] = w
        adj[(v,u)] = w
        if u not in nodes: nodes.add(u)
        if v not in nodes: nodes.add(v)
        if w > max_weight: max_weight = w

    # just ant things #antlife
    position = {n: random.choice(list(nodes)) for n in range(num_ants)}
    marked = {n: set(position[n]) for n in range(num_ants)} # marked list for each ant (avoiding classes lol)
    marked_all = [False] * num_ants # each ant can set its marked_all to true for easy checking
    travel = {n: 0 for n in range(num_ants)}
    pheromones = {} # every ant has same access; (A, B): strength, ...
    for es in itertools.product(list(nodes), repeat=2):
        e1, e2 = es
        if e1 != e2:
            pheromones[es] = 1.0
    
    # results
    path = {n: [position[n]] for n in range(num_ants)} # path for each 
    cost = {n: 0 for n in range(num_ants)} # cost of each path
    
    # chooses a node to visit
    # based on distance and pheromones
    def choose_node(ant_id):
        
        # scores a node based on pheromones
        def score(node):
            return int(pheromones[position[ant_id], node])
        
        def valid(node):
            return node not in marked[ant_id] and node != position[ant_id]
        
        # new graph, removing invalid nodes
        g = {t: int(score(t)) for t in nodes if valid(t)}
        bag = []
        for t in g:
            for _ in range(g[t]):
                bag.append(t)
        
        # choose randomly from probabilistically generated bag
        return random.choice(bag)

    def run_ant(ant_id):
        # ensure we have nodes to visit
        if len(nodes) == len(marked[ant_id]):
            # return home if not there
            if path[ant_id][0] != path[ant_id][-1]:
                path[ant_id].append(path[ant_id][0])
                cost[ant_id] += adj[position[ant_id], path[ant_id][0]]
            marked_all[ant_id] = True
            return
        # if ant is traveling, only update its travel counter
        if travel[ant_id] > 0:
            travel[ant_id] -= 1
            return
        # choose a node to visit
        to_visit = choose_node(ant_id)
        # visit the node
        marked[ant_id].add(to_visit)
        travel[ant_id] = int(adj[position[ant_id], to_visit])
        pheromones[position[ant_id], to_visit] += pheromone_increase
        # move
        path[ant_id].append(to_visit)
        cost[ant_id] += adj[position[ant_id], to_visit]
        position[ant_id] = to_visit

    def formatted_path(p, first):
        f = p.index(first)
        formatted = p[f]
        for i in range(1, len(p)):
            if p[(i+f)%len(p)] != formatted[-1] and p[(i+f)%len(p)] != formatted[0]:
                formatted += " -> " + p[(i+f)%len(p)]
        return formatted
    
    def dissapate_pheromones():
        # dissapate pheromones
        for trail in pheromones:
            if pheromones[trail] > 1 + pheromone_dissapate:
                pheromones[trail] -= pheromone_dissapate
    
    # send out all ants at once
    def theory1():
        while False in marked_all:
            for ant in range(num_ants):
                run_ant(ant)
            dissapate_pheromones()
    
    # let every ant run by itself
    def theory2():
        for ant in range(num_ants):
            while not marked_all[ant]:
                run_ant(ant)
    
    stopwatch = time.time()
    theory2()
    stopwatch = time.time() - stopwatch
    
    # pick the shortest path that the ants found
    best_ant = min(cost, key=cost.get)
    shortest_path = path[best_ant]

    print(f"Shortest path cost is: {cost[best_ant]}")
    print(f"Took {stopwatch:01f}s")
    print(f"Shortest path:")
    print(formatted_path(shortest_path, "A"))

if __name__ == "__main__":
    main()
