import streamlit as st
import datetime
import pandas as pd

if "productos_comida" not in st.session_state:
    st.session_state["productos_comida"] = {"Hamburguesa": 5.0, "Ensalada": 3.5}

if "productos_bebida" not in st.session_state:
    st.session_state["productos_bebida"] = {"Agua": 1.0, "Cola": 1.5}

productos_comida = st.session_state["productos_comida"]
productos_bebida = st.session_state["productos_bebida"]

# Agrega un título a la aplicación
st.title("Pitarra")

# Agrega una sección para los productos
st.header("Bienvenido a la Mesa 1")

# Crea botones para seleccionar el producto y la cantidad
categoria_seleccionada = st.selectbox("Selecciona una categoría:", ["Comida", "Bebida"])
if categoria_seleccionada == "Comida":
    productos = productos_comida
else:
    productos = productos_bebida

producto_seleccionado = st.selectbox("Selecciona un producto:", list(productos.keys()))
cantidad_seleccionada = st.number_input("Selecciona la cantidad:", value=1, min_value=1)

# Muestra el precio del producto seleccionado
precio_unitario = productos[producto_seleccionado]
st.write(f"Precio unitario: {precio_unitario}")

if "pedidos" not in st.session_state:
    st.session_state["pedidos"] = []


# Agrega un botón para realizar el pedido
if st.button("Realizar Pedido"):
    hora = datetime.datetime.now().strftime("%H:%M:%S") # actualiza la hora en cada pedido
    precio_total = precio_unitario * cantidad_seleccionada
    pedido = {"producto": producto_seleccionado, "cantidad": cantidad_seleccionada, "hora": hora, "precio": precio_total}
    st.session_state["pedidos"].append(pedido)
    st.success("Pedido realizado.")

    # hace un dataframe para pedidos
    df = pd.DataFrame(st.session_state["pedidos"])

    st.session_state["mesa1"] = df


# Agrega un botón para mostrar la cuenta
if st.button("Cuenta"):
    st.write(st.session_state["mesa1"])

# Agrega un botón para mostrar la cuenta total
if st.button("Cuenta Total"):
    total = sum(st.session_state["mesa1"]["precio"])
    st.write(st.session_state["mesa1"])
    st.write(f"La cuenta total es: {total}")
