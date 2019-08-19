import requests

from bs4 import BeautifulSoup


def get_url(url, url_list):
    # url = 'http://www.gzhu.edu.cn/index/tzgg/27.htm'
    r = requests.get(url=url)
    r.encoding = 'utf-8'

    # r.text获得文本，r.content获得文件
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('li')
    print(links)
    main_url = 'http://www.gzhu.edu.cn/info/1185/'

    for link in links:
        a = link.a['href']
        print(a)
        b = str(a)
        c = b.split("/")
        if len(b.split("/")) >= 4:
            index = 0
            if len(c) == 4 :
                idex = 3
            else:
                index =4

            if c[index].endswith('.htm'):
                url_list.append(main_url + c[index])

    print(url_list)
    return


def main():
    SUM = 1
    url_list = []
    while SUM != 0:
        if SUM == 27:
            get_url("http://www.gzhu.edu.cn/index/tzgg/27.htm", url_list)
        if SUM != 27:
            get_url("http://www.gzhu.edu.cn/index/tzgg/" + str(SUM) + ".htm", url_list)

        SUM = SUM - 1
    print(url_list)
    print(len(url_list))


    return


if __name__ == '__main__':
    main()
