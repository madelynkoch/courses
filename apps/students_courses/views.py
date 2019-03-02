from django.shortcuts import render, redirect, HttpResponse
from apps.students_courses.models import courses
from django.contrib import messages
# Create your views here.
def index(request):
	data = {
		'courses': courses.objects.all()
	}
	return render(request, 'students_courses/index.html', data)

def confirm(request, id):
	data = {
		'course': courses.objects.get(id=id)
	}
	return render(request, 'students_courses/delete.html', data)

def delete(request, id):
	course = courses.objects.get(id=id)
	course.delete()
	return redirect('/courses')

def create(request):
	errors = courses.objects.basic_validator(request.POST)
	if len(errors):
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/courses')
	else:
		new_course = courses.objects.create(name = request.POST['name'], desc = request.POST['desc'])
		return redirect('/courses')