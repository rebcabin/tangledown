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

def get_lines(aFilename):
    """Get lines from a file denoted by aFilename."""
    with open(aFilename) as aFile:
        return aFile.readlines ()

noweb_start_re = re.compile (r'^<noweb name="([a-zA-Z][\w\s\-_\.]+)">$')
noweb_end_re = re.compile (r'^</noweb>$')

tangle_start_re = re.compile (r'^<tangle file="([a-zA-Z][\w\s\-_\.]+)">$')
tangle_end_re = re.compile (r'^</tangle>$')

block_start_re = re.compile (r'.*<block name="([a-zA-Z][\w\s\-_\.]+)">')
block_end_re = re.compile (r'.*</bl[o]ck>')


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

def there_is_a_block_tag (lines):
    for line in lines:
        block_start_match = block_start_re.match (line)
        if (block_start_match):
            return True
    return False

def eat_block_tag (i, lines):
    for j in range (i, len(lines)):
        end_match = block_end_re.match (lines[j])
        if (end_match):
            return j + 1
        else:  # DUDE!
            pass

def expand_blocks (noweb_blocks, lines):
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

