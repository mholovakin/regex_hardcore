# Course: Python Course
# Section: Loops
# Chapter: For Loops
# Task Number: 1

try:
    list_fruits
except NameError:
    print("Variable \"list_fruits\" not defined", file=sys.stderr)
    sys.exit(0)

if not (list_fruits == ['banana', 'apple', 'mango', 'guava']):
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)

var_1 = 0
for line in user_code_lines:
    if re.search('for', line):
        var_1 = line
try:
    first = var_1.index('for'[-1])
    second = var_1.index('in')
    variable = var_1[first+1:second]
    variable = variable.strip()
except NameError:
    print("Please, use \"for\" statement", file=sys.stderr)
    sys.exit(0)

if not re.search('\s*for\s*{}\s*in\s*list_fruits\s*'.format(variable), var_1):
    print("Please, loop through \"list_fruits\" variable", file=sys.stderr)
    sys.exit(0)

is_passed = False
for line in user_code_lines:
    if re.search('\s*print\s*\(\s*{}\s*\)'.format(variable), line):
        is_passed = True

if not is_passed:
    print("Please, print all strings which is in \"list_fruits\" variable", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))