from faker import Faker
f = Faker('zh-CN')
print(f.name())
print(f.address())
print(f.phone_number())

import jieba
result = jieba.lcut('南京市长江大桥')
print(result)

import cn2an
result = cn2an.cn2an('九千七百四十三')
print(result)