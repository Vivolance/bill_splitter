from typing import List, NewType

from pydantic import BaseModel


ItemName = NewType("ItemName", str)
PeopleName = NewType("PeopleName", str)


class ItemToSplit(BaseModel):
    name: ItemName
    price: float
    people: List[PeopleName]


class ItemsToSplit(BaseModel):
    items: List[ItemToSplit]


class PeopleBill(BaseModel):
    name: PeopleName
    bill: float
    items: List[ItemToSplit]


class Bill(BaseModel):
    people_bills: List[PeopleBill]