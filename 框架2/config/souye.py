#!/user/bin/python
# -*- coding:utf-8 -*-
import requests
class xuexiao(object):
    def jichushuju(self,c):
        url='http://testsupport-be.haofenshu.com/v1/schools/infos?filterInput={}'.format(c)
        head={
            'Content - Type': 'application / x - www - form - urlencoded',
            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Cache - Control': 'max - age = 0',
            'Connection': 'keep - alive',
            'User - Agent': 'Mozilla / 5.0(WindowsNT10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 70.0.3538.77Safari / 537.36',
            'Cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'
        }
        res = requests.get(url=url, headers=head)
        html=res.content.decode('utf-8')
        return html
if __name__=='__main__':
    ss=xuexiao()
    a=ss.jichushuju(c)
    print(a)