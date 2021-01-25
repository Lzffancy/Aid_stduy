import requests
import time
import re
import os


# 获取所有IP
def __ip(url, headers):
    response = requests.get(url, headers=headers)
    html = response.text
    ip_list = re.findall(r'<td>(\d+\.\d+\.\d+\.\d+)</td>', html)
    ip_port = re.findall(r'<td>(\d+)</td>', html)
    _https = re.findall(r'<td class="country">(.+)</td>\s*<td>(\w+)</td>', html)
    _ip = []
    for i in range(len(ip_list)):
        if _https[i][0] == '高匿' and _https[i][1] == 'HTTPS':
            _ip.append(ip_list[i] + ':' + ip_port[i])
    return _ip


# 获取可用IP
def _https():
    ip_list = __ip('https://www.xicidaili.com/nn/', headers=headers)
    count = 0
    for i in ip_list:
        count += 1
        try:
            proxies = {
                'https': f'http://{i}'
            }
            url = 'https://httpbin.org/get'
            requests.get(url, headers=headers, proxies=proxies)
        except:
            print(f'| --- 获取第{count}个IP({proxies["https"][7:]})失效...... \n| --- 继续尝试获取有效IP......')
            continue
        yield proxies


# 访问首页
def access(url, headers, ip=None):
    response = requests.get(url, headers=headers, proxies=ip)
    html = response.text
    page = re.findall(r'href=\'.+/page/(.+)/\'', html)[-1]
    while True:
        print('\n| {:-^81} '.format(' 合计总页数 : ' + page + ' 页 '))
        try:
            ask = input('| --请输入你所需查看目录的页码：')
            if not (0 < int(ask) <= int(page)):
                raise ValueError
            break
        except ValueError:
            print('| ---错误：你输入的值不在范围内或输入的值有误！')
    url = f'https://www.mzitu.com/page/{ask}/'
    response = requests.get(url, headers=headers, proxies=ip)
    html = response.text
    return html


# 爬取图片url及图片标题
def photo_url(html):
    photo_urls = re.findall(r'<li><a href="(.+)" .+<img', html)
    titles = re.findall(r'data-original=\'.+ alt=\'(.+)\' w', html)
    return zip(titles, photo_urls)


# 打印专辑图库，用户选择并下载图库
def photo_choose(group, page, path):
    print('| {:-^81} '.format(' 所在目录页 : ' + page + ' 页 '))
    for i in range(len(group)):
        print('| {:-^6}> {:<} '.format(i, group[i][0]))
    print('| {:-^81} '.format(' 当前所在页 : ' + page + ' 页 '))
    while True:
        try:
            choose = input('| ---请输入你要Download的图库标号,输入"Return"返回上一步：')
            if choose == 'Return':
                break
            elif not (0 <= int(choose) < len(group)):
                raise ValueError
            break
        except ValueError:
            print('| ----错误：你输入的编号超出范围或输入错误！')
    if choose != 'Return':
        try:
            if os.getcwd() != path:
                os.chdir(os.pardir)
            os.mkdir(f'{group[int(choose)][0]}')
        except OSError:
            pass
        os.chdir(f'{group[int(choose)][0]}')
    return choose


# 获取原图片url，并保存
def save_original(count, group, headers, ip=None):
    photo_url = group[count][1]
    response = requests.get(photo_url, headers=headers, proxies=ip).text
    page = max(list(map(int, re.findall(group[count][1] + r'/(\d+)', response))))
    judge = 1
    for i in range(1, page + 1):
        url = photo_url + f'/{i}'
        rep = requests.get(url, headers=headers, proxies=ip).text
        add_page_photo = int(re.findall(r'><span>(\d+)</span></a>', rep)[-1])
        try:
            photo_urls = re.findall(r'<img class=.+ src="(.+\.jpg)" alt=', rep)
            photo_urls[0]
        except IndexError:
            print('| ---此图片专辑消失了，跳过此专辑下载...')
            break
        if not (i % 10) and judge != 'F':
            judge = input(f'| ---当前已经下载了{i - 1}张，退出当前专辑下载，返回目录页请输入<R> ; 取消此次下载询问输入<F> 并继续下载 ; 继续下载任意输入：')
            if judge == 'R':
                print('| ----正在返回目录......')
                break
        print('| ---正在准备下载条件中...  ', end='')
        save_photo(photo_urls[0], group[count][0], headers, i, add_page_photo, ip)


