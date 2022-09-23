# Tangledown: One-Step Literate Markdown


#### Brian Beckman
#### Friday, 23 Sep 2022
#### v0.0.8


# OVERVIEW


## WRITING MATTERS


Leslie Lamport, Turing-Award Winner, 2013, said, approximately:


> Writing is Nature's Way of showing you how sloppy your thinking is. Coding is Nature's Way of showing you how sloppy your writing is. Testing is Nature's Way of showing you how sloppy your coding is.


In here, we will show you how to combine testing, coding, and writing in a natural way. Your code will be the central character in a narrative, a story crafted to help your readers understand _both_ what you're doing _and_ how you're doing it. Your code will be tested because you (and your readers) can run it, right here and now, inside this Jupytext \[sic\] notebook. Your story and your code will _never_ get out of sync because you will be working with both of them all the time.


Narrative order is the natural order for a story, but it's not the natural order for interpreters and compilers, even for Jupyter kernels. Tangledown lets you write in narrative order, than, later, tangle the code out into executable order, where the definitions of the parts precede the story. That executable order is backwards and inside-out from the reader's point of view!


Without something like this, you're condemned to explaining _how_ your code works before you can say much about _what_ your code is doing. Indulge us in a little _theory of writing_, will you?


## CREATIVE WRITING 101


You're writing a murder mystery. 


**METHOD 1**: Start with a data sheet: all the characters and their relationships. Francis stands to inherit, but Evelyn has a life-insurance policy on Victor. Bobbie is strong enough to swing an axe. Alice has poisonous plants in her garden. Charlie has a gun collection. Danielle is a chef and owns sharp knives. Lay out their schedules and whereabouts for several weeks. Finally, write down the murder and the solution.


**METHOD 2**: There's a murder. Your romantic detective asks "Who knew whom? Who benefitted? Who could have been at the scene of the crime? Who had opportunity? What was the murder weapon? Who could have done it?"


If your objective is to _engage_ the audience, to motivate them to unravel the mystery and learn the twists and turns along the way, which is the better method? If your objective is to have them spend several hours wading through reference material, trying to guess where this is all going, which is the better method?


Now, you're writing about some software. 


**METHOD 1**: Present all the functions and interfaces, cross dependencies, asynchronous versus synchronous, global and local state variables, possibilities for side effects. Finally, present unit tests and a main program.


**METHOD 2**: Explain the program's rationale and concept of operation, the solution it delivers, its modes and methods. Present the unit tests and main program that fulfill all that. Finally, present all the functions, interfaces, and procedures, all the bits and bobs that could affect and effect the solution.


If your objective is to _engage_ your audience, to have them understand the software deeply, as if they wrote it themselves, which is the better method? If your objective is to have them spend several hours wading through reference material trying to guess what you mean to do, which is the better method?


## SOFTWARE AS DOCUMENTATION


Phaedrus says:


> I give good, long, descriptive names to functions and parameters to make my code readable. I use Doxygen and Sphinx to automate document production. _I'm a professional!_


And Socrates says:


> That's nice, but you only document the pieces, and say nothing about how the pieces fit together. It's like giving me a jigsaw puzzle without the box top. It's almost sadistic.

> You condemn me to reverse-engineering your software: to run it in a debugger or to trace printouts.


## LITERATE PROGRAMMING


