#!/usr/bin/env python3

import re
import sys
import argparse


def parse_args(args):
    parser.add_argument("-f", "--file", help="Create anchor links for every heading line (ie, lines starting with '#') in the supplied markdown file <FILE>", action="store")
    parser.add_argument("-a", "--anchor", help="Create one anchor link out of the double quoted string <ANCHOR>", action="store")
    parser.add_argument("-o", "--only-headers", help="Don't show headers found. Only output the created header links", action="store_true")
    return parser.parse_args(args)


def get_pretty_title(string):
    """
    Grab everything after the # and {one_or_more_spaces} and make it the pretty title
    """
    match = re.search(r"\#\s+(.*?)$", string)
    pretty_part = match.group(1) if match else "COULD NOT GET TITLE"
    return pretty_part


def replace_spaces_with_dashes(string):
    """
    Replace spaces with dashes
    """
    string = re.sub(r"\s", r"-", string, flags=re.IGNORECASE)
    return string


def drop_unwanted_chars(string):
    """
    Drop any characters that aren't "-", "_", a letter, a number or a space
    """
    string = re.sub(r"[^-_a-z0-9\s]", r"", string, flags=re.IGNORECASE)
    return string


def prepend_octothorpe(string):
    """
    Add a single # to the front of the string
    """
    string = re.sub(r"^(.*)$", r"#\1", string, flags=re.IGNORECASE)
    return string


def parenthesis_surround(string):
    """
    Add parenthesis around the whole string
    """
    string = re.sub(r"^(.*)$", r"(\1)", string, flags=re.IGNORECASE)
    return string


def remove_leading_dashes(string):
    """
    If there is a leading dash(es) (ie, #-something-something or #--something) get rid of them
    """
    string = re.sub(r"^\(#-+", r"(#", string, flags=re.IGNORECASE)
    return string


def make_lowercase(string):
    """
    Make everything lowercase
    """
    string = string.lower()
    return string


def anchor_maker(string):
    """
    Run all the functions that make the anchor and return the string
    """
    string = replace_spaces_with_dashes(string)
    string = drop_unwanted_chars(string)
    string = prepend_octothorpe(string)
    string = parenthesis_surround(string)
    string = remove_leading_dashes(string)
    string = make_lowercase(string)
    return string


def output_title_and_link(pretty_part, anchor_link):
    """
    Combine the pretty part of the title (ie, just the text) with the actual
    inline/anchor link and format it as a markdown hyperlink, ie: [title](link)
    Also adds two spaces at the end of the string; for a newline in Markdown
    """
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
        if no_titles_found is True:
            print(f"""No lines starting with "#" were found in {args.file}""")
        elif no_titles_found is False:
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
