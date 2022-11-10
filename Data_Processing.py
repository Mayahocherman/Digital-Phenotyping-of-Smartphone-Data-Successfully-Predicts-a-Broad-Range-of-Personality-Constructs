# Once import by 'Download_SQL_from_server' file, import from CSV for quick access
import numpy as np
import pandas as pd
from scipy.stats import zscore
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 20)

# -------------------------------------------------------------------------------------------
# ------------------------------- Functions  --------------------------------------------
# -------------------------------------------------------------------------------------------

def complete_null_median(df,col):
    df[col] = df[col].fillna((df[col]).median())
    return df

def z_score(df,cols):
    for col in cols:
        df[col] = zscore(df[col])
    return df

# -------------------------------------------------------------------------------------------
# ------------------------------- Questionnaire  --------------------------------------------
# -------------------------------------------------------------------------------------------

# Aware_And_Questionnaire data frame
# Due to users privacy - we didn't deploy this file. Please attach new file before running
df_data=pd.read_csv('MySQL_output\Aware_And_Questionnaire_csv.csv')
df_Aware=df_data.copy()
df_Aware=df_Aware.drop(['Timestamp','Unnamed: 0','Explorer_%_Streanth','Builder_%_Streanth', 'Director_%_Streanth','Negotiator_%_Streanth','Attachment_Style_Scale','Attachment_Style','RTB-#2','RTB-#3','RTB-#4','RTB-#5','RTB-#6','RTB-#7','RTB-#8','RTB-#9','RTB-#10', 'RTB-#13', 'RTB-#14', 'RTB-#1', 'RTB-#11', 'RTB-#12', 'RTB-#15', 'RTB-Category', 'Sum_Positive_(temp)', 'Social_Desirability_Category','Sum_Negative_(temp)','timeframe','Feminist_attitudes','Religion_if_relevant','Degree_of_religiosity','Employment Sector','Employment %', 'label','Prior Covid Domestic Work #', 'Current domestic-workplace work pattern', 'Neurological/Psychiatric dignosis and medications', 'Fixed medicine', 'timestamp', 'build_id'], axis=1)
print ("Number Of Features : ", df_Aware.shape[1])
print ("Number Of Observations : ", df_Aware.shape[0])

#Descriptive Statistics before scaling
#print(df_Aware.describe())
df_Aware.hist(figsize=(28,12))
#plt.show()


# Zscore Scaling for traits responses
label=['Explorer_Rank', 'Builder_Rank', 'Director_Rank', 'Negotiator_Rank',  'Secure_attachment', 'Anxious-preoccupied_attachment', 'Fearful-avoidant_attachment', 'Dismissive–avoidant_attachment', 'FFM_Extraversion', 'FFM_Agreeableness', 'FFM_Concientiousness', 'FFM_Neurotism', 'FFM_Openess', 'Machiavellianism', 'Narcissism', 'Psychopathy',
       'Dark_Triad_Compounded', 'RTB-Final_Score',  'Ambiguous_stimuli_in_general_(G)', 'Complex_stimuli_(C)', 'Uncertain_stimuli_(U)', 'New/unfamiliar/novel_stimuli_(N)', 'Insoluble/illogical/irreducible/internally_inconsistent_stimuli_(I)', 'TFA_SUM', 'TFA_(Tolerance_for_Ambiguity)_Score', 'Self_Efficacy', 'Self-Discipline', 'Tolerance', 'Absorption', 'Appraisal', 'Regulation',
       'Distress_Tolrance_Final', 'Creativity_bricolage', 'Pressure_stress', 'Action_persistence', 'Improvisation_capacity_Final', 'Creativity_Compound_Score_(IPIP)', 'Locus_of_Control', 'Self-emotion_appraisal_(SEA)', 'Others’_emotion_appraisal_(OEA)', 'Use_of_emotion_(UOE)', 'Regulation_of_emotion_(ROE)', 'ESI_Compund_Score', 'Social_Desirabilty_Score',
       'ERM-__Physical_Endurance', 'TMM-_Physical_Tempo', 'SS-_Risk_Seeking', 'ERS-_Social_Endurance', 'TMS-_Social_Tempo', 'EMP-_Empathy', 'ERI-_Intellectual_Endurance', 'PL-_Plasticity', 'PRO-_Probab_thinking', 'SLF-_Self-confidence', 'IMP-__Impulsivity', 'NEU-_Neuroticism',
       'CNTL-_Social_desirability_tendency_for_STQ-77_(15-20_demonstrate_high_Social_Desirablity_and_may_be_discarded_at_your_discression)', 'V_STD-_Self-direction_Thought', 'V_SDA-_Self-direction_Action', 'V_ST-_Stimulation', 'V_HE-_Hedonism', 'V_AC-_Achievement', 'V_POR-_Power_Dominance', 'V_POD-_Power_Resources', 'V_FAC-_Face', 'V_SEP-_Security_Personal', 'V_SES-_Security_Societal',
       'V_TR-_Tradition', 'V_COR-_Conformity-Rules', 'V_COI-_Conformity-Interpersonal', 'V_HU-_Humility', 'V_UNN-_Universalism-Nature', 'V_UNC-_Universalism-Concern', 'V_UNT-_Universalism-Tolerance', 'V_BEC-_Benevolence_–Care', 'V_BED-_Benevolence-Dependability']

df_Aware_zscore= z_score(df_Aware,label)
df_Aware_zscore.hist(figsize=(28,12)) #plot after Zscore scaling
#plt.show()

# -------------------------------------------------------------------------------------------
# ------------------------------- Connectivity - WIFI & Bluetooth ---------------------------
# -------------------------------------------------------------------------------------------

df_Bluetooth_week=pd.read_csv("MySQL_output\Bluetooth_week_csv.csv")
df_wifi_week=pd.read_csv('MySQL_output\Wifi_week_csv.csv')

