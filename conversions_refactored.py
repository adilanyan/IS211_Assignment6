def convert(from_unit, to_unit, value):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    value = float(value)
    if from_unit == to_unit:
        value = value
        return value

    if from_unit == 'miles':
        if to_unit == 'yards':
            value = value * 1760.0
            return round(value, 2)
        elif to_unit == 'meters':
            value = value * 1604.344
            return round(value, 2)
        else:
            raise ConversionsNotPossible('Please enter the valid units')

    if from_unit == 'yards':
        if to_unit == 'meters':
            value = value * 0.9144
            return round(value, 2)
        elif to_unit == 'miles':
            value = value / 1760.0
            return round(value, 2)
        else:
            raise ConversionsNotPossible('Please enter the valid units')

    if from_unit == 'meters':
        if to_unit == 'miles':
            value = value * 0.000621
            return round(value, 2)
        elif to_unit == 'yards':
            value = value * 1.0936
            return round(value, 2)
        else:
            raise ConversionsNotPossible('Please enter the valid units')

    if from_unit == 'celsius':
        if to_unit == 'kelvin':
            value = value + 273.15
            return round(value, 2)

        elif to_unit == 'fahrenheit':
            value = ((value * 1.8) + 32)
            return round(value, 2)
        else:
            raise ConversionsNotPossible('Please enter the valid units')

    if from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            value = ((value - 32) * 5 / 9)
            return round(value, 2)
        elif to_unit == 'kelvin':
            value = (value + 459.67) * 5 / 9
            return round(value, 2)
        else:
            raise ConversionsNotPossible('Please enter the valid units')

    if from_unit == 'kelvin':
        if to_unit == 'celsius':
            value = value - 273.15
            return round(value, 2)
        elif to_unit == 'fahrenheit':
            value = (value * 9 / 5) - 459.67
            return round(value, 2)
        else:
            raise ConversionsNotPossible('Please enter the valid units')


print(convert('meters', 'miles', 1))
print(convert('meters', 'yards', 1))
print(convert('miles', 'yards', 1))
print(convert('miles', 'meters', 1))
print(convert('yards', 'meters', 1))
print(convert('yards', 'miles', 1))
print(convert('kelvin', 'celsius', 1))
print(convert('kelvin', 'fahrenheit', 1))
print(convert('celsius', 'kelvin', 1))
print(convert('celsius', 'fahrenheit', 1))
print(convert('fahrenheit', 'kelvin', 1))
print(convert('fahrenheit', 'celsius', 1))
print(convert('fahrenheit', 'fahrenheit', 1))

