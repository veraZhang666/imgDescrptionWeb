from flask import Flask,url_for,render_template,request,jsonify
import base64
import json
import sys,os
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)


app = Flask(__name__)


app.debug=False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploadpic/',methods=['GET','POST'])
def uploadpic():
    if request.method=='POST' and request.is_xhr:
        img_str = request.form.get('pic')
        print(img_str)
        inx = img_str.find(',')
        newstring = img_str[inx + 1:]
        imgdata = base64.b64decode(newstring)
        f = open("pic.jpg", "wb")
        f.write(imgdata)
        f.close()

    return ' success '
@app.route('/returnpic/')
def return_res():
    # image to base64
    str_img_base64 =''
    des = 'Dog with wood stick in his mouth'

    with open("./BoundingBox/DogBox.png", "rb") as f:  # 转为二进制格式
        base64_data_byte = base64.b64encode(f.read())  # 使用base64进行加密
        str_img_base64 = str(base64_data_byte, 'utf-8')

    li = [{'pic_bs64': str_img_base64,
            'description': des
            }]

    return jsonify(li)

if __name__=='__main__':
	print("test ok")
	app.run()


