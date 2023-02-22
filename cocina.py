
import streamlit as st
import pandas as pd

# Agrega un título a la página de la cocina
st.title("Pitarra")

# Agrega una sección para mostrar los pedidos
st.header("Cocina")

# Verifica si hay pedidos en la mesa1 y si no los hay, los inicializa como una lista vacía en el objeto de estado de sesión
if "mesa1" not in st.session_state:
    st.session_state["mesa1"] = []

# Obtiene la lista de pedidos de la mesa1 del objeto de estado de sesión
pedidos_mesa1 = st.session_state["mesa1"]

# Muestra los pedidos de la mesa1 en una tabla si hay pedidos, o un mensaje si no los hay
if len(pedidos_mesa1) > 0:
    df_mesa1 = pd.DataFrame(pedidos_mesa1)
    st.write("Pedidos de la Mesa 1:")
    st.write(df_mesa1)
else:
    st.write("No hay pedidos en la Mesa 1.")



if "productos_comida" not in st.session_state:
    st.session_state["productos_comida"] = {"Hamburguesa": 5.0, "Ensalada": 3.5}

if "productos_bebida" not in st.session_state:
    st.session_state["productos_bebida"] = {"Agua": 1.0, "Cola": 1.5}

st.header("Agregar nuevos productos")
categoria_seleccionada = st.selectbox("Selecciona una categoría:", ["Comida", "Bebida"])

nuevo_producto_nombre = st.text_input("Nombre del nuevo producto:")
nuevo_producto_precio = st.number_input("Precio del nuevo producto:", value=0.0, step=0.1)

if st.button("Agregar"):
    if categoria_seleccionada == "Comida":
        productos = st.session_state["productos_comida"]
    else:
        productos = st.session_state["productos_bebida"]
        
    productos[nuevo_producto_nombre] = nuevo_producto_precio
    
    st.success("Nuevo producto agregado!")

