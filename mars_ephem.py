import ephem
#mars=ephem.Mars('2000/01/01')
#const=ephem.constellation(mars)
#print(mars)
#print(const)



import ephem


planet_names = {
    "марс": "mars",
    "юпитер": "jupiter",
    "уран": "uranus"
}

name = input("Введите, например: Планета Марс: ").lower()
planet_name = name.split()
print(planet_name[1])

if planet_name[1] in planet_names:
    planet = getattr(ephem, planet_names[planet_name[1]].capitalize())()
    print(str(planet))
    planet.compute()
    const = ephem.constellation(planet)
    print(f"Созвездие для {planet_name[1]}: {const[1]}")
else:
    print("Неправильное название планеты.")