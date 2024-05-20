# Это работа по «Программной инженерии»
# Группы: 2023-ФГиИБ-ПИ-1см
# Практическое занятие №11. Групповая работа
# Студентов:
# 1. Леушкин Виталий Владимирович
#       Вариант 7: "Найти средний возраст пассажиров по каждому классу обслуживания (поле Pclass,
#       указав количество братьев, сестер... (столбец SibSp): [0, …, 8]."
# 2.
#

import streamlit as st
#from var7 import var7_main
from var14 import var14_main
#from varx3 import varx2_main
#from varx4 import varx3_main
#from varx5 import varx4_main

st.header('Практическое занятие №11')
# выводим картинку
st.image('Titanic.jpg')
# выводим текст заголоака

st.header('Работа группы №3')
variants = ['Вариант 7', 'Вариант 14', 'Вариант x2', 'Вариант x3', 'Вариант x4']

chois = st.selectbox('Выберите вариант работы', ['выберите вариант']+variants)
st.text('')

if chois == 'выберите вариант':
    st.info(f'Выберите вариант из выпадающего списка!')
elif chois == variants[0]:
    st.info(f'Представлен {chois}')
#    var7_main()
elif chois == variants[4]:
   var14_main()
#elif chois == variants[2]:
#    varx3_main()
#elif chois == variants[3]:
#    varx4_main()
#elif chois == variants[4]:
#    varx5_main()
else:
    st.error(f'Вариант \"{chois}\" пока не реализован, выберите лругой вариант из выпадающего списка!')