[Literate Programming](https://en.wikipedia.org/wiki/Literate_programming) is the best known way to save your _audience_ the work of reverse engineering your code, of giving them the box top with the jigsaw puzzle.


Who is your audience?

- yourself, first, down the line, trying to remember "why the heck did I do _that_?!?"

- other programmers, eventually, when they take over maintaining and extending your code


## IMPERATIVES


> First, write a paper about your code, explaining, at least to yourself, what you want to do and how you plan to do it. Flesh out your actual code inside the paper. RUN your code inside the paper, capturing printouts and charts and diagrams and what not, so others, including, first, your future self, can see the code at work. Iterate the process, rewriting prose and code as you invent and simplify, in a loop.


## Executable Order Versus Narrative Order


> Ok, that's just ordinary Jupyter-notebook practice, right? Code inside your documentation, right? Doxygen and Sphinx inside-out, right?


No, Literate Programming is _both_ inside out _and_ upside-down from the usual, broken, way! "Notebook" solves the inside-out problem; Literate Programming solves the upside-down problem.


With ordinary notebook practice, you must write everything in ***executable order***, because a Jupyter notebook is just an interface to an execution kernel. The notebook inherits the sequential constraints of the underlying intrepreter and compiler. Executable order usually forces us to define all details before using them. With Literate Programming, you write in ***narrative order***, much more understandable to humans.


Executable order is usually the reverse of narrative order. Humans want to understrand the big picture *first*, then the details. They want to see the box-top of the jigsaw puzzle _before_ looking at all the pieces. Executable order is ***upside-down*** to the human's point-of-view.


We've all had the experience of reading code and notebooks backwards so we don't get overwhelmed by details before understanding the big picture. That observation leads us to another imperative.


> Write about your code in narrative order. Don't be tyrranized by your programming language into defining everything before you can talk about anything. Use tools to rearrange your code in executable order.


[Donald Knuth](http://amturing.acm.org/award_winners/knuth_1013846.cfm) invented Literate Programming so that he could both write _about_ [MetaFont](https://en.wikipedia.org/wiki/Metafont) and [TeX](https://texfaq.org/FAQ-lit) and _implement_ them in the same place. These are two of the most important computer programs ever written. Their longevity and quality testify to the viability of Literate Programming.


## Tangledown is Here, Inside, README.md


***Tangledown*** is the tool that rearranges code from any Markdown file into executable order. This here document, README.md, the one you're reading right now, is the Literate Program for Tangledown.


Because our documentation language is Markdown, the language of this document is _Literate Markdown_. This here README.md, which you're reading right now, contains all the source for the Literate-Markdown tool, `tangledown.py`, with all its documentation, all presented in narrative order, like a story.


`tangledown.py` ***tangles*** code out of any Markdown document, not just this here README.md that you're reading right now. The verb "tangle" is traditional in Literate Programming. You might think it should be "untangle," because a Literate Markdown document is all tangled up from executable order. But Knuth prefers the human's point of view. The Markdown document contains the code in the _correct_, narrative order.


If we need something _more_ powerful than Tangledown, we can go back to [org-babel](http://orgmode.org/worg/org-contrib/babel/) in Emacs (or [spacemacs](http://spacemacs.org/) for you VIM users). Those are much more powerful, best-of-breed Literate-Programming tools. You have to learn some Emacs to use them, and that's an  barrier for many people. Markdown is good enough for Github, and thus for most of us right now.


You can _also_ run Tangledown inside a Jupyter notebook, specifically one that is linked to this here document, README.md, the one you're reading right now. See [this section](#oh-my-jupytext) for more.


## TangleUp Intro<a id="tangleup"></a>


Tangledown, as a distribution format, is a complete solution to Literate Programming. You get a single Markdown file and all the tested source for your project is included. Run Tangledown and the project is sprayed out on disk, ready for running, further testing, and deploying.


As a development format, it's not quite enough. With only Tangledown, when you modify the source tree, your README.md is _instantly_ out of date. We can't have that. See [Section TangleUp](#tangleup) for more.


## Tangling Up Existing Code


TangleUp can generate unique names, as GUIDs, say, for new source files and blocks. You should be able to TangleUp an existing source tree into a new, fresh, non-pre-existing Markdown file and, then round-trip TangleUp and TangleDown.


## Design and Implementation


Let's do Tangledown, first, and TangleUp [later](#tangleup).


# OH MY! JUPYTEXT<a id="oh-my-jupytext"></a>


***Jupytext*** \[sic\] automatically syncs a Markdown file with a Jupyter notebook. Read about it [here](https://github.com/mwouts/jupytext). It works well in ***JupyterLab***. Read about that [here](https://github.com/jupyterlab/jupyterlab). Specifically, it lets you open this here Markdown file, README.md, that you're reading right now, as a Jupyter notebook, and you can evaluate some cells in the notebook.


Here's how I installed everything on an Apple Silicon (M1) Mac Book Pro, with Python 3.9:

<!-- #raw -->
```
pip install jupyter
pip install jupyterlab
pip install jupytext
```
<!-- #endraw -->

Here is how I run it:

<!-- #raw -->
```
jupyter lab
```
<!-- #endraw -->

or

<!-- #raw -->
```
PYTHONPATH=".:$HOME/Documents/GitHub/tangledow:$HOME/Library/Jupyter/kernels/tangledown_kernel" jupyter lab ~
```
<!-- #endraw -->

when I want the [Tangledown Kernel](#section-tangledown-kernel), and I almost always want the Tangledown kernel.


In JupyterLab


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


This here README.md, the one you're reading right now, should tell the story of Tangledown. We'll use Tangledown to _create_ Tangledown. That's just like bootstrapping a compiler. We'll use Tangledown to tangle Tangledown itself out of this here document named README.md that you're reading right now.


The first part of the story is that I just started writing the story. Then I filled in the code, moved everything around when I needed to, and kept rewriting until it all worked the way I wanted it to work.


## DISCLAIMER<a id="disclaimer"></a>


This is a useful toy, but it has zero error handling. We currently talk only about the happy path. I try to be rude ("DUDE!") in comments every place where I sense trouble, but I'm only sure I haven't been rude enough. Read this with a sense of humor. You're in on the story with me, and it's supposed to be fun!


I also didn't try it on Windows, but I did try it on WSL, the Windows Subsystem for Linux. Works great on WSL!


## HOW TO RUN TANGLEDOWN<a id="how-to-run"></a>


One way: run `python3 tangledown.py REAMDE.md` at the command line. That command should _overwrite_ tangledown.py. The code for tangledown.py is inside this here README.md that you're reading right now. The name of the file to overwrite, namely `tangledown.py`, is embedded inside this here README.md itself, in the `file` attribute of a `<tangle ...>` tag. Read about `tangle` tags [below](#section-tangle-tags)!


If you said `python3 tangledown.py MY-FOO.md`, then you would tangle
code out of `MY-FOO.md`. You'll do that once you start writing your own code in
Tangledown. You will love it! We have some big examples that we'll write about elsewhere. Those examples include embedded code and microcode for exotic hardware, all written in Python!


Tangledown is both a script and a module. You can run Tangledown in a [Jupytext](#oh-my-jupytext) cell after importing some stuff from the module. The next cell illustrates the typical bootstrapping joke of tangling Tangledown itself out of this here README.md that you're reading right now, after this Markdown file has been linked to a Jupytext notebook. We also tangle one example out to `/dev/null`, a nifty way of discarding that example. You'll see that example [below](#section-tangle-tags), where we talk about `tangle` tags.

```python
from tangledown import get_lines, accumulate_lines, tangle_all
tangle_all(*accumulate_lines(*get_lines("README.md")))
```

After you have tangled at least once, as above, and if you switch the notebook kernel to  the new, optional [Tangledown Kernel](#section-tangledown-kernel), you can evaluate the source code for the whole program in the [cell i'm linking right here, later in this notebook](#tangle-listing-tangle-all). ***How Cool is That?***


You'll also need to re-tangle and restoart the Tangledown Kernel when you add new nowebs to your files. Sorry about that. This is still just a toy.


Because Tangledown is a Python module, you can also run Tangledown from inside a standalone Python program, say in PyCharm or VS Code or whatever;
`hello_world_tangler.py` in this repository is an example.

<!-- #region -->
Once again, Jupytext lets you RUN code from a Markdown
document in a JupyterLab notebook with just the ordinary Python3 kernel. If you open `hello_world.md` as a Jupytext
notebook in JupyterLab then you
can run Tangledown in Jupyter cells. Right-click on the name `hello_world.md` in the JupyterLab GUI and choose


`Open With ...` $\longrightarrow$ `Jupytext Notebook`


Then run cells! This is getting close to the high bar set by org-babel!
<!-- #endregion -->

## HOW IT WORKS: Markdown Ignores Mysterious Tags


How can we rearrange code cells in a notebook or Markdown file from human-understandable order to executable order?


Exploit the fact that most Markdown renderers, like Jupytext's, Github's, and [PyCharm's](https://www.jetbrains.com/pycharm/), ignore HTML / XML _tags_ (that is, stuff inside angle brackets) that they don't recognize. Let's enclose blocks of real, live code with `noweb` tags, like this:


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


The contents of a `noweb` tag are between the opening `<noweb ...>` and closing `</noweb>` fenceposts. Markdown renders code contents with syntax coloring and indentation. That's why we want code cells to be CODE cells and not RAW cells.


The term _contents_ is ordinary jargon from HTML, XML, SGML, etc., and applies to any opening `<foo ...>` and closing `</foo>` pair.


#### ATTRIBUTES OF A TAG


The Tangledown dictionary key for contents of a `noweb` tag is the string value of the `name` attribute. For example, in `<noweb name="foo">`, `name` is an _attribute_, and its string value is `"foo"`.


> Noweb names must be unique in a document. TangleUp ensures that when it writes a new Markdown file from existing source, or you may do it by hand.


**NOTE**: the `name` attribute of a `noweb` opener must be on the same line, like this:

<!-- #raw -->
    <noweb name="foo">
<!-- #endraw -->

Ditto for our other tags. That's a limitation of the regular expressions that detect `noweb` tags. Remeber, [Tangledown is a toy](#disclaimer), a useful toy, but it's limited.


#### FENCEPOST CELLS


You can create the fencepost cells, `<noweb ...>` and `</noweb>`, either in the Markdown file, or you can create them in the synchronized Jupytext notebook.


If you create fencepost cells in Markdown, leave a blank line after the opening `<noweb ...>` and a blank line before the closing `</noweb>`. If you don't, the Markdown renderer won't color and indent the contents. Tangledown will still work, but the Markdown renderer will format your code like text without syntax coloring and indentatino.


If you write fencepost cells in Markdown instead of in the notebook, they appear as tiny, invisible Markdown cells because the renderer treats them as empty markdown cells. ***DON'T DELETE THEM***, but you can open (Enter) and close (Shift-Enter) them.


If you create `noweb` and `tangle` tags in the notebook and you want them _visible_, mark them _RAW_ by pressing "R" with the cell highlighted but not editable. Don't mark them CODE (don't press "Y"). Tangledown will break because Jupytext will surround them with triple-backticks.


### `block` tags


Later, in the [second pass](#second-pass), Tangledown blows the contents of `noweb` tags back out wherever it sees `block` tags with matching `name` attributes. That's how you can define code anywhere in your document and use it in any other place, later or earlier, more than once if you like.


`block` tags can and should appear in the contents of `noweb` tags and in the in the contets of `tangle` tags, too. That's how you structure your narrative!


Tangledown discards the contents of `block` tags. Only the `name` attribute of a `block` tag matters.


#### WRITE IN ANY-OLD-ORDER YOU LIKE


You don't have to write the noweb _before_ you write a matching `block` tag. You can refer to a `noweb` tag before it exists in time and space, more than once if you like. You can define things and name things and use things in any order that makes your thinking and your story more clear. This is literature, after all.


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


See the tiny, invisible Markdown cells above and below the code? Play around with opening and closing them with Enter and Shift-Enter, respectively, and marking them RAW (Press "R") and Markdown ("M"). Don't mark them CODE ("Y").


You can evaluate the cell with the new, optional [Tangledown Kernel](#section-tangledown-kernel). If you evaluate the code cell in the Python Kernel, you'll get a syntax error because the `block` tag is not valid Python. The syntax error is harmless to Tangledown.


This code tangles to the file `/dev/null`. That's a nifty trick for temporary `tangle` blocks. You can talk about them, validate them by executing their cells in the [Tangledown Kernel](#section-tangledown-kernel), and throw them away.


[TangleUp](#tangleup) knows where Tangledown puts all the blocks and tangles. That's how, when you change code on disk, TangleUp can put it all back in the single file of Literate Markdown.


# HUMAN! READ THE `block` TAGS!


Markdown renders `block` tags verbatim inside nowebs or tangles. This is good for humans, who will think


> AHA!, this `block` refers to some code in a `noweb` tag somewhere else in this Markdown document. I can read all the details of that code later, when it will make more sense. I can look at the picture on the box before the pieces of the jigsaw puzzle.

> Thank you, kindly, author! Without you, I'd be awash in details. I'd get tired and cranky before understanding the big picture!


See, I'll prove it to you. Below is the code for all of `tangledown.py` itself. You can understand this without understanding the _implementations_ of the sub-pieces, just getting a rought idea of _what_ they do from the names of the `block` tags. **READ THE NAMES IN THE BLOCK TAGS**. Later, if you want to, you can read all the details in the `noweb` tags named by the `block` tags.


# TANGLE ALL<a id="tangle-listing-tangle-all"></a>


If you're running the new, optional [Tangledown Kernel](#section-tangledown-kernel), you can evaluate this next cell and run Tangledown on Tangledown itself, right here in a Jupyter notebook. ***How Cool is That?***

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
    fn, lines = get_lines(get_aFile())
    # test_re_matching(lines)
    nowebs, tangles = accumulate_lines(fn, lines)
    tangle_all(nowebs, tangles)
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

The whole program is in the function `tangle_all`. We get hybrid vigor by testing `__name__` against `"__main__"`: `tangledown.py` is both a script and module.


All we do in `tangle_all` is loop over all the line lists in the tangles (`for filename, liness in tangles.items()`) and [expand them](#expand-tangles) to replace blocks with nowebs. Yes, "liness" has an extra "s". Remember [Smeagol](https://lotr.fandom.com/wiki/Gollum) Pronounce it like "my preciouses, my lineses!"


The code will create the subdirectories needed. For example, if you tangle to file `foo/bar/baz/qux.py,` the code creates the directory chain `./foo/br/baz/` if it doesn't exist.


## TYPES<a id="types"></a>


Let us now explain the implementation. The first block in the tangle above is _types_. What is the noweb of _types_? It's here.


A `Line` is a string, Python base type `str`. `Lines` is the type of a list of lines. `Liness` is the type of a list of list of lines, in a pluralizing shorthand borrowed from Haskell practice. Pronounce `liness` the way [Smeagol](https://lotr.fandom.com/wiki/Gollum) would do: "my preciouses, my lineses!"


A noweb name is a string, and a tangle file name is a string. A line number is an `int`, a Python base type.


Nowebs are dictionaries from noweb names to lines.


Tangles are dictionaries from file names to Liness --- lists of lists of lines. Tangledown accumulates output for `tangle` files mentioned more than once. If you tangle to `qux.py` in one place and then also tangle to `qux.py` somewhere else, the second tangle won't overwrite the first, but append to it. That's why tangles are lists of lists of lines, one list of lines for each mentioning of a tangle file. Read more about that in [expand-tangles](#expand-tangles).

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

We'll implement all the noweb blocks, like `accumulate_contents` and `eatBlockTag`, later. You can read about them, or not, after you've gotten more of the big picture.


## DEBUGGING AND REFACTORING


The Tangledown Kernel doesn't support the Jupytext debugger, yet. Sorry about that. Tangle the code out to disk and debug it with pudb or whatever, then tangle it back up into your Literate Markdown file via [TangleUp](#tangleup).


[Tangledown is still a toy](#disclaimer). Ditto refactoring. PyCharm is great for that, but you'll have to do it on tangled files and detangle (paste) back into the Markdown.


## EXPAND TANGLES<a id="expand-tangles"></a>


We separated out the inner loop over Liness \[sic\] into another function, `expand_tangles`, so that the [Tangledown Kernel](#section-tangledown-kernel) can import it and apply it to `block` tags. `tangle_all` calls `expand_tangles`; `expand_tangles` calls `expand_blocks`. Read about `expand_blocks` [here](#expand-blocks).

```python
from graphviz import Digraph
g = Digraph(graph_attr={'size': '8,5'}, node_attr={'fontname': 'courier'})
g.attr(rankdir='LR')
g.edge('tangle_all', 'expand_tangles')
g.edge('expand_tangles', 'expand_blocks')
g
```

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


Tangledown has two kinds of regular expressions (regexes) for matching tags in a Markdown file:

- regexes for `noweb` and `tangle` tags that appear on lines by themselves, left-justified

- regexes that match `<block ...>` tags that may be indented, and match their closing `</block>` tags, which may appear on the same line as `<block ...>` or on lines by themselves.


Both kinds of regex are ___safe___: they do not match themselves. That means it's safe to run
`tangledown.py` on this here `READMD.md`, which contains tangled source for `tangledown.py`.


The two regexes in noweb `left_justified_regexes` match `noweb` and`tangle` tags that appear on lines by themselves, left-justified.


> They also wont match `noweb` and `tangle` tags that are indented. That lets us _talk about_ `noweb` and `tangle` tags without processing them: just put the examples you're talking about in an _indented_ Markdown code cell instead of in a triple-backticked Markdown code cell.


The names in the attributes of `noweb` and `tangle` tags must start with a letter, and they can contain letters, numbers, hyphens, underscores, whitespace, and dots.


The names of `noweb` tags must be globally unique within the Markdown file. Multiple `tangle` tags may refer to the same output file, in which cases, Tangledown appends the contents of the second and subsequent `tangle` tags to a list of list of lines, to a `Liness`.


### LEFT-JUSTIIED REGEXES


There is a `.*` at the end to catch attributes beyon `name`. A bit of future-proofing.

<!-- #raw -->
<noweb name="left_justified_regexes">
<!-- #endraw -->

```python
noweb_start_re = re.compile (r'^<noweb name="(\w[\w\s\-.]*)".*>$')
noweb_end_re = re.compile (r'^</noweb>$')

tangle_start_re = re.compile (r'^<tangle file="(.+/\\[^/]+|.+)".*>$')
tangle_end_re = re.compile (r'^</tangle>$')
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

### ANYWHERE REGEXES


The regexes in this noweb, `anywhere_regexes`, match `block` tags that may be indented,  preserving indentation. The `block_end_re` regex also preserves indentation. Indentation is critical for Python, Haskell, and other languages.


I converted the 'o' in 'block' to a harmless regex group `[o]` so that `block_end_re` won't match itself. That makes it safe to run this code on this here document itself.

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


The code in noweb `openers` has two `block` tags that refer to the nowebs of the regexes defined above, namely `left_justified_regexes` and `anywhere_regexes`. After Tangledown substitutes the contents of the nowebs for the blocks, the code becomes valid Python and you can call `test_re_matching` in the [Tangledown Kernel](#section-tangledown-kernel) or at the command line. When you call it, it proves that we can recognize all the various kinds of tags. We leave the regexes themselves as global pseudo-constants so that they're both easy to test and to use in the body of the code ([Demeter weeps](https://en.wikipedia.org/wiki/Law_of_Demeter) because of globals).


The code in `hello_world.ipynb` (after you have Paired a Notebook with the Markdown File `hello_world.md`) runs this test as its last act to check that `tangledown.py` was correctly tangled from this here `README.md`. That code works in the ordinary Python kernel and in the [Tangledown Kernel](#section-tangledown-kernel).


Notice the special treatment for block ends, which are usually on the same lines as their block opener tags, but not necessarily so. That lets you put (useless) contents in `block` tags.

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

def test_re_matching(fp: Path, lines: Lines) -> None:
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


Tangledown passes once over the file to collect contents of `noweb` and `tangle` tags, and again over the `tangle` tags to expand `block` tags. In the second pass, Tangledown substitutes noweb contents for corresponding `block` tags until there are no more `block` tags, creating valid Python.


### GET A FILE NAME


`tangledown.py` is both a script and a module. As a script, you run it from the command line, so it gets its input file name from command-line arguments. As a module, called from another Python program, you probably want to give the file as an argument to a function, specifically, to `get_lines`.


Let's write two functions,

- `get_aFile`, which parses command-line arguments and produces a file name; the default file name is `README.md`

- `get_lines`, which

  - gets lines, without processing `noweb`, `tangle`, or `block` tags, from its argument, `aFilename`

  - replaces `#raw` and `#endraw` fenceposts with blank lines

  - writes out the full file path to a secret place where the [Tangledown Kernel](#section-tangledown-kernel) can pick it up


`get_aFile` can parse command-line arguments that come from either `python` on the command line or from a `Jupitext` notebook, which has a few kinds of command-line arguments we must ignore, namely command-line arguments that end in `.py` or in `.json`.


### GET LINES


This method for getting a file name from the argument list will eat all options. It works for the Tangledown Kernel and for tangling down from a script or a notebook, but it's not future-proofed. Tangledown is still a toy.

<!-- #raw -->
<noweb name="print-sys-argv">
<!-- #endraw -->

```python
print({f'len(sys.argv)': len(sys.argv), f'sys.argv': sys.argv})
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

<!-- #raw -->
<noweb name="getting a file and its lines">
<!-- #endraw -->

```python
def get_aFile() -> str:
    """Get a file name from the command-line arguments
    or 'README.md' as a default."""
    <block name="print-sys-argv"></block>
    aFile = 'README.md'  # default
    if len(sys.argv) > 1:
        file_names = [p for p in sys.argv
                        if (p[0] != '-')  # option
                           and (p[-3:] != '.py')
                           and (p[-5:] != '.json')]
        if file_names:
            aFile = sys.argv[1]
    return aFile

raw_line_re: re = re.compile(r'<!-- #(end)?raw -->')
def get_lines(fn: FileName) -> Lines:
    """Get lines from a file named fn. Replace
    'raw' fenceposts with blank lines. Write full path to
    a secret place for the Tangledown kernel to pick it up.
    Return tuple of file path (for TangleUp's Tracer) and
    lines."""
    <block name="save-afile-path-for-kernel"></block>
    xpath = save_aFile_path_for_kernel(fn)
    with open(fn) as f:
        in_lines: Lines = f.readlines ()
        out_lines: Lines = []
        for in_line in in_lines:
            out_lines.append(
                in_line if not raw_line_re.match(in_line) else "\n")
        return xpath, out_lines
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
def save_aFile_path_for_kernel(fn: FileName) -> FileName:
    xpath: Path = Path.cwd() / Path(fn).name
    victim_file_name = str(xpath.absolute())
    safepath: Path = Path.home() / '.tangledown/current_victim_file.txt'
    Path(safepath).parents[0].mkdir(parents=True, exist_ok=True)
    print(f"SAVING {victim_file_name} in secret place {str(safepath)}")
    with open(safepath, "w") as t:
        t.write(victim_file_name)
    return xpath
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

### First Pass: Saving Noweb and Tangle Blocks


In the first pass over the file, we'll just save the contents of noweb and tangle into dictionaries, without expanding nested `block` tags.


#### OH NO! THERE ARE TWO WAYS


Turns out there are two ways to write code blocks in Markdown:

1. indented by four spaces, useful for quoted Markdown and quoted triple-backtick blocks

2. surrounded by triple backticks and _not_ indented.


Tangledown must handle both ways.


We use the trick of a harmless regex group --- regex stuff inside square brackets --- around one of the backticks in the regex that recognizes triple backticks. This regex is safe to run on itself. See `triple_backtick_re` in the code immediately below.


The function `first_non_blank_line_is_triple_backtick`, in noweb `oh-no-there-are-two-ways` recognizes code blocks bracketed by triple backticks. The contents of this `noweb` tag  is triple-bacticked, itself. Kind of a funny self-toast joke, no?


Remember the _use-mention_ dichotomy from Philosophy class? No problem if you don't.


When we're _talking about_ `noweb` and `tangle` tags, but don't want to process them, we indent the tags and the code blocks. Tangledown won't process indented `noweb` and `tangle` tags because the regexes in noweb `left_justified_regexes` won't match them. 


We can also talk about triple-backticked blocks by indenting them. Tangledown won't mess with indented triple-backticked blocks, because the regex needs them left-justified. Markdown also wont get confused, so we can quote whole markdown files by indenting them. Yes, your Literate Markdown can _also_, recursively, tangle out more Markdown files. How cool is that? Will the recursive jokes never end?


[TangleUp](#tangleup) has a heuristic for placing language and id information on triple-backtick fence openers. Our function will retrieve those if present.


We see, below, why the code tracks line numbers. We might do all this in some super-bitchin', sophomoric list comprehension, but this is more obvious-at-a-glance. That's a good thing.


#### FIRST NON-BLANK LINE IS TRIPLE BACKTICK

<!-- #raw -->
<noweb name="oh-no-there-are-two-ways">
<!-- #endraw -->

```python
triple_backtick_re = re.compile (r'^`[`]`((\w+)?\s*(id=([0-9a-fA-F-]+))?)')
blank_line_re      = re.compile (r'^\s*$')

def first_non_blank_line_is_triple_backtick (
        i: LineNumber, lines: Lines) -> Match[Line]:
    while (blank_line_re.match (lines[i])):
        i = i + 1
    yes = triple_backtick_re.match (lines[i])
    language = "python"  # default
    id_ = None           # default
    if yes:
        language = yes.groups()[1] or language
        id_ = yes.groups()[3]  ## can be 'None'
    return i, yes, language, id_
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### ACCUMULATE CONTENTS<a id="accumulate-contents"></a>


Tangledown is a funny little compiler. It converts Literate Markdown to Python or other languages (Tangledown supports Clojure and Markdown, too). We could go nuts and write it in highfalutin' style, and then it would be much bigger, more elaborate, and easier to explain to a Haskell programmer. It might also be less of a toy. However, we want this toy Tangledown for now to be:

- very short

- independent of rich libraries like beautiful soup and parser combinators

- completely obvious to anyone


We'll just use iteration and array indices, but in a tasteful way so our functional friends won't puke. This is Python, after all, not Haskell! We can just _get it done_, with grace, panache, and aplomb.


The function `accumulate_contents` accumulates the contents of left-justified `noweb` or `tangle` tags. The function starts at line `i` of the input, then figures out whether a tag's first non-blank line is triple backtick, in which case it _won't_ snip four spaces from the beginning of every line, and finally keeps going until it sees the closing fencepost, `</noweb>` or `</tangle>`. It returns a tuple of the line index _after_ the closing fencepost, and the contents, possibly de-dented. The function manipulates line numbers to skip over triple backticks.

<!-- #raw -->
<noweb name="accumulate-contents">
<!-- #endraw -->

```python
def accumulate_contents (
        lines: Lines, i: LineNumber, end_re: re) -> LinesTuple:
    r"""Harvest contents of a noweb or tangle tag. The start
    taglet was consumed by caller. Consume the end taglet."""
    i, yes, language, id_ = first_non_blank_line_is_triple_backtick(i, lines)
    snip = 0 if yes else 4
    contents_lines: Lines = []
    for j in range (i, len(lines)):
        if (end_re.match(lines[j])):
            return j + 1, language, id_, contents_lines  # the only return
        if not triple_backtick_re.match (lines[j]):
            contents_lines.append (lines[j][snip:])
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### ACCUMULATE LINES


The function `accumulate_lines` calls `accumulate_contents` to suck up the contents of all the left-justified `noweb` tags and `tangle` tags out of a file, but doesn't expand any `block` tags that it finds. It just builds up dictionaries, `noweb_blocks` and `tangle_files`, keyed by `name` or `file` attributes it finds inside `noweb` or `tangle` tags.


`accumulate_lines` also writes out a trace file for [TangleUp](#tangleup). 

<!-- #raw -->
<noweb name="accumulate-lines">
<!-- #endraw -->

```python
<block name="normalize-file-path"></block>
<block name="tracer"></block>
from pprint import pprint
def accumulate_lines(fp: Path, lines: Lines) -> Tuple[Nowebs, Tangles]:
    tracer = Tracer()
    nowebs: Nowebs = {}
    tangles: Tangles = {}
    i = 0
    while i < len(lines):
        noweb_start_match = noweb_start_re.match (lines[i])
        tangle_start_match = tangle_start_re.match (lines[i])
        if (noweb_start_match):
            key: NowebName = noweb_start_match.group(1)
            (i, language, id_, nowebs[key]) = \
                accumulate_contents(lines, i + 1, noweb_end_re)
            tracer.add_noweb(i, language, id_, key, nowebs[key])
        elif (tangle_start_match):
            key: TangleFileName = \
                str(normalize_file_path(tangle_start_match.group(1)))
            if not (key in tangles):
                tangles[key]: Liness = []
            (i, language, id_, things) = accumulate_contents(lines, i + 1, tangle_end_re)
            tangles[key] += [things]
            tracer.add_tangle(i, language, id_, key, tangles[key])
        else:
            tracer.add_markdown(i, lines[i])
            i += 1
    tracer.dump(fp)
    return nowebs, tangles
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### TRACER


For [TangleUp](#tangleup), we'll need to trace the entire operation of Tangledown. TangleUp reverses Tangledown, so we will want a best-effort reconstruction of the original Markdown file.


Our first approach will be a sequential list of dictionaries with all the needed information.

<!-- #raw -->
<noweb name="tracer">
<!-- #endraw -->

```python
from dataclasses import dataclass, field
from typing import Union  ## TODO
@dataclass
class Tracer:
    trace: List[Dict] = field(default_factory=list)
    line_no = 0
    current_betweens: Lines = field(default_factory=list)
    def add_markdown(self, i, between: Line):
        self.line_no += 1
        self.current_betweens.append((self.line_no, between))
    def _end_betweens(self, i):
        if self.current_betweens:
            self.trace.append({"ending_line_number": self.line_no, "i": i,
                               "language": "markdown", "kind": 'between',
                               "text": self.current_betweens})
        self.current_betweens = []
    def add_noweb(self, i, language, id_, key, noweb_lines):
        self._end_betweens(i)
        self.line_no = i
        self.trace.append({"ending_line_number": self.line_no, "i": i,
                           "language": language, "id_": id_,
                           "kind": 'noweb', key: noweb_lines})
    def add_tangle(self, i, language, id_, key, tangle_liness):
        self._end_betweens(i)
        self.line_no = i
        self.trace.append({"ending_line_number": self.line_no, "i": i,
                           "language": language, "id_": id_,
                           "kind": 'tangle', key: tangle_liness})
    def dump(self, fp: Path):
        pr = fp.parent
        fn = fp.name
        fn2 = fn.translate(str.maketrans('.', '_'))
        # Store the trace in the dir where the input md file is:
        vr = f'tangledown_trace_{fn2}'
        np = pr / (vr + ".py")
        with open(np, "w") as fs:
            print(f'{vr} = (', file=fs)
            pprint(self.trace, stream=fs)
            print(')', file=fs)
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### NORMALIZE FILE PATH


We must normalize file names so that, for example, "foo.txt" and "./foo.txt" indicate the same file and so that `~/` denotes the home directory on Mac and Linux. I didn't test this on Windows.

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
- mismatched fenceposts
- dangling tags
- misspelled names
- syntax errors
- infinite loops (cycles, hangs)
- much, much more


We'll get to error handling someday, maybe. Tangledown is [just a little toy at the moment](#disclaimer), but I thought it interesting to write about. If it's ever distributed to hostile users, then we will handle all the bad cases. But not now. Let's get the happy case right.


### Second Pass: Expanding Blocks<a id="second-pass"></a>


Iterate over all the `noweb` or `tangle` tag contents and expand the
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
def expand_blocks (nowebs: Nowebs, lines: Lines,
                   language: str = "python") -> Lines:
    out_lines = []
    block_key: NowebName = ""
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

# Tangle It, Already!<a id="tangle-already"></a>


Ok, you saw [at the top](#how-to-run) that the code in this here Markdown document, README.md, when run as a script, will read in all the lines in ... this here Markdown document, `README.md`. Bootstrapping!


But you have to run something first. For that, I tangled the code manually just
once and provide `tangledown.py` in the repository. The chicken definitely comes
before the egg.


But if you have the chicken (`tangledown.py`), you can import it as a module and execute the following cell, a copy of the one [at the top](#how-to-run). That should overwrite `tangledown.py` with the contents of this notebook or Markdown file. So our little bootstrapping technique will forever update the Tangledown compiler if you change it in this here README.md that you're reading right now!

```python
from tangledown import get_lines, accumulate_lines, tangle_all
tangle_all(*accumulate_lines(*get_lines("README.md")))
```

# TODO<a id="todo"></a>


- IN-PROGRESS: more examples, specifically, a test-generator in Clojure in subdirectory `examples/asr`.
- IN-PROGRESS: TangleUp
- NOT-STARTED: Have the Tangledown Kernel, when evaluating tangle-able cells, write them out one at a time. Without this feature, the only way to write out files is to tangle the entire notebook. Possibly do these as cell magics.
- NOT-STARTED: Research cell magics for `noweb` and `tangle` cells.
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


## DUDE!


Some people write "TODO" in their code so they can find all the spots where they thought they might have trouble but didn't have time to write the error-handling (prophylactic) code at the time. I like to write "DUDE" because it sounds like both "TODO" but is more RUDE (also sounds like "DUDE") and funny. This story is supposed to be amusing.


## Known Bugs to Fix<a id="section-known-bugs"></a>


I must apologize once again, but this is just a toy at this point! Recall the [DISCLAIMER](#disclaimer). The following are stackranked from highest to lowest priority.


1. FIXED: writing to "tangledown.py" and to "./tangledown.py" clobbers the file rather than appending. Use pathlib to compare filenames rather than string comparison.
2. FIXED: tangling to files in the home directory via `~` does not work. We know one dirty way to fix it, but proper practice with pathlib is a better answer.


# TangleUp Design and Implementation<a id="tangleup"></a>


## TANGLEUP TENETS


1. Keep source tree and Literate Markdown consistent.


## NON-REAL-TIME


We'll start with a non-real-time solution. You'll manually run `tangleup` to put modified source back into the Markdown. Later, we'll do something that can track changes on disk and update the Markdown in real time.


When you modify your source tree, `tangleup` puts the modified code back into the Markdown file with reminders to _detangle_ and to _write_. There are two cases:

1. You modified some source that corresponds to an existing noweb block in the Markdown.

2. You added some source that doesn't yet correspond to a noweb block in the Markdown.


To assist TangleUp, Tangledown records unique names for existing noweb blocks along with the tangled source. Tangledown also records robust locations for existing blocks. _Robust_ means that the boundary locations are flexible: starting and ending line and character positions in a source file are not enough because changing an early one invalidates all later ones.


## When There Is No Existing Markdown File


We don't need the trace file for this case.


Enumerate all the files in a directory tree. Pair each file name with a short, unique name for the nowebs. TODO: ignore files and directories listed in the `.gitignore`.

```python
%pip install gitignore-parser
```

### TANGLEUP FILES LIST

<!-- #raw -->
<noweb name="tangleup-files-list">
<!-- #endraw -->

```python
<block name="tangleup imports"></block>
def files_list(dir_name: str) -> List[str]:
    dir_path = Path(dir_name)
    files_result = []
    nyms_result = []
    file_count = 0
    <block name="unique-names"></block>
    <block name="ignore files in .gitignore"></block>
    <block name="recurse a dir"></block>
    find_first_gitignore()
    recurse_a_dir(dir_path)
    assert file_count == len(nyms_collision_check)
    return list(zip(files_result, nyms_result))
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### RECURSE A DIR


The only complexity, here, is ignoring `.git` and files in `.gitignore`

<!-- #raw -->
<noweb name="recurse a dir">
<!-- #endraw -->

```python
def recurse_a_dir(dir_path: Path) -> None:
    for p in dir_path.glob('*'):
        q = p.absolute()
        qs = str(q)
        try:  # don't skip files in dirs above .gitignore
            ok = not in_gitignore(qs)
        except ValueError as e: # one absolute and one relative?
            ok = True
        if p.name == '.git':
            ok = False
        if not ok:
            pprint(f'... IGNORING file or dir {p}')
        if ok and q.is_file():
            nonlocal file_count
            file_count += 1
            nyms_result.append(gsnym(q))
            files_result.append(qs)
        elif ok and p.is_dir:
            recurse_a_dir(p)
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### UNIQUE NAMES


Correct for collisions, which will be really rare, so there is a negligible effect on speed.

<!-- #raw -->
<noweb name="unique-names">
<!-- #endraw -->

```python
nyms_collision_check = set()

def gsnym(p: Path) -> str:
    """Generate a short, unique name for a path."""
    nym = gsnym_candidate(p)
    while nym in nyms_collision_check:
        nym = gsnym_candidate(p)
    nyms_collision_check.add(nym)
    return nym


def gsnym_candidate(p: Path) -> str:
    """Generate a candidate short, unique name for a path."""
    return p.stem + '_' + uuid.uuid4().hex[:6].upper()
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### IGNORE FILES IN GITIGNORE


Find the first `.gitignore` in a directory tree. Parse it to produce a function that tests whether a file must be ignored by TangleUp. 

<!-- #raw -->
<noweb name="ignore files in .gitignore">
<!-- #endraw -->

```python
in_gitignore = lambda _: False

def find_first_gitignore() -> Path:
    p = dir_path
    for p in dir_path.rglob('*'):
        if p.name == '.gitignore':
            in_gitignore = parse_gitignore(str(p.absolute()))
            break;
    return p
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

### TANGLEUP IMPORTS

<!-- #raw -->
<noweb name="tangleup imports">
<!-- #endraw -->

```python
from pathlib import Path
from typing import List
import uuid
from gitignore_parser import parse_gitignore
from pprint import pprint
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

### WRITE NOWEB TO LINES


Now write the contents of each Python or Clojure file to a noweb block with its ginned-up name and a corresponding tangle block. Parenthetically, this just _screams_ for the Writer monad, but we'll just do it by hand in an obvious, kindergarten way.files_result


**WARNING**: The explicit '\n' newlines probably won't work on Windows.

<!-- #raw -->
<noweb name="tangleup-write-noweb-to-lines">
<!-- #endraw -->

```python
from typing import Tuple
from pprint import pprint
<block name="wrap one as raw"></block>
<block name="wrap several with blank lines"></block>
<block name="wrap lines with triple backticks"></block>
<block name="indent four spaces"></block>
def write_noweb_to_lines(lines: List[str],
                         file_gsnym_pair: Tuple[str],
                         language: str) -> None:
    path = Path(file_gsnym_pair[0])
    wrap_n_blank(lines, [f'## {path.name}\n'])
    wrap_1_raw(lines, f'<noweb name="{file_gsnym_pair[1]}">\n')
    with open(file_gsnym_pair[0]) as f:
        try:
            inlines = f.readlines()
        except UnicodeDecodeError as e:
            pprint(f'... SKIPPING UNDECODABLE FILE {path}')
            return
        pprint(f'DETANGLING file {path}')
    bound = []  ## Really want the monadic bind, here.
    if language == "markdown":
        indent_4(bound, inlines)
    else:
        wrap_triple_backtick(bound, inlines, language)
    wrap_n_blank(lines, bound)
    wrap_1_raw(lines, '</noweb>\n')
    lines.append(BLANK_LINE)
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### WRAP ONE LINE AS RAW

<!-- #raw -->
<noweb name="wrap one as raw">
<!-- #endraw -->

```python
BEGIN_RAW = '<!-- #raw -->\n'
END_RAW = '<!-- #endraw -->\n'
def wrap_1_raw(lines: List[str], s: str) -> None:
    lines.append(BEGIN_RAW)
    lines.append(s)
    lines.append(END_RAW)
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### WRAP SEVERAL LINES IN BLANK LINES

<!-- #raw -->
<noweb name="wrap several with blank lines">
<!-- #endraw -->

```python
BLANK_LINE = '\n'
def wrap_n_blank(lines: List[str], ss: List[str]) -> None:
    lines.append(BLANK_LINE)
    for s in ss:
        lines.append(s)
    lines.append(BLANK_LINE)
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### WRAP LINES IN TRIPLE BACKTICKS

<!-- #raw -->
<noweb name="wrap lines with triple backticks">
<!-- #endraw -->

```python
def wrap_triple_backtick(lines: List[str],
                         ss: List[str],
                         language: str) -> None:
    lines.append(f'```{language}\n')
    for s in ss:
        lines.append(s)
    lines.append(f'```\n')
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

#### INDENT ALL LINES FOUR SPACES

<!-- #raw -->
<noweb name="indent four spaces">
<!-- #endraw -->

```python
def indent_4(lines: List[str], ss: List[str]):
    for s in ss:
        lines.append('    ' + s)
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

### WRITE TANGLE TO LINES

<!-- #raw -->
<noweb name="tangleup-write-tangle-to-lines">
<!-- #endraw -->

```python
def write_tangle_to_lines(lines: List[str],
                          file_gsnym_pair: Tuple[str],
                          language: str) -> List[str]:
    wrap_1_raw(lines, f'<tangle file="{file_gsnym_pair[0]}">\n')
    bound = []
    wrap_triple_backtick(bound,
                         [f'<block name="{file_gsnym_pair[1]}"></block>\n'],
                         language)
    wrap_n_blank(lines, bound)
    wrap_1_raw(lines, f'</tangle>\n')
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

### TANGLEUP OVERWRITE MARKDOWN


Test the whole magillah, the up direction. You may have to backpatch some 'language' names when you open the markdown, but 'language' only affects syntax coloring.

<!-- #raw -->
<noweb name="tangleup-overwrite-markdown">
<!-- #endraw -->

```python
<block name="tangleup-files-list"></block>
<block name="tangleup-write-noweb-to-lines"></block>
<block name="tangleup-write-tangle-to-lines"></block>
def tangleup_overwrite_markdown(
        output_markdown_filename: str,
        input_directory: str,
        title: str = "Untitled") -> None:
    pprint(f'WRITING LITERATE MARKDOWN to file {output_markdown_filename}')
    file_gsnym_pairs = files_list(input_directory)
    lines: List[str] = [f'# {title}\n\n']
    for pair in file_gsnym_pairs:
        p = Path(pair[0])
        if p.suffix == '.clj':
            language = f'clojure id={uuid.uuid4()}'
        elif p.suffix == '.py':
            language = f'python id={uuid.uuid4()}'
        elif p.suffix == '.md':
            language = 'markdown'
        else:
            language = ''
        write_noweb_to_lines(lines, pair, language)
        write_tangle_to_lines(lines, pair, language)
    import json
    
    with open(output_markdown_filename, "w") as f:
        for line in lines:
            f.write(line)
    pass
```

<!-- #raw -->
</noweb>
<!-- #endraw -->

## When there is a Pre-Existing Markdown File


### FIRST SHOT

```python
with open("./.tangledown-trace-foobar_md.py") as f:
    contents = f.read()
contents
```

## UNIT TESTS


### NO PRE-EXISTING MARKDOWN FILE


Run these at the console for now.

<!-- #raw -->
<tangle file="tangleup_experiment.py">
<!-- #endraw -->

```python
<block name="tangleup-overwrite-markdown"></block>
if __name__ == "__main__":
    tangleup_overwrite_markdown(
        "asr_tangleup_test.md",
        "./examples",
        title="This is a First Test of the Emergency Tangleup System")
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

<!-- #raw -->
<tangle file="tangleup_experiment_2.py">
<!-- #endraw -->

```python
<block name="tangleup-overwrite-markdown"></block>
if __name__ == "__main__":
    tangleup_overwrite_markdown(
        "tangleup-test.md",
        ".",
        title="This is a Second Test of the Emergency Tangleup System")
```

<!-- #raw -->
</tangle>
<!-- #endraw -->

# APPENDIX: Developer Notes


If you change the code in this README.md and you want to test it by running the cell in Section [Tangle It, Already!](#tangle-already), you usually must restart whatever Jupyter kernel you're running because Jupytext caches code. If things continue to not make sense, try restarting the notebook server. It rarely but occasionally produces incorrect answers for more obscure reasons.


# APPENDIX: Tangledown Kernel<a id="section-tangledown-kernel"></a>


The Tangledown kernel is ***OPTIONAL***, but nice. Everything I talked about so far works fine without it, but the Tangledown Kernel lets you evaluate Jupytext notebook cells that have `block` tags in them. For example, you can run Tangledown on Tangledown itself in this notebook just by evaluating the cell that contains all of Tangledown, including the source for the kernel, [here](#tangle-listing-tangle-all).


The Tangledown Compiler writes the full path of the current Markdown file corresponding to the current notebook to fixed place in the home directory, and the Tangledown Kernel reads gets all the nowebs from there.


> If you run more than one instance of the Tangledown Kernel at one time on your machine, you must ***RETANGLE THE FILE AND RESTART THE TANGLEDOWN KERNEL WHEN YOU SWITCH NOTEBOOKS*** because the name of the current file is a fixed singleton. The Tangledown Kernel has no way to dynamically know what file you're working with. Sorry about that!


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
```
PYTHONPATH=".:/Users/brian/Library/Jupyter/kernels/tangledown_kernel" jupyter lab
```
<!-- #endraw -->

Once the kernel is installed, there are multiple ways to run it in Jupyter Lab. When you first open a notebook, you get a menu. The default is the regular Python 3 kernel, and it works fine, but you won't be able to run cells that have `block` tags in them. If you choose the Tangledown Kernel, you can run such cells.


If you modify the kernel:

1. re-tangle the kernel source, say by running the cell in [this section](#how-to-run)
2. re-install the kernel by running the little bash script above
3. restart the kernel inside the notebook


Most of the time, you don't have to restart Jupyter Lab itself, but sometimes after a really bad bug, you might have to.


## Source for the Tangledown Kernel


Adapted from [these official docs](https://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html).


The kernel calls [`expand_tangles`](#expand-tangles) after reformatting the lines a little. We learned about the reformatting by experiment. We explain `expand_tangles` [here](#expand-tangles) in the [section about Tangledown itself](#tangle-listing-tangle-all). The rest of this is boilerplate from the [official kernel documentation](https://jupyter-client.readthedocs.io/en/stable/wrapperkernels.html). There is no point, by the way, in running the cell below in any kernel. It's meant for the Jupyterlab startup engine, only. You just need to tangle it out and install it, as above.


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

## KERNEL INSTANCE VARIABLES


These get indented on expansion because the `block` tag is indented. You could do it the other way: indent the code here and DON'T indent the block tag, but that would be ugly, wouldn't it?


Notice this kernel runs Tangledown on the full file path that's stored in `current_victim_file.txt`. That file path got [written to that special place](#save-afile-path-for-kernel) when you tangled the file the first time. This may explain why you must tangle the file once and then restart the kernel whenever you switch notebooks that are running the Tangledown Kernel.

<!-- #raw -->
<noweb name="kernel-instance-variables">
<!-- #endraw -->

```python
current_victim_filepath = ""
with open(Path.home() / '.tangledown/current_victim_file.txt') as v:
    fp = v.read()
nowebs, tangles_ = accumulate_lines(*get_lines(fp))
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

## Kernel JSON Installation Helper

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
