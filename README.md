# Console Shell
Python programming course lab #3.
## Description
Interactive shell build with **typer** that can calculate n-th fibonacci number, factoral of n or sort an array with classical sorting algorithms.
___
### Libraries:
- typer
____
### Algorithm
1. User enters the command
2. Command is parsed and checked for correctness by typer
3. The result is calculated using the choosed algorithm
4. The result is returned to the user
5. Back to step 1
___

### Available commands: 
To check available commands run:
```
help
```
## How to set up?
1. Clone the repo:
```
git clone https://github.com/leanleanlean96/ConsoleApp
```
2. Install poetry if you dont have it installed:
```
pipx install poetry
```
3. Install dependescies
```
poetry install
```
4. Run the program:
```
poetry run python3 -m src.sortslab.main
```
5. To check command usage rules, type:
 ```
  help
 ```

### Tests
```
poetry run pytest ./tests/tests.py
```

## Architecture
```
AlgoPack/
├── src/sortslab/
│   ├── sorts/
│   │   ├── __init__.py
│   │   ├── bubble_sort.py
│   │   ├── bucket_sort.py
│   │   ├── counting_sort.py
│   │   ├── heap_sort.py
│   │   ├── insertion_sort.py
│   │   ├── quick_sort.py
│   │   ├── radix_sort.py
│   │   └── selection_sort.py
│   ├── common/
│   │   ├── __init__.py
│   │   └── check_types.py
│   ├── structures/
│   │   ├── __init__.py
│   │   └── stack.py
│   ├── math_functions/
│   │   ├── __init__.py
│   │   ├── factorial.py
│   │   └── fibonacci.py
│   ├── __init__.py
│   └── main.py
│		 
├── tests/
│   ├── __init__.py
│   └── test.py
├── poetry.lock
├── pyproject.toml
└── README.md
```


