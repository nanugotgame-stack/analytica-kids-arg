import streamlit as st

# Configuración de la interfaz
st.set_page_config(page_title="Analytica Kids - Argentina", page_icon="🧒")

# Título y Profesional
st.title("🧒 Analytica Kids")
st.markdown("### Método de Nutrición Invisible")
st.caption("Desarrollado por el Lic. Emanuel Viberti")

# ESTRATEGIA DE VENTA: Banner del PDF Premium
st.info("🚀 **¿Querés 20 recetas exclusivas más?** Desbloqueá platos técnicos como Ñoquis Invisibles, Albóndigas de Ricota y la Guía de Marcas por solo **$10.000**.")
if st.button("Comprar PDF Premium ($10.000)"):
    st.write("🔗 Redirigiendo a Mercado Pago / WhatsApp...")

st.divider()

# BASE DE DATOS: Los 20 Platos Gratuitos
platos = {
    "Fideos Blancos": ["Albúmina en polvo disuelta en la manteca/aceite de servido[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span).", "Proteína de alta calidad[span_4](start_span)[span_4](end_span)."],
    "Puré de Papas": ["Mezcla con 10% de coliflor blanca procesada a punto crema[span_5](start_span)[span_5](end_span)[span_6](start_span)[span_6](end_span).", "Fibra y Vitaminas[span_7](start_span)[span_7](end_span)."],
    "Arroz Blanco": ["Cocción en caldo de huesos casero filtrado (transparente)[span_8](start_span)[span_8](end_span)[span_9](start_span)[span_9](end_span).", "Aminoácidos y Minerales[span_10](start_span)[span_10](end_span)."],
    "Milanesas": ["Mezclar pan rallado con harina de girasol molida extra fina[span_11](start_span)[span_11](end_span)[span_12](start_span)[span_12](end_span).", "Zinc y Magnesio[span_13](start_span)[span_13](end_span)."],
    "Nuggets": ["Pincelar con aceite de coco neutro (sin olor)[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span).", "Grasas saludables[span_16](start_span)[span_16](end_span)."],
    "Tostadas": ["Capa milimétrica de mantequilla de maní bajo el queso[span_17](start_span)[span_17](end_span)[span_18](start_span)[span_18](end_span).", "Energía densa[span_19](start_span)[span_19](end_span)."],
    "Yogur Vainilla": ["Inulina o Psyllium en polvo (mezclar bien sin grumos)[span_20](start_span)[span_20](end_span)[span_21](start_span)[span_21](end_span).", "Salud Intestinal[span_22](start_span)[span_22](end_span)."],
    "Polenta": ["Preparar con leche fortificada y queso reggianito fino[span_23](start_span)[span_23](end_span)[span_24](start_span)[span_24](end_span).", "Calcio[span_25](start_span)[span_25](end_span)."],
    "Gelatina": ["Uso de jugos naturales de frutas colados (sin pulpa)[span_26](start_span)[span_26](end_span)[span_27](start_span)[span_27](end_span).", "Antioxidantes[span_28](start_span)[span_28](end_span)."],
    "Panqueques": ["Sustitución parcial de leche por yogur griego natural[span_29](start_span)[span_29](end_span)[span_30](start_span)[span_30](end_span).", "Proteína[span_31](start_span)[span_31](end_span)."],
    "Pizza (Muzza)": ["Puré de calabaza filtrado dentro de la salsa de tomate[span_32](start_span)[span_32](end_span)[span_33](start_span)[span_33](end_span).", "Vitamina A[span_34](start_span)[span_34](end_span)."],
    "Salchichas": ["Hervir en caldo de carne real en lugar de agua[span_35](start_span)[span_35](end_span)[span_36](start_span)[span_36](end_span).", "Hierro y B12[span_37](start_span)[span_37](end_span)."],
    "Carne Picada": ["Mezcla con zanahoria rallada ultra fina (que se deshaga)[span_38](start_span)[span_38](end_span)[span_39](start_span)[span_39](end_span).", "Betacarotenos[span_40](start_span)[span_40](end_span)."],
    "Manzana Pelada": ["Almíbar ligero de miel y limón para evitar oxidación[span_41](start_span)[span_41](end_span)[span_42](start_span)[span_42](end_span).", "Vitamina C[span_43](start_span)[span_43](end_span)."],
    "Banana": ["Pizca de coco rallado extra fino[span_44](start_span)[span_44](end_span)[span_45](start_span)[span_45](end_span).", "Potasio[span_46](start_span)[span_46](end_span)."],
    "Huevo Duro": ["Procesar yema con una pizca de palta (textura crema)[span_47](start_span)[span_47](end_span)[span_48](start_span)[span_48](end_span).", "Grasas DHA[span_49](start_span)[span_49](end_span)."],
    "Sopa de Letras": ["Base de caldo concentrado de vegetales blancos[span_50](start_span)[span_50](end_span)[span_51](start_span)[span_51](end_span).", "Minerales[span_52](start_span)[span_52](end_span)."],
    "Galletitas de Agua": ["Acompañar con dip de queso y polvo de lentejas rojas[span_53](start_span)[span_53](end_span)[span_54](start_span)[span_54](end_span).", "Hierro[span_55](start_span)[span_55](end_span)."],
    "Pochoclos": ["Rociar con polvo de semillas de zapallo molidas[span_56](start_span)[span_56](end_span)[span_57](start_span)[span_57](end_span).", "Zinc[span_58](start_span)[span_58](end_span)."],
    "Copos de Maíz": ["Microdosis de polen de abeja molido[span_59](start_span)[span_59](end_span)[span_60](start_span)[span_60](end_span).", "Multivitamínico[span_61](start_span)[span_61](end_span)."]
}

# Renderizado de la lista
st.write("Seleccioná el plato seguro que tu hijo ya acepta:")
for nombre, detalles in platos.items():
    with st.expander(f"🍴 {nombre}"):
        st.markdown(f"**Hack Invisible:** {detalles[0]}")
        st.success(f"**Aporte Nutricional:** {detalles[1]}")
        st.caption("💡 *Regla de Oro: Empezar con una pizca microscopic e ir subiendo gradualmente[span_62](start_span)[span_62](end_span).*")

# Contacto
st.divider()
st.markdown("📩 **Consultas Personalizadas:** [WhatsApp Lic. Viberti](https://wa.me/5491136768018)[span_63](start_span)[span_63](end_span)[span_64](start_span)[span_64](end_span)")
