# Your First Function - Hello World

Students write a function named say_hello that returns the string "hello world", then use it to print the greeting a chosen number of times.

Exported from the authoring form, version 1.0.0. Graded on: correctness.

| File | Who sees it | What it is |
|---|---|---|
| `assignment.yaml` | The IDE | Metadata and the list of files |
| `student/instructions.md` | Students | The assignment, in full |
| `student/starting.py` | Students | The code students start from |
| `student/spec.md` | Students | What the tests expect, stated exactly |
| `student/tests-visible.py` | Students | The visible tests students run while they work |
| `instructor/solution.py` | Instructors only | The reference solution |
| `instructor/tests-hidden.py` | Instructors only | The hidden tests, held back from students |
| `instructor/definition.yaml` | Instructors only | The full source, used to update the assignment |

Keep this folder in a **private** repository. Only the `student/` folder goes to students.

## Run the tests

```
cd student && python tests-visible.py        # a student's code against the visible tests
cd instructor && python tests-hidden.py      # the solution against the hidden tests
```

Add `--json` for results a program can read. Set `TARGET` to test a different file.

## Update this assignment

Open the authoring form, choose **Import YAML**, open `instructor/definition.yaml`, make your changes, and export again with a new version number. Every generated file is rebuilt each time, so changes made to them by hand are lost.
