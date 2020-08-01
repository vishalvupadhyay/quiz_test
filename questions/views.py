from django.shortcuts import render, HttpResponse
from .models import Question, PracticeResult
from django.db.models import Max,Q

checkAnswers = {}
practiceTestNumber = ''

def home(request):
    data = Question.objects.values('subject')
    return render(request,"home.html",{'data':data})

def practice(request):
    global practiceTestNumber
    questions = Question.objects.all()
    pTestNumber = PracticeResult.objects.aggregate(Max('practiceTestNumber'))
    practiceTestNumber = (pTestNumber['practiceTestNumber__max'])+1
    for question in questions:
        checkAnswers[question.id] = [question.id,question.question,question.correct_answer,question.subject]

   
    return render(request,"practice.html",{'questions':questions})



def result(request):

    if not checkAnswers :
        pass
    else:
        a = request.POST
        a = dict(a)
        
        #list(a)[1:-1] ia for ignoring first and last item in dict
        for i in list(a)[1:-1]:
            selectedAnswer =  str(a[i]).replace("['","").replace("']","").replace("[\"","").replace("\"]","")
            i = int(i)
            pr = PracticeResult(user="vishal",question=checkAnswers[i][1],selectedOption=selectedAnswer,correctAnswer=checkAnswers[i][2],practiceTestNumber=practiceTestNumber)
            pr.save()
        
    checkAnswers.clear()

    results = PracticeResult.objects.raw('''SELECT *
    
    
    From "questions_practiceresult"
    WHERE "questions_practiceresult"."practiceTestNumber" = (SELECT MAX("questions_practiceresult"."practiceTestNumber")    From "questions_practiceresult")
    ''')
    
    
    return render(request,"result.html",{'results':results})

