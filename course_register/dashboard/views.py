from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TimeTable, MessSchedule, ExamSchedule, BusSchedule

@login_required
def student_dashboard(request):
    student = request.user
    timetable = TimeTable.objects.filter(student=student)
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
