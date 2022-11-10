import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import seaborn as sns

# ----------------------------------------------------------------------
# ------------ functions to create and support charts  -----------------
# ----------------------------------------------------------------------

#create chart to compare ML models results for the different set of trait
def model_comparing_chart(df,title,ylabel):

    df = df.T.reset_index()
    df.columns = df.iloc[0]
    df=df[1:].rename(columns={'Unnamed: 0':'trait'})
    x = df.loc[:, ['Decision_Tree']]
    x2 = df.loc[:, ['Random_Forest']]
    x3 = df.loc[:, ['Gradient_Boosted_Trees']]
    x4 = df.loc[:, ['Support_Vector_Machine']]
    df['colors_DT'] = ['red' if x < 0.2 else 'yellowgreen' for x in df['Decision_Tree']]
    df['colors_RF'] = ['red' if x < 0.2 else 'yellowgreen' for x in df['Random_Forest']]
    df['colors_GBT'] = ['red' if x < 0.2 else 'yellowgreen' for x in df['Gradient_Boosted_Trees']]
    df['colors_SVM'] = ['red' if x < 0.2 else 'yellowgreen' for x in df['Support_Vector_Machine']]

    # Draw plot
    plt.figure(figsize=(12,24))
    plt.scatter(df.Decision_Tree, df.index, s=850, alpha=.6, color=df.colors_DT,  label='Decision Tree')
    plt.scatter(df.Random_Forest, df.index, s=850, alpha=.6, color=df.colors_RF, marker="^", label='Random Forest')
    plt.scatter(df.Gradient_Boosted_Trees, df.index, s=850, alpha=.6, color=df.colors_GBT, marker="s", label='Gradient Boosted Trees')
    plt.scatter(df.Support_Vector_Machine, df.index, s=850, alpha=.6, color=df.colors_SVM, marker="d", label='Support Vector Machine')
    for x, y, tex in zip(df.Decision_Tree, df.index, df.Decision_Tree):
        t = plt.text(x, y, round(tex, 2), horizontalalignment='center',
                     verticalalignment='center', fontdict={'color':'black'})
    for x2, y, tex in zip(df.Random_Forest, df.index, df.Random_Forest):
        t = plt.text(x2, y, round(tex, 2), horizontalalignment='center',
                     verticalalignment='center', fontdict={'color': 'black'})
    for x3, y, tex in zip(df.Gradient_Boosted_Trees, df.index, df.Gradient_Boosted_Trees):
        t = plt.text(x3, y, round(tex, 2), horizontalalignment='center',
                     verticalalignment='center', fontdict={'color': 'black'})
    for x4, y, tex in zip(df.Support_Vector_Machine, df.index, df.Support_Vector_Machine):
        t = plt.text(x4, y, round(tex, 1), horizontalalignment='center',
                     verticalalignment='center', fontdict={'color': 'black'})

    legend_elements = [Line2D([0], [0], color='w', marker='o', label='Decision Tree', markerfacecolor='w', markeredgecolor='k', markersize=17),
                       Line2D([0], [0],color='w',marker="^", label='Random Forest', markerfacecolor='w', markeredgecolor='k', markersize=17),
                       Line2D([0], [0],color='w',marker="s", label='Gradient Boosted Trees',markerfacecolor='w', markeredgecolor='k', markersize=17),
                       Line2D([0], [0],color='w',marker="d", label='Support Vector Machine', markerfacecolor='w', markeredgecolor='k', markersize=17)
                       ]
    plt.legend(handles=legend_elements, loc='best', borderpad=2.5,  labelspacing = 1.5, fontsize=16)

    # Decorations
    # Lighten borders
    plt.gca().spines["top"].set_alpha(.3)
    plt.gca().spines["bottom"].set_alpha(.3)
    plt.gca().spines["right"].set_alpha(.3)
    plt.gca().spines["left"].set_alpha(.3)

    plt.yticks(df.index, df.trait, fontsize=16)
    plt.title(title, fontdict={'size':25})
    plt.xlabel('Pearson Correlation (r)', fontsize=20)
    plt.ylabel(ylabel, fontsize=20)
    plt.grid(linestyle='--', alpha=0.5)
    plt.xlim(0, 0.7)

    #Check for Predicted successfully traits
    Predicted_successfully_DT=df.loc[df['colors_DT'] == 'yellowgreen'].reset_index()
    Predicted_successfully_DT=Predicted_successfully_DT['trait'].tolist()
    # Count the number of successfully Predicted  traits to display on the chart
    DT_str = 'Number of Decision Tree model predictions above 0.2: ' + str(len(Predicted_successfully_DT))

    Predicted_successfully_RF=df.loc[df['colors_RF'] == 'yellowgreen'].reset_index()
    Predicted_successfully_RF=Predicted_successfully_RF['trait'].tolist()
    # Count the number of successfully Predicted  traits to display on the chart
    RF_str = 'Number of Random Forest model predictions above 0.2: ' + str(len(Predicted_successfully_RF))

    Predicted_successfully_GBT=df.loc[df['colors_GBT'] == 'yellowgreen'].reset_index()
    Predicted_successfully_GBT=Predicted_successfully_GBT['trait'].tolist()
    # Count the number of successfully Predicted  traits to display on the chart)
    GBT_str = 'Number of Gradient Boosted Trees model predictions above 0.2: ' + str(len(Predicted_successfully_GBT))

    Predicted_successfully_SVM=df.loc[df['colors_SVM'] == 'yellowgreen'].reset_index()
    Predicted_successfully_SVM=Predicted_successfully_SVM['trait'].tolist()
    # Count the number of successfully Predicted  traits to display on the chart
    svm_str = 'Number of Support Vector Machine model predictions above 0.2: ' + str(len(Predicted_successfully_SVM))


    #plt.figtext(0.5, 0.01,DT_str+"\n"+ RF_str+"\n"+GBT_str+"\n"+svm_str, ha="center", fontsize=13,
    #            bbox={"facecolor": "White", "alpha": 0.5, "pad": 5})

    plt.show()

    return Predicted_successfully_DT, Predicted_successfully_RF , Predicted_successfully_GBT, Predicted_successfully_SVM
