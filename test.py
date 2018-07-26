import operator
l = [[7,9],[4,5],[7,9],[-7,-1],[0,10],[3,10],[3,6],[2,3]]
for x, y in sorted(l, key = operator.itemgetter(1)):
    print x,y