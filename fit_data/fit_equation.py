
import math


def get_percentile(sex, age, vomax):

    if sex == 'm':
        a = -9.266519
        b = -0.072175 * age
        c = 0.001209 * (math.pow(age, 2))
        d = 0.2091
        e = 0.001177 * age
        f = -0.000006232 * (math.pow(age, 2))

        p1 = a + b + c
        p2 = (d + e + f) * vomax
        x = (-1) * (p1 + p2)
        logout = math.exp(x)
        ranklong = (1.0 / (1 + logout)) * 100

        return round(ranklong, 2)

    elif sex == 'f':
        a = -9.2987421
        b = 0.0069102 * age
        c = -0.0002642 * (math.pow(age, 2))
        d = 0.2502
        e = -1 * (0.001242 * age)
        f = 0.00004126 * (math.pow(age, 2))

        p1 = a + b + c
        p2 = (d + e + f) * vomax
        x = (-1) * (p1 + p2)
        logout = math.exp(x)
        ranklong = (1.0 / (1 + logout)) * 100

        return round(ranklong, 2)

    else:
        raise ValueError('Selected sex is not an option')
