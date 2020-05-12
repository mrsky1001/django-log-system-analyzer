class MenuItem:
    def __init__(self, name, function, component=None):
        if component is None:
            component = "settings.html"
        self.id = 0
        self.name = name
        self.function = function
        self.component = component


class MenuFactory:
    def __init__(self, title, list_items=None):
        if list_items is None:
            list_items = []
        self.getTitle = lambda: title
        self.list_items = list_items
