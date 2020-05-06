#!/usr/bin/env python
"""
convert_table_to_latex.py

quick script to convert a table from csv to latex using pandas. To use
simply run

./convert_table_to_latex.py <path>/<to>/<table>

by default will dump to cwd <old table name>.txt
"""
import argparse
import pathlib

import pandas as pd

def main():
    """main loop of script"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pathname", type=str, help="path to table to be converted")
    parser.add_argument("--outpath", "-o", type=str, default=None, help="optional output path")
    args = parser.parse_args()
    path = pathlib.Path(args.pathname)

    df = pd.read_csv(path, sep='\t', index_col=0, header=0, dtype={"ndata": int})
    print("Read table:")
    print("")
    print(df)
    if args.outpath is not None:
        outname = args.outpath
    else:
        outname = path.stem + ".txt"

    with open(outname, "w+") as f:
        df.to_latex(f, float_format="{:0.2f}".format,)
    print("")
    print(f"table successfully output to {pathlib.Path(outname).absolute()}")


if __name__ == "__main__":
    main()