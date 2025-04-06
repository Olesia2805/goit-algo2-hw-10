class Teacher:
    def __init__(self, first_name, last_name, age, email, subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.assigned_subjects = set(subjects)


def create_schedule(subjects, teachers):
    schedule = []
    uncovered_subjects = set(subjects)

    while uncovered_subjects:
        if not teachers:
            return None

        best_teacher = None
        best_coverage = 0

        for teacher in teachers:
            coverage = len(uncovered_subjects.intersection(teacher.assigned_subjects))

            if coverage > best_coverage:
                best_coverage = coverage
                best_teacher = teacher

        if not best_teacher:
            return None

        schedule.append(best_teacher)
        uncovered_subjects -= best_teacher.assigned_subjects
    return schedule


if __name__ == "__main__":
    subjects = {"Math", "Physics", "Chemistry", "Informatics", "Biology"}

    teachers = [
        Teacher(
            "Oleksandr", "Ivanenko", 45, "o.ivanenko@example.com", {"Math", "Physics"}
        ),
        Teacher("Maria", "Petrenko", 38, "m.petrenko@example.com", {"Chemistry"}),
        Teacher(
            "Serhii",
            "Kovalenko",
            50,
            "s.kovalenko@example.com",
            {"Informatics", "Math"},
        ),
        Teacher(
            "Nataliia",
            "Shevchenko",
            29,
            "n.shevchenko@example.com",
            {"Biology", "Chemistry"},
        ),
        Teacher(
            "Dmytro",
            "Bondarenko",
            35,
            "d.bondarenko@example.com",
            {"Physics", "Informatics"},
        ),
        Teacher("Olena", "Grytsenko", 42, "o.grytsenko@example.com", {"Biology"}),
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Class Schedule:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} years old, email: {teacher.email}"
            )
            print(f"   Teaches subjects: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("It is impossible to cover all subjects with the available teachers.")
