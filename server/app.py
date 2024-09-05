from flask import request, session, jsonify, make_response
from flask_restful import Resource, Api
from config import app, db, api
from models import User, Monster, Buy, Media, SMed, SMed, SBu

# @app.before_request
# def check_if_logged_in():
#     print(request.endpoint)
#     if  session.get('user_id') or request.endpoint in ('login','register','session'):
#         pass
#     else:
#         return make_response({'error':'Please log in first'}, 403)

# @app.route('/login', methods = ["POST"])
# def login():
#     data = request.get_json()
#     user = User.query.filter(User.username == data["username"]).first()
#     if user:
#         session["user_id"] = user.id
#         return user.to_dict()
#     else:
#         return {"error":"Cannot login in"},400

# @app.route('/check_sessions')
# def check_sessions():
#     if session.get("user_id"):
#         user = User.query.filter(User.id == session.get("user_id")).first()
#         return user.to_dict()
#     else:
#         return {"error": "no user logged in"},401
    
# @app.route('/logout', methods=["DELETE"])
# def logout():
#     session.pop('user_id')
#     return {}, 204

class LogOUT(Resource):
    def delete(self):
        session.clear()
        return {}
api.add_resource(LogOUT,'/logout')
class SaveSe(Resource):
    def get(self):
        print(session)
        return {}
    def post(self):
        print(session)
        data = request.get_json()
        session['data'] = data['data']
        print(data)
        return {}
api.add_resource(SaveSe,'/session')
class CheckSe(Resource):
    def get(self):
        print(session)
        if session.get('stay_logged_in') == True:
            user = User.query.filter(User.id == session.get('user_id')).first()
            return user.to_dict()
        else:
            return {}, 404
api.add_resource(CheckSe,'/checksession')
class LoginIN(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter(User.username == data['username']).first()
        if user and user.authenticate(data['password']):
            session['stay_logged_in'] = data.get('stayLoggIn', False)
            session['user_id'] = user.id
            print(session)
            return user.to_dict(), 200
        return make_response({'error':'Invalid username or password'}, 401)
api.add_resource(LoginIN, '/login')
class All_User(Resource):
    def get(self):
        au = User.query.all()
        return [us.to_dict(rules=('-sbus', '-smeds','-smons')) for us in au],200
    def post(self):
        try:
            data = request.get_json()
            new_user = User(
                username = data['username'],
                password_hash = data['password'],
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
        return [us.to_dict(rules=('-smons',)) for us in au],200
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
            return new_monster.to_dict(rules=('-smons',)),200
        except Exception as e:
            return make_response({'errors': str(e)},404)
            
class One_Monster(Resource):
    def get(self, id):
        act = Monster.query.filter(Monster.id == id).first()
        if act:
            return act.to_dict(rules=('-smons',)),200
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
                return one.to_dict(rules=('-smons',)),202
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


class All_Media(Resource):
    def get(self):
        au = Media.query.all()
        return [us.to_dict(rules=('-smeds',)) for us in au],200
    def post(self):
        try:
            data = request.get_json()
            new_media = media(
                movies = data['movies'], 
                episodes = data['episodes']
            )
            db.session.add(new_media)
            db.session.commit()
            return new_media.to_dict(rules=('-smeds',)),200
        except Exception as e:
            return make_response({'errors': str(e)},404)
class One_Media(Resource):
    def get(self, id):
        act = Media.query.filter(Media.id == id).first()
        if act:
            return act.to_dict(rules=('-smeds',)),200
        else:
            return make_response({'error':'This media does not exist'},400)
    def patch(self, id):
        one = Media.query.filter(Media.id == id).first()
        if one:
            try:
                data = request.get_json()
                for key in data:
                    setattr(one,key,data[key])
                db.session.add(one)
                db.session.commit()
                return one.to_dict(rules=('-smeds',)),202
            except Exception as e:
                return make_response({"error": str(e)},404) 
        else:
            return make_response('This media does not exist',404)
    def delete(self, id):
        one = Media.query.filter(Media.id == id).first()
        if one:
            db.session.delete(one)
            db.session.commit()
            return {}, 204
        else:
            return make_response({
                'error': 'Could not find media'
            },404)
api.add_resource(All_Media,'/media')
api.add_resource(One_Media,'/media/<int:id>')


class All_Buy(Resource):
    def get(self):
        au = Buy.query.all()
        return [us.to_dict(rules=('-sbus', )) for us in au],200
    def post(self):
        try:
            data = request.get_json()
            new_buy = buy(
                cheapest = data['cheapest'], 
                most = data['most'],
                reliable = data['reliable']
            )
            db.session.add(new_buy)
            db.session.commit()
            return new_buy.to_dict(rules=('-sbus', )),200
        except Exception as e:
            return make_response({'errors': str(e)},404)
class One_Buy(Resource):
    def get(self, id):
        act = Buy.query.filter(Buy.id == id).first()
        if act:
            return act.to_dict(rules=('-sbus', )),200
        else:
            return make_response({'error':'This buy does not exist'},400)
    def patch(self, id):
        one = Buy.query.filter(Buy.id == id).first()
        if one:
            try:
                data = request.get_json()
                for key in data:
                    setattr(one,key,data[key])
                db.session.add(one)
                db.session.commit()
                return one.to_dict(rules=('-sbus', )),202
            except Exception as e:
                return make_response({"error": str(e)},404) 
        else:
            return make_response('This buy does not exist',404)
    def delete(self, id):
        one = Buy.query.filter(Buy.id == id).first()
        if one:
            db.session.delete(one)
            db.session.commit()
            return {}, 204
        else:
            return make_response({
                'error': 'Could not find buy'
            },404)
api.add_resource(All_Buy,'/buy')
api.add_resource(One_Buy,'/buy/<int:id>')
class S_Mon(Resource):
    def get(sefl,id):
        smon = SMon.query.filter(SMon.id ==id).first()
        if smon:
            return smon.to_dict()
        else:
            return {"error, not a valid id"}
    def post(self,id):
        try:
            data = request.get_json()
            monster.id = data.get('monster_id')
            user.id = data.get('user_id')
            user = User.query.get(id)
            monster = Monster.query.get(id)
            monster = Monster.query.get(monster_id)
            user = User.query.get(user_id)
            if monster and user:
                if monster and monster not in SMon.save:
                    print(monster)
                    print(user)
                    Smon.save = monster + user
                    SMon.save.append(monster)
                    SMon.save.append(user)
                    db.session.commit()
                    return {"Monster has been saved!"},201
                else:
                    return {"Monster alread saved"},400
            else:
                return {"Error, this monster doesn't exist"}
api.add_resource(S_Mon,'/s_mon')

if __name__ == '__main__':
    app.run(port=5555, debug=True)