#Assistance function to define a category for the feature
def Feature_category(row):
    if row['feature'][:7] == 'Battery':
        return 'Battery'
    if row['feature'][:9] == 'Bluetooth':
        return 'Bluetooth'
    if row['feature'][:6] == 'Screen':
        return 'Screen'
    if row['feature'][:4] == 'Wifi':
        return 'WiFi'
    return 'Communication'
#Assistance function to create inner Pie chart colors (used in feature_importance_chart)
def pie_color(row):
    if row['feature'][:7] == 'Battery':
        return 'limegreen'
    if row['feature'][:9] == 'Bluetooth':
        return 'orange'
    if row['feature'][:6] == 'Screen':
        return 'royalblue'
    if row['feature'][:4] == 'Wifi':
        return 'red'
    return 'mediumorchid'
#Assistance function to create outer Pie chart colors (used in feature_importance_chart)
def pie_color_out(row):
    if row['Category'] == 'Battery':
        return 'limegreen'
    if row['Category'] == 'Bluetooth':
        return 'orange'
    if row['Category'] == 'Screen':
        return 'royalblue'
    if row['Category'] == 'WiFi':
        return 'red'
    return 'mediumorchid'
#create chart to visualize feature importance for the different ML model
def feature_importance_chart(df_features,title):
    # Inner Pie
    df_features['Category'] = df_features.apply(lambda row: Feature_category(row), axis=1)
    df_features['color'] = df_features.apply(lambda row: pie_color(row), axis=1)
    #print('df_features',df_features)
    labels = df_features['feature']
    sizes = df_features['count']

    # Outer Pie
    df_features_cat = df_features.groupby(["Category"])['count'].agg(["sum"]).reset_index()
    df_features_cat['color'] = df_features_cat.apply(lambda row: pie_color_out(row), axis=1)
    #print('df_features_cat', df_features_cat)
    labels2 = df_features_cat['Category']
    sizes2 = df_features_cat['sum']

    # Create The Pie Chart
    fig, ax = plt.subplots()
    size = 0.3
    outer_colors = df_features_cat['color']
    inner_colors = df_features['color']

    #ax.pie(sizes2, labels=labels2, radius=1, colors=outer_colors, autopct='%1.1f%%', textprops={'fontsize': 14}, pctdistance=0.85, wedgeprops=dict(width=size, edgecolor='w'))
    ax.pie(sizes2,  radius=1, colors=outer_colors, autopct='%1.1f%%', textprops={'fontsize': 18},
           pctdistance=0.85, wedgeprops=dict(width=size, edgecolor='w'))
    """ax.legend(labels2,
              title="Feature-set Category",
              loc="upper left",
              bbox_to_anchor=(1, 0, 0.6, 1),
              prop={'size': 20}
              )"""
    ax.pie(sizes, radius=1 - size, colors=inner_colors, wedgeprops=dict(width=size, edgecolor='w'))
    ax.set_title(title, fontsize=18)

    plt.show()
