# coding=UTF-8

from setting import private
import sys
from gtts import gTTS
import random
#import mp3play
import socket
import sys
import requests
from bs4 import BeautifulSoup
import json
import re, os
import time
from time import gmtime, strftime
import _thread
import numpy
#from twitch.api import v3
#from twitch.logging import log


sys.setrecursionlimit(2000)

#from twitch import TwitchClient
#client = TwitchClient('hdy321noagj99zorkqywfp3yznap01', 'oauth:v1ivujxj94tn9c2z8xn150fe2fwozg')
#channel = client.users.get_by_id("e4e2e7343")
#print (channel)

#點歌系統
srflag = False

#操練前喝水300 cc, 喝水
#gamblingswitch = False

#---useful function
#def scmp(f, s):
#    for i in range(0, len(f)):
#        if cmp(f[i:i+len(s)], s) == 0:
#            return True
#    return False

def req_loop(url, count):
    try:
        res = requests.get(url)
        return res
    except:
        
        if count > 10:
            return None
        else:
            res = req_loop(url, count + 1)
            return res

#其他實況主的歌
def specialplay(name):
    if os.path.exists("./sound/" + name + ".mp3"):
        filename = "./sound/" + name + ".mp3"
        clip = mp3play.load(filename)
        clip.volume(50)
        clip.play()
        if name == "wow_tomato":
            time.sleep(15)        
        elif name == "nicemonsteroh":
            time.sleep(clip.seconds())        
        elif name == "gertie0123":
            time.sleep(clip.seconds())
        elif name == "danielnan":
            time.sleep(clip.seconds())
        elif name == "sugar369":
            time.sleep(clip.seconds())
        clip.stop()
    else:
        return 0
""""""
#指令類別
#分幾組system cmd
#
class CMD():
    def __init__(self, reaction="", cdtime=5, limit=3, cost=0):
        #self.reaction = self.action(react)
        self.reaction = reaction   #"""這邊打算做成直接return reaction"""
        self.cdtime = cdtime
        self.recordtime = time.time()
        self.limit = limit
        self.cost = cost

    def Act(self, viewer):
        if time.time() - self.recordtime > self.cdtime:
            if viewer.gold > self.cost:
                print (viewer.gold, self.cost)
                viewer.gold = viewer.gold - self.cost
                sendmsg(self.reaction)
                self.recordtime = time.time()
        
            
    #def action(self, react):
    #    if react == "":
        
    #def load_cmd(self, path):
    #    with open("./setting/cmd.txt", "r") as f:
    #        for line in f:
    #            buf2 = line.split(",")
    #            self.name.append(buf2[0])
    #            self.reaction[buf2[0]] = buf2[1]
    #            self.cdtime[buf2[0]] = int(buf2[2])
    #            self.recordtime[buf2[0]] = time.time()
    #            self.limit[buf2[0]] = int(buf2[3])       #1.system 2.me 3.mod 4.follower 5.everyone 6.sub
    #            self.cost[buf2[0]] = int(buf2[4])        
    #!addcom !指令 !內容 其它不輸入都預設
    #-d
    #-l
    #-k
    #def addcom(self, name, react, cdtime=5, limit=3, cost=0):
    #    print name, react, cdtime, limit, cost
    #    self.name.append(name)
    #    self.reaction[name] = react
    #    self.cdtime[name] = cdtime
    #    self.recordtime[name] = time.time()
    #    self.limit[name] = limit
    #    self.cost[name] = cost
        
        #f = open("/setting/cmd.txt", "w")
        #print "GGGGG"
        #f.write(name + "," + react + "," + str(cdtime) + "," + str(limit) + "," + str(cost) + "\n")
        #f.close()
