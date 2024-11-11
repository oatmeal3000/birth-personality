#coding: utf8

# 十神            0      1       2      3      4       5     6      7      8      9
ten_god_list = ["正官","偏官", "正印","偏印","正财","偏财","伤官","食神","比肩","劫财" ]


# 天干十神表
tiangan10god = [ [8,  9,  7,  6,  5, 4, 1, 0, 3, 2],
[9, 8 , 6, 7, 4, 5, 0, 1, 2, 3 ],
[3, 2, 8, 9, 7, 6, 5, 4, 1, 0],
[2, 3, 9, 8, 6, 7, 4, 5, 0, 1],
[1, 0, 3, 2, 8, 9, 7, 6, 5, 4],
[0, 1, 2, 3, 9, 8, 6, 7, 4, 5],
[5, 4, 1, 0, 3, 2, 8, 9, 7, 6],
[4, 5, 0, 1, 2, 3, 9, 8, 6, 7],
[7, 6, 5, 4, 1, 0, 3, 2, 8, 9],
[6, 7, 4, 5, 0, 1, 2, 3, 9, 8]
]


strong_table = [
[1,1,1,1,1,0,0,0,0,0,0,1],
[1,1,1,1,1,0,0,0,0,0,0,1],
[0,0,1,1,1,1,1,1,0,0,0,0],
[0,0,1,1,1,1,1,1,0,0,0,0],
[0,0,0,0,0,1,1,1,0,0,0,0],
[0,0,0,0,0,1,1,1,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,0],
[0,0,0,0,0,0,0,0,1,1,1,0],
[1,1,0,0,0,0,0,0,1,1,1,1],
[1,1,0,0,0,0,0,0,1,1,1,1]
]

 
'''
天干	通根地支
甲乙	亥子寅卯
丙丁	寅卯巳午
戊己    巳午未戌
庚辛    丑辰戌申酉
壬癸	申酉亥子
'''

tonggenTable = (
(11, 0, 2, 3), (11, 0, 2, 3),
(2, 3, 5, 6),  (2, 3, 5, 6),
(5, 6, 7, 10), (5, 6, 7, 10),
(1, 4, 10, 8, 9),(1, 4, 10, 8, 9),
(8, 9, 11, 0), (8, 9, 11, 0)
)


def is_tonggen(rigan, dizhi):
    if dizhi in tonggenTable[rigan]:
        return 1
    else:
        return 0


def is_dedi(zhiGod):
    singleone = zhiGod.split(',')
    singleone.pop(1)
    singleone = ' '.join(singleone)
    is_dedi = "印" in singleone or "比" in singleone or "劫" in singleone
    return is_dedi 

def is_deshi(ganGod, zhiGod):
    is_deshi = 0
    if "印" in zhiGod and "印" in ganGod:
        is_deshi = 1
    if ("比" in zhiGod or "劫" in zhiGod)  and ("比" in ganGod or "劫" in ganGod):
        is_deshi = 1
    if ganGod.count("印") + ganGod.count("比") + ganGod.count("劫") > 2 :
        is_deshi = 1
    return is_deshi
    

def is_deling(rigan, yuezhi):
    is_deling = is_tonggen( rigan, yuezhi )
    return is_deling

'''
def is_strong(rigan, nianzhi, yuezhi, rizhi, shizhi, ganGod, zhiGod):
    if is_deling(rigan, yuezhi) and is_dedi(zhiGod):
        return 1
    if is_deling(rigan, yuezhi) and is_deshi(ganGod,  zhiGod) :
        return 1
    if (not is_deling(rigan, yuezhi)) and is_dedi(zhiGod) and is_deshi(ganGod, zhiGod):
        return 1
    if (not is_deling(rigan, yuezhi)) and (not is_dedi(zhiGod)) :
        return 0
    if (not is_deling(rigan, yuezhi)) and is_dedi(zhiGod) and (not is_deshi(ganGod, zhiGod)):
        return 0

    return 0
'''


def is_strong(rigan, nianzhi, yuezhi, rizhi, shizhi, ganGod, zhiGod):
    singleGans = ganGod.split(',')

    if is_deling(rigan, yuezhi) and ( is_tonggen(rigan, rizhi) or is_tonggen(rigan, shizhi) ):
        return 1

    if is_deling(rigan, yuezhi) and (not is_tonggen(rigan, rizhi)) and (not is_tonggen(rigan, shizhi) ) and (not is_tonggen(rigan, nianzhi))  :
        return 0

    if is_deling(rigan, yuezhi) and (not is_tonggen(rigan, rizhi)) and (not is_tonggen(rigan, shizhi) ) and is_tonggen(rigan, nianzhi) and ("印" in singleGans[1] or "比" in singleGans[1] or "劫" in singleGans[1] or "印" in singleGans[3] or "比" in singleGans[3] or "劫" in singleGans[3]  ) :
        return 1

    if is_deling(rigan, yuezhi) and (not is_tonggen(rigan, rizhi)) and (not is_tonggen(rigan, shizhi) ) and is_tonggen(rigan, nianzhi) and not ("印" in singleGans[1] or "比" in singleGans[1] or "劫" in singleGans[1] or "印" in singleGans[3] or "比" in singleGans[3] or "劫" in singleGans[3]  ) :
        return 0

    if (not is_deling(rigan, yuezhi)) and not ( is_tonggen(rigan, rizhi) and is_tonggen(rigan, shizhi) ):
        return 0

    if (not is_deling(rigan, yuezhi)) and  is_tonggen(rigan, rizhi) and is_tonggen(rigan, shizhi) and is_tonggen(rigan, nianzhi) :
        return 1

    if (not is_deling(rigan, yuezhi)) and  is_tonggen(rigan, rizhi) and is_tonggen(rigan, shizhi) and (not is_tonggen(rigan, nianzhi)) and ( ("印" in singleGans[1] or "比" in singleGans[1] or "劫" in singleGans[1] ) and (  "印" in singleGans[3] or "比" in singleGans[3] or "劫" in singleGans[3])  ) :
        return 1

    if (not is_deling(rigan, yuezhi)) and  is_tonggen(rigan, rizhi) and is_tonggen(rigan, shizhi) and (not is_tonggen(rigan, nianzhi)) and not ( ("印" in singleGans[1] or "比" in singleGans[1] or "劫" in singleGans[1] ) and (  "印" in singleGans[3] or "比" in singleGans[3] or "劫" in singleGans[3])  ) :
        return 0



