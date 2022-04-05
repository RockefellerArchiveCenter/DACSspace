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

Download [Python](https://www.python.org/downloads/)

If you are using Windows, add Python to your [PATH variable](https://docs.python.org/2/using/windows.html)

Install requirements ([ConfigParser instructions](https://docs.python.org/2/library/configparser.html) /  [Requests instructions](http://docs.python-requests.org/en/master/user/install/))

## Setup

Run `setup.py` to create a configuration file named `local_settings.cfg` which will allow you to connect to your ArchivesSpace instance. You will need:
* BaseURL of your ArchivesSpace instance
* Repository ID for your ArchivesSpace installation
* ArchivesSpace username and password

Your configuration file will look something like this:
```
[ArchivesSpace]
baseURL: #BaseURL of your ArchivesSpace instance
repository: #Repository ID of your ArchivesSpace installation
user: #ArchivesSpace username
password: #ArchivesSpace password for the username used above

[Destinations]
directory: #Directory where you would like to save the csv file
filename: dacs_singlelevel_report.csv
```

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

Pull requests accepted!

## Authors

Hillel Arnold and Amy Berish

## License

This code is released under the MIT license. See `LICENSE` for further details.