# ------------------------------------------------
# ------------ Weekly aggregated calc ------------
# ------------------------------------------------

#Bluetooth_count_week is the count of distinct total weekly Bluetooth traces.
df_Bluetooth_week=df_Bluetooth_week.rename(columns={'count':'Bluetooth_count_week','median':'Bluetooth_median','std':'Bluetooth_std'})
# Wi-Fi is the count of distinct total weekly Wifi traces.
df_wifi_week=df_wifi_week.rename(columns={'count_wifi':'wifi_count_week','median':'wifi_median_week','std':'wifi_std_week'}).drop(['Unnamed: 0'], axis=1)

# ------------------------------------------------
# ---------- Daily (24h) aggregated calc ---------
# ------------------------------------------------

#Bluetooth_mean_24h is the average of daily distinct Bluetooth traces.
df_Bluetooth_24=pd.read_csv('MySQL_output\Bluetooth_csv.csv')
df_Bluetooth_24 = df_Bluetooth_24.groupby(["device_id", "date"])["count"].agg(["count"])
df_Bluetooth_24 = df_Bluetooth_24.groupby(["device_id"])["count"].agg(["mean"]).reset_index().fillna(0)
df_Bluetooth_24=df_Bluetooth_24.rename(columns={'mean':'Bluetooth_mean_24h','median':'Bluetooth_median','std':'Bluetooth_std'})

# wifi_mean_24h is the average of daily distinct Wifi traces.
df_wifi_24=pd.read_csv('MySQL_output\Wifi_csv.csv')
df_wifi_24 = df_wifi_24.groupby(["device_id", "date"])["count_wifi"].agg(["count"]).reset_index().fillna(0)
df_wifi_24 = df_wifi_24.groupby(["device_id"])["count"].agg(["mean"])
df_wifi_24=df_wifi_24.rename(columns={'mean':'wifi_mean_24h','median':'wifi_median','std':'wifi_std'})


# ------------------------------------------------
# ---------- table merge & Nulls handling --------
# ------------------------------------------------

df_aware_bluetooth= df_Aware_zscore.merge(df_Bluetooth_week, how='left', on='device_id')
df_aware_wifi_bluetooth_week= df_aware_bluetooth.merge(df_wifi_week, how='left', on='device_id')

df_aware_wifi_bluetooth_week=complete_null_median(df_aware_wifi_bluetooth_week,'Bluetooth_count_week')
df_aware_wifi_bluetooth_week=complete_null_median(df_aware_wifi_bluetooth_week,'wifi_count_week')

df_aware_bluetooth_24=df_aware_wifi_bluetooth_week.merge(df_Bluetooth_24, how='left', on='device_id')
df_aware_bluetooth_wifi_24= df_aware_bluetooth_24.merge(df_wifi_24, how='left', on='device_id')

df_aware_bluetooth_24=complete_null_median(df_aware_bluetooth_wifi_24,'Bluetooth_mean_24h')
df_aware_bluetooth_24=complete_null_median(df_aware_bluetooth_wifi_24,'wifi_mean_24h')

df_connectivity=df_aware_bluetooth_24.copy()

# -------------------------------------------------------------------------------------------
# -------------------------------------- Screen ---------------------------------------------
# -------------------------------------------------------------------------------------------

df_screen_count_week=pd.read_csv('MySQL_output\Screen_count_csv.csv')

# ------------------------------------------------
# ------------ Weekly aggregated calc ------------
# ------------------------------------------------

# Screen_count_week is the count of occurrences in which the screen was in “On” state.
df_screen_count_week = df_screen_count_week.groupby(["device_id"])['count_screen_on'].agg(["count"]).reset_index().fillna(0)
df_screen_count_week=df_screen_count_week.rename(columns={'count':'screen_count_week'})

# Screen_avg_time_week is the average duration in which the screen was in “On” state.
df_screen_time_week=pd.read_csv('MySQL_output\Screen_csv.csv',parse_dates=['time']).sort_values(by=['device_id', 'time']).reset_index().rename(columns={'screen_status':'screen_status_before','time':'time_before','part_of_the_day':'part_before','date':'date_before'})
df_screen_time2_week=pd.read_csv('MySQL_output\Screen_csv.csv',parse_dates=['time']).sort_values(by=['device_id', 'time']).iloc[1:].reset_index().rename(columns={'screen_status':'screen_status_after','time':'time_after','part_of_the_day':'part_after','date':'date_after'})
df_screen_time_join_week= df_screen_time_week.merge(df_screen_time2_week, left_index=True, right_index=True).drop(['Unnamed: 0_x', 'Unnamed: 0_y','index_x','index_y','part_after','part_before'], axis=1)
df_screen_time_join2_week=df_screen_time_join_week[df_screen_time_join_week['device_id_x']==df_screen_time_join_week['device_id_y']]
df_screen_time_join3_week=df_screen_time_join2_week[df_screen_time_join2_week['date_before']==df_screen_time_join2_week['date_after']]
df_screen_time_join4_week=df_screen_time_join3_week[df_screen_time_join3_week['screen_status_before']!=df_screen_time_join3_week['screen_status_after']]
df_screen_time_join5_week=df_screen_time_join4_week[df_screen_time_join4_week['screen_status_before']==1]
df_screen_time_calc_Week=df_screen_time_join5_week.copy()
df_screen_time_calc_Week['time_diff']=(df_screen_time_calc_Week['time_after']-df_screen_time_calc_Week['time_before']) / np.timedelta64(1, 's')
df_screen_time_calc_Week = df_screen_time_calc_Week.groupby(["device_id_x"])['time_diff'].agg(["mean"]).reset_index().fillna(0) #nulls replaced with 0
df_screen_time_calc_Week=df_screen_time_calc_Week.rename(columns={'device_id_x':'device_id','mean':'Screen_avg_time_week','median':'Screen_median_week','std':'Screen_std_week'})

