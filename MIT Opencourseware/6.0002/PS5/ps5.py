# -*- coding: utf-8 -*-
# Problem Set 5: Experimental Analysis
# Name: 
# Collaborators (discussion):
# Time:

import pylab
import re
import matplotlib.pyplot as plt
import numpy as np

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL = range(1961, 2010)
TESTING_INTERVAL = range(2010, 2016)

def calcYearAvgTemp(city, year, climate_instance):
    daily_temp_array = climate_instance.get_yearly_temp(city, year)
    year_temp_sum = daily_temp_array.sum()
    if year%4 != 0:
        year_avg_temp = year_temp_sum/365
    else:
        year_avg_temp = year_temp_sum/366
    return year_avg_temp

"""
Begin helper code
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a 1-d pylab array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return pylab.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.
    
    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by a linear
            regression model
        model: a pylab array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - x.mean())**2).sum()
    SE = pylab.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]

"""
End helper code
"""

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        degs: a list of degrees of the fitting polynomial

    Returns:
        a list of pylab arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    models_list = []
    for degree in degs:
        model = pylab.polyfit(x, y, degree)
        models_list.append(model)
    return models_list

def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    
    Args:
        y: 1-d pylab array with length N, representing the y-coordinates of the
            N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the R-squared error term
    """
    EE = ((y - estimated)**2).sum()
    mean = y.sum()/len(y)
    var_y = ((y - mean)**2).sum()
    return 1 - (EE/var_y)
    

def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-squared value for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points,
        and SE/slope (if degree of this model is 1 -- see se_over_slope). 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    def createGraph(x, y, est_y, r_squared_val, model):
        degree = len(model) - 1
        plt.plot(x, y, 'bo')
        plt.plot(x, est_y, 'r-')
        
        if degree == 1:
            se_ratio = se_over_slope(x, y, est_y, model)
            plt.title("Climate Change Model, Degree " + str(degree) + "\n" + "R^2 = " + str(r_squared_val)
                      + "\n" + "Standard Error Ratio = " + str(se_ratio))
        else:
            plt.title("Climate Change Model, Degree " + str(degree) + "\n" + "R^2 = " + str(r_squared_val))
        
        plt.xlabel("Year")
        plt.ylabel("Degrees (C)")
        plt.show()
    
    def evaluate_each_model(x, y, model):
        plt.plot(x, y, "bo")
        est_y = pylab.array([])
        n = len(model)
        for value in x:
            newVal = 0
            for k in range(n):
                newTerm = model[k]*((value)**(n - k - 1))
                newVal += newTerm
            est_y = np.append(est_y, newVal)
        r_squared_val = r_squared(y, est_y)
        createGraph(x, y, est_y, r_squared_val, model)
    
    def evaluate_all_models(x, y, models):
        for model in models:
            evaluate_each_model(x, y, model)
    
    evaluate_all_models(x, y, models)        

def gen_cities_avg(climate, multi_cities, years):
    """
    Compute the average annual temperature over multiple cities.

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to average over (list of str)
        years: the range of years of the yearly averaged temperature (list of
            int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the average annual temperature over the given
        cities for a given year.
    """
    def natlAvgforOneYear(climate, multi_cities, year):
        natl_sum = 0
        for city in multi_cities:
            city_avg = calcYearAvgTemp(city, year, climate)
            natl_sum += city_avg
        return natl_sum/len(multi_cities)
    
    def natlAvgTotal(climate, multi_cities, years):
        natl_avg_array = pylab.array([])
        for year in years:
            yearly_natl_avg = natlAvgforOneYear(climate, multi_cities, year)
            natl_avg_array = np.append(natl_avg_array, yearly_natl_avg)
        return natl_avg_array
    
    return natlAvgTotal(climate, multi_cities, years)
    
def moving_average(y, window_length):
    """
    Compute the moving average of y with specified window length.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        window_length: an integer indicating the window length for computing
            moving average

    Returns:
        an 1-d pylab array with the same length as y storing moving average of
        y-coordinates of the N sample points
    """
    def calcNewVal(y, beginning_index, end_index):
        newValSum = 0
        for i in range(beginning_index, end_index + 1):
            newValSum += y[i]
        return newValSum/(end_index - beginning_index + 1)
    
    def calcMovingAverage(y, window_length):
        new_array = pylab.array([])
        for i in range(len(y)):
            if i - window_length + 1 >= 0:
                newVal = calcNewVal(y, i-window_length+1, i)
            else:
                newVal = calcNewVal(y, 0, i)
            new_array = np.append(new_array, newVal)
        return new_array
    
    return calcMovingAverage(y, window_length)

