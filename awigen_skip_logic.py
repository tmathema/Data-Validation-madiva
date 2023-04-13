import pandas as pd
from data_instruments import Instruments

class SkipLogic:
    def __init__(self, data):
        self.data = data

    def gender_specific_skip_logic(self):
        gender_spe_col = ['number_of_pregnancies_qc', 'number_of_live_births_qc', 'breast_cancer_qc', 'cervical_cancer_qc',
                          'prostate_cancer_qc']

        for col in gender_spe_col:
            if col in ['number_of_pregnancies_qc', 'number_of_live_births_qc', 'breast_cancer_qc', 'cervical_cancer_qc']:
                mask = (self.data[col].isna() & (self.data['sex'] == 1))
                self.data[col] = self.data[col].mask(mask, -555)
            if col in ['prostate_cancer_qc']:
                mask = (self.data[col].isna() & (self.data['sex'] == 0))
                self.data[col] = self.data[col].mask(mask, -555)
        return self.data

    def hypertension_skip_logic(self):
        hypertension_col = ['hypertension_qc', 'hypertension_12months_yn_qc', 'hypertension_meds_yn_qc',
                            'hypertension_treatment_yn_qc']

        for col in hypertension_col:
            if col in ['hypertension_treatment_yn_qc', 'hypertension_meds_yn_qc']:
                mask = (self.data[col].isna() & ((self.data['hypertension_qc']==0)| (self.data['hypertension_qc']==2)))
                self.data[col] = self.data[col].mask(mask, -555)
            if col in ['hypertension_12months_yn_qc']:
                mask = ((self.data[col]==-999) & ((self.data['hypertension_qc']==0) | (self.data['hypertension_qc']==2)))
                self.data[col] = self.data[col].mask(mask, -555)
        return self.data

    def diabetes_skip_logic(self):
        diabetes_col = ['diabetes_qc', 'diabetes_12months_qc', 'diabetes_treatment_qc', 'diabetes_treat_curr_qc',
                        'diabetes_treat_pills_qc',
                        'diabetes_treat_insulin', 'diabetes_treat_weight_loss_qc', 'diabetes_treat_diet_qc',
                        'diabetes_history_qc', 'mother_diabetes_qc', 'father_diabetes_qc']

        for col in diabetes_col:
            if col in ['diabetes_12months_qc', 'diabetes_treatment_qc', 'diabetes_treat_curr_qc']:
                mask = (self.data[col].isna() & ((self.data['diabetes_qc'] == 0)| (self.data['diabetes_qc']==2)))
                self.data[col] = self.data[col].mask(mask, -555)
            if col in ['diabetes_treat_pills_qc', 'diabetes_treat_insulin_qc', 'diabetes_treat_weight_loss_qc', 'diabetes_treat_diet_qc' ]:
                mask = ((self.data[col]==0) & ((self.data['diabetes_treat_curr_qc']==0) | (self.data['diabetes_treat_curr_qc']==2)|
                                                            (self.data['diabetes_treat_curr_qc']==-555)))
                self.data[col] = self.data[col].mask(mask, -555)
            if col in ['mother_diabetes_qc', 'father_diabetes_qc']:
                mask = (self.data[col].isna() & ((self.data['diabetes_history_qc'] == 0)|(self.data['diabetes_history_qc']==2)))
                self.data[col] = self.data[col].mask(mask, -555)
        return self.data

    def tobbaco_skip_logic(self):
        tob_col = ['tobacco_use_qc', 'current_smoker_qc']

        for col in tob_col:
            if col in ['current_smoker_qc' ]:
                mask = (self.data[col].isna() & ((self.data['tobacco_use_qc'] == 0)| (self.data['tobacco_use_qc']==2)))
                self.data[col] = self.data[col].mask(mask, -555)
        return self.data

    def angina_skip_logic(self):
        angina_col = ['angina_qc', 'angina_treatment_yn_qc', 'angina_treat_now_qc']

        for col in angina_col:
            if col in ['angina_treatment_yn_qc', 'angina_treat_now_qc' ]:
                mask = (self.data[col].isna() & ((self.data['angina_qc'] == 0)| (self.data['angina_qc']==2)))
                self.data[col] = self.data[col].mask(mask, -555)
        return self.data

    def hrt_skip_logic(self):
        hrt_col = ['congestive_heart_failure_qc', 'chf_treatment_yn_qc', 'chf_treat_now_qc', 'heartattack_qc', 'heartattack_treatment_qc']

        for col in hrt_col:
            if col in ['chf_treatment_yn_qc', 'chf_treat_now_qc']:
                mask = ((self.data[col]==-999) & ((self.data['congestive_heart_failure'] == 0)| (self.data['congestive_heart_failure']==2)))
                self.data[col] = self.data[col].mask(mask, -555)
            if col in ['heartattack_treatment_qc']:
                mask = ((self.data[col]==-999) & ((self.data['heartattack_qc'] == 0)| (self.data['heartattack_qc']==2)))
                self.data[col] = self.data[col].mask(mask, -555)
        return self.data

    def alco_skip_logic(self):
        alco_col = ['consume_alcohol_qc', 'current_alcohol_consumer_qc', 'alcohol_type_consumed_beer_qc',
                    'frequence_of_alcohol_consumption', 'amount_of_alcohol_consumed_per_day_qc', 'drinking_past_year_qc',
                    'had_hangover_qc', 'consider_alcohol_cutdown_qc']

        for col in alco_col:
            if col in ['current_alcohol_consumer_qc', 'alcohol_type_consumed_beer_qc', 'amount_of_alcohol_consumed_per_day_qc']:
                mask = (self.data[col].isna() & ((self.data['consume_alcohol_qc'] == 0)| (self.data['consume_alcohol_qc']==2)))
                self.data[col] = self.data[col].mask(mask, -555)
            if col in ['frequence_of_alcohol_consumption', 'drinking_past_year_qc', 'had_hangover_qc', 'consider_alcohol_cutdown_qc'] :
                mask = (self.data[col].isna() & ((self.data['current_alcohol_consumer_qc'] == 0)|
                                (self.data['current_alcohol_consumer_qc']==2)| (self.data['current_alcohol_consumer_qc']==555)))
                self.data[col] = self.data[col].mask(mask, -555)
        return self.data

    def chol_skip_logic(self):
        chol_col = ['h_cholesterol_qc', 'cholesterol_treatment_qc', 'cholesterol_meds_weight_loss_qc',
                    'cholesterol_meds_special_diet_qc']

        for col in chol_col:
            if col in ['cholesterol_treatment_qc']:
                mask = (self.data[col].isna() & ((self.data['h_cholesterol_qc'] == 0)| (self.data['h_cholesterol_qc']==2)))
                self.data[col] = self.data[col].mask(mask, -555)
            if col in ['cholesterol_meds_weight_loss', 'cholesterol_meds_special_diet'] :
                mask = (self.data[col].isna() & ((self.data['cholesterol_treatment_qc'] == 0)|
                                (self.data['cholesterol_treatment_qc']==2)| (self.data['cholesterol_treatment_qc']==555)))
                self.data[col] = self.data[col].mask(mask, -555)
        return self.data

    def kidney_skip_logic(self):
        kidney_col = ['kidney_disease_qc', 'kidney_family_qc', 'family_kidney_mother_qc',
                    'family_kidney_father_qc', 'family_kidney_other_qc']

        for col in kidney_col:
            if col in ['family_kidney_mother_qc', 'family_kidney_father_qc', 'family_kidney_other_qc']:
                mask = ((self.data[col]==0) & ((self.data['kidney_family_qc'] == 0)| (self.data['kidney_family_qc']==2)))
                self.data[col] = self.data[col].mask(mask, -555)
        return self.data

    def hiv_skip_logic(self):
        hiv_col = ['hiv_status_qc', 'tested_hiv', 'hiv_positive_qc', 'hiv_medication_qc']

        for col in hiv_col:
            if col in ['hiv_positive_qc']:
                mask = (self.data[col].isna() & ((self.data['hiv_status_qc'] == 0)| (self.data['hiv_status_qc']==2)|
                            (self.data['hiv_status_qc']==3)|(self.data['hiv_status_qc']==-555)))
                self.data[col] = self.data[col].mask(mask, -555)
            if col in ['hiv_medication_qc']:
                mask = (self.data[col].isna() & ((self.data['hiv_positive_qc'] == 0)| (self.data['hiv_positive_qc']==2)|
                                        (self.data['hiv_positive_qc']==3)|(self.data['hiv_status_qc']==555)))
                self.data[col] = self.data[col].mask(mask, -555)
        return self.data

    def tb_skip_logic(self):
        tb_col = ['tb_qc', 'tb_12months_qc', 'tb_treatment_qc', 'tb_meds_qc', 'tb_counselling']

        for col in tb_col:
            if col in ['tb_12months_qc', 'tb_treatment_qc', 'tb_counselling']:
                mask = (self.data[col].isna() & ((self.data['tb_qc'] == 0)| (self.data['tb_qc']==2)))
                self.data[col] = self.data[col].mask(mask, -555)
            if col in ['tb_meds_qc']:
                mask = (self.data[col].isna() & ((self.data['tb_treatment_qc'] == 0)| (self.data['tb_treatment_qc']==2)|
                                        (self.data['hiv_status_qc']==555)))
                self.data[col] = self.data[col].mask(mask, -555)
        return self.data

    def malaria_skip_logic(self):
        malaria_col = ['malaria_qc', 'malaria_month_qc']

        for col in malaria_col:
            if col in ['malaria_month_qc']:
                mask = (self.data[col].isna() & ((self.data['malaria_qc'] == 0) | (self.data['malaria_qc'] == 2)))
                self.data[col] = self.data[col].mask(mask, -555)
        return self.data

    def phy_activity_skip_logic(self):
        phy_activity_col = ['work_vigorous', 'work_vigorous_days', 'work_vigorous_hours', 'work_vigorous_minutes',
                            'work_moderate', 'work_moderate_days', 'work_moderate_hours', 'work_moderate_mins',
                            'transport_physical', 'transport_physical_days', 'transport_physical_hours',
                            'transport_physical_mins', 'leisure_physical', 'leisure_vigorous_days',
                            'leisure_vigorous_hours', 'leisure_vigorous_mins', 'leisure_moderate',
                            'leisure_moderate_days', 'leisure_moderate_hours', 'leisure_moderate_mins']

        for col in phy_activity_col:
            if col == 'work_vigorous':
                mask = (self.data[col].isna() & (self.data['work_sedentary']==1))
                self.data[col] = self.data[col].mask(mask, -555)
            if col in ['work_vigorous_days', 'work_vigorous_hours', 'work_vigorous_minutes']:
                mask = (self.data[col].isna() & ((self.data['work_vigorous'] == 0)| (self.data['work_vigorous'] == -555)))
                self.data[col] = self.data[col].mask(mask, -555)
            if col == 'work_moderate':
                mask = (self.data[col].isna() & ((self.data['work_sedentary']==1)| (self.data['work_vigorous']==1)))
                self.data[col] = self.data[col].mask(mask, -555)
            if col in ['work_moderate_days', 'work_moderate_hours', 'work_moderate_mins']:
                mask = (self.data[col].isna() & ((self.data['work_moderate'] == 0)| (self.data['work_moderate']==-555)))
                self.data[col] = self.data[col].mask(mask, -555)
            if col in ['transport_physical_days', 'transport_physical_hours', 'transport_physical_mins']:
                mask = (self.data[col].isna() & (self.data['transport_physical'] == 0))
                self.data[col] = self.data[col].mask(mask, -555)
            if col in ['leisure_vigorous_days', 'leisure_vigorous_hours', 'leisure_vigorous_mins']:
                mask = (self.data[col].isna() & ((self.data['leisure_physical'] == 0) & (self.data['leisure_vigorous']==0)))
                self.data[col] = self.data[col].mask(mask, -555)
            if col == 'leisure_moderate':
                mask = (self.data[col].isna() & ((self.data['leisure_moderate']==0) & (self.data['leisure_physical']==0)))
                self.data[col] = self.data[col].mask(mask, -555)
            if col in ['leisure_moderate_days', 'leisure_moderate_hours']:
                mask = (self.data[col].isna() & ((self.data['leisure_moderate'] == 0) & (self.data['leisure_physical']==0)))
                self.data[col] = self.data[col].mask(mask, -555)
        return self.data

    def pesticide_skip_logic(self):
        malaria_col = ['malaria_qc', 'malaria_month_qc']

        for col in malaria_col:
            if col in ['malaria_month_qc']:
                mask = (self.data[col].isna() & ((self.data['malaria_qc'] == 0) | (self.data['malaria_qc'] == 2)))
                self.data[col] = self.data[col].mask(mask, -555)
        return self.data