""""""
#系統設定類別
class KSET():
    def __init__(self):
        print ("initial system...")
        
    """    #設定viewers          
        self.viewers = dict()     #觀眾           
        self.Load_viewers()  #Load_viewers
        
        #cmd分為3種, host, mod, user
        self.cmd = dict()      #存host 的CMD集合        
        self.Load_cmd() 
        
        #define vars
        self.vars = dict()         #存自訂的變數
        self.Load_vars()
        
        #define mod
        self.mod = []
        
        
        #設定mod
        self.Load_mod()
        print (self.mod)
    def Load_viewers(self):
        print ("Loading viewers...")
        f = open("./views.csv", "r")
        f.readline()
        for buf in f:
            buf2 = buf.replace("\n", "").split(",")
            self.viewers[buf2[0]] = VIEWER(int(buf2[1]), int(buf2[2]), int(buf2[3]), int(buf2[4]), int(buf2[7]), 1, 0)
        f.close()"""
        
    def Load_cmd(self):
        print ("Loading cmd...")
        
        #設定system cmd and cd
        #要有一個cmd類別
        """print ("Read system cmd ..."        )
        with open("./setting/syscmd.txt", "r") as f:
            for line in f:
                buf2 = line.split(",")
                print (buf2[0])
                self.syscmd[buf2[0]] = CMD("", int(buf2[1]), 1, 0)"""
                
        #讀齒輪資訊
        """print ("Read gear ...")
        with open("./setting/info.txt", "r") as f:
            for line in f:
                self.gear = int(line.replace("\n","")) """ 
    
    def Load_cmd(self):
        print ("Loading cmd...")
        
        #設定system cmd and cd
        #要有一個cmd類別
        """print ("Read system cmd ..."        )
        with open("./setting/syscmd.txt", "r") as f:
            for line in f:
                buf2 = line.split(",")
                print (buf2[0])
                self.syscmd[buf2[0]] = CMD("", int(buf2[1]), 1, 0)"""
    
    def Load_vars(self):    
        #讀齒輪資訊
        """print ("Read gear ...")
        with open("./setting/info.txt", "r") as f:
            for line in f:
                self.gear = int(line.replace("\n","")) """ 
    
    def Load_mod(self):
        with open("./setting/mod.txt", "r") as f:
            for line in f:
                for item in line.split(","):
                    self.mod.append(item)
    
    def saveviewers(self):
        print ("Saving viewers...")
        f = open("./views.csv", "w")
        f.write("name,prechat,pretime,nowchat,nowtime,totalchat,totaltime,gold,\n")
        for buf in self.viewers:
            f.write(buf)
            f.write(",")
            f.write(str(self.viewers[buf].prec))
            f.write(",")
            f.write(str(self.viewers[buf].pret))
            f.write(",")
            f.write(str(self.viewers[buf].nowc))
            f.write(",")
            f.write(str(self.viewers[buf].nowt))
            f.write(",")
            f.write(str(self.viewers[buf].totalc))
            f.write(",")
            f.write(str(self.viewers[buf].totalt))
            f.write(",")
            f.write(str(self.viewers[buf].gold))
            f.write(",")
            f.write("\n")
        f.close()
    
    def ad1(self):
        print ("AD SHOW1")
        sendmsg("先前的實況沒追到, 或實況看到一半睡著,")
        sendmsg("歡迎到老k的youtube頻道: https://www.youtube.com/user/killelder,")
    def ad2(self):
        print ("AD SHOW2")
        sendmsg("感謝各位觀眾的觀看, 如果喜歡老K, 可以按下右上角追隨給老K支持哦 charGasm VoHiYo")
    def ad3(self, number = random.randint(1,7)):
        print ("AD SHOW3")
        #number = random.randint(1,5)
        if number == 1:
            sendmsg("友台nmw_tw專業ㄈㄓ, 也歡迎大家的支持, https://www.twitch.tv/nmw_tw")
        elif number == 2:
            sendmsg("友台玉花親切可人, 也歡迎大家的支持, https://www.twitch.tv/gertie0123")
        elif number == 3:
            sendmsg("友台頭沒頭唯一清流, 也歡迎大家的支持, https://www.twitch.tv/wow_tomato")
        elif number == 4:
            sendmsg("友台大牛楠奶子!!, 也歡迎大家的支持, https://www.twitch.tv/danielnan")   
        elif number == 5:
            sendmsg("友台妖乖天真活潑, 也歡迎大家的支持追隨, https://www.twitch.tv/nicemonsteroh")
        elif number == 6:
            sendmsg("友台清玉實力堅強, 也歡迎大家的支持追隨, https://www.youtube.com/channel/UCZNDv1o3QNxJdu4mFa5cvCw")
        elif number == 7:
            sendmsg("感謝佛心公司英特衛  粉專: https://www.facebook.com/interwise.tw/  贊助阿加雷斯特戰記  http://www.interwise.com.tw/interwise/AGOW02")
        print (number  )  
    
    def scanuser(self, t=1):
        print ("scan user list...")
        #Check user list 
        #http://tmi.twitch.tv/group/user/e4e2e7343/chatters
        res = req_loop("http://tmi.twitch.tv/group/user/e4e2e7343/chatters", 0)
        
        if res != None:
            soup = BeautifulSoup(res.text.encode("utf-8", "ignore"))
            if "chatters" in soup.text:
                newDictionary=json.loads(str(soup))
                for buf in newDictionary["chatters"]["viewers"]:
                    self.Check_viewers(buf, 0, t)
                for buf in newDictionary["chatters"]["moderators"]:
                    self.Check_viewers(buf, 0, t)
                print ("Scan Success")
                
    def Check_viewers(self, username, ct, st):
        #print "check users..."
        check_value = 0
        for item in self.viewers:
            if username == item and self.viewers[item].trigger == 1:
                check_value = 1
                self.viewers[item].nowc = self.viewers[item].nowc + ct
                self.viewers[item].nowt = self.viewers[item].nowt + st
                self.viewers[item].totalc = self.viewers[item].totalc + ct
                self.viewers[item].totalt = self.viewers[item].totalt + st
                self.viewers[item].gold = self.viewers[item].gold + ct + st
            if username == item and self.viewers[item].trigger == 0:
                check_value = 1
                self.viewers[item].trigger = 1
                if ct != 0 or st != 0:
                    self.viewers[item].today(username)
                self.viewers[item].nowc = self.viewers[item].nowc + ct
                self.viewers[item].nowt = self.viewers[item].nowt + st
                self.viewers[item].totalc = self.viewers[item].totalc + ct
                self.viewers[item].totalt = self.viewers[item].totalt + st
                self.viewers[item].gold = self.viewers[item].gold + ct + st
        if check_value == 0:
            print ("new user: " + username)
            self.viewers[username] = VIEWER(0, 0, 0, 0, 5000, 0, 1)
            self.viewers[username].nowc = self.viewers[username].nowc + ct
            self.viewers[username].nowt = self.viewers[username].nowt + st
            self.viewers[username].gold = self.viewers[username].gold + ct + st
            if ct != 0 or st != 0:
                self.viewers[username].today(username)       
                
    def Check_syscmd(self):
        print ("scan syscmd...")
        for key, item in self.syscmd.iteritems():            
            if key == "gamble" or key == "gdtime" or key == "rollcd":   #temp for no use function
                continue
            if time.time() - item.recordtime > item.cdtime:
                print (key)
                try:
                    func = getattr(self,key)
                    thread.start_new_thread(func, ())
                    item.recordtime = time.time()
                except:
                    print ("FAIL")
                    pass
    

