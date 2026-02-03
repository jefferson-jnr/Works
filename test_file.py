students = {
    "grade_A": [{"name": "Alice", "score": 95}, {"name": "Bob", "score": 98}],
    "grade_B": [{"name": "Charlie", "score": 85}, {"name": "Diana", "score": 88}],
    "grade_C": [{"name": "Eve", "score": 75}],
}


def delete_student_by_name(data: dict, student_name: str) -> bool:
    lists_to_check = [data["grade_A"], data["grade_B"], data["grade_C"]]

    for list_idx, student_list in enumerate(lists_to_check):
        print(f"\nChecking grade list {list_idx}")
        for i, student in enumerate(student_list):
            print(f"  Index {i}: {student['name']}")
            if student["name"] == "Charlie":
                print(f"    ← MATCH FOUND at list {list_idx}, index {i}")
                del student_list[i]
                print(
                    f"    Deleted. Now list {list_idx} has {len(student_list)} students"
                )
                return True
        print(f"  No match in list {list_idx}")
    return False


deleted = delete_student_by_name(students, "Charlie")
print(f"\nDELETED: {'YES' if deleted else 'NO'}")

sdata = [students["grade_A"], students["grade_B"], students["grade_C"]]
sdata2 = [students["grade_A"] + students["grade_B"] + students["grade_C"]]

print(sdata)
print(sdata2)
