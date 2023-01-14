import streamlit as st
import sys
from streamlit_option_menu import option_menu

# Navigasi sidebar
with st.sidebar :
    selected = option_menu('KONVERSI SUHU',
    ['Konversi Suhu CELCIUS',
    'Konversi Suhu FAHRENHEIT',
    'Konversi Suhu KELVIN',
    'Konversi Suhu REAMUR'],
    default_index=0)

#Konversi Suhu CELCIUS
if (selected == 'Konversi Suhu CELCIUS') :
    st.title('Konversi Suhu CELCIUS')

    temp = st.number_input ("Masukkan Nilai Suhu dalam Celcius", 0)

    to_unit = st.radio(
        "Masukkan satuan suhu tujuan",
        ('Kelvin', 'Fahrenheit', 'Reamur'))

    def hasil(temp, to_unit):
        if to_unit in ('Kelvin'):
            return temp + 273.15
        elif to_unit in ('Fahrenheit'):
            return (temp*9/5)+32
        elif to_unit in ('Reamur'):
            return (temp *4/5)
        else:
            return temp    

    hitung = st.button ("HASIL")

    if hitung :
        converted_temp = (hasil(temp, to_unit))
        st.write ("Hasil Konversi anda = ", converted_temp)
        st.success (f"Hasil Konversi anda = {converted_temp}")


#Konversi Suhu FAHRENHEIT
if (selected == 'Konversi Suhu FAHRENHEIT') :
    st.title('Konversi Suhu FAHRENHEIT')

    temp = st.number_input ("Masukkan Nilai Suhu dalam Fahrenheit", 0)

    to_unit = st.radio(
        "Masukkan satuan suhu tujuan",
        ('Kelvin', 'Celcius', 'Reamur'))

    def hasil(temp, to_unit):
        if to_unit in ('Kelvin'):
            return (temp + 459.67)*5/9
        elif to_unit in ('Celcius'):
            return (temp-32)*5/9
        elif to_unit in ('Reamur'):
            return 4/9*(temp-32)
        else:
            return temp    

    hitung = st.button ("HASIL")

    if hitung :
        converted_temp = (hasil(temp, to_unit))
        st.write ("Hasil Konversi anda = ", converted_temp)
        st.success (f"Hasil Konversi anda = {converted_temp}")


#Konversi Suhu KELVIN
if (selected == 'Konversi Suhu KELVIN') :
    st.title('Konversi Suhu KELVIN')

    temp = st.number_input ("Masukkan Nilai Suhu dalam Kelvin", 0)

    to_unit = st.radio(
        "Masukkan satuan suhu tujuan",
        ('Celcius', 'Fahrenheit', 'Reamur'))

    def hasil(temp, to_unit):
        if to_unit in ('Celcius'):
            return temp - 273
        elif to_unit in ('Fahrenheit'):
            return (temp*9/5)-459.67
        elif to_unit in ('Reamur'):
            return 4/5*(temp-273)
        else:
            return temp    

    hitung = st.button ("HASIL")

    if hitung :
        converted_temp = (hasil(temp, to_unit))
        st.write ("Hasil Konversi anda = ", converted_temp)
        st.success (f"Hasil Konversi anda = {converted_temp}")


#Konversi Suhu REAMUR
if (selected == 'Konversi Suhu REAMUR') :
    st.title('Konversi Suhu REAMUR')

    temp = st.number_input ("Masukkan Nilai Suhu dalam Reamur", 0)

    to_unit = st.radio(
        "Masukkan satuan suhu tujuan",
        ('Kelvin', 'Fahrenheit', 'Celcius'))

    def hasil(temp, to_unit):
        if to_unit in ('Kelvin'):
            return (temp / 0.8) + 273.15
        elif to_unit in ('Fahrenheit'):
            return (temp*2.25)+32
        elif to_unit in ('Celcius'):
            return temp / 0.8
        else:
            return temp    

    hitung = st.button ("HASIL")

    if hitung :
        converted_temp = (hasil(temp, to_unit))
        st.write ("Hasil Konversi anda = ", converted_temp)
        st.success (f"Hasil Konversi anda = {converted_temp}")
