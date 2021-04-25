class TodoTask:

    def __init__(self, title: str, id=None):
        self.item = {
            "id": id,
            "Title": title
        }

    def getId(self):
        return self.item.id

    def getTitle(self):
        return self.item.Title

    def getTaskObject(self):
        return self.item

    def setTitle(self, updateTitle: str):
        self.item.title = updateTitle
