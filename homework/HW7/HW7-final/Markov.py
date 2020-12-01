import numpy as np
from enum import Enum

class Markov:

    def __init__(self):
        self.data = []
        self.weather_types = {"sunny": 0, "cloudy": 1, "rainy": 2, "snowy": 3, "windy": 4, "hailing": 5}
        # self.weather_types = ["sunny", "cloudy", "rainy", "snowy", "windy", "hailing"]

    def __iter__():
        pass
        # Returns a MarkovIterator object.
        # Hint: self.get_prob() might come in handy here.

    def load_data(self, file_path = './weather.csv'):
        self.data = np.genfromtxt(file_path, dtype = float, delimiter = ",")
        # print(self.data)
    
    def get_prob(self, current_day_weather, next_day_weather):
        
        # Inputs must be one of the six specified weather types
        # Raise an exception if one of the six strings is not specified
        if (current_day_weather not in self.weather_types) or (next_day_weather not in self.weather_types):
            raise Exception("Invalid inputs. Please enter one of following:\
                'sunny', 'cloudy', 'rainy', 'snowy', 'windy', or 'hailing'.")
        
        # Make sure the strings are lowercase. You can either raise an exception for upper case or convert them automatically.
        current_day = current_day_weather.lower()
        next_day = next_day_weather.lower()

        # Return the probability of next_day_weather given current_day_weather
        return self.data[self.weather_types[next_day]][self.weather_types[current_day]]

class MarkovIterator:

    def __init__(self, day_zero_weather, weather_types, transition_matrix):
        # Useful attributes to help you with the next method
        self.day_zero_weather = day_zero_weather
        self.weather_types = weather_types
        self.transition_matrix = transition_matrix # np.atleast_2d(transition_matrix)
        self.index_dict = {self.weather_types[index]: index for index in range(len(self.weather_types))}
        # Somehow initialize the data values from the Markov class.


    def __iter__(self):
        return self

    def __next__(self, current_day_weather):

        return np.random.choice(
            self.weather_types, p = self.transition_matrix[self.index_dict[current_day_weather], :]
        )
        # The next day's weather should be randomly selected based on the relative probabilities of the next day's weather types
        # given the current day's weather type. The next day's weather should be returned as a lowercase string value (i.e. 'sunny').

        # Once we determine the next day's weather prediction (n+1), we should be able to store it and use it to predict the next days
        # (n+2) weather prediction. This may require switching next_day and current_day.
        # numpy.random.choice might be useful for selecting net day weather.

        # Online example: https://medium.com/@__amol__/markov-chains-with-python-1109663f3678

        pass

# One possible implementation is an enumeration class with the different weather types      
# class WeatherTypes(Enum):
#     sunny = 0
#     cloudy = 1
#     rainy = 2
#     snowy = 3
#     windy = 4
#     hailing = 5