class VIEWER():
    """
        #觀眾類別
        #需要紀錄的東西
        #history: 以前有沒有來過
        #prec: 先前聊天次數
        #pret: 先前掛機時間
        #nowc: 這次聊天次數
        #nowt: 這次掛機時間
        #totalc: 總聊天次數
        #totalt: 總掛機時數
        #trigger: 今天是不是第一次來
        #gold: K粉數
        #exp: 經驗值
        #vars: 其他參數
    """
    def __init__(self, prec, pret, nowc, nowt, gold, history, trigger):
        self.history = history
        self.prec = prec
        self.pret = pret
        self.nowc = nowc
        self.nowt = nowt
        self.totalc = self.prec + self.nowc
        self.totalt = self.pret + self.nowt
        self.trigger = trigger
        self.gold = gold
        self.ticket = 0
    
    """#今天第一次進來的反應
    def today(self, name):
        c = v3.channels.by_name(name)
        if name == "orangepeel9487":
            sendmsg("橘皮老婆 <3 ~")
        if self.history == 1:
            if c["game"] and c["followers"] > 50:
                #pass
                sendmsg("歡迎實況主" + name.encode("utf-8","ignore") + "也有在實況哦~, 他在實況的是" + c["game"].encode("utf-8", "ignore"))
            else:
                pass
                #sendmsg("歡迎再次來到老K的遊戲間" + name.encode("utf-8","ignore"))
            print (" today and history = 1")
            specialplay(name)
            #googletalk("tw", "歡迎再次來到老K的遊戲間" + self.name.encode("utf-8","ignore"), lock)
        else:
            if c["game"] and c["followers"] > 50:
                #pass
                sendmsg("歡迎實況主" + name.encode("utf-8","ignore") + "第一次來到, 他也有在實況哦~, 他在實況的是" + c["game"].encode("utf-8", "ignore"))
            else:
                #pass
                sendmsg("歡迎第一次來到老K的遊戲間" + name.encode("utf-8","ignore"))
            print (" today and history != 1")
            #googletalk("tw", "歡迎第一次來到老K的遊戲間" + self.name.encode("utf-8","ignore"), lock)
            self.history = 1
        #只要來過trigger就開
        self.trigger = 1"""
    
#def dianger(name, site):
#    command = "youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v=" + site.replace(" ","")
#    print command
#    call(command.split(), shell=False)
#    f = open("./songrequestlist.txt", "a")
#    f.write(name)
#    f.write(",")
#    f.write(site)
#    f.write("\n")
#    f.close()
#
#nowsong = ""
#songreqtime = 0    
#def diangersys(timesr, ns, srtt):
#    while True:
#        if time.time() >= timesr + 5:
#            print "diangsys on"
#            timesr = time.time()
#            print ns
#            if srtt > 10:
#                ns = ""
#            if ns == "":  
#                srt = open("./songrequestlist.txt", "r")
#                buf = srt.readline()
#                if buf == "":
#                    continue
#                buf2 = buf.replace(" ","").replace("\n","").split(",")
#                ns = buf2[1]
#                print ns
#                #os.system("pause")
#                temp = ""
#                for buf in srt:
#                    if not buf:
#                        break
#                    temp = temp + buf
#                srt.close()
#                srt = open("./songrequestlist.txt", "w")
#                srt.write(temp)  
#                srt.close()
#                #temp = ""
#            else:
#                print "SRGOGO"
#                print ns
#                print "=========="
#                for root, dirs, files in os.walk("./"):
#                    for f in files:
#                        if "mp3" in f and ns in f:
#                            clip = mp3play.load(f)
#                            clip.play()
#                            time.sleep(30)
#                            clip.stop()
#                            ns = ""
#            srtt = srtt + 1
            
