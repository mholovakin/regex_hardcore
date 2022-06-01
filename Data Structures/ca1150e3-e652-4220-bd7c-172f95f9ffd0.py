# Course: Python Course
# Section: Data Structures
# Chapter: Tuples
# Task Number: 2

try:
    tuple1
except NameError:
    print('Variable \"tuple1\" not defined', file=sys.stderr)
    sys.exit(0)

if tuple1 != (5, 10, 15, 10, 25):
    print('Please, use provided initial values of variables', file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.search('\s*print\s*\(\s*tuple1.count\s*\(\s*10\s*\)\s*\)\s*$', line):
        passed = True

if not passed:
    print("Please, count the number of occurences of 10 in a tuple and print it", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))