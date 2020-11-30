"""Samara Trujillo
created: August 17, 2019"""
#Hello sammy
mapXY =[]
map =[]
current =[]
length = 7 #x
height = 7 #y
for x in range (length):
    for y in range (height):
        #x,y,g,h,f,px,py
        map.append ([x, y, 0, 0, 0, 0, 0])
        mapXY.append ([x, y]) 

blocking =[[2,0],[3,0],[4,0],[5,0],[2,2],[3,2],[4,2],[5,2],[2,3],[3,3],[2,4],[4,4],[2,5],[2,6],[4,5],[0,4]]
frontier =[]
visited =[]
virgin = map[:]

def adjustF(coordinates):
    point = coordinates[4]
    return point

def info (coordinates, c):
    #calculate h
    x = coordinates[0] - goal[0] 
    y = goal[1] - coordinates[1] 
    if x <0:
        x *= -1 
    if y<0:
        y *= -1
    h = x + y 
    coordinates[3] = h
    #calculate g
    global current
    global px 
    global py 
    if start not in visited:
        g = 0
        px = 0 
        py = 0
    else:
        g = current[2] + 1 
        coordinates[2] = g
    #calculate f
    f = g + h 
    coordinates[4] = f
    #calculate p
    coordinates[5] = px 
    coordinates[6] = py
    #if to change p and optimize
    map[c] = coordinates 

def optimize(coordinates):
    global current
    g = current[2]
    c = mapXY.index([coordinates[0],coordinates[1]])
    point = map[c]
    v=0
    if point in visited:
        visited.remove(point)
        v=1
    if point in frontier:
        frontier.remove(point)
        #v=0
    g1 = point[2]
    if g+1 < g1:
        #print("previous point:",point)
        info(point,c)
        #print("new point:",map[c])
    if v==1:
        visited.append(map[c])
    else:
        frontier.append(map[c])
        frontier.sort(key=adjustF)

