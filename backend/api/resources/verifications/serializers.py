from flask_restful import fields

VerificationSerializer = {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "action": fields.String,
    "token": fields.String,
    "date_created": fields.Integer,
}

ListEntry = {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "action": fields.String,
    "token": fields.String,
    "date_created": fields.Integer,
}

ListSerializer = {
    "cid": fields.String,
    "total": fields.Integer,
    "previous": fields.String,
    "next": fields.String,
    "results": fields.List(fields.Nested(ListEntry)),
}
