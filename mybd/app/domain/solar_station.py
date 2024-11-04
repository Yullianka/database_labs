from __future__ import annotations
from typing import Dict, Any
from sqlalchemy.orm import relationship
from app import db


class SolarStation(db.Model):
    __tablename__ = 'solar_station'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    household = db.Column(db.Integer)
    billing_account_id = db.Column(db.Integer, db.ForeignKey('billing_account.id'), nullable=False)
    
    panels = db.relationship('Panel', backref='solar_station')
    batteries = db.relationship('Battery', backref='solar_station')
    households = db.relationship('Household', backref='solar_station')
    energy_sales = db.relationship('EnergySale', backref='solar_station')

    def __repr__(self) -> str:
        return f"SolarStation({self.id}, name='{self.name}', household='{self.household}')"

    def put_into_dto(self) -> Dict[str, Any]:
        panels = [panels.put_into_dto() for panels in self.panels]
        batteries = [batteries.put_into_dto() for batteries in self.batteries]
        households = [households.put_into_dto() for households in self.households]
        energy_sales = [energy_sales.put_into_dto() for energy_sales in self.energy_sales]
        return {
            'id': self.id,
            'name': self.name,
            'household': self.household,
            'billing_account_id': self.billing_account_id,
            'panels': panels if panels else None,
            'batteries': batteries if batteries else None,
            'households': households if households else None,
            'energy_sales': energy_sales if energy_sales else None,
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> SolarStation:
        return SolarStation(
            name=dto_dict.get('name'),
            household=dto_dict.get('household'),
            billing_account_id=dto_dict.get('billing_account_id'),
        )