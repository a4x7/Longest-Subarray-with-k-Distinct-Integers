def c(p):
    l = []
    for i in range(2**p):
        l.append(f"{i:0{p}b}")
    x = l.copy()
    for j in l:
        if j.count("1") <= 1:
            x.remove(j)
            continue
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
        raise ValueError
    if k == 1:
        return 1
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
            return len(g)
    return 0

if __name__ == "__main__":
    print(longest_subarray_k_distinct([1,2,4,5,3,4,5,6,4,9,7,5], 4))