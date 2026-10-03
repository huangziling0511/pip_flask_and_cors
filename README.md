**pip_flask_and_cors**
---
这个库可以帮你下载flask和flask_cors

---
要求：  
如果你用的是Mac或Linux，你需要有pip3。  
如果你用的是windows，你需要有pip。

---
使用：
```python
import pip_flask_and_cors as pfac
app=pfac.app() #app()约等于flask.Flask(__name__)
#app()的参数：app(cors=False)，cors参数的意思是是否使用flask_cors.CORS
@app.route("/")
def home():
    return 'hello from pip_flask_and_cors'
if __name__ == '__main__':
    pfac.run(app) #等于app.run加打开页面
'''
run()的参数：(run_app,host='127.0.0.1', port=5000, debug=False, load_dotenv=True,
          use_reloader=None, use_debugger=None, use_evalex=True, threaded=False,
          processes=1, passthrough_errors=False, ssl_context=None, extra_files=None,
          reloader_interval=1,reloader_type='auto')
'''
```
