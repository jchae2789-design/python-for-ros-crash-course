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
        try:
            result = subprocess.run(
                [sys.executable, str(path)],
                input=stdin,
                capture_output=True,
                text=True,
                timeout=10,
            )
        except subprocess.TimeoutExpired:
            result = None
        if result is None:
            pytest.fail(
                "Your script did not finish within 10 seconds.\n"
                "Is there a loop that never ends, or an extra input()?",
                pytrace=False,
            )
        if result.returncode != 0:
            pytest.fail(
                f"Your script crashed. Error message:\n\n{result.stderr}",
                pytrace=False,
            )
        return result.stdout

    return _run
