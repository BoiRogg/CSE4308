Rogelio Chapa  
1000794793
Python 3.9.5 (Windows 10)
Did not test with omega

How to run code:
python find_route.py [inputfile.txt] [origin city] [destination city]

When using hueristic file use:
python find_route.py [inputfile.txt] [origin city] [destination city] [heuristicfile.txt] 

* These commands must be typed from the same directory
as the find_route.py file, input and hueristic file must also be in the
same directory as the find_route.py file

Structure:

class Nodes:

This is a class that will keep track of nodes(cities), it will hold
the nodes current city, previous node(from prev city), distance to 
current city from previous node and total distance it has traveled so 
far from origin

def readHFile(hFile):

This will open a read hueristic file and return a dictonary
of the cities along with their hueristic values

def uninformedSearch(routes, origin, dest):

This will permform the uninformed search. It will take in the 
routes which is a dictionary of all the cities, each city will have a 
smaller dictionary within it for each possible path along with the cost.
It will also take in the origin (start city) and dest (final destination)

def informedSearch(routes, origin, dest, huer):

Similar to uninformed search, this will perform an informed search.
It will also take in routes which is a dictionary of cities and all their
possible paths and costs. Origin and dest are the start and end city. 
The huer will be the dictionary of hueristic values for each city

main area:

This is where the code will start and make all the calls. It will do
the type checking and make sure the run command is called with 
enough arguments. It will also open the input file containing all
the city map and create the routes dictionary.