def dfs_min_path_recursive(graph, start, goal, path=[], shortest_path=None):
    path = path + [start]
    print(path)
    
    if start == goal:
        return path
    
    if start not in graph:
        return None
    
    for node in graph[start]:
        if node not in path:
            new_path = dfs_min_path_recursive(graph, node, goal, path, shortest_path)
            if new_path:
                if shortest_path is None or len(new_path) < len(shortest_path):
                    shortest_path = new_path
    
    return shortest_path

if __name__ == '__main__':
    graph = {
        # 'A': ['B'],
        # 'B': ['A', 'C'],
        # 'C': ['B'],
        # 'D': ['E'],
        # 'E': ['D', 'F'],
        # 'F': ['E'],
        # 'G': ['H'],
        # 'H': ['G', 'I'],
        # 'I': ['H']
        'A': ['B'],
        'C': ['D'],
        'E': ['F'],
        'G': ['H'],
        'I': ['J']
        }
    start = 'A'
    goal = 'J'
    path = dfs_min_path_recursive(graph, start, goal)
    if path:
        print(f"The path from {start} to {goal} is {path}")
    else:
        print(f"There is not path from {start} to {goal}")