# Screen_count_treshold_week is the count of occurrences in which the screen was in “On” state for less than 15 seconds.
df_screen_time_treshold_week=df_screen_time_join5_week.copy()
df_screen_time_treshold_week['time_diff']=(df_screen_time_treshold_week['time_after']-df_screen_time_treshold_week['time_before']) / np.timedelta64(1, 's')
df_screen_time_treshold_week=df_screen_time_treshold_week[df_screen_time_treshold_week['time_diff']<=15]
df_screen_time_treshold_week = df_screen_time_treshold_week.groupby(["device_id_x"])['time_diff'].agg(["count"]).reset_index().fillna(0)
df_screen_time_treshold_week=df_screen_time_treshold_week.rename(columns={'device_id_x':'device_id','count':'screen_count_treshold_week'})

# ------------------------------------------------
# ---------- Daily (24h) aggregated calc ---------
# ------------------------------------------------

#Screen_count_mean_24 is the average of daily occurrences in which the screen was in “On” state.
df_screen_count_24=pd.read_csv('MySQL_output\Screen_count_csv.csv')
df_screen_count_24 = df_screen_count_24.groupby(["device_id",'date'])['count_screen_on'].agg(["count"])
df_screen_count_24 = df_screen_count_24.groupby(["device_id"])['count'].agg(["mean"]).reset_index().fillna(0)
df_screen_count_24=df_screen_count_24.rename(columns={'mean':'screen_count_mean_24'})

#Screen_avg_time_24 is the average daily duration in seconds in which the screen was in “On” state.
df_screen_time_24=pd.read_csv('MySQL_output\Screen_csv.csv',parse_dates=['time']).sort_values(by=['device_id', 'time']).reset_index().rename(columns={'screen_status':'screen_status_before','time':'time_before','part_of_the_day':'part_before','date':'date_before'})
df_screen_time2_24=pd.read_csv('MySQL_output\Screen_csv.csv',parse_dates=['time']).sort_values(by=['device_id', 'time']).iloc[1:].reset_index().rename(columns={'screen_status':'screen_status_after','time':'time_after','part_of_the_day':'part_after','date':'date_after'})
df_screen_time_join= df_screen_time_24.merge(df_screen_time2_24, left_index=True, right_index=True).drop(['Unnamed: 0_x', 'Unnamed: 0_y','index_x','index_y','part_after','part_before'], axis=1)
df_screen_time_join2=df_screen_time_join[df_screen_time_join['device_id_x']==df_screen_time_join['device_id_y']]
df_screen_time_join3=df_screen_time_join2[df_screen_time_join2['date_before']==df_screen_time_join2['date_after']]
df_screen_time_join4=df_screen_time_join3[df_screen_time_join3['screen_status_before']!=df_screen_time_join3['screen_status_after']]
df_screen_time_join5=df_screen_time_join4[df_screen_time_join4['screen_status_before']==1]
df_screen_time_calc_24=df_screen_time_join5.copy()
df_screen_time_calc_24['time_diff']=(df_screen_time_calc_24['time_after']-df_screen_time_calc_24['time_before']) / np.timedelta64(1, 's')
df_screen_time_calc_24 = df_screen_time_calc_24.groupby(["device_id_x", "date_before"])['time_diff'].agg(["mean"])
df_screen_time_calc_24 = df_screen_time_calc_24.groupby(["device_id_x"])['mean'].agg(["mean"]).reset_index().fillna(0) #nulls replaced with 0
df_screen_time_calc_24=df_screen_time_calc_24.rename(columns={'device_id_x':'device_id','mean':'Screen_avg_time_24','median':'Screen_median_24','std':'Screen_std_24'})

#Screen_mean_treshold_24 is the average of daily occurrences in which the screen was in “On” state for less than 15 seconds.
df_screen_time_treshold_24=df_screen_time_join5.copy()
df_screen_time_treshold_24['time_diff']=(df_screen_time_treshold_24['time_after']-df_screen_time_treshold_24['time_before']) / np.timedelta64(1, 's')
df_screen_time_treshold_24=df_screen_time_treshold_24[df_screen_time_treshold_24['time_diff']<=15]
df_screen_time_treshold_24 = df_screen_time_treshold_24.groupby(["device_id_x","date_before"])['time_diff'].agg(["count"]).reset_index()
df_screen_time_treshold_24 = df_screen_time_treshold_24.groupby(["device_id_x"])['count'].agg(["mean"]).reset_index().fillna(0)
df_screen_time_treshold_24=df_screen_time_treshold_24.rename(columns={'device_id_x':'device_id','mean':'screen_mean_treshold_24'})

# ------------------------------------------------
# ------------ Final Screen table merge ----------
# ------------------------------------------------

df_aware_screenCount=df_connectivity.merge(df_screen_count_week, how='left', on='device_id')
df_aware_screenCount_screenTime= df_aware_screenCount.merge(df_screen_time_calc_Week, how='left', on='device_id')
df_aware_screenCount_screenTime_screenTreshold= df_aware_screenCount_screenTime.merge(df_screen_time_treshold_week, how='left', on='device_id')

# fill Nulls with Feature Median
df_aware_screenCount_screenTime_screenTreshold['screen_count_week'] = df_aware_screenCount_screenTime_screenTreshold['screen_count_week'].fillna((df_aware_screenCount_screenTime_screenTreshold['screen_count_week'].median()))
#fill Nulls with Feature Mean
df_aware_screenCount_screenTime_screenTreshold['Screen_avg_time_week'] = df_aware_screenCount_screenTime_screenTreshold['Screen_avg_time_week'].fillna((df_aware_screenCount_screenTime_screenTreshold['Screen_avg_time_week'].mean().mean()))
# fill Nulls with Feature Median
df_aware_screenCount_screenTime_screenTreshold['screen_count_treshold_week'] = df_aware_screenCount_screenTime_screenTreshold['screen_count_treshold_week'].fillna((df_aware_screenCount_screenTime_screenTreshold['screen_count_treshold_week'].median()))