def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the root mean square error term
    """
    var_y = ((y - estimated)**2).sum()
    return (var_y/len(y))**0.5

def gen_std_devs(climate, multi_cities, years):
    """
    For each year in years, compute the standard deviation over the averaged yearly
    temperatures for each city in multi_cities. 

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to use in our std dev calculation (list of str)
        years: the range of years to calculate standard deviation for (list of int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the standard deviation of the average annual 
        city temperatures for the given cities in a given year.
    """
    
    def get_std_for_one_year(climate, multi_cities, year):
        year_length = len(climate.get_yearly_temp(CITIES[0], year))
        daily_temp_sum_array = pylab.array([np.linspace(0, 0, year_length)])
        for city in multi_cities:
            daily_temp_city = climate.get_yearly_temp(city, year)
            daily_temp_sum_array += daily_temp_city
        daily_temp_avg_array = daily_temp_sum_array/len(multi_cities)
        return np.std(daily_temp_avg_array)
    
    std_array = pylab.array([])
    for year in years:
        newVal = get_std_for_one_year(climate, multi_cities, year)
        std_array = np.append(std_array, newVal)
    return std_array
  
def evaluate_models_on_testing(x, y, models):
    """
    For each regression model, compute the RMSE for this model and plot the
    test data along with the model’s estimation.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        RMSE of your model evaluated on the given data points. 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    def createGraphTesting(x, y, est_y, rmse_val, model):
        degree = len(model) - 1
        plt.plot(x, y, 'bo')
        plt.plot(x, est_y, 'r-')
        plt.title("Climate Change Model, Degree " + str(degree) + "\n" + "rmse = " + str(rmse_val))
        plt.xlabel("Year")
        plt.ylabel("Degrees (C)")
        plt.show()
    
    def evaluate_each_model_testing(x, y, model):
        plt.plot(x, y, "bo")
        est_y = pylab.array([])
        n = len(model)
        for value in x:
            newVal = 0
            for k in range(n):
                newTerm = model[k]*((value)**(n - k - 1))
                newVal += newTerm
            est_y = np.append(est_y, newVal)
        rmse_val = rmse(y, est_y)
        createGraphTesting(x, y, est_y, rmse_val, model)
    
    def evaluate_all_models_testing(x, y, models):
        for model in models:
            evaluate_each_model_testing(x, y, model)
    
    return evaluate_all_models_testing(x, y, models)

if __name__ == '__main__':
    
    filename = "data.csv"
    climate = Climate(filename)
    year_range = TRAINING_INTERVAL
    # Part A.4   
    def plotDailyTemp(city, month, day, year_range, climate, degs):
        x, y = pylab.array([]), pylab.array([])
        for year in year_range:
            x = np.append(x, year)
            daily_temp = climate.get_daily_temp(city, month, day, year)
            y = np.append(y, daily_temp)
        models = generate_models(x, y, degs)
        evaluate_models_on_training(x, y, models)
    
    city = "NEW YORK"
    month = 1
    day = 10
    degs = [1]
    #plotDailyTemp(city, month, day, year_range, climate, degs)
    
    def plotYearlyTemp(city, year_range, climate, degs):
        x, y = pylab.array([]), pylab.array([])
        for year in year_range:
            x = np.append(x, year)
            yearly_temp = calcYearAvgTemp(city, year, climate)
            y = np.append(y, yearly_temp)
        models = generate_models(x, y, degs)
        evaluate_models_on_training(x, y, models)  
    #plotYearlyTemp(city, year_range, climate, degs)
    
    # Part B
    multi_cities = CITIES
    def plotNatlYearlyTemp(multi_cities, year_range, climate, degs):
        x = pylab.array(np.linspace(year_range[0], year_range[-1], len(year_range)))
        y = gen_cities_avg(climate, multi_cities, year_range)
        models = generate_models(x, y, degs)
        evaluate_models_on_training(x, y, models)
    #plotNatlYearlyTemp(multi_cities, year_range, climate, degs)
    
    # Part C
    def create_x_and_y(climate, multi_cities, year_range, window_length):
        x = pylab.array(np.linspace(year_range[0], year_range[-1], len(year_range)))
        y_old = gen_cities_avg(climate, multi_cities, year_range)
        y = moving_average(y_old, window_length)
        return (x, y)

    window_length = 5
    def plotMovingAverage(climate, multi_cities, year_range, window_length, degs):
        x, y = create_x_and_y(climate, multi_cities, year_range, window_length)
        models = generate_models(x, y, degs)
        evaluate_models_on_training(x, y, models)
    #plotMovingAverage(climate, multi_cities, year_range, window_length, degs)

    # Part D.2
    year_range_testing = TESTING_INTERVAL
    degs = [1, 2, 20]
    x, y = create_x_and_y(climate, multi_cities, year_range, window_length)
    models = generate_models(x, y, degs)
    
    #plotMovingAverage(climate, multi_cities, year_range, window_length, degs)
    
    def plotMovingAverageTesting(climate, multi_cities, year_range_testing, window_length, 
                                 models):        
        x_testing, y_testing = create_x_and_y(climate, multi_cities, year_range_testing, 
                                              window_length)
        evaluate_models_on_testing(x_testing, y_testing, models)
    #plotMovingAverageTesting(climate, multi_cities, year_range_testing, 
                             #window_length, models)   
    # Part E
    degs = [1]
    def plotStDev(climate, multi_cities, year_range, window_length, degs):
        x = pylab.array(np.linspace(year_range[0], year_range[-1], len(year_range)))
        y_old = gen_std_devs(climate, multi_cities, year_range)
        y = moving_average(y_old, window_length)
        models = generate_models(x, y, degs)
        evaluate_models_on_training(x, y, models)
    #plotStDev(climate, multi_cities, year_range, window_length, degs)