#########################
##賭博專用指令
##
#########################
#Q: 題目
#Ops: 選項
#gt: 下注的時間
def start_gamble(gt, Q, Ops):
    Ques = Q + "?"
    print (Ops)
    f = open("gamble.txt", "w")
    f.close()
    Op = ""
    for i in range(0,len(Ops)):
        Op = Op + " , " + str(i+1) + ". " + Ops[i]        
    sendmsg("賭博開始(倒數" + str(gt/60) + "分鐘)," + Ques + Op + " (按下!gb 選項 金額,即可參加賭博)")
    return Ques + Op + " (按下!gb 選項 金額,即可參加賭博)"
def gambleend(kset, answer, gdg):
    worstp = ""
    worstgold = 0
    f = open("gamble.txt", "r")
    ratio = 0.01
    print ("ratio is ")
    print (gdg.sum())
    print (gdg[int(answer)-1])
    if gdg[int(answer)-1] < 1:
        sendmsg("通殺!!!!")
    else:
        if (float(gdg.sum())/float(gdg[int(answer)-1])) - 1 < 0.01:
            ratio =  0.01
        else:
            ratio = float(gdg.sum())/float(gdg[int(answer)-1]) - 1
        print (ratio)
        for buf in f:
            if not buf:
                break
            buf2 = buf.split(",")
            
            if int(buf2[1]) == int(answer):
                sendmsg("恭喜" + buf2[0] + "獲得" + str(int(int(buf2[2])*ratio)) + "K粉")
                kset.viewers[buf2[0]].gold = kset.viewers[buf2[0]].gold + int(buf2[2]) + int(int(buf2[2])*ratio)
            else:
                if worstgold < int(buf2[2]):
                    worstgold = int(buf2[2])
                    worstp = buf2[0]
            #viewers[item].gambleo = 0
        f.close()
        sendmsg("恭喜" + worstp + "損失" + str(worstgold) + "K粉," + "給" + worstp + "一罐啤酒!!")
    
def gambleviewero(kset, username, ops, gold, gdg):
    print (username, ops, gold)
    if kset.viewers[username].gold >= int(gold) + 1 and int(ops) <= 5:
        f = open("gamble.txt", "r")
        for buf in f:
            if not buf:
                break
            buf2 = buf.split(",")[0]
            if username == buf2:
                return 0
        f.close()
        #viewers[username].gambleo = int(ops)
        kset.viewers[username].gold = kset.viewers[username].gold - int(gold)
        f = open("gamble.txt", "a")
        f.write(username)
        f.write(",")
        f.write(ops)
        f.write(",")
        f.write(gold)
        f.write(",\n")
        f.close()
        gdg[int(ops)-1] = gdg[int(ops)-1] + int(gold)
        #viewers[username].gambleg = int(gold)
        #print viewers[username].gambleo
    sendmsg(username + "下注成功")
#######################            
#######################
#######################


#--------------觀眾專用指令-----------------#
def playsound(kset, username, opt, lock):
    lock.acquire()
    print ("play sound")
    print (opt    )
    if opt == 1:
        if kset.viewers[username].gold >= 700:
            kset.viewers[username].gold = kset.viewers[username].gold - 700
            print ("laugh")
            number = random.randint(1,3)
            fn = "./sound/laugh" + str(number) + ".mp3"
            clip = mp3play.load(fn)
            clip.volume(50)
            if number == 3:
                clip.volume(15)
            clip.play()
            time.sleep(clip.seconds())    
    if opt == 2:
        if kset.viewers[username].gold >= 700:
            kset.viewers[username].gold = kset.viewers[username].gold - 700
            print ("pile")
            fn = "./sound/wow_tomato.mp3"
            clip = mp3play.load(fn)
            clip.volume(40)
            clip.play()
            time.sleep(9)
    if opt == 3:
        if kset.viewers[username].gold >= 700:
            kset.viewers[username].gold = kset.viewers[username].gold - 700
            print ("gan")
            fn = "./gertie.mp3"
            clip = mp3play.load(fn)
            clip.volume(100)
            clip.play()
            time.sleep(clip.seconds())            
    if opt == 4:
        if kset.viewers[username].gold >= 500:
            kset.viewers[username].gold = kset.viewers[username].gold - 500
            print ("gulu")
            fn = "./sound/gulu.mp3"
            clip = mp3play.load(fn)
            clip.volume(100)
            clip.play()
            time.sleep(clip.seconds()) 
    lock.release()
def say_garbage(kset, username, lock):
    c = random.randint(0,len(kset.garbage))
    sendmsg(kset.garbage[c].replace("xxx", username))
    #googletalk("tw", garbage[c].replace("xxx", username), lock)

def givemoney(kset, name1, name2, gold):
    if gold >= 10:
        if kset.viewers[name1].gold >= int(gold):
            kset.viewers[name1].gold = kset.viewers[name1].gold - int(gold)
            kset.viewers[name2].gold = kset.viewers[name2].gold + int(gold)*90/100
    
