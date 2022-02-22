import csv
from flask import Flask,jsonify,request
all_movies=[]
with open ('articles.csv') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]
liked_articles=[]
not_liked_articles=[]
app=Flask(__name__)
@app.route('/get-article')
def get_article():
    return jsonify({
        'data':all_articles[0],
        'message':'success'
    })
@app.route('/liked-article',methods=['POST'])
def liked_article():
    article=all_movies[0]
    all_articles=all_articles[1:]
    liked_articles.append(article)
    return jsonify({
      'message':'success'
    }),201
@app.route('/unliked-article',methods=['POST'])
def unliked_article():
    article=all_articles[0]
    all_articles=all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
      'message':'success'
    }),201

if __name__=='__main__':
    app.run()
 
