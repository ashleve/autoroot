# autoroot

Automatic project root setup with just one import!

You only need to create empty `.project-root` file in the chosen directory.

## Installation

```bash
pip install autoroot
pip install autorootcwd
```

## Usage

```python
# this adds root folder to pythonpath, sets PROJECT_ROOT var, and loads variables from `.env`
import autoroot 
```

Or:

```python
# this also changes working directory to root
import autorootcwd 
```

That's it! You're done. One import is enough.

## How it works

Adding the `import autoroot` to top of your python script will make a call to `pyrootutils.setup_root()`, which recursively searches for `.project-root` file in parent dirs to determine which folder is root.

See pyrootutils for more info: <br>
https://github.com/ashleve/pyrootutils

Works in notebooks too.
