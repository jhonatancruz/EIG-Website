from flask import Flask, render_template


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/products')
def products():
    return render_template('products.html')

if __name__ == "__main__":
    app.run(debug=True)
