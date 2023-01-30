# SLURM usage reporter python package
This package provides a tool to generate a report of the usage of a SLURM
on a cluster. It uses the sacct command to get the information from the




## Requirements

It's a Python 3 program. It has been tested with Python 3.5, 3.6, 3.7, 3.8. It uses the following packages:
* numpy

# Installation

This project uses the standard Python packaging system. Therefore,
just run:

```
    pip install .
```

It will also automatically install any dependencies needed.

This setup does not create an appropriate config file. If you need one
to customize the tool's behaviour, read the following section. By
default config files are looked for in the current directory.

# Usage

Show help:

```
    slurm_usage_report.py --help
```

Show standard report (using defaults):

```
    slurm_usage_report.py --start 2020-01-01 --end 2020-12-31

```

