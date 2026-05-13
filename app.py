import streamlit as st

# Configuración de la interfaz
st.set_page_config(page_title="Analytica Kids - Argentina", page_icon="🧒")

# Título y Profesional
st.title("🧒 Analytica Kids")
st.markdown("### Método de Nutrición Invisible")
st.caption("Desarrollado por el Lic. Emanuel Viberti")

# ESTRATEGIA DE VENTA
st.info("🚀 **¿Querés 20 recetas exclusivas más?** Desbloqueá platos técnicos como Ñoquis Invisibles, Albóndigas de Ricota y la Guía de Marcas por solo **$10.000**.")

# Aquí podés poner tu link de Mercado Pago o que te mande al WhatsApp
if st.button("Comprar PDF Premium ($10.000)"):
    st.write("🔗 Redirigiendo a WhatsApp para coordinar el pago...")

st.divider()

# BASE DE DATOS: Los 20 Platos Gratuitos
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
    "Manzana Pelada": ["Almíbar ligero de miel y limón para evitar que se ponga marrón.", "Vitamina C."],
    "Banana": ["Pizca de coco rallado extra fino.", "Potasio."],
    "Huevo Duro": ["Procesar la yema con una pizca de palta para hacer una crema.", "Grasas DHA."],
    "Sopa de Letras": ["Base de caldo concentrado de vegetales blancos.", "Minerales."],
    "Galletitas de Agua": ["Acompañar con un dip de queso y polvo de lentejas rojas.", "Hierro."],
    "Pochoclos": ["Rociar con polvo de semillas de zapallo molidas muy finas.", "Zinc."],
    "Copos de Maíz": ["Microdosis de polen de abeja molido.", "Multivitamínico natural."]
}

# Renderizado de la lista
st.write("Seleccioná el plato seguro que tu hijo ya acepta:")
for nombre, detalles in platos.items():
    with st.expander(f"🍴 {nombre}"):
        st.markdown(f"**¿Cómo enriquecerlo?**\n\n{detalles[0]}")
        st.success(f"**¿Qué aporta?**\n\n{detalles[1]}")
        st.caption("💡 *Regla de Oro: Empezar con una pizca microscópica e ir subiendo gradualmente.*")

# Contacto
st.divider()
st.markdown("📩 **Consultas Personalizadas:** [WhatsApp Lic. Viberti](https://wa.me/5491136768018)")
