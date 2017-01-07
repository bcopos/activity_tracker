#!/usr/bin/env python

# Functions:
#   1. start/stop/pause tracker
#       - path for log file
#              - (start, end, duration, process_name, details)
#       - browser active tab url (chrome, firefox)
#   2. generate report (daily, weekly, monthly)


# determine OS type/version
from tracker import Tracker

import helpers
from helpers import utils

def main():
  os_type = utils.check_supported_os()
  try:
    assert os_type
  except:
    print "OS not supported, sorry!"   
  
  t = Tracker(os_type , '/Users/bcopos/Downloads/activity.log')
  t.activate()

main()
