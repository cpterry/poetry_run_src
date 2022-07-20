# poetry_run_src

Run `run_examples.py` to see demonstrate issue https://github.com/python-poetry/poetry/issues/6029.

It will install and uninstall the examples so make sure you're in an environment where that's OK.

It has been tested on Windows 10 and that may matter. You may have to remove the `.cmd` extensions to get the same behaviour on a non-Windows OS. I haven't tested that.

The asserts confirm the behaviour on my system. So if `assert_failure` raises an exception that means it worked for you but not for me.
