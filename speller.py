import argparse

n1 = ['', 'bir', 'ikki', 'üç', 'töt', 'beş', 'alte', 'yette', 'sekkiz', 'toqquz']
n2 = ['', 'on', 'yigirme', 'ottuz', 'qiriq', 'ellik', 'atmiş', 'yetmiş', 'seksen', 'toqsen']

months = ['yanvar', 'févral', 'mart', 'aprél', 'may', 'iyun', 'iyul', 'avğust', 'séntebir', 'öktebir', 'noyabir', 'dékabir']
month_durations = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def only_3_digits_to_str(n):
    if n == 0:
        return 'nöl'
    n_str = str(n)
    len_s = len(n_str)
    if len_s > 3:
        raise ValueError('more than 3 digits')

    if len_s == 1:
        result = n1[n]
    elif len_s == 2:
        result = (n2[int(n_str[0])] + ' ' + n1[int(n_str[1])]).lstrip().rstrip()
    else:
        s2 = (n2[int(n_str[1])] + ' ' + n1[int(n_str[2])]).lstrip().rstrip()

        if n_str[0] == '0':
            s1 = ''
        else:
            s1 = n1[int(n_str[0])] + ' yüz'
        result = (s1 + ' ' + s2).lstrip().rstrip()
    return result

def n_2_str(n_num):
    n_num_s = str(n_num)
    len_s = len(n_num_s)
    n = len_s
    if n > 12:
        raise ValueError('supported up to 12 digits')

    n_str = only_3_digits_to_str(int(n_num_s[-3:]))
    if n > 3:
        if n_str == 'nöl':
            n_str = ''
        thousands = only_3_digits_to_str(int(n_num_s[-6:-3]))

        if thousands == 'nöl':
            pass
        else:
            n_str = thousands + ' ming ' + n_str
    if n > 6:
        millions = only_3_digits_to_str(int(n_num_s[-9:-6]))
        if millions == 'nöl':
            pass
        else:
            n_str = millions + ' milyon ' + n_str
    if n > 9:
        billions = only_3_digits_to_str(int(n_num_s[-12:-9]))
        if billions == 'nöl':
            pass
        else:
            n_str = billions + ' milyard ' + n_str

    return n_str


def d_2_str(d):
    try:
        day_n, month_n, year_n = map(int, d.strip().split('.'))
    except ValueError as e:
        print('Invalid date, please use dd.mm.yyyy')
        exit(1)
    assert 0 < month_n <= 12, "invalid month"
    assert 0 < day_n <= month_durations[month_n-1], "invalid day"
    month_str = months[month_n-1]

    year_str = n_2_str(year_n)
    date_str = n_2_str(day_n) + ' ' + month_str + ' ' + year_str

    return date_str


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Number or date speller in Turkish')
    arg_group = parser.add_mutually_exclusive_group(required=True)
    arg_group.add_argument('-n', '--number', help='number to be spelled', type=int, dest='n')
    arg_group.add_argument('-d', '--date', help='date to be spelled, as dd.mm.yyyy', type=str, dest='d')
    args = parser.parse_args()

    if args.n:
        print(n_2_str(args.n))
    else:
        print(d_2_str(args.d))
