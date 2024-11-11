from .ganzhi import *
from . import tengod

def get_emotion(digitMatrix, isStrong, tenGod1, tenGod2):
    rizhi_god = tengod.get_10_god(digitMatrix[0][2], GanInDizhi[digitMatrix[1][2]][0]) 
    yuegan_god = tengod.get_10_god(digitMatrix[0][2], digitMatrix[0][1]) 
    yuezhi_god = tengod.get_10_god(digitMatrix[0][2], GanInDizhi[digitMatrix[1][1]][0]) 
    shigan_god = tengod.get_10_god(digitMatrix[0][2], digitMatrix[0][3]) 
    rizhu = Gan[ digitMatrix[0][2] ] + Zhi[ digitMatrix[1][2] ]
    marriage_result = ""
    if "甲辰" in rizhu or "甲戌" in rizhu :
        marriage_result += "夫妻容易不和，需注意选择性格温和理性的伴侣，适宜晚婚。"
    if "丙子" in rizhu or "丙午" in rizhu or "丁丑" in rizhu or "丁未" in rizhu or "戊申" in rizhu or "戊寅" in rizhu or "辛卯" in rizhu or "辛酉" in rizhu or "壬辰" in rizhu or "壬戌" in rizhu or "癸己" in rizhu or "癸亥" in rizhu : 
        marriage_result += "恋爱早了容易分手，可待事业稳定后谨慎选择性格合适的伴侣，尽量晚婚。 "
    if tenGod1.count("伤官") + tenGod2.count("伤官") >= 3:
        marriage_result += "选择配偶方面过于挑剔，可适当放低要求条件。"




    marriage_result += "\n"
    if "正官" in rizhi_god or "正印" in rizhi_god :
        marriage_result += "女命在婚姻中容易获得幸福，追求明确，容易满足。"
    if rizhi_god == "正印":
        marriage_result += "心底好，欲望不大。"
    if isStrong and ("正官" in tenGod1 or "正官" in tenGod2 ) and ("正财" in tenGod1 or "正财" in tenGod2 or "偏财" in tenGod1 or "偏财" in tenGod2)  and not ("伤官" in tenGod1 or "伤官" in tenGod2):
        marriage_result += "女命容易遇到好的丈夫，有旺夫命。"
    if (not isStrong ) and ("正官" in tenGod1 or "正官" in tenGod2 ) and ("伤官" in tenGod1 or "伤官" in tenGod2 or "食神" in tenGod1 or "食神" in tenGod2):
        marriage_result += "女命可以获得稳定的婚姻，只是多生烦恼。"
