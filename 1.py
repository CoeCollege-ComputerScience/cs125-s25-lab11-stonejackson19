cs_file = open("cs.txt", "r")
cs_majors = set(" ".join(line.split(",")).strip().lower() for line in cs_file.read().splitlines()[1:])

cs_file.close()

math_file = open("math.txt", "r")
math_majors = set(" ".join(line.split(",")).strip().lower() for line in math_file.read().splitlines()[1:])
math_file.close()

double_majors = math_majors.intersection(cs_majors)
all_majors = cs_majors.union(math_majors)
only_cs = cs_majors - math_majors

print("Math-CS Double Majors:", double_majors)
print("All Math or CS Majors:", all_majors)
print("Strictly CS Majors:", only_cs)