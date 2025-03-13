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

``