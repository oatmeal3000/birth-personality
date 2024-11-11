import sxtwl
import argparse
import collections

from . import ganzhi
from . import tengod
from . import bazitiyao
from . import mate
from . import daofa

description = '''

'''


def getWuXing(matrix_array):
    countForJin = 0
    countForMu = 0
    countForShui = 0
    countForHuo = 0
    countForTu = 0
    for num in range(len(matrix_array[0])):
        if num == 2:
            continue

        zhu_weight = 1
        if num == 0:
            zhu_weight = 0.7
        if num == 1:
            zhu_weight = 1.1
        if num == 3:
            zhu_weight = 1.1


        wuxing = ganzhi.wuxingDicForTiangan[ ganzhi.Gan[ matrix_array[0][num] ] ]
        if wuxing == "金":
            countForJin = countForJin + 50 * zhu_weight
        elif wuxing == "木":
            countForMu = countForMu + 50 * zhu_weight
        elif wuxing == "水":
            countForShui = countForShui + 50 * zhu_weight
        elif wuxing == "火":
            countForHuo = countForHuo + 50 * zhu_weight
        else:
            countForTu = countForTu + 50 * zhu_weight

    for num in range(len(matrix_array[1])):
        gan_index = 0
        zhu_weight = 1
        if num == 0:
            zhu_weight = 0.7
        if num == 1:
            zhu_weight = 1.2
        if num == 3:
            zhu_weight = 0.9

        di = ganzhi.Zhi.index( ganzhi.Zhi[ matrix_array[1][num] ] )
        for canggan in ganzhi.GanInDizhi[ di ]:
            wuxing = ganzhi.wuxingDicForTiangan[ ganzhi.Gan[canggan] ]
            if wuxing == "金":
                countForJin = countForJin + ganzhi.weightOfGan[di][gan_index]  * zhu_weight
            elif wuxing == "木":
                countForMu = countForMu + ganzhi.weightOfGan[di][gan_index] * zhu_weight
            elif wuxing == "水":
                countForShui = countForShui +  ganzhi.weightOfGan[di][gan_index] * zhu_weight
            elif wuxing == "火":
                countForHuo = countForHuo +  ganzhi.weightOfGan[di][gan_index]  * zhu_weight
            else:
                countForTu = countForTu + ganzhi.weightOfGan[di][gan_index] * zhu_weight

            gan_index += 1

    month_index =  matrix_array[1][1]
    countForJin = countForJin * ganzhi.weightOfMonth[month_index][3]
    countForMu = countForMu * ganzhi.weightOfMonth[month_index][0]
    countForShui = countForShui * ganzhi.weightOfMonth[month_index][4]
    countForHuo = countForHuo * ganzhi.weightOfMonth[month_index][1]
    countForTu = countForTu * ganzhi.weightOfMonth[month_index][2]

    sum_elements = countForJin + countForMu + countForShui + countForHuo + countForTu


    scoreForJin = int( round(countForJin / sum_elements, 2) * 100 )
    scoreForMu = int(round(countForMu / sum_elements, 2) * 100 )
    scoreForShui = int(round(countForShui / sum_elements, 2) * 100 )
    scoreForHuo = int(round(countForHuo / sum_elements, 2) * 100 )
    scoreForTu = int(round(countForTu / sum_elements, 2) * 100 )
    return (scoreForJin, scoreForMu, scoreForShui, scoreForHuo, scoreForTu)



