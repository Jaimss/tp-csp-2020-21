import collections

airports = 'PHX BKK OKC JFK LAX MEX EZE HEL LOS LAP LIM'.split(' ')
routes = [['PHX', 'LAX'],
          ['PHX', 'JFK'],
          ['JFK', 'OKC'],
          ['JFK', 'HEL'],
          ['JFK', 'LOS'],
          ['MEX', 'LAX'],
          ['MEX', 'BKK'],
          ['MEX', 'LIM'],
          ['MEX', 'EZE'],
          ['LIM', 'BKK']]

adjacencyList = {}


def add_node(airport):
    """Add a default"""
    adjacencyList[airport] = []


def add_edge(origin, destination):
    """Add an edge"""
    adjacencyList.get(origin, []).append(destination)


# create the graph
for a in airports:
    add_node(a)

for r in routes:
    add_edge(*r)


def bfs(start, find):
    visited = set()
    queue = [start]
    while len(queue) > 0:
        airport = collections.deque(queue)[0]
        destinations = adjacencyList.get(airport, [])
        for dest in destinations:
            print(dest)
            if dest == find:
                print('found it!')

            if dest not in visited:
                visited.add(dest)
                queue.insert(0, dest)


bfs('PHX', 'BFS')
