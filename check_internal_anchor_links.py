from typing import List, Dict, Set
import re, sys
from pprint import pprint

filename = "literate-copperhead-003.md"

anchor_re = r'.*<a id="(.*)">'
ref_re = r'\[(.*?)\]\(#(.*?)\)'


def find_anchors(filename: str) -> Set[str]:
    anchor_list = []
    with open(filename) as f:
        lines = f.readlines()
        index: int = 0
        for line_no, line in enumerate(lines):
            mm: List = re.findall(anchor_re, line)
            if mm:
                index += len(mm)
                for m in mm:
                    anchor_list.append(m)
    anchor_set = set(anchor_list)
    listlen = len(anchor_list)
    dupes_exist = (not (listlen == len(anchor_set)))
    print(f'THERE ARE '
          f'{"NO" if not dupes_exist else ""}'
          f' DUPLICATES AMONGST {listlen} ANCHORS')
    if dupes_exist:
        dupes_list = []
        dupes = set()
        for a in anchor_list:
            if a in dupes:
                dupes_list.append(a)
            else:
                dupes.add(a)
        print(f'THE DUPES ARE:')
        pprint(dupes_list)
    return anchor_set


def match_refs(filename: str, anchors: Set):
    with open(filename) as f:
        lines = f.readlines()
        index = 0; matchcount = 0; failcount = 0
        for line_no, line in enumerate(lines):
            mm: list = re.findall(ref_re, line)
            if mm:
                index += len(mm)
                for m in mm:
                    ref = m[1]
                    if ref in anchors:
                        matchcount += 1
                    else:
                        failcount += 1
                        print(f'FAILED TO FIND MATCHING ANCHOR: '
                              f'index: {index}, line_no: {line_no + 1}, ref: {ref} '
                              f'matchcount: {matchcount}, failcount: {failcount}.')
        if index == matchcount:
            print(f'SUCCESS IN FINDING ALL MATCHING ANCHORS: ')
            print(f'number of refs: {index}, matchcount: {matchcount}.')
        else:
            print(f'FAILED TO FIND {failcount} ANCHORS WITH '
                  f'{index} TRIALS AND {matchcount} SUCCESSES.')


if __name__ == "__main__":
    filename = sys.argv[1]
    match_refs(filename, find_anchors(filename))
