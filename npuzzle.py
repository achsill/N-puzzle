import sys

def readFile():
    with open(sys.argv[1]) as f:
        content = f.readlines()
    return content;

def restructureList():
    fileContent = readFile();
    newList = [];
    for x in fileContent:
         newList.append([int(n) for n in x.split()]);
    return newList;

def manathanDistance(grid):
    i = 0;
    for index, item in enumerate(grid):
        newLen = len(item);
        for index2, item2 in enumerate(item):
            if ((item2 != 0) and ((index2 + 1) + (newLen * index)) != item2):
                # print (str(index2 + 1) + '+' + str(newLen) + '*' + str(index)) + " = " + str(item2);
                i+= 1;
            # print(index2, item2)
        # print(index, item)
    return i;

# def replaceGrid(grid):
#     for index, item in enumerate(grid):
#         newLen = len(item);
#         for index2, item2 in enumerate(item):
#             if (item2 == 0):



def changePos(grid):
    for index, item in enumerate(grid):
        for index2, item2 in enumerate(item):
            if (item2 == 0):
                item[index2], item[index2 + 1] = item[index2 + 1], item[index2]
                return grid;
    return grid;

class node:
    def __init__(self, g, h):
        self.g = g;
        self.h = h;
        self.f = g + h;
    def get_f():
        return self.f;

newList = restructureList();
print newList;
x = manathanDistance(newList);
newGrid = changePos(newList);
print newGrid;
y = manathanDistance(newGrid);
print x;
print y;
