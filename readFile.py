import argparse
import random
import argparse
import sys
import os.path

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-m', '--manathan', action="store_true", help="Use the heuristic: Manathan Distance (Only for 8Puzzle)")
group.add_argument('-mt', '--misplaced', action='store_true', help="Use the heuristic: Misplaced Tiles (Only for 8Puzzle)")
group.add_argument('-ml', '--manathanLinear', action='store_true', help="Use the heuristic: Manathan Distance combine with Linear Conflict (Default Heuristic)")
parser.add_argument('-w', '--web', action='store_true', help="Print result for web version")
parser.add_argument('-iw', '--iweb', action='store_true', help="Print initial puzzle for web version")
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
        return [random.choice(randomMatrix), 1, 0];
    elif (len(args.sourcefile)) == 1:
        fileContent = readFile();
        newList = [];
        for i, x in enumerate(fileContent):
                newList.append([int(n) for n in x.split() if n.isdigit()]);
        newList = [x for x in newList if x];
        newList = formatMatrix(newList);
        h = choose_h();
        if args.web:
            w = 1;
        if len(newList) > 3 and h != 1:
            print "You can not use other heuristic than manathanLinear for puzzle with more than 8 tiles due to optizimation needs.\n-h for more informations."
            exit(0);
        return [newList, h, w];
    else:
        print "Please choose just one file.";
        exit(0);

def readFile():
    if os.path.exists(args.sourcefile[0]):
        with open(args.sourcefile[0]) as f:
            content = f.readlines()
        return content;
    else:
        print "file don't exist."
        exit(0);

def formatMatrix(matrix):
    toDel = [];
    mLen = None;
    for k in matrix:
        if mLen == None:
            mLen = len(k);
        if len(k) > mLen:
            mLen = len(k)

    for i, m in enumerate(matrix):
        if len(m) != mLen:
            toDel.append(i);
    result = [i for j, i in enumerate(matrix) if j not in toDel]
    return result;

randomMatrix = [
[[1,6,5],[2,7,4],[0,8,3]],
[[4,8,1],[5,6,3],[7,2,0]],
[[0,5,8],[7,4,1],[3,2,6]],
[[8,4,6],[7,2,5],[1,3,0]],
[[3,1,0],[4,8,5],[2,7,6]]
];
