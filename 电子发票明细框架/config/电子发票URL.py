#!/user/bin/python
# -*- coding:utf-8 -*-
import requests
class fapiao(object):
    def jcsj(self,a,b,c):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/electricInvoiceDetail'
        head={
            'Content-Type':'application/json',
            'x-dealer-code':'2100001',
            'x-position-code':'D_PO_1028',
            'x-resource-code':'pol4s_partOrder_electricInvoiceDetail',
            'x-track-code':'4320e7d0 - cf0c - 7ba2 - b3fe - 1ecb1f15e394',
            'x-user-code':'dhxc1u',
            'x-access-token': '0da5606a534fa727dfd7f502df38be65'
            }
        body='{"pageNum": %s,"pageSize": %s,"queryTerms":{"billingNo":"%s"}}' %(a,b,c)
        body=body.encode('utf-8')
        res=requests.post(url=url,headers=head,data=body)
        return res.json()

if __name__=='__main__':
    ss=fapiao()
    a=ss.jcsj(1,10,'0914222771')
    print(a)