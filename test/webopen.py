# -*- coding:utf-8 -*-
import webbrowser, sys

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# 도메인을 입력하면 웹 페이지 띄우기.

address = input("어떤 웹페이지로 이동할까요?")

webbrowser.get(chrome_path).open(address)