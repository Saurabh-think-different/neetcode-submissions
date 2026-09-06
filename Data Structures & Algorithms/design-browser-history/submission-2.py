class BrowserNode:
    def __init__(self, url, prev = None, next = None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = BrowserNode(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = BrowserNode(url, self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url
        
    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url
        
    def display(self):
        pass
        
