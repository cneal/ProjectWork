import csv


def read_optimal_tours(file_path):
    optimal_tour_costs = {}
    file = open(file_path, 'rb')
    try:
        reader = csv.reader(file)
        for row in reader:
            optimal_tour_costs[row[0]] = int(row[1])
    finally:
        file.close()
    return optimal_tour_costs