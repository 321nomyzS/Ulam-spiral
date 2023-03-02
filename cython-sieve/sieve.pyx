def sieve_of_eratosthenes(int n):
    cdef int i, p = 2
    cdef list sieve = [True] * (n+1)
    cdef list result = []
    while p*p <= n:
        if sieve[p]:
            for i in range(p*p, n+1, p):
                sieve[i] = False
        p += 1

    for i in range(2, n+1):
        if sieve[i]:
            result.append(i)

    return result
