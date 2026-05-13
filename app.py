import streamlit as st
import urllib.parse

# Configuración de la interfaz
st.set_page_config(page_title="Analytica Kids - Argentina", page_icon="🧒")

# Título y Profesional
st.title("🧒 Analytica Kids")
st.markdown("### Método de Nutrición Invisible")
st.caption("Desarrollado por el Lic. Emanuel Viberti")

st.divider()

# BASE DE DATOS: Los 20 Platos Gratuitos (Matriz Argentina)
platos = {
    "Fideos Blancos": ["Albúmina en polvo disuelta en la manteca o aceite de servido.", "Proteína de alta calidad para el desarrollo muscular."],
    "Puré de Papas": ["Mezcla con 10% de coliflor blanca procesada a punto crema.", "Fibra y vitaminas esenciales."],
    "Arroz Blanco": ["Cocción en caldo de huesos casero filtrado (transparente) en lugar de agua.", "Aminoácidos y minerales para la salud intestinal."],
    "Milanesas": ["Mezclar pan rallado con harina de girasol molida extra fina.", "Zinc y Magnesio para el crecimiento."],
    "Nuggets": ["Pincelar con aceite de coco neutro (sin olor).", "Grasas saludables."],
    "Tostadas": ["Capa milimétrica de mantequilla de maní bajo el queso.", "Energía densa."],
    "Yogur Vainilla": ["Inulina o Psyllium en polvo (mezclar bien sin grumos).", "Salud intestinal y prebióticos."],
    "Polenta": ["Preparar con leche fortificada y queso reggianito fino.", "Calcio para los huesos."],
    "Gelatina": ["Uso de jugos naturales de frutas colados (sin pulpa).", "Antioxidantes naturales."],
    "Panqueques": ["Sustitución parcial de leche por yogur griego natural.", "Proteína extra."],
    "Pizza (Muzza)": ["Puré de calabaza filtrado dentro de la salsa de tomate.", "Vitamina A."],
    "Salchichas": ["Hervir en caldo de carne real en lugar de agua.", "Hierro y B12."],
    "Carne Picada": ["Mezcla con zanahoria rallada ultra fina hasta que se deshaga.", "Betacarotenos."],
    "Manzana Pelada": ["Almíbar ligero de miel y limón para evitar la oxidación.", "Vitamina C."],
    "Banana": ["Pizca de coco rallado extra fino.", "Potasio."],
    "Huevo Duro": ["Procesar la yema con una pizca de palta para hacer una crema.", "Grasas DHA."],
    "Sopa de Letras": ["Base de caldo concentrado de vegetales blancos.", "Minerales."],
    "Galletitas de Agua": ["Acompañar con un dip de queso y polvo de lentejas rojas.", "Hierro."],
    "Pochoclos": ["Rociar con polvo de semillas de zapallo molidas muy finas.", "Zinc."],
    "Copos de Maíz": ["Microdosis de polen de abeja molido.", "Multivitamínico natural."]
}

# Renderizado de la lista
st.write("Seleccioná el plato seguro que tu hijo ya acepta para ver cómo enriquecerlo:")
for nombre, detalles in platos.items():
    with st.expander(f"🍴 {nombre}"):
        st.markdown(f"**¿Cómo enriquecerlo?**\n\n{detalles[0]}")
        st.success(f"**¿Qué aporta?**\n\n{detalles[1]}")
        st.caption("💡 *Regla de Oro: Empezar con una pizca microscópica e ir subiendo gradualmente.*")

st.divider()

# ESTRATEGIA DE VENTA: PDF PREMIUM
st.markdown("### 🚀 ¿Querés llevar la nutrición al siguiente nivel?")
st.write("Desbloqueá la **Guía Completa PDF** con 40 platos técnicos (Ñoquis invisibles, albóndigas de ricota y más) y la lista de marcas recomendadas en Argentina.")

# Tu Link de Mercado Pago configurado
url_mercado_pago = "https://mpago.la/1hsixwg"

st.link_button("🔥 COMPRAR GUÍA COMPLETA ($10.000)", url_mercado_pago)
st.info("Al completar el pago, el sistema te redirigirá a mi WhatsApp para enviarte el archivo a tu email.")

st.divider()

# ATENCIÓN INDIVIDUAL
st.markdown("### 📩 ¿Necesitás un plan a medida?")
st.write("Si querés consultar por un plan 100% adaptado a tu hijo/a, no dudes en escribirme.")

# Mensaje para consulta de plan
msg_consulta = "Hola Lic. Viberti, vi la app Analytica Kids y me gustaría consultar por un plan 100% adaptado para mi hijo/a."
msg_encoded = urllib.parse.quote(msg_consulta)
url_wa_consulta = f"https://wa.me/5491136768018?text={msg_encoded}"

st.markdown(f"[**👉 Escribirme por WhatsApp ahora**]({url_wa_consulta})")

# Redes Sociales
st.divider()
st.caption("Instagram: @viberti.nutricion | X: @eevibe")
st.caption("© 2026 Analytica - Todos los derechos reservados")
