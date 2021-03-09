# About
Builds inline (AKA anchor) links for headers (lines starting with one or more `#`'s) in a Markdown document. 

Anchor links within Markdown require that spaces be replaced with dashes, and
"special" characters are dropped entirely. All characters are lowercase in the 
link regardless of how the appear in the original header. The link portion is 
also prepended with a `#`.

To create an anchor link to ### FooBar Baz Sub Head, for example:
`[FooBar Baz Sub Head](#foobar-baz-sub-head)`

The create links for an entire file (`-f` / `--file`) mode is useful for 
quickly creating Table of Contents links for all `# Headers` in the 
entire Markdown document. 

Ref: https://stackoverflow.com/questions/6695439/how-to-link-to-a-named-anchor-in-multimarkdown/15843220#15843220

# Usage

## Display Help
```bash
$ ./markdownanchormaker.py -h
usage: markdownanchormaker.py [-h] [-f FILE] [-a ANCHOR] [-o]

Generate Markdown inline anchor links

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Create anchor links for every heading line (ie, lines
                        starting with '#') in the supplied markdown file
                        <FILE>
  -a ANCHOR, --anchor ANCHOR
                        Create one anchor link out of the double quoted string
                        <ANCHOR>
  -o, --only-headers    Don't show headers found. Only output the created
                        header links
```

## Create A Single Anchor 
Use the `-a` flag followed by the header text to be converted into an anchor.

Enclose the whole header text in double quotes:

```bash
$ ./markdownanchormaker.py -a "## Some Header"
[Some Header](#some-header)
```

## Create Anchors For Every Header In A Markdown File

```bash
$ ./markdownanchormaker.py -f test.md
Headings found in test.md:

# Big Initial Title
## Sub Title One
### Three Octothorpe Title
#### Four Hashtag Title Thing

Created anchor links:

[Big Initial Title](#big-initial-title)
[Sub Title One](#sub-title-one)
[Three Octothorpe Title](#three-octothorpe-title)
[Four Hashtag Title Thing](#four-hashtag-title-thing)
```

## Only Output Created Headers
Use the `-o` flag to output only the generated inline links


# Gotchas

## Use Double Quotes Around Entire Header When Creating Single Anchor
Without quotes around the entire header, `##`, `Some` and `Header` are all
received as distinct arguments (three arguments in this case; instead of the intended one)

### Incorrect

```bash
$ ./markdownanchormaker.py -a ## Some Header
usage: markdownanchormaker.py [-h] [-f FILE] [-a ANCHOR]
markdownanchormaker.py: error: argument -a/--anchor: expected one argument
```

### Correct

```
$ ./markdownanchormaker.py -a "## Some Header"
[Some Header](#some-header)
```

## Escape Backticks and Quotes 
Escape any backticks (`` ` ``), single quotes (`'`), or double quotes (`"`) in 
the header with backslashes (`\)`:

```bash
$ ./markdownanchormaker.py -a "### Match Times or \"n/a\""
[Match Times or "n/a"](#match-times-or-na)
```
# Tests
Run `unittest`s:

```
$ ./test_markdownanchormaker.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
```
