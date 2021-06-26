import sys

def uninformedSearch():
    
    return

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
        quit()
    if(dest not in routes):
        print(dest, 'does not exist.')
        quit()

    if(len(sys.argv) == 5):
        hFile = sys.argv[4]
        informedSearch(routes, origin, dest, hFile)
    else:
        uninformedSearch(routes, origin, dest)
