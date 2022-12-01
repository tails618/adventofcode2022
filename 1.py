# reads in the input data as a txt file, as a list of numbers and empty lines. Prints the output.

# puzzle one

# open data file
input = open("1-data.txt", "r")
data = input.readlines()

# remove '\n' from each item except the final one
for i in range(len(data) - 1):
    data[i] = data[i][:-1]

# sum the items between each blank in the list
lastBlank = 0
sums = []
for i, x in enumerate(data):
    if x == '':
        sums.append(sum(int(i) for i in data[lastBlank:i]))
        lastBlank = i + 1

# find the biggest sum
sums.sort()
print(sums[-1])

#puzzle two

#find the sum of the biggest three sums
print(sums[-1] + sums[-2] + sums[-3])