
def edge_count(adjList):
    """Compute number of edges in a graph from its adjacency list"""
    edges = {}
    for id, neigh in enumerate(adjList):
        for n in neigh:
            edges[max(n, id), min(n, id)] = id

    return len(edges)
