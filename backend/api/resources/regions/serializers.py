from flask_restful import fields

RegionSerializer = {
    "id": fields.String,
    "country": fields.String,
    "name": fields.String,
}

ListEntry = {"id": fields.String, "country": fields.String, "name": fields.String}

ListSerializer = {
    "cid": fields.String,
    "total": fields.Integer,
    "previous": fields.String,
    "next": fields.String,
    "results": fields.List(fields.Nested(ListEntry)),
}
