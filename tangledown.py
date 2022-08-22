import re
import sys

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

raw_line_re = re.compile(r'<!-- #(end)?raw -->')
def get_lines(aFilename):
    """Get lines from a file denoted by aFilename."""
    with open(aFilename) as aFile:
        in_lines = aFile.readlines ()
        out_lines = []
        for in_line in in_lines:
            if not raw_line_re.match(in_line):
                out_lines.append(in_line)
        return out_lines

noweb_start_re = re.compile (r'^<noweb name="(\w[\w\s\-\.]*)">$')
noweb_end_re = re.compile (r'^</noweb>$')

tangle_start_re = re.compile (r'^<tangle file="(.+\/\\[^\/]+|.+)">$')
tangle_end_re = re.compile (r'^</tangle>$')

block_start_re = re.compile (r'^(\s*)<block name="(\w[\w\s\-\.]*)">')
block_end_re = re.compile (r'^(\s)*</bl[o]ck>')


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

triple_backtick_re = re.compile (r'^`[`]`')
blank_line_re      = re.compile (r'^\s*$')

def first_non_blank_line_is_triple_backtick (i, lines):
    while (blank_line_re.match (lines[i])):
        i = i + 1
    return triple_backtick_re.match (lines[i])

def accumulate_contents (lines, i, end_re):
    r"""Harvest contents of a noweb or tangle tag. The start
    taglet was consumed by caller; we consume the end taglet."""
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

import json
from pathlib import Path
def dump_current_markdown_artifacts(nowebs, tangles):
    tangledown_dirpath = str(Path.home()) + '/.tangledown/' 
    nowebspath = tangledown_dirpath + "nowebs.json" 
    tanglespath = tangledown_dirpath + "tangles.json"
    # only need to do this 'mkdir' once for both files
    Path(nowebspath).parents[0].mkdir(parents=True, exist_ok=True)
    with open(tanglespath, "w") as t:
        json.dump(tangles, t)
    with open(nowebspath, "w") as n:
        json.dump(nowebs, n)
    return nowebs, tangles

def anchor_is_tilde(path_str: str) -> bool:
    result = (path_str[0:2] == "~/") and (Path(path_str).anchor == '')
    return result

def normalize_file_path(tangle_file_attribute: str) -> Path:
    result: Path = Path(tangle_file_attribute)
    if (anchor_is_tilde(tangle_file_attribute)):
        result = (Path.home() / tangle_file_attribute[2:])
    return result

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
            file_key = str(normalize_file_path(tangle_start_match.group(1)))
            if not (file_key in tangle_files):
                tangle_files[file_key] = []
            tangle_files[file_key] += \
                [accumulate_contents(lines, i + 1, tangle_end_re)[1]]
    return dump_current_markdown_artifacts(noweb_blocks, tangle_files)

def there_is_a_block_tag (lines):
    for line in lines:
        block_start_match = block_start_re.match (line)
        if (block_start_match):
            return True
    return False

def eat_block_tag (i, lines):
    for j in range (i, len(lines)):
        end_match = block_end_re.match (lines[j])
        # DUDE! Check leading whitespace against block_start_re
        if (end_match):
            return j + 1
        else:  # DUDE!
            pass

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


def expand_lines_list(lines_list, noweb_blocks):
    contents = []
    for lines in lines_list:
        while there_is_a_block_tag (lines):
            lines = expand_blocks (noweb_blocks, lines)
        contents += lines
    return ''.join(contents)


def tangle_all(noweb_blocks, tangle_files):
    from pathlib import Path
    for k, lines_list in tangle_files.items ():
        Path(k).parents[0].mkdir(parents=True, exist_ok=True)
        joined_contents = expand_lines_list(lines_list, noweb_blocks)
        with open (k, 'w') as outfile:
            print(f"WRITING FILE: {k}")
            outfile.write (joined_contents)

if __name__ == "__main__":
    file_from_sys_argv = get_aFile()
    lines = get_lines(file_from_sys_argv)
    # test_re_matching(lines)
    noweb_blocks, tangle_files = accumulate_lines(lines)
    tangle_all(noweb_blocks, tangle_files)

def get_current_file_tangles():
    tanglesfile = "tangles.json"
    tanglespath = str(Path.home()) + '/.tangledown/' + tanglesfile
    tangles = None
    with open(tanglespath) as k:
        tangles = json.load(k)
    return tangles

def get_current_file_nowebs():
    nowebsfile = 'nowebs.json'
    nowebspath = str(Path.home()) + '/.tangledown/' + nowebsfile
    nowebs = None
    with open(nowebspath) as n:
        nowebs = json.load(n)
    return nowebs

