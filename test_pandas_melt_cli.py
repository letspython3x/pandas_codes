from pandas_codes import pandas_melt_cli as pmc

X_DATAFRAME = {
    "Col1": ['R1C1', 'R2C1'],
    "Col2": ['R1C2', 'R2C2'],
    "Col3": ['R1C3', 'R2C3'],
}

X_EXPECTED_DF = {
    "Col1": {0: 'R1C1', 1: 'R2C1', 2: 'R1C1', 3: 'R2C1'},
    "value": {0: 'R1C2', 1: 'R2C2', 2: 'R1C3', 3: 'R2C3'},
    "variable": {0: 'Col2', 1: 'Col2', 2: 'Col3', 3: 'Col3'},
}
X_ARGS = dict(id_vars='Col1',
              value_vars='Col2,Col3',
              var_name='variable',
              value_name='value',
              col_level=None
              )


def test_returns_expected_reshaped_dataframe():
    X_DF = pmc.pd.DataFrame(X_DATAFRAME)
    X_RDF = pmc.reshape(X_DF, **X_ARGS)
    assert X_EXPECTED_DF == pmc.pd.DataFrame.to_dict(X_RDF)
