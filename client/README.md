
class S_Mon(Resource):
    def get(self,id):
        smon = SMon.query.filter(SMon.id ==id).first()
        if smon:
            return smon.to_dict()
        else:
            return {'error': 'not a valid id'}
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
                    db.session.add(monster)
                    db.session.add(user)
                    db.session.commit()
                    return {"Monster has been saved!"},201
                else:
                    return {"Monster alread saved"},400
            else:
                return {"Error, this monster doesn't exist"}
api.add_resource(S_Mon, "/s_mon")