# Преобразование числа в список
def num2arr(num):
    if num == 0:
        return [0]
    arr = []
    while num != 0:
        arr.append(num % 10)
        num = num // 10
    arr.reverse()
    return arr


# Преобразование списка в число
def arr2num(number_list):
    res = 0
    deg = len(number_list) - 1
    for numeral in number_list:
        res += numeral * (10 ** deg)
        deg -= 1
    return res


# Проверка, является ли данное число Капрекаровым
def kaprekar(number_list, base):
    mask = []
    mask.extend(number_list)
    num = arr2num(number_list)
    mask.sort(reverse=True)
    num1 = mask
    num2 = []
    num2.extend(num1)
    num2.reverse()
    if base_residual(num1, num2, base) == num:
        return 1
    else:
        return 0


# Разность с учётом системы счисления (ВАЖНО - num1 по умолчанию меньше num2)
def base_residual(num1, num2, base):
    i = len(num1) - 1
    if i == 0:
        return num1[i] - num2[i]
    ans = []
    while i >= 0:
        if num1[i] < num2[i]:
            tmp_res = num1[i] + base - num2[i]
            num1[i - 1] -= 1
        else:
            tmp_res = num1[i] - num2[i]
        ans.append(tmp_res)
        i -= 1
    ans.reverse()
    ans = arr2num(ans)
    return ans


# Перевод числа из десятичной системы счисления в произвольную
def dec2base(dec, base):
    if base == 10:
        return dec
    num = []
    while dec > 0:
        num.append(dec % base)
        dec //= base
    num.reverse()
    num = arr2num(num)
    return num


# Преобразование списка в строку
def arr2str(number_list):
    number_line = ''
    for number in number_list:
        number_line += str(number)
    return number_line


# Погнали
def run():
    base_list = list(range(2, 11))
    for base in base_list:
        print('Система счисления:', base)
        number = 0
        output_list = ['0']
        while True:
            tmp_number = dec2base(number, base)
            number_list = num2arr(tmp_number)
            tmp_len = len(number_list)
            cur_len = tmp_len
            flag = 0
            while cur_len <= 6:
                if flag == 1:
                    number_list.reverse()
                    number_list.append(0)
                    number_list.reverse()
                cur_len = len(number_list)
                if kaprekar(number_list, base) == 1 and tmp_number != 0:
                    output_list.append(arr2str(number_list))
                flag = 1
            if tmp_len > 6:
                break
            number += 1
        prev_len = 0
        for unit in output_list:
            length = len(unit)
            if prev_len != length:
                print('    Количество цифр:', length)
            print('       ',unit)
            prev_len = length


run()
