```python
import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monetization.db'
db = SQLAlchemy(app)

class Monetization(db.Model):
    __tablename__ = 'monetization'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    subscription_plan = Column(String)
    in_app_purchases = Column(Float)
    premium_features = Column(String)
    paid_content = Column(String)
    exclusive_memberships = Column(String)
    fan_based_support = Column(String)

db.create_all()

@app.route('/monetization', methods=['POST'])
def create():
    monetization_data = json.loads(request.data)
    new_monetization = Monetization(user_id=monetization_data['user_id'], subscription_plan=monetization_data['subscription_plan'], in_app_purchases=monetization_data['in_app_purchases'], premium_features=monetization_data['premium_features'], paid_content=monetization_data['paid_content'], exclusive_memberships=monetization_data['exclusive_memberships'], fan_based_support=monetization_data['fan_based_support'])
    db.session.add(new_monetization)
    db.session.commit()
    return {'id': new_monetization.id}, 200

@app.route('/monetization/<user_id>', methods=['GET'])
def get_monetization(user_id):
    monetization_data = Monetization.query.get(user_id)
    return {'subscription_plan': monetization_data.subscription_plan, 'in_app_purchases': monetization_data.in_app_purchases, 'premium_features': monetization_data.premium_features, 'paid_content': monetization_data.paid_content, 'exclusive_memberships': monetization_data.exclusive_memberships, 'fan_based_support': monetization_data.fan_based_support}

@app.route('/monetization/<user_id>', methods=['PUT'])
def update_monetization(user_id):
    monetization_data = Monetization.query.get(user_id)
    update_data = json.loads(request.data)
    monetization_data.subscription_plan = update_data['subscription_plan']
    monetization_data.in_app_purchases = update_data['in_app_purchases']
    monetization_data.premium_features = update_data['premium_features']
    monetization_data.paid_content = update_data['paid_content']
    monetization_data.exclusive_memberships = update_data['exclusive_memberships']
    monetization_data.fan_based_support = update_data['fan_based_support']
    db.session.commit()
    return {'message': 'Monetization data updated successfully.'}

@app.route('/monetization/<user_id>', methods=['DELETE'])
def delete_monetization(user_id):
    monetization_data = Monetization.query.get(user_id)
    db.session.delete(monetization_data)
    db.session.commit()
    return {'message': 'Monetization data deleted successfully.'}

if __name__ == '__main__':
    app.run(debug=True)
```