#create chart to visualize feature importance - with the feature as labels for the different ML model
def feature_importance_chart_details(df_features,title):
    # Inner Pie
    df_features['Category'] = df_features.apply(lambda row: Feature_category(row), axis=1)
    df_features['color'] = df_features.apply(lambda row: pie_color(row), axis=1)
    # print(df_features)
    labels = df_features['feature']
    sizes = df_features['count']

    # Outer Pie
    df_features_cat = df_features.groupby(["Category"])['count'].agg(["sum"]).reset_index()
    # print(df_features_cat)
    df_features_cat['color'] = df_features_cat.apply(lambda row: pie_color_out(row), axis=1)
    # print(df_features_cat)
    labels2 = df_features_cat['Category']
    sizes2 = df_features_cat['sum']

    # Create The Pie Chart
    fig, ax = plt.subplots()
    size = 0.4
    outer_colors = df_features_cat['color']
    inner_colors = df_features['color']

    ax.pie(sizes2, radius=1.1, colors=outer_colors, autopct='%1.1f%%', textprops={'fontsize': 14}, pctdistance=1.1, wedgeprops=dict(width=size, edgecolor='w'))
    ax.legend(labels2,
              title="Feature Category",
              loc="upper left",
              bbox_to_anchor=(1, 0, 0.6, 1))
    ax.pie(sizes, labels=labels, labeldistance=0.45, rotatelabels=0.7, radius=1.1 - size, colors=inner_colors, wedgeprops=dict(width=size, edgecolor='w'))
    ax.set_title(title, fontsize=18)

    #plt.show()
#Assistance function to create row colors (used in table_chart)
def row_style(row):
    if row.r >= 0.4:
        return pd.Series('background-color: limegreen', row.index)
    elif row.r >= 0.34 and row.r < 0.4:  # predicting personality from digital footprints r=0.34
        return pd.Series('background-color: lightgreen', row.index)
    elif row.r >= 0.2 and row.r < 0.34:
        return pd.Series('background-color: lightyellow', row.index)
    else:
        return pd.Series('background-color: salmon', row.index)
#Assistance function to define theory for each trait
def Theory_trait(row):
    Fisher = ['Explorer Rank', 'Builder Rank', 'Director Rank', 'Negotiator Rank']
    Big5 = ['Agreebleness', 'Concientiousness', 'Extraversion', 'Neurotism', 'Openess']
    Attachment = ['Secure attachment', 'Anxious attachment', 'Fearful-avoidant attachment',
                  'Dismissive-avoidant attachment']
    Dark_Triad = ['Dark Triad Compounded', 'Machiavellianism', 'Narcissism', 'Psychopathy']
    #Dark_Triad = ['Dark Triad Compounded']
    STQ = ['Risk Seeking', 'Physical Endurance', 'Physical Tempo', 'Social Endurance', 'Social Tempo', 'Empathy',
           'Intellectual Endurance', 'Plasticity', 'Probab thinking',
           'Self-confidence', 'Impulsivity', 'Neuroticism-STQ', 'Social desirability tendency']
    PVQ = ['Self-direction Thought', 'Self-direction Action', 'Stimulation', 'Hedonism', 'Achievement',
           'Power Dominance', 'Power Resources', 'Face', 'Security Societal', 'Security Personal', 'Tradition',
           'Conformity Rules', 'Conformity Interpersonal', 'Humility', 'Universalism Nature', 'Universalism Concern',
           'Universalism Tolerance', 'Benevolence Care', 'Benevolence Dependability']
    if row['Trait'] in Fisher:
        return 'Fisher Theory'
    if row['Trait'] in Big5:
        return 'Big Five Theory'
    if row['Trait'] in Attachment:
        return 'Attachment Theory'
    if row['Trait'] in Dark_Triad:
        return 'Dark Triad'
    if row['Trait'] in PVQ:
        return 'PVQ'
    if row['Trait'] in STQ:
        return 'STQ'
    return row['Trait']
