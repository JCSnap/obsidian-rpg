import os
import re
from typing import Dict

def get_config_from_db(vault_path: str) -> Dict[str, str]:
    database_file = os.path.join(vault_path, "RLRPG/RLRPG Database.md")
    with open(database_file, "r") as db:
        config = {line.split("| ")[0]: line.split("| ")[1].strip() for line in db}
        return config

def get_task_pattern() -> re.Pattern:
    "Returns a pattern to match marked, description, gold"
    return re.compile(r"- \[([ x])\] (.+?)\s+`(-?\d+)`")
