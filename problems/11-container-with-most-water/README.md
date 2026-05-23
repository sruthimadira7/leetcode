# Container With Most Water

## Problem Description

Given an integer array height of length n, where each element represents a vertical line at index i with height height[i].
Find two lines that form a container such that the container holds the most water.

### Key Constraints

---

1. Container is formed by **two vertical lines and the horizontal line at the bottom**
2. Water cannot tilt; **height is limited by the shorter of the two lines**
   You may not slant the container
3. Return the **maximum area of water that can be contained**

## APPROACH

1.  **Core Insight:** The area of container is calculated as:

        Area = (right - left) × min(height[left], height[right])

2.  **KEY INSIGHT:** We want maximum area. Starting from both ends
    gives us maximum width. As we move inward, width decreases, so
    we NEED taller walls to compensate.

3.  **GREEDY STRATEGY:** The shorter wall is the bottleneck—it limits
    the water level. Moving it inward has a CHANCE to find a taller
    wall. Moving the taller wall guarantees no improvement (width
    decreases, height won't improve).

4.  **ALGORITHM:**
    - Start with **pointers at both ends** => left at start, right at end
    - Calculate area with min(height[left], height[right]) × width
    - Update max_area if better
    - Move the **SHORTER pointer inward**
      - Why? The **shorter wall is the bottleneck**
      - Moving it might reveal a taller wall → potential area increase
      - Moving the taller wall guarantees no improvement (width ↓, height stays capped by shorter wall)
    - **Repeat until pointers meet**

---

## Complexity Analysis

**Time Complexity:** **O(n)**

    - Each pointer traverses the array at most once, starting from opposite ends.

**Space Complexity:** **O(1)**

    - Constant extra space independent of input size.
    - No additional data structures.

---
