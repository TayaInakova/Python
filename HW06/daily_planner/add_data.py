def add_new_data(data):
    a = input(
        'Выберите день недели, в который хотите внести новую запись: \n'
        'Понедельник - 1\n Вторник - 2\n Среда - 3\n Четверг - 4\n '
        'Пятница - 5\n Суббота - 6\n Воскресенье - 7\n')
    try:
        a = int(a)
    except Exception:
        print('Ни один день не выбран.')
        print()
    day_choice = ['Понедельник:\n', 'Вторник:\n', 'Среда:\n', 'Четверг:\n', 'Пятница:\n', 'Суббота:\n',
                  'Воскресенье:\n']
    if a <= len(day_choice):
        data[day_choice[a - 1]].append(input('Введите время новой записи (чч:мм): ') + ' ' +
                                       input('Введите содержание новой записи: ') + '\n')
        data[day_choice[a - 1]].sort()
        print()
        _ = input('Введите любой символ для возвращения в меню: ')
    else:
        print('Выход')
    return data