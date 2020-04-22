from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def Add(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)


    if request.method == "POST":
        answer = request.POST["answer"]
        old_num_1 = request.POST["old_num_1"]
        old_num_2 = request.POST["old_num_2"]
        correct_answer = int(old_num_1) + int(old_num_2)
        
        #Error handling
        if not answer:
            my_answer = "Hey! You forgat to fill out the form!"
            color = "warning"
            return render(request, 'Add.html', {
            'answer':answer,
            'my_answer' : my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color': color,
            })
        
        if int(answer) == correct_answer:
            my_answer = 'Correct! ' + old_num_1 + " + " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = 'Incorrect! ' + old_num_1 + " + " + old_num_2 + " is not " + answer + " it is " + str(correct_answer)
            color = "danger"
        return render(request, 'Add.html', {
            'answer':answer,
            'my_answer' : my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color': color,
            })
    
    return render(request, 'Add.html', {
        'num_1':num_1,
        'num_2':num_2,
    })

def Subtract(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)


    if request.method == "POST":
        answer = request.POST["answer"]
        old_num_1 = request.POST["old_num_1"]
        old_num_2 = request.POST["old_num_2"]
        correct_answer = int(old_num_1) - int(old_num_2)
        
        #Error handling is on haaanndds hereeeeeeeeeeeeeee:D
        if not answer:
            my_answer = "Hey! You forgat to fill out the form!"
            color = "warning"
            return render(request, 'Subtract.html', {
            'answer':answer,
            'my_answer' : my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color': color,
            })
        if int(answer) == correct_answer:
            my_answer = 'Correct! ' + old_num_1 + " - " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = 'Incorrect! ' + old_num_1 + " - " + old_num_2 + " is not " + answer + " it is " + str(correct_answer)
            color = "danger"
        return render(request, 'Subtract.html', {
            'answer':answer,
            'my_answer' : my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color': color,
            })
    
    return render(request, 'Subtract.html', {
        'num_1':num_1,
        'num_2':num_2,
    })

def Multiply(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(0,10)


    if request.method == "POST":
        answer = request.POST["answer"]
        old_num_1 = request.POST["old_num_1"]
        old_num_2 = request.POST["old_num_2"]
        correct_answer = int(old_num_1) * int(old_num_2)
        
        #Error handling is on haaanndds hereeeeeeeeeeeeeee:D
        if not answer:
            my_answer = "Hey! You forgat to fill out the form!"
            color = "warning"
            return render(request, 'Multiply.html', {
            'answer':answer,
            'my_answer' : my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color': color,
            })
        if int(answer) == correct_answer:
            my_answer = 'Correct! ' + old_num_1 + " * " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = 'Incorrect! ' + old_num_1 + " * " + old_num_2 + " is not " + answer + " it is " + str(correct_answer)
            color = "danger"
        return render(request, 'Multiply.html', {
            'answer':answer,
            'my_answer' : my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color': color,
            })
    
    return render(request, 'Multiply.html', {
        'num_1':num_1,
        'num_2':num_2,
    })

def Divide(request):
    from random import randint

    num_1 = randint(0,10)
    num_2 = randint(1,10)


    if request.method == "POST":
        answer = request.POST["answer"]
        old_num_1 = request.POST["old_num_1"]
        old_num_2 = request.POST["old_num_2"]
        correct_answer = int(old_num_1) / int(old_num_2)
        
        #Error handling is on haaanndds hereeeeeeeeeeeeeee:D
        if not answer:
            my_answer = "Hey! You forgat to fill out the form!"
            color = "warning"
            return render(request, 'Divide.html', {
            'answer':answer,
            'my_answer' : my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color': color,
            })
        if float(answer) == correct_answer:
            my_answer = 'Correct! ' + old_num_1 + " / " + old_num_2 + " = " + answer
            color = "success"
        else:
            my_answer = 'Incorrect! ' + old_num_1 + " / " + old_num_2 + " is not " + answer + " it is " + str(correct_answer)
            color = "danger"
        return render(request, 'Divide.html', {
            'answer':answer,
            'my_answer' : my_answer,
            'num_1':num_1,
            'num_2':num_2,
            'color': color,
            })
    
    return render(request, 'Divide.html', {
        'num_1':num_1,
        'num_2':num_2,
    })
