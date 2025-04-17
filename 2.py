cs_file = open("cs.txt", "r")
cs_majors = set(" ".join(line.split(",")).strip().lower() for line in cs_file.read().splitlines()[1:])
cs_file.close()

math_file = open("math.txt", "r")
math_majors = set(" ".join(line.split(",")).strip().lower() for line in math_file.read().splitlines()[1:])
math_file.close()

student_year_file = open("studentYear.txt", "r")
student_year = {}
for line in student_year_file.read().splitlines()[1:]:
    parts = line.split("\t")
    if len(parts) == 2 and parts[0].strip().isdigit():
        year = int(parts[0].strip())
        name = " ".join(parts[1].split(",")).strip().lower()
        student_year[name] = year
student_year_file.close()

sophomore_cs_majors = {student for student, year in student_year.items() if year == 2 and student in cs_majors}
freshmen_not_math_cs = {student for student, year in student_year.items() if year == 1 and student not in cs_majors and student not in math_majors}
senior_math_cs_majors = {student for student, year in student_year.items() if year == 4 and (student in cs_majors or student in math_majors)}

print("Sophomore CS Majors:", sophomore_cs_majors)
print("Freshmen not in Math or CS:", freshmen_not_math_cs)
print("Senior Math and CS Majors:", senior_math_cs_majors)