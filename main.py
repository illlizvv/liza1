import pandas as pd
import openpyxl
df=pd.read_excel("lab_pi_101.xlsx")
count_mark=len(df)

group=input("Введите группу, по которой необходимо вывести информацию: ")

count_mark_gr=len(df[df['Группа']==group])
count_mark_group=df.loc[df['Группа']==group, 'Личный номер студента'].nunique()
count_id=df.loc[df['Группа']==group, 'Личный номер студента'].unique()
id_group=", ".join(map(str, count_id))
form_contr=df.loc[df['Группа']==group, 'Уровень контроля'].unique()
forms=", ".join(form_contr)
years=df.loc[df['Группа']==group, 'Год'].unique()
year=", ".join(map(str, years))

print("В исходном датасете содержалось {count_mark} оценок, из них {count_mark_gr} оценок относятся к группе {group}"
"\nВ датасете находятся оценки {count_mark_group} студентов со следующими личными номерами:  {id_group}"
"\nИспользуемые формы контроля: {forms}"
"\nДанные представлены по следующим учебным годам: {year}")


