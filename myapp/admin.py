#import models from models.py
from django.contrib import admin
from .models import Student
from .models import Busses
from .models import Schedule
from .models import AdminHOD
from .models import Chief
from .models import Reservation




# adding a class for student
class StudentAdmin(admin.ModelAdmin):
    list_display = ('studentID', 'studentName', 'studentCourse', 'studentEmail', 'studentUsername', 'studentPassword')


# adding a class for bus
class BussesAdmin(admin.ModelAdmin):
    list_display = ('busID', 'busPlateNumber', 'busDriver', 'numberOfSeats', 'numberOfVacancies')


# adding a class for schedule
class ScheduleAdmin(admin.ModelAdmin):
   list_display = ('scheduleID', 'busID', 'scheduleArrival', 'scheduleDeparture','scheduleSeatVacancies')


# adding a class for admin
class AdminHODAdmin(admin.ModelAdmin):
    list_display = ('adminID', 'adminUsername', 'adminPassword', 'adminName',)


# adding a class for Chief
class ChiefAdmin(admin.ModelAdmin):
    list_display = ('chiefID', 'chiefUsername', 'chiefPassword', 'chiefName',)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservationID','studentID', 'studentName', 'busID', 'scheduleID','scheduleSeatVacancies')


admin.site.register(Student, StudentAdmin)
admin.site.register(Busses, BussesAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(AdminHOD, AdminHODAdmin)
admin.site.register(Chief, ChiefAdmin)
admin.site.register(Reservation, ReservationAdmin)