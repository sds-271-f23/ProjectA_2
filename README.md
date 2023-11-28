# SDS 271 - GROUP 5
The class `fit_and_plot` is designed to perform data analysis on atmospheric data. The class provides methods to read data from a file, clean the dataset, fit a linear model to the data, extract model parameters, and visualize the results.

## Instance attributes:

### self.path
(string) The filepath of the CSV file to be read in as data.

### self.df
(Pandas DataFrame) A cleaned dataframe containing the information in the original CSV file, but with missing values removed and a new column for temperature in Kelvin.

### self.x
(Pandas Series, numeric) The 'altitude' column from `self.df`. Used as the independent variable in the fitted model.

### self.y
(Pandas Series, numeric) The 'temperature in Kelvin' column from `self.df`. Used as the dependent variable in the fitted model.

## Summary of methods:

### \__init__(path)
Description: constructor. Initializes `self.path` to the path parameter. Passes `self.path` into `readData()` and the result into `cleanData()`; assigns the final result to `self.df`. Initalizes `self.x` as the 'altitude' column of `self.df`; and `self.y` as the 'temperature_kel' column of `self.df`. 

Parameters: 
-   path (string): The file path of the CSV file to be read in as data.

Returns: None

### readData(path):
Description: Reads data from a CSV file specified by the given file path.

Parameters:  
-   path (string): The file path of the CSV file.

Returns: A Pandas DataFrame containing the data.

### cleanData(df)
Description: Cleans the dataset by renaming columns, dropping unnecessary columns, dropping missing values, and adding a column for temperature in Kelvin.

Parameters:
-   df (DataFrame): The input data.

Returns: A cleaned Pandas DataFrame.

### linear model(x, m, b):
Description: Defines a linear model function ( y = mx + b ).

Parameters:
-   x (array-like): Independent variable values.
-   m (float): Slope of the line.
-   b (float): Y-intercept of the line.

Returns: An array of predicted y values.

### fitCurve():
Description: Fits a linear model to the data using the `curve_fit` method on `self.x` and `self.y`.

Parameters: None

Returns: A dictionary containing the fitted parameters 'r' (slope), 'T0' (y-intercept), and the fitted y values.

### getParams(var, digits=2)
Description: Extracts a specified parameter and its error from the fitted model.

Parameters:
-   var (string): The specified parameter to extract.
-   digits (int, optional): Number of decimal places to round to (default is 2).

Returns: An array containing the rounded parameter value (float) and the rounded error bounds (array).

### printParams(var) - NOT CURRENTLY SUPPORTED
Description: Prints the specified parameter and its error, both rounded to 2 decimal places.

Parameters:
-   var (string): The specified parameter to print.

Returns: A string showing the parameter and its error rounded to 2 decimal places.

### plotCurve()
Description: Plots the data as a scatterplot and shows the fitted line.

Parameters: None

Returns: None
