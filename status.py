import os

from postmarker.core import PostmarkClient

def touch(path):
  with open(path, 'a'):
    os.utime(path, None)
    
ip = '192.168.0.1'
response = os.system("ping -c 1 " + ip)
email = 'you@email.com'
APIToken = 'your-t0ken'
subjectOn = '[ONLINE] Device name'
subjectOff = '[OFFLINE] Device name'

if response == 0:
  if os.path.isfile(ip):
    os.remove(ip)
    postmark = PostmarkClient(token=APIToken)
    postmark.emails.send(
      From=email,
      To=email,
      Subject= subjectOn + ip,
      HtmlBody='<html><body>' + ip + ' is back online</body></html>'
    )
else:
  if not os.path.isfile(ip):
    touch(ip)
    postmark = PostmarkClient(token=APIToken)
    postmark.emails.send(
      From=email,
      To=email,
      Subject= subjectOff + ip,
      HtmlBody='<html><body>' + ip + ' is back down!</body></html>'
    )
