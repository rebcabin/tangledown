# TANGLE HELLO_WORLD


A noweb tag named "hello world def" defining a function named "hello_world."


<noweb name="hello world def">

    def hello_world():
        print("Hello, world, from Tangledown!")

</noweb>


A tangle tag that refers to the noweb tag named "hello world def" and writes a python file, "hello_world.py." That python file can be called as a script from the python command line. It can also be imported as a module, and the importing code (example below) can call the function, "hello_world," which is defined in "hello world def."


<tangle file="hello_world.py">

    <block name="hello world def"></block>
    if __name__ == "__main__":
        hello_world()

</tangle>


Tangle the code out of this here Markdown file using tangledown as a module.

```python
from tangledown import get_lines, accumulate_lines, tangle_all
```

```python
tangle_all(*accumulate_lines(get_lines("hello_world.md")))
```

Call the "hello_world" function imported from the "hello_world" module.

```python
import hello_world
hello_world.hello_world()
```

Isn't that cool?


Well, hell, let's bootstrap tangledown itself from "README.md." This is how you bootstrap a compiler.

```python
tangle_all(*accumulate_lines(get_lines("README.md")))
```

Do it again to make sure it all worked!

```python
tangle_all(*accumulate_lines(get_lines("README.md")))
```

Hot Dayyum!

```python

```
