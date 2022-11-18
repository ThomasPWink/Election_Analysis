print("Hello World ")
counties = ["Arapahoe","Denver","Jefferson"]
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

if counties == 'Denver':

    print(counties[1])

if "El Paso" in counties:

    print("El Paso is in the list of counties.")

else:

    print("El Paso is not in the list of counties")


for county in counties:
    print(county)

for county in counties_dict:
    print(county)

for voters in counties_dict.values():

    print(voters)

for county, voters in counties_dict.items:

    print(county + " county has ",voters + " registered voters")
