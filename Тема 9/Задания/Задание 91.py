# Решение







answer = ...

#

import datetime
import hashlib
from tests.conftest import add_result
if answer is not Ellipsis:
    result = 1 if hashlib.md5(str(answer).encode()).hexdigest() == '905056c1ac1dad141560467e0a99e1cf' else 0
    print("Верно" if result else "Неверно")