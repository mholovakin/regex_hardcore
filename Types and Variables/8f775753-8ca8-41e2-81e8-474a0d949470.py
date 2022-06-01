# Course: Python Course
# Section: Types and Variables
# Chapter: String Special Operations
# Task Number: 2

try:
    country
except NameError:
    print("Variable \"country\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    no_of_states
except NameError:
    print("Variable \"no_of_states\" not defined", file=sys.stderr)
    sys.exit(0)

if not (country == 'Cyprus ' and no_of_states == 6):
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)


code_string = '\n'.join(user_code_lines)
passed = False
if re.search('(\s*country\s*\*\s*no_of_states\s*)|(\s*no_of_states\s*\*\s*country\s*)', code_string):
    passed = True

if not passed:
    print("Please, multiply \"country\" by \"no_of_states\"", file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if line == ('Cyprus ' * 6):
        is_print = True

if not is_print:
    print("Please, print \"country\" \"no_of_states\" times using multiplication operator", file=sys.stderr)
    sys.exit(0)

print(json.dumps({'token': '{{token}}', 'passed': True}))