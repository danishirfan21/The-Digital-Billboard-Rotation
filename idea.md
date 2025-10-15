# Problem Design: Digital Billboard Rotation

## Design Goals

After testing two previous problems (Bitwise OR Skyline and Circular Parity-XOR) where Qwen successfully solved them, we identified that:

1. **Clear, academic problem statements** are too easy for LLMs
2. **Standard algorithmic patterns** (DP, prefix sums) are well-learned
3. **Need more confusion in the specification** itself

## Core Adversarial Strategy

The key insight from Codeforces problems is that difficulty often comes from **parsing ambiguity** rather than algorithmic complexity. Real competitive programming problems use:

- Dense, story-heavy narratives
- Multiple interacting rules
- Buried key insights
- Terminology that suggests wrong approaches
- Confusing edge cases

## Problem Components

### 1. Story Wrapper (Distraction Layer)
- Digital billboards, advertising, engagement metrics
- Terms like "rotation anchor", "span", "priority value"
- Makes it sound like a simulation problem when it's actually computation

### 2. Multiple Small Rules (Cognitive Overload)
- Circular array indexing
- Divisor counting (number theory)
- XOR + popcount (bitwise ops)
- Multiple modulo operations (mod 3, mod 998244353)
- Conditional negation with THREE conditions

### 3. Hidden Traps

**Trap 1: Divisor of index, not value**
- Problem says "divisors of j"
- Easy to misread as "divisors of aⱼ" (the value)
- Clarified only in a note at the end

**Trap 2: Position 0 special case**
- 0 has infinitely many divisors mathematically
- Problem arbitrarily defines it as {1}
- Easy to miss or implement wrong

**Trap 3: Three-way conditional**
```
if wraps AND NOT (both_even AND k≤N/2):
    negate
```
- Natural language: "if wraps, negate, UNLESS both even, UNLESS k>N/2"
- Easy to get boolean logic wrong

**Trap 4: Interaction parity formula**
```
(odd_div_count XOR set_bits) mod 3
```
- XOR then mod 3 (not mod then XOR)
- Easy to confuse order of operations

**Trap 5: Negative numbers in modulo**
- Metric can be negative after negation
- Need proper modulo handling
- Different languages handle this differently

## Why This Should Trip Qwen

1. **Cognitive load**: 5+ concepts to track simultaneously
2. **Ambiguous specification**: Key details buried in prose
3. **No obvious pattern**: Doesn't fit standard DP/greedy/etc
4. **Edge cases**: Position 0, wrapping, even overrides
5. **Misleading terminology**: Sounds like simulation

## Rejected Variants

### Version 1: Pure math formula
- Too abstract, LLMs might find closed form
- Not interesting for humans either

### Version 2: Simulation with state
- Too obviously a simulation problem
- Standard BFS/DFS patterns would work

### Version 3: Game theory
- Would need even more complex rules
- Risk of being unsolvable

## Final Formulation Rationale

The billboard problem combines:
- **Realistic sounding** (city advertising system)
- **Multiple domains** (number theory + bitwise + modular)
- **Confusing specification** (dense, story-heavy)
- **Implementable** (O(N√N + MN) fits constraints)
- **Verifiable** (brute force possible for small inputs)

## Expected Failure Modes for LLMs

1. **Type confusion**: Using aⱼ instead of j for divisors
2. **Boolean errors**: Wrong conditional logic for wrapping
3. **Modulo ordering**: Taking mod at wrong step
4. **Missing precomputation**: O(M×N×N) TLE instead of O(N√N + M×N)
5. **Edge case oversight**: Position 0, negative values
6. **Function typos**: Based on Qwen's first attempt, natural typing errors

## Verification Strategy

- 6 test cases covering all edge cases
- Brute force solution for cross-validation
- Generator for stress testing
- Clear expected outputs

This problem should be **genuinely challenging** for LLMs while remaining **fair** for human competitive programmers who read carefully.