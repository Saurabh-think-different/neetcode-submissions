class Observer(ABC):
    @abstractmethod
    def notify(self, itemName: str) -> None:
        pass

class Customer(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications = 0

    def notify(self, itemName: str) -> None:
        self.notifications += 1

    def countNotifications(self) -> int:
        return self.notifications

class OnlineStoreItem:
    def __init__(self, itemName: str, stock: int) -> None:
        self.itemName = itemName
        self.stock = stock
        self.subscribers = []

    def subscribe(self, observer: Observer) -> None:
        self.subscribers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self.subscribers.remove(observer)

    def updateStock(self, newStock: int) -> None:
        notify = False
        if self.stock == 0:
            notify = True
        self.stock = newStock
        if notify:
            for subscriber in self.subscribers:
                subscriber.notify(self.itemName)
