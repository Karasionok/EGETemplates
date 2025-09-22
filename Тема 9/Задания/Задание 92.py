# Решение







answer = ...

#

import datetime
import hashlib
from tests.conftest import add_result
if answer is not Ellipsis:
    result = 1 if hashlib.md5(str(answer).encode()).hexdigest() == '18b8ea83d814103c4a8f379165ce9a62' else 0
    print("Верно" if result else "Неверно")
    add_result(datetime.now().timestamp(), 92, 9, result)