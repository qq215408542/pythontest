import requests

class RequestsUtil:
    sess = requests.session()

    # 统一请求封装
    def all_send_requests(self,**kwargs):
        res = RequestsUtil.sess.request(**kwargs)
        return res