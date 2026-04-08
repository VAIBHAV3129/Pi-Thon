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
        x = random.uniform(0, D/2)     # distance from center to nearest line
        theta = random.uniform(0, math.pi)  # orientation angle
        # Check if the needle crosses a line:
        if x <= (L/2) * abs(math.sin(theta)):
            crossings += 1
    return crossings

def main():
    print("Buffon's Needle Simulation (L = D/2)")
    # Input: total needles N
    N = get_positive_int("Enter total number of needles (positive integer): ")
    # Use default L=1, D=2
    L = 1.0
    D = 2.0

    # Run the simulation
    C = simulate_buffon(N, L, D)
    if C == 0:
        print("No crossings observed. Try increasing N.")
        return

    # Calculate π using the simplified formula π ≈ N/C
    pi_est = N / C

    # Output results
    print(f"\nTotal Needles (N): {N}")
    print(f"Crossings (C): {C}")
    print(f"Estimated π: {pi_est:.6f}")
    print(f"Actual π: {math.pi:.6f}")
    print(f"Absolute Error: {abs(math.pi - pi_est):.6f}")

if __name__ == "__main__":
    main()
