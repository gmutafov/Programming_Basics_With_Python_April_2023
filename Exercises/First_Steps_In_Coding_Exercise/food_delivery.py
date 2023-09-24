CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGETARIAN_MENU = 8.15
SHIPMENT = 2.50

chicken_menu_quantity = int(input())
fish_menu_quantity = int(input())
vegetarian_menu_quantity = int(input())

chicken_menues_price = chicken_menu_quantity * CHICKEN_MENU
fish_menues_price = fish_menu_quantity * FISH_MENU
vegetarian_menues_price = vegetarian_menu_quantity * VEGETARIAN_MENU
total_menues_cost = chicken_menues_price + fish_menues_price + vegetarian_menues_price
desert_price = 0.20 * total_menues_cost
total_price = total_menues_cost + desert_price + SHIPMENT
print (f"{total_price} lv.")