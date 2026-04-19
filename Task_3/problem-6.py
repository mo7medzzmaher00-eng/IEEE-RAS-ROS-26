def analyze_grades(grades):
    if not grades:
        return "there is no gardes ya 3abeeeeeeeeet"

    return {
        "average": sum(grades) / len(grades),
        "highest": max(grades),
        "lowest": min(grades)
    }

grades = []

data = input("Enter grades: ").split()

for x in data:
    grades.append(int(x))


print(analyze_grades(grades))
