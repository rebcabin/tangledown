from pathlib import Path
from typing import List
import uuid
from gitignore_parser import parse_gitignore
from pprint import pprint

def files_list(dir_name: str) -> List[str]:
    dir_path = Path(dir_name)
    files_result = []
    nyms_result = []
    nyms_collision_check = set()
    file_count = 0
    in_gitignore = lambda _: False
    def gsnym(p: Path) -> str:
        """Generate a short, unique name for a path."""
        nym = gsnym_candidate(p)
        while nym in nyms_collision_check:
            nym = gsnym_candidate(p)
        nyms_collision_check.add(nym)
        return nym
    def gsnym_candidate(p: Path) -> str:
        """Generate a candidate short, unique name for a path."""
        return p.stem[-9:] + '_' + uuid.uuid4().hex[:6].upper()
    def find_first_gitignore() -> Path:
        nonlocal in_gitignore
        p = dir_path
        for p in dir_path.rglob('*'):
            if p.name == '.gitignore':
                in_gitignore = parse_gitignore(str(p.absolute()))
                break;
        return p
    def recurse_a_dir(dir_path: Path) -> None:
        nonlocal file_count, nyms_result, files_result, in_gitignore
        for p in dir_path.glob('*'):
            q = p.absolute()
            qs = str(q)
            try:  # don't skip files in dirs above .gitignore
                ok = not in_gitignore(qs)
            except ValueError as e:
                ok = True
            if not ok:
                pprint(f'... IGNORING file or dir {p}')
            if ok and q.is_file():
                file_count += 1
                nyms_result.append(gsnym(q))
                files_result.append(qs)
            elif ok and p.is_dir:
                recurse_a_dir(p)
    find_first_gitignore()
    recurse_a_dir(dir_path)
    assert file_count == len(nyms_collision_check)
    return list(zip(files_result, nyms_result))

from typing import Tuple
from pprint import pprint
BEGIN_RAW = '<!-- #raw -->\n'
END_RAW = '<!-- #endraw -->\n'
BLANK_LINE = '\n'
def wrap_1_raw(lines: List[str], s: str) -> None:
    lines.append(BEGIN_RAW)
    lines.append(s)
    lines.append(END_RAW)
def wrap_n_blank(lines: List[str], ss: List[str]) -> None:
    lines.append(BLANK_LINE)
    for s in ss:
        lines.append(s)
    lines.append(BLANK_LINE)
def wrap_triple_backtick(lines: List[str], 
                         ss: List[str], 
                         language: str) -> None:
    lines.append(f'```{language}\n')
    for s in ss:
        lines.append(s)
    lines.append(f'```\n')
def indent_4(lines: List[str], ss: List[str]):
    for s in ss:
        lines.append('    ' + s)
def write_noweb_to_lines(lines: List[str], 
                         file_gsnym_pair: Tuple[str],
                         language: str) -> None:
    path = Path(file_gsnym_pair[0])
    wrap_n_blank(lines, [f'## {path.name}\n'])
    wrap_1_raw(lines, f'<noweb name="{file_gsnym_pair[1]}">\n')
    with open(file_gsnym_pair[0]) as f:
        inlines = f.readlines()
        pprint(f'DETANGLING file {path}')
    bound = []  ## Really want the monadic bind, here.
    if language == "markdown":
        indent_4(bound, inlines)
    else:
        wrap_triple_backtick(bound, inlines, language)
    wrap_n_blank(lines, bound)
    wrap_1_raw(lines, '</noweb>\n')
    lines.append(BLANK_LINE)

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
    with open(output_markdown_filename, "w") as f:
        for line in lines:
            f.write(line)
    pass

if __name__ == "__main__":
    tangleup_overwrite_markdown(
        "asr_tangleup_test.md",
        "./examples/asr",
        title="This is a Test of the Emergency Tangleup System")

