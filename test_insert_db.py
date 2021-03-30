from app import *
from models.payment_details import PaymentDetails

app = create_app()
with app.app_context():
    payment1 = PaymentDetails(card_owner_name='Luis Cevallos', cardnumber='555999', expiration_date='05-21',
                                security_code='789')

    db.session.add(payment1)
    db.session.commit()
