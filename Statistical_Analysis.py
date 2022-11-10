import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 20)

df=pd.read_csv('Final_features_output\Processed_data.csv')


df_des=df.copy()
control_var = ["manufacturer - group", "Family Status"]
for i in control_var:
    print("control variable:", i)
    df_des[i].value_counts()[:].plot(kind='bar', figsize=(16, 4))
    plt.show()

#Person correlation
df_cor=df.copy()
matrix = df_cor.corr(method='pearson').round(2)
matrix = matrix.unstack()
matrix = matrix[abs(matrix) >= 0.25]
matrix.to_csv('Correlation\sig_cor.csv',index=True)


# list of related features/ personality traits from correlation found:
"""df_cor_man=df_cor_man.filter(items=['manufacturer - group','Calls_count_missing_week','Calls_trace_incoming_week',
'Calls_trace_mean_missing_24h','Calls_trace_mean_outgoing_24h','Calls_trace_missing_week','screen_count_mean_24','screen_count_week','wifi_count_week','Calls_mean_missing_24h',
'Bluetooth_count_week','Battery_count_week','Call_ratio_24h','Bluetooth_mean_24h','Calls_mean_incoming_24h','Calls_trace_outgoing_week','screen_mean_treshold_24',
'wifi_mean_24h','calls_duration_mean_24h','Calls_trace_mean_incoming_24h','Negotiator_Rank',
'Director_%_Streanth','Negotiator_%_Streanth','Fearful-avoidant_attachment','Dismissiveâ€“avoidant_attachment',
'Narcissism','Ambiguous_stimuli_in_general_(G)','Uncertain_stimuli_(U)','New/unfamiliar/novel_stimuli_(N)',
'Insoluble/illogical/irreducible/internally_inconsistent_stimuli_(I)','TFA_SUM','TFA_(Tolerance_for_Ambiguity)_Score','Creativity_bricolage',
'Pressure_stress','Improvisation_capacity_Final','Self-emotion_appraisal_(SEA)','SS-_Risk_Seeking','ERI-_Intellectual_Endurance',
'PL-_Plasticity','IMP-__Impulsivity','NEU-_Neuroticism','CNTL-_Social_desirability_tendency_for_STQ-77_(15-20_demonstrate_high_Social_Desirablity_and_may_be_discarded_at_your_discression)',
'V_HE-_Hedonism','V_AC-_Achievement','V_POD-_Power_Resources','V_FAC-_Face',
'V_HU-_Humility','V_UNN-_Universalism-Nature','V_UNT-_Universalism-Tolerance'])"""

# ----------------------------------------manufacturer---------------------------------------------
# Person correlation split by manufacturer group for significant corr
# How we select columns?
# 1. Found Person correlation for all data
# 2. ANOVA tests for smartphone features and manufacturer
# 3. For the significant features by ANOVA, and for the significant corr above, we calculate again the correlation split by manufacturer

df_cor_man=df.copy()
df_cor_man=df_cor_man.filter(items=['manufacturer - group',
'screen_count_mean_24','Calls_count_missing_week','Calls_trace_outgoing_week','Calls_trace_incoming_week','Calls_mean_incoming_24h',
'Director_%_Streanth','Negotiator_%_Streanth','Fearful-avoidant_attachment','Dismissiveâ€“avoidant_attachment', 'Narcissism','Ambiguous_stimuli_in_general_(G)','Uncertain_stimuli_(U)','New/unfamiliar/novel_stimuli_(N)',
'Insoluble/illogical/irreducible/internally_inconsistent_stimuli_(I)','TFA_SUM','TFA_(Tolerance_for_Ambiguity)_Score','Creativity_bricolage','Pressure_stress','Improvisation_capacity_Final','Self-emotion_appraisal_(SEA)','SS-_Risk_Seeking','ERI-_Intellectual_Endurance',
'PL-_Plasticity','IMP-__Impulsivity','NEU-_Neuroticism','CNTL-_Social_desirability_tendency_for_STQ-77_(15-20_demonstrate_high_Social_Desirablity_and_may_be_discarded_at_your_discression)', 'V_HE-_Hedonism','V_AC-_Achievement','V_POD-_Power_Resources','V_FAC-_Face',
'V_HU-_Humility','V_UNN-_Universalism-Nature','V_UNT-_Universalism-Tolerance'])

#Samsung
df_cor_samsung=df_cor_man[df_cor_man['manufacturer - group']=='samsung']
df_cor_samsung = df_cor_samsung.corr(method='pearson').round(2)
df_cor_samsung.to_csv('Correlation\cor_manufacturer_samsung.csv',index=True)
#print(df_cor_samsung)

#Xioami
df_cor_Xioami=df_cor_man[df_cor_man['manufacturer - group']=='Xiaomi']
df_cor_Xioami = df_cor_Xioami.corr(method='pearson').round(2)
df_cor_Xioami.to_csv('Correlation\cor_manufacturer_Xiaomi.csv',index=True)

