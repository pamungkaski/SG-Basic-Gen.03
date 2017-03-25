data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x
kata1 = readData(data1)
kata2 = readData(data2)

gabungan = [x for x in kata1 if x in kata2]
gabungan = " ".join(gabungan)
print(gabungan)