def addgold(kset, name, gold):
    print (name, gold)
    if name == "all":
        for item in kset.viewers:
            kset.viewers[item].gold = kset.viewers[item].gold + gold
    elif name == "allon":
        for item in kset.viewers:
            if kset.viewers[item].trigger == 1:
                kset.viewers[item].gold = kset.viewers[item].gold + gold
    else:
        kset.viewers[name].gold = kset.viewers[name].gold + gold
        #for item in viewers:
        #    if name == item.name:
        #        item.gold = item.gold + gold
            #if username == item.name and item.gold >= int(gold) + 1 and item.gambleg == 0:

#***************
#google小姐
#中文講話仍有時候會有點bug
#en文如果打中文會當掉
def googletalk(kset, username, lan, msg, lock):
    print ("Google Talk"   ) 
    if kset.viewers[username].gold >= 50:
        lock.acquire()
        if lan == "tw":
            try:
                tts = gTTS(text=msg, lang="zh-tw")            
                tts.save("message.mp3")
            except:
                lock.release()
                return 0
        if lan == "en":
            try:
                tts = gTTS(text=msg, lang="en")            
                tts.save("message.mp3")
            except:
                print ("en error")
                lock.release()
                return 0
        if lan == "ko":
            try:
                tts = gTTS(text=msg, lang="ko")            
                tts.save("message.mp3")
            except:
                print ("ko error")
                lock.release()
                return 0
        if lan == "jp":
            try:
                tts = gTTS(text=msg, lang="ja")            
                tts.save("message.mp3")
            except:
                print ("jp error")
                lock.release()
                return 0
        if lan == "yue":
            try:
                tts = gTTS(text=msg, lang="zh-yue")            
                tts.save("message.mp3")
            except:
                print ("yue error")
                lock.release()
                return 0
        
        filename = "message.mp3"
        clip = mp3play.load(filename)        
        clip.play()
        time.sleep(min(15, clip.seconds()))
        clip.stop()
        kset.viewers[username].gold = kset.viewers[username].gold - 50
        lock.release()
#--------------觀眾專用指令End-----------------#



#--------------系統指令-----------------#

def Show_user(viewer, username):
    sendmsg(username.encode("utf-8","ignore") + "聊天次數: " + str(viewer.nowc).encode("utf-8","ignore") + " 在線時間數: " + str(viewer.nowt).encode("utf-8","ignore") + "mins" + " K粉總額:" + str(viewer.gold).encode("utf-8","ignore"))

#--------------系統指令End-----------------# 
def shownow ():
    c = v3.channels.by_name("e4e2e7343")
    sendmsg("您正在收看的是" + c["game"].encode("utf-8", "ignore"))


#---------------------------------------------------------------------
# irc socket
# Program parameters.
# botnick  = Default nick
# bufsize  = Input buffer size
# channel  = Default IRC channel
# port     = Default IRC port number
# server   = Default IRC server hostname
# master   = Owner of the bot
# uname    = Bot username (NOT NICK!)
# realname = Bot's real name
botnick    = private.USERNAME  #twitch irc need same with master username
bufsize    = 2048
channel    = private.CHANNEL
port       = 6667
server     = "irc.twitch.tv"
master     = private.USERNAME
uname      = private.USERNAME
realname   = private.USERNAME

# Name:       ping
# Arguments:  None
# Purpose:    Responds to server Pings
#IRC cmd :
#          JOIN     :加入頻道
#          PART     :離開頻道
#          PRIVMSG  :送訊息到頻道
def ping():
    global ircsock
    ircsock.send ("PONG :pingis\n".encode("utf-8"))

def sendmsg (msg):
    global ircsock
    ircsock.send (("PRIVMSG "+ "#e4e2e7343" +" :"+ msg + "\n").encode("utf-8"))

def send_warn_msg (msg):
    global ircsock
    ircsock.send (("PRIVMSG "+ "#e4e2e7343" +" :/me "+ msg + "\n").encode("utf-8"))
    
def sendprivatemsg (user, msg):
    global ircsock
    ircsock.send (("PRIVMSG "+ "#e4e2e7343" +" :/w " + user + " " + msg + "\n").encode("utf-8"))
    
def JoinChan (chan):
    global ircsock
    ircsock.send (("JOIN "+ chan +"\n").encode("utf-8"))

#---------------------------------------------------------------------

