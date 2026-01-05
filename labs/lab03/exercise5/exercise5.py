def get_position(cars, car_number):
    for item in range(len(cars)):
        if cars[item] == car_number:
            return item

def has_overtaken(before, after, car1, car2):
    for i in range(len(before)):
        if before[i] == car1:
            car1_before = i
        if before[i] == car2:
            car2_before = i

    for j in range(len(after)):
        if after[j] == car1:
            car1_after = j
        if after[j] == car2:
            car2_after = j

    if car1_before > car2_before and car1_after < car2_after:
        return True
    else:
        return False

