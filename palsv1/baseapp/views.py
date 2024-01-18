from django.shortcuts import render , redirect 
from django.urls import reverse
from django.http import HttpResponse , JsonResponse
from django.views.generic.list import ListView
from .models import Course , Subunit , Question
from .forms import AnswerCodeForm
import subprocess







# VIEWS

#func-based views



def home(request):
    return HttpResponse("Home")

def unit_list(request,pk):
    course_current= Course.objects.get(student=request.user ,id=pk)
    units= Subunit.objects.filter(course=course_current)
    context={
        'units': units,
        'course': course_current
    }
    return render(request=request , template_name='baseapp/unit_list.html',context=context)

def question_page(request,pk):
    unit_current = Subunit.objects.get(id=pk)
    course_curr = unit_current.course
    question_set = Question.objects.filter(subunit=unit_current)
    curr_q_id = unit_current.question_completion_level
    curr_q = question_set[curr_q_id]
    form = AnswerCodeForm()
    context={
        'course':course_curr,
        'unit': unit_current,
        'question': curr_q,
        'form': form

    }
    return render(request=request, template_name='baseapp/question_page.html',context=context)


    
def answer_code_submit(request,pk):
    question = Question.objects.get(id=pk)
    if request.method =='POST':
        submitted_answer_code = request.POST.get('code')
        code_input = request.POST.get('input_value')
        question.input_data = code_input
        question.answer = submitted_answer_code
        question.save()
        
        file_path = "code.py"  
        new_code = question.answer
        with open(file_path, 'w') as file:
            file.write(new_code)

        subprocess.run(["docker", "build", "-t", "codeeval", "."], check=True)
        input_data = question.input_data
        process = subprocess.Popen("docker run -i codeeval:latest", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate(input=input_data)
        output = output.strip()
        

        context={
            'output':output,
            'error': error
        }
        return JsonResponse(context)

    else:
        return JsonResponse({'error': 'Invalid request method'})


#def course_list(request):
#     return HttpResponse("Courses")



#class-based views

class CourseList(ListView):
    model = Course
    context_object_name = 'courses'
