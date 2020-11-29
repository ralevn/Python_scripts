capitals = {country: city for country, city in zip(input().split(', '), input().split(', '))}

#countries = input().split(', ')
#cities = input().split(', ')

#capitals = dict(zip(countries, cities))

[print(f'{country} -> {city}') for country, city in capitals.items()]