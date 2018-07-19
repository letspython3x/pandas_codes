import pandas as pd
import argparse
from werkzeug.utils import cached_property


def parse_cmdline():
    parser = argparse.ArgumentParser(description="Command-line interface to pandas.melt")
    parser.add_argument("-ip", "--input_file", help="input csv file")
    parser.add_argument("-o", "--output_file", default=None, help="Csv file to output. stdout if not specified")
    parser.add_argument("-i", "--id_vars", help="Column(s) to use as identifier variables")
    parser.add_argument("-v", "--value_vars", default=None,
                        help="Column(s) to unpivot. If not specified, uses all columns that are not set as id_vars")
    parser.add_argument("--var_name", default=None,
                        help="Name to use for the variable column. If None it uses frame.columns.name or variable")
    parser.add_argument("--value_name", default=None, help="Name to use for the value column")
    parser.add_argument("--col_level", default=None,
                        help="If columns are a MultiIndex then use N to melt Un-pivot given csv_file."
                        )
    args = parser.parse_args()
    return args


def reshape(df, id_vars=None, value_vars=None, var_name=None, value_name=None, col_level=None):
    id_vars = id_vars.split(',') if isinstance(id_vars, str) else id_vars
    value_vars = value_vars.split(',') if isinstance(value_vars, str) else value_vars
    melted = pd.melt(df, id_vars=id_vars, value_vars=value_vars, var_name=var_name,
                     value_name=value_name, col_level=col_level)
    return melted


def save(df, output_file):
    if output_file:
        with open(output_file, 'w+') as fin:
            df.to_csv(fin)
    else:
        print(df)


def main():
    args = parse_cmdline()
    dataframe = pd.read_csv(args.input_file)
    rdf = reshape(dataframe, **args)
    save(rdf, args.output_file)


if __name__ == "__main__":
    main()
