
from django.urls import path, include
from . import views

urlpatterns = [
    # main urls
    path('login/', views.LoginPage, name='login-page'),
    path('logout/', views.LogoutUser, name='logout-page'),
    path('cecadmin/', views.AdminPage, name='admin-page'),
    path('driver/', views.DriverPage, name='driver-page'),
    path('reservation/', views.ReservationPage, name='reservation-page'),

    # admin url
    path('cecadmin/addstudent', views.AddStudent, name='add-student'),
    path('cecadmin/addbus', views.AddBus, name='add-bus'),
    path('cecadmin/addschedule', views.AddSchedule, name='add-schedule'),
    path('cecadmin/assigndriver', views.AssignDriver, name='assign-driver'),
    path('cecadmin/managebus', views.ManageBus, name='manage-bus'),
    path('cecadmin/manageschedule', views.ManageSchedule, name='manage-schedule'),
    path('cecadmin/managedriver', views.ManageDriver, name='manage-driver'),
    path('cecadmin/managestudent', views.ManageStudent, name='manage-student'),
    path('cecadmin/managereservation', views.ManageReservation, name='manage-reservation'),
    path('cecadmin/updatestudent/<str:username>', views.UpdateStudent, name='update-student'),
    path('cecadmin/updatestudentsave', views.UpdateStudentSave, name='update-student-save'),
    path('cecadmin/updatebus/<str:busID>', views.UpdateBus, name='update-bus'),
    path('cecadmin/updatesbussave', views.UpdateBusSave, name='update-bus-save'),
    path('cecadmin/updatedriver/<str:username>', views.UpdateDriver, name='update-driver'),
    path('cecadmin/updatesdriversave', views.UpdateDriverSave, name='update-driver-save'),
    path('cecadmin/updateschedule/<str:scheduleID>', views.UpdateSchedule, name='update-schedule'),
    path('cecadmin/updatesschedulesave', views.UpdateScheduleSave, name='update-schedule-save'),
    path('cecadmin/deletestudent/<str:username>', views.DeleteStudent, name='delete-student'),
    path('cecadmin/deletebus/<str:busID>', views.DeleteBus, name='delete-bus'),
    path('cecadmin/deleteschedule/<str:scheduleID>', views.DeleteSchedule, name='delete-schedule'),
    path('cecadmin/deletedriver/<str:username>', views.DeleteDriver, name='delete-driver'),

    # driver url
    path('driver/reservationlist', views.ReservationListPage, name='reservationlist-page'),
    path('driver/arrivedstatus/<str:scheduleID>', views.ArrivedStatus, name='arrivedstatus-page'),
    path('driver/manageschedule', views.DriverManageSchedule, name='driver-manage-schedule'),
    path('driver/updateschedule/<str:scheduleID>', views.DriverUpdateSchedule, name='driver-update-schedule'),
    path('driver/updatesschedulesave', views.DriverUpdateScheduleSave, name='driver-update-schedule-save'),
    path('driver/removereservation/<str:reservationID>', views.RemoveReservation, name='removereservation-page'),

    # students url
    path('reservation/form/<str:scheduleID>', views.ReservationFormPanel, name='reservationformpannel-page'),
]

