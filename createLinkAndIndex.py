#!/usr/bin/python3.5
# vim : set fileencoding=utf-8 :
# script créé par LYD

"""
Permet de générer les liens pour le index.html de angel-tools.ddns.net
"""
import os

fileNames = os.listdir('.')
exeptions = ['.git', 'PrintX','ajouter ici les folders à ne pas linker']

html_str = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Angel Tools</title>
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js"></script>
    <script type="text/javascript" src="https://blockchain.info/Resources/js/pay-now-button.js"></script>
    <style>
        h1{
            text-align: center;
            font-family: Fertigo, Arial,sans-serif;
        }
         .menuLink{
             width:300px;
             margin: 0 auto;
             font-size: 16px;
             text-align: center;
         }
         .blockchain-btn{
             margin: 40px auto;
         }
         .blockchain.stage-begin{
             text-align: center;
         }
         .blockchain.stage-begin img{
            width: 154px;
         }
    </style>
</head>
<body>
    <h1>Angel Tools</h1>
    <div class="menuLink">
        <a href="http://angel-tools.ddns.net:8080/">nodeServer</a>
    </div>
"""

for fileName in fileNames:
    if os.path.isdir('./' + fileName) and fileName not in exeptions:
        html_str += '    <div class="menuLink">\n'
        html_str += '        <a href="http://angel-tools.ddns.net/' + fileName + '">' + fileName + '</a>\n'
        html_str += '    </div>\n'

html_str += """

    <div class="blockchain-btn"
        data-address="1P4qB7J5TAngP4n1QzjB4tReU4rVebfwr9"
        data-shared="false">
        <div class="blockchain stage-begin">
            <img src="https://blockchain.info/Resources/buttons/donate_64.png"/>
        </div>
        <div class="blockchain stage-loading" style="text-align:center">
            <img src="https://blockchain.info/Resources/loading-large.gif"/>
        </div>
        <div class="blockchain stage-ready">
            <p align="center">Please Donate To Bitcoin Address: <b>[[address]]</b></p>
            <p align="center" class="qr-code"></p>
        </div>
        <div class="blockchain stage-paid">
            Donation of <b>[[value]] BTC</b> Received. Thank You.
        </div>
        <div class="blockchain stage-error">
            <font color="red">[[error]]</font>
        </div>
    </div>
</body>
</html>
"""

Html_file= open("index.html","w")
Html_file.write(html_str)
Html_file.close()