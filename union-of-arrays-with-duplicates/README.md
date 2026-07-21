# Union of Two Arrays

## Problem Summary

You are given two arrays `a[]` and `b[]`.

Your task is to return the **Union** of both arrays.

The **Union** of two arrays is a collection of all **distinct elements** that appear in either array.

If an element appears multiple times in one or both arrays, it should only appear **once** in the final result.

The order of the returned elements does not matter because the driver code will sort the answer before printing.

---

# Examples

## Example 1

### Input

```
a[] = [1, 2, 3, 2, 1]
b[] = [3, 2, 2, 3, 3, 2]
```

### Output

```
[1, 2, 3]
```

### Explanation

Combine both arrays:

```
[1,2,3,2,1,3,2,2,3,3,2]
```

Remove duplicates:

```
[1,2,3]
```

---

## Example 2

### Input

```
a[] = [1, 2, 3]
b[] = [4, 5, 6]
```

### Output

```
[1, 2, 3, 4, 5, 6]
```

### Explanation

There are no common elements, so every element from both arrays is included.

---

## Example 3

### Input

```
a[] = [1, 2, 1, 1, 2]
b[] = [2, 2, 1, 2, 1]
```

### Output

```
[1, 2]
```

### Explanation

The only distinct elements present are:

```
1 and 2
```

---

# Constraints

```
1 ≤ a.size(), b.size() ≤ 10^6

0 ≤ a[i], b[i] ≤ 10^5
```

Because the arrays can be very large, the solution should be efficient.

---

# Approach: Using Set

## Idea

A set is a data structure that automatically stores only unique elements.

Steps:

1. Create an empty set.
2. Add all elements from array `a`.
3. Add all elements from array `b`.
4. Convert the set into a list and return it.

---

# Python Solution

```python
class Solution:
    def findUnion(self, a, b):

        union = set()

        for num in a:
            union.add(num)

        for num in b:
            union.add(num)

        return list(union)
```

---

# Complexity Analysis

Let:

```
n = size of array a
m = size of array b
```

## Time Complexity

```
O(n + m)
```

Each element is processed once.

## Space Complexity

```
O(n + m)
```

The set stores the unique elements from both arrays.

---

# Common Mistakes

## Mistake 1: Simply Combining Arrays

Wrong:

```python
union = a + b
```

Example:

```
[1,2,3,2,1,3]
```

Duplicates remain.

---

## Mistake 2: Using a List for Duplicate Checking

Example:

```python
union = []

for num in a:
    if num not in union:
        union.append(num)
```

The problem:

Searching inside a list takes `O(n)` time.

For very large arrays, this becomes slow.

A set is better because checking membership is approximately:

```
O(1)
```

---

# Main Concept Learned

This problem teaches:

- How to remove duplicates.
- How sets work.
- How to combine collections.
- Choosing the correct data structure.

The main pattern:

```
Two arrays
     ↓
Combine elements
     ↓
Remove duplicates using set
     ↓
Return unique elements
```
