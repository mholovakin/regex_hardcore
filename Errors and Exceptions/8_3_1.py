# Course: Python Course
# Section: Errors and Exceptions
# Chapter: Raising Exceptions
# Task Number: 1

try:
    var
except NameError:
    print("Variable \"var\" not defined", file=sys.stderr)
    sys.exit(0)

is_type = False
for line in user_code_lines:
    if re.search('\s*if\s*not\s*type\s*\(\s*var\s*\)\s*is\s*int\s*:', line):
        is_type = True
    if re.search('\s*if\s*not\s*isinstance\s*\(\s*var\s*\,\s*int\s*\)\s*', line):
        is_type = True

if not is_type:
    print("Please, check the type of variable \"var\"", file=sys.stderr)
    sys.exit(0)


is_raise = False
for line in user_code_lines:
    if re.search("\s*raise\s*TypeError\s*\(.*\)\s*", line):
        is_raise = True

if not is_raise:
    print("Please, raise an \"TypeError\" exception", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))