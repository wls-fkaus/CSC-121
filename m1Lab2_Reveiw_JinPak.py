# Jin Pak
# 1/17/25
# m1Lab2
# Calculate which route is faster


count = 0

run_again = "yes"

# list for times
fastest_min = []

while run_again == "yes":
    count += 1
    distance = float(input(f"Enter route {count} distance (miles): "))
    speed = float(input(f"Enter route {count} speed (miles/hour): "))

    mins = (distance / speed) * 60

    fastest_min.append(mins)




    run_again = input("Do you want to add another route?: ")

# fastest time
fastest_time = min(fastest_min)


# fastest route number
fastest_route = fastest_min.index(fastest_time) + 1

print(f"Route {fastest_route} is fastest; {fastest_time}")


