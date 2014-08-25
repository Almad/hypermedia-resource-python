from attributes import AttributeItem
from dom import Collection

class InputCollection(Collection):

    def __init__(self):
        self.item = InputItem

class InputItem(AttributeItem):

    def __init__(self, name, value, **kwargs):
        super(InputItem, self).__init__(name, value=None, **kwargs)
        self._current_value = value
        self.placeholder = kwargs.get('placeholder', None)
        self.default_value = kwargs.get('default_value', None)
        self.options = OptionCollection()

    def changed(self):
        return self.value == self._current_value

class OptionCollection(Collection):

    def __init__(self):
        super(OptionCollection, self).__init__()
        self.item = OptionItem()

class OptionItem:

    def __init__(self, name, value, **kwargs):
        self.name = name
        self.value = value