#    if (not isStrong) and ("正官" in tenGod1 or "正官" in tenGod2 or "偏官" in tenGod1 or "偏官" in tenGod2 ) and ( "印" in tenGod1 or "印" in tenGod2 ):
#        marriage_result += "女命婚后非常幸福，同时有好的工作，丰衣足食，容易满足，野心不大，量力而行，容易获得幸福。"
    if ("正官" in tenGod1 or "正官" in tenGod2 ) and ("偏官" in tenGod1 or "偏官" in tenGod2 ) and   ( "印" in tenGod1 or "印" in tenGod2 ):  
        marriage_result += "女命可以婚姻吉祥。"
    #八字不见官杀星，但用神得力，比如身旺比劫旺而食神透，且只有一个食神，地支有比劫生食神，那么这种命婚姻都是很好的。
    if ( not ("正官" in tenGod1 or "正官" in tenGod2 or "偏官" in tenGod1 or "偏官" in tenGod2 ) ) and isStrong and tenGod1.count("食神") == 1 and ("比肩" in tenGod2 or "劫财" in tenGod2):
        marriage_result += "女命姻缘较晚，但可以婚姻如意。"
    if ( not ("正官" in tenGod1 or "正官" in tenGod2 or "偏官" in tenGod1 or "偏官" in tenGod2 ) ) and (not isStrong) and "印" in tenGod1:
        marriage_result += "女命姻缘较晚，但可以婚姻称心。"
    if tenGod1.count("食神") + tenGod1.count("伤官")+ tenGod2.count("食神") + tenGod2.count("伤官") >=3 or ( isStrong and (tenGod1.count("比肩") + tenGod1.count("劫财")+ tenGod2.count("比肩") + tenGod2.count("劫财") >=3  or  tenGod1.count("偏官") + tenGod2.count("偏官")  >=3)):
        marriage_result += "女命野心较大，不容易获得幸福，要注意控制对伴侣的言行。"

    if ("偏官" in tenGod1 or "偏官" in tenGod2 ) and ("正官" in tenGod1 or "正官" in tenGod2 ) :
        if tenGod1.count("偏官")  + tenGod2.count("偏官") >   tenGod1.count("正官")  + tenGod2.count("正官"):
            index_sha = tenGod1.find("偏官") if tenGod1.find("偏官") < tenGod2.find("偏官") else tenGod2.find("偏官")
            index_guan =tenGod1.find("正官") if tenGod1.find("正官") < tenGod2.find("正官") else tenGod2.find("正官")
            if index_sha < index_guan:
                marriage_result += "女命情感方面需坚守底线，懂得拒绝诱惑，爱惜自己，才能获得婚姻幸福。"

    if tenGod1.count("比肩") + tenGod1.count("劫财") + tenGod2.count("比肩") + tenGod2.count("劫财") >= 3 and not ("正财" in tenGod1 or "偏财" in tenGod1 or "正财" in tenGod2 or "偏财" in tenGod2 ):
        marriage_result += "女命性格比较固执、倔强、霸道冲动，自以为是，这些性格缺点都要改正，否则婚姻很难幸福。"

    if tenGod1.count("食神") + tenGod2.count("食神") > 3 or  tenGod1.count("伤官") + tenGod2.count("伤官") >= 2 or tenGod1.count("食神") + tenGod2.count("食神") +  tenGod1.count("伤官") + tenGod2.count("伤官") >= 3:
        marriage_result += "女命骄傲虚荣，对婚姻不满，没有耐心，嫌弃埋怨丈夫，需要注意自身修养，多看丈夫优点，少看缺点，减少感情摩擦，增加夫妻感情。" 

    if "伤官" in rizhi_god or "伤官" in yuegan_god or "伤官" in yuezhi_god:
        marriage_result += "女命姻缘早期不顺， 经历波折才能顺利。"
    if tenGod1.count("正财") + tenGod2.count("正财") + tenGod1.count("偏财") + tenGod2.count("偏财") >= 3 :
        marriage_result += "女命注重对方颜值，欲望大。"

    if isStrong and "正官" in rizhi_god:
        marriage_result += "女命丈夫相貌敦厚， 人品好，夫妻和睦。"
    if (not isStrong) and  "偏官" in rizhi_god:
        marriage_result += "女命容易被丈夫欺负，不可闪婚，需多观察伴侣以确定其脾气性格温和。"
    if tenGod1.count("偏官") + tenGod2.count("偏官") >= 3 :
        marriage_result += "女命容易被骗，被欺负，宜谨慎或少与不熟悉的人接触。 "
    if tenGod1.count("正官") >= 2:
        marriage_result += "女命情缘较多，婚姻决定需谨慎选择确定。 "




    marriage_result += "\n" 
    if (not isStrong) and ("偏官" in tenGod1 or "偏官" in tenGod2) and ("正官" in tenGod1 or "正官" in tenGod2) and tenGod1.count("偏官") + tenGod2.count("偏官") + tenGod1.count("正官") + tenGod2.count("正官") >= 3: 
        marriage_result += "男命有花心的迹象，需注意克制欲望。"

    if tenGod1.count("比肩") + tenGod2.count("比肩") + tenGod1.count("劫财") + tenGod2.count("劫财") >=3 :
        marriage_result += "男命脾气较急躁，需注意修身养性，降低对妻子的要求，婚姻才可长久。" 
    #日支比劫
    if "劫财" in rizhi_god or "比肩" in rizhi_god: 
        marriage_result += "男命与妻子的关系不和谐，或妻子身体容易出问题，可在保证沟通的条件下保持一定距离来调节。"
    #有财
    if tenGod1.count("偏财") + tenGod2.count("偏财") + tenGod1.count("正财") + tenGod2.count("正财") == 1 :
        marriage_result += "男命注重家庭，婚姻比较稳定。"
    ##有偏财无正财
    if ("偏财" in tenGod1 or "偏财" in tenGod2) and not ("正财" in tenGod1 or "正财" in tenGod2) :
        marriage_result += "男命与妻子感情不是很好。"
        if "偏财" in tenGod1 and "偏财" in tenGod2 :
            marriage_result += "有些花心，需注意克制欲望。"
    ##有偏财有正财
    if ("偏财" in tenGod1 or "偏财" in tenGod2) and ("正财" in tenGod1 or "正财" in tenGod2) :
        marriage_result += "男命生性风流，容易纵欲，需注意克制欲望。"
    ##有偏财有食神
    if ("偏财" in tenGod1 or "偏财" in tenGod2) and  ("食神" in tenGod1 or "食神" in tenGod2)  and not  ("伤官" in tenGod1 or "伤官" in tenGod2):
        marriage_result += "男命对待感情比较温和，保守内向一些。"
    ##有偏财有伤官
    if ("偏财" in tenGod1 or "偏财" in tenGod2) and  ("伤官" in tenGod1 or "伤官" in tenGod2)  and not ("食神" in tenGod1 or "食神" in tenGod2) :
        marriage_result += "男命对待感情容易没有分寸，对家庭伤害大，需注意自己的言行。"
        if "伤官" in rizhi_god:
            marriage_result += "男命需注意抑制婚外诱惑的影响，适宜晚婚。"
    ##有财身弱
    if ( "正财" in rizhi_god or "偏财" in rizhi_god ) and not isStrong : 
        marriage_result += "男命感情道路不太顺利，因为感情多生烦恼，要注意调整的自己的心态，用平常心对待一切，因为世间的得失皆非永恒不变。"
    if (not isStrong) and tenGod1.count("偏财") + tenGod2.count("偏财") + tenGod1.count("正财") + tenGod2.count("正财") >= 3 :
        marriage_result += "男命对妻子比较顺从，需要注意选择理性理智的对象。"
    ##有财身强
    if isStrong and tenGod1.count("偏财") + tenGod2.count("偏财") + tenGod1.count("正财") + tenGod2.count("正财") >= 3 :
        marriage_result += "男命异性缘较好， 需注意身体健康。"
    if isStrong and ("正财" in rizhi_god or "偏财" in rizhi_god) :
        marriage_result += "男命可获得妻子的帮助，获取事业上的开拓和发展。"
    #无财
    if tenGod1.count("偏财") + tenGod2.count("偏财") + tenGod1.count("正财") + tenGod2.count("正财") == 0 :
        marriage_result += "男命缺少合适的婚恋机缘，适宜晚婚，可待工作稳定后再考虑婚姻问题。"



    return marriage_result
