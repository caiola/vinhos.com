from flask_restful import fields

ListEntry = {"uuid": fields.String, "title": fields.String}

ListSerializer = {
    "total": fields.Integer,
    "previous": fields.String,
    "next": fields.String,
    "results": fields.List(fields.Nested(ListEntry)),
}
