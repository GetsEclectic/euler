import networkx
import EulerUtilities


def getNumLinesInFile(fileName):
    with open(fileName) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def buildTriangleGraphFromTxt(txtFileName):
    triangleTree = networkx.DiGraph()

    with open(txtFileName) as triangleInputFile:
        weightNumber = 0
        sourceNodeNumber = 0
        triangleSeed = 0
        nextTriangleNumber = EulerUtilities.generateTriangle(triangleSeed)
        for line in triangleInputFile:
            splitLine = line.split()

            for edgeWeight in splitLine:
                if weightNumber == nextTriangleNumber:
                    sourceNodeNumber += 1
                    triangleSeed += 1
                    nextTriangleNumber = EulerUtilities.generateTriangle(triangleSeed)

                triangleTree.add_edge(weightNumber, sourceNodeNumber, {'capacity': int(edgeWeight)})
                sourceNodeNumber += 1
                triangleTree.add_edge(weightNumber, sourceNodeNumber, {'capacity': int(edgeWeight)})

                weightNumber += 1

    return triangleTree, EulerUtilities.generateTriangle(triangleSeed)

triangleTree, triangleNumber = buildTriangleGraphFromTxt("/Users/203369/Downloads/triangle.txt")
# print triangleTree.number_of_nodes()
# print triangleNumber

for x in xrange(triangleNumber - 1, -1, -1):
    neighbors =  triangleTree.neighbors(x)
    maxCapacity = 0
    for neighbor in neighbors:
        capacity = triangleTree[x][neighbor]['capacity']
        if 'capacity' in triangleTree[neighbor]:
            capacity += triangleTree[neighbor]['capacity']
        if capacity > maxCapacity:
            maxCapacity = capacity

    triangleTree[x]['capacity'] = maxCapacity

print triangleTree[0]



# leaves = (n for n, d in triangleTree.in_degree_iter() if d == 0)
#
# for leaf in leaves:
#     leafMaxFlow = networkx.max_flow(triangleTree, leaf, 0)
#     print leafMaxFlow
#     if leafMaxFlow > treeMaxFlow:
#         treeMaxFlow = leafMaxFlow
#
# print treeMaxFlow
# print EulerUtilities.generateTriangle(2)