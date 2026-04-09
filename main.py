import math
import random

def get_positive_int(prompt):
    """
    Asks the user how many drops to simulate.
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Value must be positive")
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def simulate_buffon(N, L, D):
    """
    Simulate dropping N needles. Returns the number of crossings C.
    """
    crossings = 0
    for _ in range(N):
        x = random.uniform(0, D/2)     
        theta = random.uniform(0, math.pi)  
     
        if x <= (L/2) * abs(math.sin(theta)):
            crossings += 1
    return crossings

def main():
    print("Buffon's Needle Simulation (L = D/2)")
    
    N = get_positive_int("Enter total number of needles (positive integer): ")
   
    L = 1.0
    D = 2.0

   
    C = simulate_buffon(N, L, D)
    if C == 0:
        print("No crossings observed. Try increasing N.")
        return

    
    pi_est = N / C

    
    print(f"\nTotal Needles (N): {N}")
    print(f"Crossings (C): {C}")
    print(f"Estimated π: {pi_est:.6f}")
    print(f"Actual π: {math.pi:.6f}")
    print(f"Absolute Error: {abs(math.pi - pi_est):.6f}")

if __name__ == "__main__":
    main()
