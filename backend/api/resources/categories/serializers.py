from flask_restful import fields

CategorySerializer = {
    "id": fields.String,
    "main_category_id": fields.Integer,
    "name": fields.String
}

ListEntry = {
    "id": fields.String,
    "main_category_id": fields.String,
    "name": fields.String
}

ListSerializer = {
    "cid": fields.String,
    "total": fields.Integer,
    "previous": fields.String,
    "next": fields.String,
    "results": fields.List(fields.Nested(ListEntry)),
}
