def find_common_participants(a, b, sep=','):
    set_1 = set(a.split(sep))
    set_2 = set(b.split(sep))

    return list(set_1.intersection(set_2))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, sep='|'))
