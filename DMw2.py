C = dict() # C[n,k] is equal to n choose k

for n in range(8):
    C[n, 0] = 1
    C[n, n] = 1
    print(n)

    for k in range(1, n):
        C[n, k] = C[n - 1, k - 1] + C[n - 1, k]
        print(n, k)

print(C[5, 3])