import pandas as pd
from data_instruments import Instruments
from awigen_skip_logic import SkipLogic

if __name__ == '__main__':
    # Create a Pandas Excel writer using XlsxWriter as the engine.

    phase1 = pd.read_csv("C:/Users/A0072059/Documents/Awigen1/all_sites_20_12_22.txt", sep=',')

    writer = pd.ExcelWriter('awigen_data_val.xlsx', engine='xlsxwriter')

    # hypertension_without encodings
    hypertension = []
    hypertension_col = ['hypertension_qc', 'hypertension_12months_yn_qc', 'hypertension_meds_yn_qc',
                'hypertension_treatment_yn_qc', 'hypertension_traditional_qc', 'h_blood_pressure_mom_qc',
                'h_blood_pressure_dad_qc']

    for col in hypertension_col:
        df = phase1.groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        hypertension.append(df.T)

    hypertension[0].to_excel(writer, sheet_name='hypertension')
    hypertension[1].to_excel(writer, sheet_name='hypertension', startrow=7)
    hypertension[2].to_excel(writer, sheet_name='hypertension', startrow=14)
    hypertension[3].to_excel(writer, sheet_name='hypertension', startrow=21)
    hypertension[4].to_excel(writer, sheet_name='hypertension', startrow=28)
    hypertension[5].to_excel(writer, sheet_name='hypertension', startrow=35)
    hypertension[6].to_excel(writer, sheet_name='hypertension', startrow=42)

    # hypertension
    hypertension_encoded = []
    for col in hypertension_col:
        df = SkipLogic(phase1).hypertension_skip_logic().groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        hypertension_encoded.append(df.T)

    hypertension_encoded[0].to_excel(writer, sheet_name='hypertension', startcol=12)
    hypertension_encoded[1].to_excel(writer, sheet_name='hypertension', startrow=7, startcol=12)
    hypertension_encoded[2].to_excel(writer, sheet_name='hypertension', startrow=14, startcol=12)
    hypertension_encoded[3].to_excel(writer, sheet_name='hypertension', startrow=21, startcol=12)
    hypertension_encoded[4].to_excel(writer, sheet_name='hypertension', startrow=28, startcol=12)
    hypertension_encoded[5].to_excel(writer, sheet_name='hypertension', startrow=35, startcol=12)
    hypertension_encoded[6].to_excel(writer, sheet_name='hypertension', startrow=42, startcol=12)


    # diabetes
    diabetes = []
    diabetes_col = ['diabetes_qc', 'diabetes_12months_qc', 'diabetes_treatment_qc', 'diabetes_treat_pills_qc',
                    'diabetes_treat_insulin_qc', 'diabetes_treat_weight_loss_qc', 'diabetes_treat_diet_qc',
                    'blood_sugar_qc', 'diabetes_history_qc', 'mother_diabetes_qc', 'father_diabetes_qc']

    for col in diabetes_col:
        df = phase1.groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        diabetes.append(df.T)

    diabetes[0].to_excel(writer, sheet_name='diabetes')
    diabetes[1].to_excel(writer, sheet_name='diabetes', startrow=6)
    diabetes[2].to_excel(writer, sheet_name='diabetes', startrow=13)
    diabetes[3].to_excel(writer, sheet_name='diabetes', startrow=20)
    diabetes[4].to_excel(writer, sheet_name='diabetes', startrow=27)
    diabetes[5].to_excel(writer, sheet_name='diabetes', startrow=34)
    diabetes[6].to_excel(writer, sheet_name='diabetes', startrow=41)
    diabetes[7].to_excel(writer, sheet_name='diabetes', startrow=49)
    diabetes[8].to_excel(writer, sheet_name='diabetes', startrow=56)
    diabetes[9].to_excel(writer, sheet_name='diabetes', startrow=63)
    diabetes[10].to_excel(writer, sheet_name='diabetes', startrow=70)

    # diabetes_encoded
    diabetes_encoded = []

    for col in diabetes_col:
        df = SkipLogic(phase1).diabetes_skip_logic().groupby('site')[col].value_counts(
            dropna=False).to_frame().unstack()
        diabetes_encoded.append(df.T)

    diabetes_encoded[0].to_excel(writer, sheet_name='diabetes', startcol=12 )
    diabetes_encoded[1].to_excel(writer, sheet_name='diabetes', startrow=6, startcol=12)
    diabetes_encoded[2].to_excel(writer, sheet_name='diabetes', startrow=13, startcol=12)
    diabetes_encoded[3].to_excel(writer, sheet_name='diabetes', startrow=20, startcol=12)
    diabetes_encoded[4].to_excel(writer, sheet_name='diabetes', startrow=27, startcol=12)
    diabetes_encoded[5].to_excel(writer, sheet_name='diabetes', startrow=34, startcol=12)
    diabetes_encoded[6].to_excel(writer, sheet_name='diabetes', startrow=41, startcol=12)
    diabetes_encoded[7].to_excel(writer, sheet_name='diabetes', startrow=49, startcol=12)
    diabetes_encoded[8].to_excel(writer, sheet_name='diabetes', startrow=56, startcol=12)
    diabetes_encoded[9].to_excel(writer, sheet_name='diabetes', startrow=63, startcol=12)
    diabetes_encoded[10].to_excel(writer, sheet_name='diabetes', startrow=70, startcol=12)

    #tobacco

    tobacco = []
    tobac_col = ['tobacco_use_qc', 'current_smoker_qc', 'smokeless_tobacco_use_qc']

    for col in tobac_col:
        df = phase1.groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        tobacco.append(df.T)

    tobacco[0].to_excel(writer, sheet_name='tobacco')
    tobacco[1].to_excel(writer, sheet_name='tobacco', startrow=6)
    tobacco[2].to_excel(writer, sheet_name='tobacco', startrow=16)

    #tobbacco encoded
    tob_encoded = []
    for col in tobac_col:
        df = SkipLogic(phase1).tobbaco_skip_logic().groupby('site')[col].value_counts(
            dropna=False).to_frame().unstack()
        tob_encoded.append(df.T)

    tob_encoded[0].to_excel(writer, sheet_name='tobacco', startcol=12)
    tob_encoded[1].to_excel(writer, sheet_name='tobacco', startrow=6, startcol=12)
    tob_encoded[2].to_excel(writer, sheet_name='tobacco', startrow=16, startcol=12)


    # angina
    angina = []
    angina_col = ['angina_qc', 'angina_treatment_yn_qc', 'angina_treat_now_qc', 'angina_traditional_qc']

    for col in angina_col:
        df = phase1.groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        angina.append(df.T)

    angina[0].to_excel(writer, sheet_name='angina')
    angina[1].to_excel(writer, sheet_name='angina', startrow=7)
    angina[2].to_excel(writer, sheet_name='angina', startrow=14)
    angina[3].to_excel(writer, sheet_name='angina', startrow=21)


    # angina_encoded
    angina_encoded = []

    for col in angina_col:
        df = SkipLogic(phase1).angina_skip_logic().groupby('site')[col].value_counts(
            dropna=False).to_frame().unstack()
        angina_encoded.append(df.T)

    angina_encoded[0].to_excel(writer, sheet_name='angina', startcol=12)
    angina_encoded[1].to_excel(writer, sheet_name='angina', startrow=7, startcol=12)
    angina_encoded[2].to_excel(writer, sheet_name='angina', startrow=14, startcol=12)
    angina_encoded[3].to_excel(writer, sheet_name='angina', startrow=21, startcol=12)

    # hrt failure
    heart_failure = []
    hrt_col = ['congestive_heart_failure_qc', 'chf_treatment_yn_qc', 'chf_treat_now_qc', 'chf_traditional_qc',
                'heartattack_qc', 'heartattack_treatment_qc', 'heartattack_traditional_qc']

    for col in hrt_col:
        df = phase1.groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        heart_failure.append(df.T)

    heart_failure[0].to_excel(writer, sheet_name='heart_failure')
    heart_failure[1].to_excel(writer, sheet_name='heart_failure', startrow=7)
    heart_failure[2].to_excel(writer, sheet_name='heart_failure', startrow=14)
    heart_failure[3].to_excel(writer, sheet_name='heart_failure', startrow=21)
    heart_failure[4].to_excel(writer, sheet_name='heart_failure', startrow=28)
    heart_failure[5].to_excel(writer, sheet_name='heart_failure', startrow=35)
    heart_failure[6].to_excel(writer, sheet_name='heart_failure', startrow=42)

    # angina_encoded
    heartfailure_encoded = []

    for col in hrt_col:
        df = SkipLogic(phase1).hrt_skip_logic().groupby('site')[col].value_counts(
            dropna=False).to_frame().unstack()
        heartfailure_encoded.append(df.T)

    heartfailure_encoded[0].to_excel(writer, sheet_name='heart_failure', startcol=12)
    heartfailure_encoded[1].to_excel(writer, sheet_name='heart_failure', startrow=7, startcol=12)
    heartfailure_encoded[2].to_excel(writer, sheet_name='heart_failure', startrow=14, startcol=12)
    heartfailure_encoded[3].to_excel(writer, sheet_name='heart_failure', startrow=21, startcol=12)
    heartfailure_encoded[4].to_excel(writer, sheet_name='heart_failure', startrow=28, startcol=12)
    heartfailure_encoded[5].to_excel(writer, sheet_name='heart_failure', startrow=35, startcol=12)
    heartfailure_encoded[6].to_excel(writer, sheet_name='heart_failure', startrow=42, startcol=12)

    # alcohol
    alcohol = []
    alco_col = ['consume_alcohol_qc', 'current_alcohol_consumer_qc', 'alcohol_type_consumed_beer_qc',
                'frequence_of_alcohol_consumption', 'amount_of_alcohol_consumed_per_day_qc',
                'drinking_past_year_qc', 'had_hangover_qc', 'consider_alcohol_cutdown_qc', 'use_drug_qc']

    for col in alco_col:
        df = phase1.groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        alcohol.append(df.T)

    alcohol[0].to_excel(writer, sheet_name='alcohol')
    alcohol[1].to_excel(writer, sheet_name='alcohol', startrow=7)
    alcohol[2].to_excel(writer, sheet_name='alcohol', startrow=14)
    alcohol[3].to_excel(writer, sheet_name='alcohol', startrow=21)
    alcohol[4].to_excel(writer, sheet_name='alcohol', startrow=30)
    alcohol[5].to_excel(writer, sheet_name='alcohol', startrow=147)
    alcohol[6].to_excel(writer, sheet_name='alcohol', startrow=154)
    alcohol[7].to_excel(writer, sheet_name='alcohol', startrow=163)
    alcohol[8].to_excel(writer, sheet_name='alcohol', startrow=170)

    # alcohol_encoded
    alcohol_encoded = []

    for col in alco_col:
        df = SkipLogic(phase1).alco_skip_logic().groupby('site')[col].value_counts(
            dropna=False).to_frame().unstack()
        alcohol_encoded.append(df.T)

    alcohol_encoded[0].to_excel(writer, sheet_name='alcohol', startcol=12)
    alcohol_encoded[1].to_excel(writer, sheet_name='alcohol', startrow=7, startcol=12)
    alcohol_encoded[2].to_excel(writer, sheet_name='alcohol', startrow=14, startcol=12)
    alcohol_encoded[3].to_excel(writer, sheet_name='alcohol', startrow=21, startcol=12)
    alcohol_encoded[4].to_excel(writer, sheet_name='alcohol', startrow=30, startcol=12)
    alcohol_encoded[5].to_excel(writer, sheet_name='alcohol', startrow=147, startcol=12)
    alcohol_encoded[6].to_excel(writer, sheet_name='alcohol', startrow=154, startcol=12)
    alcohol_encoded[7].to_excel(writer, sheet_name='alcohol', startrow=163, startcol=12)
    alcohol_encoded[8].to_excel(writer, sheet_name='alcohol', startrow=170, startcol=12)

    # chol
    chol = []
    chol_col = ['h_cholesterol_qc', 'cholesterol_treatment_qc', 'cholesterol_traditional_qc',
                'cholesterol_meds_weight_loss_qc', 'cholesterol_meds_special_diet_qc', 'h_cholesterol_mom_qc',
                'h_cholesterol_dad_qc']

    for col in chol_col:
        df = phase1.groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        chol.append(df.T)

    chol[0].to_excel(writer, sheet_name='chol')
    chol[1].to_excel(writer, sheet_name='chol', startrow=7)
    chol[2].to_excel(writer, sheet_name='chol', startrow=14)
    chol[3].to_excel(writer, sheet_name='chol', startrow=21)
    chol[4].to_excel(writer, sheet_name='chol', startrow=30)
    chol[5].to_excel(writer, sheet_name='chol', startrow=41)
    chol[6].to_excel(writer, sheet_name='chol', startrow=50)

    # angina_encoded
    chol_encoded = []

    for col in chol_col:
        df = SkipLogic(phase1).chol_skip_logic().groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        chol_encoded.append(df.T)

    chol_encoded[0].to_excel(writer, sheet_name='chol', startcol=12)
    chol_encoded[1].to_excel(writer, sheet_name='chol', startrow=7, startcol=12)
    chol_encoded[2].to_excel(writer, sheet_name='chol', startrow=14, startcol=12)
    chol_encoded[3].to_excel(writer, sheet_name='chol', startrow=21, startcol=12)
    chol_encoded[4].to_excel(writer, sheet_name='chol', startrow=30, startcol=12)
    chol_encoded[5].to_excel(writer, sheet_name='chol', startrow=41, startcol=12)
    chol_encoded[6].to_excel(writer, sheet_name='chol', startrow=50, startcol=12)

    # physical_act
    physical_act = []
    physical_act_col = ['work_vigorous', 'work_vigorous_days', 'work_vigorous_hours', 'work_vigorous_minutes', 'work_moderate',
                'work_moderate_days', 'work_moderate_hours', 'work_moderate_mins', 'transport_physical',
                'transport_physical_days', 'transport_physical_hours', 'transport_physical_mins', 'leisure_physical',
                'leisure_vigorous_days', 'leisure_vigorous_hours', 'leisure_vigorous_mins', 'leisure_moderate',
                'leisure_moderate_days', 'leisure_moderate_hours', 'sitting_hours', 'sitting_work_mins']

    for col in physical_act_col:
        df = phase1.groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        physical_act.append(df.T)

    physical_act[0].to_excel(writer, sheet_name='physical_activity')
    physical_act[1].to_excel(writer, sheet_name='physical_activity', startrow=7)
    physical_act[2].to_excel(writer, sheet_name='physical_activity', startrow=20)
    physical_act[3].to_excel(writer, sheet_name='physical_activity', startrow=50)
    physical_act[4].to_excel(writer, sheet_name='physical_activity', startrow=64)
    physical_act[5].to_excel(writer, sheet_name='physical_activity', startrow=71)
    physical_act[6].to_excel(writer, sheet_name='physical_activity', startrow=84)
    physical_act[7].to_excel(writer, sheet_name='physical_activity', startrow=138)
    physical_act[8].to_excel(writer, sheet_name='physical_activity', startrow=161)
    physical_act[9].to_excel(writer, sheet_name='physical_activity', startrow=167)
    physical_act[10].to_excel(writer, sheet_name='physical_activity', startrow=180)
    physical_act[11].to_excel(writer, sheet_name='physical_activity', startrow=233)
    physical_act[12].to_excel(writer, sheet_name='physical_activity', startrow=264)
    physical_act[13].to_excel(writer, sheet_name='physical_activity', startrow=270)
    physical_act[14].to_excel(writer, sheet_name='physical_activity', startrow=283)
    physical_act[15].to_excel(writer, sheet_name='physical_activity', startrow=319)
    physical_act[16].to_excel(writer, sheet_name='physical_activity', startrow=340)
    physical_act[17].to_excel(writer, sheet_name='physical_activity', startrow=347)
    physical_act[18].to_excel(writer, sheet_name='physical_activity', startrow=360)
    physical_act[19].to_excel(writer, sheet_name='physical_activity', startrow=398)
    physical_act[20].to_excel(writer, sheet_name='physical_activity', startrow=1614)


    # angina_encoded
    physical_act_encoded = []

    for col in physical_act_col:
        df = SkipLogic(phase1).phy_activity_skip_logic().groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        physical_act_encoded.append(df.T)

    physical_act_encoded[0].to_excel(writer, sheet_name='physical_activity', startcol=12)
    physical_act_encoded[1].to_excel(writer, sheet_name='physical_activity', startrow=7, startcol=12)
    physical_act_encoded[2].to_excel(writer, sheet_name='physical_activity', startrow=20, startcol=12)
    physical_act_encoded[3].to_excel(writer, sheet_name='physical_activity', startrow=50, startcol=12)
    physical_act_encoded[4].to_excel(writer, sheet_name='physical_activity', startrow=64, startcol=12)
    physical_act_encoded[5].to_excel(writer, sheet_name='physical_activity', startrow=71, startcol=12)
    physical_act_encoded[6].to_excel(writer, sheet_name='physical_activity', startrow=84, startcol=12)
    physical_act_encoded[7].to_excel(writer, sheet_name='physical_activity', startrow=138, startcol=12)
    physical_act_encoded[8].to_excel(writer, sheet_name='physical_activity', startrow=161, startcol=12)
    physical_act_encoded[9].to_excel(writer, sheet_name='physical_activity', startrow=167, startcol=12)
    physical_act_encoded[10].to_excel(writer, sheet_name='physical_activity', startrow=180, startcol=12)
    physical_act_encoded[11].to_excel(writer, sheet_name='physical_activity', startrow=233, startcol=12)
    physical_act_encoded[12].to_excel(writer, sheet_name='physical_activity', startrow=264, startcol=12)
    physical_act_encoded[13].to_excel(writer, sheet_name='physical_activity', startrow=270, startcol=12)
    physical_act_encoded[14].to_excel(writer, sheet_name='physical_activity', startrow=283, startcol=12)
    physical_act_encoded[15].to_excel(writer, sheet_name='physical_activity', startrow=319, startcol=12)
    physical_act_encoded[16].to_excel(writer, sheet_name='physical_activity', startrow=340, startcol=12)
    physical_act_encoded[17].to_excel(writer, sheet_name='physical_activity', startrow=347, startcol=12)
    physical_act_encoded[18].to_excel(writer, sheet_name='physical_activity', startrow=360, startcol=12)
    physical_act_encoded[19].to_excel(writer, sheet_name='physical_activity', startrow=398, startcol=12)
    physical_act_encoded[20].to_excel(writer, sheet_name='physical_activity', startrow=1614, startcol=12)

    # kidney
    kidney = []
    kidney_col = ['low_kidney_function_qc', 'kidney_disease_qc', 'kidney_family_qc', 'family_kidney_mother_qc',
                'family_kidney_father_qc', 'family_kidney_other_qc']

    for col in kidney_col:
        df = phase1.groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        kidney.append(df.T)

    kidney[0].to_excel(writer, sheet_name='kidney')
    kidney[1].to_excel(writer, sheet_name='kidney', startrow=7)
    kidney[2].to_excel(writer, sheet_name='kidney', startrow=14)
    kidney[3].to_excel(writer, sheet_name='kidney', startrow=21)
    kidney[4].to_excel(writer, sheet_name='kidney', startrow=30)
    kidney[5].to_excel(writer, sheet_name='kidney', startrow=41)


    # kidney_encoded
    kidney_encoded = []

    for col in kidney_col:
        df = SkipLogic(phase1).kidney_skip_logic().groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        kidney_encoded.append(df.T)

    kidney_encoded[0].to_excel(writer, sheet_name='kidney', startcol=12)
    kidney_encoded[1].to_excel(writer, sheet_name='kidney', startrow=7, startcol=12)
    kidney_encoded[2].to_excel(writer, sheet_name='kidney', startrow=14, startcol=12)
    kidney_encoded[3].to_excel(writer, sheet_name='kidney', startrow=21, startcol=12)
    kidney_encoded[4].to_excel(writer, sheet_name='kidney', startrow=30, startcol=12)
    kidney_encoded[5].to_excel(writer, sheet_name='kidney', startrow=41, startcol=12)

    # hiv
    hiv = []
    hiv_col = ['tested_hiv', 'hiv_positive_qc', 'hiv_final_status_c', 'hiv_medication_qc', 'traditional_med_hiv']

    for col in hiv_col:
        df = phase1.groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        hiv.append(df.T)

    hiv[0].to_excel(writer, sheet_name='hiv')
    hiv[1].to_excel(writer, sheet_name='hiv', startrow=7)
    hiv[2].to_excel(writer, sheet_name='hiv', startrow=14)
    hiv[3].to_excel(writer, sheet_name='hiv', startrow=21)
    hiv[4].to_excel(writer, sheet_name='hiv', startrow=30)


    # hiv_encoded
    hiv_encoded = []

    for col in hiv_col:
        df = SkipLogic(phase1).hiv_skip_logic().groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        hiv_encoded.append(df.T)

    hiv_encoded[0].to_excel(writer, sheet_name='hiv', startcol=12)
    hiv_encoded[1].to_excel(writer, sheet_name='hiv', startrow=7, startcol=12)
    hiv_encoded[2].to_excel(writer, sheet_name='hiv', startrow=14, startcol=12)
    hiv_encoded[3].to_excel(writer, sheet_name='hiv', startrow=21, startcol=12)
    hiv_encoded[4].to_excel(writer, sheet_name='hiv', startrow=30, startcol=12)

    # tb
    tb = []
    tb_col = ['tb_qc', 'tb_12months_qc', 'tb_treatment_qc', 'tb_meds_qc', 'tb_traditional_med_qc', 'tb_counselling_qc']

    for col in tb_col:
        df = phase1.groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        tb.append(df.T)

    tb[0].to_excel(writer, sheet_name='tb')
    tb[1].to_excel(writer, sheet_name='tb', startrow=7)
    tb[2].to_excel(writer, sheet_name='tb', startrow=14)
    tb[3].to_excel(writer, sheet_name='tb', startrow=21)
    tb[4].to_excel(writer, sheet_name='tb', startrow=30)
    tb[5].to_excel(writer, sheet_name='tb', startrow=37)

    # tb_encoded
    tb_encoded = []

    for col in tb_col:
        df = SkipLogic(phase1).tb_skip_logic().groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        tb_encoded.append(df.T)

    tb_encoded[0].to_excel(writer, sheet_name='tb', startcol=12)
    tb_encoded[1].to_excel(writer, sheet_name='tb', startrow=7, startcol=12)
    tb_encoded[2].to_excel(writer, sheet_name='tb', startrow=14, startcol=12)
    tb_encoded[3].to_excel(writer, sheet_name='tb', startrow=21, startcol=12)
    tb_encoded[4].to_excel(writer, sheet_name='tb', startrow=30, startcol=12)
    tb_encoded[5].to_excel(writer, sheet_name='tb', startrow=37, startcol=12)


    # malaria
    malaria = []
    malaria_col = ['malaria_qc', 'malaria_month_qc']

    for col in malaria_col:
        df = phase1.groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        malaria.append(df.T)

    malaria[0].to_excel(writer, sheet_name='malaria')
    malaria[1].to_excel(writer, sheet_name='malaria', startrow=7)

    # malaria_encoded
    malaria_encoded = []

    for col in malaria_col:
        df = SkipLogic(phase1).malaria_skip_logic().groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        malaria_encoded.append(df.T)

    malaria_encoded[0].to_excel(writer, sheet_name='malaria', startcol=12)
    malaria_encoded[1].to_excel(writer, sheet_name='malaria', startrow=7, startcol=12)

    # malaria
    pesticide = []
    pesticide_col = ['pesticide_qc', 'region_pesticide_qc']

    for col in pesticide_col:
        df = phase1.groupby('site')[col].value_counts(dropna=False).to_frame().unstack()
        pesticide.append(df.T)

    pesticide[0].to_excel(writer, sheet_name='pesticide')
    pesticide[1].to_excel(writer, sheet_name='pesticide', startrow=7)
writer.save()

