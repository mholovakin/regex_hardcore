# Course: Python Course
# Section: Loops
# Chapter: While Loops
# Task Number: 1

try:
    variable
except NameError:
    print("Variable \"variable\" not defined", file=sys.stderr)
    sys.exit(0)

is_initial = False
for line in user_code_lines:
    if re.search("\s*variable\s*=\s*1\s*", line):
        is_initial = True

if not is_initial:
    print("Please, use provided initial value of variable", file=sys.stderr)
    sys.exit(0)

passed = False
is_square = False
for line in user_code_lines:
    if re.search('\s*while\s*\(variable\s*<=\s*5\s*\)\s*', line):
        passed = True
    if re.search('\s*print\s*\(\s*variable\s*(\*\*\s*2\s*|\*\s*variable\s*)\s*', line):
        is_square = True

if not passed:
    print("Please, use \"while\" statement", file=sys.stderr)
    sys.exit(0)

if not is_square:
    print("Please, print square of variable", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))