neighbors =[]
"""neighbors:
7     1     5
4  current  3
8     2     6
"""
def neighbor(coordinates):
    neighbors.clear ()
    global px 
    global py
    #neighbor 1
    if (current[0])>-1 and (current[1] + 1) > -1 and (current[0]) < length and (current[1] + 1) <height and[current[0], current[1] + 1] not in blocking:
        if[current[0],current[1] + 1, 0,0, 0, 0, 0] in virgin:
            c =map.index ([current[0], current[1] + 1, 0, 0, 0, 0, 0]) 
            virgin.remove ([current[0], current[1] + 1, 0, 0, 0, 0, 0]) 
            px = 0 
            py =-1 
            info ([current[0], current[1] + 1, 0, 0, 0, 0, 0],c) 
            frontier.append (map[c])
            frontier.sort(key=adjustF)
        else:
            optimize([current[0], current[1] + 1])
        neighbors.append ([current[0], current[1] + 1])
    #neighbor 2
    if (current[0])>-1 and (current[1] - 1) > -1 and (current[0]) < length and (current[1] - 1) < height and[current[0], current[1] - 1] not in blocking:
        if[current[0], current[1] - 1, 0, 0, 0, 0,0] in virgin:
            c = map.index ([current[0], current[1] - 1, 0, 0, 0, 0, 0])
            virgin.remove ([current[0], current[1] - 1, 0, 0, 0, 0, 0])
            px = 0
            py = 1
            info ([current[0], current[1] - 1, 0, 0, 0, 0, 0], c)
            frontier.append (map[c])
            frontier.sort(key=adjustF)
        else:
            optimize([current[0], current[1] - 1])
        neighbors.append ([current[0], current[1] - 1])
    #neighbor 3
    if (current[0] + 1)>-1 and (current[1]) > -1 and (current[0] + 1) < length and (current[1]) < height and[current[0] + 1, current[1]] not in blocking:
        if[current[0] + 1, current[1], 0, 0, 0, 0,0] in virgin:
            c = map.index ([current[0] + 1, current[1], 0, 0, 0, 0, 0])
            virgin.remove ([current[0] + 1, current[1], 0, 0, 0, 0, 0])
            px = -1
            py = 0
            info ([current[0] + 1, current[1], 0, 0, 0, 0, 0], c)
            frontier.append (map[c])
            frontier.sort(key=adjustF)
        else:
            optimize([current[0] + 1, current[1]])
        neighbors.append ([current[0] + 1, current[1]])
    #neighbor 4
    if (current[0] - 1)>-1 and (current[1]) > -1 and (current[0] - 1) < length and (current[1]) < height and[current[0] - 1, current[1]] not in blocking:
        if[current[0] - 1, current[1], 0, 0, 0, 0,0] in virgin:
            c =map.index ([current[0] - 1, current[1], 0, 0, 0, 0,0]) 
            virgin.remove ([current[0] - 1, current[1],0, 0, 0, 0, 0]) 
            px = 1 
            py =0 
            info ([current[0] - 1, current[1], 0, 0, 0, 0, 0],c) 
            frontier.append (map[c])
            frontier.sort(key=adjustF)
        else:
            optimize([current[0] - 1, current[1]])
        neighbors.append ([current[0] - 1, current[1]]) 
    #neighbor 5
    if [current[0],current[1]+1] not in blocking and [current[0]+1,current[1]] not in blocking:
        if (current[0] + 1)>-1 and (current[1] + 1) > -1 and (current[0] + 1) < length and (current[1] + 1) < height and[current[0] + 1, current[1] + 1] not in blocking:
            if[current[0] + 1, current[1] + 1, 0, 0, 0, 0,0] in virgin:
                c =map.index ([current[0] + 1, current[1] + 1, 0, 0, 0, 0,0]) 
                virgin.remove ([current[0] + 1,current[1] + 1, 0, 0, 0,0, 0]) 
                px = -1 
                py =-1
                info ([current[0] + 1, current[1] + 1, 0, 0, 0, 0,0], c) 
                frontier.append (map[c])
                frontier.sort(key=adjustF)
            else:
                optimize([current[0] + 1, current[1] + 1])
            neighbors.append ([current[0] + 1, current[1] + 1])
    #neighbor 6
    if [current[0]+1,current[1]] not in blocking and [current[0],current[1]-1] not in blocking:
        if (current[0] + 1)>-1 and (current[1] - 1) > -1 and (current[0] + 1) < length and (current[1] - 1) < height and[current[0] + 1, current[1] - 1] not in blocking:
            if[current[0] + 1, current[1] - 1, 0, 0, 0, 0,0] in virgin:
                c =map.index ([current[0] + 1, current[1] - 1, 0, 0, 0,0, 0]) 
                virgin.remove ([current[0] + 1,current[1] - 1,0, 0, 0, 0,0]) 
                px = -1 
                py = 1
                info ([current[0] + 1, current[1] - 1, 0, 0, 0,0, 0], c) 
                frontier.append (map[c])
                frontier.sort(key=adjustF)
            else:
                optimize([current[0] + 1, current[1] - 1])
            neighbors.append ([current[0] + 1, current[1] - 1])
    #neighbor 7
    if [current[0]-1,current[1]] not in blocking and [current[0],current[1]+1] not in blocking:
        if (current[0] - 1)>-1 and (current[1] + 1) > -1 and (current[0] - 1) < length and (current[1] + 1) < height and[current[0] - 1, current[1] + 1] not in blocking:
            if[current[0] - 1, current[1] + 1, 0, 0, 0, 0,0] in virgin:
                c =map.index ([current[0] - 1, current[1] + 1, 0, 0,0, 0,0]) 
                virgin.remove ([current[0] - 1,current[1] + 1,0, 0, 0, 0,0]) 
                px = 1 
                py =-1
                info ([current[0] - 1, current[1] + 1, 0, 0,0, 0, 0],c) 
                frontier.append (map[c])
                frontier.sort(key=adjustF)
            else:
                optimize([current[0] - 1,current[1] + 1])
            neighbors.append ([current[0] - 1, current[1] + 1])
    #neighbor 8
    if [current[0]-1,current[1]] not in blocking and [current[0],current[1]-1] not in blocking:
        if (current[0] - 1)>-1 and (current[1] - 1) > -1 and (current[0] - 1) < length and (current[1] - 1) < height and[current[0] - 1, current[1] - 1] not in blocking:
            if[current[0] - 1, current[1] - 1, 0, 0, 0,0, 0] in virgin:
                c =map.index ([current[0] - 1, current[1] - 1,0, 0, 0, 0,0]) 
                virgin.remove ([current[0] -1,current[1] -1, 0, 0, 0,0, 0]) 
                px =1 
                py =1
                info ([current[0] - 1, current[1] - 1, 0,0, 0, 0, 0],c) 
                frontier.append (map[c])
                frontier.sort(key=adjustF)
            else:
                optimize([current[0] - 1,current[1] - 1])
            neighbors.append ([current[0] - 1,current[1] -1])
    neighbors.sort ()
    return neighbors

path = []
def travel ():
    global current
    while current != goal:
        path.append(current)
        #print("current:",current)
        if [current[0], current[1]] == goalxy:
            print("Goal achieved!!")
            print("Path:",path)
            break
        neighbor(current)
        #print(neighbors)
        current = frontier[0]
        if current in frontier:
            frontier.remove(current)
        if current not in visited:
            visited.append(current)

optimalPath = []
def coolPath():
    global current
    optimalPath.append([current[0],current[1]])
    while current != start:
        px = current[5]
        py = current[6]
        c = mapXY.index([current[0] + px, current[1] + py])
        current = map[c]
        optimalPath.append([current[0],current[1]])
    optimalPath.reverse()
    print("Optimal path:",optimalPath)

"""init the program, start and goal"""
start =[0, 0, 0, 0, 0, 0, 0]
goal =[3, 4, 0, 0, 0, 0, 0]
goalxy = [3,4]
c =virgin.index (start) 
virgin.remove (start) 
c =map.index (start) 
info (start, c) 
start =map[c] 
visited.append(start)

"""program"""
c =map.index (start) 
current = map[c]
print ("start", current)
print("goal", goalxy)
travel()
print("visited:",visited)
print("frontier:",frontier)
print("current point",current)
coolPath()