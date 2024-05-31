import os,time
import requests
import random
g="\033[1;32m"  #----------green
try:
	import getuseragent
except ModuleNotFoundError:
	os.system('pip install getuseragent')
	os.system('clear')
	import getuseragent
from getuseragent import UserAgent
from rich.panel import Panel
def wait():
	for i in range(100):
		print(f"\n\n{g}[ + ] Wait 120 second For Next Submit : {i+1}/120", end='\r')
		time.sleep(1)
		os.system('clear')

#------------colour code -----------#
#-----------format colour code------------#
b="\033[1;34m"  #----------blue
bl="\033[1;30m"  #--------black
c="\033[1;36m"  #----------cyan

p="\033[1;35m"  #----------purple
r="\033[1;31m"  #----------red
y="\033[1;33m"  #----------yellow
w="\033[1;37m"  #----------white {end}
random_colour = [b, c, g]
ran = random.choice(random_colour)

#------------logo ------------#
logo = (f"""
{ran}-----------------------------------------------{w}
{c}888     888 888b    888  .d88888b.  
{c}888     888 8888b   888 d88P" "Y88b 
{c}888     888 88888b  888 888     888 
{c}888     888 888Y88b 888 888     888 
{c}888     888 888 Y88b888 888     888 
{c}888     888 888  Y88888 888     888 
{c}Y88b. .d88P 888   Y8888 Y88b. .d88P 
{c} "Y88888P"  888    Y888  "Y88888P"  
                                    
{ran}-----------------------------------------------{w}

 {c}Owner  : {ran}Uno Dos
 {c}Type   : {ran}TIKTOK FAKE VIEW
{ran}-----------------------------------{w}""")
def linex():
    print(f'{ran}-----------------------------------{w}')

def shoha_menu():
    B4="S4-"
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "5".join(uuid)
    print(logo)
    DARK=requests.get("https://github.com/Joshhi1/API.txt/tree/main").text
    if id in DARK:
        menu()
    else:
        os.system("clear")
        os.system("xdg-open https://www.facebook.com/61554782104701")
        time.sleep(3.0)
        
        os.system("clear")
        print(logo)
        print("{p}   {bl}[47m FIRST GET APPROVAL\3[00m\3[1;30m]")
        print ("")
        print("┌━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━┐ {r}│ NOTE : THAT IS PAID BECAUSE 100% OK ID JUST NOW LOGIN│{c}\━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━┘")
        print ("")
        print("                YOUR KEY IS NOT APPROVED ")
        print("               COPY AND SEND KEY TO ADMIN")
        print ("")
        print (" YOUR KEY : "+B4+id)
        name = input(" YOUR NAME : ")
        print ("")
        input(" PRESS ENTER TO SEND KEY")
        os.system("xdg-open https://www.facebook.com/61554782104701")
shoha_menu()

class TikTokBooster:
    def __init__(self):
        self.ua = UserAgent("ios").Random()
        self.base_url = 'https://api.likesjet.com/freeboost/3'

    def boost_video(self, user: str, link: str) -> dict:
        email = f"suyibislam{random.randint(10000,99999)}@gmail.com"
        headers = {
            "Host": "api.likesjet.com",
            "content-length": "137",
            "sec-ch-ua": "\"Google Chrome\";v\u003d\"119\", \"Chromium\";v\u003d\"119\", \"Not?A_Brand\";v\u003d\"24\"",
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "sec-ch-ua-mobile": "?1",
            "user-agent": self.ua,
            "sec-ch-ua-platform": "\"Android\"",
            "origin": "https://likesjet.com",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://likesjet.com/",
            "accept-language": "en-XA,en;q\u003d0.9,ar-XB;q\u003d0.8,ar;q\u003d0.7,en-GB;q\u003d0.6,en-US;q\u003d0.5"
        }
        data = {"link": link, "tiktok_username": user, "email": email}
        response = requests.post(self.base_url, json=data, headers=headers).json()
        return response

def main():
	print(logo)
	print(f"{y} ⟩⟩ ENTER YOUR TIKTOK USERNAME HERE ⬇️⬇️{w}")
	linex()
	print(f"{y} ⟩⟩ EXAMPLE »  @CHOKI «{w}") 
	linex()
	user = input(f' {ran}[?]TikTok UserName:{w} ')
	linex()
	link = input(f' {ran}[?]Video Link: {w}')
	booster = TikTokBooster()
	response = booster.boost_video(user, link)
	if response.get('status'):
		status = (f"{g}[√] Successfully 1000 View send{w}")
		print(f"{g}[√] Successfully 1000 View send{w}")
		wait()
		main()
	else:
		status = (f"{r}[‌#] SORRY I CAN'T SEND VIEW IN YOUR VIDEO{w}")
		print(f"{r}[‌#] SORRY I CAN'T SEND VIEW IN YOUR VIDEO{w}")
		wait()
		main()
if __name__ == "__main__":
	main()
