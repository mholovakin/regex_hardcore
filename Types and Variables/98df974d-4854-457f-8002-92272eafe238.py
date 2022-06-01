# Course: Python Course
# Section: Types and Variables
# Chapter: Comparison Operators
# Task Number: 3

try:
    england_population
    usa_population
    australia_population
except NameError:
    print("Variables are not defined", file=sys.stderr)
    sys.exit(0)

if not (england_population == 564321 and usa_population == 456123 and australia_population == 765432):
    print("Please, don\'t change variables initial value", file=sys.stderr)
    sys.exit(0)


passed = 0
for line in user_code_lines:
    if re.search('\s*(<|>|<=|>=)\s*', line):
        passed = passed + 1

if passed < 2:
    print('Please, print comparison of variables', file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))