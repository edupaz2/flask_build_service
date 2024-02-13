# flask_build_service

## Overview

Minimal Flask application to create a web service that allows the user to submit the URL of a git repository containing a simple C++ project with a CMakeLists.txt. The web service will use this URL to get the source code, compile the code in the repository and return to the user a zip folder with the result of the build.

For the sake of simplicity, several assumptions are made:
- The repository can contain any convention about the build-system, and it could be as straightforward as possible to build it, for example just doing some standard simple cmake calls.
- Only fetching the head of the default branch of the repo.
- It is assumed that the server already contain the necessary tools, compilers, build systems, git, etc installed.
- It can be tested with any http client, like curl, a browser, etc.

## Installation Instructions

### Easy way

Run the server:
```sh
$ ./run.sh
```

Execute the tests:
```sh
$ ./run_tests.sh
```


### Installation

Create a new virtual environment:

```sh
$ python3 -m venv venv
```

Activate the virtual environment:

```sh
$ source venv/bin/activate
```

Install the python packages specified in requirements.txt:

```sh
(venv) $ pip install -r requirements.txt
```

### Running the Flask Application

Run development server to serve the Flask application:

```sh
(venv) $ flask --app app --debug run
```

### How to test

It can be tested with any http client, like curl, a browser, etc.

Example with the test repository: https://github.com/edupaz2/cmake_example_project.git

```sh
(venv) $ curl -L http://127.0.0.1:5000/build_repo/https://github.com/edupaz2/cmake_example_project.git --output data.zip
```
or

Navigate to 'http://127.0.0.1:5000/https://github.com/edupaz2/cmake_example_project.git' in your favorite web browser to view the website!

## Testing

To run all the tests:

```sh
(venv) $ python -m pytest -v
```

To check the code coverage of the tests:

```sh
(venv) $ python -m pytest --cov-report term-missing --cov=project
```
