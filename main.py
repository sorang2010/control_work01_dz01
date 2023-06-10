import crud

# crud.init_db_txt()
print('консольное приложение заметки')
while True:
    ch1 = input('Создать файл новой заметки? (Y/N)')
    if ch1 == 'y' or ch1 == 'Y':
        crud.init_db_csv()
        print('файл создан')
    else:
        print('до новых встреч')

    ch2 = input('желаете посмотреть заметки? (Y/N)')
    if ch2 == 'y' or ch2 == 'Y':
        crud.row_read()
        print('все записи')
    else:
        print('до новых встреч')

    ch3 = input('желаете ввести новую заметку? (Y/N)')
    if ch3 == 'y' or ch3 == 'Y':
        crud.row_create()
        print('запись создана')
    else:
        print('до новых встреч')

    ch4 = input('желаете выполнить поиск? (Y/N)')
    if ch4 == 'y' or ch4 == 'Y':
        str_to_find = input('введите строку поиска ')
        crud.row_find(str_to_find)
        # print('запись создана')
    else:
        print('до новых встреч')

    ch5 = input('желаете выполнить замену данных? (Y/N)')
    if ch5 == 'y' or ch5 == 'Y':
        str_to_find = input('введите строку поиска ')
        str_to_repl = input('введите строку замены ')
        crud.row_replace(str_to_find, str_to_repl)
        # print('запись создана')
    else:
        print('до новых встреч')

    ch6 = input('желаете выполнить удаление данных? (Y/N)')
    if ch6 == 'y' or ch6 == 'Y':
        str_to_find1 = input('введите строку поиска ')
        crud.row_delete(str_to_find1)
        # print('запись создана')
    else:
        print('до новых встреч')

    ch7 = input('желаете выполнить выборку данных? (Y/N)')
    if ch7 == 'y' or ch7 == 'Y':
        date_to_find1 = input('введите начальную дату ')
        date_to_find2 = input('введите конечную дату ')
        crud.row_select(date_to_find1, date_to_find2)
        # print('запись создана')
    else:
        print('до новых встреч')