#create table chart to show the succeeded prediction by traits
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
    Predicted_df=Predicted.copy()
    Predicted_sorted = Predicted.drop(
        ['Decision_Tree', 'Random_Forest', 'Gradient_Boosted_Trees', 'Support_Vector_Machine'], axis=1).sort_values(
        by=['r'], ascending=False).reset_index()
    Predicted = Predicted.drop(['Decision_Tree', 'Random_Forest', 'Gradient_Boosted_Trees', 'Support_Vector_Machine'],
                               axis=1).reset_index()

    Predicted_sorted = Predicted_sorted.style.apply(row_style, axis=1)
    Predicted = Predicted.style.apply(row_style, axis=1)

    return Predicted_sorted, Predicted, Predicted_df


# ----------------------------------------------------------------------
# ------------ Create Charts - for different data sets   ------------
# ----------------------------------------------------------------------
"""
# all traits
df_all=pd.read_csv('ML_output\pearson_corr_all_traits.csv', header=[0])
#title_all='Comparison of models predictions - predicting personality traits using Digital Phenotyping'
title_all=' '
ylabel_all='Personality trait'
Predicted_successfully_DT, Predicted_successfully_RF , Predicted_successfully_GBT, Predicted_successfully_SVM=model_comparing_chart(df_all,title_all,ylabel_all)
#("Num of traits: ", df_all.shape[1]-1)
df_all = df_all.drop(['Unnamed: 0'], axis=1).astype(float)
df_above_threshold=df_all[df_all > 0.2].count() #table with the number of models predicted the trait in threshold above 0.2
df_suc=df_above_threshold[df_above_threshold >0].count()
print("Number of traits succeed to predict: ", df_suc)

# PVQ traits
df_pvq=pd.read_csv('ML_output\pearson_corr_PVQ.csv', header=[0])
#title_PVQ='Comparison of models predictions - predicting PVQ personality traits using Digital Phenotyping'
title_PVQ=' '
ylabel_PVQ='Personality trait - PVQ Theory'
#Predicted_successfully_DT, Predicted_successfully_RF , Predicted_successfully_GBT, Predicted_successfully_SVM=model_comparing_chart(df_pvq,title_PVQ,ylabel_PVQ)

# STQ traits
df_STQ=pd.read_csv('ML_output\pearson_corr_STQ.csv', header=[0])
title_STQ='Comparison of models predictions - predicting STQ personality traits using Digital Phenotyping'
#title_STQ=' '
ylabel_STQ='Personality trait - STQ Theory'
#Predicted_successfully_DT, Predicted_successfully_RF , Predicted_successfully_GBT, Predicted_successfully_SVM=model_comparing_chart(df_STQ,title_STQ,ylabel_STQ)

# Main Personality traits - Big5, Fisher, Attachements
df_main=pd.read_csv('ML_output\pearson_corr_main.csv', header=[0])
title_main='Comparison of models predictions - predicting main personality theories traits using Digital Phenotyping'
#title_main=' '
ylabel_main='Personality trait'
#Predicted_successfully_DT, Predicted_successfully_RF , Predicted_successfully_GBT, Predicted_successfully_SVM=model_comparing_chart(df_main,title_main,ylabel_main)

# Additional Personality traits
df_Further=pd.read_csv('ML_output\pearson_corr_additional.csv', header=[0])
#title_Further='Comparison of models predictions - predicting additional personality theories traits using Digital Phenotyping'
title_Further=' '
ylabel_Further='Personality trait'
#Predicted_successfully_DT, Predicted_successfully_RF , Predicted_successfully_GBT, Predicted_successfully_SVM=model_comparing_chart(df_Further,title_Further,ylabel_Further)

"""