#Else
df_cor_else=df_cor_man[df_cor_man['manufacturer - group']=='else']
df_cor_else = df_cor_else.corr(method='pearson').round(2)
df_cor_else.to_csv('Correlation\cor_manufacturer_else.csv',index=True)

# ----------------------------------------Family Status---------------------------------------------
# Person correlation split by Family Status group for significant corr
# How we select columns?
# 1. Found Person correlation for all data
# 2. ANOVA tests for smartphone features and Family Status
# 3. For the significant features by ANOVA, and for the significant corr above, we calculate again the correlation split by Family Status

df_cor_status=df.copy()
df_cor_status=df_cor_status.filter(items=['Family Status','Calls_trace_mean_missing_24h', 'Negotiator_Rank',
'Director_%_Streanth','Negotiator_%_Streanth','Fearful-avoidant_attachment','Dismissiveâ€“avoidant_attachment',
'Narcissism','Ambiguous_stimuli_in_general_(G)','Uncertain_stimuli_(U)','New/unfamiliar/novel_stimuli_(N)',
'Insoluble/illogical/irreducible/internally_inconsistent_stimuli_(I)','TFA_SUM','TFA_(Tolerance_for_Ambiguity)_Score','Creativity_bricolage',
'Pressure_stress','Improvisation_capacity_Final','Self-emotion_appraisal_(SEA)','SS-_Risk_Seeking','ERI-_Intellectual_Endurance',
'PL-_Plasticity','IMP-__Impulsivity','NEU-_Neuroticism','CNTL-_Social_desirability_tendency_for_STQ-77_(15-20_demonstrate_high_Social_Desirablity_and_may_be_discarded_at_your_discression)',
'V_HE-_Hedonism','V_AC-_Achievement','V_POD-_Power_Resources','V_FAC-_Face',
'V_HU-_Humility','V_UNN-_Universalism-Nature','V_UNT-_Universalism-Tolerance'])


#Singles
df_cor_status_single=df_cor_status[df_cor_status['Family Status']=='רווק/רווקה']
df_cor_status_single = df_cor_status_single.corr(method='pearson').round(2)
df_cor_status_single.to_csv('Correlation\cor_status_single.csv',index=True)
#married
df_cor_status_married=df_cor_status[df_cor_status['Family Status']=='נשוי/נשואה']
df_cor_status_married = df_cor_status_married.corr(method='pearson').round(2)
df_cor_status_married.to_csv('Correlation\cor_status_married.csv',index=True)
#Shared appertment
df_cor_status_shared=df_cor_status[df_cor_status['Family Status']=='מגורים משותפים ללא נישואין']
df_cor_status_shared = df_cor_status_shared.corr(method='pearson').round(2)
df_cor_status_shared.to_csv('Correlation\cor_status_Shared_appertment.csv',index=True)


# ----------------------------------------Employment Type ---------------------------------------------
# Person correlation split by Employment Type group for significant corr
# How we select columns?
# 1. Found Person correlation for all data
# 2. T-test for smartphone features and Employment Type
# 3. For the significant features by T-test, and for the significant corr above, we calculate again the correlation split by Employment Type

df_cor_Employment=df.copy()
df_cor_Employment=df_cor_Employment.filter(items=['Employment Type', 'Calls_mean_missing_24h',
'Negotiator_Rank','Director_%_Streanth','Negotiator_%_Streanth','Fearful-avoidant_attachment','Dismissiveâ€“avoidant_attachment',
'Narcissism','Ambiguous_stimuli_in_general_(G)','Uncertain_stimuli_(U)','New/unfamiliar/novel_stimuli_(N)',
'Insoluble/illogical/irreducible/internally_inconsistent_stimuli_(I)','TFA_SUM','TFA_(Tolerance_for_Ambiguity)_Score','Creativity_bricolage',
'Pressure_stress','Improvisation_capacity_Final','Self-emotion_appraisal_(SEA)','SS-_Risk_Seeking','ERI-_Intellectual_Endurance',
'PL-_Plasticity','IMP-__Impulsivity','NEU-_Neuroticism','CNTL-_Social_desirability_tendency_for_STQ-77_(15-20_demonstrate_high_Social_Desirablity_and_may_be_discarded_at_your_discression)',
'V_HE-_Hedonism','V_AC-_Achievement','V_POD-_Power_Resources','V_FAC-_Face',
'V_HU-_Humility','V_UNN-_Universalism-Nature','V_UNT-_Universalism-Tolerance'])
#print(df_cor_Employment['Employment Type'])

# Steady
df_cor_Employment_steady=df_cor_Employment[df_cor_Employment['Employment Type']=='קבוע']
df_cor_Employment_steady = df_cor_Employment_steady.corr(method='pearson').round(2)
df_cor_Employment_steady.to_csv('Correlation\cor_Employment_steady.csv',index=True)
# Temporary
df_cor_Employment_temp=df_cor_Employment[df_cor_Employment['Employment Type']=='זמני']
df_cor_Employment_temp = df_cor_Employment_temp.corr(method='pearson').round(2)
df_cor_Employment_temp.to_csv('Correlation\cor_Employment_temp.csv',index=True)

