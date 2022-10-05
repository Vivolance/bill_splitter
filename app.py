import json
from typing import Dict, Any, List
from flask import Flask
from flask import request

from models.items_to_split import ItemsToSplit, Bill
from utils.split_bills import split_bill

app: Flask = Flask(__name__)


@app.route("/bill_splitter", methods=["GET"])
def bill_splitter() -> Dict[str, Any]:
    raw_data: bytes = request.data
    items_dict: Dict[List[Dict[str, Any]]] = json.loads(raw_data)
    items_to_split: ItemsToSplit = ItemsToSplit.parse_obj(items_dict)
    bill: Bill = split_bill(items_to_split)

    return bill.dict()


if __name__ == "__main__":
    app.run(port=5000)