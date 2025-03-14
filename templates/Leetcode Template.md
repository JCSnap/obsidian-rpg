<%*
const id = tp.file.title.split(" ")[0];
const createdDate = tp.file.creation_date('YYYY-MM-DD');
const updatedDate = tp.file.last_modified_date('YYYY-MM-DD');

const difficultyOptions = ["easy", "medium", "hard"];
const difficulty = await tp.system.suggester(difficultyOptions, difficultyOptions, false, "Select difficulty level");

const yamlContent = `---
id: ${id}
created_date: ${createdDate}
updated_date: ${updatedDate}
type: leetcode
difficulty: ${difficulty}
---
`;

tR += yamlContent;
%>
# 📚 <% tp.file.title %>
- **🏷️Tags** :   #<% tp.file.creation_date('MM-YYYY') %> #leetcode

## 💭 Approach
- 

## ✅ Suggested solution
```python
```

## 👨‍💻 Your solution
```python
```

## 📝 Notes
- 

## Run this code after you have completed the leetcode
```run-python
import subprocess

cur_file_path = @vault_path + "/" + @note_path
leetcode_title = @title

subprocess.run(["python3", @vault_path + "/process_leetcode.py", cur_file_path, @vault_path])

```