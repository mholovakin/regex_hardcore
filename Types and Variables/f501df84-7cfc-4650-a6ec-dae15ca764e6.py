# Course: Python Course
# Section: Types and Variables
# Chapter: What are Data types and Variables
# Task Number: 1

try:
    subject_name
except NameError:
    print('Variable \"subject_name\" not defined', file=sys.stderr)
    sys.exit(0)

try:
    marks_obtained
except NameError:
    print("Variable \"marks_obtained\" not defined", file=sys.stderr)
    sys.exit(0)

if subject_name != 'Python Programming' and marks_obtained != 89:
    print('Please, use provided initial values of variables', file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if re.search('<class (\'str\'|\'int\')>', line):
        is_print = True

if not is_print:
    print('Please, print types of given variables.', file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.match('\s*print\s*\(\s*type\s*\(\s*marks_obtained\s*\)\)\s*', line):
        passed = True

if not passed:
    print("Please, print type of given variable", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))