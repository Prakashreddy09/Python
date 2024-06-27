def dfs_graph(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    if start in graph:
        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs_graph(graph, neighbor, visited)

    return visited



def connected_components(graph, visited=set()):
    count  = 0
    for i in graph:
        if i not in visited:
            count += 1
            visited = dfs_graph(graph, i, visited)
    return count
    
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
    
    print(connected_components(graph))