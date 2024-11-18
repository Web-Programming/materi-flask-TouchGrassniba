from flask import Flask,jsonify,request
import os
import time

UPLOAD_FOLDER='static/uploads'

app=Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
@app.route('/')
def home():
    return 'File Upload Demo'


@app.route('/uploadfile',methods=['GET','POST'])
def uploadfile():
    if request.method =='POST':
        foto = request.files['foto']
        if foto:
            
            timestamp=str(int(time.time()))
            ext = foto.file.split('.')[-1]

            unique_filename = f"{timestamp}.{ext}"
            foto_path = os.path.join(app.config['UPLOAD_FOLDER'],unique_filename)
            foto.save(foto_path)
            foto_path=f'uploads/{unique_filename}'
            data={
                "status":"success",
                "message":"file uploaded",
            }

            return jsonify(data)
        
        else:
            foto_path=None
            data = {
                "status" :"failed",
                "message":"File Upload Failed",
            }
            return jsonify(data)
    data = {
    "status":"success",
    "message":"Pick A foto to upload"
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)


