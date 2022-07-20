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


def assert_success(args):
    """Runs it twice to show stdout, stderr clearly.
    """
    subprocess.run(args)
    assert "success" in str(subprocess.run(args, capture_output=True).stdout)


def assert_failure(args):
    """Runs it twice to show stdout, stderr clearly.
    """
    subprocess.run(args)
    assert not "success" in str(subprocess.run(args, capture_output=True).stdout)


def run_example_a():
    print("\n\nExample A does not use the source layout. `poetry run` just works.")
    os.chdir(start_dir / "example_a")
    assert_success(["poetry", "run", "example_a"])


def run_example_b():
    print(
        '\n\nExample B uses the source layout with script: example_b = "example_b:main".'
    )
    os.chdir(start_dir)
    uninstall("example_b")
    os.chdir(start_dir / "example_b")
    print("\n`poetry run` does not work")
    assert_failure(["poetry", "run", "example_b"])
    subprocess.run(["poetry", "install"])
    print("\nIt will work after you run `poetry install`")
    assert_success(["poetry", "run", "example_b"])
    print(
        "\nSince it's installed, it can also be run in other directories and directly"
    )
    os.chdir(start_dir)
    assert_success(["example_b.cmd"])
    uninstall("example_b")


def run_example_c():
    print(
        '\n\nExample C uses the source layout with script: example_c = "src.example_c:main"'
    )
    os.chdir(start_dir)
    uninstall("example_c")
    os.chdir(start_dir / "example_c")
    print(
        "\n`poetry run` works but maybe it shouldn't. It's a pitfall to think it's right and distribute an incorrect whl."
    )
    assert_success(["poetry", "run", "example_c"])
    subprocess.run(["poetry", "install"])
    print("\nRunning `poetry install` and then calling it directly fails.")
    os.chdir(start_dir)
    assert_failure(["example_c.cmd"])
    os.chdir(start_dir)
    uninstall("example_c")


def uninstall(example):
    subprocess.run(
        ["pip", "uninstall", "-y", example], capture_output=True, check=False
    )


if __name__ == "__main__":
    main()
