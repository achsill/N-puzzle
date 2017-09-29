def finalStateMatrix(originalMatrix):
    squareMatrix = len(originalMatrix);
    w, h = squareMatrix, squareMatrix
    matrix = [[0] * w for i in range(h)]
    puissanceSquare = squareMatrix*squareMatrix;
    top, left, l, k = (0,)*4;
    bot, right = (squareMatrix - 1,)*2;
    i = 1;
    while (i < puissanceSquare):
        while (l <= right):
            if i == puissanceSquare:
                break;
            matrix[k][l] = i;
            if l == right:
                top += 1;
                break ;
            l+=1;
            i+=1;
        while (k <= bot):
            if i == puissanceSquare:
                break;
            matrix[k][l] = i;
            if k == bot:
                right-=1;
                break;
            k+=1;
            i+=1;
        while (l >= left):
            if i == puissanceSquare:
                break;
            matrix[k][l] = i;
            if l == left:
                bot-=1;
                break;
            l-=1;
            i+=1;
        while (k >= top):
            if i == puissanceSquare:
                break;
            matrix[k][l] = i;
            if k == top:
                left += 1;
                break;
            k-=1;
            i+=1;
    return matrix
