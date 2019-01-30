# -*- coding:gbk -*-
import sys
reload(sys)
sys.setdefaultencoding('gbk')

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def GetDuilian(up):
    inputDriver.clear()
    inputDriver.send_keys(up.decode('gbk'))
    buttonDriver.click() 
    r = outputDriver.text
    runds = 0
    while ( not r and runds < 200):
        r = driver.find_element_by_xpath('//div[@class="couplet-bd" and @style]').text
        runds += 1
    if r:
        #driver.quit()
        return r , 1
    else:
        #driver.quit()
        return "那啥，上联好像有点问题" , 0


import os
import logging
logging.basicConfig(
    level       = logging.INFO,
    format      = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt     = '%Y-%m-%d %H:%M:%S',
    filename    = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'CQHanlder.log'),
    filemode    = 'w+'
)

import CQSDK

class CQHandler(object):
    def __init__(self):
        global driver,inputDriver,outputDriver,buttonDriver
        logging.info('__init__')
        path = '.\chromedriver.exe'
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
        driver.get("https://ai.binwang.me/couplet/")
        inputDriver = driver.find_element_by_xpath('//*[@class="couplet-input"]')
        outputDriver = driver.find_element_by_xpath('//div[@class="couplet-bd" and @style]')
        buttonDriver = driver.find_element_by_xpath('//*[@class="couplet-btn"]')
            
    def __del__(self):
        logging.info('__del__')
        
    def OnEvent_Enable(self):
        logging.info('OnEvent_Enable')

    def OnEvent_Disable(self):
        logging.info('OnEvent_Disable')

    def OnEvent_PrivateMsg(self, subType, sendTime, fromQQ, msg, font):
        logging.info('OnEvent_PrivateMsg: subType={0}, sendTime={1}, fromQQ={2}, msg={3}, font={4}'.format(subType, sendTime, fromQQ, msg, font))
        if msg[:7] == "%对对联":
            try:
                CQSDK.SendPrivateMsg(fromQQ, "少女祈祷中……")
                down, flag = GetDuilian(msg[7:])
                if flag:
                    CQSDK.SendPrivateMsg(fromQQ, "上联：" + msg[7:] + "\n下联：" + str(down))
                else:
                    CQSDK.SendPrivateMsg(fromQQ, str(down))
            except Exception as e:
                CQSDK.SendPrivateMsg(fromQQ, str(e))
                logging.exception(e)

    def OnEvent_GroupMsg(self, subType, sendTime, fromGroup, fromQQ, fromAnonymous, msg, font):
        logging.info('OnEvent_GroupMsg: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, fromAnonymous={4}, msg={5}, font={6}'.format(subType, sendTime, fromGroup, fromQQ, fromAnonymous, msg, font))

        if msg[:7] == "%对对联":
            try:
                CQSDK.SendGroupMsg(fromGroup, "少女祈祷中……")
                down, flag = GetDuilian(msg[7:])
                if flag:
                    CQSDK.SendGroupMsg(fromGroup, "上联：" + msg[7:] + "\n下联：" + str(down))
                else:
                    CQSDK.SendGroupMsg(fromGroup, str(down))
            except Exception as e:
                CQSDK.SendGroupMsg(fromGroup, str(e))
                logging.exception(e)

    def OnEvent_DiscussMsg(self, subType, sendTime, fromDiscuss, fromQQ, msg, font):
        logging.info('OnEvent_DiscussMsg: subType={0}, sendTime={1}, fromDiscuss={2}, fromQQ={3}, msg={4}, font={5}'.format(subType, sendTime, fromDiscuss, fromQQ, msg, font))

    def OnEvent_System_GroupAdmin(self, subType, sendTime, fromGroup, beingOperateQQ):
        logging.info('OnEvent_System_GroupAdmin: subType={0}, sendTime={1}, fromGroup={2}, beingOperateQQ={3}'.format(subType, sendTime, fromGroup, beingOperateQQ))

    def OnEvent_System_GroupMemberDecrease(self, subType, sendTime, fromGroup, fromQQ, beingOperateQQ):
        logging.info('OnEvent_System_GroupMemberDecrease: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, beingOperateQQ={4}'.format(subType, sendTime, fromGroup, fromQQ, beingOperateQQ))

    def OnEvent_System_GroupMemberIncrease(self, subType, sendTime, fromGroup, fromQQ, beingOperateQQ):
        logging.info('OnEvent_System_GroupMemberIncrease: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, beingOperateQQ={4}'.format(subType, sendTime, fromGroup, fromQQ, beingOperateQQ))

    def OnEvent_Friend_Add(self, subType, sendTime, fromQQ):
        logging.info('OnEvent_Friend_Add: subType={0}, sendTime={1}, fromQQ={2}'.format(subType, sendTime, fromQQ))

    def OnEvent_Request_AddFriend(self, subType, sendTime, fromQQ, msg, responseFlag):
        logging.info('OnEvent_Request_AddFriend: subType={0}, sendTime={1}, fromQQ={2}, msg={3}, responseFlag={4}'.format(subType, sendTime, fromQQ, msg, responseFlag))

    def OnEvent_Request_AddGroup(self, subType, sendTime, fromGroup, fromQQ, msg, responseFlag):
        logging.info('OnEvent_Request_AddGroup: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, msg={4}, responseFlag={5}'.format(subType, sendTime, fromGroup, fromQQ, msg, responseFlag))

    def OnEvent_Menu01(self):
        logging.info('OnEvent_Menu01')

    def OnEvent_Menu02(self):
        logging.info('OnEvent_Menu02')

    def OnEvent_Menu03(self):
        logging.info('OnEvent_Menu03')

    def OnEvent_Menu04(self):
        logging.info('OnEvent_Menu04')

    def OnEvent_Menu05(self):
        logging.info('OnEvent_Menu05')

    def OnEvent_Menu06(self):
        logging.info('OnEvent_Menu06')

    def OnEvent_Menu07(self):
        logging.info('OnEvent_Menu07')

    def OnEvent_Menu08(self):
        logging.info('OnEvent_Menu08')

    def OnEvent_Menu09(self):
        logging.info('OnEvent_Menu09')