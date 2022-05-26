import tkinter as tk
import prepare
import acquire
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import random

class TelcoModel():

    def __init__(self):
        df = acquire.get_telco_data()
        df_prep = prepare.prep_telco(df)
        train, validate, test = prepare.split_telco_data(df_prep)
        train = prepare.telco_make_dummies(train)
        X_train = train.select_dtypes(include=['int64', 'float64', 'uint8']).drop(columns = 'churn_Yes')
        #include only the encoded target variable
        y_train = train.churn_Yes
        self.dt = DecisionTreeClassifier(max_depth=4, random_state=prepare.RAND_SEED) #make a decision tree model with depth 4
        self.dt = self.dt.fit(X_train, y_train) #fit the train data
    
    def return_prediction(self, df_gui):
        print(df_gui.T)
        df_gui = prepare.telco_make_dummies(df_gui)
        X_predict = df_gui.select_dtypes(include=['int64', 'float64', 'uint8'])
        print('df_gui.T')
        print(df_gui.T)
        print('concat df_gui:')
        print(df_gui.info())
        # print(df_gui)
        # print(X_predict.info())
        #prediction = self.dt.predict_proba(X_predict)
        return None

class TelcoGui():

    def __init__(self):
        self.model = TelcoModel()

        root = tk.Tk()

        #tenure frame
        tenure_frame = tk.Frame(root).grid()
        tenure_label = tk.Label(tenure_frame, text = 'Tenure').grid(column=0, row=0, sticky=tk.W)
        self.tenure_var = tk.IntVar()
        self.tenure_entry = tk.Entry(tenure_frame, textvariable=self.tenure_var).grid(column=1, row=0, sticky=tk.W)
        #monthly charges frame
        monthly_frame = tk.Frame(root).grid()
        monthly_label = tk.Label(monthly_frame, text = 'Monthly Charges').grid(column=0, row=1, sticky=tk.W)
        self.monthly_var = tk.IntVar()
        self.monthly_entry = tk.Entry(monthly_frame, textvariable=self.monthly_var).grid(column=1, row=1, sticky=tk.W)

        #make a frame for the contract options
        contract_frame = tk.Frame(root).grid()
        contract_label = tk.Label(contract_frame, text='Contract Type').grid(column=0, row=2, sticky=tk.W)
        #contract type
        self.contract_selected = tk.StringVar()
        contract_radio = [
            ('Month-to-Month', 'Month-to-month'),
            ('One Year', 'One year'),
            ('Two Year', 'Two year')
        ]
        for i, radio in enumerate(contract_radio):
            self.r = tk.Radiobutton(contract_frame, text = radio[0], variable=self.contract_selected, value = radio[1])
            self.r.grid(column=1, row=2+i, sticky=tk.W)
        
        #phone service type
        phone_frame = tk.Frame(root).grid()
        phone_label = tk.Label(phone_frame, text='Phone Service Type').grid(column=0,row=6, sticky=tk.W)
        self.phone_selected = tk.StringVar()
        phone_radio = [
            ('No Phone', 'No phone'),
            ('One Line', 'No'),
            ('Multiple Lines', 'Multiple lines')
        ]
        for i, radio in enumerate(phone_radio):
            self.r_phone = tk.Radiobutton(phone_frame, text=radio[0], variable=self.phone_selected, value = radio[1])
            self.r_phone.grid(column=1, row = 6+i, sticky=tk.W)

        #gender Frame
        gender_frame = tk.Frame(root).grid()
        gender_label = tk.Label(phone_frame, text='Gender').grid(column=0,row=9, sticky=tk.W)
        self.gender_selected = tk.StringVar()
        gender_radio = [
            ('Male', 'Male'),
            ('Female', 'Female')
        ]
        for i, radio in enumerate(gender_radio):
            self.r_gender = tk.Radiobutton(phone_frame, text=radio[0], variable=self.gender_selected, value = radio[1])
            self.r_gender.grid(column=1, row = 9+i, sticky=tk.W)

        internet_frame = tk.Frame(root).grid()
        internet_label = tk.Label(phone_frame, text='Internet Service').grid(column=0,row=11, sticky=tk.W)
        self.internet_selected = tk.StringVar()
        internet_radio = [
            ('DSL', 'DSL'),
            ('Fiber optic', 'Fiber optic'),
            ('No internet', 'No internet service')
        ]
        for i, radio in enumerate(internet_radio):
            self.r_internet = tk.Radiobutton(internet_frame, text=radio[0], variable=self.internet_selected, value = radio[1])
            self.r_internet.grid(column=1, row = 11+i, sticky=tk.W)

        payment_frame = tk.Frame(root).grid()
        payment_label = tk.Label(payment_frame, text='Payment method').grid(column=0,row=14, sticky=tk.W)
        self.payment_selected = tk.StringVar()
        payment_radio = [
            ('Credit Card (automatic)', 'Credit card (automatic)'),
            ('Bank transfer (automatic)', 'Bank transfer (automatic)'),
            ('Electronic check', 'Electronic check'),
            ('Mailed check', 'Mailed check')
        ]
        for i, radio in enumerate(payment_radio):
            self.r_payment = tk.Radiobutton(payment_frame, text=radio[0], variable=self.payment_selected, value = radio[1])
            self.r_payment.grid(column=1, row = 14+i, sticky=tk.W)

        partner_frame = tk.Frame(root).grid()
        self.partner_status = tk.StringVar()
        self.partner_status_check = tk.Checkbutton(partner_frame, text='Partnered', variable=self.partner_status, onvalue='Yes', offvalue='No')
        self.partner_status_check.grid(column=0, row=18)

        dependent_frame = tk.Frame(root).grid()
        self.dependent_status = tk.StringVar()
        self.dependent_status_check = tk.Checkbutton(partner_frame, text='Dependents', variable=self.dependent_status, onvalue='Yes', offvalue='No')
        self.dependent_status_check.grid(column=1, row=18)

        senior_frame = tk.Frame(root).grid()
        self.senior_status = tk.IntVar()
        self.senior_status_check = tk.Checkbutton(partner_frame, text='Senior Citizen', variable=self.senior_status, onvalue=1, offvalue=0)
        self.senior_status_check.grid(column=0, row=19)

        self.paperless_frame = tk.Frame(root).grid()
        self.paperless_status = tk.StringVar()
        self.paperless_status_check = tk.Checkbutton(partner_frame, text='Paperless Billing', variable=self.paperless_status, onvalue='Yes', offvalue='No')
        self.paperless_status_check.grid(column=1, row=19)

        online_security_frame = tk.Frame(root).grid()
        self.online_security_status = tk.StringVar()
        self.online_security_status_check = tk.Checkbutton(partner_frame, text='Online Security', variable=self.online_security_status, onvalue='Yes', offvalue='No')
        self.online_security_status_check.grid(column=0, row=20)

        online_backup_frame = tk.Frame(root).grid()
        self.online_backup_status = tk.StringVar()
        self.online_backup_check = tk.Checkbutton(partner_frame, text='Online Backup', variable=self.online_backup_status, onvalue='Yes', offvalue='No')
        self.online_backup_check.grid(column=1, row=20)

        device_protection_frame = tk.Frame(root).grid()
        self.device_protection_status = tk.StringVar()
        self.device_protection_check = tk.Checkbutton(partner_frame, text='Device Protection', variable=self.device_protection_status, onvalue='Yes', offvalue='No')
        self.device_protection_check.grid(column=0, row=21)

        tech_support_frame = tk.Frame(root).grid()
        self.tech_support_status = tk.StringVar()
        self.tech_support_check = tk.Checkbutton(partner_frame, text='Tech Support', variable=self.tech_support_status, onvalue='Yes', offvalue='No')
        self.tech_support_check.grid(column=1, row=21)

        streaming_tv_frame = tk.Frame(root).grid()
        self.streaming_tv_status = tk.StringVar()
        self.streaming_tv_check = tk.Checkbutton(partner_frame, text='Streaming TV', variable=self.streaming_tv_status, onvalue='Yes', offvalue='No')
        self.streaming_tv_check.grid(column=0, row=22)

        streaming_movies_frame = tk.Frame(root).grid()
        self.streaming_movies_status = tk.StringVar()
        self.streaming_movies_check = tk.Checkbutton(partner_frame, text='Streaming Movies', variable=self.streaming_movies_status, onvalue='Yes', offvalue='No')
        self.streaming_movies_check.grid(column=1, row=22)

        predict_frame = tk.Frame(root).grid()
        self.predict_button = tk.Button(predict_frame, text='Predict Churn Probability', command=self.get_dataframe)
        self.predict_button.grid(column=0, row=23)

        prediction_frame = tk.Frame(root).grid()
        self.prediction_entry = tk.Entry(prediction_frame)
        self.prediction_entry.grid(column=1, row=23)
        root.mainloop()

    def get_dataframe(self):
        result = {}
        result['customer_id'] = '0000-AAAAA'
        result['gender'] = self.gender_selected.get()
        result['senior_citizen'] = self.senior_status.get()
        result['partner'] = self.partner_status.get()
        result['dependents'] = self.dependent_status.get()
        result['tenure'] = self.tenure_var.get()
        if self.phone_selected.get() == 'No phone':
            result['phone_service'] = 'No'
            result['multiple_lines'] = 'No'
        else:
            result['phone_service'] = 'Yes'
            if self.phone_selected.get() == 'Multiple lines':
                result['multiple_lines'] = 'Yes'
            else:
                result['multiple_lines'] = 'No'
        if self.internet_selected.get()=='No internet service':
            result['internet_service_type'] = self.internet_selected.get()
            result['online_security'] = 'No'
            result['online_backup'] = 'No'
            result['device_protection'] = 'No'
            result['tech_support'] = 'No'
            result['streaming_tv'] = 'No'
            result['streaming_movies'] = 'No'
        else:
            result['internet_service_type'] = self.internet_selected.get()
            result['online_security'] = self.online_security_status.get()
            result['online_backup'] = self.online_backup_status.get()
            result['device_protection'] = self.device_protection_status.get()
            result['tech_support'] = self.tech_support_status.get()
            result['streaming_tv'] = self.streaming_tv_status.get()
            result['streaming_movies'] = self.streaming_movies_status.get()
        result['paperless_billing'] = self.paperless_status.get()
        result['monthly_charges'] = float(self.monthly_var.get())
        result['tenure'] = self.tenure_var.get()
        result['total_charges'] = float(self.tenure_var.get()*self.monthly_var.get())
        result['contract_type'] = self.contract_selected.get()
        result['payment_type'] = self.payment_selected.get()

        df = pd.DataFrame([result])
        prediction = self.model.return_prediction(df)
        self.prediction_entry.delete(0,tk.END)
        self.prediction_entry.insert(0,random.random())
        # print(df)
        # print(df.info())
        pass
        
if __name__=='__main__':
    gui = TelcoGui()