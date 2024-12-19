from flask import Flask, render_template, request   

app = Flask(__name__) 
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1

@app.route('/')
def home():
    return render_template('index.html')




@app.route('/data' , methods = ['POST','GET'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        phone = int(request.form['phone'])
        email = request.form['email']
        subject =request.form['subject']
        message =request.form['message']

        print("Name Of User:",name)
        print("Phone no:",phone)
        print("Email:",email)
        print("subject:",subject)
        print("message:",message)

        return render_template('index.html')
    
    else :
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)