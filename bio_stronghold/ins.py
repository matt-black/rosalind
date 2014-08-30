import sys

def insertion_sort(n,A):
    """Performs an insertion sort on the input array, A
    and returns A as a sorted array
    """
    for i in range(1,n-1):
        k = i
        while k > 1 and A[k] < A[k-1]:
            #swap the values
            temp = A[k]
            A[k] = A[k-1]
            A[k-1] = temp
            #bring k down 1
            k = k-1
    return A

def process_file(file_path):
    f = open(file_path)
    n = int(f.readline().rstrip())
    A_str = f.readline().rstrip().split()
    A = map(int, A_str)
    return n,A

if __name__ == "__main__":
    if len(sys.argv) != 1:
        raise Exception("not the right # of args! only specify the file")
    else:
        n,A = process_file(sys.argv[1])
        A_sorted = insertion_sort(n,A)
        print(A_sorted)
