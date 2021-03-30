from extensions import db


class PaymentDetails(db.Model):
    __tablename__ = 'payment_details'

    payment_detail_id = db.Column(db.Integer, primary_key=True)
    card_owner_name = db.Column(db.String(100), nullable=False)
    cardnumber = db.Column(db.String(16), nullable=False)
    expiration_date = db.Column(db.String(5), nullable=False)
    security_code = db.Column(db.String(3), nullable=False)

    def data(self):
        return {
            'payment_detail_id': self.payment_detail_id,
            'card_owner_name': self.card_owner_name,
            'cardnumber': self.cardnumber,
            'expiration_date': self.expiration_date,
            'security_code': self.security_code
        }

    @classmethod
    def get_by_cardnumber(cls, cardnumber):
        return cls.query.filter_by(cardnumber=cardnumber).first()

    @classmethod
    def get_by_id(cls, payment_detail_id):
        return cls.query.filter_by(payment_detail_id=payment_detail_id).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
