from random import *
import os

def get_ran_nucleotides():
	global nuc
	ran_num = random()

	if ran_num <= .25:
		nuc = "A"
	elif ran_num <= .50:
		nuc = "T"
	elif ran_num <= .75:
		nuc = "G"
	elif ran_num <= 1:
		nuc = "C"

def template_strand():
	global helix_1_array
	helix_1_array = []
	for numbers in range (0, 102):
		get_ran_nucleotides()
		helix_1_array.append(nuc)

	get_ran_nucleotides()
	rep1 = nuc
	get_ran_nucleotides()
	rep2 = nuc
	get_ran_nucleotides()
	rep3 = nuc

	"".join(map(str, helix_1_array)).replace("ACT", "{0}{1}{2}".format(rep1, rep2, rep3))

	helix_1_array.append("A")
	helix_1_array.append("C")
	helix_1_array.append("T")

	print("Template Strand: " + "".join(map(str, helix_1_array)))

def compliment_strand():
	global helix_2_array
	helix_2_array = []

	base_pairs = {"A":"T", "T":"A", "G":"C", "C":"G"}

	for nucleotide in "".join(map(str, helix_1_array)):
		helix_2_array.append(base_pairs[nucleotide])

	print("Compliment Strand: " + "".join(map(str, helix_2_array)))

def transcribe():
	global mRNA
	rna_base_pairs = {"A":"U", "U":"A", "G":"C", "C":"G"}
	mRNA = "".join(map(str, helix_2_array)).replace("T", "U")
	print("mRNA: " + mRNA)

def translate():
	amino_acids = {"AUU":"Isoleucine","AUC":"Isoleucine","AUA":"Isoleucine","CUU":"Leucine","CUC":"Leucine","CUA":"Leucine","CUG":"Leucine","UUA":"Leucine","UUG":"Leucine", "GUU":"Valine","GUC":"Valine","GUA":"Valine","GUG":"Valine","UUU":"Phenylalanine","UUC":"Phenylalanine","AUG":"Methionine","UGU":"Cysteine","UGC":"Cysteine","GCU":"Alanine","GCC":"Alanine","GCA":"Alanine","GCG":"Alanine","GGU":"Glycine","GGC":"Glycine","GGA":"Glycine","GGG":"Glycine","CCU":"Proline","CCC":"Proline","CCA":"Proline","CCG":"Proline","ACU":"Threonine","ACC":"Threonine","ACA":"Threonine","ACG":"Threonine","UCU":"Serine","UCC":"Serine","UCA":"Serine","UCG":"Serine","AGU":"Serine","AGC":"Serine","UAU":"Tyrosine","UAC":"Tyrosine","UGG":"Tryptophan","CAA":"Glutamine","CAG":"Glutamine","AAU":"Asparagine","AAC":"Asparagine","CAU":"Histidine","CAC":"Histidine","GAA":"Glutamic acid","GAG":"Glutamic acid","GAU":"Aspartic acid","GAC":"Aspartic acid","AAA":"Lysine","AAG":"Lysine","CGU":"Arginine","CGC":"Arginine","CGA":"Arginine","CGG":"Arginine","AGA":"Arginine","AGG":"Arginine","UAA":"Stop","UAG":"Stop","UGA":"Stop"}
	amino_acid_array = []
	codon_array = ([mRNA[i:i+3] for i in range(0, len(mRNA), 3)]) 
	for codon in codon_array:
		amino_acid = amino_acids[codon]
		amino_acid_array.append(amino_acid + ", ")
	print("Corresponding Amino Acids: " + "".join(map(str, amino_acid_array)))

template_strand()
compliment_strand()
transcribe()
translate()