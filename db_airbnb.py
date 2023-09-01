from sqlalchemy import Column, DECIMAL, Integer, String, Boolean, Text, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from engine_airbnb import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    email = Column(String(80), nullable=False)
    user_type = Column(String(50), nullable=False)
    rooms = relationship('Room', back_populates='host')
    reservations = relationship('Reservation', back_populates='guest')
    reviews_written = relationship('Review', back_populates='guest', foreign_keys='Review.user_id')
    reviews_received = relationship('Review', back_populates='host', foreign_keys='Review.user_id')
    payments = relationship('Payment', back_populates='guest')


class Room(Base):
    __tablename__ = 'rooms'

    room_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    room_count = Column(Integer, nullable=False)
    bed_count = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    has_ac = Column(Boolean, nullable=False)
    has_refrigerator = Column(Boolean, nullable=False)
    has_parking = Column(Boolean, nullable=False)

    host = relationship('User', back_populates='rooms')
    reservations = relationship('Reservation', back_populates='room')


class Reservation(Base):
    __tablename__ = 'reservations'

    reservation_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.room_id'), nullable=False)
    checkin_date = Column(Date, nullable=False)
    checkout_date = Column(Date, nullable=False)

    guest = relationship('User', back_populates='reservations')
    room = relationship('Room', back_populates='reservations')
    reviews = relationship('Review', back_populates='reservation')
    payment = relationship('Payment', back_populates='reservation')


class Review(Base):
    __tablename__ = 'reviews'
    review_id = Column(Integer, primary_key=True)
    reservation_id = Column(Integer, ForeignKey('reservations.reservation_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    rating = Column(DECIMAL(3, 2), nullable=False)
    comment = Column(Text)
    guest = relationship('User', back_populates='reviews_written', foreign_keys=[user_id])
    host = relationship('User', back_populates='reviews_received', foreign_keys=[user_id])
    reservation = relationship('Reservation', back_populates='reviews')


class Payment(Base):
    __tablename__ = 'payments'

    payment_id = Column(Integer, primary_key=True)
    reservation_id = Column(Integer, ForeignKey('reservations.reservation_id'), nullable=False)
    guest_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    payment_amount = Column(DECIMAL, nullable=False)
    payment_date = Column(Date, nullable=False)

    guest = relationship('User', back_populates='payments')
    reservation = relationship('Reservation', back_populates='payment')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
