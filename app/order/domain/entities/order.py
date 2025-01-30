from app.common.domain.entity import Entity
from app.order.domain.value_objects.id import ID
from app.order.domain.value_objects.discount import Discount
from app.order.domain.value_objects.totalPrice import TotalPrice
from app.order.domain.value_objects.totalDiscount import TotalDiscount
from app.order.domain.value_objects.date import Date
from datetime import date

class Order(Entity):
    def __init__(self, id: ID, date: Date, totalPrice: TotalPrice, discount: Discount, totalDiscount: TotalDiscount):
        self._id = id
        self._date = date
        self._totalPrice = totalPrice
        self._discount = discount
        self._totalDiscount = totalDiscount

    @classmethod
    def create(cls, id: str, date: date, totalPrice: float, discount: bool, totalDiscount: float):
        id = ID.create(id)
        date = Date.create(date)
        totalPrice = TotalPrice.create(totalPrice)
        discount = Discount.create(discount)
        totalDiscount = TotalDiscount.create(totalDiscount)
        return cls(id, date, totalPrice, discount, totalDiscount)
    
    def update(self, date: date = None, totalPrice: float = None, discount: bool = None, totalDiscount: float = None):
        if date:
            self._date = Date.create(date)
        if totalPrice:
            self._totalPrice = TotalPrice.create(totalPrice)
        if discount:
            self._discount = Discount.create(discount)
        if totalDiscount:
            self._totalDiscount = TotalDiscount.create(totalDiscount)

    def get(self):
        return self
        
        