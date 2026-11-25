# The Battery's Last Text to Its Charger

[![make.fun bounty](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/ahmed1813544/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/ahmed1813544/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

Entry for the [make.fun bounty "The Battery's Last Text to Its Charger"](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab).

`main.py` is a standard-library-only Python program that writes one line of
plain text — the phone battery's final message to the charger it waited for
all day — to `entry.txt` in the output directory (`/output` by default, or
`$MAKEFUN_OUTPUT_DIR` when set). The line is deterministic: every run writes
the exact same 182 characters.

## Run

```sh
python3 main.py
```

The text is written to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`).
