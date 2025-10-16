def count_positive_odd_divisors(n):
    """Return the number of positive odd divisors of n.
       By convention, φ(0) = 1."""
    if n == 0:
        return 1
    count = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            if d % 2 == 1:
                count += 1
            other = n // d
            if other != d and other % 2 == 1:
                count += 1
        d += 1
    return count


def hamming_distance(a, b):
    """Return the Hamming distance (number of differing bits) between a and b."""
    return bin(a ^ b).count('1')


def solve(N, A, M, commands):
    MOD = 998244353

    results = []

    for s, k in commands:
        # Step 1: Determine the indices in range J
        J = [(s + d) % N for d in range(k)]
        
        # Step 2: Terminal anchor t
        t = (s + k - 1) % N
        
        # Step 3: Compute φ(j) for each j in J, ω(s,t), then σ(j)
        phi_vals = {}
        for j in J:
            phi_vals[j] = count_positive_odd_odd_divisors(j)  # φ(j)

        omega_st = hamming_distance(s, t)  # ω(s,t)

        sigma = {}
        for j in J:
            sigma_j = (phi_vals[j] ^ omega_st) % 3
            sigma[j] = sigma_j

        # Step 4: Compute Σ(s,k) = (k * s + sum of A_j over j in J) mod 3
        total_A = sum(A[j] for j in J)
        Sigma_sk = (k * s + total_A) % 3

        # Step 5: Sum A_j for all j in J where σ(j) == Σ(s,k)
        V = sum(A[j] for j in J if sigma[j] == Sigma_sk)

        # Step 6: Check wrapping condition for negation
        # Wraps if s + k - 1 >= N
        wraps = (s + k - 1) >= N
        if wraps:
            # Negate unless both s and k are even AND k <= N/2
            if not (s % 2 == 0 and k % 2 == 0 and k <= N // 2):
                V = -V

        # Final result modulo 998244353
        results.append(V % MOD)

    return results


# Example usage:
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    # Parse first two values: N and M
    it = iter(data)
    N = int(next(it))
    M = int(next(it))

    # Next N integers: A[0] to A[N-1]
    A = [int(next(it)) for _ in range(N)]

    # Next M pairs: each command (s, k)
    commands = []
    for _ in range(M):
        s = int(next(it))
        k = int(next(it))
        commands.append((s, k))

    # Solve and print each result on separate line
    results = solve(N, A, M, commands)
    for res in results:
        print(res)