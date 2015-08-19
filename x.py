import os

for i in range (0, 5000):
	
	f = open('x1.txt', 'w')
	f.write("{\n\t\"n\": " + str(i) + "\n}")
	f.close
	
	os.system("mv x1.txt x.json")	

