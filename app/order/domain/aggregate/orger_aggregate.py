from app.common.domain.entity import Entity
from app.order.domain.value_objects.id import ID
from app.order.domain.entities.order import Order
from app.deliver.domain.entities.deliver import Deliver
from datetime import date

class OrderAggregate(Entity):
    def __init__(self, id: ID, order: Order, deliver: Deliver):
        self.id = id
        self.order = order
        self.deliver = deliver

    @classmethod
    def create(cls, order_id: str, order_date: date, totalPrice: float, discount: bool, totalDiscount: float, deliver_id: str, state: str, city: str, township: str, street: str, status: str, deliver_date: date, type: str, agency: str):
        order = Order.create(order_id, order_date, totalPrice, discount, totalDiscount)
        deliver = Deliver.create(deliver_id, state, city, township, street, status, deliver_date, type, agency)
        return cls(id, order, deliver)
    
    def update(self, date: date = None, totalPrice: float = None, discount: bool = None, totalDiscount: float = None):
        self.order.update(date, totalPrice, discount, totalDiscount)

    def get(self):
        return self.order, self.deliver