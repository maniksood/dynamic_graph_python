import os
from random import randint

for i in range (0, 5000):
	r = str(randint(0,10000))
	f = open('y1.txt', 'w')
	f.write("{\n\t\"n\": " + r + "\n}")
	f.close
	
	os.system("mv y1.txt y.json")	


# import os
# import random

# for i in range (0, 5000):
# 	r = str(random.uniform(0.1,1.9))
# 	f = open('y1.txt', 'w')
# 	f.write("{\n\t\"n\": " + r + "\n}")
# 	f.close
	
# 	os.system("mv y1.txt y.json")	

