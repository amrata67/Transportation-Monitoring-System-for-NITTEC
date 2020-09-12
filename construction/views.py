from django.http import HttpResponse
from django.shortcuts import render
from .models import Project
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template

# Add the project to the database
def addProjectToDatabase(request):
    newRecord = Project(
        dnumber = request.POST.get('dnumber'),
        road = request.POST.get('road'),
        end = request.POST.get('end'),
        start = request.POST.get('start'),
        county = request.POST.get('county'),
        place = request.POST.get('place'),
        description = request.POST.get('description')
    )
    newRecord.save()

# Print all records in PDF format
def printToPDF(request, context):
    template = get_template('construction/construction_projects.html')
    data_p = template.render(context)
    response = BytesIO()
    pdfPage = pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")), response)
    if pdfPage.err:
        return HttpResponse("Error generating PDF")
    return HttpResponse(response.getvalue(), content_type="application/pdf")

# List all projects
def projects(request):
    projectsList = Project.objects.all()
    context = {
        'projectsList': projectsList,
    }
    # Check if it is a post request and sent by the addProject button
    if request.method == "POST" and request.POST.get('addProject'):
        addProjectToDatabase(request)
    elif request.GET.get('printProjects'):
        return printToPDF(request, context)
    
    return render(request, 'construction/construction_projects.html', context)

# Page that let's the operator add projects
def addProject(request):
    return render(request, 'construction/add_project.html')

# Construction and Maintenance page
def constructionMaintenance(request):
    return render(request, 'construction/construction_maintenance.html')
