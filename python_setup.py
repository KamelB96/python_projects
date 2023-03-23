print(f"Hello from inside a file!")

def hello():
    print(f"Hello, user!")

def pack(item1, item2, item3):
    packed_list = [item1, item2, item3]
    return packed_list

def eat_lunch(food_list):
    if len(food_list) == 0:
        print(f"My lunchbox is empty!")
    else:
        print(f"First I eat a/an " + food_list[0])
        for food in food_list[1:]:
            print(f"Next I eat a/an " + food)


hello()
print(pack("a","b","c"))
eat_lunch([])
eat_lunch(["apple"])
eat_lunch(["apple","banana","orange"])