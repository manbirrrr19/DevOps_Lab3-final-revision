import employee_info


def test_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(30, 40) #IN BETWEEN 30 AND 40, NOT INCLUSIVE OF
    ans = [{"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
           {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    assert (result == ans)


def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    ans = 60166.67
    assert (result == ans)


def test_get_employees_by_dept():
    result = employee_info.get_employees_by_dept("Marketing")
    ans = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
           {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    assert (result == ans)
