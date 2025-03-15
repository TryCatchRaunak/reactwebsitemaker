#!/usr/bin/env python
import sys
import os
import warnings

from datetime import datetime

from crew import Websitemaker

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


os.system('python pdf_to_txt.py')


def setup():
    print("Setting up files... 📂")
    os.system('npm create vite@latest sample -- --template react')
    os.chdir('sample')
    print("Installing dependencies... 📦")
    os.system('npm install')
    os.system('npm install react-router-dom')
    os.system('npm install tailwindcss @tailwindcss/vite')


def deploy():
    print("Deploying website... 🚀")
    os.chdir('sample')
    print("Website is live... 🌐")
    os.system('npm run dev')

def run():
    print("Running the crew... 🚢")
    print("Development in Progress... 🚧")
    Websitemaker().crew().kickoff()


setup()
run()
deploy()