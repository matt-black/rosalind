#Finding a Protein Motif
#MPRT

#read file in, get protein names
f = open('rosalind_mprt.txt','r')
prots = []
for line in f:
    prots.append(line.rstrip())
    
from urllib.request import urlopen
import re
for prot in prots:
    #open webpage & get sequence out
    html = urlopen('http://www.uniprot.org/uniprot/'+prot+'.fasta')
    lines = []
    for line in html.readlines():
        lines.append(line.rstrip().decode('utf-8'))
    protseq = ''.join(lines[1:])
    html.close()
    #analyze the sequence
    match = re.finditer(r'(?=N[^P][ST][^P])',protseq)
    count = 0
    for m in match:
        if count == 0: print(prot)
        count += 1
        print(m.start()+1,end =' ')
    print('')