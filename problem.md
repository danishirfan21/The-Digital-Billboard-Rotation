# The Digital Billboard Rotation

## Problem Statement

A city has N digital billboards arranged in a circle (numbered 0 to N-1, where billboard N-1 is adjacent to billboard 0). Each billboard displays an advertisement with a "priority value" aᵢ (which can be negative due to debt adjustments).

The city's advertising algorithm works as follows:

Every second, the algorithm selects a "rotation anchor" position **s** and a "span" **k**. It then calculates the **engagement metric** for this configuration:

### Calculation Steps

1. **Range Definition**: Consider all billboards from position s going clockwise for k positions. This means billboards at indices s, s+1, s+2, ..., s+k-1 (wrapping around the circle if necessary).

2. **Parity Matching**: For each billboard j in this range, we check if its "interaction parity" matches the "span signature".

3. **Interaction Parity Calculation** for billboard j:
   - Count how many **divisors** of j are **odd** (including 1 and j itself as potential divisors)
   - XOR this count with the number of **set bits** (1-bits in binary) in the value (s ⊕ ((s+k-1) mod N))
   - Take the result **modulo 3**

4. **Span Signature Calculation**:
   - Compute (k × s + ∑aᵢ) mod 3, where the sum is over all priority values in the range

5. **Metric Accumulation**: 
   - For each billboard j where interaction parity equals span signature, add the priority value aⱼ to the engagement metric

6. **Wrapping Adjustment**: 
   - If the range wraps past position N-1 (i.e., if s+k-1 ≥ N), multiply the final engagement metric by -1

7. **Special Override**: 
   - However, if both s and k are even numbers, ignore the wrapping rule (step 6), UNLESS k > N/2

You are given M queries, each specifying (s, k). For each query, output the engagement metric modulo 998244353.

### Important Clarification

When we say "divisors of j", we mean the divisors of the **INDEX** j (the position number), NOT the priority value aⱼ stored at that position.

**Special case**: For j=0, we define it to have exactly one divisor: {1}. (This is a convention for this problem.)

---

## Input Format

```
N M
a₀ a₁ a₂ ... aₙ₋₁
s₁ k₁
s₂ k₂
...
sₘ kₘ
```

---

## Output Format

For each of the M queries, output the engagement metric modulo 998244353 on a separate line.

---

## Constraints

- 1 ≤ N ≤ 2000
- 1 ≤ M ≤ 10⁵
- -10⁹ ≤ aᵢ ≤ 10⁹
- 0 ≤ s < N
- 1 ≤ k ≤ N

---

## Example

### Input
```
4 3
10 20 30 40
0 2
1 3
2 4
```

### Output
```
30
90
998244253
```

### Explanation (Query 1: s=0, k=2)

- **Range**: Billboards 0 and 1
- **End position**: (0+2-1) mod 4 = 1
- **XOR value**: 0 ⊕ 1 = 1 (binary: 1), which has 1 set bit
- **Span signature**: (2×0 + (10+20)) mod 3 = 30 mod 3 = 0

For **billboard 0**:
- Divisors of 0: {1} (by convention), so 1 odd divisor
- Interaction parity: (1 XOR 1) mod 3 = 0 mod 3 = 0
- Matches span signature (0)! Add a₀ = 10

For **billboard 1**:
- Divisors of 1: {1}, so 1 odd divisor
- Interaction parity: (1 XOR 1) mod 3 = 0
- Matches span signature (0)! Add a₁ = 20

**Metric**: 10 + 20 = 30
**Wrapping check**: s+k-1 = 0+2-1 = 1 < 4, so no wrapping, no negation
**Result**: 30 mod 998244353 = **30**