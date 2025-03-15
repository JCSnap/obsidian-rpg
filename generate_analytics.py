import sys
import re
from collections import defaultdict
import shutil

if len(sys.argv) != 2:
    print("Usage: generate_analytics.py <vault_path>")
    sys.exit(1)

vault_path = sys.argv[1]

database_file = vault_path + "/RLRPG/RLRPG Database.md"
with open(database_file, "r") as db:
    config = {line.split("| ")[0]: line.split("| ")[1].strip() for line in db}

transaction_file = config.get("transaction_file_name")
folder = config.get("folder", "")
folder = "/" + folder if folder else folder

if not transaction_file:
    print("Could not find transaction file")
    sys.exit(1)

transaction_file_path = vault_path + folder + "/" + config.get("transaction_file_name")
analytics_file_path = vault_path + folder + "/" + config.get("analytics_file_name")

def plot_gold_ascii(date_to_gold, analytics_file_path):
    dates = sorted(date_to_gold.keys())
    gold_values = [date_to_gold[date] for date in dates]

    cumulative_gold = []
    total_gold = 0
    for gold in gold_values:
        total_gold += gold
        cumulative_gold.append(total_gold)

    terminal_width = shutil.get_terminal_size((80, 20)).columns
    graph_width = terminal_width - 20  # Padding for axis labels

    num_days = len(dates)
    if num_days > graph_width:
        step = num_days // graph_width
        reduced_dates = [dates[i] for i in range(0, num_days, step)]
        reduced_gold = [cumulative_gold[i] for i in range(0, num_days, step)]
    else:
        reduced_dates = dates
        reduced_gold = cumulative_gold

    # Normalize Y-axis (gold values)
    max_gold = max(reduced_gold, default=1)
    min_gold = min(reduced_gold, default=0)
    max_label_width = len(str(max_gold))
    y_step = max(1, (max_gold - min_gold) // 5) # scale

    y_labels = list(range(min_gold, max_gold + y_step, y_step))

    # Normalize cumulative gold values
    scaled_gold = [
        int(((gold - min_gold) / (max_gold - min_gold)) * (len(y_labels) - 1))
        if max_gold > min_gold else 0
        for gold in reduced_gold
    ]

    left_offset = max_label_width + 1
    graph_output = []

    graph_output.append("### Gold Accumulation Over Time\n")
    graph_output.append("```\n")
    graph_output.append("+" + "-" * (graph_width + left_offset) + "+\n")  # Top border

    # From bottom to top
    for y in reversed(y_labels):  # Reverse to make 0 at the bottom
        row = [" "] * graph_width
        for i, gold in enumerate(scaled_gold):
            position = int(i * (graph_width - 1) / max(1, len(reduced_dates) - 1))
            if gold == y_labels.index(y):
                row[position] = "*"

        graph_output.append(f"{y:>{max_label_width}} |" + "".join(row) + "|\n")  # Left Y-axis labels

    graph_output.append("+" + "-" * (graph_width + left_offset) + "+")  # Bottom border

    start_date = dates[0] if dates else ""
    end_date = dates[-1] if len(dates) > 1 else start_date
    x_axis_label = f"{start_date}{' ' * (graph_width - len(start_date) - len(end_date))}{end_date}"

    graph_output.append(" " * 5 + x_axis_label + "\n")
    graph_output.append("```\n")

    with open(analytics_file_path, "r") as f:
        lines = f.readlines()

    analytics_index = None
    analytics_start = config.get("analytics_start")
    for i, line in enumerate(lines):
        if line.strip() == analytics_start:
            analytics_index = i
            break

    open_with = "w"
    if analytics_index is not None:
        new_content = lines[:analytics_index + 1] + ["\n"] + graph_output + ["\n"]
    else:
        open_with = "a"
        new_content = [f"{analytics_start}\n"] + graph_output + ["\n"]

    with open(analytics_file_path, open_with) as f:
        f.writelines(new_content)


with open(transaction_file_path, "r") as f:
    date_to_gold = defaultdict(int)

    for line in f:
        date = line.split(": ")[0]
        gold_change = int(re.search(r'`(.*?)`', line).group(1))
        date_to_gold[date] += gold_change
    plot_gold_ascii(date_to_gold, analytics_file_path)

