# Course: Python Course
# Section: Data Structures
# Chapter: Dictionaries
# Task Number: 1

try:
    country_capital
except NameError:
    print("Variable \"country_capital\" not defined", file=sys.stderr)
    sys.exit(0)

if country_capital != {"Australia": "Canberra", "Japan": "Tokyo", "Germany": "Berlin", "Thailand": "Bangkok"}:
    print('Please, use provided initial value of variable', file=sys.stderr)
    sys.exit(0)

is_print = False
for line in user_print_lines:
    if re.match('False', line):
        is_print = True

if not is_print:
    print("Please, print the result of check", file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.search('\s*print\s*\(\s*(\'|\")Mumbai(\'|\")\s*in\s*country_capital.values\s*\(\s*\)\s*\)\s*', line):
        passed = True

if not passed:
    print("Please, check if the country Mumbai exists in the dictionary and print it in one line", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))