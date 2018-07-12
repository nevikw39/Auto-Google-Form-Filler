import lxml.html.soupparser as soupparser
import lxml.etree as etree
import requests
import random
proxies = {"https": "http://192.116.142.153:8080"}
x = dict()
x['entry.1193336520']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
x['entry.160839485']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
x['entry.2045780890']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
x['entry.1301574149']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
x['entry.1433934455']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
x['entry.42421302']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
x['entry.577564597']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
x['entry.1080377858']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
x['entry.1339362696']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
x['entry.16828446']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
x['entry.1188863233']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
x['entry.225982447']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
r = requests.post('https://docs.google.com/forms/d/e/1FAIpQLScfQx-f4aXO8ze9pvQMo73vMHUbQzHvuZZnfwxFLOznHbWl1A/formResponse', data = x, proxies=proxies)
root = soupparser.fromstring(r.text)
for i in root.xpath('//*[@class="freebirdFormviewerViewResponseConfirmationMessage"]'):
	print(i.text)
y = dict()
y['entry.1754591272']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
y['entry.1549440580']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
y['entry.1928020954']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
y['entry.964861325']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
y['entry.1348279102']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
y['entry.805255528']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
y['entry.1111198489']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
y['entry.449596388']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
y['entry.58943000']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
y['entry.1768452370']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
y['entry.52219496']=( random.choice(['沒意見','很讚','普通','很讚','普通']))
r1 = requests.post('https://docs.google.com/forms/u/1/d/e/1FAIpQLSd6OIrEW8XVQgNrdIe9NhX_rlGJ1cwERdVI_6txjdKInto0jA/formResponse', data = y, proxies=proxies)
root1 = soupparser.fromstring(r1.text)
for i in root1.xpath('//*[@class="freebirdFormviewerViewResponseConfirmationMessage"]'):
	print(i.text)
