import math

def construct_dict_from_mv3d(file_path):
    """
    Input: File path to mv3d
    Output: Dictionary with all coordinates that make up the line
    """
    with open(file_path, 'r') as file:
        lines = []
        for line in file:
            try:
                point_num = int(line[0])
                lines.append(line.split())
            except ValueError:
                continue

    coords = {}
    for sub in lines:
        key = int(sub[0])
        if key not in coords: 
            coords[key] = []
        app = [float(el) for el in sub[1:-1]]
        coords[key].append(app)

    return coords

def furthest_points(arr):
    """
    Input: List of x,y,z coords.    
    Output: List of the 2 furthest away points' coordinates. I.E endpoints.

    Farthest points algorithm (naive approach) + 3D
    """
    dist = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            p1 = [float(el) for el in arr[i]]
            p2 = [float(el) for el in arr[j]]

            new_dist = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

            if new_dist > dist:
                dist = new_dist
                i1 = i
                i2 = j 
    return [arr[i1], arr[i2]]

def connected_dict_gen(d):
    """
    Input: Dict with the endpoints of each branch
    Output: Dict of each branch number with values corresponding to a list of other branches connected to said branch.
    """

    # Try naive approach (cycle through everything) and if too slow find faster method.
    
    # Cycles through branches and geographically determines if they are connected (Naive)
    connected_dict = {}
    branches = list(d.keys())
    for branch1 in branches:
        connected_points = []
        for branch2 in branches:
            if branch1 != branch2:
                start1, end1 = d[branch1]
                start2, end2 = d[branch2]
                start1 = [float(el) for el in start1]
                start2 = [float(el) for el in start2]
                end1 = [float(el) for el in end1]
                end2 = [float(el) for el in end2]
                if start1 == start2 or start1 == end2 or start2 == start1 or start2 == end1:
                    connected_points.append(branch2)
        connected_dict[branch1] = connected_points

    return connected_dict


def get_endpoints_dictionary(coords):
    """
    Takes in a dictionary with all coordinates of each branch {0: [[x0,y0,z0], [x1, y1. z1], ...],...}
    Returns each key with just endpoints
    """

    furthest_points_coords_dict = {}
    for key in coords.keys():
        points = furthest_points(coords[key])
        if key not in furthest_points_coords_dict:
            furthest_points_coords_dict[key] = points
    return furthest_points_coords_dict

def get_root_geometrically(furthest_points):
    """
    Input: dictionary with the endpoints of each branch
    Output: the branch number that corresponds to the trachea (str)
    """
    # trying minimum z
    min_z = 10000000
    trachea = ''
    for key in furthest_points.keys():
        endpoints = furthest_points[key]
        z1, z2 = float(endpoints[0][2]), float(endpoints[1][2])
        if z1 < min_z or z2 < min_z:
            min_z = min(z1, z2)
            trachea = key
    return trachea


import re 
from anytree import Node, RenderTree

def tree_from_flow_file(flow_file):

    with open(flow_file, 'r') as file:
        links = []
        for line in file:
            if 'root' in line:
                findroot = re.compile('\d+')
                root = int(findroot.findall(line)[0])
                
            elif '-->' in line:
                try:
                    regex = re.compile('\d+\s+-->\s+\d+')
                    match = regex.findall(line)
                    links.append(match[0])
                except IndexError:
                    continue

    leaves = []
    nums = re.compile(r'\d+')
    for el in links:
        n = nums.findall(el)
        if len(n) == 2:
            child, parent = int(n[0]), int(n[1])
            leaves.append((child,parent))
        else:
            raise('Error: Tree not constructed')
    
    

    nodes = [None] * (len(leaves) + 1)  # +1 for root
    nodes[root] = Node(root)
    for el in leaves:
        index = el[0]
        nodes[index] = Node(index)

    leaves.insert(root, None)
    for i in range(len(leaves)):
        if i == 13:
            continue
        else:
            node = nodes[i]
            parent_num = leaves[i][-1]
            parent = nodes[parent_num]
            node.parent = parent
            
    return nodes[root] # return the root node

def visualise(tree):
    for pre, fill, node in RenderTree(tree):
        print("%s%s" % (pre, node.name))


    