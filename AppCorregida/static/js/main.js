const titulo = document.getElementById("titulo");

titulo.textContent = "NUESTRO GESTOR DE PRODUCTOS";

titulo.style.backgroundColor = "#052B75" 

const miBoton = document.querySelector("#boton-magico");

miBoton.addEventListener("click", function() {
    console.log("¡Has pulsado el botón!");
    document.body.classList.toggle("modo-alternativo");
});

/* --- FILTROS DINÁMICOS --- */
const botonesFiltro = document.querySelectorAll('.btn-filtro');
const secciones = document.querySelectorAll('section');
const separadores = document.querySelectorAll('hr');

botonesFiltro.forEach(boton => {
    boton.addEventListener('click', () => {
        // 1. Efecto visual en los botones
        botonesFiltro.forEach(b => b.classList.remove('active'));
        boton.classList.add('active');

        // 2. Lógica de filtrado
        const filtro = boton.getAttribute('data-filtro');

        secciones.forEach((seccion, index) => {
            const categoria = seccion.getAttribute('data-categoria');
            
            if (filtro === 'todos' || filtro === categoria) {
                seccion.classList.remove('oculto');
                if(separadores[index]) separadores[index].classList.remove('hr-oculto');
            } else {
                seccion.classList.add('oculto');
                if(separadores[index]) separadores[index].classList.add('hr-oculto');
            }
        });
    });
});

/* --- VENTANAS MODALES --- */
const modal = document.getElementById('modal-producto');
const modalTitulo = document.getElementById('modal-titulo');
const modalImagen = document.getElementById('modal-imagen');
const modalDetalles = document.getElementById('modal-detalles');
const btnCerrar = document.querySelector('.cerrar-modal');
const tarjetasProducto = document.querySelectorAll('.ficha-producto');

// Abrir modal al hacer clic en cualquier producto
tarjetasProducto.forEach(tarjeta => {
    tarjeta.addEventListener('click', (e) => {
        e.preventDefault(); // Evita que la página salte arriba si clican en la imagen (etiqueta <a>)
        
        // Capturar la información de la tarjeta seleccionada
        const titulo = tarjeta.querySelector('h3').textContent;
        const imgSrc = tarjeta.querySelector('img').src;
        const detallesHTML = tarjeta.querySelector('ul').innerHTML;

        // Inyectar la información en el Modal
        modalTitulo.textContent = titulo;
        modalImagen.src = imgSrc;
        modalDetalles.innerHTML = detallesHTML;

        // Mostrar el modal disparando el Feedback Visual CSS
        modal.classList.add('mostrar');
    });
});

// Lógica para cerrar el modal (clic en la X)
btnCerrar.addEventListener('click', () => {
    modal.classList.remove('mostrar');
});

// Lógica para cerrar el modal haciendo clic fuera de él (en el fondo oscuro)
window.addEventListener('click', (e) => {
    if (e.target === modal) {
        modal.classList.remove('mostrar');
    }
});