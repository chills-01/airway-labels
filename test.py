

test_dict = {'0': [[1, 0, 0],[1, 2, 0]], 
             '1': [[1, 2, 0],[2, 1, 0]],
             '2': [[1, 0, 0],[1, -1, 0]],
             '3': [[1, 2, 0],[2, 3, 0]],
             '4': [[0, 0, 0],[1, 0, 0]]
            }

conn_dict = {'0': ['1', '2', '3', '4'], '1': ['0', '3'], '2': ['0', '4'], '3': ['0', '1'], '4': ['0', '2']}


def connected_dict_gen(d):
    """
    Input: Dict with the endpoints of each branch
    Output: Dict of each branch number with values corresponding to a list of other branches connected to said branch.
    """

    # Try naive approach (cycle through everything) and if too slow find faster method.
    
    # Cycles through bracnhes and geographically determiebns if they are connected (Naive)
    connected_dict = {}
    branches = list(d.keys())
    for branch1 in branches:
        connected_points = []
        for branch2 in branches:
            if branch1 != branch2:
                start1, end1 = d[branch1]
                start2, end2 = d[branch2]
                if start1 == start2 or start1 == end2 or start2 == start1 or start2 == end1:
                    connected_points.append(branch2)
        connected_dict[branch1] = connected_points

    return connected_dict

#print(connected_dict_gen(test_dict, '4'))

def conn_dict_to_network(conn_dict, head):
    pass

        
        


