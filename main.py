import os
import math
### --------------------------
# this takes the .mv3d file and returns a dictionary where each key 
# has a list of all coordinates that make up the line
cwd = os.getcwd()

with open(cwd + '/resources/M37-t2.a00.rec.scl3.Spatial-Graph.mv3d', 'r') as file:

    lines = []
    for line in file:
        try:
            point_num = int(line[0])
            lines.append(line.split())
        except ValueError:
            continue

# print(lines)            
coords = {}
for sub in lines:
    key = sub[0]
    if key not in coords: 
        coords[key] = []
    coords[key].append(sub[1:-1])

### -----------------------------


# farthest points algorithm (naive approach) + 3D
def furthest_points(arr):
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


print(furthest_points(coords['0']))