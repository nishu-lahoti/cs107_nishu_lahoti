import collections
from Markov import Markov

city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}

# Create an empty dictionary to capture values from first iteration
city_dictionary = {}

# First iteration which creates prediction objects for each city
# and then runs the get_weather_for_day method for 7 days and 100 trials.
# This information is stored in the city dictionary and printed.
for i in city_weather:
    predictions = Markov(city_weather[i])
    predictions.load_data(file_path='./weather.csv')
    prediction_val = predictions.get_weather_for_day(7, 100)
    coll = collections.Counter(prediction_val)
    city_dictionary[i] = coll
    print(i, ":", dict(coll))

print("\nMost likely weather in seven days")
print("----------------------------------")


# Second iteration which iterates through the city dictionary and finds the most
# common weather type and prints it out.
for i in city_dictionary:
    most_common = city_dictionary[i].most_common()
    print(i, ":", most_common[0][0])



