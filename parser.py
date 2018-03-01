

def import_data(path:str):
    with open(path, newline='') as csvfile:
        for row in csvfile:
            print(row)

