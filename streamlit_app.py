import streamlit as st
import pandas as pd

st.write("###### José Antonio Delgado Guillermo")

def generar_tabla(cantidad, meses):
    if meses == 6:
        tasa = 0.06
    elif meses == 12:
        tasa = 0.05
    elif meses == 18:
        tasa = 0.04
    elif meses == 24:
        tasa = 0.02
    else:
        st.error("Plazo no válido.")
        return None

    pago_mensual = cantidad * tasa / (1 - (1 + tasa) ** -meses)
    saldo_actual = cantidad
    total_intereses = 0

    tabla_datos = []

    for mes in range(1, meses + 1):
        interes_mes = saldo_actual * tasa
        amortizacion_mes = pago_mensual - interes_mes
        saldo_actual -= amortizacion_mes
        total_intereses += interes_mes

        tabla_datos.append([mes, pago_mensual, interes_mes, amortizacion_mes, saldo_actual])

    tabla_df = pd.DataFrame(tabla_datos, columns=['Mes', 'Pago Mensual', 'Interés', 'Amortización', 'Saldo Restante'])
    
    st.write(f"### Tabla de Amortización para {meses} meses con {tasa*100}% de interés mensual")
    st.dataframe(tabla_df.style.format({
        "Pago Mensual": "{:,.2f}",
        "Interés": "{:,.2f}",
        "Amortización": "{:,.2f}",
        "Saldo Restante": "{:,.2f}"
    }))

    st.write(f"**Total de intereses pagados en {meses} meses:** ${total_intereses:,.2f}")

st.title("Sistema de Amortización de Préstamos")

monto_prestamo = st.number_input("Introduce el monto del préstamo ($):", min_value=1000.0, value=50000.0, step=1000.0)

plazo = st.selectbox("Selecciona el plazo en meses:", [6, 12, 18, 24])

if st.button("Calcular Amortización"):
    generar_tabla(monto_prestamo, plazo)
