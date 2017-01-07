from OS_Info_Extractor import OS_Info_Extractor
from AppKit import NSWorkspace

class Darwin_Info_Extractor(OS_Info_Extractor):
  def get_active_app(self):
    active_app = NSWorkspace.sharedWorkspace().activeApplication()
    details = [] #TODO
    return (active_app['NSApplicationName'], active_app['NSApplicationPath'], details)

