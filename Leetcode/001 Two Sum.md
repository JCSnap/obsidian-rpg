---
id: 001
created_date: 2025-03-15
updated_date: 2025-03-15
type: leetcode
difficulty: easy
---

# 📚 001 Two Sum
- **🏷️Tags** :   #03-2025 #leetcode
## 💭 Approach
- iterate

## ✅ Suggested solution
```python
```

## 👨‍💻 Your solution
```python
class Solution(object):
    def twoSum(self, nums, target):
        numToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            else:
                numToIndex[nums[i]] = i

```

## 📝 Note
- 

## Run this code after you have completed the leetcode
```run-python
import subprocess

cur_file_path = @vault_path + "/" + @note_path
leetcode_title = @title

subprocess.run(["python3", @vault_path + "/process_leetcode.py", cur_file_path, @vault_path])

```