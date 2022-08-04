# Tangledown: One-Step Literate Markdown

### Brian Beckman
### 4 Aug 2022

## DISCLAIMER: 

This is a toy. It's a useful toy, but it has zero error handling. This document currently talks only about the happy path.  I try to be rude in comments every place where I sense trouble, but I'm only sure I haven't been rude enough. Read this with sense-of-humor bit turned on.

## OVERVIEW

- README.md files are mandatory, or really should be, in projects. 

- README.md files should be authoritative and complete. README.md files that _can't_ get out of sync with code are best. 

- Let's put _all the code_ for a project inside README.md, along with authoritative documentation. 
 
- Let's write README.md for human reasoning and understanding, that is, _top-down_ instead of _bottom-up_. Let's help readers understand the big picture before overwhelming them with implementation details. 

- Let's create a tool to suck the code out of README.md and rearrange it on disk in some other, usually _botton-up_ order required by build tools. 

I just described a kind of [Literate Programming](https://en.wikipedia.org/wiki/Literate_programming), a method of software documentation invented by [Donald Knuth](http://amturing.acm.org/award_winners/knuth_1013846.cfm). Knuth wrote MetaFont and TeX in literate style. Those are two of the most important programs ever written. In a blatant appeal to authority and celebrity, doesn't that mean Literate Programming is good enough for everyone? 

This here document, README.md, the one you're reading right now, is, itself, a Literate Program. Because our documentation language is Markdown, we'll call the language of this document _Literate Markdown_. This here README.md that you're reading right now contains all the source for the Literate-Markdown tool called `tangledown.py`, with all its documentation, all presented in narrative style, like a mathematical theory or story.

_Tangledown.py_ pulls or _tangles_ code out of any Markdown document, not just this one (README.md). The verb "tangle" is traditional in Literate Programming. You might think it should be "untangle," because the Markdown document is all tangled up from the point of view of build tools. But Knuth prefers the human's point of view. The Markdown document contains the code in the _correct_ order --- the order for human reasoning and understanding, and the build tools need the code all tangled up in some other, essentially arbitrary order.

If we need something _more_ powerful than Tangledown, say to produce publishable LaTeX and PDF files, we'll go back to [org-mode](http://orgmode.org/) and [org-babel](http://orgmode.org/worg/org-contrib/babel/) in emacs (or [spacemacs](http://spacemacs.org/) for you VIM users). Those are much more powerful, best-of-breed, classical Literate-Programming tools. You have to learn some emacs to use them, and that's an insurmountable barrier for many people. Markdown is good enough for Github, and thus for most open-source.

## HOW TO RUN THIS: 

Run `python3 tangledown.py REAMDE.md`. That command should _overwrite_ tangledown.py. The code for tangledown.py is inside README.md. The name of the file to overwrite, namely `tangledown.py` is embedded inside README.md itself, in `<tangle>` tags. Read about them below!

If you said `python3 tangledown.py MY-FOO.md`, then you would be tangling the code out of `MY-FOO.md`. You'll do that once you start writing your own code in Tangledown. You will love it!

<!-- I bootstrapped tangledown once for you already and checked in the file, so this silly little compiler is already bootstrapped. If you want to run tangledown on some other Markdown document (see Section [Bootstrapping: step-by-step](#bootstrapping). Once it's bootstrapped, though, you can change code and run it over and over again ad nauseum. -->

## HOW IT WORKS: Markdown Ignores Mysterious Tags

Let's exploit the fact that most markdown renderers, like Github's and [PyCharm's](https://www.jetbrains.com/pycharm/), ignore HTML / XML tags (stuff inside angle brackets) that they don't recognize. Let's enclose blocks of real, live code with `noweb` tags, like this:

    <noweb name="my_little_tests">

        class TestSomething (unittest.TestCase):
            """unittest documented here: https://goo.gl/OqCGEx"""
            def test_something (self):
                self.assertEqual (3, 2+1)

    </noweb>
    
The block above renders as follows:

<noweb name="my_little_tests">

    class TestSomething (unittest.TestCase):
        """unittest documented here: 
        https://docs.python.org/3/library/unittest.html"""
        def test_something (self):
            self.assertEqual (3, 2+1)

</noweb>

Leave the blank line after the opening `<noweb...>` tag and another blank line before the ending `</noweb>` tag, unless you don't want to render the code like code. Here's a non-rendered `noweb` block --- no blank lines surrounding the contents of the `noweb` tag:

<noweb name="another_little_test">
    def test_something_else (self):
      self.assertEqual (42, 6 * 7)
</noweb>

Not too pretty, but it's important to know what happens when you don't leave blank lines. 

## THREE TAGS: noweb, block, and tangle

With or without the blank lines, Markdown won't render the opening `<noweb>` and closing `</noweb>` tags themselves. Markdown only renders the material between the tags, called the _contents_ of the tags.

But `tangledown.py` _doesn't_ ignore the tags. `tangledown.py` is a Python script that sucks up the contents of the `noweb` tags and sticks them into a dictionary. For the examples above, the dictionary has the keys `my_little_tests` or `another_little_test`.

In general, the key for a noweb block is the string value of the `name` attribute of the `noweb` tag. Later, Tangledown will blow those lines back out wherever it sees a `block` tag with the same name. That's how you can define some code in one `noweb` and use it later, more than once if you like, in matching `blocks`, kind of like a C macro or an inline function.  

Often, a `block` tag will be inside a `tangle` tag that sprays its entire contents to a file on disk. What file? The file named in the `file` attribute of the `tangle` tag. `block` tags can also be inside `noweb` tags, so one noweb can talk about another noweb without implementing it first.

The same rules about blank lines hold for `tangle` tags as they do for `noweb` tags: if you want Markdown to render the contents like code, bracket the contents with blank lines; otherwise, leave the blank lines out. The following

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

Because a `block` tag is inside a top-level `tangle` or `noweb` tag, Markdown will render the `block` tag verbatim to the documentation. This is good for humans, who will think "AHA!, this bit of code --- this `block` --- refers to some other code --- in a `noweb` tag with the same name --- that I should read some other place and time. 

This here beautifully written document I'm reading right now is making it easy for me to understand the big picture first, because it's breaking things up like this. Thank you, kindly, author! Without you, I'd be awash in details, I'd get tired and cranky before ever understanding the big picture!" 

That's exactly what you want for humans: talk about something in a place where you don't necessarily _implement_ it. But compilers usually need the full implementation of the block _right here and now_ before it's ever used. 

See, I'll prove it to you. Here is the code for the whole program. You can understand this without understanding the _implementations_ of the sub-pieces, just getting an idea of _what_ they do from the names of the `block` tags. All we do is loop over all the lines in the input and substitute something wherever we see a `block` tag. What do we substitute? The contents of a `noweb` tag with the same name as the name mentioned in the `block` tag.

<tangle file="tangledown.py">

    <block name="openers"></block>
    <block name="global dictionaries"></block>
    <block name="oh-no-there-are-two-ways"></block>
    <block name="accumulate-function"></block>
    <block name="accumulate-script"></block>
    <block name="thereIsABlockTag"></block>
    <block name="eatBlockTag"></block>
    <block name="expandBlocks"></block>
    
    for k, v in tangle_files.items ():
        outfile = open (k, 'w')
        lines = v
        while there_is_a_block_tag (lines):
            lines = expand_blocks (lines)
        for line in lines:
            outfile.write (line)
        outfile.close ()

</tangle>

We'll implement those bits, like `global dictionaries` and `eatBlockTag`, later, after you've gotten the big picture. Notice the names can contain spaces, can be in kebab-case, Pascal-case, camel-case, snake-case, whatever you like.

Tangledown will substitute the contents of the corresponding `noweb` for the `block` tag in a tangle block somewhere else when writing files to the disk for you. The substitution process is hidden, behind the scenes, and only needed when it's time to create files on your hard drive. 

You don't need any contents in a `block` tag, but you're welcome to put some in, say for some in-code commentary. Tangledown will eat and ignore contents of a `block` tag. Your commentary for _humans_ to read and understand is the text _surrounding_ the `block` tags, Markdown text like the text you're reading right here and now.

## <a name="bootstrapping"></a>BOOTSTRAPPING Step-by-Step

This here README.md that you're reading right now is literature, after all, so it should tell a story. Let's tell the story of creating Tangledown. And we'll use Tangledown to _create_ Tangledown. That's just like bootstrapping a compiler. Just as we ordinarily use a compiler to compile a compiler, we'll use Tangledown to tangle Tangledown itself out of this here document named README.md that you're reading right now.

### Tangledown Tangles Itself?

Tangledown uses two kinds of regular expressions for matching tags in any Markdown file: regular expressions for tags that appear on lines by themselves, left-justified, and regular expressions that match tags that may appear anywhere on a line. Both kinds are _safe_, in the sense that they do not match themselves. That means it's safe to run tangledown.py on READMD.md, which contains source for tangledown.py, including those two kinds of regular expressions.

The two regular expressions defined in the noweb `left_justified_regular_expressions` match `noweb` and`tangle` tags that appear on lines by themselves, left-justified. These regular expressions won't match themselves; that's our bootstrapping technique. They also wont match `noweb` and `tangle` tags that are indented. That lets us _talk about_ `noweb` and `tangle` without running the machinery behind them: just put the examples you're talking about in an indented Markdown code blob instead of in a triple-backticked code blob.

The names in the name attributes of `noweb` and `tangle` tags must start with a letter, and they can contain letters, numbers, hyphens, underscores, whitespace, and dots. That's what is said by the regular expressions in noweb `left_justified_regular_expressions`.

<noweb name="left_justified_regular_expressions">

    noweb_start_re = re.compile (r'^<noweb name="([a-zA-Z][\w\s\-_\.]+)">$')
    noweb_end_re = re.compile (r'^</noweb>$')
    
    tangle_start_re = re.compile (r'^<tangle file="([a-zA-Z][\w\s\-_\.]+)">$')
    tangle_end_re = re.compile (r'^</tangle>$')
    
</noweb>

The regular expressions in noweb `anywhere_regular_expressions` matches `block` tags that may appear anywhere on a line. I converted the 'o' in 'block' to a harmless regex group `[o]` so that _block_end_ doesn't match itself. That makes it safe to run this code on this here document itself during bootstrapping.

<noweb name="anywhere_regular_expressions">

    block_start_re = re.compile (r'.*<block name="([a-zA-Z][\w\s\-_\.]+)">')
    block_end_re = re.compile (r'.*</bl[o]ck>')
    
</noweb>

### Test the Regular Expressions

The code in noweb `openers` has two `block` tags that refer to the `noweb` tags of the regular expressions defined above, namely `left_justified_regular_expressions` and `anywhere_regular_expressions`. After Tangledown substitutes the contents of the `noweb` tags whose names match the names mentioned in the `block` tags, the code becomes valid Python and you can run it. When you run it, it proves that we can recognize all the various kinds of tags. Notice the special treatment for block ends, which will usually be on the same lines as their block tags, but not necessarily so. 

<noweb name="openers">

    import re
    import sys
    print({f'len(sys.argv)': len(sys.argv), f'sys.argv': sys.argv})
    aFile = None
    if len(sys.argv) > 1:
        aFile = sys.argv[1]
    else:
        aFile = open('README.md')

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

#### Oh no! There are two ways!

Turns out there are two ways to write literal blocks in Markdown: 

1. indented by four spaces and 
2. surrounded by triple backticks and _not_ indented. 

Tangledown must handle both ways. 

We use the same trick of a harmless group around one of the backticks in the regular expression that recognizes triple backticks so that this regex is safe to run on itself. 

The following function, in noweb `oh-no-there-are-two-ways` recognizes code blocks bracketed by triple backticks. Notice that the `noweb` tag for this block in this here README.md is triple-bacticked, itself. Kind of a funny self-toast joke, no? Tangledown can tangle all the options in Tangledown itself. Mostly, we use indented code blocks when we're talking about noweb and tangle tags, but don't want to run them. They won't run because they're indented, and the regular expressions in noweb `left_justified_regular_expressions` won't match them.

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

#### Accumulate

Tangledown is a little compiler, a silly compiler. We could go all highfalutin' and write it in state-machine and parser-combinator style, and then it would be much bigger, very pretty, and easy to explain to a Haskell programmer or compiler theorist. However, we want to make Tangledown

- very short

- independent of rich libraries like parser combinators

- completely obvious to anyone

We'll just use global variables and array indices and side effects, but in a tasteful way so our friends won't get seasick. This is Python, after all, not highfalutin' Haskell! We can just _get it done_.

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
                pass  # don't do nothin nohow
            else:
                block_lines.append (lines[j][snip:])
```
    
</noweb>

#### Do it already!

The next bit of code is top-level script. It sucks all the `noweb` tags and `tangle` tags out of a file, but doesn't expand any `block` tags that it finds. We use it just to build up internal dictionaries `noweb_blocks` and `tangle_files` with any blocks or file attributes it finds inside noweb or tangle tags.

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

- too many or not enough triple-backtick lines
- broken tags
- dangling tags
- misspelled names
- syntax errors
- infinite loops (hangs)
- much, much more 

We'll get to error handling someday, maybe. Tangledown is just a little toy at the moment, but I thought it interesting to write about. If it's going to be distributed to hostile users, then we will enumerate all the bad cases and handle them. But not now. Let's get the happy case right, first. 

### Second Pass: Expanding Blocks

Iterate over all the `tangle` tag contents and expand the
`block` tags we find in there. Keep going until there are no more `block` tags, because `noweb` blocks are allowed (encouraged!) to refer to other blocks. If there are cycles, this will hang. 

### DUDE! HANG?

We're doing the happy cases first, and will get to cycle detection someday, maybe.

#### There is a `block` tag

First, we need to detect that some list of lines contains a `block` tag, left-justified or not. That means we must keep running the expander on that list.

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

If there is a `block` tag, we must eat the tag and blow out its contents from the dictionary:

<noweb name="eatBlockTag">

```
def eat_block_tag (i, lines):
    for j in range (i, len(lines)):
        end_match = block_end_re.match (lines[j])
        if (end_match):
            return j + 1
        else:  # DUDE!
            pass
```

</noweb>

#### The Expander ####

The following function does one round of block expansion. The caller must check whether any `block` tags remain, and keep running the expander until there are no more `block` tags. Our functional fu might be appalled, but we don't have to be recursive _all the time_. Sometimes it's just easier to iterate.

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

## <a href="tangle_already></a>Tangle It, Already!

Ok, you saw at the top that the code in this here Markdown document, README.md, will read in all the lines in ... this here Markdown document, README.md. Bootstrapping!

But you have to run something first. For that, I tangled the code manually just once and provide `tangledown.py` in the repository.

## DUDE!

Some people like to write "TODO" in their code so they can find all the spots where they thought they might have trouble but didn't have time to write the error-handling (prophylactic) code at the time. I like to write "DUDE" because it sounds like"TODO" but is more rude and funny. 