df_week_Count=df_aware_screenCount_screenTime_screenTreshold.merge(df_screen_count_24, how='left', on='device_id')
df_week_Count_time=df_week_Count.merge(df_screen_time_calc_24, how='left', on='device_id')
df_aware_screenCount_screenTime_screenTreshold= df_week_Count_time.merge(df_screen_time_treshold_24, how='left', on='device_id')
# fill Nulls with Feature Median
df_aware_screenCount_screenTime_screenTreshold['screen_count_mean_24'] = df_aware_screenCount_screenTime_screenTreshold['screen_count_mean_24'].fillna((df_aware_screenCount_screenTime_screenTreshold['screen_count_mean_24'].median()))
#fill Nulls with Feature Mean
df_aware_screenCount_screenTime_screenTreshold['Screen_avg_time_24'] = df_aware_screenCount_screenTime_screenTreshold['Screen_avg_time_24'].fillna((df_aware_screenCount_screenTime_screenTreshold['Screen_avg_time_24'].mean()))
# fill Nulls with Feature Median
df_aware_screenCount_screenTime_screenTreshold['screen_mean_treshold_24'] = df_aware_screenCount_screenTime_screenTreshold['screen_mean_treshold_24'].fillna((df_aware_screenCount_screenTime_screenTreshold['screen_mean_treshold_24'].median()))
df_connectivity_screen=df_aware_screenCount_screenTime_screenTreshold.copy()


# -------------------------------------------------------------------------------------------
# -------------------------------------- Battery ---------------------------------------------
# -------------------------------------------------------------------------------------------

df_Battery=pd.read_csv('MySQL_output\Battery_csv.csv')

# ------------------------------------------------
# ------------ Weekly aggregated calc ------------
# ------------------------------------------------

# Battery_count_threshold_week is the count of occurrences in which the battery state is lower then 20
df_Battery_threshold_week = df_Battery[df_Battery["battery_start"]<20]
df_Battery_threshold_week=df_Battery_threshold_week.groupby(["device_id"])["battery_start"].agg(["count"]).reset_index().rename(columns={'count':'Battery_count_threshold_week'})
# Battery_count_week is the count of weekly charges
df_Battery_charges = df_Battery.groupby(["device_id"])["battery_start"].agg(["count"]).reset_index().rename(columns={'count':'Battery_count_week'})

# ------------------------------------------------
# ---------- Daily (24h) aggregated calc ---------
# ------------------------------------------------

# Battery_avg_threshold_24h is the average of daily occurrences in which the battery state is lower then 20
df_Battery_threshold_24h = df_Battery[df_Battery["battery_start"]<20]
df_Battery_threshold_24h = df_Battery_threshold_24h.groupby(["device_id","date"])["battery_start"].agg(["count"])
df_Battery_threshold_24h = df_Battery_threshold_24h.groupby(["device_id"])["count"].agg(["mean"]).reset_index().rename(columns={'mean':'Battery_avg_threshold_24h'})
#Battery_avg_24h is the average of daily charges
df_Battery_24h=df_Battery.groupby(["device_id","date"])["battery_start"].agg(["count"])
df_Battery_24h = df_Battery_24h.groupby(["device_id"])["count"].agg(["mean"]).reset_index().rename(columns={'mean':'Battery_avg_24h'})

# ------------------------------------------------
# ------------ Final Screen table merge ----------
# ------------------------------------------------

df_aware_battery_week= df_connectivity_screen.merge(df_Battery_threshold_week, how='left', on='device_id').merge(df_Battery_charges, how='left', on='device_id')
df_aware_battery=df_aware_battery_week.merge(df_Battery_threshold_24h, how='left', on='device_id').merge(df_Battery_24h, how='left', on='device_id')

#fillna
df_aware_battery['Battery_count_threshold_week'] = df_aware_battery['Battery_count_threshold_week'].fillna(0)
df_aware_battery['Battery_count_week'] = df_aware_battery['Battery_count_week'].fillna((df_aware_battery['Battery_count_week'].median()))
df_aware_battery['Battery_avg_threshold_24h'] = df_aware_battery['Battery_avg_threshold_24h'].fillna(0)
df_aware_battery['Battery_avg_24h'] = df_aware_battery['Battery_avg_24h'].fillna((df_aware_battery['Battery_avg_24h'].median()))
df_connectivity_screen_battery=df_aware_battery.copy()

# -------------------------------------------------------------------------------------------
# -------------------------------------- Communication ---------------------------------------
# -------------------------------------------------------------------------------------------

df_calls_week=pd.read_csv('MySQL_output\Calls_csv.csv')
df_messages=pd.read_csv('MySQL_output\Messages_csv.csv')

# ------------------------------------------------
# ------------ Weekly aggregated calc ------------
# ------------------------------------------------

# Calls
# 1) #Calls_count_incoming_week is the count of occurrences of incoming calls during the week.
     #Calls_count_outgoing_week is the count of occurrences of outgoing calls during the week.
     #Calls_count_missing_week is the count of occurrences of missing calls during the week.
df_num_calls_week = df_calls_week.groupby(["device_id",'call_type'])["call_type"].agg(["count"]).unstack(1).reset_index().fillna(0) #nulls replaced with 0
df_num_calls_week.columns = [''.join(str(col)) for col in df_num_calls_week.columns.values]
df_num_calls_week=df_num_calls_week.rename(columns={"('device_id', '')":'device_id',"('count', 1)":'Calls_count_incoming_week',"('count', 2)":'Calls_count_outgoing_week',"('count', 3)":'Calls_count_missing_week',"('median', 1)":'Calls_median_1',"('median', 2)":'Calls_median_2',"('median', 3)":'Calls_median_3'})

