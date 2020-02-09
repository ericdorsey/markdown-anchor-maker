### What 
This script attempts to build an (inline) anchor link to a header
within a Markdown document. Anchor links within markdown require
that spaces be replaced with dashes, and "special" characters are
dropped entirely. All characters are lowercase in the link regardless
of how the appear in the original sub-header. The link portion is also
prepended with a #.

To anchor link to ### FooBar Baz Sub Head, for example, use:  
`[FooBar Baz Sub Head](#foobar-baz-sub-head)`

#### Reference
https://stackoverflow.com/questions/6695439/how-to-link-to-a-named-anchor-in-multimarkdown/15843220#15843220

### Usage:
Add double quotes around the title being passed in:  

```
user@box:~$ ./markdownanchormaker.py "### FooBar Baz Sub Head"
```

**Output**  

```
[FooBar Baz Sub Head](#foobar-baz-sub-head)
```
