from django import forms

class RiskCalculatorForm(forms.Form):
    account_balance = forms.DecimalField(max_digits=10, decimal_places=2)
    risk_percentage = forms.DecimalField(max_digits=5, decimal_places=2)
    stop_loss = forms.DecimalField(max_digits=10, decimal_places=4)
    take_profit = forms.DecimalField(max_digits=10, decimal_places=4)

    def calculate_position_size(self):
        balance = self.cleaned_data['account_balance']
        risk_percent = self.cleaned_data['risk_percentage'] / 100
        stop_loss = self.cleaned_data['stop_loss']
        position_size = (balance * risk_percent) / stop_loss
        return position_size
