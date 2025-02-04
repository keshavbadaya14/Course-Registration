from django.contrib import admin
from .models import TimeTable, MessSchedule, ExamSchedule, BusSchedule
# Register your models here.
admin.site.register(TimeTable)
admin.site.register(MessSchedule)
admin.site.register(ExamSchedule)
admin.site.register(BusSchedule)