r"""Your First Function - Hello World: hidden tests

GENERATED FILE. Do not edit it by hand. Change the assignment in the authoring form and export again.
INSTRUCTORS ONLY. Never give this file to students.

Check the reference solution (solution.py, in this folder):
    python tests-hidden.py

Check a student's file:
    TARGET=/path/to/their/file.py python tests-hidden.py

Results as JSON, for graders and for the IDE:
    python tests-hidden.py --json
"""

import ast
import contextlib
import importlib.util
import io
import json
import math
import os
import re
import runpy
import signal
import sys
import threading
import unittest

sys.dont_write_bytecode = True  # keep __pycache__ folders out of the repository
HERE = os.path.dirname(os.path.abspath(__file__))

KIND = "hidden"
HIDDEN = True
MODE = "stdin_stdout"
FUNCTION = None
DEFAULT_TARGET = "solution.py"
CASES = []

TARGET = os.environ.get("TARGET", DEFAULT_TARGET)
TIME_LIMIT = int(os.environ.get("TEST_TIME_LIMIT", "5"))


class _Timeout(Exception):
    pass


@contextlib.contextmanager
def _time_limit(seconds):
    """Stop code that runs too long. This works where SIGALRM exists (Linux and macOS)."""
    can_alarm = hasattr(signal, "SIGALRM") and threading.current_thread() is threading.main_thread()
    if not can_alarm:
        yield
        return

    def _raise(signum, frame):
        raise _Timeout()

    previous = signal.signal(signal.SIGALRM, _raise)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


def _target_path():
    name = TARGET if TARGET.endswith(".py") else TARGET + ".py"
    return os.path.normpath(name if os.path.isabs(name) else os.path.join(HERE, name))


def _one_line(text):
    return " ".join(str(text).split())


def _same(actual, expected):
    """Compare values. Floats match to 9 decimal places, and dictionary order does not matter."""
    if isinstance(expected, bool) or isinstance(actual, bool):
        return type(actual) is type(expected) and actual == expected
    if isinstance(expected, float) or isinstance(actual, float):
        try:
            return math.isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-9)
        except TypeError:
            return False
    if isinstance(expected, dict):
        return (isinstance(actual, dict) and set(actual) == set(expected)
                and all(_same(actual[key], expected[key]) for key in expected))
    if isinstance(expected, (list, tuple)):
        return (isinstance(actual, (list, tuple)) and len(actual) == len(expected)
                and all(_same(a, b) for a, b in zip(actual, expected)))
    return actual == expected


def _check(case):
    """Return None when the case passes, or a one-line message when it fails."""
    path = _target_path()
    if not os.path.exists(path):
        return "Could not find %s next to this test file." % os.path.basename(path)
    typed = case["input"]
    if not typed.endswith("\n"):
        typed += "\n"
    stdout = io.StringIO()
    saved = (sys.stdin, sys.stdout, sys.argv)
    sys.stdin, sys.stdout, sys.argv = io.StringIO(typed), stdout, [path]
    sys.path.insert(0, os.path.dirname(path))
    problem = None
    try:
        with _time_limit(TIME_LIMIT):
            runpy.run_path(path, run_name="__main__")
    except _Timeout:
        problem = "Your program ran for more than %d seconds. Is there an infinite loop?" % TIME_LIMIT
    except EOFError:
        problem = "Your program asked for more input than this test provides."
    except SystemExit:
        pass
    except Exception as error:
        if HIDDEN:
            problem = "Your program raised an error (%s)." % type(error).__name__
        else:
            problem = "Your program raised %s: %s" % (type(error).__name__, _one_line(error))
    finally:
        sys.path.pop(0)
        sys.stdin, sys.stdout, sys.argv = saved
    if problem:
        return problem
    output = stdout.getvalue().replace("\r\n", "\n").rstrip()
    expected = case["expected"].strip()
    if output.endswith(expected):
        return None
    if HIDDEN:
        return "Your program printed something different."
    tail = output[-(len(expected) + 30):]
    return "Expected the output to end with %r but it ended with %r" % (expected, tail)


def _slug(text):
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")[:40]


class Tests(unittest.TestCase):
    """One test method per case, so IDE test explorers can list and run them."""


CASE_FOR = {}


def _add(number, case):
    label = ("hidden_%02d" % number) if HIDDEN else ("%02d_%s" % (number, _slug(case["name"])))

    def test(self):
        message = _check(case)
        if message:
            self.fail(message)

    test.__doc__ = case["name"]
    setattr(Tests, "test_" + label, test)
    CASE_FOR["test_" + label] = (number, case)


for _number, _case in enumerate(CASES, 1):
    _add(_number, _case)


def run_all():
    rows = []
    for test in unittest.defaultTestLoader.loadTestsFromTestCase(Tests):
        number, case = CASE_FOR[test._testMethodName]
        result = unittest.TestResult()
        test.run(result)
        problems = result.failures + result.errors
        message = ""
        if problems:
            message = problems[0][1].strip().splitlines()[-1]
            if message.startswith("AssertionError: "):
                message = message[len("AssertionError: "):]
        rows.append({
            "number": number,
            "name": case["name"],
            "passed": not problems,
            "points": case["points"],
            "earned": 0 if problems else case["points"],
            "message": message,
        })
    return rows


def main():
    rows = run_all()
    earned = sum(row["earned"] for row in rows)
    total = sum(row["points"] for row in rows)
    if "--json" in sys.argv:
        print(json.dumps({"kind": KIND, "target": os.path.basename(_target_path()),
                          "earned": earned, "total": total, "tests": rows}, indent=2))
    else:
        for row in rows:
            label = ("Hidden test %d" % row["number"]) if HIDDEN else row["name"]
            print("%s  %s  (%s/%s)" % ("PASS" if row["passed"] else "FAIL", label, row["earned"], row["points"]))
            if not row["passed"] and row["message"]:
                print("      " + row["message"])
        print("Score: %s/%s" % (earned, total))
    return 0 if all(row["passed"] for row in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
