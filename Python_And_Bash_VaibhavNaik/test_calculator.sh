#!/bin/bash

# Bash script to test the Python calculator functions

echo "Running calculator tests..."
echo "--------------------------"

python3 - <<'PY'
from calculator import add, subtract, multiply, divide

assert add(10, 5) == 15
assert subtract(10, 5) == 5
assert multiply(10, 5) == 50
assert divide(10, 5) == 2

assert divide(10, 0) == "Error: Cannot divide by zero."

print("Addition test: PASS")
print("Subtraction test: PASS")
print("Multiplication test: PASS")
print("Division test: PASS")
print("Division by zero test: PASS")
PY

echo "--------------------------"
echo "All tests completed."