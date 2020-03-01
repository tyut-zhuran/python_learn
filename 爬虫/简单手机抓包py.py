import requests
import re
headers = {
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh-CN,zh;q=0.8",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":'d_c0="AFDCBn-NPguPToglBsp_7rt0w8Dg4DyQygA=|1485956402"; _zap=f1d7bd1c-97e2-4fa3-aee3-433f29ee69be; q_c1=59328672a6084e959044b30500ffa2c3|1503397148000|1485956401000; q_c1=59328672a6084e959044b30500ffa2c3|1506178289000|1485956401000; l_cap_id="ODNlY2ZiMDNlMDE5NDBiMjk0Nzk3YjI1YWQ4N2QwYzc=|1506911142|ef08711e7a06ef89bb4e8572ece73e123244ea49"; r_cap_id="MGU4NWNkYzA3NTBjNDA4OGI5MzcxY2IwMjdjYTkyM2U=|1506911142|90f88af3fc602185d7837747150855b156155259"; cap_id="OTQ1MTBkODhkODViNGZhNzliYTQyYTQ0YTZkMWJjZjM=|1506911142|07e0cf4d427e129993d9fe88a023071f764b79e4"; aliyungf_tc=AQAAAPy461TYlgkAzEwL3+MFG2YjJ8pU; __utma=51854390.2084450024.1485956407.1505273775.1507358729.14; __utmb=51854390.0.10.1507358729; __utmc=51854390; __utmz=51854390.1505273775.13.11.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.010--|2=registration_date=20160703=1^3=entry_date=20170201=1',
"Host":"www.zhihu.com",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
}
r = requests.get(r"https://www.zhihu.com/appview/question/34630803/answer/240611324?appview=1&config=%7B%22content_padding_top%22%3A200%2C%22content_padding_bottom%22%3A56%2C%22content_padding_left%22%3A16%2C%22content_padding_right%22%3A16%2C%22title_font_size%22%3A22%2C%22body_font_size%22%3A16%2C%22is_dark_theme%22%3Atrue%2C%22can_auto_load_image%22%3Atrue%2C%22app_info%22%3A%22OS%3DAndroid%26Release%3D6.0.1%26Model%3DMI%2B5s%26VersionName%3D4.54.1%26VersionCode%3D507%26Width%3D1080%26Height%3D1920%26Installer%3D%25E5%25B0%258F%25E7%25B1%25B3%25E5%2595%2586%25E5%25BA%2597%26WebView%3D55.0.2883.91%22%2C%22X-SUGER%22%3A%22SU1FST04NjM4MTcwMzcxNzk2NDg%3D%22%7D&type=0",
	headers = headers)
html = r.text

content = re.findall("<script>(.*)</script>",html)

print(content)