#!/user/bin/python
# -*- coding:utf-8 -*-
import requests
class cxddlb(object):
    def ddlb(self,a,b):
        url='https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderList'
        head={
            'x-dealer-code':'2100005',
            'x-position-code':'D_PO_1028',
            'x-resource-code':'pol4s_partOrder_orderList',
            'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
            'x-user-code':'dhxc1u',
            'x-access-token':'0da5606a534fa727dfd7f502df38be65',
            'Content-Type':'application/json'
            }
        body='{"pageNum": %s,"pageSize": %s, "queryTerms":{"orderType":"","orderStatus":"","orderDelayFlag": "","orderNo":"","startReportDate": "","endReportDate": ""}}' %(a,b)
        body=body.encode('utf-8')
        res=requests.post(url=url,headers=head,data=body)
        return res.json()
if __name__=='__main__':
    ss=cxddlb()
    a=ss.ddlb(1,10)
    print(a)