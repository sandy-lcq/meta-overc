#!/usr/bin/python3 -Es

import sys, os
import subprocess
import Overc

if __name__ == '__main__':
    overc=Overc.Overc()
    overc.agency.clean_essential()
    overc.agency.clean_container() 
