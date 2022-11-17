list_cities = ["Hyderabad", "Chennai", "Bangalore", "Hyderabad", "Mumbai", "Delhi"]
print(list_cities.count("Hyderabad"))

list_countries = ["Taiwan", "Denmark", "Belgium", "United States", "Australia", "India", "Austria", "Egypt", "Brazil",
              "New Zealand", "Canada", "Thailand", "Japan"]
print(list_countries)
print(list_countries.sort())  # It returns None if we directly print it.
print(list_countries)  # Sorting is done in ascending order by default.

list_eleven = [5, 6, 7, 1, 2, 3, 4]
list_eleven.sort()
print(list_eleven)
list_cities.reverse()
print(list_cities)

list_nine = ["Tanzania", "austria", "belgium", "japan"]
list_nine.sort()
print(list_nine)  # Sorting order is case-sensitive.

list_nine.sort(key=str.lower)
print(list_nine)  # Sorting order (case in-sensitive).

list_ten = ["Python", "API", "SQL", 'DevOps', 2021, 21.07, True, False]
list_ten.reverse()
print(list_ten)



