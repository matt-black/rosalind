import sys


def two_sum(arr, s, n):
    i, j = 0, n - 1
    while i < j:
        t = arr[i] + arr[j]
        if t < s:
            i++
        elif t > s:
            j--
        else:
            return i, j
    return -1

def get_file_lines(file_path):
    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            yield line

if __name__ == "__main__":
    #grab the file
    file_path = sys.argv[1]
    with open(file_path, 'r') as f:
        line1_arr = f.readline().split()
    k, n = line1_arr[0], line1_arr[1]
    vals = []
    for i, line in get_file_lines(file_path):
        if i == 0:
            continue
        else:
            arr = list(map(int, line.split()))
            x = two_sum(arr.sort(), 0, n)
            vals.append(x)
    #write the new file
