def number(bus_stops):
    total_people = sum(people_in - people_out for people_in, people_out in bus_stops)
    return total_people

print(number([[1, 2], [9, 4]]))