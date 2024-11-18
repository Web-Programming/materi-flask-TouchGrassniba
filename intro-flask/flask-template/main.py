from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        print(f"Name: {name}, Email: {email}, Message: {message}")
        
        # You could add form validation or save to a database here

        return redirect(url_for('contact'))  # Redirect back to the contact page after form submission

    title = "Contact Page"
    return render_template('contact.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)
