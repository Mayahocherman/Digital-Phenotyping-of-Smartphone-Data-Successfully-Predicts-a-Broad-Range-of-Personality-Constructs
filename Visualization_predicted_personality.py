import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df_bar = pd.read_excel('ML_output\mean_r_theory.xlsx', header=[0])
print(df_bar)

def col(row):
    if row.r >= 0.4:
        return 'limegreen'
    elif row.r >= 0.34 and row.r < 0.4:  # predicting personality from digital footprints r=0.34
        return 'lightgreen'
    elif row.r >= 0.2 and row.r < 0.34:
        return 'wheat'
    else:
        return 'salmon'

# function to add value labels
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')

df_bar['col'] = df_bar.apply(lambda row: col(row), axis=1)
df_bar['r']= df_bar['r'].round(decimals = 2)
#df_bar['R']= df_bar['r']
courses = df_bar['Personality Theory']
values = df_bar['r']
col=df_bar['col'].tolist()
print(df_bar)


fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(courses, values, color=col,
        width=0.4)

addlabels(courses,values)
plt.xlabel("Personality Construct", fontsize=14)
plt.ylabel("Average Pearson Correlation", fontsize=14)
#plt.title("Predicted Personality Theories")
plt.xticks(fontsize=12, rotation=90)
plt.show()

#Assistance function to create row colors (used in table_chart)
import pandas as pd
Fisher= ['Explorer Rank','Builder Rank','Director Rank','Negotiator Rank']
Big5 = ['Agreebleness','Concientiousness','Extraversion','Neurotism','Openess']
Attachment=['Secure attachment','Anxious attachment','Fearful-avoidant attachment','Dismissive-avoidant attachment']
Dark_Triad =['Dark Triad Compounded','Machiavellianism','Narcissism','Psychopathy']
STQ=['Risk Seeking','Physical Endurance','Physical Tempo','Social Endurance','Social Tempo','Empathy','Intellectual Endurance','Plasticity','Probab thinking',
     'Self-confidence','Impulsivity','Neuroticism-STQ','Social desirability tendency']
PVQ=['Self-direction Thought','Self-direction Action','Stimulation','Hedonism','Achievement','Power Dominance','Power Resources','Face','Security Societal','Security Personal','Tradition',
     'Conformity Rules','Conformity Interpersonal','Humility','Universalism Nature','Universalism Concern','Universalism Tolerance','Benevolence Care','Benevolence Dependability']

def row_style(row):
    if row.r >= 0.4:
        return pd.Series('background-color: limegreen', row.index)
    elif row.r >= 0.34 and row.r < 0.4:  # predicting personality from digital footprints r=0.34
        return pd.Series('background-color: lightgreen', row.index)
    elif row.r >= 0.2 and row.r < 0.34:
        return pd.Series('background-color: lightyellow', row.index)
    else:
        return pd.Series('background-color: salmon', row.index)

def Theory_trait(row):
    if row['Trait'] in Fisher:
        return 'Fisher Theory'
    if row['Trait'] in Big5:
        return 'Big Five Theory'
    if row['Trait'] in Big5:
        return 'Attachment Theory'
    if row['Trait'] in Dark_Triad:
        return 'Dark Triad'
    if row['Trait'] in PVQ:
        return 'PVQ'
    if row['Trait'] in STQ:
        return 'STQ'
    return row['Trait']

def table_chart(df):
    df = df.T.reset_index()
    df.columns = df.iloc[0]
    df = df[1:].rename(columns={'Unnamed: 0': 'Trait'})
    df["Decision_Tree"] = pd.to_numeric(df["Decision_Tree"], downcast="float")
    df["Random_Forest"] = pd.to_numeric(df["Random_Forest"], downcast="float")
    df["Gradient_Boosted_Trees"] = pd.to_numeric(df["Gradient_Boosted_Trees"], downcast="float")
    df["Support_Vector_Machine"] = pd.to_numeric(df["Support_Vector_Machine"], downcast="float")
    df['Personality Theory'] = df.apply(lambda row: Theory_trait(row), axis=1)
    Predicted = df.set_index('Trait')
    df_str = Predicted.loc[:, ["Personality Theory"]]
    Predicted= Predicted.drop(['Personality Theory'], axis=1)
    Predicted['Best predicted Model'] = Predicted.idxmax(axis=1)
    # Predicted['Pearson Correlation (r) value'] = Predicted.max(axis = 1)
    Predicted['r'] = Predicted.max(axis=1)
    #Predicted=Predicted.concat(df_str)
    Predicted=pd.concat([Predicted, df_str], axis=1)
    print(Predicted)
    Predicted_sorted = Predicted.drop(
        ['Decision_Tree', 'Random_Forest', 'Gradient_Boosted_Trees', 'Support_Vector_Machine'], axis=1).sort_values(
        by=['r'], ascending=False).reset_index()
    Predicted = Predicted.drop(['Decision_Tree', 'Random_Forest', 'Gradient_Boosted_Trees', 'Support_Vector_Machine'],
                               axis=1).reset_index()

    Predicted_sorted = Predicted_sorted.style.apply(row_style, axis=1)
    Predicted = Predicted.style.apply(row_style, axis=1)

    return Predicted_sorted, Predicted

df_table_chart = pd.read_csv('ML_output\pearson_corr_all_traits.csv', header=[0])
Predicted_sorted, Predicted = table_chart(df_table_chart)
Predicted_sorted.to_excel("ML_output\Best_model_results_with_colors_sort_by_r.xlsx")
Predicted.to_excel("ML_output\Best_model_results_with_colors_sort_by_trait.xlsx")