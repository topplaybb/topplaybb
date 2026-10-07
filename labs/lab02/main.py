# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# CS 31 Ricardo Alvarez Davila 10/7/2026

# Print out Title
print() # prints an empty line
print("My Awesome Quiz on Pyton Concepts")
print() # prints an empty line
print("* " * 20) # print a line of 20 astericks

# Ask for the user's name
print()
username = input("What is your name?")
print(f"Hello, {username}!") # f-string format

# Ask if they want to take a quiz
print()

# Print out Title
print()  # prints an empty line
print("My Awesome Quiz on Pokemon Concepts")
print()  # prints an empty line
print("* " * 20)  # print a line of 20 asterisks

# Ask for the user's name
print()
username = input("What is your name? ")
print(f"Hello, {username}!")  # f-string format

# Ask if they want to take a quiz
print()
start = input("Would you like to take the Pokemon quiz? (yes/no): ")

if start.strip().lower() == "yes":
    print()
    print("Awesome! Let's get started. There are 5 questions in total.")
    print("=" * 40)

    # Initialize score variable
    score = 0

    # --------------------------------------------------
    # Question 1: Multiple Choice
    # --------------------------------------------------
    print()
    print("Question 1:")
    print("What type is Pikachu?")
    print("  A) Fire")
    print("  B) Electric")
    print("  C) Water")
    print("  D) Grass")
    print()

    q1_answer = input("Your answer (A, B, C, or D): ")
    if q1_answer.strip().upper() == "B":
        print("Correct! Pikachu is an Electric-type Pokemon.")
        score = score + 1
    else:
        print("Incorrect! Pikachu is an Electric-type Pokemon (Option B).")

    print(f"Current score: {score}/1")
    print("-" * 30)

    # --------------------------------------------------
    # Question 2: Text / Identification
    # --------------------------------------------------
    print()
    print("Question 2:")
    print("Which Pokemon evolves into Charizard?")
    print()

    q2_answer = input("Enter the Pokemon name: ")
    if q2_answer.strip().lower() == "charmeleon":
        print("Spot on! Charmeleon evolves into Charizard at level 36.")
        score = score + 1
    else:
        print("Not quite! Charmeleon evolves into Charizard.")

    print(f"Current score: {score}/2")
    print("-" * 30)

    # --------------------------------------------------
    # Question 3: Number / Generation
    # --------------------------------------------------
    print()
    print("Question 3:")
    print("How many original Pokemon were in Generation 1 (Kanto region)?")
    print("  A) 100")
    print("  B) 150")
    print("  C) 151")
    print("  D) 251")
    print()

    q3_answer = input("Your answer (A, B, C, or D): ")
    if q3_answer.strip().upper() == "C":
        print("Correct! There are 151 original Pokemon ending with Mew.")
        score = score + 1
    else:
        print("Incorrect! Generation 1 introduced 151 Pokemon (Option C).")

    print(f"Current score: {score}/3")
    print("-" * 30)

    # --------------------------------------------------
    # Question 4: True or False
    # --------------------------------------------------
    print()
    print("Question 4:")
    print("True or False: Water-type moves are super effective against Grass-type Pokemon.")
    print()

    q4_answer = input("Your answer (True or False): ")
    if q4_answer.strip().lower() == "false":
        print("Correct! Water is not very effective against Grass.")
        score = score + 1
    else:
        print("Incorrect! Water moves are weak against Grass-type Pokemon.")

    print(f"Current score: {score}/4")
    print("-" * 30)

    # --------------------------------------------------
    # Question 5: Lore Question
    # --------------------------------------------------
    print()
    print("Question 5:")
    print("Which item is used to wake up a sleeping Snorlax in early games?")
    print("  A) Poke Flute")
    print("  B) Silph Scope")
    print("  C) Super Potion")
    print("  D) Old Rod")
    print()

    q5_answer = input("Your answer (A, B, C, or D): ")
    if q5_answer.strip().upper() == "A":
        print("That's right! You need the Poke Flute to awaken Snorlax.")
        score = score + 1
    else:
        print("Oops! You need the Poke Flute to wake up Snorlax (Option A).")

    print(f"Current score: {score}/5")
    print("=" * 40)

    # --------------------------------------------------
    # Quiz Results and Evaluation
    # --------------------------------------------------
    print()
    print("QUIZ COMPLETE!")
    print(f"Great job, {username}!")
    print(f"Your final score is: {score} out of 5")

    percentage = (score / 5) * 100
    print(f"Your final grade: {percentage}%")
    print()

    if score == 5:
        print("Rank: Pokemon Master! You know your stuff inside and out!")
    elif score >= 3:
        print("Rank: Gym Leader! Very solid knowledge of Pokemon.")
    else:
        print("Rank: Youngster! Hit the books at the Trainer School.")

else:
    print()
    print(f"No problem, {username}. Come back when you are ready to test your skills!")

print()
print("Thank you for playing the Pokemon Quiz!")
print("=" * 40)