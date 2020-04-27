from pythonping import ping

ping.size = 2
numberOfPings = 100
listOfAverages = []
for x in range(0,numberOfPings):
	bigString = str(ping('131.123.35.17', verbose=False))
	search = bigString.find('/',bigString.find('max')) + 1
	#search is equal to the first '/' after 'max' plus 1
	listOfAverages.append(int(float(bigString[search:bigString.find('/',search)])))
minAvg = min(listOfAverages)
maxAvg = max(listOfAverages)
rangeAvg = maxAvg - minAvg
histogram = [0] * (rangeAvg + 1)
for i in listOfAverages:
	histogram[i - minAvg] +=1
	#print("adding 1 to " + str(listOfAverages[i]))
print(listOfAverages)
print(histogram)

i = 0
for x in histogram:
	print(str(i + minAvg) + "\t" + "+" * x)
	i += 1
#print("# of MS\t" + " " * (int(max(histogram)/2) - 11) + "number of occurrences" + " " * (int(max(histogram)/2) - 11 + max(histogram)%2) + str(max(histogram)))

avgResponse = 0
for x in range(0, len(histogram)):
	avgResponse += (histogram[x]+minAvg)*x
avgResponse = avgResponse/numberOfPings
#print("\nThe average response time was " + str(avgResponse))

maxResponse = maxAvg
print("The longest response time was " + str(maxResponse))

minResponse = minAvg
print("The shortest response time was " + str(minResponse))

modeResponse = max(histogram)
print("The mode response time was " + str(histogram.index(modeResponse) + minAvg) + " with " + str(modeResponse) + " occurrences.")