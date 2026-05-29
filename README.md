# 🚀 Kanan Sangal - GL Bajaj Summer Assignments 2026, 25113CN364.

A comprehensive repository tracking my daily progress through foundational programming logic, algorithmic problem-solving, and core software engineering concepts during the undergraduate summer term.

## 🛠️ Local Environment Execution Setup

To compile and execute any C file in this repository locally, open your terminal/command prompt inside the specific day's folder and execute the appropriate shortcut:

* **🍏 macOS:** `gcc ques_1.c -o output && ./output`
* **🪟 Windows:** `gcc ques_1.c -o output.exe && output.exe` *(Requires **MinGW** GCC compiler toolchain installed and added to system Environment Variables).*

---

## 📅 Day-Wise Assignment Tracker

| Day | Challenge Details | Solved Folder | Key Engineering Concepts Covered | Target Companies |
| :--- | :--- | :--- | :--- | :--- |
| [**Day 1**](./Day_1/) | • **Q1:** Calculate Sum of First N Natural Numbers<br>• **Q2:** Print Multiplication Table of a Number<br>• **Q3:** Find Factorial of a Number<br>• **Q4:** Count Digits in a Number | [📁 Day_1](./Day_1/) | Input validation validation, tracking buffers, avoiding loop mutations, managing integer bounds | TCS, Infosys, Wipro |
| [**Day 2**](./Day_2/) | • **Q5:** Find Sum of Digits of a Number<br>• **Q6:** Reverse a Number<br>• **Q7:** Find Product of All Digits<br>• **Q8:** Check if a Number is a Palindrome | [📁 Day_2](./Day_2/) | Digit extraction using Modulo (`% 10`) and Integer Division (`/ 10`), Numeric Reconstruction, Value Preservation | TCS, Infosys, Wipro |
| [**Day 3**](./Day_3/) | • **Q9:** Check Whether a Number is Prime<br>• **Q10:** Print Prime Numbers in a Range<br>• **Q11:** Find GCD of Two Numbers<br>• **Q12:** Find LCM of Two Numbers | [📁 Day_3](./Day_3/) | Loop state tracking, single-line empty loops, Euclidean Algorithm properties, linear step-wise search optimization | TCS, Infosys, Wipro |
| **Day 4** | *Coming soon...* | — | — | — |

---

## 🧠 Core Logic Blueprints Mastered

### 🍏 Day 1: Inputs & Number Limits

#### 1. Input Validation (`scanf() == 0`)
* **The Problem:** Entering a non-numeric character (e.g., `'k'`) when `scanf("%d", &num)` expects an integer leaves that character trapped in the `stdin` buffer stream. Inside a loop, this causes an immediate infinite execution spiral.
* **The Fix:** Checking `if (scanf("%d", &num) == 0)` intercepts the mismatched data state instantly, allowing the program to throw a clear error and terminate safely (`return 1`).

#### 2. 32-Bit Bounds (Integer Overflow)
* **The Problem:** A standard signed `int` caps at roughly **2.14 Billion** ($2,147,483,647$). Inputs exceeding this hardware memory capacity cause data overflows, forcing variables into unexpected default error values (e.g., `-1`) and corrupting loop math.
* **The Fix:** Constrain experimental test inputs to under 2.14 Billion, or upgrade variables to a 64-bit `long long int` (using `%lld`) to expand storage capacity up to 19 digits.

#### 📋 Challenge Matrix Implementations:
* **Q1 (Sum of Natural Numbers):** Use a `for` loop running from `1` to `N`, adding the loop control variable `i` to a running `sum` tracker on every iteration.
* **Q2 (Multiplication Table):** Run a `for` loop exactly 10 times (`1` to `10`), multiplying the user's input number by the loop index `i` inside each print statement.
* **Q3 (Factorial of a Number):** Initialize a `fact` variable to `1`, then run a loop from `1` up to `N`, continuously multiplying `fact *= i` to accumulate the product.
* **Q4 (Count Digits):** Use a `while (num != 0)` loop to continuously strip the rightmost digit using integer division (`num /= 10`), incrementing a `count` variable on each chop until the number hits `0`.

---

### 🔄 Day 2: The Digit Extraction Engine (`% 10` & `/ 10`)

All Day 2 challenges were executed by running a highly optimized two-step math pattern inside a `while (num != 0)` block to peel off and isolate integers right-to-left:

1. **The Digit Puller (`num % 10`):** Evaluates the division remainder to isolate the **absolute last digit** on the right. (e.g., `789 % 10` $\rightarrow$ **`9`**).
2. **The Digit Chopper (`num / 10`):** Uses integer division truncation to slide the number right and **drop the last digit**. (e.g., `789 / 10` $\rightarrow$ **`78`**). This acts as the loop modifier until the value reaches `0`.

#### 📋 Challenge Matrix Implementations:
* **Q5 (Sum of Digits):** Isolate the last digit with `% 10`, add it to a running `sum`, and shrink the number with `/ 10`.
* **Q7 (Product of Digits):** Isolate the last digit with `% 10`, multiply it into a running `product` (initialized to `1`), and shrink the number with `/ 10`.
* **Q6 (Reverse a Number):** Isolate the last digit with `% 10`, shift the total left (`rev = rev * 10 + rem`) to place the digit, and shrink the number with `/ 10`.
* **Q8 (Palindrome Check):** Backup the original value (`backup = num`), run the Q6 reversal logic, and check if the final `rev == backup`.

---

### 🧩 Day 3: Primes & Common Divisor Engines

#### 1. Single-Line Loop Verification & State Tracking
* **The Concept:** Traditional primality tracking uses state flags (`flag = 0/1`). By consolidating the evaluation conditions into a single loop statement (`for (j = 2; j < num && num % j != 0; j++);`), the final execution boundary of the controller index variable (`if (j == num)`) explicitly confirms primality without external state mutations.

#### 2. The Euclidean Property ($\text{GCD}(a, b) = \text{GCD}(b, a \pmod b)$)
* **The Concept:** Instead of computing all matching components linearly, dividing the primary value by the subset and cascading the resulting remainder reduces numerical bounds exponentially, resolving the Greatest Common Divisor efficiently inside a simple `while (b != 0)` loop without heavy spatial arrays or structural fallback chains.

#### 📋 Challenge Matrix Implementations:
* **Q9 (Check Prime):** Evaluate a target number across an internal factor loop starting from `2` up to `num - 1`. If no composite divisors are hit, confirm primality.
* **Q10 (Prime Range Search):** Construct a wrapped range loop executing the internal prime evaluator sequentially across a target matrix while implementing a persistent outer range counter to handle blank output defaults.
* **Q11 (GCD Engine):** Execute successive remainder reductions swapping current parameters (`rem = a % b; a = b; b = rem;`) dynamically until the evaluation floor reaches `0`.
* **Q12 (Formula-Free LCM Search):** Establish the maximum number as a core scale variable (`max`), implementing a step-wise search scaling sequentially in factor increments (`lcm += max`) until a mutual division verification step satisfies both constraints.

---