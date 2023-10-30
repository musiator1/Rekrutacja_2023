import pandas as pd

data = pd.read_csv(r"spaceship_titanic\dane.csv")

print("Passengers from Earth:", len(data[data["HomePlanet"] == "Earth"]))
print("Passengers from Europa:", len(data[data["HomePlanet"] == "Europa"]))
print("Passengers from Mars:", len(data[data["HomePlanet"] == "Mars"]))

earth_destinations = data[data["HomePlanet"] == "Earth"].groupby("Destination")["HomePlanet"].count()
europa_destinations = data[data["HomePlanet"] == "Europa"].groupby("Destination")["HomePlanet"].count()
mars_destinations = data[data["HomePlanet"] == "Mars"].groupby("Destination")["HomePlanet"].count()
print("\n", "Destinations od Earth starters:")
print(earth_destinations)
print("\n", "Destinations od Europa starters:")
print(europa_destinations)
print("\n", "Destinations od Mars starters:")
print(mars_destinations)

#nothing worth to note in report