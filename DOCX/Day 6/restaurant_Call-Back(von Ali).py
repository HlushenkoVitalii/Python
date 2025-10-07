#it is a callback example. customer in a restaurant put an order an the waiter delivers the order when it is ready

##--
#   PS CODE (beachten Sie arr_lengcht is definiern in linei 9)
#   
# def food_exists = 0
#   // "i" ist Array = 0
# FOR i IST 0 BIS i <= arr_length i PLUS 1
#   WENN food_ 

def checkFoodExistence(food_name:str):
    #
    arr_foods = ["Pizza", "Pasta", "Dönner"]
    arr_length = len(arr_foods)

    print(f"we have {arr_length} foods in Menu")

def orderFood(food_name:str, checkFoodExistence):
    print(f"your {food_name} deliver soon!")
    checkFoodExistence(food_name)

#-- actual program use upper defined methods --#

order_string = input("what is your order?")
orderFood(order_string, checkFoodExistence)