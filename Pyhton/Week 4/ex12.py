# Calculate the cost of the hotel
def hotel_cost(nights):
    cost = nights * 70
    return cost

# Calculate the cost of the plane ticket
def plane_ticket(city, flight):
    if(city == "New York"):
        return 2000 * flight
    elif(city == "Auckland"):
        return 790 * flight
    elif(city == "Venice"):
        return 154 * flight
    elif(city == "Glasgow"):
        return 65 * flight

# Calculate the cost of a rental car
def rental_car(days):
    cost = days * 30
    if(days >= 7):
        cost = hotel_cost(days) - 50
    if(days >= 3):
        cost = hotel_cost(days) - 30
    return cost

# Calculate the total cost of the trip
def total_cost(city, days, flight):
    total = hotel_cost(days) + plane_ticket(city, flight) + rental_car(days)
    return total

# Ask the user to input the city and the number of nights
city = input("Insert the name of the city:\n")
flight = float(input("Insert 1.0 for Economy | 1.3 for Premium Economy | 1.6 for Business Class | 1.9 for First Class\n"))
nights = int(input("Insert the number of days you are staying:\n"))

# Print the total cost of the trip to the user
total = total_cost(city, nights, flight)
print(f"The total cost of your trip is: {total}\n")
