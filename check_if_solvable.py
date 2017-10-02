def listBefore(index, finalList):
    newList = [];
    for nbr in finalList:
        if (nbr == index):
            return newList;
        newList.append(nbr);


def iterateAll(nbrList, index, finalList):
    k = 0;
    beforeNbr = listBefore(index, finalList);
    result = 0;
    for nbr in nbrList:
        if (k == 1 and nbr in beforeNbr):
            result+=1;
        if (nbr == index):
            k = 1;
    return result;


def numberOfSwitches(nbrList, finalList):
    result = 0;
    for nbr in nbrList:
        result = result + iterateAll(nbrList, nbr, finalList);
    return  result;

def finalList(finalMatrix):
    finalList = []
    for listM in finalMatrix:
        for nbr in listM:
            finalList.append(nbr);
    finalList.remove(0);
    return finalList;

def checkTheMatrix(matrix, finalMatrix):
    squareMatrix = len(matrix);
    puissanceSquare = squareMatrix*squareMatrix;
    nbrList = [];
    for item in matrix:
        for item2 in item:
            nbrList.append(item2);
    nbrList.remove(0);
    result = numberOfSwitches(nbrList, finalList(finalMatrix));
    if squareMatrix % 2 == 0:
        if result % 2 == 0:
            return 1;
    else:
        for i, l in enumerate(matrix):
            if 0 in l :
                if i + 1% 2 == 0:
                    if result % 2 == 0:
                        return -1;
                    else:
                        return 1;
                else:
                    if result % 2 == 0:
                        return 1;
                    else:
                        return -1;
