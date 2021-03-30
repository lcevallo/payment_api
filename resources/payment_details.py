from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.payment_details import PaymentDetails


class PaymentDetailResource(Resource):
    def get(self, payment_id):
        payment_detail = PaymentDetails.get_by_id(payment_detail_id=payment_id)

        if payment_detail is None:
            return {'message': 'Payment not found'}, HTTPStatus.NOT_FOUND

        return payment_detail.data(), HTTPStatus.OK

    def put(self, payment_id):
        json_data = request.get_json()
        payment_detail = PaymentDetails.get_by_id(payment_detail_id=payment_id)
        if payment_detail is None:
            return {'message': 'Payment not found'}, HTTPStatus.NOT_FOUND

        payment_detail.card_owner_name = json_data['card_owner_name']
        payment_detail.cardnumber = json_data['cardnumber']
        payment_detail.expiration_date = json_data['expiration_date']
        payment_detail.security_code = json_data['security_code']

        payment_detail.save()

        return payment_detail.data(), HTTPStatus.OK

    def delete(self, payment_id):
        payment_detail = PaymentDetails.get_by_id(payment_detail_id=payment_id)

        if payment_detail is None:
            return {'message': 'Payment not found'}, HTTPStatus.NOT_FOUND

        payment_detail.delete()
        return {}, HTTPStatus.NO_CONTENT


class PaymentDetailsListResource(Resource):
    def get(self):
        payments = PaymentDetails.get_all()
        data = []

        for payment in payments:
            data.append(payment.data())

        return {'data': data}, HTTPStatus.OK

    def post(self):
        json_data = request.get_json()
        card_owner_name = json_data.get('card_owner_name')
        cardnumber = json_data.get('cardnumber')
        expiration_date = json_data.get('expiration_date')
        security_code = json_data.get('security_code')

        if PaymentDetails.get_by_cardnumber(cardnumber):
            return {'message': 'El numero de tarjeta ya esta usado'}, HTTPStatus.BAD_REQUEST

        payment_details = PaymentDetails(
            card_owner_name=card_owner_name,
            cardnumber=cardnumber,
            expiration_date=expiration_date,
            security_code=security_code
        )

        payment_details.save()

        data = {
            'payment_detail_id': payment_details.payment_detail_id,
            'card_owner_name': payment_details.card_owner_name,
            'cardnumber': payment_details.cardnumber,
            'expiration_date': payment_details.expiration_date,
            'security_code': payment_details.security_code
        }
        return data, HTTPStatus.CREATED
