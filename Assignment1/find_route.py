import sys

class Node: 
    def __init__(self, prev, current, total, distCity):
        self.prev = prev
        self.total = total + distCity
        self.current = current

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

def uninformedSearch(routes, origin, dest):
    closedSet = []
    fringe = []
    nodesGen = 0
    nodesExp = 0
    nodesPop = 0

    fringe.append(Node(None, origin, 0, 0))
    nodesGen += 1

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

        if(node.current == dest):
            nodesExp -= 1
            prevCity = node.prev
            path = []
            distCity = []
            totalDist = 0
            
            while prevCity != None:
                path.append(node.current)
                path.append(prevCity.current)
                distCity.append(node.total)
                totalDist += node.total
                prevCity = prevCity.prev
                node = node.prev 

            print("Nodes popped:", nodesPop)
            print("Nodes Expanded:", nodesExp)
            print("Nodes generated", nodesGen)
            print("Distance:", totalDist, "km")
            print("Route:")
                           

            while len(path) != 0:    
                print(path.pop(), "to", path.pop() + ",", distCity.pop(),"km")
                
            return

        if(node.current in closedSet):
            return loop(nodesGen, nodesExp, nodesPop)

        else:
            nodesExp += 1
            closedSet.append(node.current)

            for city in routes[node.current]:
                nodesGen += 1
                fringe.append(Node(node, city, 0, routes[node.current][city]))

            fringe.sort(key = (lambda x: x.total), reverse = True)

        loop(nodesGen, nodesExp, nodesPop)

    loop(nodesGen, nodesExp, nodesPop)

    return

def informedSearch(routes, origin, dest, huer):
    closedSet = []
    fringe = []
    nodesGen = 0
    nodesExp = 0
    nodesPop = 0

    fringe.append(Node(None, origin, 0, 0))
    nodesGen += 1

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

        if(node.current == dest):
            prevCity = node.prev
            path = []
            distCity = []
            totalDist = 0
            
            while prevCity != None:
                path.append(node.current)
                path.append(prevCity.current)
                distCity.append(node.total)
                totalDist += node.total
                prevCity = prevCity.prev
                node = node.prev 

            print("Nodes popped:", nodesPop)
            print("Nodes Expanded:", nodesExp)
            print("Nodes generated:", nodesGen)
            print("Distance:", totalDist, "km")
            print("Route:")                

            while len(path) != 0:    
                print(path.pop(), "to", path.pop() + ",", distCity.pop(),"km")
                
            return

        if(node.current in closedSet):
            return loop(nodesGen, nodesExp, nodesPop, huer)

        else:
            nodesExp += 1
            closedSet.append(node.current)

            for city in routes[node.current]:
                nodesGen += 1
                fringe.append(Node(node, city, 0, routes[node.current][city]))

            fringe.sort(key = (lambda x: x.total + huer[x.current]), reverse = True)

        loop(nodesGen, nodesExp, nodesPop, huer)

    loop(nodesGen, nodesExp, nodesPop, huer)

    return

if(len(sys.argv) < 4 or len(sys.argv) > 5):
    print("Not enough arguments, please use on of the formats:")
    print("python find_route.py [inputfile.txt] [origin city] [destination city]")
    print("python find_route.py [inputfile.txt] [origin city] [destination city] [heuristicfile.txt]")
else:
    file = open(sys.argv[1], "r")
    input = file.readline()
    origin = sys.argv[2]
    dest = sys.argv[3]
    routes = {}
    
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

    if(len(sys.argv) == 5):
        hFile = sys.argv[4]
        informedSearch(routes, origin, dest, readHFile(hFile))

    else:
        uninformedSearch(routes, origin, dest)