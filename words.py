my_list=[]
file = open("words.txt",'r')
for line in file:
	print line,
	line_no_cr = line.strip("\r\n")
	my_list.append(line_no_cr),
print my_list[0]
