import markdown
import argparse
import logging
import requests
import sqlite3 as sql
import os 

HEADER_HTML = ''
FOOTER_HTML = ''
CSS_NORMILZE = ''
INDEX_JS = ''

def init_cliBlogGenerator():
    return

def process_listdir(filespath, outputpath):
    markdown_files = os.listdir(filespath)
    html_files = os.listdir(outputpath)
    html_files = [i.split('.')[0] for i in html_files]
    process_files = [f'{filespath}\{file}' for file in markdown_files if file.split('.')[0] not in html_files]
    for file in process_files:
        outname = f'{outputpath}\{file.split('.')[0]}.html'
        with open(file,"r", encoding='utf-8') as input:
            text = input.read()
        html = markdown.markdown(text)
        with open(outname, "w",encoding='utf-8', errors='xmlcharrefreplace') as output:
            output.write(html)
    return

def app():
    return

if __name__ == '__main__':
    app()