########### NHB visualization - EXCEL ORDER BY PERFORMANCE ###########
# STQ traits (Functional Ensemble of Temperament)
df_STQ=pd.read_csv('ML_output\pearson_corr_STQ_NHB.csv', header=[0])
title_STQ=' '
ylabel_STQ='Personality trait - Functional Ensemble of Temperament'
#Predicted_successfully_DT, Predicted_successfully_RF , Predicted_successfully_GBT, Predicted_successfully_SVM=model_comparing_chart(df_STQ,title_STQ,ylabel_STQ)

df_pvq=pd.read_csv('ML_output\pearson_corr_PVQ_NHB.csv', header=[0])
title_PVQ=' '
ylabel_PVQ='Personality trait - Theory of Basic Human Values'
#Predicted_successfully_DT, Predicted_successfully_RF , Predicted_successfully_GBT, Predicted_successfully_SVM=model_comparing_chart(df_pvq,title_PVQ,ylabel_PVQ)

# Additional Personality traits
df_Further=pd.read_csv('ML_output\pearson_corr_additional_NHB.csv', header=[0])
title_Further=' '
ylabel_Further='Personality trait'
#Predicted_successfully_DT, Predicted_successfully_RF , Predicted_successfully_GBT, Predicted_successfully_SVM=model_comparing_chart(df_Further,title_Further,ylabel_Further)


# Main Personality traits - Big5, Fisher, Attachements
df_main=pd.read_csv('ML_output\pearson_corr_main_NHB.csv', header=[0])
title_main=' '
ylabel_main='Personality trait'
Predicted_successfully_DT, Predicted_successfully_RF , Predicted_successfully_GBT, Predicted_successfully_SVM=model_comparing_chart(df_main,title_main,ylabel_main)

# ------------------------------------------------
# ------------ Feature Importance  ------------
# ------------------------------------------------

#To run the pie chart - please run "model_comparing_chart" on the last section only for 1 set of features.

########### NHB visualization - EXCEL ORDER BY PERFORMANCE ###########
df_all=pd.read_csv('ML_output\pearson_corr_all_traits.csv', header=[0])
title_all=' '
ylabel_all='Personality trait'
#Predicted_successfully_DT, Predicted_successfully_RF , Predicted_successfully_GBT, Predicted_successfully_SVM=model_comparing_chart(df_all,title_all,ylabel_all)

import os

Decision_Tree= {}
Random_Forest= {}
Gradient_Boosted_Trees= {}
Support_Vector_Machine={}

# print output from the model_comparing_chart - list of predicted successfully (r above 0.20) traits
print('Predicted_successfully_DT: ',Predicted_successfully_DT)
print('Predicted_successfully_DT num of traits: ',len(Predicted_successfully_DT))
print('Predicted_successfully_RF: ',Predicted_successfully_RF)
print('Predicted_successfully_RF num of traits: ',len(Predicted_successfully_RF))
print('Predicted_successfully_GB: ',Predicted_successfully_GBT)
print('Predicted_successfully_GB num of traits: ',len(Predicted_successfully_GBT))
print('Predicted_successfully_SVM: ',Predicted_successfully_SVM)
print('Predicted_successfully_SVM num of traits: ',len(Predicted_successfully_SVM))

