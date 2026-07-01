student_data = {
    "id1": {"name": "Sara", "Class": "V", "subject_intgration": "english,math,science" },
    "id2": {"name": "David", "Class": "V", "subject_intgration": "english,math,science" },
    "id3": {"name": "Sara", "Class": "V", "subject_intgration": "english,math,science" },
    "id4": {"name": "Surya", "Class": "V", "subject_intgration": "english,math,science" }
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["name"], details["Class"], details["subject_intgration"])
    
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ":", v)