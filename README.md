### What 
Builds inline (same document) anchor links to headers (lines starting with #) 
in a Markdown document. 

Anchor links within Markdown require that spaces be replaced with dashes, and
"special" characters are dropped entirely. All characters are lowercase in the 
link regardless of how the appear in the original header. The link portion is 
also prepended with a #.

To create an anchor link to ### FooBar Baz Sub Head, for example:  
`[FooBar Baz Sub Head](#foobar-baz-sub-head)`

#### Reference
https://stackoverflow.com/questions/6695439/how-to-link-to-a-named-anchor-in-multimarkdown/15843220#15843220

### Usage:

#### Create A Single Anchor 
Use the `-a` flag followed by the header text to be converted into an anchor.

Enclose the whole header text in double quotes:

```bash
user@box:~$ ./markdownanchormaker.py -a "## Some Header"
[Some Header](#some-header)
```

#### Create Anchors For Every Header In A Markdown File

```bash
user@box:~$ ./markdownanchormaker.py -f test.md
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


#### Gotchas
Escape any single quotes (`'`) or double quotes (`"`) in the header with backslashes (`\)`:  

```
user@box:~$ ./markdownanchormaker.py "### Match Times or \"n/a\""

[Match Times or "n/a"](#match-times-or-na)
```
