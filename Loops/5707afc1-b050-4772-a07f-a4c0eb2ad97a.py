# Course: Python Course
# Section: Loops
# Chapter: What are Loops
# Task Number: 2

try:
    language
except NameError:
    print("Variable \"language\" not defined", file=sys.stderr)
    sys.exit(0)

if not (language == ["Python", 'Java', 'C++']):
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)

var_1 = 0
for line in user_code_lines:
    if re.search('for', line):
        var_1 = line

try:
    first = var_1.index('for'[-1])
    second = var_1.index('in')
    variable = var_1[first+1:second]
    variable = variable.strip()
except NameError:
    print("Please, use \"for\" statement", file=sys.stderr)
    sys.exit(0)

if not re.search('\s*for\s*{}\s*in\s*language\s*'.format(variable), var_1):
    print("Please, loop through \"language\" variable", file=sys.stderr)
    sys.exit(0)

is_passed = False
for line in user_code_lines:
    if re.search('\s*print\s*\(\s*{}\s*\)'.format(variable), line):
        is_passed = True

if not is_passed:
    print("Please, print all strings which is in \"language\" variable", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))