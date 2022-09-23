 #endraw -->
ython
ck name="types"></block>
ck name="openers"></block>
ck name="oh-no-there-are-two-ways"></block>
ck name="accumulate-contents"></block>
ck name="accumulate-lines"></block>
ck name="thereIsABlockTag"></block>
ck name="eatBlockTag"></block>
ck name="expandBlocks"></block>
ck name="expand-tangles"></block>
tangle_all(nowebs: Nowebs, tangles: Tangles) -> None:
for filename, liness in tangles.items ():
    Path(filename).parents[0].mkdir(parents=True, exist_ok=True)
    contents: str = expand_tangles(liness, nowebs)
    with open (filename, 'w') as outfile:
        print(f"WRITING FILE: {filename}")
        outfile.write (contents)
_name__ == "__main__":
fn, lines = get_lines(get_aFile())
# test_re_matching(lines)
nowebs, tangles = accumulate_lines(fn, lines)
tangle_all(nowebs, tangles)
 #raw -->
