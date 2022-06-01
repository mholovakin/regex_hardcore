# Course: Python Course
# Section: Data Structures
# Chapter: Dictionary Operations
# Task Number: 3

try:
    capitals
except NameError:
    print("Variable \"capitals\" not defined", file=sys.stderr)
    sys.exit(0)

if capitals != {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}:
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)


var_1 = ''
for line in user_code_lines:
    if re.search('for', line):
        var_1 = line

first = var_1.index('for'[-1])
second = var_1.index('in')
variable = var_1[first+1:second]
variable = variable.strip()

code_string = '\n'.join(user_code_lines)

if not re.search('\s*for\s*{}\s*in\s*capitals.items\s*\(\s*\)\s*:\s*print\s*\(\s*{}\s*\)\s*$'.format(variable, variable), code_string):
    print("Please, loop through keys of capitals and print values", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))