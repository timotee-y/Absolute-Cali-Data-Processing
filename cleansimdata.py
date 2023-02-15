import codecs, os
import bdsWeek as bw

# 输入模拟器伪距txt
# 输出频点.txt
 
def cleansim(freq):
    path = os.getcwd()
    f = codecs.open(path + '\\8332 pseudorange\\Raw\\' + freq + '.TXT', 'r')
    currentline = f.readline()
    while True:
        try:
            while currentline[0] != 'S':
                currentline = f.readline()

            while currentline[0] == 'S':
                satnum = int(currentline[1:3].strip())
                if satnum > 9:               
                    utcTOW = currentline[3:10].strip()
                    pseudorange = currentline[18:34].strip()
                else:
                    utcTOW = currentline[3:9].strip()
                    pseudorange = currentline[18:34].strip()

                if (int(float(utcTOW)) - 435822) % 30 == 0:
                    output = str(utcTOW).lstrip() + ' ' + str(satnum) + ' ' + str(pseudorange) + '\n'
                    txtname = freq + '.txt'  
                    g = codecs.open('./8332 pseudorange/' + txtname, 'a+')
                    g.write(output)
                    g.close()
                    currentline = f.readline()
                else:
                    currentline = f.readline()
        except:
            print('End of Writing for {}'.format(freq))
            break

cleansim('L1C')
cleansim('L2C')         