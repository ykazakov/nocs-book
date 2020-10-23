import ipywidgets as widgets
import random
question = widgets.HTML() # the question text
answer = widgets.Text() # the field to enter the answer
submit_btn = widgets.Button(description="Submit", icon='check') # submit button
stats = widgets.HTML() # statistics about correct answers
feedback = widgets.HTML() # show additional feedback for the answer
progress = widgets.IntProgress(max=20) # show exercise progress
done = widgets.HTML() # display a message when the exercise is over
n_answers = 0 # the number of answers
n_correct = 0 # the number of correct answers
recent = [11,11,11,11] # avoid repeating recently used numbers
x = 11 # variable for random test values

def next_round():
    global x
    while (x in recent):
        x = random.randint(0,10)
    recent.pop()
    recent.insert(0,x)
    question.value = f'<big>2<sup>{x}</sup> = </big>'
    answer.value = ''

def submit(sumbit_btn):
    global n_answers, n_correct    
    try:
        val = int(answer.value)
    except ValueError:
        return
    n_answers += 1
    if (val == 2**x):
        n_correct += 1
        next_round()
        feedback.value = ''
        if (progress.value < progress.max):
            progress.value += 1
        if (progress.value == progress.max):                
            progress.bar_style='success'
            done.value = '<big><b>Well done!</b></big>'
    else:
        feedback.value = '<big><div style="color:red">Try again!</div></big>'
        if (progress.value > 0):
            progress.value -= 1;        
    success_rate = n_correct * 100 / n_answers    
    stats.value = f'<big>Corect: <b>{n_correct}</b> of {n_answers} ({success_rate:.0f}%)</big>'    

answer.on_submit(submit)    
submit_btn.on_click(submit)
display(widgets.HBox([question, answer, submit_btn, feedback]))
display(widgets.HBox([progress, stats]))
display(done)
next_round()