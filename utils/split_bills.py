from typing import Dict, List

from models.items_to_split import ItemsToSplit, Bill, PeopleName, ItemToSplit, PeopleBill


def _get_people_and_items_to_split(items_to_split: ItemsToSplit) -> Dict[PeopleName, List[ItemToSplit]]:
    """
    Store all items that a person is paying for in a List,
    and store the person's name as a key in the dictionary and the items as the value
    """
    people_and_items_to_split: Dict[PeopleName, List[ItemToSplit]] = {}
    for item_to_split in items_to_split.items:
        for people_name in item_to_split.people:
            people_and_items_to_split[people_name] = people_and_items_to_split.get(people_name, [])
            people_and_items_to_split[people_name].append(item_to_split)
    return people_and_items_to_split


def _calculate_bill(people_and_items_to_split: Dict[PeopleName, List[ItemToSplit]]) -> Bill:
    list_of_people_bill: List[PeopleBill] = []
    for people, items_to_split in people_and_items_to_split.items():
        people_total_bill: float = 0
        for item_to_split in items_to_split:
            people_total_bill += item_to_split.price / len(item_to_split.people)
        people_bill: PeopleBill = PeopleBill(
            name=people,
            bill=people_total_bill,
            items=items_to_split
        )
        list_of_people_bill.append(people_bill)
    return Bill(
        people_bills=list_of_people_bill
    )


def split_bill(items_to_split: ItemsToSplit) -> Bill:
    people_and_items_to_split: Dict[PeopleName, List[ItemToSplit]] = _get_people_and_items_to_split(items_to_split)
    bill: Bill = _calculate_bill(people_and_items_to_split)
    return bill
