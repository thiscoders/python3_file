#!/usr/bin/python3
# coding=utf-8
# Import modules for CGI handling 
import cgi, os
import cgitb
cgitb.enable()
form = cgi.FieldStorage()

set_password = 'hello1#'

# verity password
password = form['password']
if password.value != set_password:
   print('Content-type:text/html;charset=utf-8 \n\n')
   print('口令错误!')
else:
   # Get filename here.
   fileitem = form['uploadfile']
   # Test if the file was uploaded
   if fileitem.filename:
      # directory traversal attacks
      fn = os.path.basename(fileitem.filename)
      # get store path  and save it 
      open(os.getcwd()+'/files/' + fn,'wb').write(fileitem.file.read())
      message = fn + ' 上传成功!'
   else:
      message = '没有选择文件!'
   print('Content-type:text/html;charset=utf-8 \n\n')
   print('%s' % message)
