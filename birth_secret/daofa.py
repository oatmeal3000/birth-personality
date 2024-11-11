#coding:utf8

'''
财 3, 官 4, 印 1, 比劫 0, 食伤 2 
'''
daofa_name = ['比劫', '印', '食伤', '财', '官']

''' 金  木  水  火  土
甲  4   0   1   2   3 
乙  4   0   1   2   3
丙  3   1   4   0   2
丁  3   1   4   0   2
戊  2   4   3   1   0
己  2   4   3   1   0
庚  0   3   2   4   1
辛  0   3   2   4   1
壬  1   2   0   3   4
癸  1   2   0   3   4
'''

daofa_table=(
(  4 ,  0 ,  1 ,  2 ,  3  ),
(  4 ,  0 ,  1 ,  2 ,  3  ),
(  3 ,  1 ,  4 ,  0 ,  2  ),
(  3 ,  1 ,  4 ,  0 ,  2  ),
(  2 ,  4 ,  3 ,  1 ,  0  ),
(  2 ,  4 ,  3 ,  1 ,  0  ), 
(  0 ,  3 ,  2 ,  4 ,  1  ),
(  0 ,  3 ,  2 ,  4 ,  1  ),
(  1 ,  2 ,  0 ,  3 ,  4  ),
(  1 ,  2 ,  0 ,  3 ,  4  )

)


def get_element(riyuan, my_daofa):
    return daofa_table[riyuan].index( my_daofa )


def get_daofa(riyuan, element):
    return daofa_table[riyuan][element]



def get_in_need(riyuan, isStrong, wuxing):
    if isStrong: #补 财3 官4 食伤2
        element_cai = daofa_table[riyuan].index(3)
        element_guan = daofa_table[riyuan].index(4)
        element_shi = daofa_table[riyuan].index(2)
        elements = [wuxing[element_cai], wuxing[element_guan], wuxing[element_shi]]
        if wuxing[element_cai] == max(elements):
            return daofa_table[riyuan][element_cai]
        if wuxing[element_guan] == max(elements):
            return daofa_table[riyuan][element_guan]
        if wuxing[element_shi] == max(elements):
            return daofa_table[riyuan][element_shi]


    else: # 补  比劫0 印1
        element_bi = daofa_table[riyuan].index(0)
        element_yin = daofa_table[riyuan].index(1)
        if wuxing[element_bi] >  wuxing[element_yin]:
            return daofa_table[riyuan][element_bi]
        else:
            return daofa_table[riyuan][element_yin]

    return need_daofa




