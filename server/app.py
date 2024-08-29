from flask import request, session, jsonify, make_response
from flask_restful import Resource, Api
from config import app, db, api
from models import User, Monster, Buy, Media

# @app.before_request
# def check_if_logged_in():
#     print(request.endpoint)
#     if  session.get('user_id') or request.endpoint in ('login','register','session'):
#         pass
#     else:
#         return make_response({'error':'Please log in first'}, 403)


#HAD POST WORKING, BUT NOW BROKEN
class All_User(Resource):
    def get(self):
        au = User.query.all()
        return [us.to_dict(rules=('-sbus', '-smeds','-smons')) for us in au],200
    def post(self):
        try:
            data = request.get_json()
            new_user = User(
                username = data['username'],
                password = data['password'],
                fav_mon = data['fav_mon'], 
                fav_mov = data['fav_mov']
            )
            db.session.add(new_user)
            db.session.commit()
            return new_user.to_dict(rules=('-sbus', '-smeds','-smons')),200
        except Exception as e:
            return make_response({'errors': str(e)},404)
class One_User(Resource):
    def get(self, id):
        act = User.query.filter(User.id == id).first()
        if act:
            return act.to_dict(rules=('-sbus', '-smeds','-smons')),200
        else:
            return make_response({'error':'This user does not exist'},400)
    def patch(self, id):
        one = User.query.filter(User.id == id).first()
        if one:
            try:
                data = request.get_json()
                for key in data:
                    setattr(one,key,data[key])
                db.session.add(one)
                db.session.commit()
                return one.to_dict(rules=('-sbus', '-smeds','-smons')),202
            except Exception as e:
                return make_response({"error": str(e)},404) 
        else:
            return make_response('This user does not exist',404)
    def delete(self, id):
        one = User.query.filter(User.id == id).first()
        if one:
            db.session.delete(one)
            db.session.commit()
            return {}, 204
        else:
            return make_response({
                'error': 'Could not find user'
            },404)
api.add_resource(All_User,'/user' 
# endpoint='register'
)
api.add_resource(One_User,'/user/<int:id>')

class All_Monster(Resource):
    def get(self):
        au = Monster.query.all()
        return [us.to_dict(rules=()) for us in au],200
    def post(self):
        try:
            data = request.get_json()
            new_monster = Monster(
                name = data['name'], 
                age = data['age'], 
                parents = data['parents'], 
                siblings = data['siblings'],
                movies = data['movies'], 
                episodes = data['episodes']
            )
            db.session.add(new_monster)
            db.session.commit()
            return new_monster.to_dict(rules=()),200
        except Exception as e:
            return make_response({'errors': str(e)},404)
class One_Monster(Resource):
    def get(self, id):
        act = Monster.query.filter(Monster.id == id).first()
        if act:
            return act.to_dict(rules=()),200
        else:
            return make_response({'error':'This monster does not exist'},400)
    def patch(self, id):
        one = Monster.query.filter(Monster.id == id).first()
        if one:
            try:
                data = request.get_json()
                for key in data:
                    setattr(one,key,data[key])
                db.session.add(one)
                db.session.commit()
                return one.to_dict(rules=()),202
            except Exception as e:
                return make_response({"error": str(e)},404) 
        else:
            return make_response('This monster does not exist',404)
    def delete(self, id):
        one = Monster.query.filter(Monster.id == id).first()
        if one:
            db.session.delete(one)
            db.session.commit()
            return {}, 204
        else:
            return make_response({
                'error': 'Could not find monster'
            },404)
api.add_resource(All_Monster,'/monster')
api.add_resource(One_Monster,'/monster/<int:id>')









if __name__ == '__main__':
    app.run(port=5555, debug=True)

