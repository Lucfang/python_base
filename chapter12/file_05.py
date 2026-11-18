"""下载多个图片"""
import aiohttp
import asyncio


async def download_picture(session, url):
    print(f'开始下载：{url}')
    # 发送网络请求,获取这张图片,请求发出去后，要等待服务器将数据返回，等待的这段使劲就是IO等待
    response = await session.get(url)
    # 等待数据(图片数据可能分多次传输，需要等待数据全部读完，等的这段事件也是IO等待)
    content = await response.read()
    # print(response.content)
    print('下载完毕')
    # 保存图片到本地
    with open(url[-10:] + '.png', 'wb') as f:
        f.write(content)
    #释放资源连接(告诉 aiohttp, 这个连接我不用了，你可以回收了)
    await response.release()


async def main():
    url_list = [
        'https://fastly.picsum.photos/id/237/400/300.jpg?hmac=32RuLp2fb9I2fzPP3U-6REXQ6sZAbN8ML7_dt3R7wQ8',
        'https://fastly.picsum.photos/id/10/400/300.jpg?hmac=LyrDRcAvj_Z4a9nwJxStHJf1g2cEqvFZaq1IKjgvc1w',
        'https://fastly.picsum.photos/id/1000/400/300.jpg?hmac=40cGFk0ZhjB5ipgEKovti4co8gxPPfONDK5FP76cArM'
    ]
    # 创建会话对象(发请求的工具)
    session = aiohttp.ClientSession()

    # 创建多个协程对象
    coroutine_list = [download_picture(session, url) for url in url_list]
    # 将多个协程对象交给事件循环
    await asyncio.gather(*coroutine_list)
    # 关闭会话
    await session.close()

# 将协程对象交给循环事件
asyncio.run(main())

