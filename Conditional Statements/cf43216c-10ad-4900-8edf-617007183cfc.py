# Course: Python Course
# Section: Conditional Statements
# Chapter: The Break and Continue Statements
# Task Number: 1

if len(user_code_lines) == 0:
    print("No code found", file=sys.stderr)
    sys.exit(0)

if not ('10' in user_print_lines and '20' in user_print_lines and '30' in user_print_lines and '50' in user_print_lines):
    print("Wrong answer. Please, check \"break-continue\" operators", file=sys.stderr)
    sys.exit(0)

passed = False
for line in user_code_lines:
    if re.search('\s*for\s*[a-z]*\s*in\s*\[\s*10\s*,\s*20\s*,\s*30\s*,\s*40\s*,\s*50\s*,\s*60\s*,\s*70\s*\]', line):
        passed = True

if not passed:
    print("Please, print \"for loop\" with array [10,20,30,40,50,60,70]", file=sys.stderr)
    sys.exit(0)

code_string = '\n'.join(user_code_lines)

is_continue = False
if re.search('\s*if\s*(\(|)[a-z]+\s*\=\=\s*40\s*(\)|):\s*continue\s*', code_string):
    is_continue = True

is_break = False
if re.search('\s*(\(|)[a-z]+\s*\=\=\s*60\s*\)\s*:\s*break\s*', code_string):
    is_break = True

if not is_continue:
    print("Please, use \"continue\" statement in your code", file=sys.stderr)
    sys.exit(0)

if not is_break:
    print("Please, use \"break\" statement in your code", file=sys.stderr)
    sys.exit(0)

print(json.dumps({ 'token': '{{token}}', 'passed': True }))