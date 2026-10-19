# Starting file for LAB 3-2

print("The Test Scores program")

another_set = "y"

while another_set.lower() == "y":
    print("Enter test scores")
    print("Enter 'end' to end input")
    print("=" * 31)

    total_score = 0
    score_count = 0

    while True:
        entry = input("Enter test score: ")

        if entry.lower() == "end":
            break

        score = int(entry)
        if 0 <= score <= 100:
            total_score += score
            score_count += 1
        else:
            print("Test score must be from 0 through 100. Try again.")

    print("=" * 31)
    if score_count > 0:
        average_score = round(total_score / score_count)
        print(f"Total Score: {total_score}")
        print(f"Average Score: {average_score}")
    else:
        print("No valid scores entered.")

    print()
    another_set = input("Enter another set of test scores (y/n)? ")
    print()

print("Bye!")