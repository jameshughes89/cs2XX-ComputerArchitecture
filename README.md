# cs2XX-ComputerArchitecture

CS 2XX: Computer Architecture

Your typical computer architecture course starting with transistors and ending with assembly language.

The course can be found [here](http://modsurski.com/csci263).

This course makes use of [Digital](https://github.com/hneemann/Digital) to create circuits. 



# Setup

## Windows

Have administrative privileges and run from cmd

```sh
python -m venv --clear --prompt cs263 venv
venv\Scripts\activate.bat
pip install .
```


## Bash

```sh
python3.11 -m venv --clear --prompt cs263 venv
. venv/bin/activate
pip install .
```



# Unit Tests

Assuming Java and [Digital](https://github.com/hneemann/Digital) are available.

```sh
java -cp Digital.jar CLI test ./path_to_schematics/schematic_with_tests.dig
```



# Build

```sh
sphinx-build -b html "$SOURCEDIR" "$OUTPUTDIR"
```

# Contribute

Check out the [CONTRIBUTING](CONTRIBUTING.md) guidelines.
