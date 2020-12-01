from Markov import Markov, MarkovIterator

weather_today = Markov()
weather_today.load_data(file_path='./weather.csv')
print(weather_today.get_prob("sunny", "cloudy"))
iter(weather_today)

