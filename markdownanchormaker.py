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
import argparse

parser = argparse.ArgumentParser(description="Generate Markdown inline anchor links")

parser.add_argument("-f", "--file", help="Create multiple anchor links for the whole supplied markdown filename", action="store")

# Allow a non-flag argument as a default use case
parser.add_argument("other", nargs=argparse.REMAINDER, help="Create one anchor link out of the supplied double quoted string")

args = parser.parse_args()


def get_pretty_title(string):
    # Grab everything from #{space}{rest of line} and make it the pretty title
    match = re.search(r"[^#\s].*?$", string)
    pretty_part = match.group(0) if match else "COULD NOT GET TITLE"
    
    return pretty_part

def anchor_maker(string):
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

    return string

def output_title_and_link(pretty_part, anchor_link):
    full_title_and_link = f"[{pretty_part}]{anchor_link}  "

    return full_title_and_link


#print(args)
if args.file:
    #print(f"process -f {args.file}")
    collection_of_titles_before = []
    collection_of_titles = []
    no_titles_found = True
    with open(args.file) as myfile:
        contents = myfile.readlines()
    #print(contents)
    for i in contents:
        i = i.rstrip()
        match = re.search(r"^#.*?$", i)
        if match:
            no_titles_found = False
            collection_of_titles_before.append(i)
            pretty_part = get_pretty_title(i)
            anchor_link = anchor_maker(i)
            full_title_and_link = output_title_and_link(pretty_part, anchor_link)
            collection_of_titles.append(full_title_and_link)
    if no_titles_found == True:
        print(f"""No lines starting with "#" were found in {args.file}""")
    elif no_titles_found == False:
        print(f"Sub headings found in {args.file}:")
        print()
        for j in collection_of_titles_before:
            print(j)
        print()
        print("Anchor links created:")
        print()
        for k in collection_of_titles:
            print(k)
            
if args.other:
    # Ensure we only got one default (ie, non flag [-s, --something] argument)
    if len(args.other) > 1:
        multi_args_gotten = " ".join(args.other)
        print(f"Expected one argument only; instead got {len(args.other)} --> {multi_args_gotten}")
        print(f"Please try again with only one argument. Exiting.")
        sys.exit(1)
    pretty_part = get_pretty_title(args.other[0])
    anchor_link = anchor_maker(args.other[0])
    full_title_and_link = output_title_and_link(pretty_part, anchor_link)
    print()
    print(full_title_and_link)

