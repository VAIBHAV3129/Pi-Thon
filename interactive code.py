import math
import random

def get_funky_int(prompt):
    """Asks the mayor of Flavourtown for a righteous number of drops."""
    while True:
        try:
            value = int(input(f"🔥 {prompt} "))
            if value <= 0:
                raise ValueError("Not enough sauce!")
            return value
        except ValueError:
            print("That's not gangster. Enter a real positive integer, my friend.")

def fry_the_needles(total_servings, needle_length, gap_width):
    """Simulate dropping needles onto the griddle."""
    crossings = 0
    for _ in range(total_servings):
       
        dist_to_grill = random.uniform(0, gap_width/2)
       
        angle = random.uniform(0, math.pi)
        
   
        if dist_to_grill <= (needle_length/2) * math.sin(angle):
            crossings += 1
    return crossings

def main():
    print("------------------------------------------")
    print("🎸 WELCOME TO THE PI-THON KITCHEN 🎸")
    print("      Location: Flavourtown, Earth Surface")
    print("------------------------------------------")

  
    n_fries = get_funky_int("How many fries are we dropping on the floor?")
    
   
    fry_len = 1.0
    grill_gap = 2.0
    
    crossings = fry_the_needles(n_fries, fry_len, grill_gap)
    
    if crossings == 0:
        print("Zero hits? That's a culinary disaster. Crank up the heat (N)!")
        return

    pi_est = n_fries / crossings
    
    print("\n--- THE FINAL SCORE ---")
    print(f"Total Fries Dropped: {n_fries}")
    print(f"Fries Crossing the Line: {crossings}")
    print(f"Estimated Pi: {pi_est:.6f} 👈 OUT OF BOUNDS!")
    print(f"Actual Pi:    {math.pi:.6f}")
    print(f"Flavor Error: {abs(math.pi - pi_est):.6f}")
    print("\nPeace, Love, and Taco Grease! ✌️🌮")

if __name__ == "__main__":
    main()
