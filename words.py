my_list=[]
file = open("words.txt",'r')
for line in file:
	line_no_cr = line.strip("\r\n")
	my_list.append(line_no_cr.lower()),
file.close()
my_list.sort()
for new_line in my_list:
	print new_line
