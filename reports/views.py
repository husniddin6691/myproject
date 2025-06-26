from django.shortcuts import render

def report_dashboard(request):
    return render(request, 'reports/report_dashboard.html')

