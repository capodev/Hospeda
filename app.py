from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

# Datos simulados (mock data) para pasar a las plantillas
HOTELS = [
    
    {
    "id": 1,
    "name": "Royal Palm Galapagos",
    "description": "Un oasis de lujo en el corazón de las Islas Galápagos, donde la naturaleza se encuentra con la elegancia. Disfruta de vistas impresionantes, servicio excepcional y una experiencia inolvidable en este paraíso ecológico.",
    "slug": "royal-palm-galapagos",
    "rating": 4.9,
    "pet_friendly": True,
    "price_range": "$150 - $500 ",
    "amenities": ["Piscina", "Parqueadero gratuito", "Gimnasio", "Restaurante"],
    "location": "Santa Cruz, Galápagos",
    "image": "https://images.unsplash.com/photo-1729719022559-34978ede47d1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxsdXh1cnklMjByZXNvcnQlMjBzd2ltbWluZyUyMHBvb2x8ZW58MXx8fHwxNzcxMzc2NDQwfDA&ixlib=rb-4.1.0&q=80&w=1080",
    "adicional_info": {
            "check_in": "3:00 PM",
            "check_out": "11:00 AM",
            "cancellation_policy": "Cancelación gratuita hasta 48 horas antes de la llegada",
            "payment_methods": ["Tarjeta de crédito", "Transferencia bancaria", "Efectivo"]
        },
    "rooms": [
      {
        "type": "Suite Nupcial",
        "price": 350,
        "amenities": ["Agua caliente", "Jacuzzi privado", "WiFi", "Minibar"],
        "capacity": 2,
        "images": ["https://images.unsplash.com/photo-1729719022559-34978ede47d1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxsdXh1cnklMjByZXNvcnQlMjBzd2ltbWluZyUyMHBvb2x8ZW58MXx8fHwxNzcxMzc2NDQwfDA&ixlib=rb-4.1.0&q=80&w=1080","https://images.unsplash.com/photo-1715529023436-ad8c4a4f202e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxnbGFtcGluZyUyMHRlbnQlMjBmb3Jlc3QlMjBuYXR1cmV8ZW58MXx8fHwxNzcxMzc2NDQxfDA&ixlib=rb-4.1.0&q=80&w=1080"]
      },
      {
        "type": "Habitación Doble",
        "price": 180,
        "amenities": ["Agua caliente", "Aire acondicionado", "TV Cable"],
        "capacity": 2,
        "images": ["https://images.unsplash.com/photo-1729719022559-34978ede47d1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxsdXh1cnklMjByZXNvcnQlMjBzd2ltbWluZyUyMHBvb2x8ZW58MXx8fHwxNzcxMzc2NDQwfDA&ixlib=rb-4.1.0&q=80&w=1080","https://images.unsplash.com/photo-1715529023436-ad8c4a4f202e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxnbGFtcGluZyUyMHRlbnQlMjBmb3Jlc3QlMjBuYXR1cmV8ZW58MXx8fHwxNzcxMzc2NDQxfDA&ixlib=rb-4.1.0&q=80&w=1080"]
      },
      {
        "type": "Habitación Triple",
        "price": 280,
        "amenities": ["Agua caliente", "Aire acondicionado", "TV Cable", "WiFi","Minibar", "Balcón con vista al mar","Netflix"],
        "capacity": 3,
        "images": ["https://images.unsplash.com/photo-1729719022559-34978ede47d1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxsdXh1cnklMjByZXNvcnQlMjBzd2ltbWluZyUyMHBvb2x8ZW58MXx8fHwxNzcxMzc2NDQwfDA&ixlib=rb-4.1.0&q=80&w=1080","https://images.unsplash.com/photo-1715529023436-ad8c4a4f202e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxnbGFtcGluZyUyMHRlbnQlMjBmb3Jlc3QlMjBuYXR1cmV8ZW58MXx8fHwxNzcxMzc2NDQxfDA&ixlib=rb-4.1.0&q=80&w=1080"]
      }
    ]
    },
    {
    "id": 2,
    "name": "Mashpi Lodge",
    "description": "Un refugio natural en el corazón del Chocó Andino, donde la biodiversidad se combina con una experiencia de alojamiento única. Disfruta de paisajes exuberantes, guías expertos y un entorno ecológico protegido.",
    "slug": "mashpi-lodge",
    "rating": 5.0,
    "pet_friendly": False,
    "price_range": "$200 - $600 ",
    "amenities": ["Guías biólogos", "Centro de investigación", "Terraza de observación", "Restaurante Gourmet"],
    "location": "Pichincha, Chocó Andino",
    "image": "https://images.unsplash.com/photo-1715529023436-ad8c4a4f202e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxnbGFtcGluZyUyMHRlbnQlMjBmb3Jlc3QlMjBuYXR1cmV8ZW58MXx8fHwxNzcxMzc2NDQxfDA&ixlib=rb-4.1.0&q=80&w=1080",
    "adicional_info": {
      "check_in": "2:00 PM",
      "check_out": "12:00 PM",
      "cancellation_policy": "Cancelación 7 días antes para reembolso total",
      "payment_methods": ["Tarjeta de crédito", "Transferencia", "PayPal"]
    },
    "rooms": [
      {
        "type": "Wayra Room",
        "price": 450,
        "amenities": ["Ventilador de techo", "Caja fuerte", "Agua caliente", "Bata de baño"],
        "capacity": 2,
        "images": ["https://images.unsplash.com/photo-1590490360182-c33d57733427?w=1080", "https://images.unsplash.com/photo-1566665797739-1674de7a421a?w=1080"]
      },
      {
        "type": "Yaku Suite",
        "price": 600,
        "amenities": ["Tina exenta", "Cama King", "Agua caliente", "Sala de estar"],
        "capacity": 3,
        "images": ["https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=1080", "https://images.unsplash.com/photo-1544124499-58912cbddaad?w=1080"]
      }
    ]
  },
  {
    "id": 3,
    "name": "Swissôtel Quito",
    "description": "Un oasis de lujo en el corazón de Quito, donde la elegancia se encuentra con la comodidad. Disfruta de vistas panorámicas, servicio excepcional y una experiencia inolvidable en este refugio urbano.",
    "slug": "swissotel-quito",
    "rating": 4.8,
    "pet_friendly": True,
    "price_range": "$180 - $300 ",
    "amenities": ["Piscina climatizada", "Business Center", "Spa de lujo", "Parqueadero"],
    "location": "Quito, Ecuador",
    "image": "https://images.unsplash.com/photo-1572177215152-32f247303126?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxtb2Rlcm4lMjBob3RlbCUyMGJlZHJvb20lMjBpbnRlcmlvcnxlbnwxfHx8fDE3NzEzMTE0NzJ8MA&ixlib=rb-4.1.0&q=80&w=1080",
    "adicional_info": {
      "check_in": "3:00 PM",
      "check_out": "12:00 PM",
      "cancellation_policy": "Cancelación gratuita hasta las 6 PM del día de llegada",
      "payment_methods": ["Tarjeta de crédito", "Débito", "Efectivo"]
    },
    "rooms": [
      {
        "type": "Habitación Ejecutiva",
        "price": 180,
        "amenities": ["Escritorio", "WiFi Alta Velocidad", "TV Smart", "Aire acondicionado"],
        "capacity": 2,
        "images": ["https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=1080","https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=1080"]
      },
      {
        "type": "Junior Suite",
        "price": 280,
        "amenities": ["Minibar", "Acceso al Lounge", "Agua caliente", "Sofá cama"],
        "capacity": 4,
        "images": ["https://images.unsplash.com/photo-1591088398332-8a77d399c843?w=1080","https://images.unsplash.com/photo-1591088398332-8a77d399c843?w=1080"]
      }
    ]
  },
  {
    "id": 4,
    "name": "Casa Gangotena",
    "description": "Un oasis de lujo en el corazón del Centro Histórico de Quito, donde la elegancia se encuentra con la historia. Disfruta de vistas impresionantes, servicio excepcional y una experiencia inolvidable en este refugio urbano.",
    "slug": "casa-gangotena",
    "rating": 4.9,
    "pet_friendly": False,
    "price_range": "$250 - $450 ",
    "amenities": ["Té de la tarde", "Terraza panorámica", "Jardín interno", "Concierge"],
    "location": "Centro Histórico, Quito",
    "image": "https://images.unsplash.com/photo-1765439178218-e54dcbb64bcb?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxsdXh1cnklMjBob3RlbCUyMGV4dGVyaW9yJTIwbW9kZXJuJTIwbmlnaHR8ZW58MXx8fHwxNzcxMzc2NDQwfDA&ixlib=rb-4.1.0&q=80&w=1080",
    "adicional_info": {
      "check_in": "2:00 PM",
      "check_out": "11:00 AM",
      "cancellation_policy": "Requiere depósito del 50% reembolsable",
      "payment_methods": ["Tarjeta de crédito", "Transferencia bancaria"]
    },
    "rooms": [
      {
        "type": "Luxury Room",
        "price": 400,
        "amenities": ["Agua caliente", "WiFi", "Amenities orgánicos", "Caja fuerte"],
        "capacity": 2,
        "images": ["https://images.unsplash.com/photo-1505691723518-36a5ac3be353?w=1080","https://images.unsplash.com/photo-1505691723518-36a5ac3be353?w=1080"]
      },
      {
        "type": "Plaza View Room",
        "price": 520,
        "amenities": ["Vista a la plaza", "Agua caliente", "Ducha de lluvia", "WiFi"],
        "capacity": 2,
        "images": ["https://images.unsplash.com/photo-1618773928121-c32242e63f39?w=1080","https://images.unsplash.com/photo-1618773928121-c32242e63f39?w=1080"]
      }
    ]
  },
  {
    "id": 5,
    "name": "Luna Volcán",
    "description": "Un oasis de lujo en el corazón de Baños, donde la naturaleza se encuentra con la aventura. Disfruta de vistas impresionantes, servicio excepcional y una experiencia inolvidable en este refugio volcánico.",
    "slug": "luna-volcan",
    "rating": 4.7,
    "pet_friendly": False,
    "price_range": "$220 - $310 ",
    "amenities": ["Piscinas de agua termal", "Mirador al volcán", "Café del Cielo", "Spa"],
    "location": "Baños, Ecuador",
    "image": "https://images.unsplash.com/photo-1618500843397-cb1c3f9546aa?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxlY3VhZG9yJTIwbGFuZHNjYXBlJTIwdHJhdmVsJTIwaGlraW5nfGVufDF8fHx8MTc3MTM3NjQ0MHww&ixlib=rb-4.1.0&q=80&w=1080",
    "adicional_info": {
      "check_in": "3:00 PM",
      "check_out": "12:00 PM",
      "cancellation_policy": "No reembolsable en temporada alta",
      "payment_methods": ["Efectivo", "Tarjeta de crédito"]
    },
    "rooms": [
      {
        "type": "Habitación Romántica",
        "price": 220,
        "amenities": ["Chimenea", "Agua caliente", "WiFi", "Balcón"],
        "capacity": 2,
        "images": ["https://images.unsplash.com/photo-1590073844006-33379778ae09?w=1080",   "https://images.unsplash.com/photo-1590073844006-33379778ae09?w=1080"]
      },
      {
        "type": "Suite Volcán",
        "price": 310,
        "amenities": ["Jacuzzi", "Vista al cráter", "Agua caliente", "Minibar"],
        "capacity": 3,
        "images": ["https://images.unsplash.com/photo-1598928506311-c55ded91a20c?w=1080","https://images.unsplash.com/photo-1598928506311-c55ded91a20c?w=1080"]
      }
    ]
  },
  {
    "id": 6,
    "name": "Selina Cuenca",
    "description": "Un oasis de creatividad en el corazón de Cuenca, donde el arte se encuentra con la comunidad. Disfruta de un ambiente vibrante, eventos culturales y una experiencia única en este refugio urbano.",
    "slug": "selina-cuenca",
    "rating": 4.5,
    "pet_friendly": True,
    "price_range": "$15 - $60 ",
    "amenities": ["Espacio Cowork", "Cocina comunitaria", "Clases de Yoga", "Bar/Cine"],
    "location": "Cuenca, Ecuador",
    "image": "https://images.unsplash.com/photo-1581093195302-e5365c4d7a30?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxtb2Rlcm4lMjB0ZWNobm9sb2d5JTIwb2ZmaWNlJTIwdGVhbSUyMG1lZXRpbmd8ZW58MXx8fHwxNzcxMzc2NDQwfDA&ixlib=rb-4.1.0&q=80&w=1080",
    "adicional_info": {
      "check_in": "3:00 PM",
      "check_out": "11:00 AM",
      "cancellation_policy": "Cancelación gratuita hasta 24 horas antes",
      "payment_methods": ["PayPal", "Efectivo", "Tarjeta de crédito"]
    },
    "rooms": [
      {
        "type": "Dormitorio Compartido",
        "price": 25,
        "amenities": ["Luz de lectura", "Locker privado", "WiFi", "Baño compartido"],
        "capacity": 1,
        "images": ["https://images.unsplash.com/photo-1555854817-40e098ee7f57?w=1080","https://images.unsplash.com/photo-1555854817-40e098ee7f57?w=1080"]
      },
      {
        "type": "The Standard",
        "price": 60,
        "amenities": ["Baño privado", "Agua caliente", "Escritorio", "WiFi"],
        "capacity": 2,
        "images": ["https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?w=1080","https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?w=1080"]
      }
    ]
  },
  {
    "id": 7,
    "name": "Hotel El Cangrejal",
    "description": "Un oasis de tranquilidad en el corazón de Guayaquil, donde la naturaleza se encuentra con la comodidad. Disfruta de vistas impresionantes, servicio excepcional y una experiencia inolvidable en este refugio urbano.",
    "slug": "hotel-el-cangrejal",
    "rating": 4.2,
    "pet_friendly": False,
    "price_range": "$75 - $120 ",
    "amenities": ["Piscina", "Restaurante", "Bar", "Spa"],
    "location": "Guayaquil, Ecuador",
    "image": "https://images.unsplash.com/photo-1581093195302-e5365c4d7a30?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxlY3VhZG9yJTIwbGFuZHNjYXBlJTIwdHJhdmVsJTIwaGlraW5nfGVufDF8fHx8MTc3MTM3NjQ0MHww&ixlib=rb-4.1.0&q=80&w=1080",
    "adicional_info": {
      "check_in": "2:00 PM",
      "check_out": "12:00 PM",
      "cancellation_policy": "Cancelación gratuita hasta 48 horas antes",
      "payment_methods": ["Tarjeta de crédito", "Transferencia bancaria"]
    },
    "rooms": [
      {
        "type": "Habitación Estándar",
        "price": 75,
        "amenities": ["Agua caliente", "WiFi", "TV por cable", ""],
        "capacity": 2,
        "images": ["https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?w=1080","https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?w=1080"]
      }
    ]
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

# @app.route('/')
# def home():
    
#     featured_hotels = HOTELS
#     return render_template('index.html', featured_hotels=featured_hotels,text="Book Now")

# @app.route('/<slug>')
# def home(slug):
#     if slug is  None:
#         featured_hotels = HOTELS
#         return render_template('index.html', featured_hotels=featured_hotels,text="Book Now")
#     else:
#         featured_hotels = HOTELS
#         return render_template('saludo.html',featured_hotels=featured_hotels,text="Book Now")


@app.route('/') # Para el Home normal
@app.route('/<slug>') # Para cuando llega un slug
def home(slug=None): # Ponemos None por defecto
    featured_hotels = HOTELS
    
    if slug is None:
        # CASO: localhost:5000/
        return render_template('index.html', 
                               featured_hotels=featured_hotels, 
                               text="Book Now")
    else:
        # CASO: localhost:5000/cualquier-cosa
        # Aquí podrías buscar si el slug existe, pero según tu idea:
        return render_template('saludo.html', 
                               featured_hotels=featured_hotels, 
                               text="Book Now", slug=slug)

    
@app.route('/hotels')
def hotels():
    return render_template('hotel/hotel.html', hotels=HOTELS, text="View Details")

@app.route('/hotels/<slug>')
def hotels_view(slug):
    # Buscamos el objeto del hotel en tu array HOTELS
    hotel_encontrado = next((h for h in HOTELS if h['slug'] == slug), None)
    
    if not hotel_encontrado:
        return render_template('404.html'), 404 
        
    return render_template('hotel/hotel_view.html', hotel=hotel_encontrado)  

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
