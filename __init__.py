#-*- coding:utf-8 -*-


import os

from flask import request, jsonify

from flask import Flask, url_for
from flask import render_template,jsonify
from module.database import db_session, init_db
from module.models import User
import urllib
from module.hangul import Barcode


app = Flask(__name__)




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/keyboard', methods=['GET'])
def Keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons" : [u"등록하기", u"도움말"]
    }
 
    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
def Message():
    while True:

        dataReceive = request.get_json()
        content = dataReceive[u'content']
        
        if content == u"도움말":
            dataSend = {
                "message": {
                    "text": u"바코드를 사용하여 PPUCHA 서비스를 이용하세요. 바코드를 발급받으신 후, 임신증명사실 절차를 걸쳐야 서비스 이용이 가능해집니다. 자세한 문의는 agdal1125@gmail.com 으로 보내주세요"},
            "keyboard": {
                "type":"buttons",
                    "buttons":[u"등록하기",u"도움말"]}
                }

        
        elif content == u"처음으로":
            dataSend = {
                "message": {
                    "text": u"처음으로 돌아갑니다." },
                "keyboard":{
                   "type":"buttons",
                        "buttons":[u"등록하기", u"도움말"]} 
                            }   

        elif content == u"완료":
            dataSend = {
                "message": {
                    "text": u"반드시 임신증명사실 절차를 거치세요!" },
                "keyboard":{
                   "type":"buttons",
                        "buttons":[u"처음으로"]} }
             

        elif content == u"동의합니다":
            dataSend = {
                "message": {
                    "text": u"이름,생년월일,행운의숫자(0~9 중 한 개)를 입력해주세요! 예) 이재근:941125:9 "  }
                             }

        elif content == u"등록하기":
            dataSend = {
                "message": {
                    "text": u"등록을 하기 위해서는 개인정보 이용 동의가 필요합니다. 사용될 개인 정보는 이름, 생년월일 및 임신 사실 여부입니다."},
                "keyboard": {
                    "type": "buttons",
                        "buttons":[u"동의합니다",u"처음으로"]} 
                 }

        elif u":" in content:

       
            info = content.split(':')

            name = info[0]
            birthday = info[1]
            lucky = info[2]
                       
            new_user = Barcode(name,birthday,lucky)

            new_id = new_user.coding(name,birthday,lucky)

            init_db()
            u = User(new_id,name,birthday,lucky)

            db_session.add(u)
            db_session.commit()


            

           
            dataSend = {
                  "message": {
                    "text": u"귀하의 바코드 입니다! 바코드는 임신 사실 증명 이후 효력을 가집니다. 증빙자료를 agdal1125@gmail.com 으로 보내주세요. 확인은 최대 하루 정도 걸립니다.",
                    "photo": { 
                       "url": "https://www.barcodesinc.com/generator/image.php?code="+str(new_id)+"&style=197&type=C128B&width=206&height=50&xres=1&font=3",
                        "width" : 206, "height":50 } },
                       "keyboard": { 
                          "type":"buttons", 
                            "buttons":[u"완료",u"도움말"] }
                                    }
                    #"photo": { 
                       #"url": "http://api-bwipjs.rhcloud.com/?bcid=ean13&text="+str(new_id),
                        #"width" : 190, "height":144 } } }


        else: 
            dataSend = {
                "message": {
                    "text": u"힝...무슨말인지 모르겠어요... '도움말', '등록하기'를 이용해주세요!" }, 
                "keyboard": {
                    "type":"buttons",
                        "buttons" : [u"등록하기",u"도움말"]}
                         }
                
        return jsonify(dataSend)
                
        

@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res


