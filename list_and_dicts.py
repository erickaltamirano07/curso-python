def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dic = {"fistnmae": "Facundo", "lastname": "Garcia"}

    super_list = [
        {"fistnmae": "Facundo", "lastname": "Garcia"},
        {"fistnmae": "Miguel", "lastname": "Torres"},
        {"fistnmae": "Pepe", "lastname": "Rodelo"},
        {"fistnmae": "Susana", "lastname": "Martinez"},
        {"fistnmae": "Hose", "lastname": "Garcia"}
    ]

    super_dic = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dic.items():
        print(key, "-", value)


if __name__ == '__main__':
    run()
