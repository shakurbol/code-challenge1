# Toy Problems - Phase 3 Week 1
Overview
This repository contains solutions to three toy problems implemented in Python. Each challenge is designed to test different aspects of programming logic and problem-solving skills.

# Challenges
# Challenge 1: Converting 12-hour time to 24-hour time
Description
Convert a 12-hour time to 24-hour time format.

Function Signature
python
Copy code
def convert_to_24_hour(hour: int, minute: int, period: str) -> str:
    # Your implementation here
Example
python
Copy code
convert_to_24_hour(8, 30, "am")  # Returns "0830"
convert_to_24_hour(8, 30, "pm")  # Returns "2030"
# Challenge 2: Two numbers are positive
Description
Determine if exactly two out of three given integers are positive.

Function Signature
python
Copy code
def two_positive(a: int, b: int, c: int) -> bool:
    # Your implementation here
Example
python
Copy code
two_positive(2, 4, -3)  # Returns True
two_positive(-4, 6, 8)  # Returns True
two_positive(4, -6, 9)  # Returns True
two_positive(-4, 6, 0)  # Returns False
two_positive(4, 6, 10)  # Returns False
two_positive(-14, -3, -4)  # Returns False
# Challenge 3: Consonant value
Description
Find the highest value of consonant substrings in a given lowercase string.

Function Signature
python
Copy code
def consonant_value(s: str) -> int:
    # Your implementation here
Example
python
Copy code
consonant_value("zodiacs")  # Returns 26
consonant_value("strength")  # Returns 57
# Getting Started
Clone this repository.
 bash
Copy code
git clone https://github.com/your-username/toy-problems.git
 Navigate to the project directory.
bash
 Copy code
cd toy-problems
 Run the Python scripts to test the implemented functions.
bash
Copy code
python challenge1.py
python challenge2.py
python challenge3.py
