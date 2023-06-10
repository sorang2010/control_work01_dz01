import time


def init_db_csv(file_name='db.csv'):
    with open(file_name, 'w+', encoding='utf-8') as data:
        # data.write()
        data.close()


def row_create():
    info = []

    note_id = input('Введите номер заметки: ')
    info.append(note_id)
    title = input('Введите заголовок заметки: ')
    info.append(title)
    body_note = input('Введите текст заметки: ')
    info.append(body_note)
    date_create = time.ctime()
    info.append(date_create)

    with open('db.csv', 'a', encoding='utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')
        data.close()


def row_read():
    with open('db.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            lst_line = line.split(';')
            new_line = ''
            for l1 in lst_line:
                new_line += (l1 + ' ')
            print(new_line)
        file.close()


def row_find(str_search):
    with open('db.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if str_search in line:
                lst_line = line.split(';')
                new_line = ''
                for l1 in lst_line:
                    new_line += (l1 + ' ')
                print(new_line)

        file.close()


def row_replace(str_search, str_replace):
    with open('db.csv', 'r') as file:
        lines = file.readlines()
        file.close()
    with open('db.csv', 'w') as file1:
        for line in lines:
            # print(line)
            if str_search not in line:
                file1.write(line)
                # print(line)
            else:
                file1.write(line.replace(str_search, str_replace))
                # print(line)
        file1.close()


def row_delete(str_search):
    with open('db.csv', 'r') as file:
        lines = file.readlines()
        file.close()
    with open('db.csv', 'w') as file1:
        for line in lines:
            # print(line)
            if str_search not in line:
                file1.write(line)
                # print(line)
        file1.close()


def row_select(from_date, to_date):
    with open('db.csv', 'r') as file:
        lines = file.readlines()
        select_note = ''

        for line in lines:
            lst_line = line.split(';')
            if from_date in lst_line[3] or to_date in lst_line[3]:
                select_note += f'{lst_line[0]} {lst_line[1]} {lst_line[2]} {lst_line[3]}\n'
        print(select_note)

        file.close()
