#!/usr/bin/env python3

import re
import sys
import argparse

def parse_args(args):
    parser.add_argument("-f", "--file", help="Create anchor links for every heading line (ie, lines starting with '#') in the supplied markdown file <FILE>", action="store")
    parser.add_argument("-a", "--anchor", help="Create one anchor link out of the double quoted string <ANCHOR>", action="store")
    parser.add_argument("-o", "--only-headers", help="Don't show headers found. Only output the created header links", action="store_true")
    #args = parser.parse_args()
    return parser.parse_args(args)

def get_pretty_title(string):
    # Grab everything after the # and {one_or_more_spaces} and make it the pretty title
    match = re.search(r"\#\s+(.*?)$", string)
    pretty_part = match.group(1) if match else "COULD NOT GET TITLE"
    return pretty_part

def anchor_maker(string):
    # Replace spaces with dashes
    string = re.sub(r"\s", r"-", string, flags=re.IGNORECASE)
    # Drop any characters that aren't "-", "_", a letter, a number or a space
    string = re.sub(r"[^-_a-z0-9\s]", r"", string, flags=re.IGNORECASE)
    # Add a single # to the front of the string
    string = re.sub(r"^(.*)$", r"#\1", string, flags=re.IGNORECASE)
    # Add parentheses around the whole string
    string = re.sub(r"^(.*)$", r"(\1)", string, flags=re.IGNORECASE)
    # If there is a leading dash(es) (ie, #-something-something or #--something) get rid of them
    string = re.sub(r"^\(#-+", r"(#", string, flags=re.IGNORECASE)
    # Make everything lowercase
    string = string.lower()
    return string

def output_title_and_link(pretty_part, anchor_link):
    # Add two spaces at the end of the string for newline in Markdown
    full_title_and_link = f"[{pretty_part}]{anchor_link}  "
    return full_title_and_link

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Markdown inline anchor links")
    args = parse_args(sys.argv[1:])
    if not len(sys.argv) > 1:
        parser.print_help()
    if args.file:
        collection_of_titles_before = []
        collection_of_titles = []
        no_titles_found = True
        with open(args.file) as myfile:
            contents = myfile.readlines()
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
            if not args.only_headers:
                print(f"Headings found in {args.file}:")
                print()
                for j in collection_of_titles_before:
                    print(j)
                print()
                print("Created anchor links:")
                print()
            for k in collection_of_titles:
                print(k)
                
    if args.anchor:
        pretty_part = get_pretty_title(args.anchor)
        anchor_link = anchor_maker(args.anchor)
        full_title_and_link = output_title_and_link(pretty_part, anchor_link)
        print(full_title_and_link)
