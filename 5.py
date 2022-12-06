# day 5
# puzzle one

# open data
dataTwo = data = open('5-data.txt','r').readlines()

# initialize lists of crates
crates = []
cratesTwo = []
a = 0
while '[' in data[a]:
    a += 1
for i in range(int(data[a][-3])):
    crates.append([])
    cratesTwo.append([])

# populate lists of crates
max = int(data[a][-3])
for i in data[a - 1::-1]:
    c = 0
    for j in range(1, (4 * max - 1) + 1, 4):
        if i[j] != ' ':
            crates[c].append(i[j])
            cratesTwo[c].append(i[j])
        c += 1

for i in data[a + 2:]:
    numIdx = int(i[i.find('e') + 2:i.find('f')-1])
    fromIdx = int(i[i.find('om') + 3:i.find('t')-1]) - 1
    toIdx = int(i[i.find('to') + 3:]) - 1
    for i in range(numIdx):
        crates[toIdx].append(crates[fromIdx].pop())

print(*[i[-1] for i in crates])

# puzzle two

for i in dataTwo[a + 2:]:
    numIdx = int(i[i.find('e') + 2:i.find('f')-1])
    fromIdx = int(i[i.find('om') + 3:i.find('t')-1]) - 1
    toIdx = int(i[i.find('to') + 3:]) - 1
    cratesTwo[toIdx] += cratesTwo[fromIdx][-numIdx:]
    for i in range(numIdx):
        cratesTwo[fromIdx].pop()

print(*[i[-1] for i in cratesTwo])