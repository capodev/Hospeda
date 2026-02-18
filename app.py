from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

# Datos simulados (mock data) para pasar a las plantillas
HOTELS = [
    {
        "id": 1,
        "name": "Royal Palm Galapagos",
        "location": "Santa Cruz, Galápagos",
        "rating": 4.9,
        "price": 350,
        "type": "Hotel",
        "image": "https://images.unsplash.com/photo-1729719022559-34978ede47d1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxsdXh1cnklMjByZXNvcnQlMjBzd2ltbWluZyUyMHBvb2x8ZW58MXx8fHwxNzcxMzc2NDQwfDA&ixlib=rb-4.1.0&q=80&w=1080",
        "badge": "Lujo"
    },
    {
        "id": 2,
        "name": "Mashpi Lodge",
        "location": "Pichincha, Ecuador",
        "rating": 5.0,
        "price": 450,
        "type": "Lodge",
        "image": "https://images.unsplash.com/photo-1715529023436-ad8c4a4f202e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxnbGFtcGluZyUyMHRlbnQlMjBmb3Jlc3QlMjBuYXR1cmV8ZW58MXx8fHwxNzcxMzc2NDQxfDA&ixlib=rb-4.1.0&q=80&w=1080",
        "badge": "Ecológico"
    },
    {
        "id": 3,
        "name": "Swissôtel Quito",
        "location": "Quito, Ecuador",
        "rating": 4.8,
        "price": 180,
        "type": "Hotel",
        "image": "https://images.unsplash.com/photo-1572177215152-32f247303126?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxtb2Rlcm4lMjBob3RlbCUyMGJlZHJvb20lMjBpbnRlcmlvcnxlbnwxfHx8fDE3NzEzMTE0NzJ8MA&ixlib=rb-4.1.0&q=80&w=1080",
        "badge": "Urbano"
    },
    {
        "id": 4,
        "name": "Casa Gangotena",
        "location": "Centro Histórico, Quito",
        "rating": 4.9,
        "price": 400,
        "type": "Hotel Boutique",
        "image": "https://images.unsplash.com/photo-1765439178218-e54dcbb64bcb?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxsdXh1cnklMjBob3RlbCUyMGV4dGVyaW9yJTIwbW9kZXJuJTIwbmlnaHR8ZW58MXx8fHwxNzcxMzc2NDQwfDA&ixlib=rb-4.1.0&q=80&w=1080",
        "badge": "Histórico"
    },
    {
        "id": 5,
        "name": "Luna Volcán",
        "location": "Baños, Ecuador",
        "rating": 4.7,
        "price": 220,
        "type": "Spa",
        "image": "https://images.unsplash.com/photo-1618500843397-cb1c3f9546aa?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxlY3VhZG9yJTIwbGFuZHNjYXBlJTIwdHJhdmVsJTIwaGlraW5nfGVufDF8fHx8MTc3MTM3NjQ0MHww&ixlib=rb-4.1.0&q=80&w=1080",
        "badge": "Aventura"
    },
    {
        "id": 6,
        "name": "Selina Cuenca",
        "location": "Cuenca, Ecuador",
        "rating": 4.5,
        "price": 60,
        "type": "Hostal",
        "image": "https://images.unsplash.com/photo-1581093195302-e5365c4d7a30?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxtb2Rlcm4lMjB0ZWNobm9sb2d5JTIwb2ZmaWNlJTIwdGVhbSUyMG1lZXRpbmd8ZW58MXx8fHwxNzcxMzc2NDQwfDA&ixlib=rb-4.1.0&q=80&w=1080",
        "badge": "Económico"
    }
]

ARTICLES = [
    {
        "id": 1,
        "title": "Los 10 mejores destinos ocultos en la Amazonía Ecuatoriana",
        "excerpt": "Descubre selvas vírgenes y comunidades locales que ofrecen experiencias de ecoturismo inigualables.",
        "date": "12 Oct, 2024",
        "author": "Zam Tech Team",
        "category": "Guía de Viaje",
        "image": "https://images.unsplash.com/photo-1715529023436-ad8c4a4f202e"
    },
    {
        "id": 2,
        "title": "Guía completa para visitar las Islas Galápagos con presupuesto",
        "excerpt": "Tips esenciales para ahorrar sin sacrificar la calidad de tu experiencia en las islas encantadas.",
        "date": "05 Nov, 2024",
        "author": "Maria Gonzalez",
        "category": "Tips de Ahorro",
        "image": "https://images.unsplash.com/photo-1729719022559-34978ede47d1"
    },
    {
        "id": 3,
        "title": "El auge del turismo digital en Latinoamérica",
        "excerpt": "Cómo la tecnología está transformando la forma en que reservamos y experimentamos nuestros viajes.",
        "date": "20 Nov, 2024",
        "author": "Carlos Zambrano",
        "category": "Tecnología",
        "image": "https://images.unsplash.com/photo-1581093195302-e5365c4d7a30"
    },
    {
        "id": 4,
        "title": "Ruta de los Volcanes: Una aventura de altura",
        "excerpt": "Prepara tu equipo y aclimátate para recorrer la famosa Avenida de los Volcanes.",
        "date": "01 Dic, 2024",
        "author": "Zam Tech Team",
        "category": "Aventura",
        "image": "https://images.unsplash.com/photo-1618500843397-cb1c3f9546aa"
    }
]

@app.context_processor
def inject_year():
    from datetime import datetime
    return {'year': datetime.now().year}

@app.route('/')
def home():
    # Enviar solo los primeros 3 como destacados
    featured_hotels = HOTELS[:3]
    return render_template('index.html', featured_hotels=featured_hotels)

@app.route('/hotel')
def hotel():
    return render_template('hotel/hotel.html', hotels=HOTELS)

@app.route('/blog')
def blog():
    return render_template('blog/blog.html', articles=ARTICLES)

@app.route('/about')
def about():
    return render_template('about/about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Aquí iría la lógica para enviar el correo o guardar en base de datos
        print(f"Nuevo mensaje de {name} ({email}): {subject} - {message}")
        
        flash('¡Gracias por contactarnos! Hemos recibido tu mensaje.', 'success')
        return redirect(url_for('contact'))
        
    return render_template('contact/contact.html')

if __name__ == '__main__':
    app.run(debug=True)
