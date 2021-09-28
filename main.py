
import kendall_tau
import csv

if __name__ == '__main__':


    nominatim = []
    qrank = []



    with open('nominatim_ranked_castles.csv', 'r') as file:
        reader = csv.reader(file)
        nominatim = [item for item in reader]
    with open('qrank_ranked_castles.csv', 'r') as file:
        reader = csv.reader(file)
        qrank = [item for item in reader]

    count = 200

    qrank = qrank[:count]
    nominatim = nominatim[:count]

    kendall_tau.calculate_kendall_tau(nominatim, qrank)

    # determine amount of different entries
    x_array = nominatim
    y_array = qrank

    count_difference = 0

    for item in x_array:
        if item not in y_array:
            count_difference += 1

    for item in y_array:
        if item not in x_array:
            count_difference += 1
    # print difference
    print(f"difference: {count_difference}")

