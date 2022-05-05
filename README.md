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

Using the command line, navigate to the directory containing the DACSspace repository and run `dacsspace.py` to execute the script.

DACSspace will check your ArchivesSpace and CSV filepaths. Your CSV filepath must have a .csv file extension and cannot contain the following characters: * ? : " < > | '

The DACSspace client will handle communication with your ArchivesSpace repository and gets the data from the resources in your AS repository. The client will only fetch data from published resources.

The DACSspace validator will then validate the data that was fetched against a JSON schema. The default schema is the single_level_required JSON schema. If you want to use a different schema, use the command line argument `--schema_identifier` for a schema that is part of the DACSspace `schemas` directory or use `--schema_filepath` for a schema that is external to DACSspace.

From the data fetched from ArchivesSpace by the client, the validator will return the result which is a dictionary including the object's URI (ex. /repositories/2/resources/1234), a boolean indication of the validation result (True or False), an integer representation of the number of validation errors (ex. 1), and if necessary, an explanation of any validation errors (You are missing the following fields ...).

The DACSspace reporter will then write the results produced by the validator to a CSV file. The reporter will return a list of dictionaries containing information about the validation results. The reporter will only write invalid results to the CSV file.

The field names for the CSV file are taken from the result returned by the validator: uri, valid, error_count, and explanation.

If you are using Microsoft Excel to view the CSV file, consult the following links to avoid encoding issues: [Excel 2007](https://www.itg.ias.edu/content/how-import-csv-file-uses-utf-8-character-encoding-0), [Excel 2013](https://www.ias.edu/itg/how-import-csv-file-uses-utf-8-character-encoding).

## Contributing

Pull requests accepted!

## Authors

Hillel Arnold and Amy Berish

## License

This code is released under the MIT license. See `LICENSE` for further details.
