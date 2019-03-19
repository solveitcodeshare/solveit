import shlex
N, M, K = [int(s) for s in input().split()]

def findPlanet(name,planets):
    for i, p in enumerate(planets):
        if p[0] ==  name: return i
    return 0

def distanceTo(planet1, planet2):
    x = planet1[1] - planet2[1]
    y = planet1[2] - planet2[2]
    z = planet1[3] - planet2[3]
    return (x * x + y * y + z * z) ** 0.5

planetLines = [input() for i in range(N)]
searchPlaneLines =  [input() for i in range(M)]
planets = []
searchPlanets = []

for i, planetLine in enumerate(planetLines):
    p = shlex.split(planetLine,posix=False) #shlex.split handles where the planet name has spaces in it
    planets.append((p[0], float(p[1]), float(p[2]), float(p[3])))

for l in searchPlaneLines: #add the index of the planet in the planets array
    searchPlanets.append(findPlanet(l,planets))

for i in range(len(searchPlanets)):
    planet1 = planets[searchPlanets[i]]
    matrixLine = []
    for j in range(N):
        matrixLine.append(distanceTo(planet1, planets[j]))
    #sort and select store the K closest neighbours: we need the INDEXES not the values, as we need to print the planet names
    sortedIndexes = [i[0] for i in sorted(enumerate(matrixLine), key=lambda x:x[1])][1:K+1]
     #ignore 0 distance in matrixLIne[0] as that is the same planet
    print(planet1[0]+ ": "+", ".join([planets[x][0] for x in sortedIndexes]))
