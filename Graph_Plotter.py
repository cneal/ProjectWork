import numpy as np

def plot_graph(instance_dictionary):
    """
    Plot the graph represented by `nodes` and `edges` using Matplotlib.
    """

    nodes = instance_dictionary["nodes"]
    edges = instance_dictionary["edges"]

    import matplotlib.pyplot as plt
    from matplotlib.collections import LineCollection

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Plot nodes.
    x = [node[0] for node in nodes.values()]
    y = [node[1] for node in nodes.values()]

    # Plot edges.
    edge_pos = np.asarray([(nodes[e[0]], nodes[e[1]]) for e in edges])
    edge_collection = LineCollection(edge_pos, linewidth=1.5, antialiased=True,
                                     colors=(.8, .8, .8), alpha=.75, zorder=0)
    ax.add_collection(edge_collection)
    ax.scatter(x, y, s=35, c='r', antialiased=True, alpha=.75, zorder=1)
    ax.set_xlim(min(x) - 10, max(x) + 10)
    ax.set_ylim(min(y) - 10, max(y) + 10)

    plt.show()

def plot_over_full_graph(instance_dictionary, min_graph_dict, start_node=-1):

    # Original Instance
    nodes = instance_dictionary["nodes"]
    edges = instance_dictionary["edges"]

    import matplotlib.pyplot as plt
    from matplotlib.collections import LineCollection

    fig = plt.figure()
    ax = fig.add_subplot(111)

    x = [node[0] for node in nodes.values()]
    y = [node[1] for node in nodes.values()]

    edge_pos = np.asarray([(nodes[e[0]], nodes[e[1]]) for e in edges])
    edge_collection = LineCollection(edge_pos, linewidth=1.5, antialiased=True,
                                     colors=(.8, .8, .8), alpha=.75, zorder=0)
    ax.add_collection(edge_collection)
    ax.scatter(x, y, s=35, c='r', antialiased=True, alpha=.75, zorder=1)

    #Min span tree instance
    nodes_min = min_graph_dict["nodes"]
    edges_min = min_graph_dict["edges"]

    x_min = [node[0] for node in nodes_min.values()]
    y_min = [node[1] for node in nodes_min.values()]

    edge_pos = np.asarray([(nodes_min[e[0]], nodes_min[e[1]]) for e in edges_min])
    edge_collection_min = LineCollection(edge_pos, linewidth=1.5, antialiased=True, colors='b', alpha=.75, zorder=0)
    ax.add_collection(edge_collection_min)
    ax.scatter(x_min, y_min, s=35, c='r', antialiased=True, alpha=.75, zorder=1)

    ax.set_xlim(min(x) - 10, max(x) + 10)
    ax.set_ylim(min(y) - 10, max(y) + 10)

    #highlight the start node if it was passed
    if start_node != -1:
        startX = [x[start_node]]
        startY = [y[start_node]]
        ax.scatter(startX, startY, s=35, c='#FFFF11', antialiased=True, alpha=.75, zorder=1)

    plt.show()


