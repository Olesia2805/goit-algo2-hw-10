# Quick Sort Comparison

## Sorting array of size **10000**
  - Randomized Quick Sort Time: *0.039234* seconds
  - Deterministic Quick Sort Time: *0.032933* seconds

## Sorting array of size **50000**
  - Randomized Quick Sort Time: *0.167020* seconds
  - Deterministic Quick Sort Time: *0.169725* seconds

## Sorting array of size **100000**
  - Randomized Quick Sort Time: *0.348140* seconds
  - Deterministic Quick Sort Time: *0.337603* seconds

## Sorting array of size **500000**
  - Randomized Quick Sort Time: *1.733858* seconds
  - Deterministic Quick Sort Time: *1.796944* seconds

---

![Comparison_of_QuickSort_Algorithms](./Comparison_of_QuickSort_Algorithms.png)
---

# Greedy Algorithm

## Initial data V1

```bash
    subjects = {"Math", "Physics", "Chemistry", "Informatics", "Biology"}
```

```bash
    teachers = [

        Teacher("Oleksandr", "Ivanenko", 45, "o.ivanenko@example.com", {"Math", "Physics"}),

        Teacher("Maria", "Petrenko", 38, "m.petrenko@example.com", {"Chemistry"}),

        Teacher("Serhii", "Kovalenko", 50, "s.kovalenko@example.com", {"Informatics", "Math"},),

        Teacher("Nataliia", "Shevchenko", 29, "n.shevchenko@example.com", {"Biology", "Chemistry"},),

        Teacher("Dmytro", "Bondarenko", 35, "d.bondarenko@example.com", {"Physics", "Informatics"},),

        Teacher("Olena", "Grytsenko", 42, "o.grytsenko@example.com", {"Biology"}),

    ]
```

## Class Schedule:

- **Oleksandr Ivanenko**, 45 years old, email: o.ivanenko@example.com

   `Teaches subjects`: Math, Physics

- **Nataliia Shevchenko**, 29 years old, email: n.shevchenko@example.com

   `Teaches subjects`: Biology, Chemistry

- **Serhii Kovalenko**, 50 years old, email: s.kovalenko@example.com

   `Teaches subjects`: Math, Informatics

## Initial data V2

```bash
    subjects = {"Math", "Physics", "Chemistry", "Informatics", "Biology", "English"}
```

```bash
    teachers = [

        Teacher("Oleksandr", "Ivanenko", 45, "o.ivanenko@example.com", {"Math", "Physics"}),

        Teacher("Maria", "Petrenko", 38, "m.petrenko@example.com", {"Chemistry"}),

        Teacher("Serhii", "Kovalenko", 50, "s.kovalenko@example.com", {"Informatics", "Math"},),

        Teacher("Nataliia", "Shevchenko", 29, "n.shevchenko@example.com", {"Biology", "Chemistry"},),

        Teacher("Dmytro", "Bondarenko", 35, "d.bondarenko@example.com", {"Physics", "Informatics"},),

        Teacher("Olena", "Grytsenko", 42, "o.grytsenko@example.com", {"Biology"}),

    ]
```

## Class Schedule:

- It is impossible to cover all subjects with the available teachers.