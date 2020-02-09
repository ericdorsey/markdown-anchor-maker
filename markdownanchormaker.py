#!/usr/bin/env python3

"""
This script attempts to build an (inline) anchor link to a header 
within a Markdown document. Anchor links within markdown require
that spaces be replaced with dashes, and "special" characters are 
dropped entirely. All characters are lowercase in the link regardless
of how the appear in the original sub-header. The link portion is also
prepended with a #.

To anchor link to ### FooBar Baz Sub Head, for example, use;
[FooBar Baz Sub Head](#foobar-baz-sub-head) 

Ref:
https://stackoverflow.com/questions/6695439/how-to-link-to-a-named-anchor-in-multimarkdown/15843220#15843220

Usage -- add double quotes around the title being passed in:
user@box:~$ ./markdownanchormaker.py "### FooBar Baz Sub Head"
"""

import re
import sys
import traceback

try:
    string = sys.argv[1]
except IndexError as err:
    traceback.print_exc()
    print("\033[91mINFO: Was the whole title argument not surrounded by double quotes? Exiting.\033[00m")
    sys.exit(1)

match = re.search(r"[^#\s].*?$", string)
pretty_part = match.group(0) if match else "COULD NOT GET TITLE"

# Replace spaces with dashes
string = re.sub(r"\s", r"-", string, flags=re.IGNORECASE)

# Drop any characters that aren't "-", "_", a letter, number or a space
string = re.sub(r"[^-_a-z0-9\s]", r"", string, flags=re.IGNORECASE)

# Add a single # to the front of the string
string = re.sub(r"^(.*)$", r"#\1", string, flags=re.IGNORECASE)

# Add parentheses around the whole string
string = re.sub(r"^(.*)$", r"(\1)", string, flags=re.IGNORECASE)

# If there is a leading dash (ie, #-something-something)  get rid of it
string = re.sub(r"^\(#-", r"(#", string)

# Make everything lowercase
string = string.lower()

print()
print(f"[{pretty_part}]{string}")