# 2) Calls_duration_mean_week  is the average duration for a call excluding missing calls.
df_calls_duration_week=df_calls_week[df_calls_week["call_type"]!=3]
df_calls_duration_week = df_calls_duration_week.groupby(["device_id"])["call_duration"].agg(["mean"]).reset_index().fillna(0) #nulls replaced with 0
df_calls_duration_week=df_calls_duration_week.rename(columns={"mean":'calls_duration_mean_week',"median":'calls_duration_median',"std":'calls_duration_std'})

# 3) Count AVG distinct users (trace) per type
        # Calls_trace_outgoing_week is the count of distinct users which the particpant call to during the week.
        # Calls_trace_incoming_week is the count of distinct users which the particpant recived a call from during the week.
        # Calls_trace_missing_week is the count of distinct users which the particpant recived a call and missed it during the week.

df_calls_trace_week=pd.read_csv('MySQL_output\Calls_csv.csv')
df_calls_trace_week = df_calls_trace_week.groupby(["device_id", 'call_type', 'trace'])["trace"].agg(["count"]).reset_index()
df_calls_trace_week = df_calls_trace_week.groupby(["device_id",'call_type'])["trace"].agg(["count"]).unstack(1).reset_index().fillna(0) #nulls replaced
df_calls_trace_week.columns = [''.join(str(col)) for col in df_calls_trace_week.columns.values]
df_calls_trace_week=df_calls_trace_week.rename(columns={"('device_id', '')":'device_id',"('count', 1)":'Calls_trace_incoming_week',"('count', 2)":'Calls_trace_outgoing_week',"('count', 3)":'Calls_trace_missing_week',"('median', 1)":'Calls_trace_median_1',"('median', 2)":'Calls_trace_median_2',"('median', 3)":'Calls_trace_median_3'})

# 4) Call_ratio_week is the count of incoming calls divided by the count of all calls.
df_all_calls_week=pd.read_csv('MySQL_output\Calls_csv.csv')
df_all_calls_week = df_all_calls_week.groupby(["device_id", 'call_type'])['call_type'].agg(["sum"]).reset_index()
df_incoming_calls_week=df_all_calls_week[df_all_calls_week['call_type']==1].rename(columns={'sum':'incoming'})
df_count_total_calls_week=df_all_calls_week.groupby(["device_id"])['sum'].agg(["sum"]).reset_index().rename(columns={'sum':'all'})
df_calls_ratio_week= df_incoming_calls_week.merge(df_count_total_calls_week, how='right', on=['device_id']).fillna(0)
df_calls_ratio_week["Call_ratio"]=df_calls_ratio_week["incoming"]/df_calls_ratio_week["all"]
df_calls_ratio_week=df_calls_ratio_week.drop(['call_type', 'incoming','all'], axis=1).rename(columns={'Call_ratio':'Call_ratio_week'})

# Messages

df_messages=pd.read_csv('MySQL_output\Messages_csv.csv')

# 1) #messages_count_incoming_week is the count of occurrences of incoming messages during the week.
     #messages_count_outgoing_week is the count of occurrences of outgoing messages during the week.

df_messages_num_week=df_messages.copy()
df_messages_num_week = df_messages_num_week.groupby(["device_id",'message_type'])['message_type'].agg(["count"]).unstack(1).reset_index().fillna(0)
df_messages_num_week.columns = [''.join(str(col)) for col in df_messages_num_week.columns.values]
df_messages_num_week=df_messages_num_week.rename(columns={"('device_id', '')":'device_id',"('count', 1)":'messages_count_incoming_week',"('count', 2)":'messages_count_outgoing_week',"('mean', 3)":'messages_week_mean_3',"('median', 1)":'messages_week_median_1',"('median', 2)":'messages_week_median_2',"('median', 3)":'messages_week_median_3'})

# 2) # messages_trace_outgoing_week is the count of distinct users which the particpant text to during the week.
     # messages_trace_incoming_week is the count of distinct users which the particpant recived a text message from during the week.

df_messages_trace_week=df_messages.copy()
df_messages_trace_week = df_messages_trace_week.groupby(["device_id",'message_type','trace'])["trace"].agg(["count"]).reset_index()
df_messages_trace_week = df_messages_trace_week.groupby(["device_id",'message_type'])["trace"].agg(["count"]).unstack(1).reset_index().fillna(0) #nulls replaced
df_messages_trace_week.columns = [''.join(str(col)) for col in df_messages_trace_week.columns.values]
df_messages_trace_week=df_messages_trace_week.rename(columns={"('device_id', '')":'device_id',"('count', 1)":'messages_trace_outgoing_week',"('count', 2)":'messages_trace_incoming_week','std':'messages_week_trace_std'})


# ------------------------------------------------
# ---------- Daily (24h) aggregated calc ---------
# ------------------------------------------------

# Calls

# 1) Calls_mean_incoming_24h is the average of occurrences of incoming calls during the week.
    # Calls_mean_outgoing_24h is the average of occurrences of outgoing calls during the week.
    # Calls_mean_missing_24h is the average of occurrences of missing calls during the week.
