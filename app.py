from flask import Flask, render_template, request,jsonify
from werkzeug import secure_filename
import datetime
import nltk
import cv2 
import numpy as np
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize 
from nltk.tokenize import WordPunctTokenizer 
app = Flask(__name__)


def bgr_img(filename_type,filename,typo):
    image = cv2.imread(filename_type) 
    r=image.shape[0]
    c=image.shape[1]
    B=np.zeros((r,c,3),dtype=int)
    G=np.zeros((r,c,3),dtype=int)
    R=np.zeros((r,c,3),dtype=int)
    B[:,:,0]=image[:,:,0]
    G[:,:,1]=image[:,:,1]
    R[:,:,2]=image[:,:,2]

    # cv2_imshow(B)
    # cv2.waitKey(0)

    # cv2_imshow(G)
    # cv2.waitKey(0)

    # cv2_imshow(R)
    # cv2.waitKey(0)
    cv2.imwrite('./templates/'+filename+'_b.'+typo,B)
    cv2.imwrite('./templates/'+filename+'_g.'+typo,G)
    cv2.imwrite('./templates/'+filename+'_r.'+typo,R)
    cv2.destroyAllWindows()

def textfunc():
    pass

@app.route('/result',methods=['POST','GET'])
def display():
    fl=request.files['file_type']
    filetype=fl.filename.split('.')[-1]
    filtypes=['txt','csv','xlsv','gif','png','jpg','mp4']
    if filetype in filtypes:
        fl.save(fl.filename)
    if filetype=='txt':
        with open(fl.filename, 'r') as content_file:
            content = content_file.read()
        
        tokenizer=WordPunctTokenizer()
        return str(tokenizer.tokenize(content))

    elif filetype=='png':
        onlyfn=str(fl.filename[0:len(fl.filename)-4])
        bgr_img(fl.filename,onlyfn,'png')
        return render_template('image.html',filename_b=onlyfn +'_b.png',filename_g=onlyfn+'_g.png',filename_r=onlyfn+'_r.png')
    elif filetype=='jpg':
        onlyfn=fl.filename[0:len(fl.filename)-4]
        bgr_img(fl.filename,onlyfn,'jpg')
        return render_template('image.html',filename_b=onlyfn+'_b.jpg',filename_g=onlyfn+'_g.jpg',filename_r=onlyfn+'_r.jpg')
    return filetype
    


@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)