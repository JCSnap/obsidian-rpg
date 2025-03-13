## RPG in Obsidian
This is an example template to make your Obsidian workflow more dynamic. To demonstrate this, we will be "gamifying" our todo-list into an RPG.

The premise is simple - complete tasks to earn coins

## How this works?
1. File created in Obsidian are stored locally as `.md` files
2. There is an Obsidian [plugin](https://github.com/twibiral/obsidian-execute-code) that can allow you to execute code blocks written in Obsidian (basically turning your `.md` files into jupyter notebooks)

This means that we can create python code blocks that acts like "buttons" to do things like this!
```
// open up `Main.md`
// check if tasks are completed
// if completed, open up inventory file and add coins
```

Except you do not have to manually create the scripts since it will be provided by this template

## Todo-list
In Your `RLRPG Main`, there are 3 main sections:
1. Your gold count
2. Your active tasks
3. Your passive tasks

Active tasks are one-time off tasks meant to be completed. Passive tasks are recurring tasks that once completed, will be reset the next day. You can add your own tasks and the gold count associated with each task in an inline code block `like this`

At the end of the day, run the code at the end of the `RLRPG Main` file. It will go through all your tasks.
1. Add gold for completed tasks, log the transactions in `RLRPG Transactions`
2. Delete completed active tasks, reset completed passive tasks

## Main File structure
- `RLRPG Main`: The "home screen" for your game. For QOL improvement, you can download the [homepage plugin](https://github.com/mirnovov/obsidian-homepage) and set your home page to this file
- `RLRPG Transactions` This will serve as a book-keeping for all your coins inflow and outflow (think a Bitcoin ledger)
- `RLRPG Database`: The source of truth for all variables (actually more like pointers to source of truth)?
- `RLRPG Skill Tree`: Contain links to resources for the important skills you want to develop. Contain quests for you to earn gold
- The character files like `RLRPG Academics` and `RLRPG Health` etc. will contain important links, information and quests related to that aspect
- `RLRPG Scripts`: Contains API documentation for some of the functions behind the hood. You only need to care about this if you are intending to extend this template and implement your own automation

## Skill Tree
You can create your own skill tree and define tasks which when completed, will add gold and experience points to your skill (enough experience points will cause your level for the skill to increase)