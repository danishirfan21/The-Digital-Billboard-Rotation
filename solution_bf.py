import sys

def get_divisors(n):
    """Get all divisors of n."""
    if n == 0:
        return [1]  # Special case
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

def count_odd_divisors_bf(n):
    """Count odd divisors (brute force)."""
    divs = get_divisors(n)
    return sum(1 for d in divs if d % 2 == 1)

def popcount_bf(n):
    """Count set bits (brute force)."""
    count = 0
    while n > 0:
        if n & 1:
            count += 1
        n >>= 1
    return count

MOD = 998244353

N, M = map(int, input().split())
priorities = list(map(int, input().split()))

for _ in range(M):
    s, k = map(int, input().split())
    
    # End position
    end = (s + k - 1) % N
    
    # XOR and popcount
    xor_val = s ^ end
    set_bits = popcount_bf(xor_val)
    
    # Span signature
    range_sum = 0
    positions = []
    for i in range(k):
        pos = (s + i) % N
        positions.append(pos)
        range_sum += priorities[pos]
    
    span_sig = (k * s + range_sum) % 3
    
    # Engagement metric
    metric = 0
    for pos in positions:
        odd_divs = count_odd_divisors_bf(pos)
        interact_parity = (odd_divs ^ set_bits) % 3
        if interact_parity == span_sig:
            metric += priorities[pos]
    
    # Wrapping rule
    wraps = (s + k - 1) >= N
    both_even = (s % 2 == 0) and (k % 2 == 0)
    override = both_even and (k <= N // 2)
    
    if wraps and not override:
        metric = -metric
    
    print(metric % MOD)