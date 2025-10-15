import random
import sys

def generate_test(N=10, M=5, seed=None):
    """Generate random test case for Billboard problem."""
    if seed is not None:
        random.seed(seed)
    
    # Generate priorities
    priorities = [random.randint(-1000, 1000) for _ in range(N)]
    
    print(N, M)
    print(' '.join(map(str, priorities)))
    
    # Generate queries
    for _ in range(M):
        s = random.randint(0, N-1)
        k = random.randint(1, N)
        print(s, k)

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        N = int(sys.argv[1])
        M = int(sys.argv[2])
        seed = int(sys.argv[3]) if len(sys.argv) > 3 else None
        generate_test(N, M, seed)
    else:
        # Default: small test
        generate_test(10, 5, 42)