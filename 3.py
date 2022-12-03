# day 3
# puzzle one

# open data file
data = open("3-data.txt", "r").readlines()

# make a list of the element that appears in both halves of each line
matches = []
for x in data:
    half = int(len(x)/2)
    for char in x[:half]:
        if char in x[half:]:
            matches.append(char)
            break

# convert each item in matches to a score
def toScore(l):
    scores = []
    for i in l:
        scores.append(ord(i) - 96 if i.islower() else ord(i) - 38)
    return scores

print(sum(toScore(matches)))

# puzzle two

# make a list of the element that appears in all three items
badgeMatches = []
for i in range(0, len(data), 3):
    for x in data[i]:
        if x in data[i+1] and x in data[i+2]:
            badgeMatches.append(x)
            break

print(sum(toScore(badgeMatches)))