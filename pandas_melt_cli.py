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


class MeltCsv(object):
    def __init__(self, input_file, output_file=None, id_vars=None,
                 value_vars=None, var_name=None, value_name=None,
                 col_level=None):
        self.input_file = input_file
        self.output_file = output_file or ''
        self.id_vars = id_vars.split(',')
        self.value_vars = value_vars.split(',')
        self.var_name = var_name or 'variable'
        self.value_name = value_name or 'value'
        self.col_level = col_level

    @cached_property
    def df(self):
        dataframe = pd.read_csv(self.input_file)
        return dataframe

    def melt(self):
        melted = pd.melt(self.df, id_vars=self.id_vars,
                         value_vars=self.value_vars, var_name=self.var_name,
                         value_name=self.value_name, col_level=self.col_level)
        return melted

    def save(self, df):
        if self.output_file:
            df.to_csv(self.output_file)
        else:
            print(df)


def main():
    args = parse_cmdline()
    m = MeltCsv(**args)
    mdf = m.melt()
    m.save(mdf)


if __name__ == "__main__":
    main()
