# UNITTEST
[<..](https://github.com/TheeKingZa/AirBnB_clone/blob/master/README.md) 
---
## Python Unit Tests:
  * Allowed editors: vi, vim, emacs
  * All your files should end with a new line
  * All your test files should be inside a folder tests
  * You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
  * All your test files should be python files (extension: .py)
  * All your test files and folders should start by [test_](#unittests)
  * Your file organization in the tests folder should be the same as your project
  * e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
  * e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
  * All your tests should be executed by using this command: python3 -m unittest discover tests
  * You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
  * All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
  * All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
  * All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
  * We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Unittests

All your files, classes, functions must be tested with unit tests
---
    guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
    ...................................................................................
    ...................................................................................
    .......................
    ----------------------------------------------------------------------
    Ran 189 tests in 13.135s

    OK
    guillaume@ubuntu:~/AirBnB$

---
Note that this is just an example, the number of tests you create can be different from the above example.

**Warning**:

Unit tests must also pass in non-interactive mode:
---
    guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
    ...................................................................................
    ...................................................................................
    .......................
    ----------------------------------------------------------------------
    Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$
