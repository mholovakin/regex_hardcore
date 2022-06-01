# Course: Python Course
# Section: Types and Variables
# Chapter: Assignment Operators
# Task Number: 2

try:
    score
except NameError:
    print("Variable \"score\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    multiplier
except NameError:
    print("Variable \"multiplier\" not defined", file=sys.stderr)
    sys.exit(0)

if multiplier != 3:
    print("Please, use variables initial value", file=sys.stderr)
    sys.exit(0)

initial_passed = False
for line in user_code_lines:
    if re.match('\s*score\s*\=\s*1500\s*', line):
        initial_passed = True

if not initial_passed:
    print("Please, use provided initial value of \"score\" variable", file=sys.stderr)
    sys.exit(0)

counter = 0
passed = False
for line in user_code_lines:
    if re.search('\s*print\s*\(\'\w+( \w+)*:\s*\',\s*score\s*\)\s*', line):
        counter = counter + 1
    if re.search('\s*score\s*\*\=\s*multiplier\s*', line):
        passed = True

if counter != 2:
    print("Please, print \"score\" variable before and after multiplication", file=sys.stderr)
    sys.exit(0)

if not passed:
    print("Please, use \"*=\" operator", file=sys.stderr)
    sys.exit(0)

if score != 4500:
    print("Wrong value of \"score\" variable", file=sys.stderr)
    sys.exit(0)

print(json.dumps({'token': '{{token}}', 'passed': True}))