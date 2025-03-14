<%*
const id = tp.file.title.split(" ")[0];
const createdDate = tp.file.creation_date('YYYY-MM-DD');
const updatedDate = tp.file.last_modified_date('YYYY-MM-DD');

// Define difficulty options
const difficultyOptions = ["easy", "medium", "hard"];
// Prompt user to select difficulty
const difficulty = await tp.system.suggester(difficultyOptions, difficultyOptions, false, "Select difficulty level");

// Construct YAML frontmatter
const yamlContent = `---
id: ${id}
created_date: ${createdDate}
updated_date: ${updatedDate}
type: leetcode
difficulty: ${difficulty}
---
`;

// Output YAML frontmatter
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

## 📝 Note
- 
## Run this code after you have completed the leetcode
```run-python
import subprocess

cur_file_path = @vault_path + "/" + @note_path
leetcode_title = @title

subprocess.run(["python3", @vault_path + "/process_leetcode.py", cur_file_path, @vault_path])

```