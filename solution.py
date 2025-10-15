import sys

def count_odd_divisors(n):
    """Count divisors of n that are odd."""
    if n == 0:
        return 1  # Special case: position 0 has divisor {1}
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i % 2 == 1:
                count += 1
            if i != n // i and (n // i) % 2 == 1:
                count += 1
        i += 1
    return count

def popcount(n):
    """Count number of set bits in n."""
    return bin(n).count('1')

def main():
    MOD = 998244353
    
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    priorities = [int(next(it)) for _ in range(N)]
    
    # Precompute odd divisor counts for all positions
    odd_divs = [count_odd_divisors(i) for i in range(N)]
    
    # Process each query
    for _ in range(M):
        s = int(next(it))
        k = int(next(it))
        
        # Calculate end position (wrapped)
        end = (s + k - 1) % N
        
        # Calculate XOR and its popcount
        xor_val = s ^ end
        set_bits = popcount(xor_val)
        
        # Calculate span signature
        range_sum = sum(priorities[(s + i) % N] for i in range(k))
        span_sig = (k * s + range_sum) % 3
        
        # Calculate engagement metric
        metric = 0
        for i in range(k):
            pos = (s + i) % N
            # Interaction parity for position pos
            interact_parity = (odd_divs[pos] ^ set_bits) % 3
            # Check if matches span signature
            if interact_parity == span_sig:
                metric += priorities[pos]
        
        # Apply wrapping rule
        wraps = (s + k - 1) >= N
        both_even = (s % 2 == 0) and (k % 2 == 0)
        override = both_even and (k <= N // 2)
        
        if wraps and not override:
            metric = -metric
        
        # Output with proper modulo for negative numbers
        result = metric % MOD
        print(result)

if __name__ == "__main__":
    main()