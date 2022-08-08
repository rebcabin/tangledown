# Tangledown: One-Step Literate Markdown


### Brian Beckman
### 5 Aug 2022


## DISCLAIMER:


This is a toy. It's a useful toy, but it has zero error handling. This document currently talks only about the happy path.  I try to be rude ("DUDE!") in comments every place where I sense trouble, but I'm only sure I haven't been rude enough. Read this with sense-of-humor bit turned on.


## OVERVIEW


- README.md files are mandatory, or really should be, in projects.

- README.md files should be authoritative and complete. README.md files that _can't_ get out of sync with code are best.

- Let's put _all the real, live code_ for a project inside README.md, along with authoritative documentation. When you modify one, modify the other along with it.

- Let's write README.md for human reasoning and understanding, that is, _top-down_ instead of _bottom-up_. Let's help readers understand the big picture before overwhelming them with implementation details.

- Let's create a tool to suck the code out of README.md and rearrange it on disk in some other order required by build tools, debuggers, and IDEs.


I just described a kind of [Literate Programming](https://en.wikipedia.org/wiki/Literate_programming), a method of software documentation invented by [Donald Knuth](http://amturing.acm.org/award_winners/knuth_1013846.cfm). Knuth wrote MetaFont and TeX in literate style. Those are two of the most important programs ever written. In a blatant appeal to authority and celebrity, doesn't that mean Literate Programming is good enough for everyone?


This here document, README.md, the one you're reading right now, is, itself, a Literate Program. Because our documentation language is Markdown, we'll call the language of this document _Literate Markdown_. This here README.md that you're reading right now contains all the source for the Literate-Markdown tool called `tangledown.py`, with all its documentation, all presented in narrative style, like a story or a mathematical theory.


_Tangledown.py_ pulls or _tangles_ code out of any Markdown document, not just this one (README.md). The verb "tangle" is traditional in Literate Programming. You might think it should be "untangle," because the Markdown document is all tangled up from the point of view of build tools. But Knuth prefers the human's point of view. The Markdown document contains the code in the _correct_ order --- the order for human reasoning and understanding. Build tools need the code all tangled up in some other, effectively arbitrary order.


If we need something _more_ powerful than Tangledown, say to produce publishable LaTeX and PDF files, we'll go back to [org-mode](http://orgmode.org/) and [org-babel](http://orgmode.org/worg/org-contrib/babel/) in Emacs (or [spacemacs](http://spacemacs.org/) for you VIM users). Those are much more powerful, best-of-breed, classical Literate-Programming tools. You have to learn some Emacs to use them, and that's an insurmountable barrier for many people. Markdown is good enough for Github, and thus for almost everyone.


## HOW TO RUN TANGLEDOWN:


One way: run `python3 tangledown.py REAMDE.md` at the command line. That command should _overwrite_ tangledown.py. The code for tangledown.py is inside README.md. The name of the file to overwrite, namely `tangledown.py` is embedded inside README.md itself, in the `file` attribute of a `<tangle>` tag. Read about them below!


If you said `python3 tangledown.py MY-FOO.md`, then you would be tangling the
code out of `MY-FOO.md`. You'll do that once you start writing your own code in
Tangledown. You will love it!


You can also run tangledown from inside a python program;
`hello_world_tangler.py` is an example.
[Jupytext](https://github.com/mwouts/jupytext) lets you RUN code from a Markdown
document in a Jupyter notebook. If you open `hello_world.md` as a Jupytext [sic]
notebook in [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) then you
can run Tangledown in Jupyter cells. It's very, very cool and is getting close
to the high bar set by org-babel!


## HOW IT WORKS: Markdown Ignores Mysterious Tags


Let's exploit the fact that most markdown renderers, like Github's and [PyCharm's](https://www.jetbrains.com/pycharm/), ignore HTML / XML _tags_ (that it, stuff inside angle brackets) that they don't recognize. Let's enclose blocks of real, live code with `noweb` tags, like this:


    <noweb name="my_little_tests">

        class TestSomething (unittest.TestCase):
            """unittest documented here: https://goo.gl/OqCGEx"""
            def test_something (self):
                self.assertEqual (3, 2+1)

    </noweb>


The block above renders as follows:

```python
    class TestSomething (unittest.TestCase):
        """unittest documented here:
        https://docs.python.org/3/library/unittest.html"""
        def test_something (self):
            self.assertEqual (3, 2+1)
```

Leave a blank line after the opening `<noweb...>` tag and another blank line before the ending `</noweb>` tag, unless you don't want to render the code like code. Here's a non-rendered `noweb` block --- no blank lines surrounding the contents of the `noweb` tag:


<noweb name="another_little_test">
    def test_something_else (self):
      self.assertEqual (42, 6 * 7)
</noweb>


Not too pretty, but it's important to know what happens when you don't leave blank lines.


## THREE TAGS: noweb, block, and tangle


With or without the blank lines, Markdown won't render the opening `<noweb>` and closing `</noweb>` tags themselves. Markdown only renders the material between the tags, the _contents_ of the tags.


But `tangledown.py` _doesn't_ ignore the tags. `tangledown.py` is a Python script (and module) that sucks up the contents of the `noweb` tags and sticks them into a dictionary. For the examples above, the dictionary has the keys `my_little_tests` or `another_little_test`.


The dictionary key for a noweb block is the string value of the `name` attribute of the `noweb` tag. Later, Tangledown will blow those lines back out wherever it sees a `block` tag with the same name. That's how you can define some code in one `noweb` and use it later in matching `block` tags, more than once if you like, kind of like defining a C macro or inline function once and using it many times. The difference, here, with Literate Programming, is that you don't have to _define_ things before you _use_ them. You can define and use in any order that makes your prose more clear..


Often, a `block` tag will be inside a `tangle` tag that sprays its expanded contents to a file on disk. What file? The file named in the `file` attribute of the `tangle` tag. `block` tags can also be inside `noweb` tags, so one noweb can talk about another noweb without implementing it first.


The same rules about blank lines hold for `tangle` tags as they do for `noweb` tags: if you want Markdown to render the contents like code, surround the contents with blank lines; otherwise, leave the blank lines out. The following


    <tangle file="a_unit_testing_sample.py">

        import unittest

        <block name="my_little_tests"></block>

        if __name__ == '__main__':
          unittest.main()

    </tangle>


renders like this

```python
import unittest

<block name="my_little_tests"></block>

if __name__ == '__main__':
    unittest.main()
```

## IMPORTANT FOR JUPYTEXT USERS


Jupytext automatically syncs a Markdown file with a Jupyter notebook. If you open README.md in Jupyter Lab, then `View->Activate Command Palette`, then check `Pair Notebook with Markdown`, then if you edit one of the two, Jupytext will update the other. Though to see the updates, you must `File->Reload Notebook from Disk` or `File->Reload Markdown File from Disk`, as appropriate.


If you're reading or modifying README.md as a Jupyter notebook, that is, if you are reading or modifying README.ipynb, you will see tiny cells above and below all your tagged nowebs, blocks, and tangles. *DON'T DELETE THEM*. Markdown renderers simply ignore the tags, but Jupytext makes tiny cells out of them!


You also probably don't want to RUN tagged blocks in Jupyter, but you DO want to run some blocks of code. See `hello_world.ipynb` after you have opened `hello_world.md` and Paired Notebook With Markdown; remember the Activate Command Palette GUI?


## YOUR'RE A HUMAN! READ THE NAMES IN THE `block` TAGS!


Markdown renders `block` tags verbatim to the documentation. This is good for humans, who will think


> AHA!, this `block` refers to some code in a `noweb` tag with the same name that I can read some other place and time.


> This here beautifully written document I'm reading right now is making it easy for me to understand the big picture first, because it's breaking things up like this. Thank you, kindly, author! Without you, I'd be awash in details, I'd get tired and cranky before understanding the big picture!


That's exactly what you want for humans: talk about something in a place where you don't necessarily _implement_ it. But compilers usually need the full implementation of the block _right here and now_ before it's ever used.


See, I'll prove it to you. Here is the code for the whole program. You can understand this without understanding the _implementations_ of the sub-pieces, just getting an idea of _what_ they do from the names of the `block` tags. READ THE NAMES IN THE BLOCK TAGS to get the big picture.


All we do in the code below the block tags, in function `tangle_all`, is loop over all the lines in the input and substitute something wherever we see a `block` tag. What do we substitute? The contents of a `noweb` tag with the same name as the name mentioned in the `block` tag.


This program can run as a script or can be imported as a module. We get that hybrid vigor by the standard Python trick of testing `__name__` against `"__main__"`.


Now, if you're reading this as a Jupyter notebook in Jupytext (as explained above), you'll see a little tiny cell just before the code below and just after the code below. This code is in _the contents of_ a `tangle` tag. The _contents_ of any tag `foo` is the stuff between the opening tag `<foo>` and the closing tag `</foo>`. I know, we use the word _tag_ to mean three things: the opener `<foo>`, the closer `</foo>`, or the entire magilla between the opener `<foo>` and the closer `</foo>`. Forgive us, will you? I'm not sure any literature on HTML, XML, or SGML is any better about that nomenclature.


The notebook won't render `<tangle ...>`, but will render the contents between `<tangle ...>` and `</tangle>` and will represent `<tangle ...>` and `</tangle>` with tiny cells. Those tiny cells contain the all-important `tangle` start and end taglets (see, there I invented a disambiguating word).


DON'T DELETE THE TINY CELLS (if you're reading this as a Jupyter notebok with Jupytext)


<tangle file="tangledown.py">

```python
<block name="openers"></block>
<block name="oh-no-there-are-two-ways"></block>
<block name="accumulate-contents"></block>
<block name="accumulate-lines"></block>
<block name="thereIsABlockTag"></block>
<block name="eatBlockTag"></block>
<block name="expandBlocks"></block>

from pathlib import Path
def tangle_all(noweb_blocks, tangle_files):
    for k, v in tangle_files.items ():
        Path(k).parents[0].mkdir(parents=True, exist_ok=True)
        with open (k, 'w') as outfile:
            lines = v
            while there_is_a_block_tag (lines):
                lines = expand_blocks (noweb_blocks, lines)
            for line in lines:
                outfile.write (line)

if __name__ == "__main__":
   file_from_sys_argv = get_aFile()
   lines = get_lines(file_from_sys_argv)
   test_re_matching(lines)
   noweb_blocks, tangle_files = accumulate_lines(lines)
   tangle_all(noweb_blocks, tangle_files)
```

</tangle>


We'll implement those block tags, like `accumulate_contents` and `eatBlockTag`, later, after you've gotten the big picture. Notice the names can contain spaces, can be in kebab-case, Pascal-case, camel-case, snake-case, whatever you like.


`block` tags don't need any contents, but you're welcome to put some in, say for in-code commentary. Tangledown will eat and ignore contents of a `block` tag. With Tangledown, in-code commentary is less important than it is in normal code, however, because your commentary for _humans_ is the text _surrounding_ the `block` tags, Markdown text like the text you're reading right here and now.


## BOOTSTRAPPING, Step-by-Step<a name="bootstrapping"></a>


This here README.md that you're reading right now is literature, after all, so it should tell a story. Let's tell the story of creating Tangledown. We'll use Tangledown to _create_ Tangledown. That's just like bootstrapping a compiler. Just as we compile a compiler with a compiler, we'll use Tangledown to tangle Tangledown itself out of this here document named README.md that you're reading right now.


### Tangledown Tangles Itself?


Tangledown uses two kinds of regular expressions (regexes) for matching tags in any Markdown file: regexes for tags that appear on lines by themselves, left-justified, and regexes that match tags that may appear anywhere on a line. Both kinds are _safe_, in the sense that they do not match themselves. That means it's safe to run
`tangledown.py` on `READMD.md`, which contains source for `tangledown.py`, including those two kinds of regexes. We need to ensure the regexes don't match themselves, otherwise Tangledown will get lost.


The two regexes defined in the noweb `left_justified_regexes` match `noweb` and`tangle` tags that appear on lines by themselves, left-justified. These regexes won't match themselves; that's our bootstrapping technique. They also wont match `noweb` and `tangle` tags that are indented. That lets us _talk about_ `noweb` and `tangle` tags: just put the examples you're talking about in an indented Markdown code blob instead of in a triple-backticked code blob with no indentation.


The names in the attributes of `noweb` and `tangle` tags must start with a letter, and they can contain letters, numbers, hyphens, underscores, whitespace, and dots. That's what is said by the regexes in noweb `left_justified_regexes`, right here, this next one:


#### noweb left_justified_regexes


<noweb name="left_justified_regexes">

```python
noweb_start_re = re.compile (r'^<noweb name="([\w\s\-\.]+)">$')
noweb_end_re = re.compile (r'^</noweb>$')

tangle_start_re = re.compile (r'^<tangle file="(.+\/\\[^\/]+|.+)">$')
tangle_end_re = re.compile (r'^</tangle>$')
```

</noweb>


The regexes in noweb `anywhere_regexes` matches `block` tags that may appear anywhere on a line. The regex preserves leading white space so that indented `block` tags indent their `noweb` brethren appropriately. The `block-end` regex also preserves leading white space so it can be checked against its twin opening `block-start` regex. I converted the 'o' in 'block' to a harmless regex group `[o]` so that _block_end_ doesn't match itself. That makes it safe to run this code on this here document itself.


#### noweb anywhere_regexes


<noweb name="anywhere_regexes">

```python
block_start_re = re.compile (r'^(\s*)<block name="([\w\s\-\.]+)">')
block_end_re = re.compile (r'^(\s)*</bl[o]ck>')
```

</noweb>


### Test the Regular Expressions


The code in noweb `openers` has two `block` tags that refer to the nowebs of the regexes defined above, namely `left_justified_regexes` and `anywhere_regexes`. After Tangledown substitutes the contents of the nowebs, the code becomes valid Python and you can run it. When you run it, it proves that we can recognize all the various kinds of tags. We leave the regexes themselves as global pseudo-constants so that they're easy to test and to use in the body of the code.


The code in `hello_world.ipynb` (after you have Paired a Notebook with the Markdown File) runs this test as its last act to check that `tangledown.py` was correctly tangled from `README.md`


Notice the special treatment for block ends, which will usually be on the same lines as their block tags, but not necessarily so.


#### noweb openers


<noweb name="openers">

```python
import re
import sys

<block name="getting a file and its lines"></block>
<block name="left_justified_regexes"></block>
<block name="anywhere_regexes"></block>

def test_re_matching(lines):
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
```

</noweb>


## TANGLEDOWN: Two Passes


Tangledown operates in two passes, once over the file and a second time over the tangle tags that it collected in the first pass. In the second pass, Tangledown does the substitution for block tags, creating valid code on the disk if the markdown is correctly written.


### Getting a File Name


`tangledown.py` is both a script and a module. As a script, you run it from the command line, so it gets its input file name from the command-line arguments. As a module, called from another Python program, you probably want to give the file as an argument to a function. See `hello_world_tangler.py` and `hello_world.md` for examples.


Let's write two functions, `get_aFile`, which parses command-line arguments, and `get_lines`, which gets lines from a file denoted by its argument, `aFilename`.


`get_aFile` can parse command-line arguments that come from either `python` on the command line or from a `Jupitext` notebook, which has a few kinds of command-line arguments we must ignore, namely command-line arguments that end in `.py` or in `.json`.


#### noweb getting a file and its lines


<noweb name="getting a file and its lines">

```python
def get_aFile():
    """Get a file name from the command-line arguments."""
    print({f'len(sys.argv)': len(sys.argv), f'sys.argv': sys.argv})
    aFile = 'README.md'
    if len(sys.argv) > 1:
        file_names = [p for p in sys.argv
                        if (p[0] != '-')  # option
                           and (p[-3:] != '.py')
                           and (p[-5:] != '.json')]
        if file_names:
            aFile = sys.argv[1]
    return aFile

def get_lines(aFilename):
    """Get lines from a file denoted by aFilename."""
    with open(aFilename) as aFile:
        return aFile.readlines ()
```

</noweb>


### First Pass: Saving Noweb and Tangle Blocks


In the first pass over the file, we'll just save the noweb and tangle contents into dictionaries, without expanding nested `block` tags.


#### Oh no! There are two ways!


Turns out there are two ways to write literal blocks in Markdown:


1. indented by four spaces and
2. surrounded by triple backticks and _not_ indented.


Tangledown must handle both ways.


We use the same trick of a harmless group around one of the backticks in the regex that recognizes triple backticks so that this regex is safe to run on itself.


The following function, in noweb `oh-no-there-are-two-ways` recognizes code blocks bracketed by triple backticks. Notice that the `noweb` tag for this block in this here README.md is triple-bacticked, itself. Kind of a funny self-toast joke, no? Tangledown can tangle all the options in Tangledown itself.


Mostly, we use indented code blocks when we're talking about noweb and tangle tags, but don't want to process them. Tangledown won't process them because they're indented, and the regexes in noweb `left_justified_regexes` won't match them.


#### noweb oh-no-there-are-two-ways


<noweb name="oh-no-there-are-two-ways">

```python
triple_backtick_re = re.compile (r'^`[`]`')
blank_line_re      = re.compile (r'^\s*$')

def first_non_blank_line_is_triple_backtick (i, lines):
    while (blank_line_re.match (lines[i])):
        i = i + 1
    return triple_backtick_re.match (lines[i])
```

</noweb>


#### Accumulate Contents


Tangledown is a silly little compiler. We could go all highfalutin' and write it in state-machine and parser-combinator style, and then it would be much bigger, prettier, and easy to explain to a Haskell programmer or compiler theorist. However, we want to make Tangledown


- very short
- independent of rich libraries like parser combinators
- completely obvious to anyone


We'll just use iteration and array indices in a tasteful way so our functional friends won't get seasick. This is Python, after all, not highfalutin' Haskell! We can just _get it done_.


The function `accumulate_contents` starts at line `i`, then figures out whether a tag's first non-blank line is triple backtick, in which case it _won't_ snip four spaces from the beginning of every line, and finally keeps going until it sees the end of the tag. This function accumulates the contents of `noweb` or `tangle` tags. Remember that `block` tags don't have meanigful contents.


#### noweb accumulate-contents


<noweb name="accumulate-contents">

```python
def accumulate_contents (lines, i, end_re):
    if (first_non_blank_line_is_triple_backtick (i, lines)):
        i = i + 1 # eat the line
        snip = 0
    else:
        snip = 4
    contents_lines = []
    for j in range (i, len(lines)):
        end_match = end_re.match(lines[j])
        if (end_match):
            # This is the only place we return!
            return j + 1, contents_lines
        else:
            if (snip == 0 and triple_backtick_re.match (lines[j])):
                pass  # don't do nothin nohow
            else:
                contents_lines.append (lines[j][snip:])
```

</noweb>


#### Do it already!


The function `accumulate_lines` sucks all the `noweb` tags and `tangle` tags out of a file, but doesn't expand any `block` tags that it finds. It just builds up dictionaries `noweb_blocks` and `tangle_files` with any code or file attributes it finds inside noweb or tangle tags.


#### noweb accumulate-lines


<noweb name="accumulate-lines">

```python
def accumulate_lines(lines):
    noweb_blocks = {}
    tangle_files = {}
    for i in range(len(lines)):
        noweb_start_match = noweb_start_re.match (lines[i])
        tangle_start_match = tangle_start_re.match (lines[i])
        if (noweb_start_match):
            block_key = noweb_start_match.group (1)
            i, noweb_blocks[block_key] = \
                accumulate_contents(lines, i + 1, noweb_end_re)
        elif (tangle_start_match):
            file_key = tangle_start_match.group (1)
            i, tangle_files[file_key] = \
                accumulate_contents(lines, i + 1, tangle_end_re)
    return noweb_blocks, tangle_files
```

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


We'll get to error handling someday, maybe. Tangledown is just a little toy at the moment, but I thought it interesting to write about. If it's ever distributed to hostile users, then we will handle all the bad cases. But not now. Let's get the happy case right.


### Second Pass: Expanding Blocks


Iterate over all the `tangle` tag contents and expand the
`block` tags we find in there. Keep going until there are no more `block` tags, because `noweb` blocks are allowed (encouraged!) to refer to other blocks. If there are cycles, this will hang.


### DUDE! HANG?


We're doing the happy cases first, and will get to cycle detection someday, maybe.


#### noweb thereIsABlockTag


First, we need to detect that some list of lines contains a `block` tag, left-justified or not. That means we must keep running the expander on that list.


<noweb name="thereIsABlockTag">

```python
def there_is_a_block_tag (lines):
    for line in lines:
        block_start_match = block_start_re.match (line)
        if (block_start_match):
            return True
    return False
```

</noweb>


#### noweb eatBlockTag


If there is a `block` tag, we must eat the tag and its meaningless contents:


<noweb name="eatBlockTag">

```python
def eat_block_tag (i, lines):
    for j in range (i, len(lines)):
        end_match = block_end_re.match (lines[j])
        # DUDE! Check leading whitespace against block_start_re
        if (end_match):
            return j + 1
        else:  # DUDE!
            pass
```

</noweb>


#### noweb expandBlocks


The following function does one round of block expansion. The caller must test whether any `block` tags remain, and keep running the expander until there are no more `block` tags. Our functional fu might be appalled, but sometimes it's just easier to iterate than to recurse.


<noweb name="expandBlocks">

```python
def expand_blocks (noweb_blocks, lines):
    out_lines = []
    for i in range (len (lines)):
        block_start_match = block_start_re.match (lines[i])
        if (block_start_match):
            leading_whitespace = block_start_match.group (1)
            block_key = block_start_match.group (2)
            block_lines = noweb_blocks [block_key]  # DUDE!
            i = eat_block_tag (i, lines)
            for block_line in block_lines:
                out_lines.append (leading_whitespace + block_line)
        else:
            out_lines.append (lines[i])
    return out_lines

```

</noweb>


## Tangle It, Already!<a id="tangle_already"></a>


Ok, you saw at the top that the code in this here Markdown document, README.md, when run as a script, will read in all the lines in ... this here Markdown document, README.md. Bootstrapping!


But you have to run something first. For that, I tangled the code manually just
once and provide `tangledown.py` in the repository. The chicken definitely comes
before the egg.


But if you have the chicken (`tangledown.py`), you can import it as a module and execute the following cell. That should overwrite `tangledown.py` with the contents of this notebook or Markdown file.

```python
from tangledown import get_lines, accumulate_lines, tangle_all
tangle_all(*accumulate_lines(get_lines("README.md")))
```

## DUDE!


Some people write "TODO" in their code so they can find all the spots where they thought they might have trouble but didn't have time to write the error-handling (prophylactic) code at the time. I like to write "DUDE" because it sounds like"TODO" but is more rude and funny.


## Next Steps


- modern Pythonic Type Annotation (PEP 484)
- more examples
- error handling (big job)

```python

```
