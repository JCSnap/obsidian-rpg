## Items
Gold: `0`

## Active Quests
- [ ] Finish assignment 1 for CS0000  `20`
- [ ] Submit application for XXX Program `10`

## Passive Quests (pinned)
- [ ] Consume < 1.9k calories for the day `10`
- [ ] Walk 5k steps `5`
- [ ] Drink 3 bottles of water `5`
- [ ] Read 3 articles `10`

## Character Pages
[[RLRPG Academics]]
[[RLRPG Career]]
[[RLRPG Finance]]
[[RLRPG Health]]
[[RLRPG Life]]

```run-python
vault_path = @vault_path
database_file_title = 'RLRPG Database.md'
database_path = vault_path + "/RLRPG/" + database_file_title

with open(database_path, "r") as db:
	  config = {line.split(": ")[0]: line.split(": ")[1].strip() for line in db}
	  print(config)
	  print(vault_path)
```

```run-python
import subprocess
vault_path = @vault_path
pa = vault_path + "/RLRPG/scripts/hello.py"

subprocess.run(["python3", pa, vault_path])
```