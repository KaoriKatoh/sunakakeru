from flask import Flask,render_template,request,redirect,session

app = Flask (__name__)


#-----シークレットキーのセット/" "この中は通常　乱数が入る"
app.secret_key="SUNABACO"




#------template作成   
@app.route('/')
def template():
    return render_template('base.html')

    













#-------404エラーだぴょん
@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 404




#-------最後のきめ文句　ここから後は書いても無駄
if __name__=="__main__":
    app.run(debug=True)