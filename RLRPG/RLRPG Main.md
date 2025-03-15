## Items
Gold: `67`

## Active Quests
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

### Run this code when you are done for the day

```run-python
import subprocess
vault_path = @vault_path
subprocess.run(["python3", vault_path + "/process_tasks.py", vault_path])
```