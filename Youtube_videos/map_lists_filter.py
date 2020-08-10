
# Convert temperature from Celsius to fahrenheit

temp = [("Berlin", 25), ("Amsterdam", 15), ("Zurich", 3)]

c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

print(list(map(c_to_f, temp)))

# filters

import numpy as np

data = [2.5, 3.6, 8.5, 9.1, 7.7, 5.5 ]

avg = np.mean(data)

print(avg)

print(list(filter(lambda x: x > avg, data)))



# Remove missing data

countries = ["", "Argentina", "", "India", "Chile", "Switzerland", ""]

print(list(filter(None, countries)))