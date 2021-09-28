import math


def calculate_kendall_tau(x_array, y_array): # xArray is also used to determine the order of both lists.
    provision = 0
    inversion = 0
    x_tie = 0
    y_tie = 0

    #pair_map = {} # consists of: KEY: {array with x_value and y_value} VALUE: operation of pair ('0' => Match, '+' => add to provision, '-' => add to inversion)

    tested = []

    for current_item in y_array:
        index_current_item = y_array.index(current_item)
        # compare with all entries that have currentIndex<=
        for index_opposing_item in range(index_current_item, len(x_array)):

            # print(f"{tested} + {index_opposing_item}")
            if (index_opposing_item in tested) or (current_item not in x_array):
                useless = "yup... i'm pretty much useless"

            # if currentIndex in arrayX == currentItem then totalTie++
            elif current_item == x_array[index_opposing_item]:
                # print(f"{index_current_item} - {index_opposing_item}")
                if index_current_item == index_opposing_item:
                    x_tie += 1
                    y_tie += 1

                    #pair_map[{y_array[current_item], x_array[index_opposing_item]}] = '0'

            # if rdmIndex in arrayX >= currentItem then provisionalSum++
            elif index_opposing_item > x_array.index(current_item):
                # print(f"{index_current_item} {index_opposing_item}")
                provision += 1

                #pair_map[{y_array[current_item], x_array[index_opposing_item]}] = '+'

            # if rdmIndex in arrayY <= currentItem then provisionalSum--
            elif index_opposing_item < x_array.index(current_item):
                inversion += 1

                #pair_map[{y_array[current_item], x_array[index_opposing_item]}] = '-'

        # if xArray doesn't have current Item -> totalTie++
        if current_item not in x_array:
            y_tie += 1
        else:
            tested.append(x_array.index(current_item))

    # if y_item not in yArray
    for x_item in x_array:
        if x_item not in y_array:
            x_tie += 1

    print(f"{provision} {inversion} {x_tie} {y_tie}")
    print(calculate_tau_result(provision, inversion, x_tie, y_tie))
#    print_map(pair_map)


def calculate_tau_result(provision, inversion, x_tie, y_tie):
    return (provision-inversion)/math.sqrt((provision + inversion + x_tie) * (provision + inversion + y_tie))


def calc_big_t(n, x_range):
    sum = 0
    for x in range(n):
        sum += x_range*(x_range-1)/2

    return sum


def print_map(map):
    result_str = ""
    for key, value in map.items():
        result_str += f"{key[0]} - {key[1]} o: {value}"

    print(result_str)


