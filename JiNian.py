from webbrowser import Error

def str_to_num(a:str):
    n = int(a)
    return n

def gan(n):
    if n >10 or n < 1:
        return Error
    elif n == 1:
        gan = "甲"
    elif n == 2:
        gan ="乙"
    elif n == 3:
        gan = "丙"
    elif n == 4:
        gan = "订"
    elif n == 5:
        gan = "戊"
    elif n == 6:
        gan = "己"
    elif n == 7:
        gan = "庚"
    elif n == 8:
        gan = "辛"
    elif n == 9:
        gan = "壬"
    elif n == 10:
        gan = "癸"
    return gan

def gan_fan(gan):
    if gan == "甲":
        n = 1
    elif gan == "乙":
        n = 2
    elif gan == "丙":
        n = 3
    elif gan == "丁":
        n = 4
    elif gan == "戊":
        n = 5
    elif gan == "己":
        n = 6
    elif gan == "庚":
        n = 7
    elif gan == "辛":
        n = 8
    elif gan == "壬":
        n = 9
    elif gan == "癸":
        n = 10
    return n

def zhi(n):
    if n > 12 or n < 0:
        return Error
    elif n == 1:
        zhi = "寅"
    elif n == 2:
        zhi = "卯"
    elif n == 3:
        zhi = "辰"
    elif n == 4:
        zhi = "巳"
    elif n == 5:
        zhi = "午"
    elif n == 6:
        zhi = "未"
    elif n == 7:
        zhi = "申"
    elif n == 8:
        zhi = "酉"
    elif n == 9:
        zhi = "戌"
    elif n == 10:
        zhi = "亥"
    elif n == 11:
        zhi = "子"
    elif n == 12:
        zhi = "丑"
    elif n == 0:
        zhi = "丑"
    return zhi

def nian_gan(year:str):
    a = int(year[3])
    if a > 3:
        n = a -3
    elif a <= 3 :
        n = a + 10 - 3
    x = gan(n)
    return x

def nian_zhi(year:int):
    n = (year + 7) % 12
    x = zhi(n)
    return x

def shi_ji_chang_shu(year)-> str :
    c = int(year[0] + year[1]) + 1
    x1 = 44 * (c - 17) + (c-17) // 4 + 3
    x = x1 % 60
    return x

def run_nian(year_num) -> int:
    if year_num % 100 == 0:
        if year_num % 400 == 0:
            year_feb = 29
        else:
            year_feb = 28
    else:
        if year_num % 4 == 0:
            year_feb = 29
        else:
            year_feb = 28
    if year_feb == 29:
        return True
    else:
        return False


def rizhu(year,month, day) -> str :
    if int(month) == 1:
        m = 0
    elif int(month) == 2:
        m = 31
    elif int(month) == 3:
        m = 0 - 1
    elif int(month) == 4:
        m = 30
    elif int(month) == 5:
        m = 0
    elif int(month) == 6:
        m = 31
    elif int(month) == 7:
        m = 1
    elif int(month) == 8:
        m = 32
    elif int(month) == 9:
        m = 3
    elif int(month) == 10:
        m = 33
    elif int(month) == 11:
        m = 4
    elif int(month) == 12:
        m = 34
    s = int(year[2] + year[3]) - 1
    n = s // 4
    u = s % 4
    d = int(day)
    x = shi_ji_chang_shu(year)
    r = n * 6 + 5 * (n*3 +u) + m + d + x
    year_num = int(year)
    if run_nian(year_num) is True and int(month) > 2:
        r = r+1

    xu = r % 60
    return xu

gan_zhi_biao = {1:"甲子", 2:"乙丑", 3:"丙寅" ,4: "丁卯", 5:"戊辰", 6:"己巳", 7:"庚午", 8:"辛未", 9:"壬申", 10:"癸酉",
                11:"甲戌", 12:"乙亥", 13:"丙子", 14:"丁丑", 15:"戊寅", 16:"己卯", 17:"庚辰", 18:"辛巳", 19:"壬午", 20:"癸未",
                21:"甲申", 22:"乙酉", 23:"丙戌", 24:"丁亥", 25:"戊子", 26:"己丑", 27:"庚寅", 28:"辛卯", 29:"壬辰", 30:"癸巳",
                31:"甲午", 32:"乙未", 33:"丙申", 34:"丁酉", 35:"戊戌", 36:"己亥", 37:"庚子", 38:"辛丑", 39:"壬寅", 40:"癸卯",
                41:"甲辰", 42:"乙巳", 43:"丙午", 44:"丁未", 45:"戊申", 46:"己酉", 47:"庚戌", 48:"辛亥", 49:"壬子", 50:"癸丑",
                51:"甲寅", 52:"乙卯", 53:"丙辰", 54:"丁巳", 55:"戊午", 56:"己未", 57:"庚申", 58:"辛寅", 59:"壬戌", 60:"癸亥"}
def main():
    date = input("输入年月日时以以下格式：yyyy/mm/dd/hh:mm: ")
    date_list = date.split("/")

    year = date_list[0]
    month = date_list[1]
    day = date_list[2]
    time = date_list[3]
    time_list = time.split(":")
    hour = time_list[0]
    minute = time_list[1]

    year_num = str_to_num(year)
    if year_num % 100 == 0:
        if year_num % 400 == 0:
            year_feb = 29
        else:
            year_feb = 28
    else:
        if year_num % 4 == 0:
            year_feb = 29
        else:
            year_feb = 28


    month_num = str_to_num(month) -1
    while month_num < 1 or month_num > 12:
        month_num = input("月份错误！！！重新输入月份以以下格式：mm: ")
        month = str(month_num)

    day_num = str_to_num(day)
    if month_num == 1 or month_num == 3 or month_num == 5 or month_num == 7 or month_num == 8 or month == 10 or month_num == 12:
        while day_num < 1 or day_num > 31:
            day_num = input("日期错误！！！重新输入日期以以下格式：dd: ")
    elif month_num == 4 or month_num == 6 or month_num == 9 or month_num == 11:
        while day_num < 1 or day_num > 30:
            day_num = input("日期错误！！！重新输入日期以以下格式：dd: ")
    elif month_num == 2:
        if year_feb == 28:
            while day_num < 1 or day_num >28:
                day_num = input("日期错误！！！重新输入日期以以下格式：dd: ")
        elif year_feb == 29:
            while day_num < 1 or day_num > 29:
                day_num = input("日期错误！！！重新输入日期以以下格式：dd: ")

    hour_num = str_to_num(hour)
    minute_num = str_to_num(minute)

    nian1 = nian_gan(year)
    nian2 = nian_zhi(year_num)
    j_nian = nian1 + nian2

    yue2 = zhi(month_num)
    yue1 = gan_fan(nian1) * 2 + (month_num)
    if yue1 > 10:
        yue1 = yue1 - 10
    yue_gan = gan(yue1)
    j_yue = yue_gan+yue2

    #纪日
    ri1= rizhu(year,month,day)
    j_ri = gan_zhi_biao[ri1]

    #纪时
    if hour_num % 2 == 0:
        shi_zhi = hour_num/2 - 1
    else:
        shi_zhi = (hour_num + 1)/2 -1
    if shi_zhi == -1:
        shi2 = "子"
    else:
        shi2 = zhi(shi_zhi)
    shi_gan = gan_fan(j_ri[0]) *2 +shi_zhi
    while shi_gan > 10:
        shi_gan = shi_gan - 10
    shi1 = gan(shi_gan)
    j_shi = shi1 + shi2


    return print(f"{j_nian} 年 {j_yue} 月 {j_ri} 日 {j_shi} 时")

main()


