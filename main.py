#!/usr/bin/env python
import sys
import os
import warnings

from datetime import datetime

from crew import Websitemaker

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


os.system('python pdf_to_txt.py')


def setup():
    os.system('npm create vite@latest sample --template react-js')
    os.chdir('sample')
    os.system('npm install')
    os.system('npm install react-router-dom')
    os.system('npm install tailwindcss @tailwindcss/vite')


def deploy():
    os.chdir('sample')
    os.system('npm run dev')

def run():
    Websitemaker().crew().kickoff()


setup()
run()
deploy()