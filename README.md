# Tangledown: One-Step Literate Markdown


#### Brian Beckman
#### Tue, 30 Aug 2022
#### v0.0.5


## OVERVIEW


### SOFTWARE AS LITERATURE


You're writing a murder mystery. METHOD 1: You introduce a data sheet with all the characters and their relationships to all the other characters. Francis stands to inherit, but Evelyn has a life-insurance policy on Victor. Bobbie is strong enough to swing an axe. Alice has poisonous plants in her garden. Charlie has a gun collection. Danielle is a chef and owns sharp knives. You lay out their schedules and whereabouts for several weeks. After presenting the data sheet, you write down the murder and the solution. 


METHOD 2: There's a murder. Your romantic detective asks "Who knew whom? Who benefitted? Who could have been at the scene of the crime? What was the murder weapon? Who could have done it?"


If your objective is to _engage_ the audience, to motivate them to unravel the mystery and learn the twists and turns along the way, which is the better method? If your objective is to have them spend several hours trying to guess where this is all going, which is the better method?


Now, you're writing about some complex software. METHOD 1: You present all the functions and interfaces, cross dependencies, asynchronous versus synchronous, global and local state variables, possibilities for side effects. Finally, you present unit tests and a main program.


METHOD 2: You present the unit tests and main program first, its rationale and concept of operation, the solution it delivers, its modes and methods. Finally, you present all the functions, interfaces, and procedures, all the bits and bobs that could effect the solution.


If your objective is to _engage_ your audience, to have them understand the software deeply, as if they had written it themselves, which is the better method? If your objective is to have them spend several hours in fits and starts trying to guess what you mean, which is the better method?


### SOFTWARE AS DOCUMENTATION


Tragically, the standard level of documentation in software forces every reader to reverse-engineer software.


You say:


> I give good names to functions and parameters to make my code readable. I use Doxygen and Sphinx to document parameters and return types. _I'm a professional!_


And I say


> That's nice, but it only documents the pieces, and says nothing about how the pieces fit together. It's like giving me a jigsaw puzzle without the box top. It's almost sadistic.

> The big picture, the rationale, the goals and objectives, the proofs, the motivation, the "what" and the "why?", the concept of operations, the architecture, the methaphorical blueprints, where is that?

> You condemn me to reverse-engineering your software: to run it in a debugger or to trace printouts. 

> Don't make me do all that.


### LITERATE PROGRAMMING


