import sxtwl
import argparse
import collections

import tengod
import bazitiyao

description = '''

'''
#天干 0     1    2    3    4    5    6    7    8    9
Gan=['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
#地支 0     1    2    3    4    5    6    7    8    9   10   11
Zhi=['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']


wuxingDicForTiangan = {
    "甲": "木",
    "乙": "木",
    "丙": "火",
    "丁": "火",
    "戊": "土",
    "己": "土",
    "庚": "金",
    "辛": "金",
    "壬": "水",
    "癸": "水"
}

wuxingDicForDizhi = {
    "子": "水",
    "丑": "土",
    "寅": "木",
    "卯": "木",
    "辰": "土",
    "巳": "火",
    "午": "火",
    "未": "土",
    "申": "金",
    "酉": "金",
    "戌": "土",
    "亥": "水"
}

GanInDizhi = [(9, ), (5, 9, 7), (0, 2,4), (1, ), (4, 1, 9), (2, 6, 4), (3, 5), (5, 3, 1), (6, 8, 4), (7, ), (4,7,3), (8, 0)]


def getWuXing(zhus):
    wuxingList = []
    countForJin = 0
    countForMu = 0
    countForShui = 0
    countForHuo = 0
    countForTu = 0
    for bazi in zhus:
        wuxingList.append(wuxingDicForTiangan[bazi[0]])
        wuxingList.append(wuxingDicForDizhi[bazi[1]])
    for wuxing in wuxingList:
        if wuxing == "金":
            countForJin = countForJin + 1
        elif wuxing == "木":
            countForMu = countForMu + 1
        elif wuxing == "水":
            countForShui = countForShui + 1
        elif wuxing == "火":
            countForHuo = countForHuo + 1
        else:
            countForTu = countForTu + 1
    scoreForJin = round(countForJin / 8, 2)
    scoreForMu = round(countForMu / 8, 2)
    scoreForShui = round(countForShui / 8, 2)
    scoreForHuo = round(countForHuo / 8, 2)
    scoreForTu = round(countForTu / 8, 2)
    return (scoreForJin, scoreForMu, scoreForShui, scoreForHuo, scoreForTu)


def main():
    parser = argparse.ArgumentParser(description=description,
                                 formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('year', action="store", help=u'year')
    parser.add_argument('month', action="store", help=u'month')
    parser.add_argument('day', action="store", help=u'day')
    parser.add_argument('time', action="store", help=u'time')
    options = parser.parse_args()
   
    Gans = collections.namedtuple("Gans", "year month day time")
    Zhis = collections.namedtuple("Zhis", "year month day time") 
    lunar = sxtwl.Lunar();
    day = lunar.getDayBySolar(
            int(options.year), int(options.month), int(options.day))
    gz = lunar.getShiGz(day.Lday2.tg, int(options.time))
    gans = Gans(year=Gan[day.Lyear2.tg], month=Gan[day.Lmonth2.tg], 
                day=Gan[day.Lday2.tg], time=Gan[gz.tg])
    zhis = Zhis(year=Zhi[day.Lyear2.dz], month=Zhi[day.Lmonth2.dz], 
                day=Zhi[day.Lday2.dz], time=Zhi[gz.dz]) 
    zhus = [item for item in zip(gans, zhis)]
    wuxing = getWuXing(zhus)
    print(gans)
    print(zhis)
    print("五行: 金 %.2f, 木 %.2f, 水 %.2f, 火 %.2f, 土 %.2f" % (wuxing))
   
    digitMatrix = [[-1,-1,-1,-1],[-1,-1,-1,-1]]
    tenGod1 = "十神:\n"
    for i in range(4):
        digitMatrix[0][i] =  Gan.index( gans[i] )
        digitMatrix[1][i] =  Zhi.index( zhis[i] ) 

    for i in range(4):
        if i == 2:
            tenGod1 = tenGod1 + "日元"
        else:
            if digitMatrix[0][i] != -1:
                tenGod1 = tenGod1 + tengod.get_10_god(digitMatrix[0][2], digitMatrix[0][i])
        tenGod1 = tenGod1 + ",\t"

    tenGod2 = ""
    for i in range(4):
        if digitMatrix[1][i] != -1:
            tenGod2 = tenGod2 + tengod.get_10_god(digitMatrix[0][2], GanInDizhi[digitMatrix[1][i]][0]) 

            tenGod2 = tenGod2 + ",\t"

    tenGod2 = tenGod2 + "\n"
    print(tenGod1)
    print(tenGod2)

    isStrong = tengod.is_strong(digitMatrix[0][2], digitMatrix[1][1])
    character = tengod.get_character(tenGod1, tenGod2, isStrong)
    print(character)
    destiny = bazitiyao.get_destiny(digitMatrix)
    print(destiny)


if __name__ == '__main__':
    main()
    
