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
</head>
<body>

<div>
    <a href="http://angel-tools.ddns.net:8080/">nodeServer</a>
</div>
"""

for fileName in fileNames:
    if os.path.isdir('./' + fileName) and fileName not in exeptions:
        html_str += '<div>\n'
        html_str += '    <a href="http://angel-tools.ddns.net/' + fileName + '">' + fileName + '</a>\n'
        html_str += '</div>\n'

html_str += "</body></html>"

Html_file= open("index.html","w")
Html_file.write(html_str)
Html_file.close()