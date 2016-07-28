arr = [[10,0],[3,5],[5,8]]

def number(bus_stops):
    total = 0
    for pair in bus_stops:
        for ind,pas in enumerate(pair):
            if ind==0:
                total+=pas
            if ind==1:
                total-=pas
    return total