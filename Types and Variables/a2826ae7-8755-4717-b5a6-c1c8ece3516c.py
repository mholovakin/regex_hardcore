# Course: Python Course
# Section: Types and Variables
# Chapter: What are Data types and Variables
# Task Number: 3

try:
    subject_name
except NameError:
    print('Variable \"subject_name\" not defined', file=sys.stderr)
    sys.exit(0)

if subject_name != 'Python Programming':
    print('Please, use provided initial values of variable', file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if line.search('<class \'str\'>'):
        is_print = True

if not is_print:
    print('Please, print the type of given variable.', file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.match('\s*subject_name\s*=\s*\"Python Programming\"\s*', line):
        passed = True

if not passed:
    print('You should change the single quotes to double quotes in \'subject_name\'', file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))