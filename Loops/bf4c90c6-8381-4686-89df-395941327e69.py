# Course: Python Course
# Section: Loops
# Chapter: For Loops
# Task Number: 2

passed = False
is_comparison = False
is_print_even = False
is_print_odd = False

var_1 = 0
for line in user_code_lines:
    if re.search('for', line):
        var_1 = line

first = var_1.index('for'[-1])
second = var_1.index('in')
variable = var_1[first+1:second]
variable = variable.strip()

for line in user_code_lines:
    if re.search("\s*for\s*{}\s*in\s*range\s*\(\s*1\s*,\s*21\s*\):\s*".format(variable), line):
        passed = True
    if re.search('\s*{}\s*\%\s*2\s*\=\=\s*0\s*'.format(variable), line):
        is_comparison = True
    if re.search('\s*print\s*\(\s*{}\s*.*Even\s*'.format(variable), line):
        is_print_even = True
    if re.search('\s*print\s*\(\s*{}\s*.*Odd\s*'.format(variable), line):
        is_print_odd = True

if not passed:
    print("Please, use initial \"for loop\"", file=sys.stderr)
    sys.exit(0)

if not is_comparison:
    print("Please, use integer division by 2 to find even numbers", file=sys.stderr)
    sys.exit(0)

if not (is_print_even and is_print_odd):
    print("Please, print Odd or Even", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))
