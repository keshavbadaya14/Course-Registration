from django.shortcuts import render
from .models import TimeTable, MessSchedule, ExamSchedule, BusSchedule

def student_dashboard(request):
    # If user is not authenticated, do not filter by student
    if request.user.is_authenticated:
        timetable = TimeTable.objects.filter(student=request.user)
    else:
        timetable = TimeTable.objects.all()  # Show empty or all timetables

    mess_schedule = MessSchedule.objects.all()
    exam_schedule = ExamSchedule.objects.all()
    bus_schedule = BusSchedule.objects.all()

    context = {
        'timetable': timetable,
        'mess_schedule': mess_schedule,
        'exam_schedule': exam_schedule,
        'bus_schedule': bus_schedule,
    }
    
    return render(request, 'dashboard/dashboard.html', context)
