from django.shortcuts import render
from .forms import RiskCalculatorForm

def risk_calculator(request):
    form = RiskCalculatorForm()
    position_size = None

    if request.method == 'POST':
        form = RiskCalculatorForm(request.POST)
        if form.is_valid():
            position_size = form.calculate_position_size()

    return render(request, 'journal/risk_calculator.html', {'form': form, 'position_size': position_size})