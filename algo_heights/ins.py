import os,sys


def main(argv):
    #make the directory if it doesn't exist
    ins_dir = os.path.join(os.path.dirname(argv[0]), "ins")
    if not os.path.exists(ins_dir):
        os.makedirs(ins_dir)
    #read the array in from file
    A = process_text_file(argv[1])
    A_sorted, count = insertion_sort(A)
    print(A_sorted)
    with open(os.path.join(ins_dir, "results.txt"), 'w') as f:
        f.write(str(count))

def insertion_sort(A):
    """performs insertion sort and counts the number of swaps made to perform
    the sort.
    """
    count = 0
    for i in range(1, len(A)):
        k = i
        while k > 0 and A[k] < A[k-1]:
            A = swap(A, k)
            count += 1
            k -= 1
    return A, count


def swap(A, k):
    """swap the values at keys 'k' and 'k-1' in the array, 'A'
    returns A with swapped values"""
    tmp = A[k]
    A[k] = A[k-1]
    A[k-1] = tmp
    return A


def process_text_file(file_path):
    f = open(file_path)
    f.readline()  #ignore the first line
    A = f.readline().rstrip().split()
    f.close()
    A_int = map(int,A)
    return list(A_int)

if __name__ == "__main__":
    main(sys.argv)