df_calls_24=pd.read_csv('MySQL_output\Calls_csv.csv')
df_num_calls_24 = df_calls_24.groupby(["device_id", "date",'call_type'])["call_type"].agg(["count"])
df_num_calls_24 = df_num_calls_24.groupby(["device_id",'call_type'])["count"].agg(["mean"]).unstack(1).reset_index().fillna(0) #nulls replaced with 0
df_num_calls_24.columns = [''.join(str(col)) for col in df_num_calls_24.columns.values]
df_num_calls_24=df_num_calls_24.rename(columns={"('device_id', '')":'device_id',"('mean', 1)":'Calls_mean_incoming_24h',"('mean', 2)":'Calls_mean_outgoing_24h',"('mean', 3)":'Calls_mean_missing_24h',"('median', 1)":'Calls_median_1',"('median', 2)":'Calls_median_2',"('median', 3)":'Calls_median_3'})

# 2) Calls_duration_mean_24h  is the average duration for a call excluding missing calls.
df_calls_duration_24=df_calls_week[df_calls_week["call_type"]!=3]
df_calls_duration_24 = df_calls_duration_24.groupby(["device_id", "date"])["call_duration"].agg(["mean"])
df_calls_duration_24 = df_calls_duration_24.groupby(["device_id"])["mean"].agg(["mean"]).reset_index().fillna(0) #nulls replaced with 0
df_calls_duration_24=df_calls_duration_24.rename(columns={"mean":'calls_duration_mean_24h',"median":'calls_duration_median',"std":'calls_duration_std'})

# 3)    # Calls_trace_mean_outgoing_24h is the average of distinct users which the participant call to.
        # Calls_trace_mean_incoming_24h is the average of distinct users which the participant recived a call from.
        # Calls_trace_mean_missing_24h is the average of distinct users which the participant recived a call and missed it.df_calls_trace_24=df_calls_week.copy()
df_calls_trace_24=df_calls_week.copy()
df_calls_trace_24 = df_calls_trace_24.groupby(["device_id", "date",'call_type','trace'])["trace"].agg(["count"]).reset_index()
df_calls_trace_24 = df_calls_trace_24.groupby(["device_id", "date",'call_type'])["trace"].agg(["count"])
df_calls_trace_24 = df_calls_trace_24.groupby(["device_id", 'call_type'])["count"].agg(["mean"]).unstack(1).reset_index().fillna(0) #nulls replaced
df_calls_trace_24.columns = [''.join(str(col)) for col in df_calls_trace_24.columns.values]
df_calls_trace_24=df_calls_trace_24.rename(columns={"('device_id', '')":'device_id',"('mean', 1)":'Calls_trace_mean_incoming_24h',"('mean', 2)":'Calls_trace_mean_outgoing_24h',"('mean', 3)":'Calls_trace_mean_missing_24h',"('median', 1)":'Calls_trace_median_1',"('median', 2)":'Calls_trace_median_2',"('median', 3)":'Calls_trace_median_3'})

# 4) Call_ratio_24h is the average of count of incoming calls divided by the count of all calls per day.
df_all_calls_24=df_calls_week.copy()
df_all_calls_24 = df_all_calls_24.groupby(["device_id", "date",'call_type'])['call_type'].agg(["sum"]).reset_index()
df_incoming_calls_24=df_all_calls_24[df_all_calls_24['call_type']==1].rename(columns={'sum':'incoming'})
df_count_total_calls_24=df_all_calls_24.groupby(["device_id","date"])['sum'].agg(["sum"]).reset_index().rename(columns={'sum':'all'})
df_calls_ratio_24= df_incoming_calls_24.merge(df_count_total_calls_24, how='right', on=['device_id',"date"]).fillna(0)
df_calls_ratio_24["Call_ratio"]=df_calls_ratio_24["incoming"]/df_calls_ratio_24["all"]
df_calls_ratio_24=df_calls_ratio_24.drop(['call_type', 'incoming','all'], axis=1)
df_calls_ratio_24 = df_calls_ratio_24.groupby(["device_id"])["Call_ratio"].agg(["mean"]).reset_index().rename(columns={'mean':'Call_ratio_24h'})

# Messages
# 1) #messages_mean_incoming_24h is the average of occurrences of incoming messages.
     #messages_mean_outgoing_24h is the average of occurrences of incoming messages.
df_messages_24=pd.read_csv('MySQL_output\Messages_csv.csv')
df_messages_num_24 = df_messages_24.groupby(["device_id", "date",'message_type'])['message_type'].agg(["count"])
df_messages_num_24 = df_messages_num_24.groupby(["device_id",'message_type'])['count'].agg(["mean"]).unstack(1).reset_index().fillna(0)
df_messages_num_24.columns = [''.join(str(col)) for col in df_messages_num_24.columns.values]
df_messages_num_24=df_messages_num_24.rename(columns={"('device_id', '')":'device_id',"('mean', 1)":'messages_mean_incoming_24h',"('mean', 2)":'messages_mean_outgoing_24h',"('mean', 3)":'messages_mean_3',"('median', 1)":'messages_median_1',"('median', 2)":'messages_median_2',"('median', 3)":'messages_median_3'})

# 2) # messages_trace_outgoing_24h is the average of distinct users which the participant text to.
     # messages_trace_incoming_24h is the average of distinct users which the participant recived a text message from.
df_messages_trace_24=df_messages_24.copy()
df_messages_trace_24 = df_messages_trace_24.groupby(["device_id", "date",'message_type','trace'])["trace"].agg(["count"]).reset_index()
df_messages_trace_24 = df_messages_trace_24.groupby(["device_id", "date",'message_type'])["trace"].agg(["count"])
df_messages_trace_24 = df_messages_trace_24.groupby(["device_id", 'message_type'])["count"].agg(["mean"]).unstack(1).reset_index().fillna(0) #nulls replaced
df_messages_trace_24.columns = [''.join(str(col)) for col in df_messages_trace_24.columns.values]
df_messages_trace_24=df_messages_trace_24.rename(columns={"('device_id', '')":'device_id',"('mean', 1)":'messages_trace_outgoing_24h',"('mean', 2)":'messages_trace_incoming_24h','std':'messages_trace_std'})


