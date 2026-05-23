# What is a Palindrome Number ?

- A number that reads the same from forward and backward.

## How to find whether the given number is a Palindrome or not ?

- If I find the reverse of the given number, then the given number and it's reverse are equal then we can say the given number is palindrome.

---

## How should I approach this ?

Core Idea : Reverse only the second half of the number and compare it with the first half.
This approach avoids string conversion overhead and potential integer overflow from fully reversing large numbers

### Step 1: Check Edge Cases

---

1. Negative numbers cannot be palindromes
2. Numbers ending with 0 cannot be palindromes (except 0 itself)

### Step 2: Reverse the Second Half

---

1.  Initailize a variable named **reverse_x** to **zero.**
2.  Use a **while loop** with condition **x > reverse_x**
3.  Extract the **last digit of x** using **x % 10**
4.  **Build the reverse_x:**

        reverse_x = reverse_x * 10 + x % 10

5.  **Remove the last digit from x:**

        x = x // 10

6.  **Stop when we've processed half the digits (when x ≤ reverse_x)**

### Step 3: Compare Halves

---

1. For **even-length** numbers: Check if x == reverse_x
2. For **odd-length** numbers: Check if x == reverse_x // 10 (middle digit ignored)

---
