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

## File structure
- `RLRPG Main`: The "home screen" for your game. For QOL improvement, you can download the [homepage plugin](https://github.com/mirnovov/obsidian-homepage) and set your home page to this file
- `RLRPG Transactions` This will serve as a book-keeping for all your coins inflow and outflow (think a Bitcoin ledger)