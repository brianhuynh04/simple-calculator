# CodeScribe Calculator
This project is a simple calculator demonstrating basic arithmetic operations and serving as a demo repository for CodeScribe agent reviews.

## Overview
This project provides a foundational set of arithmetic functions, designed to be a clear and understandable baseline. It serves as the initial module for the CodeScribe demo repository, illustrating how new features are introduced and reviewed through separate modules and pull requests.

## Architecture
The system employs a modular architecture, where core calculator functionalities are separated into distinct Python modules. The primary calculator.py module provides fundamental arithmetic operations, acting as the stable base. New, expanded operations are introduced in separate modules, such as expanded_calc_ops_20260511-182232.py and more_calc_ops_20260511-190128.py, allowing for isolated development and review. This separation facilitates a clear distinction between stable core features and ongoing development.

Key components:
- calculator.py: This module contains the essential arithmetic functions like addition, subtraction, multiplication, and division. It also includes a main function to demonstrate its usage.
- expanded_calc_ops_20260511-182232.py: This module introduces additional mathematical operations such as percentage calculation, range checking, and square root computation. It represents new features being added to the calculator.
- more_calc_ops_20260511-190128.py: This module provides further mathematical operations, including computing averages, adjusting values by one percent, and halving numbers. It demonstrates ongoing feature expansion.
- test_calculator.py: This module houses the unit tests for the functions defined in calculator.py, ensuring the correctness and reliability of the core arithmetic operations.

The data flow is straightforward. A user or another program calls a specific function from either calculator.py, expanded_calc_ops_20260511-182232.py, or more_calc_ops_20260511-190128.py, providing input values. The function then performs the requested calculation and returns the result. The test module verifies these operations by providing predefined inputs and asserting the expected outputs.

## Features
- Basic Arithmetic Operations: Perform addition, subtraction, multiplication, and division.
- Error Handling for Division: Prevents division by zero with a specific error.
- Expanded Mathematical Operations: Includes functions for calculating percentages, checking if a value is within a specified range, computing square roots, calculating the arithmetic mean of a list of numbers, adding one percent to a value, and halving a number.
- Unit Testing: Comprehensive tests for core arithmetic functions to ensure reliability.

## How It Works
The CodeScribe Calculator operates by exposing individual functions for each mathematical operation. When the main function in calculator.py is executed, it demonstrates the use of these core arithmetic functions by printing the results of predefined calculations. For expanded operations, functions within expanded_calc_ops_20260511-182232.py and more_calc_ops_20260511-190128.py can be imported and called directly to perform more specialized calculations. The test_calculator.py module imports functions from calculator.py and runs a series of assertions to confirm that each operation produces the correct output for various inputs, including testing error conditions like division by zero.

## Installation

Prerequisites: Python 3.6+ is required to run this project. The pytest library is needed for running tests.

Step-by-step installation:
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies

Commands:
```bash
git clone <repository-url>
cd codescribe-calculator
pip install pytest
```

## Usage

To run the main demonstration of the basic calculator operations:
```bash
python calculator.py
```

To use the functions in your own Python script, you can import them:
```python
from calculator import add, subtract
from expanded_calc_ops_20260511-182232 import percentage, square_root
from more_calc_ops_20260511-190128 import compute_average, add_one_percent, half

result_add = add(5, 7)
result_percent = percentage(25, 100)
result_sqrt = square_root(16)
result_average = compute_average([10, 20, 30])
result_plus_one_percent = add_one_percent(100)
result_half = half(50)

print(f"5 + 7 = {result_add}")
print(f"25 is {result_percent}% of 100")
print(f"Square root of 16 is {result_sqrt}")
print(f"Average of [10, 20, 30] is {result_average}")
print(f"100 plus one percent is {result_plus_one_percent}")
print(f"Half of 50 is {result_half}")
```

## Project Structure

The codebase is organized with a clear separation of concerns. The root directory contains all the Python modules. The primary calculator.py module defines the fundamental operations. New features are introduced in separate modules, such as expanded_calc_ops_20260511-182232.py and more_calc_ops_20260511-190128.py, to facilitate modular development and review processes. Testing for the core functionality is handled in a dedicated test file.

Important files:
- calculator.py: This is the core module containing basic arithmetic functions and a demonstration entry point.
- expanded_calc_ops_20260511-182232.py: This module provides additional, more advanced mathematical operations.
- more_calc_ops_20260511-190128.py: This module introduces further mathematical operations like averaging, percent adjustment, and halving.
- test_calculator.py: This module contains unit tests to verify the correctness of the functions in calculator.py.

## Technology Stack
- Python: The primary programming language used for all modules and scripts. Python was chosen for its readability, extensive libraries, and suitability for scripting and rapid development.
- pytest: A robust testing framework used for writing and running unit tests. pytest was selected for its simplicity, powerful features, and clear test reporting, which helps ensure the reliability of the calculator functions.

These technologies work together to provide a functional and testable calculator application. Python handles the core logic, while pytest ensures the integrity of the arithmetic operations.

## Development

To run the unit tests for the calculator module:
```bash
pytest
```

## Contributing
Contributions are welcome, especially those demonstrating new features or improvements that can be reviewed by CodeScribe agents.

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes, ensuring they adhere to the existing code style.
4. Write appropriate unit tests for new functionality or changes.
5. Ensure all existing tests pass