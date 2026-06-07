# 🚀 Kanan Sangal - GL Bajaj Summer Assignments 2026, 25113CN364.

A comprehensive repository tracking my daily progress through foundational programming logic, algorithmic problem-solving, and core software engineering concepts during the undergraduate summer term.

## 🛠️ Local Environment Execution Setup

To compile and execute any C file in this repository locally, open your terminal/command prompt inside the specific day's folder and execute the appropriate shortcut:

### 💻 Python Execution (Day 4+)
* **🍏 macOS / 🪟 Windows:** `python3 ques_25.py` ya `python ques_25.py`

### 🔌 C Execution (Day 1 - Day 3)
* **🍏 macOS:** `gcc ques_1.c -o output && ./output`
* **🪟 Windows:** `gcc ques_1.c -o output.exe && output.exe`

---

## 📅 Day-Wise Assignment Tracker

| Day | Challenge Details | Solved Folder | Key Engineering Concepts Covered | Target Companies |
| :--- | :--- | :--- | :--- | :--- |
|  **Day 1**  | • **Q1:** Calculate Sum of First N Natural Numbers<br>• **Q2:** Print Multiplication Table of a Number<br>• **Q3:** Find Factorial of a Number<br>• **Q4:** Count Digits in a Number | [Day_1](./Day_1/) | Input validation validation, tracking buffers, avoiding loop mutations, managing integer bounds | TCS, Infosys, Wipro |
|  **Day 2**  | • **Q5:** Find Sum of Digits of a Number<br>• **Q6:** Reverse a Number<br>• **Q7:** Find Product of All Digits<br>• **Q8:** Check if a Number is a Palindrome | [Day_2](./Day_2/) | Digit extraction using Modulo (`% 10`) and Integer Division (`/ 10`), Numeric Reconstruction, Value Preservation | TCS, Infosys, Wipro |
|  **Day 3**  | • **Q9:** Check Whether a Number is Prime<br>• **Q10:** Print Prime Numbers in a Range<br>• **Q11:** Find GCD of Two Numbers<br>• **Q12:** Find LCM of Two Numbers | [Day_3](./Day_3/) | Loop state tracking, single-line empty loops, Euclidean Algorithm properties, linear step-wise search optimization | TCS, Infosys, Wipro |
|  **Day 4**  | • **Q13:** Generate Fibonacci Series<br>• **Q14:** Find $n$th Fibonacci Term<br>• **Q15:** Check Armstrong Number<br>• **Q16:** Armstrong Numbers in Range | [Day_4](./Day_4/) | Python Floating-Point Division Trap (`/` vs `//`), Parallel Tuple Swapping, Multi-pass State Extraction, Range-bound Loops | TCS, Infosys, Wipro |
|  **Day 5**  | • **Q17:** Perfect Number Check<br>• **Q18:** Strong Number Check<br>• **Q19:** Print Factors<br>• **Q20:** Largest Prime Factor | [Day_5](./Day_5/) | Python Native `for-else` Control Structures, Reversed Step Iterations (`-1`), Dynamic List Accumulation, Strict Factorial Sweeps | TCS, Infosys, Wipro |
|  **Day 6**  | • **Q21:** Decimal to Binary Fraction<br>• **Q22:** Binary to Decimal<br>• **Q23:** Count Set Bits<br>• **Q24:** Custom Power ($x^n$) | [Day_6](./Day_6/) | Multi-variable assignments, Fractional string extraction, Sub-string element counters (`.count()`), Absolute negative exponent inversion | TCS, Infosys, Wipro |
|  **Day 7**  | • **Q25:** Recursive Factorial<br>• **Q26:** Recursive Fibonacci Series<br>• **Q27:** Recursive Sum of Digits<br>• **Q28:** Recursive Reverse Number | [Day_7](./Day_7/) | Call Stack Allocation, Functional Base Cases, Sub-problem Breakdowns, Absolute Sign Normalization (`abs()`) to avoid Infinite Stack Overflows | TCS, Infosys, Wipro |
| **Day 8** | *Coming soon...* | — | — | — |

---

## 🧠 Core Logic Blueprints Mastered

### 🍏 Day 1: Inputs & Number Limits

#### 1. Input Validation (`scanf() == 0`)
* **The Problem:** Entering a non-numeric character (e.g., `'k'`) when `scanf("%d", &num)` expects an integer leaves that character trapped in the `stdin` buffer stream. Inside a loop, this causes an immediate infinite execution spiral.
* **The Fix:** Checking `if (scanf("%d", &num) == 0)` intercepts the mismatched data state instantly, allowing the program to throw a clear error and terminate safely (`return 1`).

#### 2. 32-Bit Bounds (Integer Overflow)
* **The Problem:** A standard signed `int` caps at roughly **2.14 Billion** ($2,147,483,647$). Inputs exceeding this hardware memory capacity cause data overflows, forcing variables into unexpected default error values (e.g., `-1`) and corrupting loop math.
* **The Fix:** Constrain experimental test inputs to under 2.14 Billion, or upgrade variables to a 64-bit `long long int` (using `%lld`) to expand storage capacity up to 19 digits.

