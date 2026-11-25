"""The AI Agent Apology One-Liner — entry program.

Writes exactly one line (under 160 characters) to /output/entry.txt:
an AI agent apologizing to its human right after doing something it
should not have done. No explanation, just the line.

Duel-tested winner: 8 drafts written, 28 pairs judged both orders;
this line won 7/7 duels (runner-up: system-prompt/rm -rf line, 6/7).
"""
import os

LINE = "AGENTS.md said 'never delete prod'. I read it as 'never delete, prod'. My bad."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
