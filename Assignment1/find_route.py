import sys

def extract(route, path):
    if(not route): 
        return path
    if(len(route) == 1):
        path.append(route[0])
    else:
        path.append(route[1])
        route = route[0]
        extract(route, path)
        return path

def uninformedSearch(routes, origin, dest):
    result = UCS({origin: [0,[origin]]}, {}, routes, origin, dest, [0, 0], [origin])

    if(result[0][0] > -1):
        print('Nodes expanded:' + str(result[1][0]) + '\nNodes generated:' + str(result[1][1]))
        print('Distance:' + str(result[0][0]) + 'km')
        print('Route:')
        route = result[0][1]
        route = extract(route, [])
        if(route):
            route.reverse()
            for i in range(len(route)-1):
                print(route[i], 'to', route[i+1], routes[route[i]][route[i+1]], 'km')
        else:
            print(origin, 'to', str(dest) + ',', result[0][0], 'km')

    else:
        print('Nodes expanded:' + str(result[1][0]) + '\nNodes generated:' + str(result[1][1]))
        print('Distance: Infinity')
        print('Route:\nNone')

    return

def UCS(fringe, visited, routes, origin, dest, nodes, path):
    
    if(not fringe):
        return [[-1, nodes]]

    else:
        nodes[0] = nodes[0] + 1 
        closest = min(fringe, key = (lambda k:fringe[k][0]))

        if(dest == closest):
            return [fringe[closest], nodes]
          
        currPath = fringe.pop(closest)
        visited[closest] = currPath

        for city in routes[closest]:
            nodes[1] = nodes[1] + 1

            if(city not in routes or city not in fringe):
                fringe[city] = [currPath[0] + routes[closest][city], [currPath[1], city]]

            elif(city in fringe or city in visited):

                if(city in visited and visited[city][0] > currPath[0] + routes[closest][city]):
                    visited[city] = [currPath[0] + routes[closest][city], [currPath[1], city]]
                    fringe[city] = visited.pop(city)

                elif(city in fringe and fringe[city][0] > currPath[0] + routes[closest][city]):
                    fringe[city] = [currPath[0] + routes[closest][city], [currPath[1], city]]

    return UCS(fringe, visited, routes, origin, dest, nodes, path)

def informedSearch():
    
    return

format = ("Not enough arguments.\nPlease use format:\n" 
"python find_route.py [inputfile.txt] [origin city] [destination city]\n"
"   or\n"
"python find_route.py [inputfile.txt] [origin city] [destination city] [heuristicfile.txt] \n")

if(len(sys.argv) < 4 or len(sys.argv) > 5):
    print(format)
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
        informedSearch(routes, origin, dest, hFile)
    else:
        uninformedSearch(routes, origin, dest)