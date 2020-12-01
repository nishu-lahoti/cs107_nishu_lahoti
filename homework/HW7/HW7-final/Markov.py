import numpy as np
from enum import Enum

class Markov:

    def __init__(self):
        self.data = []
        self.weather_types = {"sunny": 0, "cloudy": 1, "rainy": 2, "snowy": 3, "windy": 4, "hailing": 5}
        # self.weather_types = ["sunny", "cloudy", "rainy", "snowy", "windy", "hailing"]

    def load_data(self, file_path = './weather.csv'):
        self.data = np.genfromtxt(file_path, dtype = float, delimiter = ",")
    
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

# One possible implementation is an enumeration class with the different weather types      
# class WeatherTypes(Enum):
#     sunny = 0
#     cloudy = 1
#     rainy = 2
#     snowy = 3
#     windy = 4
#     hailing = 5
