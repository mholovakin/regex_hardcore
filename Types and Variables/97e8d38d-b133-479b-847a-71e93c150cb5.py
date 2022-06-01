# Course: Python Course
# Section: Types and Variables
# Chapter: Assignment Operators
# Task Number: 1

try:
    project_budget
except NameError:
    print('Variable \"project_budget\" not defined', file=sys.stderr)
    sys.exit(0)

try:
    bonus
except NameError:
    print("Variable \"bonus\" not defined", file=sys.stderr)
    sys.exit(0)

if bonus != 100:
    print("Please, use \"bonus\" variable initial value", file=sys.stderr)
    sys.exit(0)

initial_passed = False
for line in user_code_lines:
    if re.search('\s*project_budget\s*\=\s*500\s*', line):
        initial_passed = True

if not initial_passed:
    print("Please, use provided initial value of \"project_budget\" variable", file=sys.stderr)
    sys.exit(0)

counter = 0
passed = False
for line in user_code_lines:
    if re.search('\s*print\s*\(\'\w+( \w+)*:\s*\',\s*project_budget\)\s*', line):
        counter = counter + 1
    if re.search('\s*project_budget\s*\+\=\s*bonus\s*', line):
        passed = True

if counter != 2:
    print("Please, print \"project_budget\" variable before and after addition", file=sys.stderr)
    sys.exit(0)

if not passed:
    print("Please, use \"+=\" operator", file=sys.stderr)
    sys.exit(0)

if project_budget != 600:
    print("Wrong value of \"project_budget\" variable", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))