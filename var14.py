import matplotlib.pyplot as plt
import streamlit as st

filename = "data.csv"

def show_web(sum_liave_m, sum_liave_f, sum_dead_m, sum_dead_f):

    st.image('Titanic.jpg')
    st.header('Данные пассажиров Титаника')
    st.write('Для просмотра числа родственников у выживших и погибших пассажиров, выберите пол пассажира')
    option = st.selectbox('Значение поля Sex:', ['Мужской', 'Женский'])
    if option == 'Мужской':
        data = {'тип': ['Родственников у выживших', 'Родственников у погибших'], 'данные': [sum_liave_m, sum_dead_m]}
    elif option == 'Женский':
        data = {'тип': ['Родственников у выживших', 'Родственников у погибших'], 'данные': [sum_liave_f, sum_dead_f]}

    st.table(data)

    fig = plt.figure(figsize=(10, 5))
    plt.bar(data['тип'], data['данные'])
    xlab = "Пол {}".format(option)
    plt.xlabel(xlab)
    plt.ylabel("Колличество родственников")
    plt.title("Колличество родственников у выживших и погибших пассажиров")
    st.pyplot(fig)

def get_data(fn):
    with open (fn) as file:
        lines = file.readlines()

    return lines[1:]

def work(lines):
    sum_liave_m = 0
    sum_liave_f = 0
    sum_dead_m = 0
    sum_dead_f = 0
    for line  in lines :
        #Пропускаем первую строку
          #Разбиваю на столбцы
        tmpR = line.strip().rsplit(",",8)
        tmp = line.strip().split(",",3)
        #print("tmp: {}".format(tmp[:3]))
        #print("tmpR: {}".format(tmpR[1:]))
        #Считаем выживших и погибших
        who = -1
        # if tmp[1].isdigit():
        if str(tmp[1]).strip().isdigit():
            who = int(tmp[1])
        # print("who: {}".format(who))
        # количество братьеев, сестер в т.ч. сводных
        SibSp = 0
        if str(tmpR[3]).strip().isdigit():
            SibSp = int(tmpR[3])

        # количество родителей и детей
        Parch = 0
        if str(tmpR[4]).strip().isdigit():
            Parch = int(tmpR[4])

        sex = tmpR[1]

        # print("who: {} SibSp: {} Prach: {} sex: {}".format(who,SibSp, Parch, sex))
        #if who.isdigit():
    #Суммируем родственников выживших и погибших
        if who == 0:
            if sex == 'male':
                sum_dead_m = sum_dead_m + SibSp + Parch
            elif sex == 'female':
                sum_dead_f = sum_dead_f + SibSp + Parch
        if who == 1:
            if sex == 'male':
                sum_liave_m = sum_liave_m + SibSp + Parch
            elif sex == 'female':
                sum_liave_f = sum_liave_f + SibSp + Parch

    return (sum_liave_m, sum_liave_f, sum_dead_m, sum_dead_f)

lines = get_data(filename)
# print(lines)

sum_liave_m, sum_liave_f, sum_dead_m, sum_dead_f = work(lines)

# print("Родственников у погибших: m {} - f {}".format(sum_dead_m,sum_dead_f))
# print("Родственников у выживших: m {} - f {}".format(sum_liave_m, sum_liave_f))

show_web(sum_liave_m, sum_liave_f, sum_dead_m, sum_dead_f)
