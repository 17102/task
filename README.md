# task


---

# Machine Learning Intern Assignment - BOT Shreyasi

## Overview
This repository contains the solutions to the assignment tasks for the Machine Learning Intern role at BOT Shreyasi. The assignment consists of three tasks: a Python function to evaluate password strength, a Python function for prime factorization, and an SQL query design for retrieving posts made by friends.

## Task 1: Password Strength Evaluator

### File: `password_strength.py`

### Function: `evaluate_password_strength(password)`

### Description:
The function `evaluate_password_strength` takes a password string as input and returns a strength score. The score is calculated based on several criteria:
- **Length**: Passwords with 8 or more characters score higher.
- **Character Type**: Inclusion of both uppercase and lowercase letters, numbers, and special characters contribute to a higher score.

### Example:
```python
from password_strength import evaluate_password_strength

print(evaluate_password_strength("StrongP@ssw0rd"))  # Output: 8
```

## Task 2: Prime Factorization

### File: `prime_factorization.py`

### Function: `prime_factors(n)`

### Description:
The `prime_factors` function takes an integer as input and returns a list of tuples, where each tuple contains a prime factor and its corresponding exponent. This represents the prime factorization of the integer.

### Example:
```python
from prime_factorization import prime_factors

print(prime_factors(60))  # Output: [(2, 2), (3, 1), (5, 1)]
```

## Task 3: SQL Query Design

### File: `query.sql`

### Description:
The SQL query in `query.sql` retrieves posts made by friends of a given user from a social media platform's `posts` table. It assumes the existence of a `friends` table that stores the relationships between users and their friends.

### SQL Query:
```sql
SELECT p.*
FROM posts p
JOIN friends f ON p.user_id = f.friend_id
WHERE f.user_id = <current_user_id>;
```

## Setup and Running the Code

### Prerequisites:
- Python 3.x installed on your system.

### Instructions:
1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Run the Python Scripts:**
    - To evaluate password strength:
        ```bash
        python3 password_strength.py
        ```
    - To perform prime factorization:
        ```bash
        python3 prime_factorization.py
        ```

3. **SQL Query:**
   - Open the `query.sql` file and adapt the query to your specific database schema.

### Testing:
Ensure to test the functions with various inputs to validate the correctness and efficiency of the code.

## Assumptions:
- The password evaluator assumes that passwords shorter than 6 characters are weak.
- The prime factorization function assumes the input is a positive integer greater than 1.
- The SQL query assumes the existence of `posts` and `friends` tables with appropriate fields.

## Contact:
For any queries or additional information, please feel free to reach out.

---


