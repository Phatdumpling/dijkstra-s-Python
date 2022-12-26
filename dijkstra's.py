#Assumming V the list if vertices list vertices from 0 to n

V = [0,1,2,3,4,5]
E = [(0, 1), (0, 2), (1, 2), (1, 3), (3, 5), (5, 4), (4, 2), (2, 3), (3, 4)]

Vi_neighbour = []

for x in V:
    Vi_neighbour_index = []
    for y in E:
        if y[0] == x:
            if y[1] in Vi_neighbour_index:
                continue
            Vi_neighbour_index.append(y[1])
        if y[1] == x:
            if y[0] in Vi_neighbour_index:
                continue            
            Vi_neighbour_index.append(y[0])
    Vi_neighbour.append(Vi_neighbour_index)
    
print(Vi_neighbour)

#shortest route from 0 to 4

Tentative_dist = []


#9999999999 will represent infinity
app = [9999999999, []]

for x in V:
    app[1].append(False)

for x in V:
    Tentative_dist.append(app.copy())
    Tentative_dist[x].append(x)

#Tentative_dist = [[0, [True, True, True, True, True, True]], [10000, [False, False, False, False, False, False]], [10000, [False, False, False, False, False, False]], [10000, [False, False, False, False, False, False]], [10000, [False, False, False, False, False, False]], [10000, [False, False, False, False, False, False]]]

current_node = 4 #Tentative_dist.index(min(Tentative_dist))


Tentative_dist[current_node]=[0, []]

for x in V:
    Tentative_dist[current_node][1].append(True)
Tentative_dist[current_node].append(current_node)

print(current_node)

def visit_nodes(current_node1, Dist):
    print("current node is "+ str(current_node1))
    for x in Vi_neighbour[current_node1]:
        print("node "+str(x))
        
        Tentdist = Tentative_dist[current_node1][0]+1
        if Tentative_dist[x][0] >= Tentdist:
            Tentative_dist[x][0] = Tentdist
        Tentative_dist[current_node1][1][x] = True
    
    
    for x in Vi_neighbour[current_node1]:
        Visited = True
        for y in Vi_neighbour[x]:
            print("visiting node "+str(y))
            if Tentative_dist[x][1][y] == False:
                Visited = False
                
        if Visited == False:
            visit_nodes(x, Dist)
    
        
        

visit_nodes(current_node, Tentative_dist[current_node][0])

print(Tentative_dist)

for x in Tentative_dist:
    print("Dist from node " + str(current_node) + " to node " + str(x[2]) + ": "+ str(x[0]))