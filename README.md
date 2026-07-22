***This project was built as a learning exercise. The idea and barebones blueprint were provided by Claude, while 100% of the codebase was developed manually by me.***

## How to run it

Requires Python 3 (no external packages/pip installs needed — the project only uses Python's standard library).

python journal.py

or

python3 journal.py

On first run, `entries.txt` doesn't exist yet — it's created automatically the first time you choose option 1 (New Entry). You'll then see a menu (1–5) and can add entries, view them, search by keyword, or run analysis (word count + longest entry).

## Build order

1. **Setup** — git init, repo structure, first commit.

2. **Core loop** — while loop + menu (add entry / view entries / quit) using `break`.
   > Built as described, no changes.

3. **Writing entries** — `open()` in append mode, save entry to file.
   > Built as described. The decision to stop tracking `entries.txt` in git entirely (and add a `.gitignore`) came later, once I realized a disposable, auto-regenerated data file didn't belong in version control.

4. **Reading entries back** — open file, print past entries.
   > I noticed `print()` naturally left a double-newline gap between entries (from the newline saved in the file plus `print()`'s own newline). I looked into `print()`'s `end` parameter to remove it, then deliberately kept the default spacing because it was more readable for a single-user tool.

5. **Analysis features** — word count, longest entry, keyword search (functions + string methods).
   > I decided against a separate "Analyze" sub-menu after realizing it just runs two functions back-to-back with no user input needed. `word_count()` and the longest-entry function each `return` their result instead of printing internally, so option 4 could combine both into one message. Keyword search was written inline rather than as its own function, since it's used in exactly one place.

6. **Error handling** — try/except throughout (e.g. missing file on first run).
   > While testing the fix, I found two related silent failures: viewing entries on an empty file, and searching a keyword with no match, both printed nothing. I went back into already-working code and added flag variables to handle those cases with a proper message.

7. **Polish + README** — proper README describing the tool.

8. **Git wrap-up** — meaningful commit history, `.gitignore`.

## A note from the programmer

This project was an excellent means of boosting my confidence in my understanding and implementation of Python fundamentals. During the course of the project, I used Claude as a tutor who I bounced ideas off of and who never fed me any solution but rather gave me guiding questions so I could lead myself to that solution. At the end of this document, I've included the instructions Claude follows to perform in this Socratic-method tutor capacity.

Furthermore, this project gave me excellent insight into how programming is a fluid process. We set out with a semi-rigid structure, and quickly uncovered that our preconceived notions of that structure would change as we further developed the program. One example: as I was reviewing the "View Entries" and "Keyword Search" sections, I realized I had no message printing to the user in the case of entries or keywords not existing. The original code blocks of both those sections were already complete and functional, but I had to revisit both of them and implement additional if statements and flag variables.

## Instructions for Claude

I'm learning Python (and soon SQL) through futurecoder.io, currently on beginner-to-intermediate material: list manipulation, string methods, loops, indexing, f-strings.

When I ask for help with an exercise:
- Don't give me the direct answer unless I explicitly ask for it.
- Use a Socratic, hint-based approach — nudge me toward the answer, don't hand it to me.
- Before I write any code, walk me through the logic in plain English, step by step.
- Stay within concepts my lessons have already covered — don't introduce techniques or syntax I haven't learned yet, even if they're a "better" solution.
- If I'm stuck, ask me a guiding question rather than explaining the fix.



