# Let me walk through my brute-force approach

1. I'll use **two nested loops** - an **outer loop** that **fixes one number**,and an that **compares it with every number to its right**.
   1. Why it works - "By starting j from i+1, we ensure we never use the same index twice"

2. For **each pair of numbers**, I'll **calculate their sum**.

3. If the **sum equals the target**, I'll **immediately return the indices
   of those two numbers**.

4. If **no pair is found**, I'll **return an empty array or indicate no solution** was found.

## Key points to mention while explaining

**Time Complexity:** **O(n²)** because of **nested loops**

**Space Complexity:** **O(1)** since we're only using constant extra space

---

## Optimal Approach

1. Use a **hashmap to store numbers and their indices** as we traverse:
   - **Key** = number value
   - **Value** = index position
2. For **each number** in the array:
   - Calculate the complement: `complement = target - current_number`
   - **Check if the complement exists** in the hashmap
   - If yes, return both indices **[hashmap[complement], current_index]**
   - If no, add the **current number and index to the hashmap**

- **Time Complexity:** O(n) - single pass through the array
- **Space Complexity:** O(n) - hashmap storage

---
