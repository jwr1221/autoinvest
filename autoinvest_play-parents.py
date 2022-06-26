#!/usr/bin/env python
# coding: utf-8

import pyautogui
import schedule
import time
import datetime
import sys
import threading
import pytesseract
import cv2
import os
from PIL import ImageGrab
from PIL import Image
import pyautogui as pag
import keyboard

now = datetime.datetime.now()
tradesignal = (201, 231, 243) #조건검색 버튼 클릭 후 매매 종목이 있으면 나오는 바탕색.블루
ownedstock = (201, 231, 243) #계좌관리에 보유 주식이 있을 경우 나오는 바탕색.블루.tradesignal과 동일.
nosignal = (252, 253, 255) #매매종목 및 보유 주식이 없을 경우 나오는 바탕색. 흰색
nosignal2 = (255, 255, 255)

def startTimer():
    timer = threading.Timer(60, startTimer)

def programstart(): #08:40 영웅문 아이콘 클릭 및 접속
    pyautogui.moveTo(40, 536, 0.25) #바탕화면 내 영웅문 아이콘 위치
    pyautogui.doubleClick()
    time.sleep(60)
    pyautogui.moveTo(1006, 686, 0.25) #영웅문 인증서 비번 입력창 위치
    pyautogui.click()
    time.sleep(10)
    pyautogui.click()
    time.sleep(10)
    pyautogui.hotkey('d', interval=0.2) #핀번호 입력
    pyautogui.hotkey('u', interval=0.2)
    pyautogui.hotkey('s', interval=0.2)
    pyautogui.hotkey('a', interval=0.2)
    pyautogui.hotkey('u', interval=0.2)
    pyautogui.hotkey('d', interval=0.2)
    pyautogui.hotkey('7', interval=0.2)
    pyautogui.hotkey('!', interval=0.2)
    pyautogui.hotkey('!', interval=0.2)
    time.sleep(5)
    pyautogui.click()
    pyautogui.moveTo(1075, 742, 0.25) #인증서 선택(확인)창 위치
    pyautogui.click()
    print(("programstart"),(time.strftime('%H:%M:%S')))
    
def programreduction(): #08:43 영웅문 버튼 최소화
    time.sleep(180)
    pyautogui.hotkey("Enter")
    pyautogui.moveTo(1859, 20, 0.25) #영웅문 최소화 버튼 위치
    time.sleep(10)
    pyautogui.click()
    pyautogui.click()
    time.sleep(120)
    print(("programreduction"),(time.strftime('%H:%M:%S')))

def tradingstart():
    pyautogui.moveTo(1859, 20, 0.25)  # 영웅문 최소화 버튼 위치
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1575, 264, 0.25)  # 계좌잔고첫번째줄이동.클릭한번필
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    screen = ImageGrab.grab()
    pos4 = screen.getpixel((1730, 758))  # 0156 조건검색실시간 자동매매_매도용 첫번째 줄 위치
    pos3 = screen.getpixel((1729, 573))  # 0156 조건검색실시간 자동매매_매수용 첫번째 줄 위치
    pos2 = screen.getpixel((1575, 264))  # 계좌잔고 첫번째 줄 위치

    #잔고내역O = 매도신호 검색
    if pos2 == tradesignal:
        sellsignalsearch()

    #잔고내역X = 매수신호 검색
    if pos2 == nosignal:
        buysignalsearch()

    #잔고내역X + 매수신호O  = 매수
    if pos3 == tradesignal:
        buysignalclick()

    #잔고내역O + 매도신호O  = 매도
    if pos4 == tradesignal:
        sellsignalclick()

def buysignalclick(): #매수신호포착
    pyautogui.moveTo(1469, 850, 0.25) #멀티쾌속주문 중 매수버튼 위치
    time.sleep(3)
    pyautogui.click()
    time.sleep(3)
    # pyautogui.moveTo(989, 1013, 0.25) #멀티쾌속주문 중 매수주문 확인버튼
    # time.sleep(2)
    # pyautogui.click()
    # time.sleep(2)
    # pyautogui.hotkey("Enter")
    # time.sleep(3)
    pyautogui.moveTo(1881, 574, 0.25)#조건검색실시간-자동매매_매수용화면 중 삭제 아이콘
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    time.sleep(1)
    print(("buysignalclick"),(time.strftime('%H:%M:%S')))

def sellsignalclick(): #매도신호포착
    pyautogui.moveTo(1587, 852, 0.25) #멀티쾌속주문 중 매도버튼 위치
    time.sleep(3)
    pyautogui.click()
    time.sleep(3)
    # pyautogui.moveTo(1241, 1018, 0.25) #멀티쾌속주문 중 매도주문 확인버튼
    # time.sleep(3)
    # pyautogui.click()
    # time.sleep(2)
    # pyautogui.hotkey("Enter")
    # time.sleep(2)
    pyautogui.moveTo(1882, 762, 0.25) #조건검색실시간-자동매매_매도용화면 중 삭제 아이콘
    time.sleep(3)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    time.sleep(1)
    print(("sellsignalclick"),(time.strftime('%H:%M:%S')))
    
def buysignalsearch(): # 0156 조건검색실시간 - 자동매매_매수용 창
    pyautogui.moveTo(1754, 449, 0.25) #조건검색 실시간 창 중 재조회 버튼으로 이동
    time.sleep(3)
    pyautogui.click()
    # time.sleep(2)
    # pyautogui.hotkey("Enter")
    time.sleep(1)
    pyautogui.moveTo(1729, 573, 0.25) #검색창 첫번째 줄 위치
    time.sleep(3)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    time.sleep(1)
    print(("buysignalsearch"),(time.strftime('%H:%M:%S')))
    
def sellsignalsearch(): # 0156 조건검색실시간 - 자동매매_매도용 창
    pyautogui.moveTo(1758, 636, 0.25) #조건검색 실시간 창 중 재조회 버튼으로 이동
    time.sleep(3)
    pyautogui.click()
    # time.sleep(2)
    # pyautogui.hotkey("Enter")
    time.sleep(1)
    pyautogui.moveTo(1730, 758, 0.25) #검색창 첫번째 줄 위치
    time.sleep(3)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    time.sleep(1)
    print(("sellsignalsearch"),(time.strftime('%H:%M:%S')))

def programend():
    pyautogui.moveTo(1051, 1059, 0.25) #작업표시줄 영웅문 아이콘 위치
    time.sleep(5)
    pyautogui.moveTo(713, 903, 0.25) #영웅문4 아이콘 X 아이콘 위치
    time.sleep(4)
    pyautogui.click()
    time.sleep(3)
    print(("today_invest_end"),(time.strftime('%H:%M:%S')))


def exit(): #코드실행 종료
    print(("job_end"),(time.strftime('%H:%M:%S')))
    sys.exit()

# # -----바탕화면 하단 영웅문 아이콘 클릭후 인증서암호 입력 후 엔터-------------------------

programstart()

# -------------영웅문 화면 최소화---------------------------------------------  

programreduction()

# --------------------자동 매매 로직 시작!!!------------------------

schedule.every(3).minutes.do(tradingstart)
schedule.every().day.at("15:18").do(sellsignalclick)

# ---------------------15:20 매매종료!!!-------------------------

schedule.every().day.at("15:20").do(programend)  
schedule.every().day.at("15:22").do(exit)

while True:
    schedule.run_pending()
    time.sleep(1)
