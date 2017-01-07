from helpers.os import OS_Info_Extractor, OS_Info_Extractor_Factory

import os
import datetime
import time


class Tracker(object):
  def __init__(self, opsys, logpath):
    try:
      assert os.path.isdir(os.path.dirname(logpath))
    except AssertionError:
      print "Tracker failed to initialize (log path does not exist)"
    self.log_fd = open(logpath, 'a')
    self.pid = None
    self.OS_Info_Extractor = OS_Info_Extractor_Factory.OS_Info_Extractor_Factory().create_info_extractor(opsys)

  def activate(self):
    #self.pid = __spawn_tracker(os, logpath)		
    self.__track(self.log_fd)

  def pause(self):
    # pause
    #self.pid
    return 

  def resume(self):
    #self.pid
    return

  def deactivate(self):
    # deactivate
    #self.pid
    self.log_fd.close()
    return

  def __spawn_tracker(self):
    #p = Process(target = __track, args = ())
    return

  def __track(self, log_fd):	
    prev_active_app = None	
    while True:
      app, path, details = self.OS_Info_Extractor.get_active_app()
      if app != prev_active_app:
        cur_time = datetime.datetime.now().strftime('%s')					
        
        # log
        # TODO: async?
        log_fd.write(str(cur_time) + ',' + str(app) + ',' + str(path) + ',' + str(details) + '\n')
        log_fd.flush()

        prev_active_app = app
      time.sleep(1)