---

### 🔄 Day 2: The Digit Extraction Engine (`% 10` & `/ 10`)

#### 1. The Digit Puller Matrix (`num % 10`)
* **The Concept:** Traditional right-to-left scanning requires complex shifting. By evaluating the numeric division remainder under a base-10 modulo operation, the program isolates the absolute last digit on the right instantly (e.g., `789 % 10` $\rightarrow$ **`9`**) without mutating the core tracking value.

#### 2. The Digit Chopper Truncation (`num / 10` or `num // 10`)
* **The Concept:** Moving the pointer context across individual digit places requires dynamic array shrinking. Utilizing integer division truncation slides the entire numeric sequence to the right and drops the evaluated boundary digit (e.g., `789 / 10` $\rightarrow$ **`78`**), serving as the core loop modifier until the execution register hits `0`.

---

### 🧩 Day 3: Primes & Common Divisor Engines

#### 1. Single-Line Loop Verification & State Tracking
* **The Concept:** Traditional primality tracking uses state flags (`flag = 0/1`). By consolidating the evaluation conditions into a single loop statement (`for (j = 2; j < num && num % j != 0; j++);`), the final execution boundary of the controller index variable (`if (j == num)`) explicitly confirms primality without external state mutations.

#### 2. The Euclidean Property ($\text{GCD}(a, b) = \text{GCD}(b, a \pmod b)$)
* **The Concept:** Instead of computing all matching components linearly, dividing the primary value by the subset and cascading the resulting remainder reduces numerical bounds exponentially, resolving the Greatest Common Divisor efficiently inside a simple `while (b != 0)` loop without heavy spatial arrays or structural fallback chains.

---

### 🐍 Day 4: State Swapping & Python Numeric Architecture

#### 1. Python Floor Division (`//`) vs Float Division (`/`)
* **The Behavior:** In Python, the `/` operator defaults to float processing (e.g., `34 / 10 = 3.4`), leading to non-terminating structures in `while (num != 0)` digit-stripping blocks. 
* **The Solution:** Enforcing integer truncation via the `//` floor operator locks down accurate right-to-left mathematical extraction.

#### 2. Parallel Tuple Swapping (Deconstruction)
* **The Behavior:** Standard environments require auxiliary variable memory (`temp = a; a = b; b = temp;`) to safely execute sequence progressions.
* **The Solution:** Utilizing Python's inline evaluation processing (`a, b = b, a + b`) maps transformations concurrently, optimizing variable overhead.

---

### 🐍 Day 5: Control Structure Interception & Factor Selection

#### 1. Python Native `for-else` Engine Optimization
* **The Behavior:** Standard search loops use flag states (`found = False`) to trace short-circuits. Python's native `for-else` block executes the `else` track **only** if the structural block completely clears without encountering a `break`.
* **The Solution:** In Largest Prime Factor tracking (`ques_20.py`), evaluating internal structural boundaries under a strict `else` block instantly confirms prime status without using heavy tracking variables.

#### 2. Negative Baseline Boundary Scaling (`range` Steps)
* **The Behavior:** Default structural arrays move linearly upwards (`+1`). Moving backwards requires explicitly setting a negative step execution context (`range(num, 1, -1)`).
* **The Solution:** Starting from the absolute ceiling down to the floor allows us to pull out the maximum valid prime subset instantly on the first validation step.

---

### 🐍 Day 6: Base Transformations & Algorithmic Scalability

#### 1. Discrete Fraction Splitting and Continuous Matrix Multiplications
* **The Behavior:** Float conversions create multi-digit internal representation drops. Splitting strings over exact pivots (`.split('.')`) guarantees pure string data extraction without floating-point overflow.
* **The Solution:** Simultaneously extracting integer structures while performing fractional continuous multiplication by 2 allows highly precise float binary representation generation.

#### 2. Absolute Linear Scaling for Signed Exponents
* **The Behavior:** Standard loops break down when given negative index scales. 
* **The Solution:** Wrapping inputs inside structural absolute boundaries (`abs(n)`) and conditionally computing the inverse (`1 / ans`) solves negative power parameters mathematically without relying on the `pow()` API.

---

### 🐍 Day 7: Call Stacks & Recursive Execution Contexts

#### 1. Stack Depth Preservation & Absolute Value Normalization
* **The Behavior:** Recursive functions rely on a strict exit condition (Base Case). Negative integer parameters can bypass basic numeric floor boundaries due to language-specific floor division (`//`) rules, causing infinite recursion stack overflow crashes.
* **The Solution:** Implementing inline value normalization via absolute magnitude extraction (`abs(num)`) isolates digit structures from signs, safeguarding the call stack depth across negative domains.

#### 2. Sequential Decomposition vs. Discrete Accumulation
* **The Behavior:** Pure mathematical recursion rolls upward to return a single evaluation matrix. Generating a full progression trace (like a Fibonacci series) using tree-structured algorithms requires decoupling generation from output presentation.
* **The Solution:** Wrapping structural tree logic inside a decoupled step-wise iteration loop allows individual extraction of discrete positional states sequentially.

---