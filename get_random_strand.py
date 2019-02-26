from random import *
import os

s_array = []
for numbers in range (0, 1000):
	ran_num = random()
	if ran_num <= .25:
		s_array.append("A")
	elif ran_num <= .50:
		s_array.append("T")
	elif ran_num <= .75:
		s_array.append("G")
	elif ran_num <= 1:
			s_array.append("C")
s = "".join(map(str, s_array))
print(s)

current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)

file = open("random_strand.txt","w")  
file.write(s) 
file.close() 