data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x
sensor =["I","and","The","you"]
kata = readData(data1)
kata = [x for x in kata if x not in sensor]
gabung = " ".join(kata)
print(gabung)