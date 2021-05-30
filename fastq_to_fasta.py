#Script: Conversion of fastq file to fasta format
#Author: Zarrine 
#Date: 30/05/2021

fh = open("test.fastq","r")

n=60
while True:
	header = fh.readline().replace("@",">")
	print(header.rstrip())
	read = fh.readline()
	for i in range(0,len(read),n):
		out = read[i:i+n]
		print(out.rstrip())
	fh.readline()
	fh.readline()
	if len(header) == 0:
		break
	
	
	
			


