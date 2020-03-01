import urllib.request
import urllib.parse

headers = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.8",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":"anonymid=j0xsmf1yk8whx3; _r01_=1; depovince=SX; jebecookies=9125cf29-03f3-461d-845d-18a4282ddfb3|||||; JSESSIONID=abcV_KU3kswN698t8aT2v; jebe_key=d28ff8a7-07d5-4605-ab29-5710cb0f09a0%7Cfc6e0a34e4d909c6eef4a9d2b7bca03d%7C1499836771802%7C1%7C1501846292782; ick_login=53b10f3e-bdb4-45f6-ac49-f3f55cdcec09; _de=DB9E61F3CFF67E7EC894EBF6D8B726C8; p=333847bf944a1daf44ac12f8f7cb34b01; ap=946224841; first_login_flag=1; ln_uact=15035917897; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=35a2b3e4441881b396e45fa86ece9bf81; societyguester=35a2b3e4441881b396e45fa86ece9bf81; id=946224841; xnsid=52fc00ea; loginfrom=syshome; vip=1; XNESSESSIONID=bff15d6f845c; BAIDU_SSP_lcr=https://www.baidu.com/link?url=jPprGu6STQqD_o5Md_eYRua0ULywTaq0id6nVdw7W_y&wd=&eqid=ccad487100002f870000000359845c34; ch_id=10050; wp_fold=0",
"Host":"www.renren.com",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
}
#headers = urllib.parse.urlencode(headers)

url = "http://www.renren.com/946224841/profile"


request= urllib.request.Request(url,headers =  headers)

response = urllib.request.urlopen(request)

print(response.read().decode("utf-8"))