
<p style="font-family: Arial; font-size:2.1em;color:#1234CC; font-style:bold"><br> 
Example of Reshaping Pandas Data With Melt </p>

<p>[Pandas](https://pandas.pydata.org/) is a python data analysis library and in this post, we will reshape pandas data with melt.</p>


```python
import pandas as pd
data = {
    "location":['CityA', 'CityB'],   
    "Temperature" : ["Predict", "Actual"],
    "Jan-2010":[30, 32],
    "Feb-2010":[45, 43],
    "Mar-2010":[24, 22]
}
print(data)
```

    {'Feb-2010': [45, 43], 'Jan-2010': [30, 32], 'Mar-2010': [24, 22], 'location': ['CityA', 'CityB'], 'Temperature': ['Predict', 'Actual']}


Above Data is a collection of  average Temperature of 2 cities **CityA** and **CityB** in months of _Jan_, _Feb_ & _Mar_.

<p style="font-family:Arial; font-size:1.25em; color:#1234CC; font-style:bold"><br>
Create a pandas dataframe</p>

Let's create a pandas DataFrame object so we could perform our operations on the data.


```python
df = pd.DataFrame(data, columns=['location', 'Temperature','Jan-2010', 'Feb-2010', 'Mar-2010'])
print(df)
```

      location Temperature  Jan-2010  Feb-2010  Mar-2010
    0    CityA     Predict        30        45        24
    1    CityB      Actual        32        43        22


<p style="font-family:Arial; font-size:1.25em; font-style:bold; color:#1234CC"><br>
Reshape DataFrame for better Analysis.</p>

<p>This Data is currently in a human readable form, as there is a row for each location, and a separate column for Temparture in specific months; but is not good for analysis as; if we wanted to create use ‘groupby‘ operations or begin to normalise this dataframe to we would need to do some reshaping.

Let's reshape the dataframe to have a column containing location, and another column to contain Temperature information.</p>


```python
df2 = pd.melt(df, id_vars=["location", "Temperature"], var_name="Date", value_name="Value")
print(df2)
```

      location Temperature      Date  Value
    0    CityA     Predict  Jan-2010     30
    1    CityB      Actual  Jan-2010     32
    2    CityA     Predict  Feb-2010     45
    3    CityB      Actual  Feb-2010     43
    4    CityA     Predict  Mar-2010     24
    5    CityB      Actual  Mar-2010     22


<p style="font-family:Arial; font-size:1.2em; font-style:bold; color:#1234CC"><br>
Sort the data</p>

To sort the data we may use `pandas.DataFrame.sort_values(column_list)` & pass the list of columns to it.


```python
df_sorted = df2.sort_values(["location", "Temperature"])
print(df_sorted)
```

      location Temperature      Date  Value
    0    CityA     Predict  Jan-2010     30
    2    CityA     Predict  Feb-2010     45
    4    CityA     Predict  Mar-2010     24
    1    CityB      Actual  Jan-2010     32
    3    CityB      Actual  Feb-2010     43
    5    CityB      Actual  Mar-2010     22


<p style="font-family:Arial; color:#1234CC; font-size:1.3em; font-style:bold"><br>
References:</p>

* [pandas convert some columns into rows](https://stackoverflow.com/questions/28654047/pandas-convert-some-columns-into-rows)
* [pandas melt library](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.melt.html)
