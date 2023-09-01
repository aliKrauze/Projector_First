from sqlalchemy.orm import sessionmaker
from create_engine import engine
from datetime import datetime
from db_airbnb import User, Room, Reservation, Review, Payment

Session = sessionmaker(bind=engine)
session = Session()

user_data = [
    {'user_name': 'guest1', 'email': 'guest1@google.com', 'user_type': 'guest'},
    {'user_name': 'guest2', 'email': 'guest2@google.com', 'user_type': 'guest'},
    {'user_name': 'host1', 'email': 'host1@google.com', 'user_type': 'host'},
]

for data in user_data:
    user = User(**data)
    session.add(user)

room_data = [
    {'user_id': 1, 'room_count': 2, 'bed_count': 2, 'price': 100,
     'has_ac': True, 'has_refrigerator': False, 'has_parking': True},
    {'user_id': 2, 'room_count': 1, 'bed_count': 1, 'price': 60,
     'has_ac': True, 'has_refrigerator': True, 'has_parking': False},
    {'user_id': 3, 'room_count': 1, 'bed_count': 2, 'price': 50,
     'has_ac': False, 'has_refrigerator': True, 'has_parking': True},
]

for data in room_data:
    room = Room(**data)
    session.add(room)

reservation_data = [
    {'user_id': 1, 'room_id': 1, 'checkin_date': datetime(2023, 2, 1),
     'checkout_date': datetime(2023, 2, 5)},
    {'user_id': 2, 'room_id': 2, 'checkin_date': datetime(2023, 4, 2),
     'checkout_date': datetime(2023, 4, 10)},
    {'user_id': 1, 'room_id': 1, 'checkin_date': datetime(2023, 5, 3),
     'checkout_date': datetime(2023, 5, 12)},
]

for data in reservation_data:
    reservation = Reservation(**data)
    session.add(reservation)

review_data = [
    {'reservation_id': 1, 'user_id': 2, 'rating': 4.8,
     'comment': 'Very nice, clean and cozy place'},
    {'reservation_id': 2, 'user_id': 1, 'rating': 5.0,
     'comment': 'Excelent place for the perfect vacation'},
    {'reservation_id': 3, 'user_id': 2, 'rating': 3.8,
     'comment': 'Not bad, but the noise outside all over the night was so irritating'},
]

for data in review_data:
    review = Review(**data)
    session.add(review)

payment_data = [
    {'reservation_id': 1, 'guest_id': 2,
     'payment_amount': 100.00, 'payment_date': datetime(2023, 2, 12)},
    {'reservation_id': 2, 'guest_id': 1,
     'payment_amount': 80.00, 'payment_date': datetime(2023, 3, 3)},
    {'reservation_id': 3, 'guest_id': 3,
     'payment_amount': 75.00, 'payment_date': datetime(2023, 5, 4)},
]

for data in payment_data:
    payment = Payment(**data)
    session.add(payment)

session.commit()
session.close()
