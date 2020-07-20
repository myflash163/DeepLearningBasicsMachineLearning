from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree

allElectronicsData = open(r'AllElectronics.csv', 'rt')
reader = csv.reader(allElectronicsData)
headers = next(reader)

print(headers)

featureList = []
labelList = []

for row in reader:
    labelList.append(row[len(row) - 1])
    rowDict = {}
    for i in range(1, len(row) - 1):
        rowDict[headers[i]] = row[i]

    featureList.append(rowDict)

print(featureList)
#Vetorize features
#dummyX = vec.fit_tran