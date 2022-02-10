

from configuration import app, db




# @app.before_first_request
# def creat_all():
#     db.create_all()

@app.route('/')
def first():
    return 'hello'




if __name__=="__main__":
    app.run(debug=True)