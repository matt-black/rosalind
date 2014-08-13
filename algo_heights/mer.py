import sys, os

def main(argv):
    #make the dir if it doesn't exist
    mer_dir = os.path.join(os.path.dirname(argv[0]), "mer")
    if not os.path.exists(mer_dir):
        os.makedirs(mer_dir)
    #make the A, B arrays
    A, B = process_text_file(argv[1])
    A = list(map(int, A))
    B = list(map(int, B))
    #determine which first element is smaller and call merge_sort accordingly
    if A[0] > B[0]:
        C = merge_sort(B, A)
    else:
        C = merge_sort(A, B)
    C = list(map(str,C))
    with open(os.path.join(mer_dir, "results.txt"), 'w') as f:
        f.write(' '.join(C))


def merge_sort(A, B):
    """merges the two sorted arrays 'A' and 'B' where A[0] < B[0]
    by inserting elements from B into A
    """
    ind_A = 1
    for b in B:
        if b >= A[-1]:
            A.append(b)
        else:
            inserted = False
            while not inserted:
                if b <= A[ind_A]:
                    A.insert(ind_A, b)
                    inserted = True
                else:
                    #try the next ind
                    ind_A += 1
    return A


def process_text_file(file_path):
    """processes the text file and produces the 2 arrays that will be sorted
    """
    f = open(file_path, 'r')
    f.readline()  #ignore the first line
    A = f.readline().rstrip().split()
    f.readline()
    B = f.readline().rstrip().split()
    f.close
    return A, B


if __name__ == "__main__":
    main(sys.argv)
