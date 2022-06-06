# DACSspace

A Python package to evaluate your ArchivesSpace instance for DACS [single-level required](https://saa-ts-dacs.github.io/dacs/06_part_I/02_chapter_01.html#single-level-required) elements.

DACSspace utilizes the ArchivesSpace API and a default JSON schema to validate resources. The output is a CSV containing a list of invalid URIs with the following fields: validation status, error count, and explanation.

DACSspace also allows users to specify a schema to validate against other than the default DACS single-level required schema. Refer to [What Schema to Validate Your Data Against](https://github.com/RockefellerArchiveCenter/DACSspace#what-schema-to-validate-your-data-against) for more information.

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

DACSspace can be used as a command line utility to evaluate your ArchivesSpace repository for DACS compliance, and it can also be used as part of another Python program.

Required arguments:
- `csv_filepath`

Use this argument to set the filepath to the CSV file where the output of DACSspace will print. Your CSV filepath must have a .csv extension and cannot contain the following characters: * ? : " < > | '

Optional arguments:
- `--published_only`
- `--invalid_only`
- `--schema_identifier`
- `--schema_filepath`

For use cases on how these optional arguments can be employed, look under the next section, Running DACSspace from the command line.

### Running DACSspace from the command line

In the command line, run `dacsspace`. You also need to pass in the `csv_filepath` argument with the name of your CSV filepath in order to run the script (see [above]((https://github.com/RockefellerArchiveCenter/DACSspace#usage))).

You can use the different DACSspace optional arguments to decide what data DACSspace will fetch, what data it will report out on, and what schema it will validate the data against.

#### What data to fetch

If you plan to only evaluate DACS compliance on resources in your ArchivesSpace repository that are published, pass in the argument `--published_only` into the command line. This tells the DACSspace client class to only fetch data from published resources.

#### What data to report on

If you want to limit your CSV file to contain information on resources that do not meet DACS compliance, pass in the argument `--invalid_only` into the command line. This tells the DACSspace reporter class to only write information on invalid results of the validation to your CSV file.

The output to your CSV will include the following field names:
- uri: The ArchivesSpace object's unique identifier (ex. /repositories/2/resources/1234)
- valid: A boolean indication of the validation result (True or False)
- error_count: An integer representation of the number of validation errors (ex. 1)
- explanation: An explanation of any validation errors (You are missing the following fields ...)

If you are using Microsoft Excel to view the CSV file, consult the following links to avoid encoding issues: [Excel 2007](https://www.itg.ias.edu/content/how-import-csv-file-uses-utf-8-character-encoding-0), [Excel 2013](https://www.ias.edu/itg/how-import-csv-file-uses-utf-8-character-encoding).

#### What schema to validate your data against

The default JSON schema that DACSspace will run the data it fetches from your ArchivesSpace repository against is the single_level_required JSON schema. If you want to validate your data against a different schema, you have two options:

1. To run DACSspace against a schema other than single_level_required within the `schemas` directory in dacsspace, use the command line argument `--schema_identifier` and specify the identifier for that schema. The identifier must be entered in as a string.
2. To run DACSspace against a schema that is external to dacsspace, use the command line argument `schema_filepath` and specify the filepath to this external schema. The filepath must be entered in as a string.

### Using DACSspace in another Python program

Different components of the DACSspace package can be incorporated into other Python programs.

For example, say you had a set of data that has already been exported from ArchivesSpace into another sort of container. You do not need to run the entire DACSspace package, but you do want to validate your data set against a JSON schema. To do this, add this code to your script:

```
from dacsspace.validator import Validator

exported_data = [{"title": "Archival object" ... }, { ...}]
validator = Validator("single_level_required.json", None)
results = [validator.validate_data(obj) for obj in exported_data]
print(results)
```

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

After locally installing pre-commit, install the git-hook scripts in the DACSSpace directory: ```pre-commit install```  

#### Documentation

Docstrings should explain what a module, class, or function does by explaining its syntax and the semantics of its components. They focus on specific elements of the code, and less on how the code works. The point of docstrings is to provide information about the code you have written; what it does, any exceptions it raises, what it returns, relevant details about the parameters, and any assumptions which might not be obvious. Docstrings should describe a small segment of code and not the way the code is implemented in a larger environment.

DACSspace adheres to [Google’s docstring style guide](https://google.github.io/styleguide/pyguide.html#381-docstrings). There are two types of docstrings: one-liners and multi-line docstrings. A one-line docstring may be perfectly appropriate for obvious cases where the code is immediately self-explanatory. Use multiline docstrings for all other cases.

#### Tests

New code should  have unit tests. Tests are written in unittest style and run using [tox](https://tox.readthedocs.io/). 

## Authors

Initial version: Hillel Arnold and Amy Berish.

Version 1.0: Hillel Arnold, Amy Berish, Bonnie Gordon, Katie Martin, and Darren Young.

## License

This code is released under the MIT license. See `LICENSE` for further details.
