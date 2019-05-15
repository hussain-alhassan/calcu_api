# Calcu API

Calcu API is a calculator performing some operations using Web API and CLI (Command Line Interface). Also, it shows you reports about the times each operation has been used on daily, weekly, and monthly basis.

## Technologies used:
  - Flask (Python Web framework)
  - SQLAlchemy (Database Toolkit for Python)
  - Click (Python package to create command line interfaces)
  - unittest (Python unit testing framework)
### Instalation (Note: Python 3 is required)
1- Open a terminal window and clone the project by running this command.
```sh
git clone git@github.com:hussain-alhassan/calcu_api.git
```
2- Navigate to the project root directory.
```sh
cd calcu_api
```
3- Install the dependencies.
```sh
python3 -m pip install -r requirements.txt
```
4- Run the server to test the project on the browser
```sh
python3 run.py
```
5- Click this link http://localhost:5000 (your url might be slighly different)
  - The project has a web page for you to test the Web API and see the response in JSON Format.
  - Plus, it has Report section to show you how many times each operator has been used.


### CLI Usage
1- Navigate to the sub directory 'calcu_api'. Make sure you are in the direcory that has cli_calcu.py file
```sh
cd calcu_api
```
2- We need to pass the function name (required), the first number (required), and the second number (if needed).
The functions we have:
- add
- substract
- multiply
- divide
- square_root
- cube_root
- power
- factorial
So, an example to use the add function, run this command
```sh
python3 cli_calcu.py -function add -first 4 -second 5
```
An example to use square_root function
```sh
python3 cli_calcu.py -function square_root -first 16
```
You should get the API response in the terminal window


## Running the automated tests
1- Navigate to the tests directory (it is in the project root directory)
2- Run this command:
```sh
python3 -m unittest tests/test_calculation.py
```

Written by Hussain Alhassan. Feel free to use it.