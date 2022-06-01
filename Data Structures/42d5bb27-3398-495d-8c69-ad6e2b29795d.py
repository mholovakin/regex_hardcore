# Course: Python Course
# Section: Data Structures
# Chapter: Tuples
# Task Number: 1

try:
    tuple1
except NameError:
    print('Variable \"tuple1\" not defined', file=sys.stderr)
    sys.exit(0)

if tuple1 != ("orange", [10,20,30], (5,10,15)):
    print('Please, use provided initial values of variables', file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.search('\s*print\s*\(\s*tuple1\s*\[\s*1\s*\]\s*\[\s*1\s*\]\s*\)\s*', line):
        passed = True

if not passed:
    print("Please, access a value 20 from the following tuple and print it", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))