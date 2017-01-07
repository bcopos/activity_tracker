import platform

SUPPORTED_SYSTEMS = {
  'darwin': ['10.12.2']
  }



def get_system_info():
  return (platform.system(), platform.dist(), platform.mac_ver()[0])

def check_supported_os():
  system, dist, mac_ver = get_system_info()
  if system.lower() in SUPPORTED_SYSTEMS.keys():
    if system.lower() == 'darwin':
      if mac_ver in SUPPORTED_SYSTEMS['darwin']:
        return system.lower()
    elif system.lower() == 'linux':
      pass #TODO
    elif system.lower() == 'windows':
      pass #TODO
    else:
      pass
  return None

  
