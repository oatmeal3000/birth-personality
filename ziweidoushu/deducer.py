import json

#with open('output.json','r',encoding='utf8') as fp:
#    star_data = json.load(fp)
#    print('data in json ',star_data)

class Deducer():
    def __init__(self, star_json):
        self.star_plate = star_json

    def deduce(self):
        with open('./starlist.json','r',encoding='utf8') as fp:
            fate_data = json.load(fp)

        final_result = ""
        for key, value in self.star_plate.items():
            if key == "身宫":
                final_result += "身宫在" + value + ": " + fate_data["身"][value] + "\n"
            elif key != "五行局":
                GongWei = value["宫位"] 
                ZhuXingList = value["主星"]
                JiXingList = value["吉星"]
                ShaXingList = value["煞星"]
                ZaYaoList = value["杂曜"]
                for item in ZhuXingList:  #主星名称
                    final_result += item[0] + "在" + GongWei + ": " + fate_data[ item[0] ][GongWei] + "\n"
                    if item[2] != "":
                        final_result += item[2] + "在" + GongWei + ": " + fate_data[ item[2] ][GongWei] + "\n"
                for item in JiXingList:  
                    final_result += item[0] + "在" + GongWei + ": " + fate_data[ item[0] ][GongWei] + "\n"
                    if item[2] != "":
                        final_result += item[2] + "在" + GongWei + ": " + fate_data[ item[2] ][GongWei] + "\n"
                for item in ShaXingList: 
                    final_result += item[0] + "在" + GongWei + ": " + fate_data[ item[0] ][GongWei] + "\n"
                    if item[2] != "":
                        final_result += item[2] + "在" + GongWei + ": " + fate_data[ item[2] ][GongWei] + "\n"

        
#        print(final_result)
        return final_result
         

