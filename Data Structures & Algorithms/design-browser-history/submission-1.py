class BrowserNode:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None
        self.distance_to_head = 0

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = BrowserNode(homepage)
        self.tail = BrowserNode("last_page")

        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.distance_to_head = 1

        self.on_page_node = self.head
        self.total_pages = 1

    def visit(self, url: str) -> None:
        # Create new node
        new_browser_node = BrowserNode(url)

        # Connect new nodes to the chain
        new_browser_node.prev = self.on_page_node
        new_browser_node.next = self.tail
        new_browser_node.distance_to_head = self.on_page_node.distance_to_head + 1

        #Disconnect the existing forward chain
        forward_page = self.on_page_node.next
        last_page = self.tail.prev

        forward_page.prev = None
        last_page.next = None

        # Connecting the on page and tail to new node
        self.on_page_node.next = new_browser_node

        self.tail.prev = new_browser_node
        self.tail.distance_to_head = new_browser_node.distance_to_head + 1

        # Updating new on page node
        self.on_page_node = new_browser_node
        self.total_pages = self.tail.distance_to_head

    def back(self, steps: int) -> str:
        print(f"Going back {steps} steps from {self.on_page_node.url}")
        print(f"Distance to head: {self.on_page_node.distance_to_head}, Total pages: {self.total_pages}")
        if steps >= self.on_page_node.distance_to_head:
            self.on_page_node = self.head
        else:
            for _ in range(steps):
                self.on_page_node = self.on_page_node.prev
        
        return self.on_page_node.url
        
    def forward(self, steps: int) -> str:
        print(f"Going forward {steps} steps from {self.on_page_node.url}")
        print(f"Distance to head: {self.on_page_node.distance_to_head}, Total pages: {self.total_pages}")
        if steps > (self.total_pages - self.on_page_node.distance_to_head-1):
            self.on_page_node = self.tail.prev
        else:
            for _ in range(steps):
                self.on_page_node = self.on_page_node.next
        return self.on_page_node.url
        
    def display(self):
        current = self.head
        print()
        print("Total Pages:", self.total_pages)
        while current:
            if current == self.on_page_node:
                print(f"URL: {current.url}, Distance to Head: {current.distance_to_head} <-- Current Page")
            else:
                print(f"URL: {current.url}, Distance to Head: {current.distance_to_head}")
            current = current.next
