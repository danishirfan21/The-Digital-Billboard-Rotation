def count_odd_divisors(n):
    """Count odd divisors of n"""
    if n == 0:
        return 1  # Special case: 0 has divisor {1} as mentioned
    count = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 1:
            count += 1
    return count

def count_set_bits(n):
    """Count number of 1-bits in binary representation"""
    return bin(n).count('1')

# Read input
N, M = map(int, input().split())
priorities = list(map(int, input().split()))

# Precompute odd divisor counts for all positions 0 to N-1
odd_divisor_count = []
for j in range(N):
    odd_divisor_count.append(count_odd_divisor(j))

MOD = 998244353

# Process each query
for _ in range(M):
    s, k = map(int, input().split())
    
    # Calculate end position
    end_pos = (s + k - 1) % N
    
    # Calculate s XOR ((s+k-1) mod N)
    xor_val = s ^ end_pos
    set_bits = count_set_bits(xor_val)
    
    # Calculate span signature
    range_sum = 0
    positions_in_range = []
    
    # Get all positions in the range
    for i in range(k):
        pos = (s + i) % N
        positions_in_range.append(pos)
        range_sum += priorities[pos]
    
    span_signature = (k * s + range_sum) % 3
    
    # Calculate engagement metric
    engagement_metric = 0
    
    for pos in positions_in_range:
        # Calculate interaction parity for position pos
        odd_div_count = odd_divisor_count[pos]
        interaction_parity = (odd_div_count ^ set_bits) % 3
        
        # Check if interaction parity matches span signature
        if interaction_parity == span_signature:
            engagement_metric += priorities[pos]
    
    # Handle wrapping rule
    wraps = (s + k - 1) >= N
    
    # Special condition: both s and k are even, and k <= N/2
    both_even_and_small_k = (s % 2 == 0 and k % 2 == 0 and k <= N // 2)
    
    # Apply negative multiplier if wraps and not the special case
    if wraps and not both_even_and_small_k:
        engagement_metric *= -1
    
    # Output result modulo 998244353
    # Handle negative modulo correctly
    result = engagement_metric % MOD
    if result < 0:
        result += MOD
    print(result)