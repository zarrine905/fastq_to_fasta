

fh = open("test.fastq","r")


while True:
	header = fh.readline().replace("@",">")
	read = fh.readline()
	fh.readline()
	fh.readline()
	if len(header) == 0:
		break
	print(header+read.rstrip())
			



