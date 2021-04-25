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
        if self.item["id"] is None:
            temp = self.item
            temp.pop("id")
        return temp

    def setTitle(self, updateTitle: str):
        self.item.title = updateTitle
