from random import *
import os

current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)

file = open("random_strand.txt", "r")
helix_1 = file.read()
file.close()

helix_2_array = []
base_pair = {"A":"T","T":"A","C":"G","G":"C"}

for nucleotides in helix_1:
	helix_2_array.append(base_pair[nucleotides])

helix_2 = "".join(map(str, helix_2_array))

count = 0
for nucleotides in range (0, 100):
	print(helix_1[count] + " " + helix_2[count])
	count += 1