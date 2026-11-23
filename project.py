


def check_eligibility(name, age, citizen):

    if age >= 18 and citizen == "y":
        print(name, "is eligible to vote.")
        return True

    else:
        print(name, "is not eligible to vote.")

        if age < 18:
            print("Reason: Age is below 18.")
            print("Years left to become eligible:", 18 - age)

        if citizen == "n":
            print("Reason: Not an Indian citizen.")

        return False

voters_checked = 0
eligible_voters = 0
not_eligible_voters = 0

while True:

    name = input("\nEnter your name: ")

    while True:
        try:
            age = int(input("Enter your age: "))

            if age < 0 or age > 120:
                print("Invalid age. Age must be between 0 and 120.")
                continue

            break

        except ValueError:
            print("Invalid input. Enter a whole number.")

    while True:
        citizen = input("Indian citizen (y/n): ").lower()

        if citizen == "y" or citizen == "n":
            break
        else:
            print("Please enter y or n.")

    result = check_eligibility(name, age, citizen)

    voters_checked += 1

    if result:
        eligible_voters += 1
    else:
        not_eligible_voters += 1


    again = input("\nCheck another voter? (y/n): ").lower()

    if again != "y":
        break

print("Voters checked:", voters_checked)
print("Eligible voters:", eligible_voters)
print("Not eligible voters:", not_eligible_voters)


