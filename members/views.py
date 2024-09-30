from django.http import HttpResponse
from django.template import loader
from .models import anggota

def members(request):
  mymembers = anggota.objects.all().values()
  template = loader.get_template('personel.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = anggota.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))