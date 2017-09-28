matrix = [
[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]

top = 0;
left = 0;
bot = 2;
right = 2;
l = 0;
k = 0;
i = 1;
while (i < 9):
    while (l <= right):
        if i == 9:
            break;
        matrix[k][l] = i;
        if l == right:
            top += 1;
            break ;
        l+=1;
        i+=1;
    while (k <= bot):
        if i == 9:
            break;
        matrix[k][l] = i;
        if k == bot:
            right-=1;
            break;
        k+=1;
        i+=1;
    while (l >= left):
        if i == 9:
            break;
        matrix[k][l] = i;
        if l == left:
            bot-=1;
            break;
        l-=1;
        i+=1;
    while (k >= top):
        if i == 9:
            break;
        matrix[k][l] = i;
        if k == top:
            left += 1;
            break;
        k-=1;
        i+=1;
print matrix;
