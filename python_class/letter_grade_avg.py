# main_program.py
from grade_compute import letter_to_number, number_to_letter

def main():
    grades = []  # will hold pairs: (letter, number)

     #grades from the user
    print("Enter grades such as a, A,b-,C,D")
    while len(grades) < 4:
        g = input(f"Enter grade #{len(grades)+1} (or q to quit): ").strip()
        # Allow quit
        if g.lower() == "q":
            print("Quitting program.")
            return

        # Convert grade to number
        num = letter_to_number(g)
        
        # make all grades uppercase because lowercase is stuupid
        grades.append((g.upper(), num))

    # STEP 2: Find the lowest grade had to watch a long video about lambda :)
    lowest = min(grades, key=lambda x: x[1])

    # average of the remaining scores
    remaining = [num for (let, num) in grades if num != lowest[1]]
    avg = sum(remaining) / 3

    #results
    print("\nResults:")
    print("Lowest dropped:", lowest[0])
    print("Average (number):", round(avg, 3))
    print("Average (letter):", number_to_letter(avg))


#actually calling the function
main()


