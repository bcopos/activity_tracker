from Darwin_Info_Extractor import Darwin_Info_Extractor

compatible_os = {
  'darwin': Darwin_Info_Extractor
}

class OS_Info_Extractor_Factory():
  def create_info_extractor(self, os_type):
    return compatible_os[os_type]()
