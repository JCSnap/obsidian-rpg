## Items
Gold: `67`

## Active Quests
- [ ] Submit application for XXX Program `10`

## Passive Quests (pinned)
- [ ] Spend < $10 for the day `5`
- [ ] Consume < 1.6k calories for the day `10`
- [ ] Go to the gym `10`
- [ ] Walk > 5k steps `5`
- [ ] Drink 3 bottles of water `5`

## Character Pages
[[RLRPG Academics]]
[[RLRPG Career]]
[[RLRPG Finance]]
[[RLRPG Health]]
[[RLRPG Life]]

### Refresh passive quests
You can create recurring quests within your character pages. Check the ones you want to pin in the homepage. Run the code below to refresh your home page with the new quests.

```run-python
import subprocess
vault_path = @vault_path
subprocess.run(["python3", vault_path + "/refresh_passive_quests.py", vault_path])
```

### Run this code when you are done for the day

```run-python
import subprocess
vault_path = @vault_path
subprocess.run(["python3", vault_path + "/process_tasks.py", vault_path])
```/n/n/n/n/n/n/n/n/n/n