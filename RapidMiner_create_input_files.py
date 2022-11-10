# This file creates Excel inputs for Rapid Miner Auto Model
import numpy as np
import pandas as pd

data=pd.read_csv('Data_processing_output\Processed_data.csv')

cols=['Explorer_Rank', 'Builder_Rank', 'Director_Rank', 'Negotiator_Rank',  'Secure_attachment', 'Anxious-preoccupied_attachment', 'Fearful-avoidant_attachment', 'Dismissive–avoidant_attachment', 'FFM_Extraversion', 'FFM_Agreeableness', 'FFM_Concientiousness', 'FFM_Neurotism', 'FFM_Openess', 'Machiavellianism', 'Narcissism', 'Psychopathy',
       'Dark_Triad_Compounded', 'RTB-Final_Score',  'Ambiguous_stimuli_in_general_(G)', 'Complex_stimuli_(C)', 'Uncertain_stimuli_(U)', 'Novel_stimuli_(N)', 'Insoluble/illogical/irreducible/internally_inconsistent_stimuli_(I)', 'TFA_SUM', 'TFA_(Tolerance_for_Ambiguity)_Score', 'Self_Efficacy', 'Self-Discipline', 'Tolerance', 'Absorption', 'Appraisal', 'Regulation',
       'Distress_Tolrance_Final', 'Creativity_bricolage', 'Pressure_stress', 'Action_persistence', 'Improvisation_capacity_Final', 'Creativity_Compound_Score_(IPIP)', 'Locus_of_Control', 'Self-emotion_appraisal_(SEA)', 'Others’_emotion_appraisal_(OEA)', 'Use_of_emotion_(UOE)', 'Regulation_of_emotion_(ROE)', 'ESI_Compund_Score', 'Social_Desirabilty_Score',
       'ERM-__Physical_Endurance', 'TMM-_Physical_Tempo', 'SS-_Risk_Seeking', 'ERS-_Social_Endurance', 'TMS-_Social_Tempo', 'EMP-_Empathy', 'ERI-_Intellectual_Endurance', 'PL-_Plasticity', 'PRO-_Probab_thinking', 'SLF-_Self-confidence', 'IMP-__Impulsivity', 'NEU-_Neuroticism',
       'CNTL-_Social_desirability_tendency_for_STQ-77_(15-20_demonstrate_high_Social_Desirablity_and_may_be_discarded_at_your_discression)', 'V_STD-_Self-direction_Thought', 'V_SDA-_Self-direction_Action', 'V_ST-_Stimulation', 'V_HE-_Hedonism', 'V_AC-_Achievement', 'V_POR-_Power_Dominance', 'V_POD-_Power_Resources', 'V_FAC-_Face', 'V_SEP-_Security_Personal', 'V_SES-_Security_Societal',
       'V_TR-_Tradition', 'V_COR-_Conformity-Rules', 'V_COI-_Conformity-Interpersonal', 'V_HU-_Humility', 'V_UNN-_Universalism-Nature', 'V_UNC-_Universalism-Concern', 'V_UNT-_Universalism-Tolerance', 'V_BEC-_Benevolence_–Care', 'V_BED-_Benevolence-Dependability',
        'Age', 'Gender','Family Status', 'Education','Employment Type', 'device_id', 'manufacturer']
