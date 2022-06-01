# Course: Python Course
# Section: Types and Variables
# Chapter: Bitwise Operators
# Task Number: 2

is_print = False
for line in user_print_lines:
    if line == '50':
        is_print = True

if not is_print:
    print("Please, print result of bitwise \"OR\" between 34 and 50", file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.match('\s*print\s*\(\s*34\s*\|\s*50\s*\)', line):
        passed = True

if not passed:
    print("Please, print result of bitwise \"OR\" between 34 and 50", file=sys.stderr)
    sys.exit(0)

print(json.dumps({'token': '{{token}}', 'passed': True}))