import sys

def binary_search(A, key):
    '''Searches the given array, A, for key using binary search
    '''
    lo, hi = 0, len(A)-1
    while lo <= hi:
        mid = (lo + hi)/2
        if A[mid] > value: #need to search the top 1/2 of array
            lo = mid + 1
        elif A[mid] < value: #need to search bottom 1/2 of array
            hi = mid - 1
        else: # A[mid] = value
            return mid
    return -1

def process_text_file(file_path):
    '''Reads the text file and implements binary search
    '''
    #open the file
    f = open(file_path)
    len_A = int(f.readline().rstrip())
    f.readline()
    A = f.readline().rstrip().split()
    nums = f.readline().rstrip().split()

    res = []
    for num in nums:
        res.append(binary_search(num))
    return binary_search(nums)

if __name__ == "__main__":
    process_text_file(sys.argv[1])
