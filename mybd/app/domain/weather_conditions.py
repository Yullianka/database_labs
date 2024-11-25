from __future__ import annotations
from typing import Dict, Any
from app import db
from sqlalchemy import event, select


class WeatherCondition(db.Model):
    __tablename__ = 'weather_conditions'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    wind_speed = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    solar_station_id = db.Column(db.Integer, db.ForeignKey('solar_station.id'), nullable=False)

    def __repr__(self) -> str:
        return f"WeatherCondition(id={self.id}, location='{self.location}', " \
               f"temperature={self.temperature}, humidity={self.humidity}, " \
               f"wind_speed={self.wind_speed}, date={self.date})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'location': self.location,
            'temperature': self.temperature,
            'humidity': self.humidity,
            'wind_speed': self.wind_speed,
            'date': self.date,
            'solar_station_id': self.solar_station_id 
            
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> WeatherCondition:
        return WeatherCondition(
            location=dto_dict.get('location'),
            temperature=dto_dict.get('temperature'),
            humidity=dto_dict.get('humidity'),
            wind_speed=dto_dict.get('wind_speed'),
            date=dto_dict.get('date'),
            solar_station_id=dto_dict.get('solar_station_id')
        )
    


@event.listens_for(WeatherCondition, "before_insert")
def check_solar_station(mapper, connection, target):
    solar_station_table = db.Table('solar_station', db.metadata, autoload_with=db.engine)
    
   
    solar_station_exists = connection.execute(
        select(solar_station_table.c.id).where(solar_station_table.c.id == target.solar_station_id)
    ).first()

    if not solar_station_exists:
        raise ValueError(f"Solar station with id {target.solar_station_id} does not exist.")

