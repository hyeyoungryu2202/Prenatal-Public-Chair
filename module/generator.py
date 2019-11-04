#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import urllib
from hangul import Barcode

reload(sys)
sys.setdefaultencoding('utf8')

raw_name = raw_input(u"이름을 입력하세요 :")
raw_birthday = raw_input(u"생년월일을 입력하세요 (예: 94115): ").encode("utf-8")
raw_lucky = raw_input(u"0부터 9 중에서 좋아하는 숫자를 입력하세요: ").encode("utf-8")

name = raw_name.decode("utf-8")
birthday = raw_birthday.decode("utf-8")
lucky = raw_lucky.decode("utf-8")

new_user = Users(name,birthday,lucky)

new_id = new_user.coding(name,birthday,lucky)
print new_id

barcode_url = "http://api-bwipjs.rhcloud.com/?bcid=ean13&text=" + str(new_id)

print barcode_url
urllib.urlretrieve(barcode_url, "test")




