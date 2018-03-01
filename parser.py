from objects import GeneralInfo, Ride


def import_data(path:str):
    general_info = None
    rides = []
    with open(path, newline='') as csvfile:
        first = True
        for i, row in enumerate(csvfile):
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
                first = False
            else:
                rides.append(Ride(
                    i,
                    a[0],
                    a[1],
                    a[2],
                    a[3],
                    a[4],
                    a[5]
                ))

    return general_info, rides



