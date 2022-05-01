import random
import itertools
from math import sqrt
import time
import sys

'''
TODO: are these right?
Ant Colony Optimization
Program type: Probabilistic
Time complex: O(AN)
'''

def ACO():
    # constants
    num_ants = 200
    pheromone_initial = 1.0
    pheromone_increase = 10.0
    pheromone_decrease = 0.3
    pheromone_power = 1
    weight_power = 4

    # get input and create graph
    weight = {}
    max_weight = 0
    nodes = set()
    num_nodes = int(input())
    start = input()
    num_edges = int((num_nodes*(num_nodes-1))/2)
    for _ in range(num_edges):
        u, v, w = input().split()
        w = int(w)
        weight[(u, v)] = w
        weight[(v, u)] = w
        if u not in nodes: nodes.add(u)
        if v not in nodes: nodes.add(v)
        if w > max_weight: max_weight = w
    expected_solution = int(input())

    # best values thus far. these get updated as the ants use
    # their pheromones to probablistically construct better paths
    best_path = []
    best_cost = sys.maxsize

    # variables for ants
    position = {n: start for n in range(num_ants)}
    marked = {n: set([start]) for n in range(num_ants)}
    marked_all = [False] * num_ants
    
    # global pheromone counters for each edge
    pheromones = {}
    for edge in itertools.product(list(nodes), repeat=2):
        n1, n2 = edge
        if n1 != n2:
            pheromones[edge] = pheromone_initial
    
    # increases pheromones between two given nodes of `trail`
    def increase_pheromones(trail):
        n1, n2 = trail
        pheromones[n1, n2] += pheromone_increase
    
    # simulates time by dissapating the pheromone level of an edge
    # without having to use a for loop to wait
    def dissapate_pheromones(trail):
        # dissapate the pheromones
        pheromones[trail] += (pheromone_increase - (pheromone_decrease * weight[trail]))
        # ensure that the minimum is there
        if pheromones[trail] < pheromone_initial: pheromones[trail] = pheromone_initial
    
    # takes care of pheromone things as an ant travels on a given
    # trail (aka path or edge)
    def travel(trail):
        increase_pheromones(trail)
        dissapate_pheromones(trail)
    
    # simulates an ant looking at its options and choosing a path
    # randomly, but with some bias towards pheromone-heavy paths
    def choose_node(ant_id):
        # scores a node based on its pheromone level
        def score(node):
            score = (1/weight[position[ant_id], node])**weight_power
            score *= pheromones[position[ant_id], node]**pheromone_power
            return int(score) if score > 1 else 1
        # return True if a node hasn't been visited by this ant
        def valid(node):
            return node not in marked[ant_id] and node != position[ant_id]
        
        bag = [n for n in nodes if valid(n)]
        bag_weight = [score(n) for n in bag]
        return random.choices(bag, bag_weight)[0]
    
    # run an ant. it will choose it's next node and go there, dropping
    # pheromones as it goes and they will dissapate as he travels
    def run_ant(ant_id):
        # ensure we have nodes to visit
        if len(nodes) == len(marked[ant_id]):
            # go home if not there already
            if position[ant_id] != start:
                increase_pheromones((position[ant_id], start))
                position[ant_id] = start
            marked_all[ant_id] = True
            return start
        # choose and visit next node
        next_node = choose_node(ant_id)
        marked[ant_id].add(next_node)
        travel((position[ant_id], next_node))
        position[ant_id] = next_node
        return next_node
    
    # run ants through the graph, timing their efforts. keeps
    # track of the best path so far, and ants will hone down
    # the paths they prefer based on pheromones and randomness
    stopwatch = time.time()
    for ant in range(num_ants):
        path, cost = [start], 0
        while not marked_all[ant]:
            path.append(run_ant(ant))
            cost += weight[path[-2], path[-1]]
        if cost < best_cost:
            best_path = path
            best_cost = cost
    stopwatch = time.time() - stopwatch

    # output solutions
    print(f"Given best path cost: {expected_solution}")
    print(f"Ants found path cost: {best_cost}")
    print(f"Ants' path: {' -> '.join(best_path)}")
    print(f"Ants took {stopwatch:.3f} seconds")

if __name__ == "__main__":
    ACO()
