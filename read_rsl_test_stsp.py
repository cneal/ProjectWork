def get_stsp_data():
    """
    Creates test graph instance as seen in class
    :return: stspDict
    """

    stspDict = {}  # initialize the dictionary

    #header
    header = {}
    header["NAME"] = "test_instance"
    header['DIMENSION'] = 8

    #nodes
    nodes = {}
    nodes[0] = tuple([float(10), float(50)])
    nodes[1] = tuple([float(10), float(30)])
    nodes[2] = tuple([float(2), float(20)])
    nodes[3] = tuple([float(30), float(50)])
    nodes[4] = tuple([float(40), float(40)])
    nodes[5] = tuple([float(30), float(30)])
    nodes[6] = tuple([float(50), float(30)])
    nodes[7] = tuple([float(20), float(10)])

    edges = set()
    for i in xrange(8):
        for j in xrange(i,8):
            if i==j or (i==0 and j==1) or (i==0 and j==3)  or (i==1 and j==2) or (i==1 and j==7) \
                    or (i==3 and j==4) or (i==4 and j==5)  or (i==4 and j==6):
                continue
            edges.add((i, j, 2))

    edges.add((0, 1, 1))
    edges.add((0, 3, 1))
    edges.add((1, 2, 1))
    edges.add((1, 7, 1))
    edges.add((3, 4, 1))
    edges.add((4, 5, 1))
    edges.add((4, 6, 1))

    #put together the dictionary
    stspDict["header"] = header
    stspDict["nodes"] = nodes
    stspDict["edges"] = edges

    return stspDict
