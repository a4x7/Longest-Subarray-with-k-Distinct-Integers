def c(p):
    l = []
    for i in range(2**p):
        l.append(f"{i:0{p}b}")
    x = l.copy()
    for j in l:
        for idx, k in enumerate(j):
            if idx == 0 or idx == len(j) - 1:
                continue
            if k == "1" and j[idx-1] != "1" and j[idx+1] != "1":
                x.remove(j)
                break
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
        for idx, x in enumerate(g):
            if x in z:
                continue
            for y in g[:idx] + g[idx+1:]:
                if x == y:
                    z.append(x)
                    count += 1
        count = len(g) - count
        if count == k:
            return len(g)
    return 0

if __name__ == "__main__":
    print(longest_subarray_k_distinct([1,2,3,4,3,6], 3))