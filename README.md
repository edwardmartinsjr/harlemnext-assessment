# Harlem Next Assessment

[![CircleCI](https://circleci.com/gh/edwardmartinsjr/harlemnext-assessment/tree/master.svg?style=shield)](https://circleci.com/gh/edwardmartinsjr/harlemnext-assessment/tree/master)

1. This program is a single .py file.

2. This program is written in python 3.7, using only python’s built-in libraries.

3. This program contains a main() method that:

4. This program checks whether or not the password that is entered by the user (via console input) is acceptable or not.  Password acceptance is determined by the following rules:

    a. At least 1 letter between [a-z]
    b. At least 1 numbr between [0-9]
    c. At least 1 letter between [A-Z]
    d. At least 1 special character within [$%#]
    e. At least 6 characters long but not more than 12 characters

If password is accepted print to screen “Accepted” else “Not Accepted”

5. Test:
```
python test_main.py -v
```

6. Run:
```
python main.py -p s0m3#N1c3%P4$$w0rD
```
