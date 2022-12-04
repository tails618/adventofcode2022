# day 4
# puzzle one

# open data
data = open('4-data.txt','r').readlines()

n = 0
for l in data:
    comma = l.find(',')
    dash1 = l.find('-')
    dash2 = l[comma + 1:].find('-') + len(l[:comma + 1])
    id1 = list(range(int(l[:dash1]), int(l[dash1 + 1:comma]) + 1))
    id2 = list(range(int(l[comma + 1:dash2]), int(l[dash2 + 1:]) + 1))
    if all(i in id1 for i in id2) or all(i in id2 for i in id1):
        n += 1

print(n)

# puzzle two

n = 0
for l in data:
    comma = l.find(',')
    dash1 = l.find('-')
    dash2 = l[comma + 1:].find('-') + len(l[:comma + 1])
    id1 = list(range(int(l[:dash1]), int(l[dash1 + 1:comma]) + 1))
    id2 = list(range(int(l[comma + 1:dash2]), int(l[dash2 + 1:]) + 1))
    if any(i in id1 for i in id2):
        n += 1

print(n)