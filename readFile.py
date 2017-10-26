import argparse
import random
import argparse
import sys

# parser = argparse.ArgumentParser()
# parser.add_argument('-m', '--manathan', dest='check_cycles', default=False,
#                             action='store_const', const=False, help="Use the heuristic: Manathan Distance")
# parser.add_argument('-l', '--linear', dest='check_cycles', default=False,
#                             action='store_const', const=False, help="Use the heuristic: Linear Conflict")
# parser.add_argument('-mt', '--misplaced', dest='check_cycles', default=False,
#                             action='store_const', const=False, help="Use the heuristic: Misplaced Tiles")
# parser.add_argument('-ml', '--manathanLinear', dest='check_cycles', default=False,
#                             action='store_const', const=False, help="Use the heuristic: Manathan Distance combine with Linear Conflict")
# parser.add_argument('sourcefile',nargs='*', help='File to parse')
# args = parser.parse_args()
# print args.sourcefile;
def readFile():
    with open(sys.argv[1]) as f:
        content = f.readlines()
    return content;

def restructureList():
    if len(sys.argv) < 2:
        return random.choice(randomMatrix);
    else:
        fileContent = readFile();
    newList = [];
    for i, x in enumerate(fileContent):
        if i > 1:
            newList.append([int(n) for n in x.split()]);
    return newList;

randomMatrix = [
[[1,6,5],[2,7,4],[0,8,3]],
[[4,8,1],[5,6,3],[7,2,0]],
[[0,5,8],[7,4,1],[3,2,6]],
[[8,4,6],[7,2,5],[1,3,0]],
[[3,1,0],[4,8,5],[2,7,6]]
];
