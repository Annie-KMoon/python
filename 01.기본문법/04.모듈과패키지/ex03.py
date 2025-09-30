import travel.thailand as tt , travel.vietnam as tv

tt.thailand1()
tv.vietnam1()

import inspect #모듈위치를 나타내주는 것
import random
print(1,inspect.getfile(random))
print(2,inspect.getfile(tt))