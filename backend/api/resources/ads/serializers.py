from flask_restful import fields

AdSerializer = {
    "uuid": fields.String,
    "title": fields.String,
    "description": fields.String,
}

ListEntry = {"uuid": fields.String, "title": fields.String}

ListSerializer = {
    "total": fields.Integer,
    "previous": fields.String,
    "next": fields.String,
    "results": fields.List(fields.Nested(ListEntry)),
}
