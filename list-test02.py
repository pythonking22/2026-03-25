#로또번호생성-난수
mylotto = []

import random
r=random.randint(1,45)
if r not in mylotto:
    mylotto.append(r)
r=random.randint(1,45)
if r not in mylotto:
    mylotto.append(r)
r=random.randint(1,45)
if r not in mylotto:
    mylotto.append(r)
r=random.randint(1,45)
if r not in mylotto:
    mylotto.append(r)
r=random.randint(1,45)
if r not in mylotto:
    mylotto.append(r)
r=random.randint(1,45)
if r not in mylotto:
    mylotto.append(r)
    
print(mylotto)