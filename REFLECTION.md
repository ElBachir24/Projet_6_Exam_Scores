# Team Reflection & Debugging Log

## Team Contributions & Role Breakdown
- **Leader / Member 5 (Diouf Mouhamed El Bachir)**: Integrated all functions into `project.py`, structured the `main()` execution block, set up the Git/GitHub repository, and authored the documentation.
- **Member 1 (Ousseynou Sow)**: Implemented the `mean()` and `median()` statistical functions.
- **Member 2 (MINGANE GRACIA)**: Developed `mode()` using frequency dictionaries and `std_dev()` for score dispersion.
- **Member 3 (Dlamini Sandziso Siyabonga)**: Created the `outliers()` detection function based on standard deviations.
- **Member 4 (Nusaiba Alrasheed Osman Alfaki)**: Built the `grade_histogram()` extra feature and class comparison logic.

## Challenges Encountered & Bugs Resolved

### 1. Loop Structure in Median Calculation (Member 1: Ousseynou Sow)
- **Issue**: The initial `median()` implementation contained an unnecessary `for` loop wrapping the parity check (`if/else`).
- **Fix**: Removed the loop to ensure direct indexing using integer division (`mid = n // 2`).

### 2. Global State Pollution in Outliers (Member 2: MINGANE GRACIA)
- **Issue**: The outlier list was initially instantiated as a global variable outside the function, causing scores from previous class checks to accumulate.
- **Fix**: Encapsulated `outlier_list = []` inside the local function scope to maintain state independence.

### 3. External Module Constraint Violation (Member 3: Dlamini Sandziso Siyabonga)
- **Issue**: An external module (`import math as aims`) was used for square root operations, violating project constraints. Additionally, `outlier.append(aims)` appended the module object instead of the score.
- **Fix**: Removed `math` import, replaced `sqrt` with exponentiation `** 0.5`, and correctly appended `score`.

### 4. Cumulative Sum Error in Variance Calculation (Member 4: Nusaiba Alrasheed Osman Alfaki)
- **Issue**: Variance calculation used `total = (score - m) ** 2` instead of accumulating values, overwriting the total on each iteration.
- **Fix**: Updated the loop to use accumulation (`sum_squares += (score - m) ** 2`).
