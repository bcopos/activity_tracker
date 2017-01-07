import abc

class OS_Info_Extractor(object):
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def get_active_app(self):
    pass
