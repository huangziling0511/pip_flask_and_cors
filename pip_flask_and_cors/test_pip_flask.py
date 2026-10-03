import pip_flask_and_cors as pfac
app=pfac.app()
@app.route("/")
def home():
    return 'hello from pip_flask_and_cors'
if __name__ == '__main__':
    pfac.run(app)
