from flask import Flask, request, jsonify
import json

app = Flask(__name__)

items = [
    {"id":"1","name":"Milo","category":"1","price":"20.5","instock":"100"},
    {"id":"2","name":"Coffee","category":"2","price":"30.5","instock":"200"},
    {"id":"3","name":"Tea","category":"3","price":"25.5","instock":"300"},
]

nextItemId = 4

def _find_next_id(id):
    data = [x for x in items if x["id"]==id]
    return data

#GET - REST APIs
@app.route("/items", methods=["GET"])
def get_item():
    return jsonify(items)

#GET - by ID
@app.route("/items/<id>", methods=["GET"])
def get_item_id(id):
    data = _find_next_id(id)
    return jsonify(data)

def get_item(id):
  return next((x for x in items if x["id"] == id), None)

def item_is_valid(item):
  for key in item.keys():
    if key != "name":
      return False
  return True

@app.route("/items", methods=["POST"])
def post_item():
    id = request.form.get("id")
    name = request.form.get("name")
    category = request.form.get("category")
    price = request.form.get("price")
    instock = request.form.get("instock")

    new_data = {
        "id": id,
        "name": name,
        "category": category,
        "price": price,
        "instock": instock
    }

    if (_find_next_id(id)):
        return {"error": "Bad Request"}, id
    else:
        items.append(new_data)
        return jsonify(items)

@app.route('/items/<id>', methods=["PUT"])
def update_item(id):
    global items
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')
    update_data = {
        "name" : name,
        "category": category,
        "price": price,
        "instock": instock
    }
    for item in items:
        if id == item.get("id"):
            item["name"] = str(name)
            item["category"] = str(category)
            item["price"] = str(price)
            item["instock"] = str(instock)
            return jsonify(items)
    else:
        return "Error", 404

@app.route('/items/<id>', methods=["PATCH"])
def patch_item(id):
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')
    update_data = {
        "name" : name,
        "category": category,
        "price": price,
        "instock": instock
    }
    for item in items:
        if id == item.get("id"):
            item["name"] = str(name)
            item["category"] = str(category)
            item["price"] = str(price)
            item["instock"] = str(instock)
            return jsonify(items)
    else:
        return "Error", 404
        
@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
  global items
  item = get_item(id)
  if item is None:
    return jsonify({ 'error': 'Item does not exist.' }), 404

  items = [x for x in items if x['id'] != id]
  return jsonify(" Successfully deleted item "), 200

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=5000, debug=True)