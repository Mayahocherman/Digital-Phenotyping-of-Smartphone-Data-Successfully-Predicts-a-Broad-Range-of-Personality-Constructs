import numpy as np
import pandas as pd
from scipy.stats import zscore
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


def correlation_matrix_plot(droped):
    droped_labels = droped.columns.values[:]
    corr_matrix = droped.corr(method='pearson')
    corr_matrix.to_csv('Correlation\droped.csv',index=True)
    fig = plt.figure(figsize=[20, 30])
    ax = fig.add_subplot(111)
    plt.title('Feature Correlation')
    cax = ax.matshow(corr_matrix, vmin=-1, vmax=1)
    fig.colorbar(cax)
    ticks = np.arange(0, len(droped_labels), 1)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(droped_labels)
    ax.set_yticklabels(droped_labels)
    plt.show()
    # Select upper triangle of correlation matrix
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))
    # Find index of feature columns with correlation greater than 0.95
    to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]
    #if to_drop != []:
    #    print("Correlated Features:", to_drop)

df_data=pd.read_csv('Data_processing_output\Processed_data.csv')

print ("Number Of cols : ", df_data.shape[1])
print ("Number Of Observations : ", df_data.shape[0])

traits_labels=['Explorer_Rank', 'Builder_Rank', 'Director_Rank', 'Negotiator_Rank',  'Secure_attachment', 'Anxious-preoccupied_attachment', 'Fearful-avoidant_attachment', 'Dismissive–avoidant_attachment', 'FFM_Extraversion', 'FFM_Agreeableness', 'FFM_Concientiousness', 'FFM_Neurotism', 'FFM_Openess', 'Machiavellianism', 'Narcissism', 'Psychopathy',
       'Dark_Triad_Compounded', 'RTB-Final_Score',  'Ambiguous_stimuli_in_general_(G)', 'Complex_stimuli_(C)', 'Uncertain_stimuli_(U)', 'New/unfamiliar/novel_stimuli_(N)', 'Insoluble/illogical/irreducible/internally_inconsistent_stimuli_(I)', 'TFA_SUM', 'TFA_(Tolerance_for_Ambiguity)_Score', 'Self_Efficacy', 'Self-Discipline', 'Tolerance', 'Absorption', 'Appraisal', 'Regulation',
       'Distress_Tolrance_Final', 'Creativity_bricolage', 'Pressure_stress', 'Action_persistence', 'Improvisation_capacity_Final', 'Creativity_Compound_Score_(IPIP)', 'Locus_of_Control', 'Self-emotion_appraisal_(SEA)', 'Others’_emotion_appraisal_(OEA)', 'Use_of_emotion_(UOE)', 'Regulation_of_emotion_(ROE)', 'ESI_Compund_Score', 'Social_Desirabilty_Score',
       'ERM-__Physical_Endurance', 'TMM-_Physical_Tempo', 'SS-_Risk_Seeking', 'ERS-_Social_Endurance', 'TMS-_Social_Tempo', 'EMP-_Empathy', 'ERI-_Intellectual_Endurance', 'PL-_Plasticity', 'PRO-_Probab_thinking', 'SLF-_Self-confidence', 'IMP-__Impulsivity', 'NEU-_Neuroticism',
       'CNTL-_Social_desirability_tendency_for_STQ-77_(15-20_demonstrate_high_Social_Desirablity_and_may_be_discarded_at_your_discression)', 'V_STD-_Self-direction_Thought', 'V_SDA-_Self-direction_Action', 'V_ST-_Stimulation', 'V_HE-_Hedonism', 'V_AC-_Achievement', 'V_POR-_Power_Dominance', 'V_POD-_Power_Resources', 'V_FAC-_Face', 'V_SEP-_Security_Personal', 'V_SES-_Security_Societal',
       'V_TR-_Tradition', 'V_COR-_Conformity-Rules', 'V_COI-_Conformity-Interpersonal', 'V_HU-_Humility', 'V_UNN-_Universalism-Nature', 'V_UNC-_Universalism-Concern', 'V_UNT-_Universalism-Tolerance', 'V_BEC-_Benevolence_–Care', 'V_BED-_Benevolence-Dependability']

