# import matplotlib, pandas, and curve_fit function
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# define class fit_and_plot:
class fit_and_plot: 

    # constructor
    # initialize self.path to path parameter, self.df to a cleaned dataframe read from self.path,
    # self.x to self.df's altitude column, and self.y to self.df's temperature_kel column
    def __init__(self, path):
        self.path = path
        self.df = self.cleanData(self.readData(self.path))
        self.x = self.df["altitude"]
        self.y = self.df["temperature_kel"]

    
    # method to read in data, used in constructor
    def readData(self):
        # read in data from file path 
        return pd.read_csv(self.path)
        
    
    
    # method to clean dataset, used in constructor
    def cleanData(self, df):
        # drop rows with NA
        clean_df = self.df.dropna()
        #rename columns
        clean_df = self.df.rename(columns ={"Temperature (C)":"temp (C)"})
        # drop columns
        clean_df = self.df.drop(columns = {"Pressure (mb)"})
        # create new column representing temperature in Kelvin
        clean_df.loc[:,"temp (K)"] = clean_df.loc[:,"temp (C)"] + 273.15

        # return the cleaned dataframe
        return clean_df
        
    

    # method containing the linear model, used in fitCurve()
    def linearModel(x, m, b):
        return (m * x) + b
    

    # static method to fit a linear model and return fitted parameters
    @staticmethod
    def fitCurve(self):
        # fit line using linear regression model from .linearModel()
        popt, pcov = curve_fit(linearModel, self.x, self.y)
        # create dictionary with parameter values (r and T0), parameter errors, and fitted y values
        m,b = popt
        param_dict = {"r":m, "T0":b, "fitted y vals": pcov}
        # return fitted parameters
        return param_dict


    # method to extract a specified parameter and its error
    # arguments: self, specified parameter, number of decimal places to round to (default=2)
    def getParams(self, var, digits = 2):
        # fit model using fitCurve method
        model = self.fitCurve()
        # extract parameter value and error value for specified parameter
        param, error = model[var][0].round(digits), [var][1].round(digits)

        # return parameter and error
        return param, error
    

    # method to print a specified parameter
    # arguments: self, the specified parameter
    #WE COULDN'T GET THIS TO WORK IN TIME
    #def printParams(self, var):
    #    # get parameter and error value from getParams method
    #    param, error = self.getParams(var)
    #    # print formatted values
    #    return print(var, ': ', param, ', error: ', error, sep = '')


    # method to plot data and fit line
    def plotCurve(self):
        # fit a model using the fitCurve method
        model = self.fitCurve()
        # plot data as a scatterplot
        x = self.clean_df["temp (K)"]
        y = self.clean_df["Altitude (km)"]
        plt.scatter(x,y)
        # add fit line
        plt.plot(x, getParams(fitCurve()["fitted y vals"]), color="red")
                 # add labels
        plt.xlabel("Temperature (K)")
        plt.ylabel("Altitude (km)")
        # add plot title, labels for x-axis and y-axis, and legend
        plt.title("Altitude (km) vs. Temperature (K)")
        plt.legend(fontsize = 12)
