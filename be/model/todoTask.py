class TodoTask:

    def __init__(self, title: str = None, _id=None):
        self.item = {
            "_id": _id,
            "Title": title
        }

    def getId(self):
        return self.item["_id"]

    def getTitle(self):
        return self.item["Title"]

    def getTaskObject(self):
        if self.item["_id"] is None:
            temp = self.item
            temp.pop("_id")
            return temp
        else:
            return self.item

    def setTitle(self, updateTitle: str):
        self.item["Title"] = updateTitle

    def setId(self, _id):
        self.item["_id"] = _id
