#!/usr/bin/env python3
import sys
sys.path.append('../')

from ClassScan.core.client import sms

def main():
    text = sms()
    text.message('hello', '+12142360479')

main()