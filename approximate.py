import random
import itertools
from math import sqrt
import time

'''
TODO: are these right?
Ant Colony Optimization
Program type: Probabilistic
Time complex: O(A*log(E))?
'''

def ACO():
    # constants
    num_ants = 500
    pheromone_initial = 1.0
    pheromone_increase = 8.0
    pheromone_decrease = 0.4

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
    
    # greedily chooses a path based on pheromone levels, NOT edge
    # weights. essentially chooses most traveled tour. returns a
    # tuple of the path and the cost, respectively
    def greedy_path():
        path = [start]
        cost = 0
        while len(nodes) > len(path):
            # choose the next node
            strongest_ph = 0
            best_node = None
            for node in nodes:
                # if node if valid
                if node != path[-1] and node not in path:
                    # if node is better
                    if pheromones[path[-1], node] > strongest_ph:
                        strongest_ph = pheromones[path[-1], node]
                        best_node = node
            # add pheromoniest node
            cost += weight[path[-1], best_node]
            path.append(best_node)
        cost += weight[path[-1], start]
        path.append(start)
        return path, cost
    
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
            score = (max_weight - weight[position[ant_id], node])
            score += pheromones[position[ant_id], node]
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
            return
        # choose and visit next node
        to_visit = choose_node(ant_id)
        marked[ant_id].add(to_visit)
        travel((position[ant_id], to_visit))
        position[ant_id] = to_visit
    
    # run ants through the graph, timing their efforts
    stopwatch = time.time()
    while False in marked_all:
        for ant in range(num_ants):
            run_ant(ant)
    stopwatch = time.time() - stopwatch

    # follow the pheromones to get ants' path
    best_path, best_cost = greedy_path()

    # output solutions
    print(f"Given best path cost: {expected_solution}")
    print(f"Ants found path cost: {best_cost}")
    print(f"Ants' path: {' -> '.join(best_path)}")
    print(f"Ants took {stopwatch:.3f} seconds")

if __name__ == "__main__":
    ACO()
