import sys

def main():
    MOD = 998244353

    def count_positive_odd_odd_divisors(j: int) -> int:
        if j <= 0:
            return 1 if j == 0 else 0
        count = 0
        i = 1
        while i * i <= j:
            if j % i == 0:
                if i % 2 == 1:
                    count += 1
                other = j // i
                if other != i and other % 2 == 1:
                    count += 1
            i += 1
        return count

    def odd_index_divisor_count(j: int) -> int:
        return count_positive_odd_odd_divisors(j)

    def count_odd_divisors(j: int) -> int:
        return odd_index_divisor_count(j)

    def xor_popcount(a: int, b: int) -> int:
        return bin(a ^ b).count("1")

    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    A = list(map(int, data[2:2+n]))
    
    queries = []
    index = 2 + n
    for i in range(m):
        s = int(data[index]); k = int(data[index+1]); index += 2
        queries.append((s, k))
    
    # Process each query
    for s, k in queries:
        # Compute ω = popcount(s ⊕ t)
        t = k
        omega = xor_popcount(s, t)
        
        # φ(j) is the number of positive odd divisors of j
        def phi(j):
            return count_odd_divisors(j)
        
        arc_sum = 0
        # Iterate over j from 0 to k-1 (arc indices)
        for j in range(k):
            # σ(j) = (φ(j) XOR ω) % 3
            sigma_j = (phi(j) ^ omega) % 3
            # Σ = (k·s + sum over arc) % 3
            # The value contributed by index j is A[(s + j) % n]
            idx = (s + j) % n
            element = A[idx]
            sigma = sigma_j  # σ at position j
            Sigma = (k * s + arc_sum) % 3  # Σ up to but not including current
            
            # Apply transformation based on σ and Σ
            # Write the formula inline as specified
            # σ(j) = ( phi(j) XOR omega ) % 3
            
            # Wrap negation with even/even/half exception
            # Rule: if σ == 0: leave unchanged
            #       if σ == 1: negate if Σ is even, else leave
            #       if σ == 2: negate only if Σ is even AND we are at half index?
            # But "even/even/half" exception suggests:
            # According to standard Aurora: 
            #   v_j' = (-1)^{δ} * v_j
            #   where δ = 1 when:
            #     σ=1 and Σ even, OR
            #     σ=2 and Σ even and j == k//2 (half)
            #     otherwise 0.
            
            negate = False
            if sigma == 1:
                if Sigma % 2 == 0:
                    negate = True
            elif sigma == 2:
                if Sigma % 2 == 0:
                    # Check for half exception: j == k//2 (when k is odd, exact middle; when even, first of two middles?)
                    # Typically "half" means j == k//2
                    if j == k // 2:
                        negate = True
            
            transformed = -element if negate else element
            arc_sum += transformed
        
        # Final V is the total transformed sum
        V = arc_sum % MOD
        print(V)

if __name__ == "__main__":
    main()