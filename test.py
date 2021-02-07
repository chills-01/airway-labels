from anytree import Node, RenderTree

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
    """
    Input: A dictionary from connected_dict_gen() where each branch has a list with all other branches, the head node (trachea)
    Output: A tree with each child (subordinate) branch of each branch in the system
    """
    # directed_airways = {}
    # checked_airways = []
    # current_node = head
    # while len(checked_airways) != len(list(conn_dict.keys())):
    #     children = []
    #     for el in conn_dict[current_node]:
    #         if el not in checked_airways:
    #             children.append(el)
    #     if current_node not in directed_airways.keys():
    #         directed_airways[current_node] = children
    #     checked_airways.append(current_node)
    #     children_left = [child for child in children if child not in checked_airways]
    #     if len(children_left) != 0:
    added = []
    current_node = Node(head)
    while len(added) != len(list(conn_dict.keys())):
        children = [el for el in conn_dict[current_node.name] if el not in added]
        if len(children) != 0:
            current_node.children = children
            
        added.append(current_node)
        




    

            





# Might need these
# class Tree:
#     def __init__(self, cargo, *args):
#         self.cargo = cargo
#         self.children = []
#         for arg in args:
#             self.children.append(arg)
#     def __str__(self):
#         return str(self.cargo)

# def conn_dict_to_network_aux(branch, children):
#     if children is None:
#         return
#     else:
#         branch


        
        


