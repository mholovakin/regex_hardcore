# Course: Python Course
# Section: Data Structures
# Chapter: Dictionaries
# Task Number: 2

try:
    country_capital
except NameError:
    print("Variable \"country_capital\" not defined", file=sys.stderr)
    sys.exit(0)

code_string = '\n'.join(user_code_lines)

init = False
if re.search("\s*country_capital\s*\=\s*\{(\"|\')Australia(\"|\')\s*:\s*(\"|\')Canberra(\"|\'),\s*(\"|\')Japan(\"|\'):\s*(\"|\')Tokyo(\"|\'),\s*(\"|\')Germany(\"|\'):\s*(\"|\')Berlin(\"|\'),\s*(\"|\')Thailand(\"|\'):\s*(\"|\')Bangkok(\"|\')\s*\}\s*", code_string):
    init = True

if not init:
    print("Please, use provided initial values of variables", file=sys.stderr)
    sys.exit(0)


passed = False
for line in user_code_lines:
    if re.search('\s*del\s*country_capital\s*\[(\'|\")Japan(\'|\")\]\s*'):
        passed = True

if not passed:
    print("Please, try to remove Japan from dictionary using \"del\" operator", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))