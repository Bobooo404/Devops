score_input = input("Enter your score: ").strip().lower()

if score_input == "90+" or score_input.startswith("90"):
    print("Grade: A")

elif score_input in ["80-89", "80-90"] or (score_input.isdigit() and 80 <= int(score_input) <= 89):
    print("Grade: B")

elif score_input in ["70-79"] or (score_input.isdigit() and 70 <= int(score_input) <= 79):
    print("Grade: C")

elif score_input in ["60-69"] or (score_input.isdigit() and 60 <= int(score_input) <= 69):
    print("Grade: D")

elif score_input in ["below 60", "below60", "<60"] or (score_input.isdigit() and int(score_input) < 60):
    print("Grade: F")

else:
    # Try to treat it as a pure number
    try:
        score = int(score_input)
        if score >= 90:
            print("Grade: A")
        elif score >= 80:
            print("Grade: B")
        elif score >= 70:
            print("Grade: C")
        elif score >= 60:
            print("Grade: D")
        else:
            print("Grade: F")
    except:
        print("Invalid input! Please enter something like 90+, 80-89, 75, or 45")