def KBot(kset):
    
    #initial irc socket
    global ircsock
    
    ircsock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    ircsock.connect ((server, port))
    ircsock.send ("PASS {}\r\n".format(private.PASS).encode("utf-8"))
    ircsock.send (("USER " + uname + " 2 3 " + realname + "\n").encode("utf-8"))
    ircsock.send (("NICK "+ botnick + "\n").encode("utf-8"))
    JoinChan (channel)          # Join channel
    #EnableIRCCMD()
    friend = 0
    #%H:%M:%S
    opentime = time.time()
    Log_year = strftime("%Y", gmtime())
    Log_mon = strftime("%m", gmtime())
    Log_day = strftime("%d", gmtime())
    Log = open("./chatlog/" + Log_year + "_" + Log_mon + "_" + Log_day + ".txt", "a")
    Log.write("Start time at : " + strftime("#%H:%M:%S", gmtime()) + "\n")
    
    #Main System
    while True:
    
        ircmsg = ircsock.recv (bufsize)
        ircmsg = ircmsg.strip ('\n\r'.encode("utf-8")).decode("utf-8")
        print(ircmsg)
        
        #每五分鐘, server會PING, 回應PONG就好
        if ircmsg.find ("PING :") != -1:
            ping()
        else:
            if ":e4e2e7343!e4e2e7343@e4e2e7343.tmi.twitch.tv JOIN #e4e2e7343" in ircmsg or ":e4e2e7343.tmi.twitch.tv 353 e4e2e7343 = #e4e2e7343 :e4e2e7343" in ircmsg:
                continue
            
            username = ircmsg.split(":")[1].split("!")[0].lower()
            message = ""
            ucmd = ""
            """if username[0:13] == "tmi.twitch.tv":
                continue
            for i in range(2, len(ircmsg.split(":"))):
                message = message + ircmsg.split(":")[2].lower()
            if message[0] == "!":
                ucmd = message[0:].split(" ")[0]
            
            thread.start_new_thread(kset.Check_viewers, (username,1,0,)) #檢查講話的人是不是新的人
            
            print ("For log " + username + ":" + message)
            Log.write(username + " : " + message)
            Log.write("\n")"""
            """--------------------------------------------------------"""
            
            #if username == message:
            #    thread.start_new_thread(Show_user, (kset.viewers[username], username,))
            #    #Show_user(username)
            ##我專用cmd
            #if username == "e4e2e7343":
            #    if message == "!exitbot":
            #        break
            #    #elif message == "!sroff":
            #    #    srflag = False
            #    #    sendmsg("點歌系統關閉")
            #    #elif message == "!sron":
            #    #    srflag = True
            #    #    sendmsg("點歌系統開啟")
            #    elif "!gamble" in message:
            #        kset.syscmd["gamble"].cdtime = int(message.split("|")[0].split("!gamble")[1])
            #        msgforgamble = start_gamble(kset.syscmd["gamble"].cdtime,message.split("|")[1], message.split("|")[2:])
            #        kset.syscmd["gamble"].recordtime = time.time()   
            #        for i in range(0, 5):
            #            gdg[i] = 0
            #        gamblingswitch = True       
            #    elif "!answer" in message:
            #        gamblingswitch = False
            #        if len(message.split("!answer")[1].split(" ")) == 2:
            #            thread.start_new_thread(gambleend, (kset, int(message.split("!answer")[1]),gdg,))   
            #            thread.start_new_thread(kset.saveviewers, ())                        
            #
            ##mod專用cmd
            ##print kest.mod
            #if username in kset.mod:
            #    if "!setgd" in message and len(message.split("!setgd")) == 2:
            #        if len(message.split("!setgd")[1].split(" ")) == 2:
            #            kset.syscmd["gdtime"].cdtime = int(message.split("!setgd")[1].split(" ")[1])
            #            sendmsg("google小姐cd設定為" + message.split("!setgd")[1].split(" ")[1] + "秒")
            #    if "!bb" in message and len(message.split("!bb")) == 2:
            #        if len(message.split("!bb")[1].split(" ")) == 2:
            #            print "/timeout " + message.split("!bb")[1].split(" ")[1] + " 600"
            #            sendmsg("/timeout " + message.split("!bb")[1].split(" ")[1] + " 600")
            #    if "!add" in message[:len("!add")] and len(message.split("!add")) == 2 and "!addcom" not in message:
            #        if len(message.split("!add")[1].split(" ")) == 3:
            #            thread.start_new_thread(addgold, (kset,message.split("!add")[1].split(" ")[1], int(message.split("!add")[1].split(" ")[2]),))
            ##if username == "unamnesia" or username == "e4e2e7343":
            #    """if "!addcom" in message[:7]:
            #        #!addcom !指令 !內容 其它不輸入都預設
            #        #-d
            #        #-l
            #        #-k
            #        cdtime = 5
            #        limit = 3
            #        kcost = 0
            #        if len(message.split(" !")) != 3:
            #            continue
            #        if "-d" in message:
            #            cdtime = int(message.split("-d")[1].split(" ")[0])
            #        if "-l" in message:
            #            limit = int(message.split("-l")[1].split(" ")[0])
            #        if "-k" in message:
            #            kcost = int(message.split("-k")[1].split(" ")[0])
            #        try:
            #            kset.usercmd[message.split(" !")[1]].reaction = ircmsg.split(":")[2].split(" !")[2].split(" -")[0]
            #            kset.usercmd[message.split(" !")[1]].cdtime = cdtime
            #            kset.usercmd[message.split(" !")[1]].limit = limit
            #            kset.usercmd[message.split(" !")[1]].kcost = kcost
            #        except:
            #            kset.usercmd[message.split(" !")[1]] = CMD(ircmsg.split(":")[2].split(" !")[2].split(" -")[0],cdtime,limit,kcost)"""
            ##elif 
            ##大家可以使用的cmd
            #"""ucmd = message[1:]"""
            #
            #if message[0] == "!":
            #    #print message
            #    #print message[1:]
            #    #print cmdset.name
            #    try:
            #        thread.start_new_thread(kset.usercmd[message[1:]].Act(kset.viewers[username]), ())
            #    except:
            #        pass
            #    #if kset.usercmd[message[1:]].Act():
            #
            #if "!晚安" == message[:len("!晚安")]:
            #    sendmsg(username.encode("utf-8","ignore") + "晚安, 聊天室大家一起對" + username.encode("utf-8","ignore") + "說晚安哦")
            #if "!老k" == message[:len("!老k")]:
            #    sendmsg("老K: 職業:巨人族, 失智:87, 嘴砲:99, 興趣: 宣揚邪教思想, 個性: 鐵(ㄔ)漢柔(ㄙㄜˋ)情")
            #if "齒輪" in message:
            #    kset.gear = kset.gear + 1
            #    gearf = open("./info.txt", "w")
            #    gearf.write(str(kset.gear))
            #    gearf.close()
            #    #sendmsg("本台已經收集" + str(gear) + "個齒輪, 讓我們招喚Mona姊  VoHiYo VoHiYo VoHiYo")
            #if "!kalpha" == message[:len("!kalpha")]:
            #    sendmsg("Kalpha: 職業:老K的mod, 年齡:0.6, 技能: 抓出所有潛水觀眾 個性:死要錢")
            #""""""
            #if "!roll" == message[:len("!roll")] and time.time() - kset.syscmd["rollcd"].recordtime > kset.syscmd["rollcd"].cdtime :
            #    thread.start_new_thread(say_garbage, (kset,username,googlelock,))
            #    kset.syscmd["rollcd"].recordtime = time.time()
            #if time.time() - kset.syscmd["gdtime"].recordtime  > kset.syscmd["gdtime"].cdtime :    
            #    if "!jp" in message:
            #        if len(message.split("!jp")) == 2:
            #            thread.start_new_thread(googletalk, (kset, username, "jp",message.split("!jp")[1], googlelock,))
            #            kset.syscmd["gdtime"].recordtime  = time.time()
            #    if "!tw" in message:
            #        if len(message.split("!tw")) == 2:
            #            thread.start_new_thread(googletalk, (kset, username, "tw",message.split("!tw")[1], googlelock,))
            #            kset.syscmd["gdtime"].recordtime = time.time()
            #    if "!yue" in message:
            #        if len(message.split("!yue")) == 2:
            #            thread.start_new_thread(googletalk, (kset, username, "yue",message.split("!yue")[1], googlelock,))            
            #            kset.syscmd["gdtime"].recordtime = time.time()
            #    if "!en" in message:
            #        if len(message.split("!en")) == 2:
            #            thread.start_new_thread(googletalk, (kset, username, "en",message.split("!en")[1], googlelock,))            
            #            kset.syscmd["gdtime"].recordtime = time.time()
            #    if "!ko" in message:
            #        if len(message.split("!ko")) == 2:
            #            thread.start_new_thread(googletalk, (kset, username, "ko",message.split("!ko")[1], googlelock,))            
            #            kset.syscmd["gdtime"].recordtime = time.time()
            #""""""
            #if "!give" in message:
            #    print len(message.split("!give")[1].split(" "))
            #    if len(message.split("!give")[1].split(" ")) == 3:
            #        thread.start_new_thread(givemoney, (kset, username,(message.split("!give")[1].split(" ")[1]),(message.split("!give")[1].split(" ")[2]),))
            #if gamblingswitch == True and "!gb" in message and "-" not in message:
            #    #print "=====" + message.split("!gb")[1] + "\n"
            #    #print int(message.split("!gb")[1])
            #    print len(message.split("!gb")[1].split(" "))
            #    if len(message.split("!gb")[1].split(" ")) == 3:                    
            #        thread.start_new_thread(gambleviewero, (kset, username,(message.split("!gb")[1].split(" ")[1]),(message.split("!gb")[1].split(" ")[2]),gdg,))
            #   
            #if "!友台" == message[:len("!友台")]:
            #    friend = random.randint(1,7)
            #    print friend
            #    thread.start_new_thread(kset.ad3, (friend,))
            #if "!nmw_tw" == message[:len("!nmw_tw")]:
            #    thread.start_new_thread(kset.ad3, (1,))
            #if "!玉花" == message[:len("!玉花")]:
            #    thread.start_new_thread(kset.ad3, (2,))
            #if "!番茄" == message[:len("!番茄")]:
            #    thread.start_new_thread(kset.ad3, (3,))
            #if "!大牛楠" == message[:len("!大牛楠")]:
            #    thread.start_new_thread(kset.ad3, (4,))
            #if "!妖乖" == message[:len("!妖乖")]:
            #    thread.start_new_thread(kset.ad3, (5,))
            #if "!清玉" == message[:len("!清玉")]:
            #    thread.start_new_thread(kset.ad3, (6,))
            #if "!英特衛" == message[:len("!英特衛")]:
            #    thread.start_new_thread(kset.ad3, (7,))
            #    ftemp = open("20180913temp.txt", "a")
            #    ftemp.write(username+"\n")
            #    ftemp.close()
            #if "!抽獎" == message[:len("!武俠乂")]:
            #    sendmsg("今天抽的是由天命奇御周邊畫卡, 畫冊, 地圖通通送給你!!")
            #    #sendmsg("https://wx.cubejoy.com/index.html")
            #    ftemp = open("20180913temp.txt", "a")
            #    ftemp.write(username+"\n")
            #    ftemp.close()
            #if "!天命奇御" == message[:len("!天命奇御")]: 
            #    sendmsg("http://fs.jslgame.com/ 武俠天命 由你開啟!!")
            #    sendmsg("今天抽的是由天命奇御周邊畫卡, 畫冊, 地圖通通送給你!!")
            #    ftemp = open("20180913temp.txt", "a")
            #    ftemp.write(username+"\n")
            #    ftemp.close()
            #if "!阿加雷斯特" == message[:len("!阿加雷斯特")]:
            #    sendmsg("阿加雷斯特戰記2(Agarest:Generations of War)延續1代風格，增加打擊感及可玩性")
            #    #ftemp = open("20180628temp.txt", "a")
            #    #ftemp.write(username+"\n")
            #    #ftemp.close()
            ##    recordtime ["gdtalk"] = time.time()        
            ##if scmp(message, "!quest"):
            ##    thread.start_new_thread(writefile, (username,message,))            
            #if "!賠率" == message[:len("!賠率")]:
            #    sts = ""
            #    for m in range(0,5):
            #        if gdg[m] != 0:
            #            sts = sts + str(m+1) + "下注金額" + str(gdg[m]) + " "
            #    sendmsg(sts)
            #    sendmsg(msgforgamble)
            ##if srflag == True:
            ##    if scmp(message, "!sr") and scmp(message, "sron") == False and scmp(message, "sroff") == False:
            ##        print len(message.split("!sr"))
            ##        if len(message.split("!sr")) == 2:
            ##            print message.split("!sr")[1]
            ##            thread.start_new_thread(dianger, (username,(ircmsg.split(":")[2].split("!songreq")[1])))
            #""""""    
            #if time.time() - kset.syscmd["gamble"].recordtime > kset.syscmd["gamble"].cdtime and gamblingswitch == True:
            #    gamblingswitch = False
            #    sendmsg("下好離手")
            #""""""
            #if "!uptime" == message:
            #    sendmsg("已經開台" + str((time.time()-opentime)/60) + "分鐘")
            #if "!laugh" == message:
            #    thread.start_new_thread(playsound, (kset,username,1,soundlock,))
            #if "!pi" == message:
            #    thread.start_new_thread(playsound, (kset,username,2,soundlock,))
            #if "!gan" == message:
            #    thread.start_new_thread(playsound, (kset,username,3,soundlock,))
            #if "咕嚕" in message:
            #    thread.start_new_thread(playsound, (kset,username,4,soundlock,))
            #if "!now" == message and time.time() - kset.syscmd["rollcd"].recordtime > kset.syscmd["rollcd"].cdtime:
            #    thread.start_new_thread(shownow, ())
            #    kset.syscmd["rollcd"].recordtime = time.time()
            #
            #backengine.setname(username, random.randint(1,3))
    Log.close()
    f = open("./setting/info.txt", "w")
    f.write(str(kset.gear))
    f.close()

def recount():
    f = open("views.csv", "r")
    rpt = open("views2.csv", "w")
    buf = f.readline()
    rpt.write(buf)
    
    for buf in f:
        if not buf:
            break
        buf2 = buf.replace("\n", "").split(",")
        buf2[1] = str(int(buf2[1]) + int(buf2[3]))
        buf2[2] = str(int(buf2[2]) + int(buf2[4]))
        if int(buf2[4]) == 0:
            buf2[7] = "1000"            
        buf2[3] = "0"
        buf2[4] = "0"
        for buf3 in buf2:
            rpt.write(buf3)
            rpt.write(",")
        rpt.write("\n")

if __name__ == '__main__':        
    kset = KSET()
    #try:            
    KBot(kset) 
        #kset.saveviewers()
    #except:
        
    """kset.saveviewers()
    f = open("./setting/info.txt", "w")
    f.write(str(kset.gear))
    f.close()"""
    exit(0)                     # Exit with success status