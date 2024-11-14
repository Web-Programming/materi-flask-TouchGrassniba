from Flask import Flask, 
app=Flask(__name__)

@app.route('/contact',method={'GET','POST'})
def contact():
    if request



if __name__ =='__main__':
    app.run(debug=True)   