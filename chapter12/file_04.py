"""下载多个图片"""
import requests

def download_picture(url):
    print(f'开始下载：{url}')
    # 发送网络请求。获取这张图片
    response = requests.get(url)
    # print(response.content)
    print('下载完毕')
    # 保存图片到本地
    with open(url[-10:]+'.png','wb') as f:
        f.write(response.content)

def main():
    url_list = [
        'https://fastly.picsum.photos/id/237/400/300.jpg?hmac=32RuLp2fb9I2fzPP3U-6REXQ6sZAbN8ML7_dt3R7wQ8',
        'https://fastly.picsum.photos/id/10/400/300.jpg?hmac=LyrDRcAvj_Z4a9nwJxStHJf1g2cEqvFZaq1IKjgvc1w',
        'https://fastly.picsum.photos/id/1000/400/300.jpg?hmac=40cGFk0ZhjB5ipgEKovti4co8gxPPfONDK5FP76cArM'
    ]
    for url in url_list:
        download_picture(url)

main()
