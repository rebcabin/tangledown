import re
aFile = open ('tangledown.md')
lines = aFile.readlines ()
aFile.close ()
noweb_start_re = re.compile (r'^<noweb name="([a-zA-Z][\w\s\-_\.]+)">$')
noweb_end_re = re.compile (r'^</noweb>$')

tangle_start_re = re.compile (r'^<tangle file="([a-zA-Z][\w\s\-_\.]+)">$')
tangle_end_re = re.compile (r'^</tangle>$')

block_start_re = re.compile (r'.*<block name="([a-zA-Z][\w\s\-_\.]+)">')
block_end_re = re.compile (r'.*</bl[o]ck>')


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
noweb_blocks = {}
tangle_files = {}

triple_backtick_re = re.compile (r'^`[`]`')
blank_line_re      = re.compile (r'^\s*$')

def first_non_blank_line_is_triple_backtick (i, lines):
    while (blank_line_re.match (lines[i])):
        i = i + 1
    return triple_backtick_re.match (lines[i])

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
    
for i in range (len (lines)):
    noweb_start_match = noweb_start_re.match (lines[i])
    tangle_start_match = tangle_start_re.match (lines[i])
    if (noweb_start_match):
        block_key = noweb_start_match.group (1)
        i, noweb_blocks[block_key] = accumulate (i + 1, noweb_end_re)
    elif (tangle_start_match):
        file_key = tangle_start_match.group (1)
        i, tangle_files[file_key] = accumulate (i + 1, tangle_end_re)
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
        else: # DUDE!
            pass

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



for k, v in tangle_files.iteritems ():
    outfile = open (k, 'w')
    lines = v
    while there_is_a_block_tag (lines):
        lines = expand_blocks (lines)
    for line in lines:
        outfile.write (line)
    outfile.close ()

