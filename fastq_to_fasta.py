

fh = open("test.fastq","r")

n=60
while True:
	header = fh.readline().replace("@",">")
	print(header.rstrip())
	read = fh.readline()
	#out = [(read[i:i+n]) for i in range(0, len(read), n)]
	for i in range(0,len(read),n):
		out = read[i:i+n]
		print(out.rstrip())
	fh.readline()
	fh.readline()
	if len(header) == 0:
		break
	
	
	
			


