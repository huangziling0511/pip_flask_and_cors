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
app=pfac.app() #app约等于flask.Flask(__name__)
#app的参数：app(cors=False)，cors参数的意思是是否使用flask_cors.CORS
@app.route("/")
def home():
    return 'hello from pip_flask_and_cors'
if __name__ == '__main__':
    pfac.run(app) #等于app.run加打开页面
'''
run的参数：run(host=host,port=port,debug=debug,load_dotenv=load_dotenv,
                use_reloader=use_reloader, use_debugger=use_debugger, use_evalex=use_evalex, threaded=threaded,
                processes=processes, passthrough_errors=passthrough_errors, ssl_context=ssl_context,
                extra_files=extra_files,eloader_interval=eloader_interval,reloader_type=reloader_type
```
