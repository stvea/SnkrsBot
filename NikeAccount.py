# -*- coding: utf-8 -*-
import uuid
class NikeAccount:
    def __init__(self,access_token):
    	self.checkoutId = str(uuid.uuid4())
    	self.paymentsId = str(uuid.uuid4())
    	self.shippingId = str(uuid.uuid4())
    	self.recipientInfo = {"lastName": '李', "firstName": '小'}
    	self.addressInfo = {"state": 'CN-42', "city": '武汉市', "address1": '彭刘杨巷19号', "postalCode": "430060","address2": "123", "county": "武昌区", "country": "CN"}
        self.access_token = access_token
        self.contactInfo = {"phoneNumber": '13951807086', "email": '1191743792@qq.com'}
        self.launchRecipient = {"lastName": '李', "firstName": '小', "email": '1123123792@qq.com',"phoneNumber": '139123123123'}
        self.launchAddress = {"state": 'CN-42', "city": '武汉市', "address1": '彭刘杨巷19号', "county": "武昌区", "country": "CN"}
    def setEntryId(id):
    	self.setEntryId = id