[Literate Programming](https://en.wikipedia.org/wiki/Literate_programming) is the best known way to save your _audience_ the work of reverse engineering your code, of giving them the box top with the jigsaw puzzle.


Who is your audience?

- yourself, first, down the line, trying to remember "why the heck did I do _that_?!?"

- other programmers, eventually, when they take over maintaining and extending your code


### COLOPHON: Why Writing Matters


Leslie Lamport, Turing-Award Winner, 2013, said, approximately:


> Writing is Nature's Way of showing you how sloppy your thinking is. Coding is Nature's Way of showing you how sloppy your writing is. Testing is Nature's Way of showing you how sloppy your coding is.


## IMPERATIVES


> First, write a paper about your code, explaining, at least to yourself, what you want to do and how you plan to do it. Flesh out your actual code inside the paper. RUN your code inside the paper, capturing printouts and charts and diagrams and what not, so others (including your future self) can see the code at work. Iterate the process, rewriting prose and code as you invent and simplify, in a loop.


I once instructed a flock of interns to spend their first week writing their final report. After the predictable eyebrow-raising and mutual sidelong glances, I explained why:

- If you commence your research and coding before thinking out your objective and goals, you will have many false starts and waste time backtracking. Thinking means writing, and thinking is good.

- If you wait till the end, you will spend three weeks trying to remember and rationalize all the decisions, good and bad you made along the way.

- Of course you will revise your report as your results emerge, but revising an organized paper is much more efficient than organizing half-forgotten decisions.


### Executable Order Versus Human-Understandable Order


Ok, that's just ordinary Jupyter-notebook practice, right? Code inside your documentation, right?


With ordinary Jupyter-notebook practice, you must write everything in ***executable order***, because a Jupyter notebook is just a fancy interface to an underlying execution kernel. Executable order usually forces you to define all details before you use them. With Literate Programming, you don't necessarily write your code in executable order, the order forced by kernels. You write your code in ***human-understandable order***.


Executable order is usually the reverse of human-understandable order. Humans want to understrand the big picture *first*, then the details. They want to see the box-top of the jigsaw puzzle _before_ looking at all the pieces. Executable order is ***upside-down and inside-out***. 


We've all had the experience of reading code and Jupyter notebooks backwards so we don't get overwhelmed by details before understanding the big picture. That observation leads us to another imperative.


> Write about your code in human-understandable order. Don't be tyrranized by your programming language into defining everything in full, formal detail before you can talk about anything. Use tools to rearrange your code in executable order.


[Donald Knuth](http://amturing.acm.org/award_winners/knuth_1013846.cfm) invented Literate Programming so that he could both write _about_ [MetaFont](https://en.wikipedia.org/wiki/Metafont) and [TeX](https://texfaq.org/FAQ-lit) and _implement_ them in the same place. These are two of the most important computer programs ever written. Their longevity and quality speak to the viability of Literate Programming.


## What to do with Existing Code?


When rewriting old code base in literate style, ***detangle*** the existing code into understandable small pieces, rearrange it, and write about it in human-understandable order. To run the code, use a tool like Tangledown to re-tangle the code out to executable order on disk where compilers and interpreters can pick it up and run it, even inside notebook cells.


## Tangledown is Inside This Here Document, README.md


***Tangledown*** is the tool that extracts code from any Markdown file into executable order on the disk. This here document, README.md, the one you're reading right now, is the Literate Program for Tangledown. 


Because our documentation language is Markdown, the language of this document is _Literate Markdown_. This here README.md, which you're reading right now, contains all the source for the Literate-Markdown tool, `tangledown.py`, with all its documentation, all presented in human-understandable order, a top-down narrative style, like a story.


`tangledown.py` pulls or ***tangles*** code out of any Markdown document, not just this here README.md that you're reading right now. The verb "tangle" is traditional in Literate Programming. You might think it should be "untangle," because the Markdown document is all tangled up from executable order. But Knuth prefers the human's point of view. The Markdown document contains the code in the _correct_, human-understandable order. 


If we need something _more_ powerful than Tangledown, we'll go back to [org-babel](http://orgmode.org/worg/org-contrib/babel/) in Emacs (or [spacemacs](http://spacemacs.org/) for you VIM users). Those are much more powerful, best-of-breed Literate-Programming tools. You have to learn some Emacs to use them, and that's an insurmountable barrier for many people. Markdown is good enough for Github, and thus for most of us right now.


You can _also_ run Tangledown inside a Jupyter notebook, specifically one that is linked to this here document, README.md, the one you're reading right now. See [this section](#oh-my-jupytext) for more.


## OH MY! JUPYTEXT<a id="oh-my-jupytext"></a>


***Jupytext*** \[sic\] automatically syncs a Markdown file with a Jupyter notebook. Read about it [here](https://github.com/mwouts/jupytext). It works well in ***JupyterLab***. Read abou that [here](https://github.com/jupyterlab/jupyterlab). Specifically, it lets you open this here Markdown file, README.md, that you're reading right now, as a Jupyter notebook, and you can evaluate some cells in the notebook.


Here's how I installed everything on an Apple Silicon (M1) Mac Book Pro, with Python 3.9:

<!-- #raw -->
pip install jupyter
pip install jupyterlab
pip install jupytext
<!-- #endraw -->

Here is how I run it:

<!-- #raw -->
jupyter lab
<!-- #endraw -->

or

<!-- #raw -->
PYTHONPATH=".:$HOME/Documents/GitHub/tangledow:$HOME/Library/Jupyter/kernels/tangledown_kernel" jupyter lab ~
<!-- #endraw -->

when I want the [Tangledown Kernel](#section-tangledown-kernel), and I almost always want the Tangledown kernel.


If, in JupyterLab, you


- open README.md
- `View->Activate Command Palette`
- check `Pair Notebook with Markdown`
- right-click `README.md` and say `Open With -> Jupytext Notebook`
- edit one of the two, `README.md` or `README.ipynb` ...


Jupytext will update the other,


> ***IMPORTANT***: To see the updates in the notebook when you modify the Markdown, you must `File->Reload Notebook from Disk`, and to see updates in the Markdown when you modify the notebook, you must `File->Reload Markdown File from Disk`. Jupytext forces you to reload changed files manually. I'll apologize here, on behalf of the Jupytext team.


If you're reading or modifying `README.ipynb`, or if you `Open With -> Jupytext Notebook` on `README.md` (my preference), you may see tiny, unrendered Markdown cells above and below all your tagged nowebs and tangles. ***DON'T DELETE THE TINY CELLS***. Renderers of Markdown simply ignore the tags, but Jupytext makes tiny, invisible cells out of them!


Unless you're running the optional, new [Tangledown Kernel](#section-tangledown-kernel), don't RUN cells with embedded `block` tags in Jupyter, you'll just get syntax errors from Python.


# LET ME TELL YOU A STORY


This here README.md, the one you're reading right now, is *literature*, after all, so it should tell a story. Let's tell the story of creating Tangledown itself. We'll use Tangledown to _create_ Tangledown. That's just like bootstrapping a compiler. Just as we compile a compiler with a compiler, we'll use Tangledown to tangle Tangledown itself out of this here document named README.md that you're reading right now.


The first part of the story is that I just started writing the story, the Markdown. Then I filled in the code, moved everything around when I needed to, and kept rewriting until it all worked the way I wanted it to work.


## DISCLAIMER<a id="disclaimer"></a>


This is a useful toy, but it has zero error handling. We This document currently talks only about the happy path.  I try to be rude ("DUDE!") in comments every place where I sense trouble, but I'm only sure I haven't been rude enough. Read this with sense-of-humor bit turned on. This story is supposed to be fun!


I also didn't try it on Windows, but I did try it on WSL, the Windows Subsystem for Linux. Works great on WSL!


## HOW TO RUN TANGLEDOWN<a id="how-to-run"></a>


One way: run `python3 tangledown.py REAMDE.md` at the command line. That command should _overwrite_ tangledown.py. The code for tangledown.py is inside this here README.md that you're reading right now. The name of the file to overwrite, namely `tangledown.py`, is embedded inside this here README.md itself, in the `file` attribute of a `<tangle ...>` tag. Read about `tangle` tags [below](#section-tangle-tags)!


If you said `python3 tangledown.py MY-FOO.md`, then you would tangle the
code out of `MY-FOO.md`. You'll do that once you start writing your own code in
Tangledown. You will love it! We have some big examples that we'll write about elsewhere. Those examples include embedded code and microcode for exotic hardware, all written in Python!


Tangledown is both a script and a module. You can run Tangledown in a [Jupytext](#oh-my-jupytext) cell after importing some stuff from the module. The next cell illustrates the typical bootstrapping joke of tangling Tangledown itself out of this here README.md that you're reading right now, after this Markdown file has been linked to a Jupytext notebook. We also tangle one example out to `/dev/null`, a nifty way of discarding that example. You'll see that example [below](#section-tangle-tags), where we talk about `tangle` tags.

```python
from tangledown import get_lines, accumulate_lines, tangle_all
tangle_all(*accumulate_lines(get_lines("README.md")))
```

After you have tangled at least once, as above, and if you're running the new, optional [Tangledown Kernel](#section-tangledown-kernel), you can evaluate the source code for the whole program in the [cell i'm linking right here in this notebook](#tangle-listing-tangle-all). ***How Cool is That?***


Because Tangledown is a Python module, you can also run Tangledown from inside a standalone Python program, say in PyCharm or VS Code or whatever;
`hello_world_tangler.py` in this repository is an example.

<!-- #region -->
Once again, Jupytext lets you RUN code from a Markdown
document in a Jupyter notebook. If you open `hello_world.md` as a Jupytext
notebook in JupyterLab then you
can run Tangledown in Jupyter cells. Right-click on the name `hello_world.md` in the JupyterLab GUI and choose


`Open With ...` $\longrightarrow$ `Jupytext Notebook`


Then run cells! This is getting close to the high bar set by org-babel!
<!-- #endregion -->

## HOW IT WORKS: Markdown Ignores Mysterious Tags


Let's exploit the fact that most Markdown renderers, like Jupytext's, Github's, and [PyCharm's](https://www.jetbrains.com/pycharm/), ignore HTML / XML _tags_ (that is, stuff inside angle brackets) that they don't recognize. Let's enclose blocks of real, live code with `noweb` tags, like this:


    <noweb name="my_little_tests">

    class TestSomething (): 
        def test_something (self):
            assert (3 == 2+1)

    </noweb>


The markdown above renders as follows. You can see the `noweb` one-liner raw cells above and below the code in Jupytext. If they were Markdown cells, they'd be tiny and invisible. That's 100% OK, and may be more to your liking! Try changing the cells from RAW (press "R") to Markdown (press "M") and back, then closing them (Shift-Enter) and opening them (Enter). If you mark them CODE (press "Y"), Tangledown won't work because Jupytext will surround them with triple-backticks.

<!-- #raw -->
<noweb name="my_little_tests">
<!-- #endraw -->

```python
class TestSomething ():
    def test_something (self):
        assert (42 == 6 * 7)
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

What are the `<noweb ...>` and `</noweb>` tags? We explain them immediately below.


## THREE TAGS: noweb, block, and tangle


### `noweb` tags


Markdown ignores `<noweb ...>` and `</noweb>` tags, but `tangledown.py` _doesn't_. `tangledown.py` sucks up the ***contents*** of the `noweb` tags and sticks them into a dictionary for later lookup when processing `block` tags.


#### CONTENTS OF A TAG


The contents of a `noweb` tag is (are?) the material between the opening `<noweb ...>` and closing `</noweb>` fenceposts. Markdown renders contents with syntax coloring and indentation. The term _contents_ is ordinary jargon from HTML, XML, SGML, etc., and applies to any opening `<foo ...>` and closing `</foo>` pair.


#### ATTRIBUTES OF A TAG


The Tangledown dictionary key for contents of a `noweb` tag is the string value of the `name` attribute. For example, in `<noweb name="foo">`, `name` is an _attribute_, and its string value is `"foo"`. 


> Noweb names must be unique in a document.


**NOTE**: the `name` attribute of a `noweb` opener must be on the same line, like this:

<!-- #raw -->
    <noweb name="foo"> 
<!-- #endraw -->

Ditto for our other tags. That's a limitation of the regular expressions that detect `noweb` tags. Remeber, [Tangledown is a toy](#disclaimer), a very useful toy, but it's limited.


#### FENCEPOST CELLS


You can create the fencepost cells, `<noweb ...>` and `</noweb>`, either in the Markdown file, or you can create them in the synchronized Jupytext notebook. 


If you create them in Markdown, leave a blank line after the opening `<noweb ...>` and a blank line before the closing `</noweb>`. If you don't, the Markdown renderer won't color and indent the contents. Tangledown will still work, but your code will look like text. 


If you write them in Markdown instead of in the notebook, they appear in the notebook as tiny, invisible Markdown cells because the renderer ignores them. ***DON'T DELETE THEM***, but you can open (Enter) and close (Shift-Enter) them. 


If you create `noweb` and `tangle` tags in the notebook and you want them _visible_, mark them _RAW_ by pressing "R" with the cell highlighted but not editable. Don't mark them CODE (don't press "Y"). Tangledown will break because Jupytext will surround them with triple-backticks.


### `block` tags


Later, in the [second pass](#second-pass), Tangledown blows the contents of a `noweb` back out wherever it sees a `block` tag with the same `name` attribute. That's how you can define code anywhere in your document and use it in any other place, later or earlier, more than once if you like. 


`block` tags may appear in the contents of `noweb` tags and in the in the contets of `tangle` tags, too. The contents of `block` tags are discarded. Only the `name` attribute of a `block` tag matters.


#### WRITE IN ANY-OLD-ORDER YOU LIKE


You don't have to write the noweb _before_ you write a matching `block` tag. You can refer to a `noweb` tag before it exists in time and positionally before it exists in space, more than once if you like. You can define things and name things and use things in any order that makes your thinking and your story more clear. This is literature, after all.


### `tangle` tags <a id="section-tangle-tags"></a>


A `tangle` tag sprays its block-expanded contents to a file on disk. What file? The file named in the `file` attribute of the `tangle` tag. ***Expanding*** contents of a `tangle` tag means replacing every `block` tag with the contents of its matching `noweb` tag, recursively, until everything bottoms out in valid Python.


The same rules about blank lines hold for `tangle` tags as they do for `noweb` tags: if you want Markdown to render the contents like code, surround the contents with blank lines or mark the tag cells _RAW_. The following Markdown


    <tangle file="/dev/null">

    <block name="my_little_tests"></block>

    if __name__ == '__main__':
        TestSomething().test_something()

    </tangle>


renders like this


<tangle file="/dev/null">

```python
import unittest

<block name="my_little_tests"></block>

if __name__ == '__main__':
    TestSomething().test_something()
```

</tangle>


The example above has the tags in tiny, invisible Markdown cells above and below the code. Play around with opening and closing them with Enter and Shift-Enter, respectively.


You can evaluate the cell with the new, optional [Tangledown Kernel](#section-tangledown-kernel). Don't evaluate the code cell in the Python Kernel, you'll get a syntax error because the `block` tag is not valid Python. 


This code tangles to the file `/dev/null`. That's a nifty trick for temporary `tangle` blocks. You can talk about them, validate them by executing their cells in the [Tangledown Kernel](#section-tangledown-kernel), and throw them away.


# HUMAN! READ THE `block` TAGS!


Markdown renders `block` tags verbatim inside nowebs or tangles. This is good for humans, who will think


> AHA!, this `block` refers to some code in a `noweb` tag somewhere else in this Markdown document. I can read all the details of that code later, when it will make more sense, after I've understood the big picture. I can look at the pieces of the jigsaw puzzle (the `noweb` tags) after I've looked at the completed puzzle on the box top (the `tangle` tags).

> This here beautifully written document I'm reading right here and now is making it easy for me to understand the big picture first. Thank you, kindly, author! Without you, I'd be awash in details. I'd get tired and cranky before understanding the big picture!


That's exactly what you want for humans: talk about something, name the pieces, show how they fit together, without necessarily choking down all the details first.


See, I'll prove it to you. Below is the code for all of `tangledown.py` itself. You can understand this without understanding the _implementations_ of the sub-pieces, just getting an idea of _what_ they do from the names of the `block` tags. **READ THE NAMES IN THE BLOCK TAGS**. Later, if you want to, you can read all the details in the `noweb` tags named by the `block` tags.


## TANGLE ALL<a id="tangle-listing-tangle-all"></a>


If you're running the new, optional [Tangledown Kernel](#section-tangledown-kernel), you can evaluate this cell and run Tangledown on Tangledown itself, right here in a Jupyter notebook. ***How Cool is That?***

<!-- #raw -->
<tangle file="./tangledown.py">
<!-- #endraw -->

```python
<block name="types"></block>
<block name="openers"></block>
<block name="oh-no-there-are-two-ways"></block>
<block name="accumulate-contents"></block>
<block name="accumulate-lines"></block>
<block name="thereIsABlockTag"></block>
<block name="eatBlockTag"></block>
<block name="expandBlocks"></block>
<block name="expand-tangles"></block>


def tangle_all(nowebs: Nowebs, tangles: Tangles) -> None:
    for filename, liness in tangles.items ():
        Path(filename).parents[0].mkdir(parents=True, exist_ok=True)
        contents: str = expand_tangles(liness, nowebs)
        with open (filename, 'w') as outfile:
            print(f"WRITING FILE: {filename}")
            outfile.write (contents)

            
if __name__ == "__main__":
    file_from_sys_argv = get_aFile()
    lines = get_lines(file_from_sys_argv)
    # test_re_matching(lines)
    nowebs, tangles = accumulate_lines(lines)
    tangle_all(nowebs, tangles)
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

The whole program is in the function `tangle_all`. The standard Python trick of testing `__name__` against `"__main__"` give hybrid vigor: `tangledown.py` is both a script and module to import.


All we do in `tangle_all` is loop over all the line lists in the tangles (`for filename, liness in tangles.items()`) and [expand them](#expand-lines-list) to replace blocks with nowebs. 


The code will create the subdirectories needed. For example, if you tangle to file `foo/bar/baz/qux.py,` the code creates the directory chain `./foo/br/baz/` if it doesn't exist.


### TYPES


A `Line` is a string, Python base type `str`. `Lines` is the type of a list of lines. `Liness` is the type of a list of list of lines, in a pluralizing shorthand borrowed from Haskell practice.


A noweb name is a string, and a tangle file name is a string. A line number is an `int`, a Python base type.


Nowebs are dictionaries from noweb names to lines. 


Tangles are dictionaries from file names to Liness --- lists of lists of lines. Tangledown accumulates output for `tangle` files mentioned more than once. If you tangle to `qux.py` in one place and then also tangle to `qux.py` somewhere else, the second tangle won't overwrite the first, but append to it. That's why tangles are lists of lists of lines, one list of lines for each mentioning of a given file. Read more about that in [expand-tangles](#expand-tangles).

<!-- #raw -->
<noweb name="types">
<!-- #endraw -->

```python
from typing import List, Dict, Tuple, Match

NowebName = str
FileName = str
TangleFileName = FileName
LineNumber = int
Line = str
Lines = List[Line]
Liness = List[Lines]
LinesTuple = Tuple[LineNumber, Lines]

Nowebs = Dict[NowebName, Lines]
Tangles = Dict[TangleFileName, Liness]
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

We'll implement all the noweb blocks, like `accumulate_contents` and `eatBlockTag`, later. You can read about them, or not, after you've gotten the big picture.


## DEBUGGING AND REFACTORING


The Tangledown Kernel doesn't support the Jupytext debugger, yet. Sorry about that. Tangle the code out to disk and debug it with pudb or whatever. [Tangledown is still a toy](#disclaimer). Ditto refactoring. PyCharm is great for that, but you'll have to do it on tangled files.


## EXPAND TANGLES<a id="expand-tangles"></a>


We separated out the inner loop over Liness into another function, `expand_tangles`, so that the [Tangledown Kernel](#section-tangledown-kernel) can import it and apply it to `block` tags. `tangle_all` calls `expand_tangles`; `expand_tangles` calls `expand_blocks`. Read about `expand_blocks` [here](#expand-blocks).

<!-- #raw -->
<noweb name="expand-tangles">
<!-- #endraw -->

```python
def expand_tangles(liness: Liness, nowebs: Nowebs) -> str:
    contents: Lines = []
    for lines in liness:
        while there_is_a_block_tag (lines):
            lines = expand_blocks (nowebs, lines)
        contents += lines
    return ''.join(contents)
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

## Tangledown Tangles Itself?


Tangledown uses two kinds of regular expressions (regexes) for matching tags in any Markdown file:

- regexes for `noweb` and `tangle` tags that appear on lines by themselves, left-justified

- regexes that match `<block ...>` tags that may be indented, and match their closing `</block>` tags, which may appear on the same line as `<block ...>` or lines by themselves.


Both kinds of regex are ___safe___, in the sense that they do not match themselves. That means it's safe to run
`tangledown.py` on this here `READMD.md`, which contains source for `tangledown.py`.


The two regexes in noweb `left_justified_regexes` match `noweb` and`tangle` tags that appear on lines by themselves, left-justified. These regexes won't match themselves; that's our bootstrapping technique. 


> They also wont match `noweb` and `tangle` tags that are indented. That lets us _talk about_ `noweb` and `tangle` tags: just put the examples you're talking about in an _indented_ Markdown code cell instead of in a triple-backticked code cell with no indentation.


The names in the attributes of `noweb` and `tangle` tags must start with a letter, and they can contain letters, numbers, hyphens, underscores, whitespace, and dots. 


The names of `noweb` tags must be globally unique within the Markdown file. Multiple `tangle` tags may refer to the same output file, in which cases, the contents of the second and subsequent `tangle` tags will be appended to a list of lines.


### LEFT-JUSTIIED REGEXES

<!-- #raw -->
<noweb name="left_justified_regexes">
<!-- #endraw -->

```python
noweb_start_re = re.compile (r'^<noweb name="(\w[\w\s\-.]*)">$')
noweb_end_re = re.compile (r'^</noweb>$')

tangle_start_re = re.compile (r'^<tangle file="(.+/\\[^/]+|.+)">$')
tangle_end_re = re.compile (r'^</tangle>$')
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

### ANYWHERE REGEXES


The regexes in this noweb, `anywhere_regexes`, match `block` tags that may be indented,  preserving indentation. The `block_end_re` regex also preserves indentation. 


I converted the 'o' in 'block' to a harmless regex group `[o]` so that _block_end_ doesn't match itself. That makes it safe to run this code on this here document itself.

<!-- #raw -->
<noweb name="anywhere_regexes">
<!-- #endraw -->

```python
block_start_re = re.compile (r'^(\s*)<block name="(\w[\w\s\-.]*)">')
block_end_re = re.compile (r'^(\s)*</bl[o]ck>')
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

## Test the Regular Expressions


### OPENERS


The code in noweb `openers` has two `block` tags that refer to the nowebs of the regexes defined above, namely `left_justified_regexes` and `anywhere_regexes`. After Tangledown substitutes the contents of the nowebs for the blocks, the code becomes valid Python and you can call `test_re_matching` in the [Tangledown Kernel](#section-tangledown-kernel) or at the command line. When you call it, it proves that we can recognize all the various kinds of tags. We leave the regexes themselves as global pseudo-constants so that they're both easy to test and to use in the body of the code ([Demeter weeps](https://en.wikipedia.org/wiki/Law_of_Demeter)).


The code in `hello_world.ipynb` (after you have Paired a Notebook with the Markdown File `hello_world.md`) runs this test as its last act to check that `tangledown.py` was correctly tangled from this here `README.md`. That code works in the ordinary Python kernel and in the [Tangledown Kernel](#section-tangledown-kernel).


Notice the special treatment for block ends, which are usually on the same lines as their block opener tags, but not necessarily so. That's what lets you put (useless) contents in `block` tags.

<!-- #raw -->
<noweb name="openers">
<!-- #endraw -->

```python
import re
import sys
from pathlib import Path

<block name="getting a file and its lines"></block>
<block name="left_justified_regexes"></block>
<block name="anywhere_regexes"></block>

def test_re_matching(lines: Lines) -> None:
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

<!-- #raw -->
</noweb>
<!-- #endraw -->

## TANGLEDOWN: Two Passes


Tangledown operates in two passes, once over the file to collect contents of `noweb` and `tangle` tags, and a second time over the `tangle` tags to expand `block` tags. That is, in the second pass, Tangledown substitutes noweb contents for corresponding `block` tags until there are no more, creating valid code that it writes to disk if the Markdown is correctly written.


### Getting a File Name


`tangledown.py` is both a script and a module. As a script, you run it from the command line, so it gets its input file name from command-line arguments. As a module, called from another Python program, you probably want to give the file as an argument to a function, specifically, to `get_lines`.


Let's write two functions, 

- `get_aFile`, which parses command-line arguments and produces a file name

- `get_lines`, which 

  - gets lines, without processing `noweb`, `tangle`, or `block` tags, from a file denoted by its argument, `aFilename`
  
  - strips out `#raw` and `#endraw` fenceposts 
  
  - writes out the full file path to a secret place where the [Tangledown Kernel](#section-tangledown-kernel) can pick it up.


`get_aFile` can parse command-line arguments that come from either `python` on the command line or from a `Jupitext` notebook, which has a few kinds of command-line arguments we must ignore, namely command-line arguments that end in `.py` or in `.json`.


### GETTING A FILE AND ITS LINES

<!-- #raw -->
<noweb name="getting a file and its lines">
<!-- #endraw -->

```python
def get_aFile() -> str:
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

<block name="save-afile-path-for-kernel"></block>
raw_line_re: re = re.compile(r'<!-- #(end)?raw -->')
def get_lines(aFilename: str) -> Lines:
    """Get lines from a file denoted by aFilename. Strip 'raw'
    fenceposts. Write full path to a secret place for the 
    kernel to pick it up."""
    save_aFile_path_for_kernel(aFilename)
    with open(aFilename) as aFile:
        in_lines: Lines = aFile.readlines ()
        out_lines: Lines = []
        for in_line in in_lines:
            if not raw_line_re.match(in_line):
                out_lines.append(in_line)
        return out_lines
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

### SAVE A FILE PATH FOR THE KERNEL<a id="save-afile-path-for-kernel"></a>


Returns its input file name after expanding its full path and saving the full path in a special place where the [Tangledown Kernel](#section-tangledown-kernel) can find it.

<!-- #raw -->
<noweb name="save-afile-path-for-kernel">
<!-- #endraw -->

```python
def save_aFile_path_for_kernel(aFile: FileName) -> FileName:
  xpath: Path = Path.cwd() / Path(aFile).name
  victim_file_name = str(xpath.absolute())
  safepath: Path = Path.home() / '.tangledown/current_victim_file.txt'
  Path(safepath).parents[0].mkdir(parents=True, exist_ok=True)
  print(f"SAVING {victim_file_name} in secret place {str(safepath)}")
  with open(safepath, "w") as t:
      t.write(victim_file_name)
  return aFile
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

### First Pass: Saving Noweb and Tangle Blocks


In the first pass over the file, we'll just save the contents of noweb and tangle into dictionaries, without expanding nested `block` tags.


#### OH NO! THERE ARE TWO WAYS


Turns out there are two ways to write literal blocks in Markdown:

1. indented by four spaces and

2. surrounded by triple backticks and _not_ indented.


Tangledown must handle both ways.


We use the trick of a harmless regex group --- stuff inside square brackets --- around one of the backticks in the regex that recognizes triple backticks. Now this regex is safe to run on itself. See `triple_backtick_re` in the code immediately below.


The function `first_non_blank_line_is_triple_backtick`, in noweb `oh-no-there-are-two-ways` recognizes code blocks bracketed by triple backticks. Notice that the contents of this `noweb` tag  is triple-bacticked, itself. Kind of a funny self-toast joke, no?


Remember the _use-mention_ dichotomy from Philosophy class? No problem if you don't.


When we're _talking about_ `noweb` and `tangle` tags, but don't want to process them, we use indented code blocks, not triple-backticked. Tangledown won't process indented `noweb` and `tangle` tags because the regexes in noweb `left_justified_regexes` won't match them. 


We also see, here, why line numbers help. We might do this in some bitchin' list comprehension, but this is more obvious-at-a-glance. That's a good thing.

<!-- #raw -->
<noweb name="oh-no-there-are-two-ways">
<!-- #endraw -->

```python
triple_backtick_re = re.compile (r'^`[`]`')
blank_line_re      = re.compile (r'^\s*$')

def first_non_blank_line_is_triple_backtick (
        i: LineNumber, lines: Lines) -> Match[Line]:
    while (blank_line_re.match (lines[i])):
        i = i + 1
    return triple_backtick_re.match (lines[i])
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### ACCUMULATE CONTENTS<a id="accumulate-contents"></a>


Tangledown is a funny little compiler. It converts Literate Markdown to Python. We could go nuts and write it in highfalutin' style, and then it would be much bigger, more elaborate if not more elegant, and easier to explain to a Haskell programmer. It might also be less of a toy. However, we want this toy Tangledown for now to be:

- very short

- independent of rich libraries like parser combinators

- completely obvious to anyone


We'll just use iteration and array indices, but in a tasteful way so our functional friends won't get seasick. This is Python, after all, not highfalutin' Haskell! We can just _get it done_, but with some grace, panache, and aplomb.


The function `accumulate_contents` accumulates the contents of `noweb` or `tangle` tags. The function starts at line `i`, then figures out whether a tag's first non-blank line is triple backtick, in which case it _won't_ snip four spaces from the beginning of every line, and finally keeps going until it sees the closing taglet, `</noweb>` or `</tangle>`. It returns a tuple of the line index _after_ the closing taglet, and the contents, possibly de-dented. The function manipulates line numbers to skip over triple backticks.

<!-- #raw -->
<noweb name="accumulate-contents">
<!-- #endraw -->

```python
def accumulate_contents (
        lines: Lines, i: LineNumber, end_re: re) -> LinesTuple:
    r"""Harvest contents of a noweb or tangle tag. The start
    taglet was consumed by caller; we consume the end taglet."""
    if (first_non_blank_line_is_triple_backtick (i, lines)):
        i = i + 1 # eat the line containing triple backticks
        snip = 0
    else:
        snip = 4
    contents_lines: Lines = []
    for j in range (i, len(lines)):
        end_match = end_re.match(lines[j])
        if (end_match):  # This is the only place we return!
            return j + 1, contents_lines
        else:
            if (snip == 0 and triple_backtick_re.match (lines[j])):
                pass  # don't do nothin nohow
            else:
                contents_lines.append (lines[j][snip:])
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### ACCUMULATE LINES


The function `accumulate_lines` sucks the contents of all the `noweb` tags and `tangle` tags out of a file, but doesn't expand any `block` tags that it finds. It just builds up dictionaries, `noweb_blocks` and `tangle_files`, keyed by `name` or `file` attributes it finds inside `noweb` or `tangle` tags.

<!-- #raw -->
<noweb name="accumulate-lines">
<!-- #endraw -->

```python
<block name="normalize-file-path"></block>
def accumulate_lines(lines: Lines) -> Tuple[Nowebs, Tangles]:
    nowebs: Nowebs = {}
    tangles: Tangles = {}
    for i in range(len(lines)):
        noweb_start_match = noweb_start_re.match (lines[i])
        tangle_start_match = tangle_start_re.match (lines[i])
        if (noweb_start_match):
            key: NowebName = noweb_start_match.group (1)
            (i, nowebs[key]) = \
                accumulate_contents(lines, i + 1, noweb_end_re)
        elif (tangle_start_match):
            key: TangleFileName = \
                str(normalize_file_path(tangle_start_match.group(1)))
            if not (key in tangles):
                tangles[key]: Liness = []
            tangles[key] += \
                [accumulate_contents(lines, i + 1, tangle_end_re)[1]]
                # the [1] gets the lines, omits the line number
    return nowebs, tangles
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### NORMALIZE FILE PATH


We must normalize file names so that, for example, "foo.txt" and "./foo.txt" indicate the same file and so that `~/` denotes the home directory on Mac and Linux.

<!-- #raw -->
<noweb name="normalize-file-path">
<!-- #endraw -->

```python
def anchor_is_tilde(path_str: str) -> bool:
    result = (path_str[0:2] == "~/") and (Path(path_str).anchor == '')
    return result

def normalize_file_path(tangle_file_attribute: str) -> Path:
    result: Path = Path(tangle_file_attribute)
    if (anchor_is_tilde(tangle_file_attribute)):
        result = (Path.home() / tangle_file_attribute[2:])
    return result.absolute()
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

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


We'll get to error handling someday, maybe. Tangledown is [just a little toy at the moment](#disclaimer), but I thought it interesting to write about. If it's ever distributed to hostile users, then we will handle all the bad cases. But not now. Let's get the happy case right.


### Second Pass: Expanding Blocks<a id="second-pass"></a>


Iterate over all the `tangle` tag contents and expand the
`block` tags we find in there, recursively. That means keep going until there are no more `block` tags, because nowebss are allowed (encouraged!) to refer to other nowebs via `block` tags. If there are cycles, this will hang.


#### DUDE! HANG?


We're doing the happy cases first, and will get to cycle detection someday, maybe.


#### THERE IS A BLOCK TAG


First, we need to detect that some list of lines contains a `block` tag, left-justified or not. That means we must keep running the expander on that list.

<!-- #raw -->
<noweb name="thereIsABlockTag">
<!-- #endraw -->

```python
def there_is_a_block_tag (lines: Lines) -> bool:
    for line in lines:
        block_start_match = block_start_re.match (line)
        if (block_start_match):
            return True
    return False
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### EAT A BLOCK TAG


If there is a `block` tag, we must eat the tag and its meaningless contents:

<!-- #raw -->
<noweb name="eatBlockTag">
<!-- #endraw -->

```python
def eat_block_tag (i: LineNumber, lines: Lines) -> LineNumber:
    for j in range (i, len(lines)):
        end_match = block_end_re.match (lines[j])
        # DUDE! Check leading whitespace against block_start_re
        if (end_match):
            return j + 1
        else:  # DUDE!
            pass
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### EXPAND BLOCKS<a id="expand-blocks"></a>


The following function does one round of block expansion. The caller must test whether any `block` tags remain, and keep running the expander until there are no more `block` tags. Our functional fu grandmaster might be appalled, but sometimes it's just easier to iterate than to recurse.

<!-- #raw -->
<noweb name="expandBlocks">
<!-- #endraw -->

```python
def expand_blocks (nowebs: Nowebs, lines: Lines) -> Lines:
    out_lines = []
    for i in range (len (lines)):
        block_start_match = block_start_re.match (lines[i])
        if (block_start_match):
            leading_whitespace: str = block_start_match.group (1)
            block_key: NowebName = block_start_match.group (2)
            block_lines: Lines = nowebs [block_key]  # DUDE!
            i: LineNumber = eat_block_tag (i, lines)
            for block_line in block_lines:
                out_lines.append (leading_whitespace + block_line)
        else:
            out_lines.append (lines[i])
    return out_lines
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

## Tangle It, Already!<a id="tangle_already"></a>


Ok, you saw [at the top](#how-to-run) that the code in this here Markdown document, README.md, when run as a script, will read in all the lines in ... this here Markdown document, `README.md`. Bootstrapping!


But you have to run something first. For that, I tangled the code manually just
once and provide `tangledown.py` in the repository. The chicken definitely comes
before the egg.


But if you have the chicken (`tangledown.py`), you can import it as a module and execute the following cell, a copy of the one [at the top](#how-to-run). That should overwrite `tangledown.py` with the contents of this notebook or Markdown file. So our little bootstrapping technique will forever update the Tangledown compiler if you change it in this here README.md that you're reading right now!

```python
from tangledown import get_lines, accumulate_lines, tangle_all
tangle_all(*accumulate_lines(get_lines("README.md")))
```

## DUDE!


Some people write "TODO" in their code so they can find all the spots where they thought they might have trouble but didn't have time to write the error-handling (prophylactic) code at the time. I like to write "DUDE" because it sounds like both "TODO" but is more RUDE (also sounds like "DUDE") and funny. This story is supposed to be amusing.


## Known Bugs to Fix<a id="section-known-bugs"></a>


I must apologize once again, but this is just a toy at this point! Recall the [DISCLAIMER](#disclaimer). The following are stackranked from highest to lowest priority.


1. FIXED: writing to "tangledown.py" and to "./tangledown.py" clobbers the file rather than appending. Use pathlib to compare filenames rather than string comparison.
2. FIXED: tangling to files in the home directory via `~` does not work. We know one dirty way to fix it, but proper practice with pathlib is a better answer.


# TODO<a id="todo"></a>


- NOT-STARTED: Have the Tangledown Kernel, when evaluating tangle-able cells, write them out one at a time. Without this feature, the only way to write out files is to tangle the entire notebook. Possibly do these as cell magics.
- NOT-STARTED: Research cell magics for `noweb` and `tangle` cells.
- NOT-STARTED: more examples
- NOT-STARTED: error handling (big job)
- NOT-STARTED: type annotations for the kernel
- DONE: convert relative file paths to absolute
- DONE: modern Pythonic Type Annotation (PEP 484)
- DONE: use pathlib to compare tangle file names
- DONE: somehow get the Tangledown Kernel to tangle everything automatically when it's restarted
- DONE: Support multiple instances of the Tangledown Kernel. Because it reads files with fixed names in the home directory, it has no way of processing multiple Tangledown notebooks.
    - DONE: investigate [Papermill](https://papermill.readthedocs.io/en/latest/) as a solution
- DONE: find out whether pickle is a better alternative to json for dumping dictionaries for the kernel
- DONE: Jupytext kernel for `tangledown` so we can run `noweb` and `block` tags that have `block` tags in them.


# APPENDIX: Developer Notes


If you change the code in this README.md and you want to test it by running the cell in Section [Tangle It, Already!](#tangle-already), you usually must restart whatever Jupyter kernel you're running because Jupytext caches code. If things continue to not make sense, try restarting the notebook server. It rarely but occasionally produces incorrect answers for more obscure reasons.


# APPENDIX: Tangledown Kernel<a id="section-tangledown-kernel"></a>


The Tangledown kernel is ***OPTIONAL***, but nice. Everything I talked about so far works fine without it, but the Tangledown Kernel lets you evaluate Jupytext notebook cells that have `block` tags in them. For example, you can run Tangledown on Tangledown itself in this notebook just by evaluating the cell that contains all of Tangledown, including the source for the kernel, [here](#tangle-listing-tangle-all).


The Tangledown Compiler writes the full path of the current Markdown file corresponding to the current notebook to fixed place in the home directory, and the Tangledown Kernel reads gets all the nowebs from there. 


If you are running more than one instance of the Tangledown Kernel at one time on your machine, you must ***RESTART THE TANGLEDOWN KERNEL WHEN YOU SWITCH NOTEBOOKS*** because the name of the current file is a fixed, singleton. The Tangledown Kernel has no way to dynamically know what file you're working with. Sorry about that!


## Installing the Tangledown Kernel


After you tangle the code out of this here README.md at least once, you will have two new files
- `./tangledown_kernel/tangledown_kernel.py`
- `./tangledown_kernel/kernel.json`


You must inform Jupyter about your new kernel. The following works for me on the Mac. It might be different on your machine:

```bash
jupyter kernelspec install --user tangledown_kernel
```

## Running the Tangledown Kernel


You must put the source for the Tangledown Kernel somewhere Python can find it before you start Jupyter Lab. One way is to modify the `PYTHONPATH` environment variable. The following works for me on the Mac:

<!-- #raw -->
PYTHONPATH=".:/Users/brian/Library/Jupyter/kernels/tangledown_kernel" jupyter lab
<!-- #endraw -->

Once the kernel is installed, there are multiple ways to run it in Jupyter Lab. When you first open a notebook, you get a menu. The default is the regular Python 3 kernel, and it works fine, but you won't be able to run cells that have `block` tags in them. If you choose the Tangledown Kernel, you can run such cells.


If you modify the kernel: 

1. re-tangle the kernel source, say by running the cell in [this section](#how-to-run)
2. re-install the kernel by running the little bash script above
3. restart the kernel inside the notebook


Most of the time, you don't have to restart Jupyter Lab itself, but sometimes after a really bad bug, you might have to.


## Source for the Tangledown Kernel


Adapted from [these official docs](https://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html).


The kernel calls [`expand_tangles`](#expand-tangles) after reformatting the lines a little. We learned about the reformatting by experiment. We explain `expand_tangles` [here](#expand-lines-list) in the [section about Tangledown itself](#tangle-listing-tangle-all). The rest of this is boilerplate from the [official kernel documentation](https://jupyter-client.readthedocs.io/en/stable/wrapperkernels.html). There is no point, by the way, in running the cell below in any kernel. It's meant for the Jupyterlab startup engine, only. You just need to tangle it out and install it, as above.


> **NOTE**: You will get errors if you run this cell in the notebook.

<!-- #raw -->
<tangle file="./tangledown_kernel/tangledown_kernel.py">
<!-- #endraw -->

```python
<block name="kernel-imports">
class TangledownKernel(IPythonKernel):
    <block name="kernel-instance-variables">
    async def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            cleaned_lines = [line + '\n' for line in code.split('\n')]
            # HERE'S THE BEEF!
            expanded_code = expand_tangles([cleaned_lines], self.nowebs)
            reply_content = await super().do_execute(
                expanded_code, silent, store_history, user_expressions)
            stream_content = {
                'name': 'stdout',
                'text': reply_content,
            }
            self.send_response(self.iopub_socket, 'stream', stream_content)
        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=TangledownKernel)
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

<!-- #raw -->
<noweb name="kernel-imports">
<!-- #endraw -->

```python
from ipykernel.ipkernel import IPythonKernel
from pprint import pprint
import sys  # for version_info
from pathlib import Path
from tangledown import \
        accumulate_lines, \
        get_lines, \
        expand_tangles
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### KERNEL INSTANCE VARIABLES


These get indented on expansion because the `block` tag is indented. You could do it the other way: indent the code here and DON'T indent the block tag, but that would be ugly, wouldn't it?


Notice this kernel runs Tangledown on the full file path that's stored in `current_victim_file.txt`. That file path got [written to that special place](#save-afile-path-for-kernel) when you tangled the file the first time. This may explain why you must tangle the file once and then restart the kernel whenever you switch notebooks that are running the Tangledown Kernel.

<!-- #raw -->
<noweb name="kernel-instance-variables">
<!-- #endraw -->

```python
current_victim_filepath = ""
with open(Path.home() / '.tangledown/current_victim_file.txt') as v:
    current_victim_filepath = v.read()
nowebs, tangles_ = accumulate_lines(get_lines(current_victim_filepath))
implementation = 'Tangledown'
implementation_version = '1.0'
language = 'no-op'
language_version = '0.1'
language_info = {  # for syntax coloring
    "name": "python",
    "version": sys.version.split()[0],
    "mimetype": "text/x-python",
    "codemirror_mode": {"name": "ipython", "version": sys.version_info[0]},
    "pygments_lexer": "ipython%d" % 3,
    "nbconvert_exporter": "python",
    "file_extension": ".py",
}
banner = "Tangledown kernel - expanding 'block' tags"
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

### Kernel JSON Installation Helper

<!-- #raw -->
<tangle file="./tangledown_kernel/kernel.json">
<!-- #endraw -->

```json
{"argv":["python","-m","tangledown_kernel", "-f", "{connection_file}"],
 "display_name":"Tangledown"
}
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

# APPENDIX: Experimental Playground

```python

```
