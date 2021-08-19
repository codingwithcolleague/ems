from poll.models import Question

def polls_count(request):
    count = Question.objects.count()
    print("count",count)
    return { "count" : count }