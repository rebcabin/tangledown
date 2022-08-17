# Tangledown: One-Step Literate Markdown


### Brian Beckman
### Mon, 15 Aug 2022


## OVERVIEW


You wouldn't build a house without blueprints. You wouldn't write equations without writing rationale. You wouldn't write a theorem without writing a proof. Why would you write code without documentation? Tragically, that's the common practice.


You might rejoin


> I give good names to functions and arguments so I or anyone else can read my code later.


And I say


> That's nice, but it only documents the pieces, and says nothing about how the pieces fit together. It's like giving me a jigsaw puzzle without the box and its picture of what the puzzle looks like when it's assembled. It's not enough. It's almost sadistic.

> The big picture, the rationale, the proofs, the motivation, the "why?", the concept of operations, the architecture, the blueprints, all get lost in the details, literally "lost" as in never written down.

>To understand code without higher-level documentation, you end up reverse-engineering it: running it in a debugger or by tracing printouts. It's the same with mathematics: to understand under-documented mathematics, you create yourself some actual examples and reverse engineer proofs. Likewise, to understand the plumbing of a house with missing or inadequate blueprints, you tear out the walls.

> Don't make me do all that.


[Literate Programming](https://en.wikipedia.org/wiki/Literate_programming) is the best known way to save your _audience_ the work of reverse engineering your code, of giving them the box with the picture of the finished jigsaw puzzle on its top.


Who is your audience?
- yourself, first, especially six months down the line when you're trying to refresh your memory --- "why the heck did I do _that_?!?"
- other programmers, eventually, when they take over the job of maintaining and extending your code


With Literate Programming, you write documentation *first*, and you put your code inside your documentation: your actual, live, running code. The alternative is comments, documentation inside your code. Comments are almost always DOA --- Dead On Arrival. Writers don't keep them up-to-date and readers don't read them.


## Literate-Programming Imperatives


> First, write a paper about your code, explaining, at least to yourself, what you want to do and how you plan to do it. Flesh out your actual code inside the paper. RUN your code inside the paper, capturing printouts and charts and diagrams and what not, so others (including your future self) can see the code at work. Iterate the process, rewriting prose and code as you invent and simplify, in a loop.


Ok, that's just ordinary Jupyter-notebook practice, right? Code inside your documentation, right?


### Jupyter Isn't Exactly Literate Programming


Literate Programming has one difference to ordinary Jupyter-notebook practice. With ordinary Jupyter-notebook practice, you must write everything in ***executable order***, because a Jupyter notebook is just a fancy interface to an underlying execution kernel. Executable order usually forces you to define all details before you use them. With Literate Programming, you don't necessarily write your code in executable order, the order forced by kernels. You write your code in ***human-understandable order***.


Executable order is usually the reverse of the best order for human reasoning. Humans want to understrand the big picture *first*, then the details. They want to see the box-top of the jigsaw puzzle _before_ looking at all the pieces. Executable order is ***upside-down and inside-out***. We've all had the experience of reading Jupyter notebooks backwards so we don't get overwhelmed by details before understanding the big picture. That observation leads us to another imperative.


> Write about your code in human-understandable order. Don't be tyrranized by your programming language into defining everything in full, formal detail before you can talk about anything. Use tools to rearrange your code in executable order.


[Donald Knuth](http://amturing.acm.org/award_winners/knuth_1013846.cfm) invented Literate Programming so that he could both write _about_ [MetaFont](https://en.wikipedia.org/wiki/Metafont) and [TeX](https://texfaq.org/FAQ-lit) and _implement_ them in the same place. These are two of the most important computer programs ever written. Their longevity and quality speak to the viability of Literate Programming.


## What to do with Existing Code?


Literate programming is ***not*** literate reverse engineering. Literate Programming is an inversion of the usual, broken process in software, which is "write the software, then go through hell whilst you write some half-baked, inaccurate, instantly out-of-date, reverse-engineered document about what you did months and years ago!" ***NO!***


When rewriting old code base in literate style, ***detangle*** the existing code into understandable small pieces, rearrange it, and write about it in human-understandable order. To run the code, use a tool like Tangledown to re-tangle the code out to executable order on disk where compilers and interpreters can pick it up and run it, even inside notebook cells.


With a new project, write the documentation *first*, fill in the code, test, revise, etc. Incrementally, interactively, using Markdown *as* your IDE. Write the blueprints _before_ building the house!


***Tangledown*** is a tool that extracts code from any Markdown file into executable order on the disk.


## Tangledown is Inside This Here Document, README.md


This here document, README.md, the one you're reading right now, is, itself, a Literate Program. Because our documentation language is Markdown for [Jupytext](https://github.com/mwouts/jupytext) \[sic\] notebooks, we'll call the language of this document _Literate Markdownn_. This here README.md, which you're reading right now, contains all the source for the Literate-Markdown tool, `tangledown.py`, with all its documentation, all presented in top-down narrative style optimized for human understanding, like a mathematical theory or a story.


`tangledown.py` pulls or ***tangles*** code out of any Markdown document, not just this one (README.md). The verb "tangle" is traditional in Literate Programming. You might think it should be "untangle," because the Markdown document is all tangled up from executable order, from the point of view of build tools. But Knuth prefers the human's point of view. The Markdown document contains the code in the _correct_ order --- the human-understandable order. Build tools need the code all tangled up in executable other, which is effectively arbitrary from the human's point of view.


If we need something _more_ powerful than Tangledown, say to produce publishable LaTeX and PDF files or to run code from multiple languages in one document, we'll go back to [org-babel](http://orgmode.org/worg/org-contrib/babel/) in Emacs (or [spacemacs](http://spacemacs.org/) for you VIM users). Those are much more powerful, best-of-breed Literate-Programming tools. You have to learn some Emacs to use them, and that's an insurmountable barrier for many people. Markdown is good enough for Github, and thus for most of us right now.


Eventually, we will have a **tangledown kernel**, which will let you run any tangledown cells in a Jupytext notebook. For now, you can run _some_ cells in a notebook, specifically those that don't contain `block` tags. A Python kernel can't parse `block` tags, so you will get syntax errors when you evaluate cells that contain `block` tags.


### COLOPHON: Why Writing Matters


Leslie Lamport, Turing-Award Winner, 2013, said, approximately:


> Writing is Nature's Way of showing you how sloppy your thinking is. Coding is Nature's Way of showing you how sloppy your writing is. Testing your code is Nature's Way of showing you how sloppy your coding is.


I once told a flock of interns that, in their first week, they would write their final report. After the usual gasps, eye-rolling, eyebrow-raising, and mutual "he's crazy, idn't he?" glances, I explained why:
- If you wait till the end, you will spend the equivalent of three weeks of sleepless nights trying to remember what you did and why.
- If you commence your research and coding without having thought it out in advance, you will have many false starts and you will waste time backtracking. Writing about it _first_ will force you to _think_, and thinking is good.
- Obviously, you will revise the final report based on what you discover during research and coding. But revising a thought-out document is much more efficient than trying to turn weeks of disorganized, half-remembered decisions into rational discourse at the end of your term.


So I wrote Tangledown by writing this here README.md that you're reading right now, _first_. I slowly, slowly put the code in, revising the documentation as necessary as I went along, and the whole thing took me less than a week of spare time.


Writing good code is like writing mathematics. Good, tested code is like a proof of a theorem, like a solved jigsaw puzzle. Code without documentation is like a pile of equations with no prose explanation, like a house without blueprints, like a jigsaw puzzle without a box top, like Lego bricks without instructions of what to build. It requires expensive reverse engineering to understand it, let alone use it creatively or even just to maintain it. We've all experienced projects wherein the team decided it's just easier to start over from scratch than it is to understand the old code, which isn't correctly documented and is too expensive to reverse-engineer. From my time at Microsoft, I remember a reverse-engineering effort on Microsoft Word, meant to recover the original design of _ExtendedTextOut_ from its assembly-language source of about 20,000 lines. After a large team spent several months on the task, they eventually gave up.


Let's write out the engineering up-front, saving everyone the unnecessary rerverse-engineering work.


To keep testing close to writing, to close Lamport's virtuous loop of writing, thinking, proving, we need to RUN code, bit-by-bit, in our documents. Jupytext is good for that: it keeps a Markdown file and a Jupyter notebook in sync.


### Let Me Tell You a Fun Story


This here README.md, the one you're reading right now, is *literature*, after all, so it should tell a story. Let's tell the story of creating Tangledown itself. We'll use Tangledown to _create_ Tangledown. That's just like bootstrapping a compiler. Just as we compile a compiler with a compiler, we'll use Tangledown to tangle Tangledown itself out of this here document named README.md that you're reading right now.


## DISCLAIMER:


This is a useful toy, but it has zero error handling. This document currently talks only about the happy path.  I try to be rude ("DUDE!") in comments every place where I sense trouble, but I'm only sure I haven't been rude enough. Read this with sense-of-humor bit turned on. This story is supposed to be fun!


## HOW TO RUN TANGLEDOWN:


One way: run `python3 tangledown.py REAMDE.md` at the command line. That command should _overwrite_ tangledown.py. The code for tangledown.py is inside this here README.md that you're reading right now. The name of the file to overwrite, namely `tangledown.py`, is embedded inside this here README.md itself, in the `file` attribute of a `<tangle ...>` tag. Read about `tangle` tags below!


If you said `python3 tangledown.py MY-FOO.md`, then you would be tangling the
code out of `MY-FOO.md`. You'll do that once you start writing your own code in
Tangledown. You will love it! We have some big examples that we'll write about elsewhere. Those examples include embedded code and microcode for exotic hardware, all written in Python!


Tangledown is both a script and a module. You can run Tangledown in a Jupytext cell after importing some stuff from the module. The next cell illustrates the (funny?) bootstrapping joke of tangling Tangledown itself out of this here README.md that you're reading right now. It also tangles an example out to `/dev/null`, discarding it. You'll see that example [below](#section-tangle-tags), where we talk about `tangle` tags.

```python
from tangledown import get_lines, accumulate_lines, tangle_all
tangle_all(*accumulate_lines(get_lines("README.md")))
```

Because Tangledown is a Python module, you can also run Tangledown from inside a standalone Python program, say in PyCharm or VS Code or whatever;
`hello_world_tangler.py` in this repository is an example.

<!-- #region -->
Once again, Jupytext lets you RUN code from a Markdown
document in a Jupyter notebook. If you open `hello_world.md` as a Jupytext
notebook in [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) then you
can run Tangledown in more Jupyter cells. Right-click on the name `hello_world.md` in the JupyterLab GUI and choose


`Open With ...` $\longrightarrow$ `Jupytext Notebook`


Then run cells! This is getting close to the high bar set by org-babel! We can get to that high bar later
by writing a Tangledown kernel for Jupytext (someday, maybe; see [Next Steps](#next-steps) below).
<!-- #endregion -->

## HOW IT WORKS: Markdown Ignores Mysterious Tags


Let's exploit the fact that most markdown renderers, like Jupytext's, Github's, and [PyCharm's](https://www.jetbrains.com/pycharm/), ignore HTML / XML _tags_ (that is, stuff inside angle brackets) that they don't recognize. Let's enclose blocks of real, live code with `noweb` tags, like this:


    <noweb name="my_little_tests">

        class TestSomething (unittest.TestCase):
            """unittest documented here: https://goo.gl/OqCGEx"""
            def test_something (self):
                self.assertEqual (3, 2+1)

    </noweb>


The block above renders as follows. You can see the `noweb` tags by _expanding_ the little tiny, raw cells (pressing _Enter_ on them) above and below the code in Jupytext. You can close those cells up by "running" the cells (pressing _Shift-Enter_ on them). ***DON'T DELETE THE TINY RAW CELLS***.


By the way, there's no point to running the code cell; that won't do anything except tell you that `unittest` isn't defined.


<noweb name="my_little_tests">

```python
    class TestSomething (unittest.TestCase):
        """unittest documented here:
        https://docs.python.org/3/library/unittest.html"""
        def test_something (self):
            self.assertEqual (3, 2+1)
```

</noweb>


The tiny raw cells in the notebook appear in Markdown as `noweb` tags and blank lines surrounding the code. Leave a blank line after the opening `<noweb...>` tag and another blank line before the ending `</noweb>` tag, unless you don't want to render the code like code, with indentation and syntax coloring.


Here's a `noweb` block with no blank lines surrounding the code contents of the `noweb` tags. The `noweb` opening and closing tags aren't rendered, as usual, so _expand_ the cell (press _Enter_ on it) to see them and to see that they don't have blank lines after and before them, respectively.


<noweb name="another_little_test">
    def test_something_else (self):
      self.assertEqual (42, 6 * 7)
</noweb>


Not too pretty, but it's important to know what code looks like in the notebook when you don't leave blank lines. The code looks fine in the Markdown version of the notebook.


## THREE TAGS: noweb, block, and tangle


### `noweb` tags


With or without the blank lines, Markdown won't render the opening `<noweb ...>` and closing `</noweb>` tags themselves. Markdown only renders the material between the opening and closing tags. That material is called the _contents_ of the tags. The word _contents_ is ordinary jargon from HTML, XML, SGML, etc.


**NOTE**: the `name` attribute must be on the same line as the `<noweb ...>` opener. That's just a limitation of the regular expression that detect `noweb` tags. Remeber, Tangledown is still just a toy, a very useful toy, but it's limited.


But `tangledown.py` _doesn't_ ignore the tags. `tangledown.py` is a Python script (and module) that sucks up the contents of the `noweb` tags and sticks them into a dictionary. For the examples above, the dictionary has the keys `my_little_tests` or `another_little_test`. You can see those keys in the Markdown file, or by expanding the little tiny, unlabeled, almost invisible, raw cells that Jupytext renders for the tags. ***DON'T DELETE THE LITTLE TINY, UNLABELED, ALMOST INVISIBLE, RAW CELLS.*** But it's completely safe to expand them (press _Enter_), look at them, close them up (press `Shift-Enter`) even edit them in a notebook.


You can create cells for `noweb` and `tangle` tags in the Markdown file or in the synchronized Jupytext notebook, as _RAW_ cells. If you create them in the notebook, be sure to make them RAW by pressing "R" with the cell highlighted but not editable. If you leave them as _CODE_ cells, Jupyter will think they're Python and will give you syntax errors on them.


### `block` tags


The dictionary key for contents of a `noweb` tag is the string value of the `name` attribute of the `noweb` tag. For example, in this `noweb` tag, `<noweb name="foo">`, `name` is an _attribute_, and its string value is `"foo"`.


Later, Tangledown will blow the contents of a `noweb` back out wherever it sees a `block` tag with the same `name` attribute. That's how you can define some code in one `noweb` and use it in some other  place, later or earlier in your document, in matching `block` tags, more than once if you like. This is kind of like defining a C macro or inline function once and using it many times. The difference, here, with Literate Programming, is that you don't have to write the `noweb` tag in a position before you write a matching `block` tag. You don't have to _define_ things, or even to _name_ them, before you _use_ them. You can refer to a `noweb` tag in a `block` tag _before_ the place where you define the `noweb` tag. You can define things and name things and use things in any order that makes your thinking and your prose more clear.


`block` tags appear in the contents of `noweb` tags and in the in the contets of a `tangle` tags, too. The contents of `block` tags are discarded. Only the `name` attribute matters.


### `tangle` tags <a id="section-tangle-tags"></a>


A `tangle` tag sprays its expanded contents to a file on disk. What file? The file named in the `file` attribute of the `tangle` tag. _Expanding_ contents of a `tangle` tag means replacing every `block` tag with the contents of its matching `noweb` tag, recursively, until everything bottoms out in valid Python.


The same rules about blank lines hold for `tangle` tags as they do for `noweb` tags: if you want Markdown to render the contents like code, surround the contents with blank lines; otherwise, leave the blank lines out. The following


    <tangle file="/dev/null">

        import unittest

        <block name="my_little_tests"></block>

        if __name__ == '__main__':
          unittest.main()

    </tangle>


renders like this


<tangle file="/dev/null">

```python
import unittest

<block name="my_little_tests"></block>

if __name__ == '__main__':
    unittest.main()
```

</tangle>


Notice we discard this file by writing it to `/dev/null`.


Don't evaluate the code cell, you'll get a syntax error because the `block` tag is not valid Python until after tangling. I could make the code cell a raw cell, which never evaluates, but I would lose Python syntax coloring.


## IMPORTANT FOR JUPYTEXT USERS


Jupytext automatically syncs a Markdown file with a Jupyter notebook. If, in JupyterLab, you


- first open README.md
- then you do `View->Activate Command Palette`
- then you check `Pair Notebook with Markdown`
- then you right-click `README.md` and say `Open With -> Jupytext Notebook`
- then if you edit one of the two, `README.md` or `README.ipynb` ...


Jupytext will update the other,


> ***IMPORTANT***: To see the updates, you must `File->Reload Notebook from Disk` or `File->Reload Markdown File from Disk`, as appropriate. Jupytext forces you to reload changed files manually.


If you're reading or modifying `README.ipynb`, or if you `Open With -> Jupytext Notebook` on `README.md` (my preference), you will see tiny raw cells above and below all your tagged nowebs and tangles. ***DON'T DELETE THE TINY RAW CELLS***. Renderers of Markdown simply ignore the tags, but Jupytext makes tiny raw cells out of them!


Don't RUN cells with embedded `block` tags in Jupyter, you'll just get syntax errors from Python, at least until we write a new Tangledown kernel. See the end of this document, and also see `hello_world.ipynb` after you have opened `hello_world.md` and _Paired Notebook With Markdown_; remember the _Activate Command Palette_ GUI?


## YOUR'RE A HUMAN! READ THE NAMES IN THE `block` TAGS!


Markdown renders `block` tags verbatim when they appear in the contents of `noweb` or `tangle` tags. This is good for humans, who will think


> AHA!, this `block` refers to some code in a `noweb` tag somewhere else with the same name. I can read all the details of that code later, when it will make more sense, after I've understood the big picture. I can look at the pieces of the jigsaw puzzle (the `noweb` tags) after I've looked at the picture of the completed puzzle on the box top (the `tangle` tags).

> This here beautifully written document I'm reading right now is making it easy for me to understand the big picture first, because it's breaking things up like this. Thank you, kindly, author! Without you, I'd be awash in details, I'd get tired and cranky before understanding the big picture!


That's exactly what you want for humans: talk about something, name the pieces, show how they fit together, without necessarily defining all the details first.


See, I'll prove it to you. Below is the code for all of `tangledown.py` itself. You can understand this without understanding the _implementations_ of the sub-pieces, just getting an idea of _what_ they do from the names of the `block` tags. **READ THE NAMES IN THE BLOCK TAGS** to get the big picture. Later, if you want to, you can read all the details in the `noweb` tags named by the `block` tags.


***DON'T DELETE THE TINY RAW CELLS*** above and below the code (if you're reading this as a Jupyter notebok with Jupytext).


The code is in _the contents of_ the `tangle` tag. The _contents_ of the `tangle` tag is the stuff between the opening tag `<tangle ...>` and the closing tag `</tangle>`.


I know, we use the word _tag_ to mean three things: the opener `<tangle ...>`, the closer `</tangle>`, or the entire magillah (contents) between the opener `<tangle ...>` and the closer `</tangle>`. Forgive us, will you? I'm not sure any literature on HTML, XML, or SGML is any better about that nomenclature. Again, the contents of _any_ tag `foo` is the stuff between the opener `<foo ...>` and the closer `</foo>`.


The notebook won't render `<tangle ...>`, but will render the contents between `<tangle ...>` and `</tangle>` and will represent `<tangle ...>` and `</tangle>` with tiny raw cells. Those tiny raw cells contain the all-important `tangle` start and end taglets (see, there I invented a disambiguating word). The blank line after the opener `<tangle ...>` and the blank line before the closer `</tangle>` in the Markdown file corresponding to the Jupytext notebook just assist the Markdown renderer to display the contents with syntax coloring.


Here is the whole code for Tangledown itself (don't delete or rearrange the tiny raw cells above and below the code. They contain the opening and closing `tangle` tags).


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
    for k, lines_list in tangle_files.items ():
        Path(k).parents[0].mkdir(parents=True, exist_ok=True)
        contents = []
        for lines in lines_list:
            while there_is_a_block_tag (lines):
                lines = expand_blocks (noweb_blocks, lines)
            contents += lines
        with open (k, 'w') as outfile:
            print(f"WRITING FILE: {k}")
            outfile.write (''.join(contents))

if __name__ == "__main__":
   file_from_sys_argv = get_aFile()
   lines = get_lines(file_from_sys_argv)
   # test_re_matching(lines)
   noweb_blocks, tangle_files = accumulate_lines(lines)
   tangle_all(noweb_blocks, tangle_files)
```

</tangle>


The whole program is in the function `tangle_all`. The business with `__main__` lets the code run as a script. It just calls `tangle_all` after getting and accumulating lines from the given Markdown file.


All we do in `tangle_all` is loop over all the lines (`for k, lines_list in ...`) in the input and substitute something wherever we see a `block` tag (`while there_is_a_block_tag`). What do we substitute? The contents of a `noweb` tag with the same name as the `block` tag. `Expand_blocks` does that job. See how it's implemented [here](#expand-blocks).


The code will create the subdirectories needed. For example, if you tangle to file `foo/bar/baz/qux.py,` the code creates the directory chain `./foo/br/baz/` if it doesn't exist. (DUDE! the code won't create subdirectories under `~`, my home directory! Figure it out and fix it!)


The code will also accumulate output for `tangle` files mentioned more than once. If you tangle to `qux.py` in one place and then also tangle to `qux.py` somewhere else, the second tangle won't overwrite the first, but append to it. That's why the loop `for k, lines_list in tangle_files...` actually loops over _lists_ of lines. Each list contains all the lines for a given output file.


You can run Tangldedown as a script or  import it as a module. We get that hybrid vigor by the standard Python trick of testing `__name__` against `"__main__"`.


We'll implement the blocks, like `accumulate_contents` and `eatBlockTag`, later. You can read about them, or not, after you've gotten the big picture. 


Notice the `name` attributes of `noweb` and matching `block` tags can contain spaces, can be in kebab-case, Pascal-case, camel-case, snake-case, whatever you like.


`block` tags don't need any contents, but you're welcome to put some in, say for in-code commentary. Tangledown will eat and ignore contents of a `block` tag. With Tangledown, in-code commentary is less important than it is in normal (tragically flawed!) code, however, because your commentary for _humans_ is the text _surrounding_ the `block` tags, Markdown text like the text you're reading right here and now.


## Tangledown Tangles Itself?


Tangledown uses two kinds of regular expressions (regexes) for matching tags in any Markdown file:
- regexes for `noweb` and `tangle` tags that appear on lines by themselves, left-justified
- regexes that match `<block ...>` tags that may appear anywhere on a line, and match their closing `</block>` taglets, which may appear on the same line as their opening, twin `<block ...>` taglets on lines by themselves.


Both kinds of regex are _safe_, in the sense that they do not match themselves. That means it's safe to run
`tangledown.py` on this here `READMD.md`, which contains source for `tangledown.py`.


The two regexes defined in the noweb `left_justified_regexes` match `noweb` and`tangle` tags that appear on lines by themselves, left-justified. These regexes won't match themselves; that's our bootstrapping technique. They also wont match `noweb` and `tangle` tags that are indented. That lets us _talk about_ `noweb` and `tangle` tags: just put the examples you're talking about in an _indented_ Markdown code cell instead of in a triple-backticked code cell with no indentation.


The names in the attributes of `noweb` and `tangle` tags must start with a letter, and they can contain letters, numbers, hyphens, underscores, whitespace, and dots. That's what is said by the regexes in noweb `left_justified_regexes`, right here, this next noweb:


## noweb left_justified_regexes


<noweb name="left_justified_regexes">

```python
noweb_start_re = re.compile (r'^<noweb name="(\w[\w\s\-\.]*)">$')
noweb_end_re = re.compile (r'^</noweb>$')

tangle_start_re = re.compile (r'^<tangle file="(.+\/\\[^\/]+|.+)">$')
tangle_end_re = re.compile (r'^</tangle>$')
```

</noweb>


## noweb anywhere_regexes


The regexes in this noweb, `anywhere_regexes`, matches `block` tags that may appear anywhere on a line. The regex preserves leading white space so that indented `block` tags indent the contents of their `noweb` brethren appropriately. The `block_end_re` regex also preserves leading white space so it's indented the same as its twin opening `block-start` regex. I converted the 'o' in 'block' to a harmless regex group `[o]` so that _block_end_ doesn't match itself. That makes it safe to run this code on this here document itself.


<noweb name="anywhere_regexes">

```python
block_start_re = re.compile (r'^(\s*)<block name="(\w[\w\s\-\.]*)">')
block_end_re = re.compile (r'^(\s)*</bl[o]ck>')
```

</noweb>


## Test the Regular Expressions


### noweb openers


The code in noweb `openers` has two `block` tags that refer to the nowebs of the regexes defined above, namely `left_justified_regexes` and `anywhere_regexes`. After Tangledown substitutes the contents of the nowebs for the blocks, the code becomes valid Python and you can run it. When you run it, it proves that we can recognize all the various kinds of tags. We leave the regexes themselves as global pseudo-constants so that they're both easy to test and to use in the body of the code.


The code in `hello_world.ipynb` (after you have Paired a Notebook with the Markdown File `hello_world.md`) runs this test as its last act to check that `tangledown.py` was correctly tangled from this here `README.md`


Notice the special treatment for block ends, which are usually on the same lines as their block opener tags, but not necessarily so. That's what lets you put (useless) contents in `block` tags.


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


Tangledown operates in two passes, once over the file to collect `noweb` and `tangle` tags, and a second time over the `tangle` tags that it collected in the first pass to expand `block` tags. That is, in the second pass, Tangledown substitutes noweb contents for corresponding `block` tags until there are no more, creating valid code that it writes to disk if the markdown is correctly written.


### Getting a File Name


`tangledown.py` is both a script and a module. As a script, you run it from the command line, so it gets its input file name from command-line arguments. As a module, called from another Python program, you probably want to give the file as an argument to a function, specifically, to `get_lines`.


Let's write two functions, `get_aFile`, which parses command-line arguments, and `get_lines`, which gets lines, without processing them, from a file denoted by its argument, `aFilename`.


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


In the first pass over the file, we'll just save the contents of noweb and tangle into dictionaries, without expanding nested `block` tags.


#### Oh no! There are two ways!


Turns out there are two ways to write literal blocks in Markdown:


1. indented by four spaces and
2. surrounded by triple backticks and _not_ indented.


Tangledown must handle both ways.


We use the trick of a harmless regex group --- stuff inside square brackets --- around one of the backticks in the regex that recognizes triple backticks. Now this regex is safe to run on itself. See `triple_backtick_re` in the code immediately below.


The function `first_non_blank_line_is_triple_backtick`, in noweb `oh-no-there-are-two-ways` recognizes code blocks bracketed by triple backticks. Notice that the contents of this `noweb` tag  is triple-bacticked, itself. Kind of a funny self-toast joke, no?


Mostly, we use indented code blocks, not triple-backticked, when we're talking about `noweb` and `tangle` tags, but don't want to process them. Tangledown won't process indented `noweb` and `tangle` tags because they're indented, and the regexes in noweb `left_justified_regexes` won't match them.


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


Tangledown is a funny little compiler. We could go all highfalutin' and write it in state-machine and parser-combinator style, and then it would be much bigger, more elaborate if not more elegant, and easier to explain to a Haskell programmer or compiler theorist. It might also be less of a toy. However, we want to make this toy Tangledown


- very short
- independent of rich libraries like parser combinators
- completely obvious to anyone


We'll just use iteration and array indices in a tasteful way so our functional friends won't get seasick. This is Python, after all, not highfalutin' Haskell! We can just _get it done_.


The function `accumulate_contents` accumulates the contents of `noweb` or `tangle` tags. Remember that `block` tags don't have meanigful contents. The function starts at line `i`, then figures out whether a tag's first non-blank line is triple backtick, in which case it _won't_ snip four spaces from the beginning of every line, and finally keeps going until it sees the closing taglet, `</noweb>` or `</tangle>`.


#### noweb accumulate-contents


<noweb name="accumulate-contents">

```python
def accumulate_contents (lines, i, end_re):
    if (first_non_blank_line_is_triple_backtick (i, lines)):
        i = i + 1 # eat the line containing triple backticks
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


The function `accumulate_lines` sucks the contents of all the `noweb` tags and `tangle` tags out of a file, but doesn't expand any `block` tags that it finds. It just builds up dictionaries, `noweb_blocks` and `tangle_files`, with any `name` or `file` attributes it finds inside `noweb` or `tangle` tags. 


The names of `noweb` tags must be globally unique within the Markdown file. Multiple `tangle` tags may refer to the same output file, in which cases, the contents of the second and subsequent `tangle` tags will be appended to a list of lines.


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
            if not (file_key in tangle_files):
                tangle_files[file_key] = []
            tangle_files[file_key] += \
                [accumulate_contents(lines, i + 1, tangle_end_re)[1]]
    return noweb_blocks, tangle_files
```

</noweb>


### DUDE!


There is a lot that can go wrong. We can have all kinds of mal-formed contents:


- too many or not enough triple-backtick lines
- indentation errors
- broken tags
- dangling tags
- misspelled names
- syntax errors
- infinite loops (cycles, hangs)
- much, much more


We'll get to error handling someday, maybe. Tangledown is just a little toy at the moment, but I thought it interesting to write about. If it's ever distributed to hostile users, then we will handle all the bad cases. But not now. Let's get the happy case right.


### Second Pass: Expanding Blocks


Iterate over all the `tangle` tag contents and expand the
`block` tags we find in there, recursively. That means keep going until there are no more `block` tags, because nowebss are allowed (encouraged!) to refer to other nowebs via `block` tags. If there are cycles, this will hang.


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


#### noweb expandBlocks<a id="expand-blocks"></a>


The following function does one round of block expansion. The caller must test whether any `block` tags remain, and keep running the expander until there are no more `block` tags. Our functional fu grandmaster might be appalled, but sometimes it's just easier to iterate than to recurse.


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


Ok, you saw at the top that the code in this here Markdown document, README.md, when run as a script, will read in all the lines in ... this here Markdown document, `README.md`. Bootstrapping!


But you have to run something first. For that, I tangled the code manually just
once and provide `tangledown.py` in the repository. The chicken definitely comes
before the egg.


But if you have the chicken (`tangledown.py`), you can import it as a module and execute the following cell. That should overwrite `tangledown.py` with the contents of this notebook or Markdown file. So our little bootstrapping technique will forever update the compiler if you change it in this here README.md that you're reading right now!

```python
from tangledown import get_lines, accumulate_lines, tangle_all
tangle_all(*accumulate_lines(get_lines("README.md")))
```

## DUDE!


Some people write "TODO" in their code so they can find all the spots where they thought they might have trouble but didn't have time to write the error-handling (prophylactic) code at the time. I like to write "DUDE" because it sounds like both "TODO" but is more RUDE (also sounds like "DUDE") and funny. This story is supposed to be amusing.


## Next Steps


- modern Pythonic Type Annotation (PEP 484)
- more examples
- error handling (big job)
- Jupytext kernel for `tangledown` so we can run `noweb` and `block` tags that have `block` tags in them.

```python

```
