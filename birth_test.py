from birth_secret import birth_main
from ziweidoushu import arranger
from ziweidoushu import deducer 
import argparse


description=''
parser = argparse.ArgumentParser(description=description,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('year', action="store", help=u'year')
parser.add_argument('month', action="store", help=u'month')
parser.add_argument('day', action="store", help=u'day')
parser.add_argument('time', action="store", help=u'time')
options = parser.parse_args()
  
a = arranger.Arranger()
output_json = a.arrange(int(options.year), int(options.month), int(options.day), int(options.time))  
#print(output_json)

d = deducer.Deducer(output_json)
fate_result = d.deduce()
print(fate_result)

profession_result = birth_main.get_fate(options.year, options.month, options.day, options.time)
print(profession_result)
