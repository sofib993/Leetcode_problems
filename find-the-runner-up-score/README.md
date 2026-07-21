# Find the Runner-Up Score! (Python)

Given the scores of participants in a University Sports Day, find the **runner-up score** (the second highest **distinct** score).

## 📖 Problem Statement

You are given a list of participant scores. Store the scores in a list and determine the runner-up score.

The runner-up score is the **second highest unique score**, meaning duplicate highest scores should be ignored.

---

## 🎯 Task

Given a list of integer scores:

1. Find the highest score.
2. Remove all occurrences of the highest score.
3. Print the next highest score.

---

## 📝 Input Format

- The first line contains an integer `n`, the number of participants.
- The second line contains `n` space-separated integers representing the participants' scores.

---

## 📤 Output Format

Print the runner-up score.

---

## 📥 Sample Input

```text
5
2 3 6 6 5
```

### Sample Output

```text
5
```

### Explanation

The given scores are:

```text
[2, 3, 6, 6, 5]
```

The highest score is:

```text
6
```

After removing all occurrences of `6`, the remaining scores are:

```text
[2, 3, 5]
```

The highest remaining score is:

```text
5
```

Therefore, the runner-up score is:

```text
5
```

---

## 💻 Solution

```python
if __name__ == "__main__":
    n = int(input())
    scores = list(map(int, input().split()))

    highest = max(scores)

    while highest in scores:
        scores.remove(highest)

    print(max(scores))
```

---

## 🧠 Concepts Used

- Lists
- `max()`
- `remove()`
- Loops
- User Input

---

## ⏱️ Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## 🚀 Alternative Solution

Using a set to remove duplicates:

```python
n = int(input())
scores = list(map(int, input().split()))

unique_scores = sorted(set(scores))
print(unique_scores[-2])
```

This solution first removes duplicate scores using a `set`, sorts the unique values, and prints the second largest score.