def get_fate(input_year, input_month, input_day, input_time):
    result = ""
    Gans = collections.namedtuple("Gans", "year month day time")
    Zhis = collections.namedtuple("Zhis", "year month day time") 
    lunar = sxtwl.Lunar();
    day = lunar.getDayBySolar(
            int(input_year), int(input_month), int(input_day))
    gz = lunar.getShiGz(day.Lday2.tg, int(input_time))
    
    gans = Gans(year=ganzhi.Gan[day.Lyear2.tg], month=ganzhi.Gan[day.Lmonth2.tg], 
                day=ganzhi.Gan[day.Lday2.tg], time=ganzhi.Gan[gz.tg])
    zhis = Zhis(year=ganzhi.Zhi[day.Lyear2.dz], month=ganzhi.Zhi[day.Lmonth2.dz], 
                day=ganzhi.Zhi[day.Lday2.dz], time=ganzhi.Zhi[gz.dz]) 
    zhus = [item for item in zip(gans, zhis)]

    digitMatrix = [[-1,-1,-1,-1],[-1,-1,-1,-1]]
    for i in range(4):
        digitMatrix[0][i] =  ganzhi.Gan.index( gans[i] )
        digitMatrix[1][i] =  ganzhi.Zhi.index( zhis[i] ) 


    wuxing = getWuXing(digitMatrix)
    result += ''.join(gans) + "\n"
    result += ''.join(zhis) + "\n\n"
    result += "五行: 金%d 木%d 水%d 火%d 土%d \n" % (wuxing)
   
    result += "\n十神:\n"
    tenGod1 = ""
    for i in range(4):
        if i == 2:
            tenGod1 = tenGod1 + "日元"
        else:
            if digitMatrix[0][i] != -1:
                tenGod1 = tenGod1 + tengod.get_10_god(digitMatrix[0][2], digitMatrix[0][i])
        tenGod1 = tenGod1 + ",\t\t"

    tenGod2 = ""
    for i in range(4):
        if digitMatrix[1][i] != -1:
            for dizhigan in ganzhi.GanInDizhi[digitMatrix[1][i]]:
                tenGod2 = tenGod2 + tengod.get_10_god(digitMatrix[0][2], dizhigan) 
            tenGod2 = tenGod2 + ",\t"

    tenGod2 = tenGod2 + "\n"
    result += tenGod1 + "\n"
    result += tenGod2 + "\n"

#    isStrong = tengod.is_strong(digitMatrix[0][2], digitMatrix[1][0],digitMatrix[1][1],digitMatrix[1][2], digitMatrix[1][3], tenGod1, tenGod2)
#    if isStrong:
#        result += "日元强\n"
#    else:
#        result += "日元弱\n"

    destiny = bazitiyao.get_destiny(digitMatrix)
    result += destiny + "\n"
    result += "\n"

    significance = sorted(wuxing, reverse=True)
    significant_index1 = wuxing.index(significance[0])
    my_daofa = daofa.get_daofa(digitMatrix[0][2], significant_index1)
    result += "十神中的 "
    result += daofa.daofa_name[my_daofa]
    result += " 力量强\n\n"
    if my_daofa == 0 or my_daofa == 1:
        isStrong = 1
    else:
        isStrong = 0

    significant_index2 = wuxing.index(significance[1])
    in_need = daofa.get_in_need(digitMatrix[0][2], isStrong, wuxing)
 

    character = tengod.get_character(tenGod1, tenGod2, isStrong)
    result += character + "\n"
    marriage = mate.get_emotion(digitMatrix, isStrong, tenGod1, tenGod2)
    result += marriage + "\n\n"


    profession1 = daofa.get_preferrence(my_daofa,  in_need) 
    result += profession1 
    if significance[1] >= 30:
        profession2 = daofa.get_preferrence(daofa.get_daofa(digitMatrix[0][2], significant_index2), in_need) 
        result += profession2 
    

    cai = daofa.get_element(digitMatrix[0][2], 3) 
    guan = daofa.get_element(digitMatrix[0][2], 4) 
    yin = daofa.get_element(digitMatrix[0][2], 1) 
    shishang = daofa.get_element(digitMatrix[0][2], 2) 

    result += "\n读博士需要十神中的财弱，印重，有食伤："
    if wuxing[cai] < 20 and wuxing[yin] > 20 and wuxing[shishang] > 0 :
        result += "性格适合读博士。\n"
    else:
        if wuxing[cai] >= 20:
            result += "容易被他人所影响而难于专心学术研究，科研意志不太坚定。"
        if wuxing[yin] <= 20:
            result += "不太喜欢安稳，不能忍受清贫的生活。"
        if wuxing[shishang] == 0:
            result += "创造性和表达力不足。"
 
        result += "性格不太适合读博士。\n"


    return result 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('year', action="store", help=u'year')
    parser.add_argument('month', action="store", help=u'month')
    parser.add_argument('day', action="store", help=u'day')
    parser.add_argument('time', action="store", help=u'time')
    options = parser.parse_args()
  
    result = get_fate(options.year, options.month, options.day, options.time)
    print(result)
    
