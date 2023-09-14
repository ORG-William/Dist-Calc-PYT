import random

while True:

    print("Dice Sim Menu")
    print("1: Roll Dice Once")
    print("2: Roll Dice 5 Times")
    print("3: Roll Dice 'n' times")
    print("4: Roll Dice until Snake Eyes")
    print("5: Exit")
    print('')

    roll = input("\nSelect an option (1-5): ")
    print('')

    if roll == "1":
        randNumA = random.randint(1, 6)
        randNumB = random.randint(1, 6)
        print(f"{randNumA}, {randNumB} (Sum: {randNumA + randNumB})")
    elif roll == "2":
        for n in range(5):
            randNumA = random.randint(1, 6)
            randNumB = random.randint(1, 6)
            print(f"{randNumA}, {randNumB} (Sum: {randNumA + randNumB})")
    elif roll == "3":
        ranD = int(input("Enter the number of times you want to roll: "))
        for n in range(ranD):
            randNumA = random.randint(1, 6)
            randNumB = random.randint(1, 6)
            print(f"{randNumA}, {randNumB} (Sum: {randNumA + randNumB})")
    elif roll == "4":
        rollCnt = 0
        while True:
            randNumA = random.randint(1, 6)
            randNumB = random.randint(1, 6)
            print(f"{randNumA}, {randNumB} (Sum: {randNumA + randNumB})")
            rollCnt += 1
            if randNumA == randNumB:
                print(
                    f"SNAKE EYES! It took {rollCnt} rolls to get snake eyes.")
                break
    elif roll == "5":
        print("Thanks for using the Simulator")
        break
