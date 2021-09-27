"""Imports and return random data from files in directory data_files."""
import random
import os
from pathlib import Path


def project_root():
    """Get project root."""
    return Path(__file__).parent.parent.parent.parent


def absolute_path(file_name):
    """Get absolute path for the file in argument."""
    abs_path = os.path.join(project_root(), "app", "db", "data_files")
    return os.path.join(abs_path, file_name)


def random_bank(file_name):
    """Return a random bank name from filename."""
    with open(absolute_path(file_name), encoding="utf8") as f:
        return random.choice(([line.strip('\n') for line in f.readlines()]))

def random_first_name(file_name):
    """Loop trough and gives index [0] from file first_last_names.txt."""
    with open(absolute_path(file_name), encoding="utf8") as f:
        name = random.choice([line.strip('\n') for line in f.readlines()])
        first_name = [n for n in name.split(' ')]
        return first_name[0]


def random_last_name(file_name):
    """Loop trough and gives index [1] from file first_last_names.txt."""
    with open(absolute_path(file_name), encoding="utf8") as f:
        name = random.choice([line.strip('\n') for line in f.readlines()])
        first_name = [n for n in name.split(' ')]
        return first_name[1]


def random_currency(file_name):
    """Return random abbreviated currency, example SEK for swedish krona."""
    with open(absolute_path(file_name), encoding="utf8") as f:
        currency = random.choice([line.strip('\n') for line in f.readlines()])
        short_currency = [c for c in currency.split(',')]
        return short_currency[0]

