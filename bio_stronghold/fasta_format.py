'''Quick utility for working with FASTA files
'''

'''OOP representation of a FASTA file
Use this for operating on the file, itself
'''
class FastaFile:
    '''Initialize with a path to the file
    '''
    def __init__(self, file_path):
        f = open(file_path)
        self.sequences = []

        for i, line in enumerate(f):
            if line[0] == '>':  #we're on a line with sequence id
                self.sequences.append((i, line[1:]))
            else:  #we're on a line w/ sequence data
                continue
        f.close()

    '''Takes a sequence ID, finds that ID in the file, and spits out
    the sequence associated with it, as a FastaSeq
    '''
    def get_seq(self, identifier):
        pass

    '''Get all the identifiers present in a file
    '''
    def get_ids(self):
        return [i[1] for i in sequences]

    '''Processes the entire FASTA file and generates a dictionary
    of FastaSeqs with all the sequences in the file
    '''
    def process_file(self):
        pass
