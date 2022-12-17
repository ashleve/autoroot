import os
import sys
from pathlib import Path

from pyrootutils import setup_root

# this line finds the absolute path of the original python script that is being run
startfile = os.path.abspath(sys.argv[0])

# if we are in notebook or pytest, just use current working directory
if startfile.endswith("ipykernel_launcher.py") or startfile.endswith("pytest"):
    startfile = os.getcwd()

# convert to Path object
startfile = Path(startfile)

# this line recursively searches for ".project-root" file
# starting from folder containing the entry python script and going up until it finds it
root = setup_root(
    search_from=startfile,
    indicator=".project-root",
    project_root_env_var=True,
    dotenv=True,
    pythonpath=True,
    cwd=False,
)
