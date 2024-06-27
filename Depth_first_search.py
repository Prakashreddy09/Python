def dfs_graph(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start + "-->", end= "")

    if start in graph:
        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs_graph(graph, neighbor, visited)

    return 

    
if __name__ == '__main__':
    
    # graph = {'A': set(['B', 'C']),
    #      'B': set(['A', 'D', 'E']),
    #      'C': set(['A', 'F']),
    #      'D': set(['B']),
    #      'E': set(['B', 'F']),
    #      'F': set(['C', 'E'])}
    graph = {
        'A': ['B'],
        'C': ['D'],
        'E': ['F'],
        'G': ['H'],
        'I': ['J']
    }
    
    dfs_graph(graph, 'F')