# 保存图片，显示下载进度条
def save_photo(url, title, headers, count, page, ip=None):
    with open(title + f'{count}.jpg', 'wb') as f:
        response = requests.get(url, headers=headers, stream=True, proxies=ip)
        chunk_size = 50
        size = 0
        content_size = int(response.headers['content-length'])
        _temp = page-count
        if _temp == -1:
            _temp = 0
        print('[文件大小]{:.2f}KB  正在下载第 {} 张  本专辑还剩 {} 张'.format(content_size / (chunk_size*2*10.24),count,_temp))
        start = time.time()
        for data in response.iter_content(chunk_size=chunk_size):
            f.write(data)
            size += len(data)
            print('\r' + '| --- 下载进度 %s%.2f%%' % ('>' * int(size * 50 / content_size), float(size / content_size * 100)),
                  end='')
        end = time.time()
        print('   下载完成！用时%.2f秒' % (end - start))


# 调用主程序
def main(url, headers):
    print('\n| {:-^84} |'.format('<  抓 M M 机 2.5  >'))
    print('| {:-^81} |'.format('< 请 <评分> 后使用 >'))
    path = os.getcwd()
    print('| {:-^73} |\n|\n| --- 楼主求<评分>，各位绅士别当白嫖怪好吗~ \n| '.format('< Ps：该爬虫仅供学习、娱乐 分享于：FishC论坛 by:Twilight6 >'))
    print('| --- 提示：若不是大量下载，不必使用IP代理，不过听说给 <!本帖子评分!> 后会给你的IP加速哦！\n|')
    ask = input('| --- 是否IP代理(高匿)，输入‘Yes’使用代理，任意输入则不使用(IP代理速度较慢) ：')
    if ask == 'Yes':
        print('| --- 正在获取一个可用IP地址,请稍等......')
        start = time.time()
        proxies = next(_https())
        end = time.time()
        print('| --- 成功获取一个可用IP地址:[{}],获取耗时{:.2f}秒...'.format(proxies['https'][7:],end-start))
    else:
        proxies = None
    print('|\n|\n| --------------- |食用说明')
    print('| --------------- |1.若您使用的是代理IP，则访问速度和代理IP的具体状态有关与你本机的网速无关')
    print('| --------------- |2.输入后回车若无反应，请稍等片刻，访问速度快慢有很多种因素')
    print('| --------------- |3.输入你想访问的页数，回车即可显示该页所有专辑图库')
    print('| --------------- |4.输入显示后的专辑编号，即可开始下载                     by:Twilight\n|\n| --- 正在访问网页中......\n|',end='')

    while True:
        try:
            html = access(url, headers, proxies)
            group = list(photo_url(html))
            page = re.findall(r'aria-current=.+>(\d+)', html)[0]
            choose = photo_choose(group, page, path)
            if choose == 'R':
                continue
            save_original(int(choose), group, headers, proxies)
        except:
            print('| ---部分图片下载中断，代理失效，重新获取代理中...')
            start = time.time()
            proxies = next(_https())
            end = time.time()
            print('| --- 成功获取一个可用IP地址:[{}],获取耗时{:.2f}秒...'.format(proxies['https'][7:], end - start))

base_url = 'https://www.mzitu.com/'
headers = {
    'Referer': 'https://www.mzitu.com/',
    'Sec-Fetch-Dest': 'image',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

if __name__ == '__main__':
    main(base_url, headers)
