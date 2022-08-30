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

import re
import sys
from pathlib import Path

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

def save_aFile_path_for_kernel(aFile: FileName) -> FileName:
  xpath: Path = Path.cwd() / Path(aFile).name
  victim_file_name = str(xpath.absolute())
  safepath: Path = Path.home() / '.tangledown/current_victim_file.txt'
  Path(safepath).parents[0].mkdir(parents=True, exist_ok=True)
  print(f"SAVING {victim_file_name} in secret place {str(safepath)}")
  with open(safepath, "w") as t:
      t.write(victim_file_name)
  return aFile

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

noweb_start_re = re.compile (r'^<noweb name="(\w[\w\s\-.]*)">$')
noweb_end_re = re.compile (r'^</noweb>$')

tangle_start_re = re.compile (r'^<tangle file="(.+/\\[^/]+|.+)">$')
tangle_end_re = re.compile (r'^</tangle>$')

block_start_re = re.compile (r'^(\s*)<block name="(\w[\w\s\-.]*)">')
block_end_re = re.compile (r'^(\s)*</bl[o]ck>')


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

triple_backtick_re = re.compile (r'^`[`]`')
blank_line_re      = re.compile (r'^\s*$')

def first_non_blank_line_is_triple_backtick (
        i: LineNumber, lines: Lines) -> Match[Line]:
    while (blank_line_re.match (lines[i])):
        i = i + 1
    return triple_backtick_re.match (lines[i])

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

def anchor_is_tilde(path_str: str) -> bool:
    result = (path_str[0:2] == "~/") and (Path(path_str).anchor == '')
    return result

def normalize_file_path(tangle_file_attribute: str) -> Path:
    result: Path = Path(tangle_file_attribute)
    if (anchor_is_tilde(tangle_file_attribute)):
        result = (Path.home() / tangle_file_attribute[2:])
    return result.absolute()

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

def there_is_a_block_tag (lines: Lines) -> bool:
    for line in lines:
        block_start_match = block_start_re.match (line)
        if (block_start_match):
            return True
    return False

def eat_block_tag (i: LineNumber, lines: Lines) -> LineNumber:
    for j in range (i, len(lines)):
        end_match = block_end_re.match (lines[j])
        # DUDE! Check leading whitespace against block_start_re
        if (end_match):
            return j + 1
        else:  # DUDE!
            pass

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

def expand_tangles(liness: Liness, nowebs: Nowebs) -> str:
    contents: Lines = []
    for lines in liness:
        while there_is_a_block_tag (lines):
            lines = expand_blocks (nowebs, lines)
        contents += lines
    return ''.join(contents)



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