# ------------------------------------------------
# ------------ Final Screen table merge ----------
# ------------------------------------------------

df_aware_call_num=df_connectivity_screen_battery.merge(df_num_calls_week, how='left', on='device_id')

# fill Nulls with Feature Median
df_aware_call_num['Calls_count_incoming_week'] = df_aware_call_num['Calls_count_incoming_week'].fillna((df_aware_call_num['Calls_count_incoming_week'].median()))
df_aware_call_num['Calls_count_outgoing_week'] = df_aware_call_num['Calls_count_outgoing_week'].fillna((df_aware_call_num['Calls_count_outgoing_week'].median()))
df_aware_call_num['Calls_count_missing_week'] = df_aware_call_num['Calls_count_missing_week'].fillna((df_aware_call_num['Calls_count_missing_week'].median()))
df_aware_call_num_duration=df_aware_call_num.merge(df_calls_duration_week, how='left', on='device_id')

# fill Nulls with Feature Mean
df_aware_call_num_duration['calls_duration_mean_week'] = df_aware_call_num_duration['calls_duration_mean_week'].fillna((df_aware_call_num_duration['calls_duration_mean_week'].mean()))
df_aware_call_num_duration_trace=df_aware_call_num_duration.merge(df_calls_trace_week, how='left', on='device_id')
# fill Nulls with Feature Median
df_aware_call_num_duration_trace['Calls_trace_incoming_week'] = df_aware_call_num_duration_trace['Calls_trace_incoming_week'].fillna((df_aware_call_num_duration_trace['Calls_trace_incoming_week'].median()))
df_aware_call_num_duration_trace['Calls_trace_outgoing_week'] = df_aware_call_num_duration_trace['Calls_trace_outgoing_week'].fillna((df_aware_call_num_duration_trace['Calls_trace_outgoing_week'].median()))
df_aware_call_num_duration_trace['Calls_trace_missing_week'] = df_aware_call_num_duration_trace['Calls_trace_missing_week'].fillna((df_aware_call_num_duration_trace['Calls_trace_missing_week'].median()))

df_aware_call_num_duration_trace_ratio=df_aware_call_num_duration_trace.merge(df_calls_ratio_week, how='left', on='device_id')
# fill Nulls with Feature Median
df_aware_call_num_duration_trace_ratio['Call_ratio_week'] = df_aware_call_num_duration_trace_ratio['Call_ratio_week'].fillna((df_aware_call_num_duration_trace_ratio['Call_ratio_week'].median()))
df_calls_messages_num= df_aware_call_num_duration_trace_ratio.merge(df_messages_num_week, how='left', on='device_id')
# fill Nulls with Feature Median
df_calls_messages_num['messages_count_incoming_week'] = df_calls_messages_num['messages_count_incoming_week'].fillna((df_calls_messages_num['messages_count_incoming_week'].median()))
df_calls_messages_num['messages_count_outgoing_week'] = df_calls_messages_num['messages_count_outgoing_week'].fillna((df_calls_messages_num['messages_count_outgoing_week'].median()))
df_calls_messages_num_trace= df_calls_messages_num.merge(df_messages_trace_week, how='left', on='device_id')
# fill Nulls with Feature Median
df_calls_messages_num_trace['messages_trace_outgoing_week'] = df_calls_messages_num_trace['messages_trace_outgoing_week'].fillna((df_calls_messages_num_trace['messages_trace_outgoing_week'].median()))
df_calls_messages_num_trace['messages_trace_incoming_week'] = df_calls_messages_num_trace['messages_trace_incoming_week'].fillna((df_calls_messages_num_trace['messages_trace_incoming_week'].median()))

#Daily:
df_aware_call_num=df_calls_messages_num_trace.merge(df_num_calls_24, how='left', on='device_id')
# fill Nulls with Feature Median
df_aware_call_num['Calls_mean_incoming_24h'] = df_aware_call_num['Calls_mean_incoming_24h'].fillna((df_aware_call_num['Calls_mean_incoming_24h'].median()))
df_aware_call_num['Calls_mean_outgoing_24h'] = df_aware_call_num['Calls_mean_outgoing_24h'].fillna((df_aware_call_num['Calls_mean_outgoing_24h'].median()))
df_aware_call_num['Calls_mean_missing_24h'] = df_aware_call_num['Calls_mean_missing_24h'].fillna((df_aware_call_num['Calls_mean_missing_24h'].median()))
df_aware_call_num_duration=df_aware_call_num.merge(df_calls_duration_24, how='left', on='device_id')
# fill Nulls with Feature Mean
df_aware_call_num_duration['calls_duration_mean_24h'] = df_aware_call_num_duration['calls_duration_mean_24h'].fillna((df_aware_call_num_duration['calls_duration_mean_24h'].mean()))
df_aware_call_num_duration_trace=df_aware_call_num_duration.merge(df_calls_trace_24, how='left', on='device_id')
# fill Nulls with Feature Median
df_aware_call_num_duration_trace['Calls_trace_mean_incoming_24h'] = df_aware_call_num_duration_trace['Calls_trace_mean_incoming_24h'].fillna((df_aware_call_num_duration_trace['Calls_trace_mean_incoming_24h'].median()))
df_aware_call_num_duration_trace['Calls_trace_mean_outgoing_24h'] = df_aware_call_num_duration_trace['Calls_trace_mean_outgoing_24h'].fillna((df_aware_call_num_duration_trace['Calls_trace_mean_outgoing_24h'].median()))
df_aware_call_num_duration_trace['Calls_trace_mean_missing_24h'] = df_aware_call_num_duration_trace['Calls_trace_mean_missing_24h'].fillna((df_aware_call_num_duration_trace['Calls_trace_mean_missing_24h'].median()))
df_aware_call_num_duration_trace_ratio=df_aware_call_num_duration_trace.merge(df_calls_ratio_24, how='left', on='device_id')
# fill Nulls with Feature Median
df_aware_call_num_duration_trace_ratio['Call_ratio_24h'] = df_aware_call_num_duration_trace_ratio['Call_ratio_24h'].fillna((df_aware_call_num_duration_trace_ratio['Call_ratio_24h'].median()))
df_calls_messages_num= df_aware_call_num_duration_trace_ratio.merge(df_messages_num_24, how='left', on='device_id')
# fill Nulls with Feature Median
df_calls_messages_num['messages_mean_incoming_24h'] = df_calls_messages_num['messages_mean_incoming_24h'].fillna((df_calls_messages_num['messages_mean_incoming_24h'].median()))
df_calls_messages_num['messages_mean_outgoing_24h'] = df_calls_messages_num['messages_mean_outgoing_24h'].fillna((df_calls_messages_num['messages_mean_outgoing_24h'].median()))
df_calls_messages_num_trace= df_calls_messages_num.merge(df_messages_trace_24, how='left', on='device_id')
# fill Nulls with Feature Median
df_calls_messages_num_trace['messages_trace_outgoing_24h'] = df_calls_messages_num_trace['messages_trace_outgoing_24h'].fillna((df_calls_messages_num_trace['messages_trace_outgoing_24h'].median()))
df_calls_messages_num_trace['messages_trace_incoming_24h'] = df_calls_messages_num_trace['messages_trace_incoming_24h'].fillna((df_calls_messages_num_trace['messages_trace_incoming_24h'].median()))
df_connectivity_screen_battery_communication=df_calls_messages_num_trace.copy()


