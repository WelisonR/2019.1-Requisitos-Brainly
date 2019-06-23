#!/usr/bin/env python3

# Instructions
## Install with pip:
## 	ezodf==0.3.2
##	lxml==3.7.2

## To execute:
##	python ods_para_md.py entrada.ods > saida.md


# Not suport merge cells

from __future__ import print_function

import ezodf
import sys
import unicodedata

# Ref: http://stackoverflow.com/a/31666966/224671
DISPLAY_WIDTH = {
    'A': 1,
    'F': 2,
    'H': 1,
    'N': 1,
    'Na': 1,
    'W': 2,
}

def display_text(cell):
    v = cell.value
    if isinstance(v, float):
        return '{:g}'.format(v)
    elif v is None:
        return ''
    else:
        return str(v)

def display_len(s):
    return sum(DISPLAY_WIDTH[unicodedata.east_asian_width(c)] for c in s)

def main(odf_path, out_file):
    ods = ezodf.opendoc(odf_path)

    for sheet in ods.sheets:
        column_widths = [max(display_len(display_text(cell)) for cell in column) for column in sheet.columns()]
        if not any(column_widths):
            continue

        print('##', sheet.name, file=out_file)
        printed_header = False

        for row in sheet.rows():
            contents = [display_text(cell) for cell in row]
            if not any(contents):
                continue

            print('|', end='', file=out_file)
            for m, content in enumerate(contents):
                column_width = column_widths[m]
                if not column_width:
                    continue
                disp_len = column_width + len(content) - display_len(content)
                print(' {0:<{1}}'.format(content, disp_len), end=' |', file=out_file)
            print(file=out_file)

            if not printed_header:
                printed_header = True
                print('|', end='', file=out_file)
                for w in column_widths:
                    if w:
                        print(':', '-' * (w+1), '|', sep='', end='', file=out_file)
                print(file=out_file)

if __name__ == '__main__':
    main(sys.argv[1], sys.stdout)
