from parser import import_data, export_result

file_path = "doc_given/a_example.in"
result_path = "result/a_example.out"

def main():
    general_info, rides, vehicles = import_data(file_path)
    for i in range(0,general_info.steps):
        if
















    export_result(result_path, vehicles)












    export_result(result_path, vehicles)

if __name__ == "__main__":
    main()
