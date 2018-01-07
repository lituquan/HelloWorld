from flask import Flask

app=Flask.app()

@app.route("/")
def helloWorld():
  return "Hello,world"

if __name__=="__main__":
  app.run()  