def get_10_god(tian1, tian2):
    return ten_god_list[tiangan10god[tian1][tian2]]


def get_character(ganGod, zhiGod, isStrong):
    result = ""
    if not ("正财" in ganGod or "偏财" in ganGod or "正财" in zhiGod or "偏财" in zhiGod):
        result += "金钱观念天生不强，心思也不细腻，不会精打细算，不会把精力放在财务运营上；\n不适合秘书或财务等需要心细的工作；\n父亲能够提供的帮助较少，男命容易晚婚或与妻子聚少离多。\n"
        if ("食神" in ganGod and "食神" in zhiGod or "伤官" in ganGod and "伤官" in zhiGod  or zhiGod.count("食神") + zhiGod.count("伤官")  > 2):
            result += "妥协和落地能力差。\n"
    if not ("正官" in ganGod or "偏官" in ganGod or "正官" in zhiGod or "偏官" in zhiGod):
        result += "思想和性格上有些叛逆，比起社会规则更愿意倾向自己内心的想法；\n通常事情不会想得很透，思虑也不会很重，在职场工作中比较吃亏；\n女命较难找到合适的配偶，容易晚婚；\n不在意世俗的要求，遵从自己内心的想法。\n"
    if not ("印" in ganGod or "印" in zhiGod ):
        result += "事业全靠自己，很难静下心来一步一步从基层逐步发展；\n缺乏耐力，很难在一个领域深耕发展，在看不到成绩的情况下，容易半途而废；\n情绪比较敏感，波动也比较大，喜怒形于色，容易让人一眼看明白目的和想法。\n"
    if not ("食神" in ganGod or "伤官" in ganGod or "食神" in zhiGod or "伤官" in zhiGod):
        result += "整体情绪比较平衡，不会大起大落，也不会有太多感性的一面，缺少趣味；\n对新鲜事物接受能力弱，对变化太快的事物会不太适应，处理起来思维容易一下短路；\n更喜欢稳定的工作状态，愿意在某个行业持续发展；\n思想比较传统，口才较差，适合选择不需要很多创造性，有明确制度和规章的稳定工作。\n"
    if not ("比肩" in ganGod or "劫财" in ganGod or "比肩" in zhiGod or "劫财" in zhiGod):
        result += "自主意识差，缺乏担起事的勇气和能力，适合出谋划策，提供意见。"
        if not ("财" in ganGod or "财" in zhiGod):
            result += "朋友少，易有社交恐惧。\n"

    if ("正财" in ganGod and "正财" in zhiGod)  or ("偏财" in ganGod and "偏财" in zhiGod) or zhiGod.count("正财") + zhiGod.count("偏财")  > 2 :
        if not isStrong:
            result += "物质欲望多，花费支出较大；\n感情中比较弱势，思虑过重；\n男命缺少决断，比较优柔寡断；\n体弱多病，多为慢性疾病。\n"
    if ("正官" in ganGod and "正官" in zhiGod or "偏官" in ganGod and "偏官" in zhiGod  or zhiGod.count("正官") + zhiGod.count("偏官")  > 2):
        result += "女命婚姻变动性大；\n个人容易失去自我，安全感差，性格弱势，容易思虑过重，做事停滞不前；\n为人处事比较谨慎，自尊心强，情绪多，容易过度内耗自己；\n建议多看书调整自己状态。\n"
    if ("正印" in ganGod and "正印" in zhiGod or "偏印" in ganGod and "偏印" in zhiGod  or zhiGod.count("印") > 2):
        result += "不太愿意接受变化太快的事物，适合做一些需要常年累积的工作，在已有的模式进程中慢慢耕耘；\n有固定的生活圈，喜欢按部就班，不愿意改变，讨厌突发情况；\n身材容易发福丰腴。\n"
    if ("食神" in ganGod and "食神" in zhiGod or "伤官" in ganGod and "伤官" in zhiGod  or zhiGod.count("食神") + zhiGod.count("伤官")  > 2):
        result += "注重精神世界。\n"
    if ("比肩" in ganGod and "比肩" in zhiGod or "劫财" in ganGod and "劫财" in zhiGod  or zhiGod.count("比肩") + zhiGod.count("劫财")  > 2):
        if isStrong:
            result += "容易得朋友相助，但也容易被坑；\n倾向于过度自信和武断。\n"

    return result