# ------------------------------------------------
# --------------- Outliers removal ---------------
# ------------------------------------------------

col = ['Bluetooth_count_week','wifi_count_week', 'Bluetooth_mean_24h','wifi_mean_24h',
       'screen_count_week', 'Screen_avg_time_week','screen_count_treshold_week','screen_count_mean_24','Screen_avg_time_24','screen_mean_treshold_24',
       'Battery_count_threshold_week','Battery_count_week','Battery_avg_threshold_24h','Battery_avg_24h',
       'Calls_count_incoming_week','Calls_count_outgoing_week','Calls_count_missing_week','calls_duration_mean_week','Calls_trace_incoming_week','Calls_trace_outgoing_week','Calls_trace_missing_week','Call_ratio_week',
        'Calls_mean_incoming_24h','Calls_mean_outgoing_24h','Calls_mean_missing_24h','calls_duration_mean_24h','Calls_trace_mean_incoming_24h','Calls_trace_mean_outgoing_24h','Calls_trace_mean_missing_24h','Call_ratio_24h']

"""
# Creating plot - with outliers
#plt.boxplot(df_aware_whatsapp_bluetooth_wifi[col])
# show plot
#plt.show()
"""

# IQR (Inter Quartile Range) Inter Quartile Range approach
df=df_connectivity_screen_battery_communication.copy()
Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)
IQR = Q3 - Q1
whisker_width = 1.5
lower_whisker = Q1 -(whisker_width*IQR)
lower_whisker =lower_whisker.where(lower_whisker>0, 0)
upper_whisker = Q3 + (whisker_width*IQR)
df[col] = np.where(df[col] > upper_whisker, df[col].median(),
            np.where(df[col] < lower_whisker, df[col].median(),df[col]))


# Creating plot - without outliers
#plt.boxplot(df[col])# show plot
#plt.show()

# ------------------------------------------------
# --------------- Scaling ----------------------
# ------------------------------------------------

col_with_mes = ['Bluetooth_count_week','wifi_count_week', 'Bluetooth_mean_24h','wifi_mean_24h',
       'screen_count_week', 'Screen_avg_time_week','screen_count_treshold_week','screen_count_mean_24','Screen_avg_time_24','screen_mean_treshold_24',
       'Battery_count_threshold_week','Battery_count_week','Battery_avg_threshold_24h','Battery_avg_24h',
       'Calls_count_incoming_week','Calls_count_outgoing_week','Calls_count_missing_week','calls_duration_mean_week','Calls_trace_incoming_week','Calls_trace_outgoing_week','Calls_trace_missing_week','Call_ratio_week',
        'messages_count_incoming_week','messages_count_outgoing_week','messages_trace_outgoing_week','messages_trace_incoming_week',
        'Calls_mean_incoming_24h','Calls_mean_outgoing_24h','Calls_mean_missing_24h','calls_duration_mean_24h','Calls_trace_mean_incoming_24h','Calls_trace_mean_outgoing_24h','Calls_trace_mean_missing_24h','Call_ratio_24h',
        'messages_mean_incoming_24h','messages_mean_outgoing_24h','messages_trace_outgoing_24h','messages_trace_incoming_24h']

# Zscore Scaling for features (based on smartphone data)
df_feature_zscore= z_score(df,col_with_mes)
#df_feature_zscore.to_csv('Data_processing_output\FINAL_zscore.csv',index=False)

# ------------------------------------------------
# --------------- cols ----------------
# ------------------------------------------------

#every value in "manufacturer" column that is not C0 ,classify as others
df_data=df_feature_zscore.copy()
a=[]
for i in df_data["manufacturer"].values[:]:
    if i not in a:
        a.append(i)

a.remove("samsung")
a.remove("Xiaomi")
df_data["manufacturer"]=df_data["manufacturer"].replace(a,"other")
df_data["manufacturer"].value_counts()[:].plot(kind='bar',figsize =(16,4))
#plt.show()

df_data=df_data.drop(['Email','Unnamed: 0'], axis=1)
df_data.to_csv('Data_processing_output\Processed_data.csv',index=False)