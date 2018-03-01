from parser import import_data, export_result

# file_path = "doc_given/a_example.in"
# result_path = "result/a_example.out"

# file_path = "doc_given/b_should_be_easy.in"
# result_path = "result/b_should_be_easy.out"

# file_path = "doc_given/c_no_hurry.in"
# result_path = "result/c_no_hurry.out"

# file_path = "doc_given/d_metropolis.in"
# result_path = "result/d_metropolis.out"

file_path = "doc_given/e_high_bonus.in"
result_path = "result/e_high_bonus.out"

def main():
    general_info, rides_orig, vehicles = import_data(file_path)
    rides = sorted(rides_orig, key=lambda x: x.weight(), reverse=True)
    for i in range(0,general_info.steps):
        for v in vehicles:
            if v.fulluntil <= i and rides:
                j=0
                # while(True):
                v.rides.append(str(rides[0].i))
                v.fulluntil = i + rides[0].calculate_distance()
                rides.remove(rides[0])
        if len(rides) == 0:
            break


    export_result(result_path, vehicles)


if __name__ == "__main__":
    main()
