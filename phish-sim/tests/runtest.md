# Phishing Simulation Tool - Test Guide

Follow the steps below to run the unit tests for each part of the phishing simulation tool.

### 1. Navigate to the Project Directory

Open your terminal and go to the project root directory where the test files are located:

```bash

cd  phishing-simulation-tool

````

---

2.  Running  Unit  Tests  for  Individual  Files

If  you  want  to  run  tests  for  specific  files,  use  the  following  commands  based  on  the  test  file  name.

### a. Running Tests for Website Spoofer (`test_websitespoofer.py`)

Use  the  command:

```bash

use the command: python -m unittest tests/test_websitespoofer.py

```

This will execute all tests in the `test_websitespoofer.py` file.

#### b. Running Tests for Phishing Email (`test_phishing_email.py`)

Use the command:

```bash

use  the  command:  python  -m  unittest  tests/test_phishing_email.py

```

This will execute all tests in the `test_phishing_email.py` file.

#### c. Running Tests for Website Copier (`test_websitecopier.py`)

Use the command:

```bash

use  the  command:  python  -m  unittest  tests/test_websitecopier.py

```

This will execute all tests in the `test_websitecopier.py` file.

#### d. Running Tests for Tracking Server (`test_tracking_server.py`)

Use the command:

```bash

use  the  command:  python  -m  unittest  tests/test_tracking_server.py

```

This will execute all tests in the `test_tracking_server.py` file.

---

### 3. Running All Tests at Once

If you want to run all the tests for the project at once, you can use the following command. This will discover and run all the test files that start with `test_` in the `/tests` directory.

```bash

use  the  command:  python  -m  unittest  discover  tests/

```

---

## Test Results

Once you run the tests, you'll see an output indicating whether each test passed or failed. For example:

```bash

....

----------------------------------------------------------------------

Ran  4  tests  in  0.003s

OK

```

If there are any failures, the output will display error details to help you troubleshoot and fix the issues.

---

## Conclusion

Running these tests will help you ensure that each part of the phishing simulation tool is working as expected. Make sure to regularly run the tests during development to catch any potential issues early.