print ("Number Of traits (labels) to predict : ", len(traits_labels))

smartphone_features = ['Bluetooth_count_week','wifi_count_week', 'Bluetooth_mean_24h','wifi_mean_24h',
       'screen_count_week', 'Screen_avg_time_week','screen_count_treshold_week','screen_count_mean_24','Screen_avg_time_24','screen_mean_treshold_24',
       'Battery_count_threshold_week','Battery_count_week','Battery_avg_threshold_24h','Battery_avg_24h',
       'Calls_count_incoming_week','Calls_count_outgoing_week','Calls_count_missing_week','calls_duration_mean_week','Calls_trace_incoming_week','Calls_trace_outgoing_week','Calls_trace_missing_week','Call_ratio_week',
        'messages_count_incoming_week','messages_count_outgoing_week','messages_trace_outgoing_week','messages_trace_incoming_week',
        'Calls_mean_incoming_24h','Calls_mean_outgoing_24h','Calls_mean_missing_24h','calls_duration_mean_24h','Calls_trace_mean_incoming_24h','Calls_trace_mean_outgoing_24h','Calls_trace_mean_missing_24h','Call_ratio_24h',
        'messages_mean_incoming_24h','messages_mean_outgoing_24h','messages_trace_outgoing_24h','messages_trace_incoming_24h']

print ("Number Of features : ", len(smartphone_features))

Control_variables=['Age', 'Gender','Family Status', 'Education','Employment Type', 'device_id', 'manufacturer']

print ("Number Control variables : ", len(Control_variables)-1)


# ------------------------------------------------
# -------------------- Features  -----------------
# ------------------------------------------------
df_features=df_data[smartphone_features]
df_features.hist(figsize=(28,12))
plt.show()

corr_matrix = df_features.corr(method='pearson')
corr_matrix.to_csv('Correlation\Features_corr.csv', index=True)
correlation_matrix_plot(df_features)

# ------------------------------------------------
# -------------- Label (traits)  ----------------
# ------------------------------------------------
df_labels=df_data[traits_labels]
df_labels.hist(figsize=(28,12))
plt.show()

corr_matrix = df_labels.corr(method='pearson')
#corr_matrix.to_csv('Correlation\Labels_corr.csv', index=True)
correlation_matrix_plot(df_labels)


# ------------------------------------------------
# -------------- Control variables  ----------------
# ------------------------------------------------

Control_variables_num=['Age']
Control_variables_cat=['Gender','Family Status', 'Education','Employment Type', 'manufacturer']

#Age hist
df_age=df_data[Control_variables_num]
df_labels.hist(figsize=(28,12))
plt.show()

for i in Control_variables_cat:
     print ("control var:",i)
     df_data[i].value_counts()[:].plot(kind='bar',figsize =(16,4))
     #plt.show()


# ------------------------------------------------
# -------------- Features and Label (traits)  ----
# ------------------------------------------------
data=df_data.copy().drop(Control_variables, axis=1)

corr_matrix = data.corr(method='pearson')
corr_matrix = corr_matrix.iloc[0:76,76:]
corr_matrix=corr_matrix.drop(['messages_count_outgoing_week', 'messages_trace_incoming_week','messages_mean_outgoing_24h','messages_trace_incoming_24h'], axis=1)

corr_matrix_pairs = corr_matrix.unstack()
corr_matrix_pairs_sort = corr_matrix_pairs.sort_values(kind="quicksort")

corr_matrix_pairs.to_csv('Correlation\corr_matrix_pairs.csv', index=True)
corr_matrix_pairs_sort.to_csv('Correlation\corr_matrix_pairs_sort.csv', index=True)
