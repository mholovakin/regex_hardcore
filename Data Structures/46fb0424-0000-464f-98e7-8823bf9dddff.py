# Course: Python Course
# Section: Data Structures
# Chapter: List Comprehension
# Task Number: 2

try:
    list1
except NameError:
    print("Variable \"list1\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    new_list
except NameError:
    print("Variable \"new_list\" not defined", file=sys.stderr)
    sys.exit(0)

if list1 != ['Python', 'is', 'a', 'Programming', 'language']:
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)

var_1 = ''
for line in user_code_lines:
    if re.search('for', line):
        var_1 = line
        break

first = var_1.index('for')+2
second = var_1.index('in')
variable = var_1[first+1:second]
variable = variable.strip()

passed = False
for line in user_code_lines:
    if re.search('\s*new_list\s*\=\s*\[\s*{}\[0\]\s*for\s*{}\s*in\s*list1\s*\]\s*'.format(variable, variable), line):
        passed = True

if not passed:
    print("Please, iterate over the variable \"list1\" using list comprehension, picking the first letter of sentence", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_code_lines:
    if re.search('\s*print\s*\(\s*new_list\s*\)\s*', line):
        is_print = True

if not is_print:
    print("Please, print value of \"new_list\"", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))