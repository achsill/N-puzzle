import argparse
import random
import argparse
import sys

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-m', '--manathan', action="store_true", help="Use the heuristic: Manathan Distance")
group.add_argument('-mt', '--misplaced', action='store_true', help="Use the heuristic: Misplaced Tiles")
group.add_argument('-ml', '--manathanLinear', action='store_true', help="Use the heuristic: Manathan Distance combine with Linear Conflict")
parser.add_argument('-w', '--web', action='store_true', help="Use the heuristic: Manathan Distance combine with Linear Conflict")
parser.add_argument('sourcefile',nargs='*', help='File to parse')
args = parser.parse_args()

def choose_h():
    if args.manathan:
        return 2;
    elif args.misplaced:
        return 3;
    return 1;


def restructureList():
    w = 0;
    if (len(args.sourcefile)) == 0:
        return [random.choice(randomMatrix), 1];
    elif (len(args.sourcefile)) == 1:
        fileContent = readFile();
        newList = [];
        for i, x in enumerate(fileContent):
            if i > 1:
                newList.append([int(n) for n in x.split()]);
        h = choose_h();
        if args.web:
            w = 1;
        return [newList, h, w];
    else:
        print "Please choose just one file.";
        exit(0);

def readFile():
    with open(sys.argv[1]) as f:
        content = f.readlines()
    return content;
#
# def restructureList():
#     if len(sys.argv) < 2:
#         return random.choice(randomMatrix);
#     else:
#         fileContent = readFile();
#     newList = [];
#     for i, x in enumerate(fileContent):
#         if i > 1:
#             newList.append([int(n) for n in x.split()]);
#     return newList;

randomMatrix = [
[[1,6,5],[2,7,4],[0,8,3]],
[[4,8,1],[5,6,3],[7,2,0]],
[[0,5,8],[7,4,1],[3,2,6]],
[[8,4,6],[7,2,5],[1,3,0]],
[[3,1,0],[4,8,5],[2,7,6]]
];
