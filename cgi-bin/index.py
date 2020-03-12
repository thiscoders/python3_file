#!/usr/bin/python3
# coding=utf-8

html_content = '''
<html>
<head>
    <meta http-equiv="content-type" content="txt/html; charset=utf-8">
    <title>file upload</title>
</head>
<style>
    .box {
        width: 300px;
        height: 120px;
        border: 2px solid yellowgreen;
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        right: 0;
        margin: auto;
    }
</style>

<body>

    <div>
        <form action="http://localhost:8000/cgi-bin/server.py" method="post" enctype="multipart/form-data">
            <table class="box">
                <tr>
                    <th><label for="file">文件:</label></th>
                    <th><input name="uploadfile" id="file" type="file"/></th>
                </tr>
                <tr>
                    <th><label for="password">口令:</label></th>
                    <th><input name="password" id="password" type="password"/></th>
                </tr>
                <tr>
                    <th colspan="2"><input type="submit" name="submit" value="提交"/></th>
                </tr>
            </table>
        </form>
    </div>

</body>

</html>
'''
print(html_content)

