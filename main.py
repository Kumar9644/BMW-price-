from joblib import *

import streamlit as st
model_pred=load('bmw_sales_prediction.pkl')



def main():
    st.title('Welcome to the  BMW car sale ')
    st.image('bmw.jpg')
    model=['1 series','2 series','3 series','4 series',
           '5 series','6 series','7 series','8 series',
           'M2','M3','M4','M5','X1','X2','X3','X4','X5',
           'X6','X7','Z4','i8','i3']
    model_op=[i for i in range(24) if i!=12 and i!=20]

    model_series=st.selectbox('Enter Model',model_op,format_func=lambda x:model[x] if x<=11 else(model[x-1] if x>11 and x<=19 else model[x-2]))

    year=[i for i in range(1996,2021)]
    model_year=st.selectbox('Select model year',year,format_func=lambda x:x)

    trans=['Automatic','Mannual','Semi-Automatic']
    gen=[i for i in range(len(trans))]
    model_trans=st.selectbox('Select Transmission Type',gen,format_func=lambda x:trans[x])

    mil=st.text_input('Enter Mileage of your car')

    fuel=['Diesel','Electric','Hybrid','Other','Petrol']
    gen_1=[i for i in range(len(fuel))]
    fuel_type=st.selectbox('Select fuel type',gen_1,format_func=lambda x:fuel[x])

    distance=st.text_input('Enter Kms of your car')

    size=[0.6,1,1.5,1.6,1.9,2.0,2.2,2.5,2.8,3.0,3.2,4.0,4.4,5.0,6.6]
    engine_size=st.selectbox('Select Engine size',size)
    prediction=st.button('Predict')

    if prediction:
        array=[model_series,model_year,model_trans,mil,fuel_type,distance,engine_size]
        data=[float(i) for i in array]
        pred=model_pred.predict([data])
        st.success('The price of your car will be {}'.format(pred[0]))








if __name__ == '__main__':
    main()