## Prebuilt functions
### add_gold.py
#### Accepts
- `gold_count`: str (amount of gold to add or deduct from account)
- `description`: string (reason of transaction)
- `vault_path`: the current vault path, can be gotten from running `@vault_path` within the code block
#### Behaviour
- Adds the amount of gold specified to the main page
- Logs the transaction in the transaction page with the format
> {date}: `+gold_count` (description)
#### Returns
`None`
#### How to run
```run-python
import subprocess

subprocess.run(["python3", @vault_path + "/add_gold.py", "-10", "completed lab 1", @vault_path])
```

---
### process_tasks.py
#### Accepts
- `vault_path`: The current vault path, which can be retrieved by running `@vault_path` within the code block.
#### Behaviour
- Scans active and passive quests in `RLRPG Main.md`.
- Identifies completed tasks (marked `[x]`).
- Calls `add_gold.py` to add gold for completed tasks.
- Deletes completed active tasks.
- Resets completed passive tasks.
- Updates `RLRPG Main.md` to reflect changes.
#### Returns
`None`
#### How to run
```run-python
import subprocess

subprocess.run(["python3", @vault_path + "/process_tasks.py", @vault_path])
```

---
### process_leetcode.py
#### Accepts
- `leetcode_file_path`: The file path to the LeetCode markdown file.
- `vault_path`: The current vault path, which can be retrieved by running `@vault_path` within the code block.
#### Behaviour
- Reads the LeetCode markdown file to extract the difficulty level (`easy`, `medium`, or `hard`).
- Looks up the corresponding gold reward from `RLRPG Database.md` using difficulty-specific variables:
    - `leetcode_easy_gold`
    - `leetcode_medium_gold`
    - `leetcode_hard_gold`
- Calls `add_gold.py` to add gold for the completed LeetCode problem.
#### Returns
`None`
#### How to run
```run-python
import subprocess

subprocess.run(["python3", @vault_path + "/process_leetcode.py", "/path/to/leetcode_file.md", @vault_path])
```
---
### generate_analytics.py
#### Accepts
- `vault_path`: The current vault path, which can be retrieved by running `@vault_path` within the code block.
#### Behaviour
- Reads transaction history from `RLRPG Transactions.md` (or the configured transaction file).
- Extracts gold earnings over time from transactions.
- Generates an ASCII graph displaying cumulative gold accumulation.
- Normalizes the graph width based on terminal size and adjusts for a large number of data points.
#### Returns
`None`
#### How to run
```run-python
import subprocess

subprocess.run(["python3", @vault_path + "/generate_analytics.py", @vault_path])
```

---
### refresh_passive_quests.py
#### Accepts
- `vault_path`: The current vault path, which can be retrieved by running `@vault_path` within the code block.
#### Behaviour
- Reads checked passive quests from character pages.
- Extracts task name, gold value, and source for each checked passive quest.
- Overwrites the passive quests section in `RLRPG Main.md` with the updated passive quests from character pages.
- Ensures that only checked passive tasks are carried over, resetting them as unchecked `[ ]` in `RLRPG Main.md`.
#### Returns
`None`
#### How to run
```run-python
import subprocess

subprocess.run(["python3", @vault_path + "/refresh_passive_quests.py", @vault_path])
```
