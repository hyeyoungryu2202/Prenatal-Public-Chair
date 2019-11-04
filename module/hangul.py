#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Barcode:
  
  def __init__(self,name,birthday,lucky):
    
    self.name = name
    self.birthday = birthday
    self.lucky = lucky

  def coding(self, name, birthday,lucky):
    
    
  
  # 한글을 초성, 중성, 종성으로 분리하기.
  
  
   
  # 유니코드 한글 시작 : 44032, 끝 : 55199
    BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

  # 초성 리스트. 00 ~ 18
    CHOSUNG_LIST = [u'ㄱ', u'ㄲ', u'ㄴ', u'ㄷ', u'ㄸ', u'ㄹ', u'ㅁ', u'ㅂ', u'ㅃ',        u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅉ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']

  # 중성 리스트. 00 ~ 20
    JUNGSUNG_LIST = [u'ㅏ', u'ㅐ', u'ㅑ', u'ㅒ', u'ㅓ', u'ㅔ', u'ㅕ', u'ㅖ', u'ㅗ', u'ㅘ', u'ㅙ', u'ㅚ', u'ㅛ', u'ㅜ', u'ㅝ', u'ㅞ', u'ㅟ', u'ㅠ', u'ㅡ', u'ㅢ', u'ㅣ']

  # 종성 리스트. 00 ~ 27 + 1(1개 없음)
    JONGSUNG_LIST = [u' ', u'ㄱ', u'ㄲ', u'ㄳ', u'ㄴ', u'ㄵ', u'ㄶ', u'ㄷ', u'ㄹ', u'ㄺ', u'ㄻ', u'ㄼ', u'ㄽ', u'ㄾ', u'ㄿ', u'ㅀ', u'ㅁ', u'ㅂ', u'ㅄ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']

    CODING_LIST = CHOSUNG_LIST + JONGSUNG_LIST + JUNGSUNG_LIST

    NUMBERING = ['00','01','02','03','04','05','06','07','08','09','10',
               '11','12','13','14','15','16','17','18','19','20',
               '21','22','23','24','25','26','27','28','29','30',
                '31','32','33','34','35','36','37','38','39','40',
                 '41','42','43','44','45','46','47','48','49','50',
                 '51','52','53','54','55','56','57','58','59','60',
                 '61','62','63','64','65','66','67']

    BARCODING = dict(zip(CODING_LIST, NUMBERING))

  # BASE_CODE(4403244) 제거
  
    chos = []
    jungs = []
    jongs = []
 
  
    for str in name:
     
      for charTemp in str:
        cBase = ord(charTemp) - BASE_CODE

        c1 = cBase / CHOSUNG
        #print '초성 : {}  /  유니코드 : {}'.format(CHOSUNG_LIST[c1], unichr(c1))
        c2 = (cBase - (CHOSUNG * c1)) / JUNGSUNG
        #print '중성 : {}  /  유니코드 : {}'.format(JUNGSUNG_LIST[c2], unichr(c2))
        c3 = (cBase - (CHOSUNG * c1) - (JUNGSUNG * c2))
        #print '종성 : {}  /  유니코드 : {}'.format(JONGSUNG_LIST[c3], unichr(c3))

        chos.append(CHOSUNG_LIST[c1])
        #jungs.append(JUNGSUNG_LIST[c2])
        #jongs.append(JONGSUNG_LIST[c3])
    


    barcode = []
    for a in chos:
      barcode.append(BARCODING[a])
    
    #for b in jungs:
      #barcode.append(BARCODING[b])
    
    #for c in jongs:
      #barcode.append(BARCODING[c])
    
  
    tag = ''.join(barcode)
    ID = birthday[1:] + tag + lucky
    
     
  
    return ID
