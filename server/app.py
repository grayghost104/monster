from flask import request, session
from flask_restful import Resource, Api
from config import app, db, api
from moodels import User, Monster, Buy, Media, Story, Saved

@app.before_request
def check_if_logged_in():
    print(request.endpoint)
    if  session.get('user_id') or request.endpoint in ('login','register','session'):
        pass
    else:
        return make_response({'error':'Please log in first'}, 403)

class All_User(Resource):
    def get(self):
        au = User.query.all()
        return [us.to_dict(rules=()) for us in au],200
    def post(self):
        try:
            data = request.get_json()
            new_user = User(
                username = data['username'], 
                fav_mon = data['fav_mon'], 
                fav_mov = data['fav_mov']
            )
            db.session.add(new_user)
            db.session.commit()
            return new_user.to_dict(rules=()),200
        except Exception as e:
            return make_response({'errors': str(e)},404)
class One_User(Resource):
    def get(self, id):
        act = User.query.filter(User.id == id).first()
        if act:
            return act.to_dict(rules=()),200
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
                return one.to_dict(rules=()),202
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
api.add_resource(All_User,'/users', endpoint='register')
api.add_resource(One_User,'/users/<int:id>')

class All_Saved(Resource):
    def get(self):
        au = Saved.query.all()
        return [us.to_dict(rules=()) for us in au],200
    def post(self):
        try:
            data = request.get_json()
            new_saved = saved(
                buying = data['buying'], 
                watching = data['watching'], 
                mon = data['mon'], 
                story = data['story']
            )
            db.session.add(new_saved)
            db.session.commit()
            return new_saved.to_dict(rules=()),200
        except Exception as e:
            return make_response({'errors': str(e)},404)
class One_saved(Resource):
    def get(self, id):
        act = Saved.query.filter(Saved.id == id).first()
        if act:
            return act.to_dict(rules=()),200
        else:
            return make_response({'error':'This saved does not exist'},400)
    def patch(self, id):
        one = Saved.query.filter(saved.id == id).first()
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
            return make_response('This saved does not exist',404)
    def delete(self, id):
        one = Saved.query.filter(Saved.id == id).first()
        if one:
            db.session.delete(one)
            db.session.commit()
            return {}, 204
        else:
            return make_response({
                'error': 'Could not find saved'
            },404)
api.add_resource(All_saved,'/saveds', endpoint='register')
api.add_resource(One_saved,'/saveds/<int:id>')


























if __name__ == '__main__':
    app.run(port=5555, debug=True)

