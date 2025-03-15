#!/usr/bin/env python
import sys
import os
import warnings

from datetime import datetime

from crew import Websitemaker

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def setup():
    os.system('npm create vite@latest sample --template react-js')
    os.chdir('sample')
    os.system('npm install')
    os.system('npm install react-router-dom')
    os.system('npm install tailwindcss @tailwindcss/vite')


def deploy():
    os.system('npm run dev')

def run():
    """
    Run the crew.
    """
    try:
        Websitemaker().crew().kickoff()
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


setup()
run()
deploy()