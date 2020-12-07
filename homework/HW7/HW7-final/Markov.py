import numpy as np

class Markov:

    def __init__(self, day_zero_weather = None):
        self.data = []
        self.weather_types_map = {"sunny": 0, "cloudy": 1, "rainy": 2, "snowy": 3, "windy": 4, "hailing": 5}
        self.weather_types = ['sunny', 'cloudy', 'rainy', 'snowy', 'windy', 'hailing']
        self.day_zero_weather = day_zero_weather
        self._current_day = 0
        self._current_day_weather = 'sunny'

    def __iter__(self):
        
        transition_matrix = dict()
        weather_probability = [self.get_prob(self._current_day_weather, w) for w in self.weather_types]
        # print(weather_probability)

        for i in self.weather_types:
            transition_matrix[i] = [self.get_prob(i, w) for w in self.weather_types]
        
        # Returns a MarkovIterator object.
        return MarkovIterator(self.weather_types, transition_matrix, weather_probability)

    def load_data(self, file_path = './weather.csv'):
        self.data = np.genfromtxt(file_path, dtype = float, delimiter = ",")

    def get_prob(self, current_day_weather, next_day_weather):
        
        # Inputs must be one of the six specified weather types
        # Raise an exception if one of the six strings is not specified
        if (current_day_weather not in self.weather_types) or (next_day_weather not in self.weather_types):
            raise Exception("Invalid inputs. Please enter one of following:\
                'sunny', 'cloudy', 'rainy', 'snowy', 'windy', or 'hailing'.")
        
        # Make sure the strings are lowercase. You can either raise an exception for upper case or convert them automatically.
        # current_day = current_day_weather.lower()
        # next_day = next_day_weather.lower()

        current_day_index = self.weather_types_map[current_day_weather]
        next_day_index = self.weather_types_map[next_day_weather]

        # Return the probability of next_day_weather given current_day_weather
        return self.data[current_day_index][next_day_index]

    def _simulate_weather_for_day(self, day):
        
        # This method returns the predicted weather as a string on the specified day.

        # countDays useful for decrementing input day value.
        countDays = day
        
        # Catch if the day value is equal to zero and set it equal to day_zero_weather
        if day == 0:
            return self.day_zero_weather
        
        # Iterate through self and update _current_day and _current_day_weather. Break when countDays = 0.
        for i in self:
            self._current_day += 1
            self._current_day_weather = i
            countDays -= 1
            if countDays == 0:
                break

        return self._current_day_weather

    def get_weather_for_day(self, day, trials = 7):
        
        # Create empty array to store simulations
        simulated_days = []

        # For the number of trials, run the simulator. Provide ways to refresh the current day and current weather.
        while trials > 0:
            simulated_days.append(self._simulate_weather_for_day(day))
            self._current_day = 0
            self._current_day_weather = self.day_zero_weather
            trials -=1

        return simulated_days


class MarkovIterator:

    def __init__(self, weather_types, transition_matrix, weather_probability):
        
        # Initialize the data values and weather types from the Markov class.
        self.weather_types = weather_types
        self.transition_matrix = transition_matrix 
        self.weather_probability = weather_probability
        

    def __iter__(self):
        return self

    def __next__(self):

        # Use np.random.choice to select one of the weather types based on the probabilities inside
        # the transition matrix. Question is: how do I inform the transition matrix to call the right column?
        
        # The next day's weather should be randomly selected based on the relative probabilities of the next day's weather types
        # given the current day's weather type. The next day's weather should be returned as a lowercase string value (i.e. 'sunny').
        next_day_weather = np.random.choice(self.weather_types, p = self.weather_probability)
        self.weather_probability = self.transition_matrix[next_day_weather]

        # Once we determine the next day's weather prediction (n+1), we should be able to store it and use it to predict the next days
        # weather prediction. 
        # self.current_day_weather = next_day_weather
        # print(next_day_weather)
        return next_day_weather
    

