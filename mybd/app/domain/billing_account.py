from __future__ import annotations
from typing import Dict, Any
from app import db


class BillingAccount(db.Model):
    __tablename__ = 'billing_account'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    balance = db.Column(db.String(45), nullable=False) 
    account_number = db.Column(db.String(45), unique=True, nullable=False)
    
    def __repr__(self) -> str:
        return f"BillingAccount(id='{self.id}', balance='{self.balance}', account_number='{self.account_number}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'balance': self.balance,
            'account_number': self.account_number,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> BillingAccount:
        return BillingAccount(
            balance=dto_dict.get('balance'),
            account_number=dto_dict.get('account_number')
        )
