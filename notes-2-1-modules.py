# Modules
# Lucas
# Mar 11 2024

import random

# Demonstrate some parts of the random modlues.
# random.random() -> [0,1]

def coin_flip():
    # Return either heads, tails, or other?
    # Heads -- (0, 0.5)
    # tails -- (0.5, 0.999999)
    # Other -- the rest
    result = random.random()

    if result < 0.5:
        return "heads"
    elif result < 0.999999:
        return "tails"
    else:
        return "other"
    
def main():
    heads = 0
    tails = 0
    others = 0

    for _ in range(5_000_000):
        result = coin_flip()

        if result == "heads":
            heads += 1
        elif result == "tails":
            tails += 1
        else:
            others += 1

    print(f"Heads: {heads}")
    print(f"Tails: {tails}")
    print(f"Other: {others}")

main()