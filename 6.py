# day 6
# puzzles one and two

# open data
data = open('6-data.txt','r').readlines()[0]

def findMarker(length):
    for i in range(length - 1, len(data)):
        l = []
        for j in range(length):
            l.append(data[i - j])
        if len(l) == len(set(l)):
            return(i + 1)

#puzzle one
print(findMarker(4))

#puzzle two
print(findMarker(14))