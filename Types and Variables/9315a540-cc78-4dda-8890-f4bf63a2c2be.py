# Course: Python Course
# Section: Types and Variables
# Chapter: Comparison Operators
# Task Number: 1

try:
    france_population
except NameError:
    print("Variable \"france_population\" not defined", file=sys.stderr)
    sys.exit(0)

try:
    uk_population
except NameError:
    print("Variable \"uk_population\" not defined", file=sys.stderr)
    sys.exit(0)


if not (france_population == 669700000 and uk_population == 662700000):
    print("Please, don\'t change variables initial value", file=sys.stderr)
    sys.exit(0)


passed = False
for line in user_code_lines:
    if re.match('\s*print\s*\((\s*uk_population\s*(>|<|>=|<=|==)\s*france_population)|(\s*france_population\s*(>|<|>=|<=|==)\s*uk_population)\s*\)\s*', line):
        passed = True

if not passed:
    print("Please, print comparison of france_population and uk_population", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))