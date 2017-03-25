data1= "DataSet.txt"
def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x
kalimat = readData(data1)
hasil=[]
kata = kalimat[0]
kata = kata[0].upper()+kata[1:]
hasil.append(kata)
for i in range(1,len(kalimat)):
    kata=kalimat[i]
    if kata.isdigit() :
        kata=kata[::-1]
    elif kalimat[i][len(kalimat[i])-1]==".":
        kata=kata[0].upper()+kata[1:]
    hasil.append(kata)
hasil= " ".join(hasil)
print(hasil)