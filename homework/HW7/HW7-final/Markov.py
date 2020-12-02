import numpy as np

class Markov:

    def __init__(self, day_zero_weather = None):
        self.data = []
        self.weather_types = {"sunny": 0, "cloudy": 1, "rainy": 2, "snowy": 3, "windy": 4, "hailing": 5}
        self.day_zero_weather = day_zero_weather

    def __iter__(self):
        # Returns a MarkovIterator object.

        weather_probability_dict = dict()
        weather_probability = [self.get_prob(self.day_zero_weather, w) for w in self.weather_types]
        print(weather_probability)

        for i in self.weather_types:
            weather_probability_dict[i] = [self.get_prob(i, w) for w in self.weather_types]

        return MarkovIterator(self.weather_types, weather_probability_dict, weather_probability, 3)

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

    def _simulate_weather_for_day(day):
        pass

    def get_weather_for_day(day, trials):
        pass



class MarkovIterator:

    def __init__(self, weather_types, transition_matrix, weather_probability, days):
        
        # Initialize the data values and weather types from the Markov class.
        self.weather_types = weather_types
        self.transition_matrix = transition_matrix 
        self.weather_probability = weather_probability
        self.days = days
        

    def __iter__(self):
        return self

    def __next__(self):

        # Use np.random.choice to select one of the weather types based on the probabilities inside
        # the transition matrix. Question is: how do I inform the transition matrix to call the right column?
        
        # The next day's weather should be randomly selected based on the relative probabilities of the next day's weather types
        # given the current day's weather type. The next day's weather should be returned as a lowercase string value (i.e. 'sunny').
        next_day_weather = np.random.choice(self.weather_types, p = self.transition_matrix)
        self.weather_probability = self.transition_matrix[next_day_weather]


        # Once we determine the next day's weather prediction (n+1), we should be able to store it and use it to predict the next days
        # (n+2) weather prediction. This may require switching next_day and current_day.
        # numpy.random.choice might be useful for selecting net day weather.
        self.current_day_weather = next_day_weather
        print(next_day_weather)
        
        return next_day_weather
    



