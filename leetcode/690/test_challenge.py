from challenge import Employee, Solution
# Pytesting

def testing(emps: list, emp_id: int, correct_importance: list[int]) -> None:
    sol = Solution()
    assert sol.getImportance(emps, emp_id) == correct_importance


if __name__ == "__main__":
    emps = [Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])]
    testing(emps, 1, 11)

    emps = [Employee(1, 2, [5]), Employee(5, -3, [])]
    testing(emps, 5, -3)
