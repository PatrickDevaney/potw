def ipconvert(tenIP):
	octIP = []
	for i in range(4):
		octIP = [(tenIP % 256)] + octIP
		tenIP = tenIP // 256
	final = ""
	for n in octIP:
		final += str(n) + "."
	# Taking "print out" literally
	print(final[:-1])
