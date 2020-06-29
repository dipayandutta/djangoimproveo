from django.shortcuts import render
from .forms import ReportForm,ProblemReportedForm
from .models import Report


# Create your views here.
def report_view(request,production_line):
    form = ReportForm()
    pform = ProblemReportedForm()
    querySet = Report.objects.filter(production_line__name=production_line.upper())
    #querySet = Report.objects.all()
    context = {
        'form':form,
        'pform':pform,
        'object_list':querySet,
    }

    return render(request,'reports/report.html',context)

