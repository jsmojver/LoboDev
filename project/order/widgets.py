from django.forms import Widget
from django.forms.widgets import  flatatt

class AutoselectForeign(Widget):
  def __init__(self, *args, **kwargs):
    """A widget that ...
    """
    self.key_attrs = {}
    self.val_attrs = {}
    if "key_attrs" in kwargs:
      self.key_attrs = kwargs.pop("key_attrs")
    if "val_attrs" in kwargs:
      self.val_attrs = kwargs.pop("val_attrs")
    Widget.__init__(self, *args, **kwargs)

    def render(self, name, value, attrs=None):
        """Renders this widget into an html string
        """


