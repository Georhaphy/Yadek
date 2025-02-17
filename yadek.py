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
st.markdown("<h1 style='text-align: center; color: black ; font-size: 19px ;'><em>Good precision Good using</em></h1>", unsafe_allow_html=True)


listofmed = ['Amoxycillin','Augmentin','Augmentin 457','Azithromycin','Buscopan','Dicloxacilin','Erythromycin','Paracetamol','Salbutamol']



def check_int(a) :
    if int(a) == float(a):
        return int(a)
    else:
        return f'{a:.1f}'
    
    
    
    
col1, col2, col3, col4  = st.columns([1,1,1,1])

with col1:
    age = st.text_input("อายุ(ปี)", key='age',value= None) 


with col2:
    kg = st.text_input("น้ำหนัก(kg)", value= None , key='kg' )   
    

with col3:
    med = st.selectbox("ชื่อยา",(listofmed),index=0, key ='med')
    
with col4:
    blank = st.write("")
    blank1 = st.write("")
    but = st.button("คำนวณ", key='calculate')
    
    
    
if but:
    if med == 'Amoxycillin':
        st.code(f'{check_int(float(kg)*1)} cc po bid pc (125mg/5ml)')
        st.code(f'{check_int(float(kg)*0.5)} cc po bid pc (250mg/5ml)')
    
    elif med == 'Paracetamol':
        st.code(f'{check_int(float(kg)*0.416)} cc-{check_int(float(kg)*0.625)} cc po q 4-6 hr (120mg/5ml)')
        
    elif med == 'Augmentin':
        st.code(f'{check_int(float(kg)*0.625)} cc po bid pc (228.5mg/5ml)')
        
    elif med == 'Augmentin 457':
        st.code(f'{check_int(float(kg)*0.3125)} cc po bid pc (457mg/5ml)')
        
    elif med == 'Dicloxacilin':
        st.code(f'{check_int(float(kg)*0.25)} cc-{check_int(float(kg)*0.5)} cc po q 6 hr (62.5mg/5ml)')
    
    elif med == 'Erythromycin':
        st.code(f'{check_int(float(kg)*0.4)} cc-{check_int(float(kg)*0.67)} cc po tid pc (125mg/5ml)')
    
    elif med == 'Buscopan':
        if float(age) < 1:
            st.code('5 cc po tid pc (5mg/5ml)')
        elif float(age) <=6 :
            st.code('5-10 cc po tid pc (5mg/5ml)')
        else:
            st.code('10-20 cc po tid pc (5mg/5ml)')
            
    elif med == 'Salbutamol':
        if float(age) < 6:
            st.code(f'{check_int(float(kg)*0.25)} cc-{check_int(float(kg)*0.5)} cc po tid pc (2mg/5ml)')
        else:
            st.code('5 cc po tid pc (2mg/5ml)')
            
    elif med == 'Azithromycin':
        st.code(f'{check_int(float(kg)*0.25)} cc po OD (200mg/5ml)')