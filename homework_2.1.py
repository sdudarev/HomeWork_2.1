def recipes():
    cook_book ={}
    with open('new.txt', encoding= 'utf8') as f:
        recipe = []
        for entry in f:
            entry = entry.strip()
            if entry == '':
                cook_book.update(pars_recipe(recipe))
                recipe = []
            else:
                recipe.append(entry)
        cook_book.update(pars_recipe(recipe))
    return cook_book

def pars_recipe(recipe):
    cook = {}
    dish = recipe[0].strip()
    cook[dish] = []
    ingredients_quantity = int(recipe[1])
    for index in range(ingredients_quantity):
        ingredient = recipe[index+2].split('|')
        cook[dish].append({"ingridient_name": ingredient[0].strip(), "quantity": int(ingredient[1]), "measure": ingredient[2].strip()})
    return cook


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item["quantity"] *= person_count
            if new_shop_list_item["ingridient_name"] not in shop_list:
                shop_list[new_shop_list_item["ingridient_name"]] = new_shop_list_item
            else:
                shop_list[new_shop_list_item["ingridient_name"]]["quantity"] += new_shop_list_item["quantity"]
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))


def create_shop_list():
    cook_book = recipes()
    person_count = int(input('Введите количество человек: '))
    dishes = input('ВВедите блюдо в расчете на одного человека (через запятую): ').split(', ')
    shop_list = get_shop_list_by_dishes(cook_book ,dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()