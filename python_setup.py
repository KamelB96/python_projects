print("Hello from inside a file!")

def hello():
    print("Hello, user!")

def pack(item1, item2, item3):
    packed_list = [item1, item2, item3]
    return packed_list

def eat_lunch(food_list):
    if len(food_list) == 0:
        print("My lunchbox is empty!")
    else:
        print("First I eat " + food_list[0])
        for food in food_list[1:]:
            print("Next I eat " + food)
