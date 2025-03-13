## Prebuilt functions
### add_coins.py
#### Accepts
- `gold_count`: str (amount of gold to add or deduct from account)
- `description`: string (reason of transaction)
- `vault_path`: the current vault path, can be gotten from running `@vault_path` within the code block
#### Behaviour
- Adds the amount of coin specified to the main page
- Logs the transaction in the transaction page with the format
> {date}: `+gold_count` (description)
#### Returns
`None`
#### How to run
```run-python
import subprocess

subprocess.run(["python3", @vault_path + "/add_coins.py", "-10", "completed lab 1", @vault_path])
```