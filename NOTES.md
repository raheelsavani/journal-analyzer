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
`commit` locks it into local history. `push` sends that history to GitHub.
None of the first three need internet — only `push`/`pull` do.

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

---

## This machine's setup (as of Jul 17, 2026)
- Git version: 2.50.1 (Apple Git-155)
- Git config: user.name = Raheel_Savani, user.email = raheelsavani@gmail.com
- Auth method: HTTPS + Personal Access Token (classic), scope: `repo` only
  - Token stored in macOS Keychain after first push — shouldn't need to re-enter
    unless it expires or Keychain forgets it
- No SSH keys on this Mac (auth is HTTPS/token-based, not SSH)
- VS Code updated to 1.129.1, Python extension (Microsoft, official) installed
  and working — run Python files with the ▶️ "Run Python File" button in the
  top-right of the editor, no debugger extension needed for this project
- Always open the project via File → Open Folder... (not just the single file)
  so VS Code treats it as a proper workspace

---

## Project: Journal / Log Analyzer

A command-line app: write daily log entries to a text file, then read back
and analyze that file (word counts, longest entry, keyword search, etc.).
Uses every concept covered so far: loops, while/break, try/except/else/finally,
lists, string methods, f-strings, functions, and file I/O.

### Build order
1. **Setup** — git init, repo structure, first commit ✅ DONE
2. **Core loop** — while loop + menu (add entry / view entries / quit) using `break` ✅ DONE
3. **Writing entries** — `open()` in append mode, save entry to file ✅ DONE
4. **Reading entries back** — open file, print past entries ⬅️ NEXT
5. **Analysis features** — word count, longest entry, keyword search
   (functions + string methods)
6. **Error handling** — try/except throughout (e.g. missing file on first run)
7. **Polish + README** — proper README describing the tool
8. **Git wrap-up** — meaningful commit history, maybe a `.gitignore`
   (add `.DS_Store` to it)

### Step 3 notes (new concepts learned, not from futurecoder)
- `open()` takes a second argument controlling mode: `"r"` (read, default),
  `"w"` (overwrite/erase), `"a"` (append — adds to end, preserves existing content)
- `open(filename, "a")` auto-creates the file if it doesn't already exist —
  confirmed by testing, no need to pre-create the entries file
- `.write(text)` only accepts strings, does **not** auto-add a newline
  (unlike `print()`) — forgetting `"\n"` runs entries together on one line
- `.write()` returns the number of characters written (e.g. `7` for `"Testing"`)
- Writes are buffered — nothing actually lands in the file until the file is
  closed. Manual `open()`/`.close()` works but is risky (skipped `.close()`
  if the program crashes = lost data)
- `with open(filename, "a") as file:` is the safer pattern — auto-closes the
  file when the block ends, even on error. Preferred going forward.
- Current working add-entry code:
  ```python
  if selection == "1":
      entry = input("Please type your entry here:  ")
      with open("entries.txt", "a") as file:
          file.write(entry + "\n")
  ```
- Decision: `entries.txt` is fine to commit/push publicly for this project —
  no personal/sensitive content planned in test entries
- Reminder for step 4: a random person cloning the public repo and running
  the program only writes to *their own local copy* of entries.txt — they
  have no push access to the actual GitHub repo unless added as a collaborator

### Current full code (end of step 3)
```python
print("Welcome to your journal. Enter 1 to Add Entry, 2 to View Entries, 3 to Quit")

while True:
    selection = input("Please enter selection.  ").strip()
    if selection == "1":
        entry = input("Please type your entry here:  ")
        with open("entries.txt", "a") as file:
            file.write(entry + "\n")
    elif selection == "2":
        print("Viewing Entries")
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
  (like file-write mechanics above) get taught directly first, then practiced
- If stuck, ask a guiding question rather than explaining the fix

### Git habit while building
Commit after each meaningful step above (e.g. "add core menu loop", "add entry
writing with append mode") rather than one giant commit at the end. Small,
descriptive commits make it easier to see progress and undo mistakes if needed.