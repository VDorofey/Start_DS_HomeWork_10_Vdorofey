import pandas as pd
import streamlit as st
from PIL import Image

def process_main_page():
    show_main_page()
    process_side_bar_inputs()

def show_main_page():
    image = Image.open('logo.jpg')

    st.set_page_config(
        layout="wide",
        initial_sidebar_state="auto",
        page_title="Indian Patient",
        page_icon=image,
    )

    st.write(
        """
        # Определение наличия заболеваний печени у индийского пациента
        Определяем тех, кто страдает от заболевания печени, а кто - нет
        """
    )

    st.image(image)


df = pd.read_csv("indian_liver_patient_train.csv")
df = df[["Age", "Gender", "Total_Bilirubin", "Direct_Bilirubin", "Alkaline_Phosphotase", "Alamine_Aminotransferase", "Aspartate_Aminotransferase", "Total_Protiens", "Albumin", "Albumin_and_Globulin_Ratio"]]
Age_min = df.Age.min()
Age_max = df.Age.max()

Total_Bilirubin_min = df.Total_Bilirubin.min()
Total_Bilirubin_max = df.Total_Bilirubin.max()

Direct_Bilirubin_min = df.Direct_Bilirubin.min()
Direct_Bilirubin_max = df.Direct_Bilirubin.max()

Alkaline_Phosphotase_min = df.Alkaline_Phosphotase.min()
Alkaline_Phosphotase_max = df.Alkaline_Phosphotase.max()

Alamine_Aminotransferase_min = df.Alamine_Aminotransferase.min()
Alamine_Aminotransferase_max = df.Alamine_Aminotransferase.max()

Aspartate_Aminotransferase_min = df.Aspartate_Aminotransferase.min()
Aspartate_Aminotransferase_max = df.Aspartate_Aminotransferase.max()

Total_Protiens_min = df.Total_Protiens.min()
Total_Protiens_max = df.Total_Protiens.max()

Albumin_min = df.Albumin.min()
Albumin_max = df.Albumin.max()

Albumin_and_Globulin_Ratio_min = df.Albumin_and_Globulin_Ratio.min()
Albumin_and_Globulin_Ratio_max = df.Albumin_and_Globulin_Ratio.max()


def process_side_bar_inputs():
    st.sidebar.header('Данные пациента')
    user_input_df = sidebar_input_features()

    
def sidebar_input_features():
    Gender = st.sidebar.selectbox("Пол", ("Мужской", "Женский"))
   
    Age = st.sidebar.slider("Возраст", min_value=Age_min, max_value=Age_max, value=Age_min + 20, step=1)

    Total_Bilirubin = st.sidebar.slider("Общий билирубин",
        min_value=Total_Bilirubin_min, max_value=Total_Bilirubin_max, value=Total_Bilirubin_min + 1.0, step=0.1)

    Direct_Bilirubin = st.sidebar.slider("Прямой билирубин",
        min_value=Direct_Bilirubin_min, max_value=Direct_Bilirubin_max, value=Direct_Bilirubin_min + 0.5, step=0.1)

    Alkaline_Phosphotase = st.sidebar.slider("Щелочная фосфотаза",
        min_value=Alkaline_Phosphotase_min, max_value=Alkaline_Phosphotase_max, value=Alkaline_Phosphotase_min + 70, step=1)

    Alamine_Aminotransferase = st.sidebar.slider("АЛТ",
        min_value=Alamine_Aminotransferase_min, max_value=Alamine_Aminotransferase_max, value=Alamine_Aminotransferase_min + 20, step=1)
    
    Aspartate_Aminotransferase = st.sidebar.slider("АСТ",
        min_value=Aspartate_Aminotransferase_min, max_value=Aspartate_Aminotransferase_max, value=Aspartate_Aminotransferase_min + 20, step=1)


    Total_Protiens = st.sidebar.slider("Общий белок",
        min_value=Total_Protiens_min, max_value=Total_Protiens_max, value=Total_Protiens_min + 3.0, step=0.1)

    Albumin = st.sidebar.slider(
        "Альбумин",
        min_value=Albumin_min, max_value=Albumin_max, value=Albumin_min + 1.0, step=0.1)

    Albumin_and_Globulin_Ratio = st.sidebar.slider(
        "Соотношение Альбумин/Глобулин",
        min_value=Albumin_and_Globulin_Ratio_min, max_value=Albumin_and_Globulin_Ratio_max, value=Albumin_and_Globulin_Ratio_min + 0.5, step=0.1)

    translatetion = {
        "Мужской": "Муж",
        "Женский": "Жен",
         }

    data = {
        "Возраст": Age,
        "Пол": translatetion[Gender],
        "Общ.билирубин": Total_Bilirubin,
        "Прямой билирубин": Direct_Bilirubin,
        "Щелочн.фосфотаза": Alkaline_Phosphotase,
        "АЛТ": Alamine_Aminotransferase,
        "АСТ": Aspartate_Aminotransferase,
        "Общ.белок": Total_Protiens,
        "Альбумин": Albumin,
        "Альбумин/Глобулин": Albumin_and_Globulin_Ratio,
    }

    df = pd.DataFrame(data, index=[0])
    st.dataframe(df)

    st.write("# Заключение врача:")
    if (Age >= 50) or (Total_Bilirubin > 45) or (Direct_Bilirubin > 10) or (Alkaline_Phosphotase > 1000) or (Alamine_Aminotransferase >1000) or   (Aspartate_Aminotransferase > 1000) or (Total_Protiens > 5.8) or (Albumin > 2.75) or (Albumin_and_Globulin_Ratio > 1.4):
        st.write("Пациент скорее болен, чем здоров")
    else:
        st.write("Пациент скорее здоров, чем болен")

    return df

if __name__ == "__main__":
    process_main_page()
