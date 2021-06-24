from collections import Counter

import csv
with open('HeightWeight.csv',newline = '') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)

weightData = []

for i in range(len(data)):
    weight = data[i][2]
    weightData.append(float(weight))


mean = 0
sum = 0
length = len(weightData)

for value in weightData:
    sum += value

mean = sum/length

median = 0
middle = length//2

weightData.sort()

if length % 2 == 1:
    median = weightData[middle]
    # print(median)
    # print('ODD')
else:
    median = (weightData[middle] + weightData[middle-1])/2
    # print(median)
    # print('EVEN')

#counting the data and creating range of data given in csv file
weightCounter = Counter(weightData)
weightDataRange = {'50-60':0,'60-70':0,'70-80':0,'80-90':0}

#items in the data
items = weightCounter.items()

#Adding the occurence the appropriate range
for weight,occurence in items:
    if 50 < float(weight) < 60:
        weightDataRange['50-60'] += occurence
    elif 60 < float(weight) < 70:
        weightDataRange['60-70'] += occurence
    elif 70 < float(weight) < 80:
        weightDataRange['70-80'] += occurence
    elif 80 < float(weight) < 90:
        weightDataRange['80-90'] += occurence

# print(weightDataRange)

modeRange = 0
modeOcurrence = 0

"""In the items, the range with the highest value is stored in modeRange
    modeOccurence is given value of occurence so that the if condition becomes false
    mode = the addition of the highest occuring values/2
"""
for range,occurence in weightDataRange.items():
    if occurence > modeOcurrence:
        modeRange = [int(range.split('-')[0]),int(range.split('-')[1])]
        modeOcurrence = occurence
        # print(modeRange)
        # print(modeOcurrence)

mode = modeRange[0] + modeRange[1]
mode = mode/2

print('The average weight is: ',mean)
print('Median is: ',median)
print('The most common weight is:',mode)