from models import UserModel, db, ContractModel


class ContractRepository:
    @staticmethod
    def get_contract_by_id(contract_id, with_user=False):

        if with_user:
            resp = ContractModel.query.select_from(ContractModel).join(
                UserModel).where(ContractModel.id == contract_id).first()
            return resp
        else:
            return ContractModel.query.get(contract_id)

    @staticmethod
    def get_contract_by_user_id(user_id, limit=10, offset=0):
        return ContractModel.query.filter_by(user_id=user_id).limit(limit).offset(offset).all()

    @staticmethod
    def get_contract_by(prop_name, prop_value):
        return ContractModel.query.filter_by(**{prop_name: prop_value}).first()

    @staticmethod
    def add(contract_model):
        db.session.add(contract_model)
        db.session.commit()

    @staticmethod
    def delete(contract_model):
        db.session.delete(contract_model)
        db.session.commit()
