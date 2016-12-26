
def edge_count(adjList):
    """Compute number of edges in a graph from its adjacency list"""
    edges = {}
    for id, neigh in enumerate(adjList):
        for n in neigh:
            edges[max(n, id), min(n, id)] = id

    return len(edges)


def valid_path(adjList, path):
    """
    Check path goes from node to node following existing edges.

    Arguments:
        AdjList (list): Graph adjacency list
        path (list): The list of node ids that define the path

    Returns:
        Bool: True valid, false otherwise
    """
    max_node = len(adjList)-1

    # Check all nodes with in 0-max_node
    for n in path:
        assert isinstance(n, int)
        assert 0<=n<=max_node

    if len(path) == 1:
        return

    # Check all path edges exist
    prev = path[0]
    for n in path[1:]:
        if n not in adjList[prev]:
            return False
        else:
            prev=n

    return True


def draw_graph(adjList, coordList, path=None, markersize=4):    
    """
    Draw graph using matplotlib
    """
    import matplotlib.patches as patches
    from matplotlib.path import Path
    import pylab as pl


    fig, ax = pl.subplots()

    def draw_segment(ax, start, end, color='green', lw=0.5):
        verts = [start, end]
        codes = [Path.MOVETO, Path.LINETO]
        path = Path(verts, codes)
        ax.add_patch(patches.PathPatch(path, color=color, lw=lw))


    # Draw segments
    for id in range(len(adjList)):
        for neigh in adjList[id]:
            draw_segment(ax, coordList[id], coordList[neigh])

    # Draw points
    x = [coord[0] for id, coord in enumerate(coordList)]
    y = [coord[1] for id, coord in enumerate(coordList)]
    pl.plot(x, y, 'go', markersize=markersize)

    # Draw path
    if path is not None and valid_path(adjList, path):

        # Draw path edges
        prev = path[0]
        for n in path[1:]:
            draw_segment(ax, coordList[prev], coordList[n], color='red', lw=2.0)
            prev=n

        # Draw path nodes
        x = [coordList[node][0] for node in path]
        y = [coordList[node][1] for node in path]
        pl.plot(x, y, 'ro', markersize=markersize)

        
    pl.axis('equal')
    pl.show()



