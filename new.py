import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesRegressor
import pickle 

loaded_model = pickle.load(open('C:/Users/ramsa/Downloads/Data analysis assignments/flipkart/trained_model.sav', 'rb'))

st.title('Laptop Price Estimator')
Brand = st.selectbox('Select the Brand', ('select','Lenovo', 'ASUS', 'Redmi', 'APPLE', 'HP', 'Infinix', 'SAMSUNG', 'acer', 'MSI', 'DELL', 'realme', 'GIGABYTE', 'Mi', 'ALIENWARE'))
st.write('You selected:', Brand)
Processor = st.selectbox('Select the Processor', ('select','Celeron Dual', 'Core i5', 'Core i3', 'Ryzen 5 Hexa', 'M1', 'Athlon Dual', 'Ryzen 7 Octa', 'Ryzen 5 Quad', 'Ryzen 3 Quad', 'M2', 'Core i9', 'Core i7', 'Ryzen 3 Dual', 'AMD Dual', 'Ryzen 9 Octa', 'Pentium', 'Celeron Quad', 'Ryzen 5 Dual'))
st.write('You selected:', Processor)
RAM = st.selectbox('Select RAM (in GB)', ('select','8 GB', '4 GB', '16 GB', '32 GB'))
st.write('You selected:', RAM)
Storage = st.selectbox('Select the Storage', ('select','256 GB SSD', '512 GB SSD', '1 TB SSD', '2 TB SSD', '128 GB SSD', '4 TB SSD', '1TB + 256GB SSD'))
st.write('You selected:', Storage)
Warranty = st.selectbox('Select the Warranty', ('select','2 Year Warranty', '1 Year Warranty', '1 Year Premium', '1 Year International', '2 Year Carry', '3 Years Onsite', '3 Year Premium'))
st.write('You selected:', Warranty)
# Brand encoding    
if Brand == "Lenovo":
        Brand = 7 
elif Brand == "ASUS":
        Brand = 2
elif Brand == "Redmi":
        Brand = 10
elif Brand == "APPLE":
        Brand = 1
elif Brand == "HP":
        Brand = 5
elif Brand == "Infinix":
        Brand = 6
elif Brand == "SAMSUNG":
        Brand = 11
elif Brand == "acer":
        Brand = 12
elif Brand == "MSI":
        Brand = 8
elif Brand == "DELL":
        Brand = 3
elif Brand == "realme":
        Brand = 13
elif Brand == "GIGABYTE":
        Brand = 4
elif Brand == "Mi":
        Brand = 9
elif Brand == "ALIENWARE":
        Brand = 0     
    
    # Processor encoding
if Processor == "Celeron Dual":
        Processor = 2
elif Processor == "Core i5":
        Processor = 5
elif Processor == "Core i3":
        Processor = 4 
elif Processor == "Ryzen 5 Hexa":
        Processor = 14
elif Processor == "M1":
        Processor = 8
elif Processor == "Athlon Dual":
        Processor = 1
elif Processor == "Ryzen 7 Octa":
        Processor = 17
elif Processor == "Ryzen 5 Quad":
        Processor = 15
elif Processor == "Ryzen 3 Quad":
        Processor = 12
elif Processor == "M2":
        Processor = 9
elif Processor == "Core i9":
        Processor = 7 
elif Processor == "Core i7":
        Processor = 6
elif Processor == "Ryzen 3 Dual":
        Processor = 11
elif Processor == "AMD Dual":
        Processor = 0 
elif Processor == "Ryzen 9 Octa":
        Processor = 18
elif Processor == "Pentium":
        Processor = 10
elif Processor == "Celeron Quad":
        Processor = 3
elif Processor == "Ryzen 5 Dual":
        Processor = 13
elif Processor == "Ryzen 7 Hexa":
        Processor = 16 

    # RAM encoding
if RAM == "8 GB":
        RAM = 3
elif RAM == "4 GB":
        RAM = 2
elif RAM == "16 GB":
        RAM = 0
elif RAM == "32 GB":
        RAM = 1
      
     #Storage
if Storage == "256 GB SSD":
       Storage = 4
elif Storage == "512 GB SSD":
       Storage =6
elif Storage == "1 TB SSD":
       Storage = 0
elif Storage == "2 TB SSD":
       Storage = 3
elif Storage == "128 GB SSD":
       Storage = 1
elif Storage == "4 TB SSD":
       Storage = 5
elif Storage == "1TB + 256GB SSD":
       Storage =2

       

  #Warranty encoding
if Warranty == "2 Year Warranty":
        Warranty = 4
elif Warranty == "1 Year Warranty":
        Warranty =2
elif Warranty == "1 Year Premium":
        Warranty = 1
elif Warranty == "1 Year International":
        Warranty = 0
elif Warranty == "2 Year Carry":
        Warranty =3
elif Warranty == "3 Years Onsite":
        Warranty = 6
elif Warranty == "3 Year Premium":
        Warranty =5


def predict():
        input_data =(Brand,Processor,RAM,Storage,Warranty)
#converting input data to numpy array       
        input_data_as_numpy_array = np.asarray(input_data)
#reshaping
        input_reshape = input_data_as_numpy_array.reshape(1,-1)
        prediction =loaded_model.predict(input_reshape)
        return prediction[0]
if st.button('predict'):
    prediction = predict()
    st.success('Your estimated laptop price: {}'.format(prediction))

    