# DACSspace

A Python package to evaluate your ArchivesSpace instance for DACS [single-level required](https://saa-ts-dacs.github.io/dacs/06_part_I/02_chapter_01.html#single-level-required) elements.

DACSspace utilizes the ArchivesSpace API and a default JSON schema to validate resources. The output is a CSV containing a list of invalid URIs with the following fields: validation status, error count, and explanation.

DACSspace also allows users to specify a schema to validate against other than the default DACS single-level required schema, see [Usage](https://github.com/RockefellerArchiveCenter/DACSspace#usage) section for more information.

## Requirements

*   Python 3 (tested on Python 3.10)
*   [ArchivesSnake](https://github.com/archivesspace-labs/ArchivesSnake) (Python library) (0.9.1 or higher)
*   Requests module
*   JSONschema

## Installation

Download and install [Python](https://www.python.org/downloads/)

* If you are using Windows, add Python to your [PATH variable](https://docs.python.org/2/using/windows.html)

Install DACSspace and its requirements: ```pip install dacsspace```

## Setup

Create a file to hold your ArchivesSpace credentials. This file should contain:
* The base URL of your ArchivesSpace instance
* A Repository ID for your ArchivesSpace installation
* An ArchivesSpace username and associated password

The easiest way to do this is to rename `as_config.example` to `as_config.cfg`
and update it with your values.

By default, DACSspace expects this file to be named `as_config.cfg`, but you can
pass a different filepath via the `as_config` command-line argument.  


## Usage

Using the command line navigate to the directory containing the DACSspace repository and run `single-level.py` to execute the script.

DACSspace will prompt you to answer two questions allowing you to limit which resources you'd like the script to evaluate:

```
Welcome to DACSspace!
I'll ask you a series of questions to refine how to script works.
If you want to use the default value for a question press the ENTER key.

Do you want DACSspace to include unpublished resources? y/n (default is n):
Do you want to further limit the script by a specific resource id? If so, enter a string that must be present in the resource id (enter to skip):
```

Pressing the ENTER key for both questions will use the default version of the script which will get ALL resources.

The script will create a list of evaluated resources in a csv file (default is `dacs_singlelevel_report.csv`).

A sample csv file will look like this:

| title | publish | resource | extent | date| language | repository | creator | scope | restrictions
|---|---|---|---|---|---|---|---|---|---|
| #resource title | TRUE | #resourceId | 20.8 | inclusive|  eng   | #NameofRepository | FALSE | #scopenote| #accessrestriction
| #resource title | TRUE | #resourceId | 50.6 | single   |  FALSE | #NameofRepository | #creator | FALSE| FALSE

If you are using Microsoft Excel to view the csv file, consult the following links to avoid encoding issues: [Excel 2007](https://www.itg.ias.edu/content/how-import-csv-file-uses-utf-8-character-encoding-0), [Excel 2013](https://www.itg.ias.edu/node/985).

## Contributing

Found a bug? [File an issue.](https://github.com/RockefellerArchiveCenter/DACSspace/issues/new/choose)

Pull requests accepted! To contribute:

1. File an issue in the repository or work on an issue already documented
2. Fork the repository and create a new branch for your work
3. After you have completed your work, push your branch back to the repository and open a pull request

### Contribution standards

#### Style

DACSspace uses the Python PEP8 community style guidelines. To conform to these guidelines, the following linters are part of the pre-commit:

* autopep8 formats the code automatically
* flake8 checks for style problems as well as errors and complexity
* isort sorts imports alphabetically, and automatically separated into sections and by type

After locally installing pre-commit, install the git-hook scripts in the DACSSpace directory:

    ```
    pre-commit install
    ```  

#### Documentation

Docstrings should explain what a module, class, or function does by explaining its syntax and the semantics of its components. They focus on specific elements of the code, and less on how the code works. The point of docstrings is to provide information about the code you have written; what it does, any exceptions it raises, what it returns, relevant details about the parameters, and any assumptions which might not be obvious. Docstrings should describe a small segment of code and not the way the code is implemented in a larger environment.

DACSspace adheres to [Google’s docstring style guide](https://google.github.io/styleguide/pyguide.html#381-docstrings). There are two types of docstrings: one-liners and multi-line docstrings. A one-line docstring may be perfectly appropriate for obvious cases where the code is immediately self-explanatory. Use multiline docstrings for all other cases.

#### Tests

New code should  have unit tests. Tests are written in unittest style and run using [tox](https://tox.readthedocs.io/). 

## Authors

Initial version: Hillel Arnold and Amy Berish.

Version 2.0: Hillel Arnold, Amy Berish, Bonnie Gordon, Katie Martin, and Darren Young.

## License

This code is released under the MIT license. See `LICENSE` for further details.
