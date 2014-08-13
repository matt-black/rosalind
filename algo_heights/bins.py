import os, sys
import math


def main(argv):
    res = []
    #make the new dir if it doesn't exist already
    bins_dir = os.path.join(os.path.dirname(argv[0]), "bins")
    if not os.path.exists(bins_dir):
        os.makedirs(bins_dir)
    #do the hard work!
    A, nums = process_text_file(argv[1])
    for num in nums:
        res.append(binary_search(A, num))
    # write res to a text file
    with open(os.path.join(bins_dir, "result.txt"), "w") as f:
        new_res = map(add_one_if_found, res)
        str_res = map(str, new_res)
        f.write(' '.join(str_res))


def add_one_if_found(num):
    """adds one to the number if it was found by the binary search
    """
    if num > -1:
        return num + 1
    else:
        return num


def binary_search(A, key):
    """Searches the given array, A, for supplied key using binary search
    """
    lo, hi = 0, len(A)
    while lo < hi:
        mid = (lo + hi)//2
        if key < A[mid]:
            #search the bottom half of the array
            hi = mid
        elif key > A[mid]:
            #search the top half of the array
            lo = mid + 1
        else:
            #found it!
            return mid
    return -1


def process_text_file(file_path):
    """Reads the text file in and returns the relevant variables
    """
    with open(file_path) as f:
        #need to clear first 2 lines
        f.readline()
        f.readline()
        A_str = f.readline().rstrip().split()
        A = list(map(int, A_str))
        nums_str = f.readline().rstrip().split()
        nums = map(int, nums_str)
    return A, nums


if __name__ == "__main__":
    main(sys.argv)
