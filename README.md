# Digital Billboard Rotation — CP Problem Package

An adversarial Div1/Div2-level competitive programming problem designed to challenge LLM reasoning through:
- Multiple interacting conditional rules
- Number theory (divisor counting)
- Bitwise operations (XOR, popcount)
- Circular array handling
- Ambiguous/verbose problem statement

## Files Included

- `problem.md` — Full problem statement
- `solution.md` — Algorithm explanation and complexity analysis
- `solution.py` — Optimal O(N × M × √N) solution
- `solution_bf.py` — Brute force for verification
- `requirements.json` — Time/memory limits
- `test_cases/` — 6 test cases covering edge cases
- `qwen/` — Three Qwen attempts (expected to fail)
- `idea.md` — Problem design rationale
- `generator.py` — Random test generator

## Running Tests

```bash
# Linux/macOS
python3 solution.py < test_cases/1.in

# Windows PowerShell
Get-Content .\test_cases\1.in | python .\solution.py
```

## Key Adversarial Features

1. **Dense specification** — Multiple rules that interact
2. **Divisor counting** — Requires number theory knowledge
3. **XOR + popcount combo** — Easy to confuse with simpler operations
4. **Conditional negation** — Three-way conditional (wraps, even s/k, k>N/2)
5. **Modulo arithmetic** — Multiple mod operations (mod 3, mod 998244353)
6. **Edge case: position 0** — Special divisor handling

## Expected LLM Failure Modes

- Confusing divisor count with value operations
- Wrong implementation of "both even AND k≤N/2" logic
- Forgetting to handle negative numbers in modulo
- Off-by-one in wrap detection
- Missing precomputation of divisors (TLE on large M)