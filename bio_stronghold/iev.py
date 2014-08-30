#Calculating Expected Offspring
#IEV

"""Given: Six positive integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring."""

data_in = [17042,17697,19646,16600,19198,16178] #modify this line
d = {0:1,1:1,2:1,3:0.75,4:0.5,5:0}
Ex = 0

for index,val in enumerate(data_in):
    Ex += 2*val*d[index]
    
print(Ex)