traits_labels=['Explorer_Rank', 'Builder_Rank', 'Director_Rank', 'Negotiator_Rank',  'Secure_attachment', 'Anxious-preoccupied_attachment', 'Fearful-avoidant_attachment', 'Dismissive–avoidant_attachment', 'FFM_Extraversion', 'FFM_Agreeableness', 'FFM_Concientiousness', 'FFM_Neurotism', 'FFM_Openess', 'Machiavellianism', 'Narcissism', 'Psychopathy',
       'Dark_Triad_Compounded', 'RTB-Final_Score',  'Ambiguous_stimuli_in_general_(G)', 'Complex_stimuli_(C)', 'Uncertain_stimuli_(U)', 'Novel_stimuli_(N)', 'Internally_inconsistent_stimuli_(I)', 'TFA_SUM', 'TFA_(Tolerance_for_Ambiguity)_Score', 'Self_Efficacy', 'Self-Discipline', 'Tolerance', 'Absorption', 'Appraisal', 'Regulation',
       'Distress_Tolrance_Final', 'Creativity_bricolage', 'Pressure_stress', 'Action_persistence', 'Improvisation_capacity_Final', 'Creativity_Compound_Score_(IPIP)', 'Locus_of_Control', 'Self-emotion_appraisal_(SEA)', 'Others’_emotion_appraisal_(OEA)', 'Use_of_emotion_(UOE)', 'Regulation_of_emotion_(ROE)', 'ESI_Compund_Score', 'Social_Desirabilty_Score',
       'ERM-__Physical_Endurance', 'TMM-_Physical_Tempo', 'SS-_Risk_Seeking', 'ERS-_Social_Endurance', 'TMS-_Social_Tempo', 'EMP-_Empathy', 'ERI-_Intellectual_Endurance', 'PL-_Plasticity', 'PRO-_Probab_thinking', 'SLF-_Self-confidence', 'IMP-__Impulsivity', 'NEU-_Neuroticism',
       'CNTL-_Social_desirability_tendency', 'V_STD-_Self-direction_Thought', 'V_SDA-_Self-direction_Action', 'V_ST-_Stimulation', 'V_HE-_Hedonism', 'V_AC-_Achievement', 'V_POR-_Power_Dominance', 'V_POD-_Power_Resources', 'V_FAC-_Face', 'V_SEP-_Security_Personal', 'V_SES-_Security_Societal',
       'V_TR-_Tradition', 'V_COR-_Conformity-Rules', 'V_COI-_Conformity-Interpersonal', 'V_HU-_Humility', 'V_UNN-_Universalism-Nature', 'V_UNC-_Universalism-Concern', 'V_UNT-_Universalism-Tolerance', 'V_BEC-_Benevolence_–Care', 'V_BED-_Benevolence-Dependability']
smartphone_features = ['Bluetooth_count_week','wifi_count_week', 'Bluetooth_mean_24h','wifi_mean_24h',
       'screen_count_week', 'Screen_avg_time_week','screen_count_treshold_week','screen_count_mean_24','Screen_avg_time_24','screen_mean_treshold_24',
       'Battery_count_threshold_week','Battery_count_week','Battery_avg_threshold_24h','Battery_avg_24h',
       'Calls_count_incoming_week','Calls_count_outgoing_week','Calls_count_missing_week','calls_duration_mean_week','Calls_trace_incoming_week','Calls_trace_outgoing_week','Calls_trace_missing_week','Call_ratio_week',
        'messages_count_incoming_week','messages_count_outgoing_week','messages_trace_outgoing_week','messages_trace_incoming_week',
        'Calls_mean_incoming_24h','Calls_mean_outgoing_24h','Calls_mean_missing_24h','calls_duration_mean_24h','Calls_trace_mean_incoming_24h','Calls_trace_mean_outgoing_24h','Calls_trace_mean_missing_24h','Call_ratio_24h',
        'messages_mean_incoming_24h','messages_mean_outgoing_24h','messages_trace_outgoing_24h','messages_trace_incoming_24h']
Control_variables=['Age', 'Gender','Family Status', 'Education','Employment Type', 'device_id', 'manufacturer']

data2=data.copy()
data2=data2.rename(columns={'New/unfamiliar/novel_stimuli_(N)':'Novel_stimuli_(N)','Insoluble/illogical/irreducible/internally_inconsistent_stimuli_(I)':'Internally_inconsistent_stimuli_(I)','CNTL-_Social_desirability_tendency_for_STQ-77_(15-20_demonstrate_high_Social_Desirablity_and_may_be_discarded_at_your_discression)':'CNTL-_Social_desirability_tendency'})

for trait in traits_labels:
    print(trait)
    features=data2[smartphone_features]
    label=data2[trait]
    df= pd.concat([label,features], axis=1, sort=False)
    df.to_csv(f'Data_processing_output\RapidMiner_input_{trait} .csv', index=True)
