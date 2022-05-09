# DACSspace

A simple Python script to evaluate your ArchivesSpace instance for DACS [single-level minimum](http://www2.archivists.org/standards/DACS/part_I/chapter_1) required elements.

DACSspace utilizes the ArchivesSpace API to check resources for DACS compliance and produces a csv containing a list of evaluated resources. If a DACS field is present its content will be written to the csv, if a field is missing the csv will read "FALSE" for that item.

## Requirements

*   Python 3 (tested on Python 3.10)
*   [ArchivesSnake](https://github.com/archivesspace-labs/ArchivesSnake) (Python library) (0.9.1 or higher)
*   Requests module
*   JSONschema
*   [tox](https://tox.readthedocs.io/) (for running tests)
*   [pre-commit](https://pre-commit.com/) (for running linters before committing)
    *   After locally installing pre-commit, install the git-hook scripts in the DACSSpace directory:

    ```
    pre-commit install
    ```  

## Installation

Download and install [Python](https://www.python.org/downloads/)

* If you are using Windows, add Python to your [PATH variable](https://docs.python.org/2/using/windows.html)

Download or [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository

Install requirements from within the main DACSspace directory: ```pip install -r requirements.txt```

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

### Running DACSspace from the command line

In the command line, run `dacsspace`. You will need to pass in different arguments to decide what data DACSspace will fetch, what data it will report out on, and what schema it will validate the data against.

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

## Contributing

Pull requests accepted!

## Authors

Hillel Arnold and Amy Berish

## License

This code is released under the MIT license. See `LICENSE` for further details.
