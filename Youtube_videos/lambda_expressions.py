def f(x):

    return 3*x + 1


print(f(3))

g = lambda x: 3*x + 2

print(g(5))

# Combine first name and last name into a single "Full name"

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

print(full_name('ankit', 'izardar'))


# sort acoording to last names

names = ["Ankit Izardar", "Rocky Gueardina", "Pilait Greuwes"]


names.sort(key=lambda name: name.split(" ")[-1].lower())

print(names)


def build_quadratic_function(x, a, b, c):

    """ Returns the function f(x) = ax^2 + bx + c """

    return a*x*x + b*x + c

print(build_quadratic_function(2, 1, 1, 1))
    