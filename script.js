// Base de datos de alojamientos (en una aplicación real, esto vendría de un servidor)
let accommodations = [
    {
        id: 1,
        name: "Hotel Playa del Sol",
        type: "hotel",
        location: "Barcelona, España",
        price: 89,
        description: "Hotel de lujo frente al mar con vistas espectaculares. Incluye piscina, spa y restaurante de alta cocina.",
        imageUrl: ""
    },
    {
        id: 2,
        name: "Hostal Centro Histórico",
        type: "hostal",
        location: "Madrid, España",
        price: 35,
        description: "Acogedor hostal en el corazón de Madrid. Perfecto para jóvenes viajeros que buscan ubicación céntrica.",
        imageUrl: ""
    },
    {
        id: 3,
        name: "Apartamento Vista Montaña",
        type: "apartamento",
        location: "Granada, España",
        price: 65,
        description: "Apartamento moderno con vistas a Sierra Nevada. Totalmente equipado con cocina y sala de estar espaciosa.",
        imageUrl: ""
    },
    {
        id: 4,
        name: "Casa Rural El Olivo",
        type: "casa",
        location: "Sevilla, España",
        price: 120,
        description: "Hermosa casa rural rodeada de olivares. Ideal para familias, con jardín privado y piscina.",
        imageUrl: ""
    },
    {
        id: 5,
        name: "Cabaña en el Bosque",
        type: "cabaña",
        location: "Pirineos, España",
        price: 75,
        description: "Cabaña de madera con chimenea en medio de la naturaleza. Perfecta para una escapada romántica.",
        imageUrl: ""
    },
    {
        id: 6,
        name: "Hotel Boutique Modernista",
        type: "hotel",
        location: "Valencia, España",
        price: 110,
        description: "Hotel boutique de diseño en edificio modernista restaurado. Arte y confort en el centro de Valencia.",
        imageUrl: ""
    },
    {
        id: 7,
        name: "Apartamento Playa Malvarrosa",
        type: "apartamento",
        location: "Valencia, España",
        price: 80,
        description: "Apartamento luminoso a 100 metros de la playa. Terraza con vistas al mar y cocina completamente equipada.",
        imageUrl: ""
    },
    {
        id: 8,
        name: "Hostal La Rambla",
        type: "hostal",
        location: "Barcelona, España",
        price: 45,
        description: "Hostal económico en la famosa Rambla de Barcelona. Habitaciones limpias y personal amable.",
        imageUrl: ""
    }
];

// Función para obtener el emoji según el tipo de alojamiento
function getTypeEmoji(type) {
    const emojis = {
        'hotel': '🏨',
        'hostal': '🏩',
        'apartamento': '🏢',
        'casa': '🏡',
        'cabaña': '🏕️'
    };
    return emojis[type] || '🏠';
}

// Función para renderizar las tarjetas de alojamiento
function renderAccommodations(accommodationsToRender = accommodations) {
    const grid = document.getElementById('accommodationsGrid');
    
    if (accommodationsToRender.length === 0) {
        grid.innerHTML = '<p style="text-align: center; color: #666; padding: 2rem;">No se encontraron alojamientos que coincidan con tu búsqueda.</p>';
        return;
    }
    
    grid.innerHTML = accommodationsToRender.map(accommodation => `
        <div class="accommodation-card">
            <div class="accommodation-image">
                ${accommodation.imageUrl ? 
                    `<img src="${accommodation.imageUrl}" alt="${accommodation.name}">` : 
                    getTypeEmoji(accommodation.type)
                }
            </div>
            <div class="accommodation-content">
                <div class="accommodation-header">
                    <h3 class="accommodation-title">${accommodation.name}</h3>
                    <span class="accommodation-type">${accommodation.type}</span>
                </div>
                <p class="accommodation-location">📍 ${accommodation.location}</p>
                <p class="accommodation-description">${accommodation.description}</p>
                <p class="accommodation-price">€${accommodation.price} <span>/ noche</span></p>
            </div>
        </div>
    `).join('');
}

// Función para filtrar alojamientos
function filterAccommodations() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    const typeFilter = document.getElementById('typeFilter').value;
    
    const filtered = accommodations.filter(accommodation => {
        const matchesSearch = 
            accommodation.name.toLowerCase().includes(searchTerm) ||
            accommodation.location.toLowerCase().includes(searchTerm) ||
            accommodation.type.toLowerCase().includes(searchTerm) ||
            accommodation.description.toLowerCase().includes(searchTerm);
        
        const matchesType = !typeFilter || accommodation.type === typeFilter;
        
        return matchesSearch && matchesType;
    });
    
    renderAccommodations(filtered);
}

// Función para mostrar/ocultar el formulario
function toggleForm() {
    const form = document.getElementById('addAccommodationForm');
    if (form.style.display === 'none') {
        form.style.display = 'block';
        form.scrollIntoView({ behavior: 'smooth' });
    } else {
        form.style.display = 'none';
        form.reset();
    }
}

// Función para agregar un nuevo alojamiento
function addAccommodation(event) {
    event.preventDefault();
    
    // Generar ID único basado en el ID más alto existente
    const maxId = accommodations.length > 0 ? Math.max(...accommodations.map(a => a.id)) : 0;
    
    const newAccommodation = {
        id: maxId + 1,
        name: document.getElementById('name').value,
        type: document.getElementById('type').value,
        location: document.getElementById('location').value,
        price: parseInt(document.getElementById('price').value),
        description: document.getElementById('description').value,
        imageUrl: document.getElementById('imageUrl').value || ''
    };
    
    accommodations.unshift(newAccommodation); // Agregar al inicio del array
    renderAccommodations();
    toggleForm();
    
    // Mostrar mensaje de éxito no bloqueante
    showSuccessMessage('¡Alojamiento publicado con éxito! 🎉');
    
    // Scroll al inicio para ver el nuevo alojamiento
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Función para mostrar mensajes de éxito
function showSuccessMessage(message) {
    // Crear elemento de notificación
    const notification = document.createElement('div');
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        left: 50%;
        transform: translateX(-50%);
        background: #4caf50;
        color: white;
        padding: 1rem 2rem;
        border-radius: 5px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        z-index: 1000;
        animation: slideDown 0.3s ease-out;
    `;
    
    document.body.appendChild(notification);
    
    // Eliminar después de 3 segundos
    setTimeout(() => {
        notification.style.animation = 'slideUp 0.3s ease-out';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    renderAccommodations();
    
    const form = document.getElementById('addAccommodationForm');
    form.addEventListener('submit', addAccommodation);
    
    // Agregar event listener para búsqueda en tiempo real
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', filterAccommodations);
});
