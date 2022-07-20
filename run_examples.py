"""Run the examples to demonstrate https://github.com/python-poetry/poetry/issues/6029
"""

import os
import subprocess
from pathlib import Path

start_dir = Path(__file__).parent.absolute()


def main():
    print(
        "This runs the different examples including `poetry install` and `pip uninstall`."
    )
    print(
        "Direct calls to the installed example executables are run with a `.cmd` extension to handle Window specific behaviour."
    )
    run_example_a()
    run_example_b()
    run_example_c()
    print("\nFinished.")


def run_example_a():

    print("\n\nExample A does not use the source layout. `poetry run` just works.")
    os.chdir(start_dir / "example_a")
    subprocess.run(["poetry", "run", "example_a"])


def run_example_b():
    print(
        '\n\nExample B uses the source layout with script: example_b = "example_b:main".'
    )
    os.chdir(start_dir)
    uninstall("example_b")
    os.chdir(start_dir / "example_b")
    print("`poetry run` does not work")
    subprocess.run(["poetry", "run", "example_b"])
    subprocess.run(["poetry", "install"])
    print("It will work after you run `poetry install`")
    subprocess.run(["poetry", "run", "example_b"])
    print("Since it's installed, it can also be run in other directories and directly")
    os.chdir(start_dir)
    subprocess.run(["example_b.cmd"])
    uninstall("example_b")


def run_example_c():
    print(
        '\n\nExample C uses the source layout with script: example_c = "src.example_c:main"'
    )
    os.chdir(start_dir)
    uninstall("example_c")
    os.chdir(start_dir / "example_c")
    print(
        "`poetry run` works but maybe it shouldn't. It's a pitfall to think it's right and distribute an incorrect whl."
    )
    subprocess.run(["poetry", "run", "example_c"])
    subprocess.run(["poetry", "install"])
    print("Running `poetry install` and then calling it directly fails.")
    os.chdir(start_dir)
    subprocess.run(["example_c.cmd"])
    os.chdir(start_dir)
    uninstall("example_c")


def uninstall(example):
    subprocess.run(
        ["pip", "uninstall", "-y", example], capture_output=True, check=False
    )


if __name__ == "__main__":
    main()
