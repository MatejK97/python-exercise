'''import random
VACCINES = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"testing vaccines {vac}")
    if vac == LUCKY:
        print("#############")
        print(f"{LUCKY} Vacine, Test SUCCESSFUL")
        print("#############")
        print()
        break
    print("XXXXXXXXXXXXXXXXX")
    print("Test Failed")
    print("XXXXXXXXXXXXXXXXX")
    print()'''

import random
VACCINES = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"testing vaccines {vac}")
    if vac == LUCKY:
        print("#############")
        print(f"{LUCKY} Vacine, Test SUCCESSFUL")
        print("#############")
        print()
        continue
    print("XXXXXXXXXXXXXXXXX")
    print("Test Failed")
    print("XXXXXXXXXXXXXXXXX")
    print()