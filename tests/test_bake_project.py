from contextlib import contextmanager

import os
import subprocess


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def test_project_tree(cookies):
    result = cookies.bake(extra_context={"project_slug": "test_project"})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "test_project"

    top_level_files = [
        "config",
        "data",
        "log",
        "models",
        "notebooks",
        "submit",
        "Makefile",
        "setup.py",
        "requirements.in",
        "requirements.txt",
    ]

    found_toplevel_files = [f.basename for f in result.project.listdir()]
    for file_name in top_level_files:
        assert file_name in found_toplevel_files


def test_run_flake8(cookies):
    result = cookies.bake(extra_context={"project_slug": "flake8_compat"})
    with inside_dir(str(result.project)):
        subprocess.check_call(["flake8"])
