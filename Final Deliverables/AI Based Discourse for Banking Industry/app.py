from flask import Flask,render_template
app=Flask(__name__,template_folder='template')
@app.route('/')
def Chatbot():
    return render_template('Chatbot.html')
if __name__ =='__main__':
    app.run(debug=True)
