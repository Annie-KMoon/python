from travel.thailand import *
from travel.vietnam import *

#from travel import thailand -임포트되어야 모듈위치 확인가능

thailand1()
thailand2()
vietnam1()

import inspect #모듈위치를 나타내주는 것
import random
print(1,inspect.getfile(random))

