from flask import Flask, request, render_template


import pickle



file1 = open('bodyfatmodel.pkl', 'rb')
rf = pickle.load(file1)
file1.close()


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        my_dict = request.form

        density = float(my_dict['density'])
        abdomen = float(my_dict['abdomen'])
        chest = float(my_dict['chest'])
        weight = float(my_dict['weight'])
        hip = float(my_dict['hip'])
        
        # get the measurements in the form of an array
        #pass that array to make the prediction and taking 
        # the first number and rounding to 2 places
        input_features = [[density, abdomen, chest, weight, hip]]
        prediction = rf.predict(input_features)[0].round(2)

        # <p class="big-font">Hello World !!</p>', unsafe_allow_html=True
        #were getting the result as a string 
        string = 'Percentage of Body Fat Estimated is : ' + str(prediction)+'%'

        return render_template('show.html', string=string)

    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
