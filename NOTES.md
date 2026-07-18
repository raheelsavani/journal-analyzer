# Git Reference & Project Brief — journal-analyzer

## Git commands, what they do, and when to use them

### Everyday loop (you'll use these constantly)
```bash
git status              # what's changed since my last commit? (safe, run this often)
git add .                # stage ALL changed files for the next commit
git add <filename>       # stage just one file
git commit -m "message"  # save the staged changes as a permanent snapshot
git push                 # send commits to GitHub (needs internet)
git pull                 # fetch + merge changes from GitHub (needs internet)
```
**The mental model:** `add` builds up what you *want* to commit (staging area).
`commit` takes a snapshot of everything currently staged, with a caption (`-m`).
`push` sends that history to GitHub. None of the first three need internet — only `push`/`pull` do.

**Multi-file workflow (current approach):** you don't have to add/commit/push after
every single file change. You can stage and commit files separately (e.g. code first,
then notes), and batch multiple commits into a single `push` at the end:
```bash
git add journal_analyzer.py
git commit -m "add read-entries feature"
git add NOTES.md
git commit -m "update notes for step 4"
git push
```
Two commits, one push — push just sends whatever hasn't gone up yet, however many
commits are waiting.

### Checking things
```bash
git log                  # see commit history (hash, author, date, message)
git log --oneline        # same, but compact — one line per commit
git diff                 # see exact line-by-line changes not yet staged
git remote -v            # see what remote(s) this repo is connected to
```

### One-time setup (already done for this repo, here for reference)
```bash
git init                                  # turn a folder into a git repo (local only)
git remote add origin <url>               # point local repo at a GitHub repo (local only)
git push -u origin main                   # first push; links local main to origin main
```

### If you're stuck at a `dquote>` or similar prompt
Type `"` and hit enter to close the string, or `Ctrl+C` to force back to a clean prompt.
Usually caused by a missing closing quote or a typo'd flag (e.g. `~m` instead of `-m`).

### Handling merge conflicts (learned this the hard way)
If `git push` gets rejected with "fetch first," run `git pull` — this pulls down
remote changes so your local history can reconcile with GitHub's.
If pull says branches have "diverged," you'll need to pick a strategy once:
```bash
git config pull.rebase false   # merge strategy (recommended for solo projects)
git pull
```
If a conflict shows up on `.DS_Store` (a junk file macOS creates automatically,
unrelated to your code), just remove it and commit:
```bash
git rm .DS_Store
git commit -m "merge: remove .DS_Store"
git push
```
Worth adding `.DS_Store` to `.gitignore` eventually (see step 8 below) so this
doesn't recur.


## Project: Journal / Log Analyzer

A command-line app: write daily log entries to a text file, then read back
and analyze that file (word counts, longest entry, keyword search, etc.).
Uses every concept covered so far: loops, while/break, try/except/else/finally,
lists, string methods, f-strings, functions, and file I/O.

### Build order
1. **Setup** — git init, repo structure, first commit ✅ DONE
2. **Core loop** — while loop + menu (add entry / view entries / quit) using `break` ✅ DONE
3. **Writing entries** — `open()` in append mode, save entry to file ✅ DONE
4. **Reading entries back** — open file, print past entries ✅ DONE
5. **Analysis features** — word count, longest entry, keyword search
   (functions + string methods) ⬅️ NEXT
6. **Error handling** — try/except throughout (e.g. missing file on first run)
7. **Polish + README** — proper README describing the tool
8. **Git wrap-up** — meaningful commit history, maybe a `.gitignore`
   (add `.DS_Store` to it)

### Step 4 notes (new concepts learned, not from futurecoder)
- A file object opened with `open("entries.txt")` (no mode arg = defaults to `"r"`,
  read-only) is iterable — `for line in file:` loops over it one line at a time
- Each `line` already ends in `"\n"` (carried over from how entries were saved in
  step 3 with `.write(entry + "\n")`)
- `print()` also adds its own trailing `"\n"` by default — combined with the `"\n"`
  already in `line`, this produces a blank line between each printed entry
- `print()` has an `end` parameter (default `end="\n"`) that controls what gets
  printed after the given text — `print(line, end="")` suppresses print's own
  newline, removing the double-gap effect
- Decision: kept the double-newline gap (default `print(line)`, no `end` override) —
  it improves readability for a personal journal tool. Considered but explicitly
  rejected building a user-facing formatting choice (tight vs. spaced entries via
  an input prompt) — concluded the mechanics were easy but the feature added no
  real value for a single-user personal tool; not worth the complexity
- Current working view-entries code:
```python
  elif selection == "2":
      with open("entries.txt") as file:
          for line in file:
              print(line)
```

### Current full code (end of step 4)
```python
print("Welcome to your journal. Enter 1 to Add Entry, 2 to View Entries, 3 to Quit")

while True:
    selection = input("Please enter selection.  ").strip()
    if selection == "1":
        entry = input("Please type your entry here:  ")
        with open("entries.txt", "a") as file:
            file.write(entry + "\n")
    elif selection == "2":
        with open("entries.txt") as file:
            for line in file:
                print(line)
    elif selection == "3":
        print("Quitting Program")
        break
    else:
        print("Invalid Entry.")
```

### Working style reminder (for Claude, when we resume)
- Socratic / hint-based — nudge toward the answer, don't hand it over
- Walk through logic in plain English before any code
- Stay within concepts already covered in futurecoder lessons — but new gaps
  (like file-write/file-read mechanics) get taught directly first, then practiced
- If stuck, ask a guiding question rather than explaining the fix

### Git habit while building
Batch commits, don't have to push after every one. Pattern: modify code, modify
NOTES.md, then `git add <file>` + `git commit -m "..."` separately for each file
(code first, then notes), followed by a single `git push` at the end covering
both commits.