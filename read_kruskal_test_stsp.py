def get_stsp_data():
    """
    Creates test graph instance as seen in class
    :return: stspDict
    """

    stspDict = {}  # initialize the dictionary

    #header
    header = {}
    header["NAME"] = "test_instance"
    header['DIMENSION'] = 9

    #nodes
    nodes = {}
    nodes[0] = tuple([float(10), float(20)])
    nodes[1] = tuple([float(20), float(30)])
    nodes[2] = tuple([float(40), float(30)])
    nodes[3] = tuple([float(50), float(30)])
    nodes[4] = tuple([float(60), float(20)])
    nodes[5] = tuple([float(50), float(10)])
    nodes[6] = tuple([float(40), float(10)])
    nodes[7] = tuple([float(20), float(10)])
    nodes[8] = tuple([float(30), float(20)])

    #edges
    edges = set()
    edge1 = (0, 1, 4)
    edge2 = (0, 7, 8)
    edge3 = (1, 7, 11)
    edge4 = (1, 2, 8)
    edge5 = (2, 8, 2)
    edge6 = (2, 5, 4)
    edge7 = (2, 3, 7)
    edge8 = (3, 5, 14)
    edge9 = (3, 4, 9)
    edge10 = (4, 5, 10)
    edge11 = (5, 6, 2)
    edge12 = (6, 8, 6)
    edge13 = (6, 7, 1)
    edge14 = (7, 8, 7)

    edges.add(edge1)
    edges.add(edge2)
    edges.add(edge3)
    edges.add(edge4)
    edges.add(edge5)
    edges.add(edge6)
    edges.add(edge7)
    edges.add(edge8)
    edges.add(edge9)
    edges.add(edge10)
    edges.add(edge11)
    edges.add(edge12)
    edges.add(edge13)
    edges.add(edge14)

    #put together the dictionary
    stspDict["header"] = header
    stspDict["nodes"] = nodes
    stspDict["edges"] = edges

    return stspDict
