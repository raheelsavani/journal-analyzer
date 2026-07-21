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
5a. **Analysis features, part 1** — word count + longest entry (functions, return values) ✅ DONE
5b. **Analysis features, part 2** — keyword search ⬅️ NEXT
6. **Error handling** — try/except throughout (e.g. missing file on first run)
7. **Polish + README** — proper README describing the tool
8. **Git wrap-up** — meaningful commit history, maybe a `.gitignore` (add `.DS_Store` to it)

### Step 5a notes (word count + longest entry, functions + return values)
- Redesigned menu: 1=New Entry, 2=View Entries, 3=Keyword Search, 4=Analyze, 5=Quit
- Considered a separate "Analyze" sub-menu with its own input prompt, then dropped it —
  Analyze just runs two functions back-to-back with no user choice, so no sub-menu,
  no extra input validation, and no inner loop needed
- `word_count()` and `longest_line()` each `return` their result instead of printing it,
  so option 4 can combine both into a single `print(f"...")` message
- Function definitions live at the top of `journal.py`, above the main `while True:` loop
- Wrote and tested each function standalone (temporary `print(word_count())` call above
  the loop) before touching/restructuring the menu, to isolate logic bugs from wiring bugs
- `word_count()`: accumulator set to `0` above the loop; for each line, `.strip()` then
  `.split()` into a list of words, add `len()` of that list to the accumulator, `return`
  the accumulator after the loop
- `longest_line()`: `longest = ""` before the loop (guarantees the first real line always
  wins the first comparison, since any real entry has `len() > 0`); for each line,
  `.strip()` then `.split()` then `" ".join()` back into a single-spaced string (this
  normalizes away extra/doubled internal spaces so accidental double-spacing can't
  artificially inflate an entry's length); compare `len()` of that normalized string
  against `len(longest)` with `>`, update `longest` if greater; `return longest` after
  the loop
- Bug caught during testing: found `elif selection == "1":` was missing `+ "\n"` on the
  `file.write()` call — confirmed via `git diff` that this was never actually committed/
  pushed from the Mac (despite step 3/4 notes saying it was done), not a git pull issue.
  Fixed and will be committed with this update.
- Confirmed via testing: `word_count()` and `longest_line()` called directly inside an
  f-string (e.g. `{word_count()}`) get evaluated immediately when Python builds the
  string — no need to store the return value in a variable first, though doing so is
  also valid
- Real-world gap found (not solved yet, deferred to step 6 by design): a missing
  `entries.txt` file (e.g. on a freshly cloned machine, since it's gitignored) causes a
  crash if the user picks any option other than "1" first. Step 6 (error handling) is
  the intended fix.

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