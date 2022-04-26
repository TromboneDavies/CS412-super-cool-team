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
    num_ants = 500
    pheromone_increase = 1
    pheromone_dissapate = 0.1

    # these will require input
    num_nodes = 5 # however many nodes there are
    G = set() # (x1, y1), (x2, y2), ...
    for x in range(num_nodes): # TODO make this better with itertools
        for y in range(num_nodes):
            G.add((x, y))

    # just ant things #antlife
    marked = {n: set() for n in range(num_ants)} # marked list for each ant (avoiding classes lol)
    marked_all = [False] * num_ants # each ant can set its marked_all to true for easy checking
    position = {n: (random.randint(0, num_nodes-1), random.randint(0, num_nodes-1)) for n in range(num_ants)}
    travel = {n: 0 for n in range(num_ants)}
    pheromones = {} # every ant has same access; ((x1, y1), (x2, y2)): strength, ...
    for es in itertools.product(list(G), repeat=2):
        e1, e2 = es
        if e1 != e2:
            pheromones[es] = 1.0
    
    # results
    path = {n: [] for n in range(num_ants)} # path for each 
    cost = {n: 0 for n in range(num_ants)} # cost of each path

    # calculates distance between two points
    def distance(a, b):
        x1, y1 = a
        x2, y2 = b
        return sqrt((x2-x1)**2 + (y2-y1)**2)
    
    # chooses a node to visit
    # based on distance and pheromones
    def choose_node(ant_id):
        
        # scores a node based on it's distance and pheromones
        def score(node):
            pos = position[ant_id]
            max_dist = distance((0,0), (num_nodes, num_nodes))
            ant_dist = distance(pos, node)
            return  int((max_dist - ant_dist) * pheromones[pos, node])
        
        def valid(node):
            return node not in marked[ant_id] and node != position[ant_id]
        
        # build weighted graph
        g = {t: int(score(t)) for t in G if valid(t)}
        # this is stupid
        bag = []
        for t in g:
            for _ in range(g[t]):
                bag.append(t)
        return random.choice(bag)

    def run_ant(ant_id):
        # ensure we have nodes to visit
        if len(G) == len(marked[ant_id]):
            marked_all[ant_id] = True
            return
        # if ant is traveling, only update it's 
        if travel[ant_id] > 0:
            travel[ant_id] -= 1
            return
        # choose a node to visit
        to_visit = choose_node(ant_id)
        # visit the node
        marked[ant_id].add(to_visit)
        travel[ant_id] = int(distance(position[ant_id], to_visit))
        pheromones[position[ant_id], to_visit] += pheromone_increase
        # move
        path[ant_id].append(to_visit)
        cost[ant_id] += distance(position[ant_id], to_visit)
        position[ant_id] = to_visit

    stopwatch = time.time()
    
    # until all paths traveled
    while False in marked_all:
        # let ants run
        for ant in range(num_ants):
            run_ant(ant)
        # dissapate pheromones
        for trail in pheromones:
            if pheromones[trail] > 1 + pheromone_dissapate:
                pheromones[trail] -= pheromone_dissapate
    
    # pick the shortest path that the ants found
    least_cost = min(cost.values())
    best_ant = [k for k in cost if cost[k] == least_cost][0]
    shortest_path = path[best_ant]

    stopwatch = time.time() - stopwatch

    print(f"Shortest path cost is: {least_cost}")
    print(f"Took {stopwatch:01f}s")
    # print(f"Shortest path:")
    # print(shortest_path[0], end="")
    # for n in range(1, len(shortest_path)):
    #     print(f" -> {shortest_path[n]}", end="")
    # print()

if __name__ == "__main__":
    main()
