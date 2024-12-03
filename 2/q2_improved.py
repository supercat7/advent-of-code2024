from os.path import dirname

# Read input from file
with open(f"{dirname(__file__)}/input.txt", "r") as file:
    lines = file.read().splitlines()

def is_safe_report(arr):
    """Check if the report is strictly increasing/decreasing with valid distances."""
    return (
        all(0 < (arr[i + 1] - arr[i]) < 4 for i in range(len(arr) - 1)) or
        all(0 < (arr[i] - arr[i + 1]) < 4 for i in range(len(arr) - 1))
    )

def is_safe_with_removal(arr):
    """Check if removing one element makes the report safe."""
    for i in range(len(arr)):
        modified_report = arr[:i] + arr[i + 1:]
        if is_safe_report(modified_report):
            return True
    return False

def is_safe(arr):
    """Check if the report is safe, either as-is or after removing one element."""
    return is_safe_report(arr) or is_safe_with_removal(arr)

# Parse input and count safe reports
safe_report_num = sum(1 for line in lines if is_safe(list(map(int, line.split()))))

print(safe_report_num)
