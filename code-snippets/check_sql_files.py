#!/usr/bin/env python3
import subprocess
import re

GREEN = '\033[32m'
RED = '\033[31m'
RESET = '\033[0m'

# Check if there are any .sql files staged for commit
# Applies the check for files that are Added, Copied, Modified or Renamed
sql_files = subprocess.check_output(['git', 'diff', '--cached', '--name-only', '--diff-filter=ACMR', '*.sql']).decode().splitlines()

if sql_files:
    search_string = 'abc.abc'
    print(f"There are staged SQL-files, checking for faulty {search_string}-annotations")
    for file in sql_files:
        with open(file,'r') as f:
            content = f.read()

        # Find all occurrences of search_string in the SQL file(s)
        matches = re.finditer(search_string, content)
        line_numbers = [content.count('\n', 0, match.start()) + 1 for match in matches]
        if (line_numbers):
            found_search_string = True
            print(f"{RED}Aborting commit. The annotation '{search_string}' is found in {file} at line(s): {', '.join(map(str, line_numbers))}")
            print(f"use 'abc.table_name' instead{RESET}")

    if (found_search_string):
        exit(1)

    else: 
        print(f"{GREEN}No faulty '{search_string}'-annotations found!{RESET}")