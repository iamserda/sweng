from collections import deque


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: list["Employee"], id: int) -> int:
        emp_dictio = {}

        for employee in employees:
            emp_dictio[employee.id] = employee

        total_importance = 0
        subordinates = deque()
        subordinates.append(id)

        while subordinates:
            eid = subordinates.popleft()
            total_importance += emp_dictio[eid].importance
            for subordinate_id in emp_dictio[eid].subordinates:
                subordinates.append(subordinate_id)

        return total_importance
