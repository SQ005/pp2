#1///

import re
import codecs
file = codecs.open('row.txt', 'r', 'utf-8')
pattern = "а.*б"
x = re.search(pattern, file)





print(x)
