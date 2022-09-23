from tangledown import get_lines, accumulate_lines, tangle_all

tangle_all(*accumulate_lines(*get_lines("hello_world.md")))
