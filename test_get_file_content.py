from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

result = get_file_content("calculator", "main.py")
print(f"main.py result: {result}")
print(f"main.py length: {len(result)}")
print(f"main.py truncated: {'truncated' in result}")

result = get_file_content("calculator", "pkg/calculator.py")
print(f"calculator.py result: {result}")
print(f"pkg/calculator.py length: {len(result)}")
print(f"pkg/calculator.py truncated: {'truncated' in result}")

result = get_file_content("calculator", "/bin/cat") # this should return an error string
print(result)

result = get_file_content("calculator", "pkg/does_not_exist.py") # this should return an error string
print(result)