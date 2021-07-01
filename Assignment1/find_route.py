import sys

#This class will bout our node and will keep track of the previous node,
#the current city, the distance to current city from prev node, and the
#total distance traveled so far
class Node: 
    def __init__(self, prev, current, total, distCity):
        self.prev = prev
        self.total = total
        self.dist = distCity
        self.current = current

#Takes in the hueristic file name and reads file
#to create a dictionary of cities along with hueristic  values
def readHFile(hFile):
    hValues = {}
    f = open(hFile, 'r')
    input = f.readline()

    while("END OF INPUT" not in input):
        input = input.split()
        distance = int(input[1])
        hValues[input[0]] = distance
        input = f.readline()
    
    return hValues

#Performs uninformed search, takes in routes which is a dictionary of each city, each city
#has a smaller dictionary of all the paths it can take and their cost. Will also take origin
#which is the start city and dest which is the destination city.
def uninformedSearch(routes, origin, dest):
    closedSet = []
    fringe = []
    nodesGen = 0
    nodesExp = 0
    nodesPop = 0

    #create the first nodes to go on fringe from origin city
    fringe.append(Node(None, origin, 0, 0))
    nodesGen += 1

    #Check for empty fringe at start of loop, reaching this point means no route was found
    def loop(nodesGen, nodesExp, nodesPop):
        if(len(fringe) == 0 ):
            print("Nodes popped:", nodesPop)
            print("Nodes expanded:", nodesExp)
            print("Nodes generated:", nodesGen)
            print("Distance: Infinity")
            print("Route:\nNone")
            quit()
        
        
        node = fringe.pop()
        nodesPop += 1

        #Pop fringe in to node and check if it contains the destination city, if so
        #we have found the solution
        if(node.current == dest):
            prevCity = node.prev
            path = []
            distCity = []
            totalDist = node.total
            
            while prevCity != None:
                path.append(node.current)
                path.append(prevCity.current)
                distCity.append(node.dist)
                prevCity = prevCity.prev
                node = node.prev 

            print("Nodes popped:", nodesPop)
            print("Nodes expanded:", nodesExp)
            print("Nodes generated", nodesGen)
            print("Distance:", totalDist, "km")
            print("Route:")
                           
            while len(path) != 0:    
                print(path.pop(), "to", path.pop() + ",", distCity.pop(),"km")
                
            return

        #If current city (node.current) is in closedSet, then we have already explored this cities
        #paths, we will skip it and just run next iteration of loop
        if(node.current in closedSet):
            return loop(nodesGen, nodesExp, nodesPop)
        
        #If current city (node.current) was not in closed set this mean we have not explored this
        #cities paths, we will now add the current city to the closed set and add all paths to the 
        #fringe, the fringe is then sorted by total dist traveled so far
        #the node/city with the lowest value will be at the top of the fringe
        else:
            nodesExp += 1
            closedSet.append(node.current)

            for city in routes[node.current]:
                nodesGen += 1
                fringe.append(Node(node, city, routes[node.current][city] + node.total, routes[node.current][city]))

            fringe.sort(key = (lambda x: x.total), reverse = True)

        loop(nodesGen, nodesExp, nodesPop)

    loop(nodesGen, nodesExp, nodesPop)

    return

#Performs informed search, takes in routes which is a dictionary of each city, each city
#has a smaller dictionary of all the paths it can take and their cost. Will also take origin
#which is the start city and dest which is the destination city. In addition it will also take
#huer which is a dictionary of citites along with their hueristic values
def informedSearch(routes, origin, dest, huer):
    closedSet = []
    fringe = []
    nodesGen = 0
    nodesExp = 0
    nodesPop = 0

    #create the first nodes to go on fringe from origin city
    fringe.append(Node(None, origin, 0, 0))
    nodesGen += 1

    #Check for empty fringe at start of loop, reaching this point means no route was found
    def loop(nodesGen, nodesExp, nodesPop, huer):
        if(len(fringe) == 0 ):
            print("Nodes popped:", nodesPop)
            print("Nodes expanded:", nodesExp)
            print("Nodes generated:", nodesGen)
            print("Distance: Infinity")
            print("Route:\nNone")
            quit()
        
        node = fringe.pop()
        nodesPop += 1

        #Pop fringe in to node and check if it contains the destination city, if so
        #we have found the solution
        if(node.current == dest):
            prevCity = node.prev
            path = []
            distCity = []
            totalDist = node.total
            
            while prevCity != None:
                path.append(node.current)
                path.append(prevCity.current)
                distCity.append(node.dist)
                prevCity = prevCity.prev
                node = node.prev 

            print("Nodes popped:", nodesPop)
            print("Nodes expanded:", nodesExp)
            print("Nodes generated:", nodesGen)
            print("Distance:", totalDist, "km")
            print("Route:")                

            while len(path) != 0:    
                print(path.pop(), "to", path.pop() + ",", distCity.pop(),"km")
                
            return

        #If current city (node.current) is in closedSet, then we have already explored this cities
        #paths, we will skip it and just run next iteration of loop
        if(node.current in closedSet):
            return loop(nodesGen, nodesExp, nodesPop, huer)

        #If current city (node.current) was not in closed set this mean we have not explored this
        #cities paths, we will now add the current city to the closed set and add all paths to the 
        #fringe, the fringe is then sorted by total distance traveled so far plus the hueristic value
        #the node/city with the lowest value will be at the top of the fringe
        else:
            nodesExp += 1
            closedSet.append(node.current)

            for city in routes[node.current]:
                nodesGen += 1
                fringe.append(Node(node, city, routes[node.current][city] + node.total, routes[node.current][city]))

            fringe.sort(key = (lambda x: x.total + huer[x.current]), reverse = True)

        loop(nodesGen, nodesExp, nodesPop, huer)

    loop(nodesGen, nodesExp, nodesPop, huer)

    return

#Type checking for the length of command arguemnts, print out correct format when incorrect amount
#of args are entered
if(len(sys.argv) < 4 or len(sys.argv) > 5):
    print("Not enough arguments, please use on of the formats:")
    print("python find_route.py [inputfile.txt] [origin city] [destination city]")
    print("python find_route.py [inputfile.txt] [origin city] [destination city] [heuristicfile.txt]")

#If correct command format is entered we will read file of input in to routes dictionary
else:
    file = open(sys.argv[1], "r")
    input = file.readline()
    origin = sys.argv[2]
    dest = sys.argv[3]
    routes = {}
    
    #This will create a dictionary of routes for each city, each city element in the dictionary
    #will have a smaller dictionary containing all its paths and cost
    while("END OF INPUT" not in input):
        input = input.split()
        routes.setdefault(input[0], {})[input[1]] = int(input[2])
        routes.setdefault(input[1], {})[input[0]] = int(input[2])
        input = file.readline()

    if(origin not in routes):
        print(origin, 'does not exists.')
    if(dest not in routes):
        print(dest, 'does not exist.')
    if(dest not in routes or origin not in routes):
        quit()

    #If a 5th argument was etner it will be the hueristic file so we call informed search and
    #readHFile to create hueristic dictionary
    if(len(sys.argv) == 5):
        hFile = sys.argv[4]
        informedSearch(routes, origin, dest, readHFile(hFile))
    
    #If no 5th argument then we just perform uninformed search
    else:
        uninformedSearch(routes, origin, dest)