# Open feature importance files and take only top five predictors for predicted successfully (r above 0.20) traits
Directory="ML_output\Feature Importance"
for filename in os.listdir('ML_output\Feature Importance'):
    # Random Forest Feature Importance
    if filename.endswith('RF.xlsx'):
        if filename[:-8] in Predicted_successfully_RF:
            path = Directory+'\\'+filename
            df_RF = pd.read_excel(path)
            #take only 5 features importance
            main_5_RF_features=df_RF.head(5)
            lst=main_5_RF_features['Attribute'].tolist()
            Random_Forest[filename]=lst
    # Decision Tree Feature Importance
    if filename.endswith('DT.xlsx'):
        if filename[:-8] in Predicted_successfully_DT:
            path = Directory + '\\' + filename
            df_DT = pd.read_excel(path)
            # take only 5 features importance
            main_5_DT_features = df_DT.head(5)
            lst_DT = main_5_DT_features['Attribute'].tolist()
            Decision_Tree[filename] = lst_DT
    # Gradient Boosted Trees Feature Importance
    if filename.endswith('GB.xlsx'):
        if filename[:-8] in Predicted_successfully_GBT:
            path = Directory + '\\' + filename
            df_GB = pd.read_excel(path)
            # take only 5 features importance
            main_5_GB_features = df_GB.head(5)
            lst_GB = main_5_GB_features['Attribute'].tolist()
            Gradient_Boosted_Trees[filename] = lst_GB
    # Support Vector Machine Feature Importance
    if filename.endswith('SVM.xlsx'):
        if filename[:-9] in Predicted_successfully_SVM:
            path = Directory + '\\' + filename
            df_SVM = pd.read_excel(path)
            # take only 5 features importance
            main_5_SVM_features = df_SVM.head(5)
            lst_SVM = main_5_SVM_features['Attribute'].tolist()
            Support_Vector_Machine[filename] = lst_SVM

# Decision Tree
#('Decision Tree: ', Decision_Tree)
#print('Decision_Tree num of traits: ', len(Decision_Tree))
features_dt = list(Decision_Tree.values())
flat_list_dt = [item for sublist in features_dt for item in sublist]
df_features_dt = pd.DataFrame (flat_list_dt, columns = ['feature'])
df_features_dt['feature']=df_features_dt['feature'].str.title()
df_features_dt = df_features_dt.groupby(["feature"])['feature'].agg(["count"]).reset_index()
#feature_importance_chart(df_features_dt, 'Feature Importance Decision Tree model for additional succeeded predicted traits using top 5 predictors')
#feature_importance_chart_details(df_features_dt, 'Feature Importance Decision Tree model for additional succeeded predicted traits using top 5 predictors')
feature_importance_chart(df_features_dt, 'Decision Tree')

#Random Forest
#('Random_Forest_dict: ', Random_Forest)
#print('Random_Forest_dict num of traits: ', len(Random_Forest))
features = list(Random_Forest.values())
flat_list = [item for sublist in features for item in sublist]
df_features_rf = pd.DataFrame (flat_list, columns = ['feature'])
df_features_rf["feature"]=df_features_rf["feature"].str.title()
df_features_rf = df_features_rf.groupby(["feature"])['feature'].agg(["count"]).reset_index()
#feature_importance_chart(df_features_rf, 'Feature Importance Random Forest model for additional succeeded predicted traits using top 5 predictors')
#feature_importance_chart_details(df_features_rf, 'Feature Importance Random Forest model for additional succeeded predicted traits using top 5 predictors')
feature_importance_chart(df_features_rf, 'Random Forest')

#Gradient_Boosted_Trees
#print('Gradient_Boosted_Trees: ', Gradient_Boosted_Trees)
#print('Gradient_Boosted_Trees num of traits: ', len(Gradient_Boosted_Trees))
features_gb = list(Gradient_Boosted_Trees.values())
flat_list_gb = [item for sublist in features_gb for item in sublist]
df_features_gb = pd.DataFrame (flat_list_gb, columns = ['feature'])
df_features_gb['feature']=df_features_gb['feature'].str.title()
df_features_gb = df_features_gb.groupby(["feature"])['feature'].agg(["count"]).reset_index()
#feature_importance_chart(df_features_gb, 'Feature Importance Gradient Boosted Trees model for additional succeeded predicted traits using top 5 predictors')
#feature_importance_chart_details(df_features_gb, 'Feature Importance Gradient Boosted Trees model for additional succeeded predicted traits using top 5 predictors')
feature_importance_chart(df_features_gb, 'Gradient Boosted Trees')

