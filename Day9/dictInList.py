travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country,visits,cities):
    new_location = {}

    new_location["country"] = country
    new_location["visits"] = visits
    new_location["cities"] = cities

    travel_log.append(new_location)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)