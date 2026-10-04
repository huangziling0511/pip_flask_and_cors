import os,sys,webbrowser as web
def use_pip3():
    if (os.path.abspath(sys.argv[0]))[0] != '/':
        return False
    else:
        return True
try:
    import flask
except:
    if use_pip3():
        os.system("pip3 install flask")
try:
    import flask_cors
except:
    if use_pip3():
        os.system("pip3 install flask-cors")
import flask_cors, flask
def app(cors=False):
    if cors:
        a=flask.Flask(__name__)
        flask_cors.CORS(a)
    else:
        a=flask.Flask(__name__)
    return a
def run(run_app,host='127.0.0.1', port=5000, debug=False, load_dotenv=True,
        use_reloader=None, use_debugger=None, use_evalex=True, threaded=False,
        processes=1, passthrough_errors=False, ssl_context=None, extra_files=None,
        reloader_interval=1,reloader_type='auto'):
    web.open(f"http://{host}:{port}")
    run_app.run(host=host,port=port,debug=debug,load_dotenv=load_dotenv,
                use_reloader=use_reloader, use_debugger=use_debugger, use_evalex=use_evalex, threaded=threaded,
                processes=processes, passthrough_errors=passthrough_errors, ssl_context=ssl_context,
                extra_files=extra_files,reloader_interval=eloader_interval,reloader_type=reloader_type)
