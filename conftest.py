"""Shared test helpers. You do not need to edit this file."""

import subprocess
import sys
from pathlib import Path

import pytest


@pytest.fixture
def run_script():
    """Run a Python script like you would in the terminal.

    Returns the text the script printed. `stdin` is what you would type.
    """

    def _run(path: Path, stdin: str = "") -> str:
        result = subprocess.run(
            [sys.executable, str(path)],
            input=stdin,
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode != 0:
            pytest.fail(
                f"Your script crashed. Error message:\n\n{result.stderr}"
            )
        return result.stdout

    return _run
