# Course: Python Course
# Section: Loops
# Chapter: Nested for Loops
# Task Number: 2

try:
    persons
except NameError:
    print("Variable \"persons\" not defined", file=sys.stderr)
    sys.exit(0)

if not (persons == ['Alice', 'Bob', 'Carey', 'David']):
    print("Please, use variable initial value", file=sys.stderr)
    sys.exit(0)

var_1 = ''
for line in user_code_lines:
    if re.search('for', line):
        var_1 = line
        break

var_2 = ''
for line in user_code_lines:
    if re.search('for', line):
        var_2 = line

first = var_1.index('for'[-1])
second = var_1.index('in')
variable_1 = var_1[first + 1:second]
variable_1 = variable_1.strip()

first = var_2.index('for'[-1])
second = var_2.index('in')
variable_2 = var_2[first + 1:second]
variable_2 = variable_2.strip()

code_string = '\n'.join(user_code_lines)

if not re.search('\s*for\s*{}\s*in\s*persons:\s*'.format(variable_1), code_string):
    print("Please, use for loop", file=sys.stderr)
    sys.exit(0)

if not re.search('\s*for\s*{}\s*in\s*persons:\s*'.format(variable_2), code_string):
    print("Please, use nested for loop", file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.search('\s*if\s*{}\s*!=\s*{}\s*'.format(variable_1, variable_2), line):
        passed = True

if not passed:
    print("Please, use if statements to compare the values of outer loop with inner loop", file=sys.stderr)
    sys.exit(0)

if not re.search('\s*print\s*\(\s*{}\s*,\s*(\'|\")meets(\'|\"),\s*{}\)\s*'.format(variable_1,variable_2), code_string):
    print("Please, print the names as indicated in the assignment", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))