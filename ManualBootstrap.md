---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Manually Bootstrapping Tangledown


This is an illiterate version of `tangledown.py`, one that will bootstrap `tangledown.py`. That means this notebook will tangle `tangledown.py` out of `README.md`. Once that is done one time, you can run `python tangledown.py README.md` over and over again. Each time, `tangledown.py` will be overwritten by a copy of itself. You can also tangle `tangledown.py` from another Python program by importing functions from `tangledown.py`. The notebook `hello_world.ipynb` shows how to do that.

```python
from typing import List, Dict, Tuple, Match
```

```python
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

```python
import re
import sys
from pathlib import Path
```

```python
def get_aFile() -> str:
    """Get a file name from the command-line arguments."""
    print({f'len(sys.argv)': len(sys.argv), f'sys.argv': sys.argv})
    
    
    aFile = 'README.md'  # default
    if len(sys.argv) > 1:
        file_names = [p for p in sys.argv
                        if (p[0] != '-')  # option
                           and (p[-3:] != '.py')
                           and (p[-5:] != '.json')]
        if file_names:
            aFile = sys.argv[1]
    return aFile
```

```python
raw_line_re: re = re.compile(r'<!-- #(end)?raw -->')
def get_lines(fn: FileName) -> Lines:
    """Get lines from a file named fn. Replace
    'raw' fenceposts with blank lines. Write full path to
    a secret place for the Tangledown kernel to pick it up.
    Return tuple of file name (for Tracer) and lines """
    def save_aFile_path_for_kernel(fn: FileName) -> FileName:
        xpath: Path = Path.cwd() / Path(fn).name
        victim_file_name = str(xpath.absolute())
        safepath: Path = Path.home() / '.tangledown/current_victim_file.txt'
        Path(safepath).parents[0].mkdir(parents=True, exist_ok=True)
        print(f"SAVING {victim_file_name} in secret place {str(safepath)}")
        with open(safepath, "w") as t:
            t.write(victim_file_name)
        return xpath
    
    
    xpath = save_aFile_path_for_kernel(fn)
    with open(fn) as f:
        in_lines: Lines = f.readlines ()
        out_lines: Lines = []
        for in_line in in_lines:
            out_lines.append(
                in_line if not raw_line_re.match(in_line) else "\n")
        return xpath, out_lines
```

```python
noweb_start_re = re.compile (r'^<noweb name="(\w[\w\s\-.]*)".*>$')
noweb_end_re = re.compile (r'^</noweb>$')
```

```python
tangle_start_re = re.compile (r'^<tangle file="(.+/\\[^/]+|.+)".*>$')
tangle_end_re = re.compile (r'^</tangle>$')
```

```python
block_start_re = re.compile (r'^(\s*)<block name="(\w[\w\s\-.]*)">')
block_end_re = re.compile (r'^(\s)*</bl[o]ck>')
```

```python
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

```python
triple_backtick_re = re.compile (r'^`[`]`((\w+)?\s*(id=([0-9a-fA-F-]+))?)')
blank_line_re      = re.compile (r'^\s*$')
```

```python
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

```python
def anchor_is_tilde(path_str: str) -> bool:
    result = (path_str[0:2] == "~/") and (Path(path_str).anchor == '')
    return result
```

```python
def normalize_file_path(tangle_file_attribute: str) -> Path:
    result: Path = Path(tangle_file_attribute)
    if (anchor_is_tilde(tangle_file_attribute)):
        result = (Path.home() / tangle_file_attribute[2:])
    return result.absolute()
```

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
        np = pr / f".tangledown-trace-{fn2}.py"
        vr = f'tangledown_trace_{fn2}'
        with open(np, "w") as fs:
            print(f'{vr} = (', file=fs)
            pprint(self.trace, stream=fs)
            pprint(')', stream=fs)
```

```python
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

```python
def there_is_a_block_tag (lines: Lines) -> bool:
    for line in lines:
        block_start_match = block_start_re.match (line)
        if (block_start_match):
            return True
    return False
```

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

```python
def expand_tangles(liness: Liness, nowebs: Nowebs) -> str:
    contents: Lines = []
    for lines in liness:
        while there_is_a_block_tag (lines):
            lines = expand_blocks (nowebs, lines)
        contents += lines
    return ''.join(contents)
```

```python
def tangle_all(nowebs: Nowebs, tangles: Tangles) -> None:
    for filename, liness in tangles.items ():
        Path(filename).parents[0].mkdir(parents=True, exist_ok=True)
        contents: str = expand_tangles(liness, nowebs)
        with open (filename, 'w') as outfile:
            print(f"WRITING FILE: {filename}")
            outfile.write (contents)
```

```python
if __name__ == "__main__":
    fn, lines = get_lines(get_aFile())
    # test_re_matching(lines)
    nowebs, tangles = accumulate_lines(fn, lines)
    tangle_all(nowebs, tangles)
```
