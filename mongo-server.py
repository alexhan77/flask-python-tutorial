import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.operators
collection = db.op

floor_division = {
  "name": "Floor Division",
  "description": "Division that rounds down to the nearest integer. Also known as integer division.",
  "symbol": "//",
  "example": "3 // 2 == 1",
  "uses": "A common situation we might see this operator is when we need to calcuate a list index, which will need to be a whole number. For example, perhaps we are trying to find the middle index of a list, but there are an even number of elements. In this case, we could use floor division to select the leftmost element in the list by default."
}
addition = {
  "name": "Add",
  "description": "Add that rounds down to the nearest integer. Also known as integer division.",
  "symbol": "//",
  "example": "3 + 2 = 5",
  "uses": "A common situation we might see this operator is when we need to calcuate a list index, which will need to be a whole number. For example, perhaps we are trying to find the middle index of a list, but there are an even number of elements. In this case, we could use floor division to select the leftmost element in the list by default."
}
subtraction = {
  "name": "Sub",
  "description": "Sub that rounds down to the nearest integer. Also known as integer division.",
  "symbol": "//",
  "example": "3 - 2 = 1",
  "uses": "A common situation we might see this operator is when we need to calcuate a list index, which will need to be a whole number. For example, perhaps we are trying to find the middle index of a list, but there are an even number of elements. In this case, we could use floor division to select the leftmost element in the list by default."
}

db.op.insert_many([floor_division, addition, subtraction])