class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, other_country):
        combined_name = f"{self.name} {other_country.name}"
        combined_population = self.population + other_country.population
        combined_country = Country(combined_name, combined_population)
        return combined_country


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
print(f"Countries population is: {bosnia_herzegovina.population}")
print(f"Countries Names are: {bosnia_herzegovina.name}")
