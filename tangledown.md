# Tangledown: One-Step Literate Markdown

### Brian Beckman
### 21 July 2016

## DISCLAIMER: 

This is a toy. It's a useful toy, but it has zero error handling. This document currently talks only about the happy path.  I try to be rude in comments every place where I sense trouble, but I'm only sure I haven't been rude enough. Read this with sense-of-humor bit turned on.

## OVERVIEW

README.md files are mandatory, or really should be, in projects. README.md files should be authoritative and complete. README.md files that _can't_ get out of sync with code are best. 

Let's write README.md files that _contain all the code for a project_, along with authoritative documentation. Let the README.md  presentation be optimized for human consumption. Let's use a tool to suck the code out of README.md files and spray it out onto the disk drive in some other  order optimized for build tools. 

I just described a kind of [Literate Programming](https://en.wikipedia.org/wiki/Literate_programming), a method of software documentation invented by [Donald Knuth](http://amturing.acm.org/award_winners/knuth_1013846.cfm). Because our documentation language is Markdown, we'll call this variation _Literate Markdown_. 

This here document, the one you're reading right now, is, itself, an instance of literate Markdown. It contains the literate-Markdown tool called _Tangledown_ with all the documentation and literature about it.

This tool pulls or _tangles_ code out of any Markdown document. The verb "tangle" is traditional in the literate-programming community. You might think it really means "untangle," because the order of presentation in the Markdown document is all tangled up from the point of view of the build tools. But Knuth thinks it's the other way around: he prefers the human's point of view. The Markdown document contains the code in the _correct_ order --- the one for human consumption, and the build tools need the code all tangled up in some other, essentially arbitrary order.

If we need something _more_ powerful than Markdown, say to produce publishable PDF files, we'll go back to [org-mode](http://orgmode.org/) and [org-babel](http://orgmode.org/worg/org-contrib/babel/) in emacs (or [spacemacs](http://spacemacs.org/) for you VIM users), which are best-of-breed, classical literate programming tools. But Markdown is good enough for Github, and thus for the vast majority of open-source code in the world.

## EXPLOIT: Markdown Ignores Mysterious Tags

Let's exploit the fact that at least some markdown renderers, like Github's and like [MOU](http://25.io/mou/), ignore HTML / XML tags that they don't recognize. We can name blocks of code with `noweb` tags, like this:

    <noweb name="my_little_tests">

        class TestSomething (unittest.TestCase):
            """unittest documented here: https://goo.gl/OqCGEx"""
            def test_something (self):
                self.assertEqual (3, 2+1)

    </noweb>
    
The block above renders as follows:

<noweb name="my_little_tests">

```
class TestSomething (unittest.TestCase):
    """unittest documented here: https://goo.gl/OqCGEx"""
    def test_something (self):
        self.assertEqual (3, 2+1)
```

</noweb>

Leave the blank line after the opening `<noweb...>` tag and another blank line before the ending `</noweb>` tag, unless you don't want to render the code like code. Here's a non-rendered `noweb` block --- no blank lines surrounding the contents of the `noweb` tag:

<noweb name="another_little_test">
    def test_something_else (self):
      self.assertEqual (42, 6 * 7)
</noweb>

Not too pretty, but it's important to know what happens when you don't leave blank lines. 

## THREE TAGS: noweb, block, and tangle

With or without the blank lines, MOU won't render the tags themselves.
MOU only renders the material between the opening and closing tags, called the _contents_ of the tags.

But this here Tangledown compiler _doesn't_ ignore the tags. Tangledown is a Python script that sucks up the contents of the `noweb` tags and sticks them into a dictionary with the keys `my_little_tests` or `another_little_test`, at least for the samples above. 

In general, the key for a noweb block is the string value of the `name` attribute of the `noweb` tag. Later, Tangledown will blow those lines back out wherever it sees a `block` tag with the same name. 

Often, a `block` tag will be inside a `tangle` tag that causes its entire contents to spray out to the disk drive to a file. What file? The file named in the `file` attribute of the `tangle` tag. 

The same rules for blank lines hold for `tangle` tags as they do for `noweb` tags: if you want MOU to render the contents like code, bracket the contents with blank lines; otherwise, leave the blank lines out. The following

    <tangle file="a_unit_testing_sample.py">
    
        import unittest
        
        <block name="my_little_tests"></block>
    
        if __name__ == '__main__':
          unittest.main()
    
    </tangle>

renders like this

    import unittest
        
    <block name="my_little_tests"></block>
    
    if __name__ == '__main__':
        unittest.main()
    
### You're a human! Read the `block` tags!

Because the `block` tag is inside a top-level `tangle` or `noweb` tag, MOU will render the `block` tag verbatim to the documentation. This is good for humans, who will think "AHA!, this bit of code --- this `block` --- refers to some other code --- in a `noweb` tag with the same name --- that I should read in another place and time. This here beautifully written document I'm reading right now is making it easy for me to understand the big picture because it's breaking things up like this. Thank you, kindly, author!" 

In fact, that's exactly what you want for humans: talk about something in a place where you don't necessarily implement it.  But compilers need the block _right here and now_. Tangledown will substitute the contents of a block for the `block` tag in a tangle block somewhere else when writing files to the disk for you. The substitution process is hidden, behind the scenes, and only needed when it's time to create files on your hard drive. 

You don't need any contents in a `block` tag, but you're welcome to put some in, say for some commentary. Tangledown will eat and ignore any contents in a `block` tag.

## BOOTSTRAPPING Step-by-Step

This here document that you're reading right now is literature, after all, so we should tell a story. Let's tell the story of creating Tangledown. And we'll use Tangledown to _build_ Tangledown. That's just like bootstrapping a compiler. Tangledown is a (very small and silly) compiler. Just as we ordinarily use a compiler to compile a compiler, we'll use Tangledown to tangle Tangledown itself out of this here document named tangledown.md that you're reading right now.

### Recognize Tags

The following regular expressions match tags that must appear on lines by themselves, left-justified. These regular expressions won't match themselves, so it's safe to run this code on this file itself --- that's our bootstrapping technique.

The names in the name attributes of `noweb` and `tangle` tags must start with a letter, and they can contain letters, numbers, hyphens, underscores, whitespace, and dots.

<noweb name="left_justified_regular_expressions">

    noweb_start_re = re.compile (r'^<noweb name="([a-zA-Z][\w\s\-_\.]+)">$')
    noweb_end_re = re.compile (r'^</noweb>$')
    
    tangle_start_re = re.compile (r'^<tangle file="([a-zA-Z][\w\s\-_\.]+)">$')
    tangle_end_re = re.compile (r'^</tangle>$')
    
</noweb>

The following regular expressions match tags that may appear anywhere on a line. I converted the 'o' in 'block' to a harmless group '[o]' so that _block_end_ doesn't match itself. That makes it safe to run this code on this here document itself during bootstrapping.

<noweb name="anywhere_regular_expressions">

    block_start_re = re.compile (r'.*<block name="([a-zA-Z][\w\s\-_\.]+)">')
    block_end_re = re.compile (r'.*</bl[o]ck>')
    
</noweb>

### Test the recognizers

The following code has two `block` tags that refer to the `noweb` tags of the regular expressions defined above. After Tangledown substitutes the contents of the `noweb` tags, the code becomes valid Python and you can run it. I lightly tested this with Python 2.7.11. When you run it, it proves that we can regognize all the various kinds of tags. Notice the special treatment for block ends, which will usually be on the same lines as their block tags, but not necessarily so. Also notice that it only operates on one specific file, this here document you're reading right now, namely, tangledown.md, so we need to fix that later.

<noweb name="openers">

    import re

    aFile = open ('tangledown.md')
    lines = aFile.readlines ()
    aFile.close ()

    <block name="left_justified_regular_expressions"></block>
    <block name="anywhere_regular_expressions"></block>
    
    for line in lines:
        noweb_start_match = noweb_start_re.match (line)
        tangle_start_match = tangle_start_re.match (line)
        block_start_match = block_start_re.match (line)
    
        noweb_end_match = noweb_end_re.match (line)
        tangle_end_match = tangle_end_re.match (line)
        block_end_match = block_end_re.match (line)
    
        if (noweb_start_match):
            print ('NOWEB: ', noweb_start_match.group (0))
            print ('name of the block: ', noweb_start_match.group (1))
        elif (noweb_end_match):
            print ('NOWEB END: ', noweb_end_match.group (0))
        elif (tangle_start_match):
            print ('TANGLE: ', tangle_start_match.group (0))
            print ('name of the file: ', tangle_start_match.group (1))
        elif (tangle_end_match):
            print ('TANGLE END: ', tangle_end_match.group (0))
        elif (block_start_match):
            print ('BLOCK: ', block_start_match.group (0))
            print ('name of the block: ', block_start_match.group (1))
            if (block_end_match):
                print ('BLOCK END SAME LINE: ', block_end_match.group (0))
            else:
                print ('BLOCK NO END')
        elif (block_end_match):
            print ('BLOCK END ANOTHER LINE: ', block_end_match.group (0))
        else:
            pass

</noweb>
 
## TANGLEDOWN: Two Passes

Tangledown operates in two passes, once over the file and a second time over the tangle blocks that it collected in the first pass. In the second pass, Tangledown does the substitution for block tags, creating valid code on the disk if the markdown is correctly written.

### First Pass: Saving Noweb and Tangle Blocks

In the first pass over the file, we'll just save the noweb and tangle contents into dictionaries, without expanding nested `block` tags.

#### global dictionaries

<noweb name="global dictionaries">

    noweb_blocks = {}
    tangle_files = {}
    
</noweb>

#### Oh no! There are two ways

Turns out there are two ways to write literal blocks in MOU's flavor of
Markdown: 

1. indented by four spaces and 
2. surrounded by triple backticks and _not_ indented. 

We need to handle both ways. 

We use the same trick of a harmless group around one of the backticks in the
regular expression that recognizes triple backticks so that this regex is safe
to run on itself. 

The following function recognizes code blocks bracketed by triple backticks

<noweb name="oh-no-there-are-two-ways">

```
triple_backtick_re = re.compile (r'^`[`]`')
blank_line_re      = re.compile (r'^\s*$')

def first_non_blank_line_is_triple_backtick (i, lines):
    while (blank_line_re.match (lines[i])):
        i = i + 1
    return triple_backtick_re.match (lines[i])
```

</noweb>

#### accumulate

Tangledown is a little compiler, a silly compiler. We could go  highfalutin' and write it in state-machine and parser-combinator style, and then it would be very pretty and easy to explain to a compiler theorist. However, we want to make it

- very short
- independent of rich libraries like parser combinators
- completely obvious to anyone

We'll just use global variables and array indices and side effects, but in a tasteful way.

The function `accumulate` starts at line `i`, then figures out whether a tag's first non-blank line is triple backtick, in which case it _won't_ snip four spaces from the beginning of every line, and finally keeps going until it sees the end of the tag. This function is meant to accumulate the contents of `noweb` or `tangle` tags.

<noweb name="accumulate-function">

```
def accumulate (i, end_re):
    if (first_non_blank_line_is_triple_backtick (i, lines)):
        i = i + 1 # eat the line
        snip = 0
    else:
        snip = 4
    block_lines = []
    for j in range (i, len(lines)):
        end_match = end_re.match(lines[j])
        if (end_match):
            # This is the only place we return!
            return j + 1, block_lines
        else:
            if (snip == 0 and triple_backtick_re.match (lines[j])):
                pass
            else:
                block_lines.append (lines[j][snip:])
```
    
</noweb>

#### Do it already!

The next bit of code is top-level script. It sucks all the `noweb` tags and `tangle` tags out of a file, but doesn't expand any `block` tags that it finds. We use it just to build up our internal dictionaries.

<noweb name="accumulate-script">

    for i in range (len (lines)):
        noweb_start_match = noweb_start_re.match (lines[i])
        tangle_start_match = tangle_start_re.match (lines[i])
        if (noweb_start_match):
            block_key = noweb_start_match.group (1)
            i, noweb_blocks[block_key] = accumulate (i + 1, noweb_end_re)
        elif (tangle_start_match):
            file_key = tangle_start_match.group (1)
            i, tangle_files[file_key] = accumulate (i + 1, tangle_end_re)

</noweb>

### DUDE!

There is a lot that can go wrong. We can have all kinds of mal-formed contents:
too many or not enough triple-backtick lines, broken tags, dangling tags, misspelled names, syntax errors, and much, much more. 

We'll get to error handling someday, maybe. Tangledown is just a little tool for
my personal use at the moment, but I thought it interesting to write about. If it's going to be distributed to hostile users, then we will enumerate all the bad cases and handle them. But not now. Let's get the happy case right, first. 



### Second Pass: Expanding Blocks

Iterate over all the `tangle` tag contents and expand the
`block` tags we find in there. We must keep going until there are no more `block` tags, because `noweb` blocks are allowed (encouraged!) to refer to other blocks. If there are cycles, this will hang. 

### DUDE! HANG?

We're doing the happy cases first, and
will get to error handling someday, maybe.

#### There is a `block` tag

First, we need to detect that some list of lines contains a `block` tag. That
means we must keep running the expander on that list.

<noweb name="thereIsABlockTag">

```
def there_is_a_block_tag (lines):
    for line in lines:
        block_start_match = block_start_re.match (line)
        if (block_start_match):
            return True
    return False
```

</noweb>

#### Eat a `block` tag ####

If there is a `block` tag, we must eat it:

<noweb name="eatBlockTag">

```
def eat_block_tag (i, lines):
    for j in range (i, len(lines)):
        end_match = block_end_re.match (lines[j])
        if (end_match):
            return j + 1
        else: # DUDE!
            pass
```

</noweb>

#### The Expander ####

The following function does one round of block expansion. The caller must check
whether any `block` tags remain, and keep running the expander until there are no
more `block` tags. Our functional-programming conscience might be apalled, but, see, we don't have to be recursive _all the time_. Sometimes it's just easier to iterate.

<noweb name="expandBlocks">

```
def expand_blocks (lines):
    out_lines = []
    for i in range (len (lines)):
        block_start_match = block_start_re.match (lines[i])
        if (block_start_match):
            block_key = block_start_match.group (1)
            block_lines = noweb_blocks [block_key] # DUDE!
            i = eat_block_tag (i, lines)
            for block_line in block_lines:
                out_lines.append (block_line)
        else:
            out_lines.append (lines[i])
    return out_lines

```

</noweb>

## Tangle It, Already!

Ok, you saw at the top that the code in this here Markdown document will read in all the lines in ... this here Markdown document. Bootstrapping!

But you have to run something first. For that, I provide "bootstrap.py."  It's a version of the code in this here document that will get you started. The first thing to do, then, is run the following at the command line

```
python bootstrap.py
```

That should create a file named "tangledown.py."  You can then run that over and over again

```
python tangledown.py
```

and it will just keep writing over itself. Whee! we're in a loop, but we bootstrapped the thing.


<tangle file="tangledown.py">

```
<block name="openers"></block>
<block name="global dictionaries"></block>
<block name="oh-no-there-are-two-ways"></block>
<block name="accumulate-function"></block>
<block name="accumulate-script"></block>
<block name="thereIsABlockTag"></block>
<block name="eatBlockTag"></block>
<block name="expandBlocks"></block>

for k, v in tangle_files.iteritems ():
    outfile = open (k, 'w')
    lines = v
    while there_is_a_block_tag (lines):
        lines = expand_blocks (lines)
    for line in lines:
        outfile.write (line)
    outfile.close ()
```

</tangle>

To make this work on any file instead of just on itself, change the contents of the `openers` tag: `import sys` and get a file name from the command line via `sys.argv`.

## DUDE!

Some people like to write "TODO" in their code so they can find all the spots
where they thought they might have trouble but didn't have time to write the
prophylactic code at the time. I like to write "DUDE" because it sounds like
"TODO" but is more rude and funny. 

