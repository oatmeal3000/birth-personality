import argparse
import arranger
import deducer

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
