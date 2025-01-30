def count_students(students, sandwiches) -> int:
    counter = len(students)

    while True:
        print(students, sandwiches)
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            counter = len(students)
        else:
            students.append(students.pop(0))
            counter -= 1
        if counter == 0:
            break

    return len(students)

assert count_students(students=[1,1,1,0,0,1], sandwiches=[1,0,0,0,1,1]) == 0