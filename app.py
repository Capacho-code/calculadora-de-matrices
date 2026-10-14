import streamlit as st

st.title("🧮 Calculadora de Matrices por Cramer (Paso a Paso)")
st.write(
    "Selecciona el sistema de ecuaciones e ingresa los valores para ver la"
    " solución con procedimiento."
)

opcion = st.selectbox("Elige el tipo de sistema:", ["Sistema 2x2", "Sistema 3x3"])

if opcion == "Sistema 2x2":
  st.subheader("Ecuaciones: ax + by = c  |  dx + ey = f")

  col1, col2, col3 = st.columns(3)
  with col1:
    a = st.number_input("a", value=0.0)
    d = st.number_input("d", value=0.0)
  with col2:
    b = st.number_input("b", value=0.0)
    e = st.number_input("e", value=0.0)
  with col3:
    c = st.number_input("c", value=0.0)
    f = st.number_input("f", value=0.0)

  if st.button("Resolver 2x2"):
    # Cálculos de los determinantes
    delta_s = a * e - d * b
    delta_x = c * e - f * b
    delta_y = a * f - d * c

    st.markdown("---")
    st.subheader("📋 Procedimiento Paso a Paso:")

    # Paso 1: Determinante del Sistema
    st.write("### 1. Determinante del Sistema (Δs)")
    st.write(f"Δs = ({a} × {e}) - ({d} × {b})")
    st.write(f"**Δs = {delta_s}**")

    if delta_s != 0:
      # Paso 2: Determinante de X
      st.write("### 2. Determinante de X (Δx)")
      st.write(f"Δx = ({c} × {e}) - ({f} × {b})")
      st.write(f"**Δx = {delta_x}**")

      # Paso 3: Determinante de Y
      st.write("### 3. Determinante de Y (Δy)")
      st.write(f"Δy = ({a} × {f}) - ({d} × {c})")
      st.write(f"**Δy = {delta_y}**")

      # Paso 4: Resultados finales
      x = delta_x / delta_s
      y = delta_y / delta_s

      st.write("### 4. Valores finales")
      st.write(f"**X** = Δx / Δs = {delta_x} / {delta_s} = **{x}**")
      st.write(f"**Y** = Δy / Δs = {delta_y} / {delta_s} = **{y}**")

      st.success(f"¡Solución completada! X = {x}, Y = {y}")
    else:
      if delta_x == 0 and delta_y == 0:
        st.warning("Como Δs = 0 y Δx = Δy = 0, el sistema tiene soluciones infinitas.")
      else:
        st.error("Como Δs = 0, el sistema no tiene solución (las rectas son paralelas).")

else:
  st.subheader(
      "Ecuaciones: ax + by + cz = d  |  ex + fy + gz = h  |  ix + jy + kz = l"
  )

  # Fila 1
  c1, c2, c3, c4 = st.columns(4)
  with c1:
    a = st.number_input("a", value=0.0)
  with c2:
    b = st.number_input("b", value=0.0)
  with c3:
    c = st.number_input("c", value=0.0)
  with c4:
    d = st.number_input("d", value=0.0)

  # Fila 2
  c1, c2, c3, c4 = st.columns(4)
  with c1:
    e = st.number_input("e", value=0.0)
  with c2:
    f = st.number_input("f", value=0.0)
  with c3:
    g = st.number_input("g", value=0.0)
  with c4:
    h = st.number_input("h", value=0.0)

  # Fila 3
  c1, c2, c3, c4 = st.columns(4)
  with c1:
    i = st.number_input("i", value=0.0)
  with c2:
    j = st.number_input("j", value=0.0)
  with c3:
    k = st.number_input("k", value=0.0)
  with c4:
    l = st.number_input("l", value=0.0)

  if st.button("Resolver 3x3"):
    delta_s = a * (f * k - j * g) - b * (e * k - i * g) + c * (e * j - i * f)
    delta_x = d * (f * k - j * g) - b * (h * k - l * g) + c * (h * j - l * f)
    delta_y = a * (h * k - l * g) - d * (e * k - i * g) + c * (e * l - i * h)
    delta_z = a * (f * l - j * h) - b * (e * l - i * h) + d * (e * j - i * f)

    st.markdown("---")
    st.subheader("📋 Procedimiento Paso a Paso:")

    st.write("### 1. Determinante del Sistema (Δs)")
    st.write(
        f"Δs = {a}({f}×{k} - {j}×{g}) - {b}({e}×{k} - {i}×{g}) +"
        f" {c}({e}×{j} - {i}×{f})"
    )
    st.write(f"**Δs = {delta_s}**")

    if delta_s != 0:
      st.write("### 2. Determinante de X (Δx)")
      st.write(
          f"Δx = {d}({f}×{k} - {j}×{g}) - {b}({h}×{k} - {l}×{g}) +"
          f" {c}({h}×{j} - {l}×{f})"
      )
      st.write(f"**Δx = {delta_x}**")

      st.write("### 3. Determinante de Y (Δy)")
      st.write(
          f"Δy = {a}({h}×{k} - {l}×{g}) - {d}({e}×{k} - {i}×{g}) +"
          f" {c}({e}×{l} - {i}×{h})"
      )
      st.write(f"**Δy = {delta_y}**")

      st.write("### 4. Determinante de Z (Δz)")
      st.write(
          f"Δz = {a}({f}×{l} - {j}×{h}) - {b}({e}×{l} - {i}×{h}) +"
          f" {d}({e}×{j} - {i}×{f})"
      )
      st.write(f"**Δz = {delta_z}**")

      x = delta_x / delta_s
      y = delta_y / delta_s
      z = delta_z / delta_s

      st.write("### 5. Valores finales")
      st.write(f"**X** = Δx / Δs = {delta_x} / {delta_s} = **{x}**")
      st.write(f"**Y** = Δy / Δs = {delta_y} / {delta_s} = **{y}**")
      st.write(f"**Z** = Δz / Δs = {delta_z} / {delta_s} = **{z}**")

      st.success(f"¡Solución completada! X = {x}, Y = {y}, Z = {z}")
    else:
      if delta_x == 0 and delta_y == 0 and delta_z == 0:
        st.warning("Como Δs = 0 y todos los Δ son 0, el sistema tiene soluciones infinitas.")
      else:
        st.error("Como Δs = 0, el sistema no tiene solución.")