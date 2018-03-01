from objects import GeneralInfo, Ride, Vehicle


def import_data(path:str):
    general_info = None
    rides = []
    vehicles = []
    with open(path, newline='') as csvfile:
        first = True
        count = 0
        for row in csvfile:
            a = row.split(sep=" ")
            for i, x in enumerate(a):
                a[i] = int(x)
            if first:
                general_info = GeneralInfo(
                    a[0],
                    a[1],
                    a[2],
                    a[3],
                    a[4],
                    a[5]
                )
                for c in range(0, general_info.float):
                    vehicles.append(Vehicle(c, 0, 0))


                first = False
            else:
                rides.append(Ride(
                    count-1,
                    a[0],
                    a[1],
                    a[2],
                    a[3],
                    a[4],
                    a[5]
                ))
            count += 1

    return general_info, rides, vehicles