profession = (
        ( ''' ''', ''' ''', '''
比劫配食伤的人，虽然也是比劫性格，但是由于食伤的配合，会变得更加率直，专注于自己的发挥而不是管理他人。
表现为具有不错的专业实力 + 很强的输出能力，工作表现通常不错。
学习和接受新鲜事物的能力非常强，对于变化快的市场，有自己独特的见解，擅长快速切入全新的领域。
做人风格直来直往，自信率直，情绪强烈，感染力强，并用自己的输出能力去影响别人。
本格局可以从非物质的事物上获得很强的愉悦感，比如某种专业技艺的享受与精进，或某种精神领域的执着，能不断完善自己的专业追求并强力输出去影响他人，财富也会因此而来。
适合职业有：创业者，运动员，设计师，演员等
''', '''
比劫配财的人，往往将自信表现在社交方面，非常有人气，能够在人群中吸引别人信任、追随自己。
朋友多，人脉广，善于跟别人交流合作，达成信息整合、利益互换，收获良好回报；能体察别人的需求，可以hold住比较复杂的人际关系。
对信息、数据、金钱财物的敏锐嗅觉，能从大量信息交换与流通中提取价值，比他人更先发现赚钱的机会。
相对其它格局来说，销售能力出众得多，能搞定各类客户，善于把握市场方向和节奏，在揣摩市场需求方面有自己独到的见解，懂得打信息差，什么时候做什么事，能够利用营销方式广泛连接资源，创造财富产出。
适合职业有：销售，贸易，自营生意人，外交，商务等
'''
,
        '''
比劫配官杀的人，首先具备极强的比劫特征，同时有夹杂着官杀的优点，往往表现为有野心有欲望，也有强大的心理素质与意志，敢扛敢干，抗压能力强力争上游，在团体中可以产生不小的影响力。
做事居安思危，目光长远，善于分解复杂事件与目标，有不错的规划与组织管理能力。
相对其它格局来说有天生的领袖气场，适合创造不可替代的业务价值，能在顺境不受诱惑坚持正确的方向。
事业的发展上很少依靠运气和随机性，而是从零开始规划构建事业王国，在远景追求上，有句名言“人生除了生死都是擦伤”，很适合形容此格局的磅礴心力。
适合职业有：企业领导，创业者，军人
''' )
, (''' ''', ''' ''', '''
印的淡定从容配上食伤的创造性，是非常容易出艺术家的组合。表现为抗压能力强，心志稳定，一旦专注进入工作状态，雷打不动。
能够参与需要漫长回报期的项目和目标，可以坚持到最后等来胜利；不会轻易被他人情绪或意外事件所影响。
不喜参与人事斗争，团队中容易受人信赖，给人以信赖和安心的感觉。
专业技艺能力强，富于才华和表现力，通常有自己热爱和精专的领域，在这方面是有非常纯粹的追求的。
经常能提出创新型解决思路，相对其它格局来说，是稳定大气但又不失开放灵活，适合从专业技术或技艺才艺上获得财富的回报与来源。
适合职业有：科研工作者，教育从业者，医生，工程师，宗教学者，程序员等
''', '''
印的宽容善良加上财的善解人意，这种组合是沟通天才，最容易出暖男暖女。
在人际交往中是很有自己的方式方法的，善于在跟别人的交流合作中，达成信息整合、利益互换，收获良好回报，也能协助团队达成各种形式的沟通合作。
心思细腻，善于体察别人的需求，有同理心，考虑周全，是一个愿意为了大家付出的人；虽然有时也会在人际上敏感纠结，但影响不大。
相对其它格局来说，懂得做事和做人之间的微妙平衡，善于在复杂的职场环境中平衡各方利益，以盘活事业和工作上的各种资源，发现新的财富机会。
适合职业有：财务，运营，经纪人
''', '''
印配官杀的人往往有耐心，沉得住气，适合参与需要漫长回报期的项目和目标。
抗压能力强，遇事沉着冷静，喜怒不形于色，不会轻易将私人情绪带进工作之中。
团队中容易受人信赖，给人以信任和安心的感觉，可以为了目标理智控制自己的行为，是一个靠谱有责任心的人。
工作中能够对自己提出要求，对工作结果很重视，能够在规则内步步扎实，稳定推进项目发展。
善于思考总结，有一定方法论以及不错的目标规划与组织管理能力，能井井有条地安排事情并达成良好工作目标，获得领导同事的信赖，交付重要工作。
适合职业有：行政，学者，公务员等
'''),
('''
食伤配比劫的人，往往具备强烈的好奇心和求知欲，对新兴行业或新生事物的敏感度高。专业技艺能力强，富于才华和表现力。
点子多，直觉准，反应迅速，总能灵光乍现解决问题，时常有出奇制胜、四两拨千斤的奇招。
有野心有欲望，敢扛敢干，力争上游，输出能力强，在团队中有很强的情绪感染力，能打鸡血，头脑风暴中经常有好的创意。
工作上只要确定目标后会非常坚定，加之干劲十足，不畏挫折，可以用强大的行动力迅速突破局面，经常在工作快速切入的初期打开局面，非常适合创意破局。
适合职业有：创作设计，营销推广，演说家，自由职业，演员等
''', '''
食伤配印的人是最具才华的，能最大程度的发挥自己的专业知识。
对新兴行业或新生事物的敏感度高，对市场变化有自己独特的见解，能较快的切入新领域。
输出能力强，善于表达，工作中相对专注，有耐心，沉得住气，能够参与需要漫长回报期的项目，锚定航道后基本不会偏离目标。
因性格热情开朗，对人真诚，团队中容易受人喜好，会给人灵动和聪明的感觉，可以成为团队中出色的智多星。
相对其它格局来说，善于沟通，温和有才华，容易被领导前辈赏识，获得额外的发展空间和提携机会。
适合职业有：宣传设计，新闻媒体，艺术创作，咨询师，建筑师，摄影师等
''', ''' ''', ''' ''' , ''' ''' ), 
('''
财配比劫的人对信息、数据、金钱财物的嗅觉敏锐，能比他人更先发现赚钱的机会，善于在信息整合与利益互换中收获良好回报。
心思细腻，能够体察别人的需求，有同理心，考虑周全，但同时也力争上游，享受竞争的感觉，可以快速在团体中展现自己的价值。
能够在相对复杂的团队配合中，做到很好的配合协调，也能通过沟通协调，处理较为复杂的人际关系。
相对其它格局来说，很懂得量力而行的技巧，能够该妥协的时候妥协，该强硬的时候知道分寸，擅长把握市场动态，利用信息不对称收获意料之外的财务回报。
适合职业有：商人，销售，证券从业者
''', '''
财配印的人心思细腻，善于体察别人的需求，有同理心，考虑周全，是一个愿意为了大家付出的人。
情感共鸣方面很强大，情商高，能够观察到他人的情绪并及时照顾到地方，虽然有时也会在人际和琐事上敏感纠结，但并不影响他们独有的人格魅力。
在相对复杂的团队配合中，是很有自己的方式方法的，可以做到很好的配合协调。
相对其它格局来说，做事不冲，个性温和，善于缓解团队竞争的紧张气氛，容易受到年长领导的关照与帮助。能够因为广结善缘，收获到各种的财富事业回报。
适合职业有：市场运营，财务会计，经纪人，行政文秘
''', ''' ''' , ''' ''', ''' '''), 
('''
官杀配比劫的人，工作上只要确定目标后会非常坚定，加之干劲十足，不畏挫折。
自身很有目标感，会对自己和他人不断提出更高的要求，所以会精益求精，不断完善自己的行为，对工作结果很重视。
相对其它格局来说，能够非常得力地安排并完成工作任务，无论是个人还是带团队，推进效率都很高。
作为下属，善于快速帮领导解决问题，办事靠谱；作为管理者，公私分明，赏罚得当。
在相对成熟的企业平台环境中，因为有明确规范的上升路径，可以凭借自己的努力和吃苦精神，获得稳定的成长与发展。
适合职业有：企业中层，国企，司法从业者，审计风控等
''', '''
官杀配印的人，在工作中既有野心也能沉得住气，适合一步一步稳定发展。
工作中有目标感，会对自己不断提出更高的要求，对上级的方案执行度会认真执行并落实。
遇到问题能反思，从而不断改进自己的工作结构，深受领导器重，非常适合在国企，央企这种大公司上班。
相对其它格局来说，能够在复杂的信息中看穿问题的本质，经常作为一个靠谱军师角色受到领导看重；因为守＞攻，也很适合在稳定成熟的大平台环境里，经营自己的一席之地，获得稳固发展。
适合职业有：企业管理层，学者，公务员
''', ''' ''', ''' ''', ''' '''
)

)

def get_preferrence(most, need):
    return profession[most][need];

