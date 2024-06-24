from flask import Flask  #name이름을 통한 flask객체 생성 
 
app = Flask(__name__)

@app.route("/")          #라우팅을 위한 뷰 함수 등록 
def hello():
  return "hello world"

@app.route("/name")
def name():
	return "<h1>My name is Oh hye-jin</h1>"

@app.route("/age")
def age():
 return "<h1>I'm 27 year's old</h1>"

if __name__ == "__main__":  #터미널에서 직접 실행시키면 실행파일이 main으로 바뀐다 
	app.run(host="0.0.0.0",port="12345", debug=True) #실행을 위한 명령문으로 보면 된다 
