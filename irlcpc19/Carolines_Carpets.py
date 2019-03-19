D, O, N = [int(s) for s in input().split()]
# D is the dimension of the X * X sqaure carpet shape, with 3**D being th side lenght. D can be up to 50- 3**50 is way too big to traverse directly
# O is the order- the number of iterations the pattern is drawn
# N is the number of data points to check (check if they identify a white of black point)
def find_point(x, y, o, d, sx, sy):
    #if the point is in the middle third of the square, it is white else, recalculate on a smaller square until order O is reached
    sxC = (3**d)//3**o
    #print("{} {} sx {} sy {} o {} d {} sxC {} (sy+sxC) {} ".format(x, y, sx, sy,o, d,sxC,(sy+sxC)))
    if (x >= sx  and x < (sx+sxC)) and (y >= sy and y < (sy+sxC)): return 'w'
    elif o == O: return 'b'
    else:
        #recalculate the next square to draw a white middle third in
        if x <= sx: sx //= 3
        elif x < 2 * sx: sx += sx // 3
        else: sx = (2 * sx) + sx // 3

        if y <= sy: sy //= 3
        elif y < 2 * sy: sy += sy // 3
        else: sy = (2 * sy) + sy // 3
        return find_point(x, y, o+1, d, sx, sy)

query_points = []
sx = (3 ** (D))//3
sy = sx

for i in range(N):
    point = [int(s) for s in input().split()]
    query_points.append(point)
    #if i%(3**D) == 0: print()
    print(find_point(point[0], point[1], 1, D, sx, sy), end=" ")