# Support Vector Machine
#print('Support_Vector_Machine: ', Support_Vector_Machine)
#print('Support_Vector_Machine num of traits: ', len(Support_Vector_Machine))
features_svm = list(Support_Vector_Machine.values())
flat_list_svm = [item for sublist in features_svm for item in sublist]
df_features_svm = pd.DataFrame (flat_list_svm, columns = ['feature'])
df_features_svm['feature']=df_features_svm['feature'].str.title()
df_features_svm = df_features_svm.groupby(["feature"])['feature'].agg(["count"]).reset_index()
#feature_importance_chart(df_features_svm, 'Feature Importance Support Vector Machine model for main succeeded predicted traits using top 5 predictors')
#feature_importance_chart_details(df_features_svm, 'Feature Importance Support Vector Machine model for main succeeded predicted traits using top 5 predictors')
feature_importance_chart(df_features_svm, 'Support Vector Machine')

"""#only for testing - approve feature importance list contains all feature

# Decision_Tree
check_list_contain_all_features_dt = list(Decision_Tree.keys())
check_list_contain_all_features_dt=[feature[:-8] for feature in check_list_contain_all_features_dt]
#print("check_list_contain_all_features_SVM", check_list_contain_all_features_dt)

missing_dt=[]
for item in Predicted_successfully_DT:
    if item in check_list_contain_all_features_dt:
        continue
    else:
        missing_dt.append(item)
print('missing features files dt: ', missing_dt)

#Random Forest
check_list_contain_all_features = list(Random_Forest.keys())
check_list_contain_all_features=[feature[:-8] for feature in check_list_contain_all_features]
#print("check_list_contain_all_features", check_list_contain_all_features)

missing=[]
for item in Predicted_successfully_RF:
    if item in check_list_contain_all_features:
        continue
    else:
        missing.append(item)
print('missing features files RF: ', missing)

check_list_contain_all_features_gb = list(Gradient_Boosted_Trees.keys())
check_list_contain_all_features_gb=[feature[:-8] for feature in check_list_contain_all_features_gb]
#print("check_list_contain_all_features_gb", check_list_contain_all_features_gb)

missing_gb=[]
for item in Predicted_successfully_GBT:
    if item in check_list_contain_all_features_gb:
        continue
    else:
        missing_gb.append(item)
print('missing features files GB: ', missing_gb)

# Support_Vector_Machine
check_list_contain_all_features_SVM = list(Support_Vector_Machine.keys())
check_list_contain_all_features_SVM=[feature[:-9] for feature in check_list_contain_all_features_SVM]
#print("check_list_contain_all_features_SVM", check_list_contain_all_features_SVM)

missing_SVM=[]
for item in Predicted_successfully_SVM:
    if item in check_list_contain_all_features_SVM:
        continue
    else:
        missing_SVM.append(item)
print('missing features files SVM: ', missing_SVM)"""

# ------------------------------------------------------------
# ------------ Traits succeeded to be predicted  ------------
# ------------------------------------------------------------
df_table_chart = pd.read_csv('ML_output\pearson_corr_all_traits.csv', header=[0])
Predicted_sorted, Predicted, df_pred = table_chart(df_table_chart)

df_pred_traits=df_pred.drop(
        ['Decision_Tree', 'Random_Forest', 'Gradient_Boosted_Trees', 'Support_Vector_Machine'], axis=1).reset_index()
df_pred=df_pred.groupby(["Personality Theory"])['r'].agg(["mean","std"]).sort_values(by=['mean'], ascending=False).reset_index().rename(columns={'mean':'r'})

result = pd.merge(df_pred, df_pred_traits, how="inner", on=["Personality Theory"]).rename(columns={'r_x':'r','Personality Theory':'Personality Construct' })
result = result.style.apply(row_style, axis=1)
#table of the Predictive performance for personality constructs with r avg, std and best model and r fir each trait
result.to_excel("ML_output\Predictive_performance_for_personality_constructs.xlsx")

theory = df_pred.style.apply(row_style, axis=1)
theory.to_excel("ML_output\mean_r_theory.xlsx")
#Predicted_sorted.to_excel("ML_output\Best_model_results_with_colors_sort_by_r.xlsx")
#Predicted.to_excel("ML_output\Best_model_results_with_colors_sort_by_trait.xlsx")


