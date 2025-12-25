import random

def c(p):
    l = []
    for i in range(2**p):
        l.append(f"{i:0{p}b}")
    x = l.copy()
    for j in l:
        pre = j.find("1")-1
        for idx, k in enumerate(j):
            if k == "1":
                if idx != pre + 1:
                    x.remove(j)
                    break
                pre += 1
    x.sort(key = lambda x: x.count("0"))
    return x

def longest_subarray_k_distinct(n, k):
    if k > len(n):
        raise ValueError("k cannot have a value which is greater than the length of the input list!")
    for i in c(len(n)):
        g = []
        for idx, j in enumerate(i):
            if j == "1":
                g.append(n[idx])
        count = 0
        z = []
        for x in g:
            if x not in z and g.count(x) > 1:
                count += g.count(x)-1
                z.append(x)
        count = len(g) - count
        if count == k:
            return n, g, len(g)
    return n, [], 0

def main():
    l = []
    length = int(input())
    if length > 20:
        raise ValueError("Length of input list should not exceed 20!")
    for i in range(length):
        l.append(random.randint(0,9))
    k = int(input())
    print(longest_subarray_k_distinct(l, k))

if __name__ == "__main__":
    main()