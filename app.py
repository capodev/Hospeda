from flask import Flask, render_template

app = Flask(__name__)
@app.route('/about')
def about():
    return render_template('about/about.html')

@app.route('/services')
def services():
    return render_template('services/services.html')
@app.route('/gallery')
def gallery():
    return render_template('gallery/gallery.html')  
@app.route('/contacto')
def contacto():
    return render_template('contacto/contacto.html')
    
@app.route('/faqs')
def faqs():
    return render_template('faqs/faqs.html')    
@app.route('/<usuario>')
def saludo(usuario):
    return render_template('saludo.html', usuario=usuario)
@app.route('/')
def home():
    return render_template('home/hero-home.html')

if __name__ == '__main__':
    app.run(debug=True)