from django.shortcuts import render


def todo_list(request):

	return render(request, 'todo_list.html', 

	{
	"list": [{
		"task": "Task 1",
		"created": "10.09.2018",
		"dueto": "12.09.2018",
		"owner": "admin",
		"mark": True
	}, {
		"task": "Task 2",
		"created": "10.09.2018",
		"dueto": "12.09.2018",
		"owner": "admin",
		"mark": True
	}, {
		"task": "Task 3",
		"created": "10.09.2018",
		"dueto": "12.09.2018",
		"owner": "admin",
		"mark": True
	}, {
		"task": "Task 4",
		"created": "10.09.2018",
		"dueto": "12.09.2018",
		"owner": "admin",
		"mark": True
	}, {
		"task": "Task 5",
		"created": "10.09.2018",
		"dueto": "12.09.2018",
		"owner": "admin",
		"mark": True
	}]
})
# Create your views here.




def completed_todo_list(request):
	return render(request, 'completed_todo_list.html',
		{
	"list": [{
		"task": "Task 1",
		"created": "10.09.2018",
		"dueto": "12.09.2018",
		"owner": "admin",
		"mark": False
		}]
	})
# Create your views here.
