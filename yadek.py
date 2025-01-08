# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 09:23:35 2025

@author: user
"""

import streamlit as st 
import math
from datetime import  date, datetime
from dateutil.relativedelta import relativedelta

background_image = """
<style>
[data-testid="stAppViewContainer"]  {
    background-image: url("https://img5.pic.in.th/file/secure-sv1/smsk-1e26f337bb6ec6813.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)



st.markdown("<h1 style='text-align: center; color: black ; font-size: 40px ;'>Sakhon Yadek</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: black ; font-size: 19px ;'><em>Good precise Good using</em></h1>", unsafe_allow_html=True)


listofmed = ['Amoxycillin','Augmentin','Dicloxacilin','Paracetamol']


col1, col2, col3, col4, col5, col6, col7, col8   = st.columns([0.5,1,0.5,1,1,0.5,2,2])

with col1:
    yr = st.write("อายุ")
    
with col2:
    age = st.text_input("อายุ(ปี)", key='age',value= None, label_visibility= "collapsed") 

with col3:
    yr1 = st.write("ปี")
    
with col4:
    bw = st.write("น้ำหนัก")
    
with col5:
    kg = st.text_input("น้ำหนัก(kg)", value= None , key='kg' ,label_visibility= "collapsed")   
    
with col6:
    bw1 = st.write("กิโล")
    
with col7:
    med = st.selectbox("ชื่อยา",(listofmed),index=0, key ='med')
    
with col8:
    but = st.button("คำนวณ", key='calculate')
    
    
    
if but:
    if med == 'Amoxycillin':
        print('ok')
