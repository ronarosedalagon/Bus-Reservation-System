from django.shortcuts import render,redirect
from django.contrib import messages, auth
from .forms import *
from .forms import RegisterUserForm

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .decorations import unauthenticated_user, allowed_users, admin_only

# create views

# function for unauthorized user
@unauthenticated_user
def LoginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group == 'student':
                return redirect('reservation-page')

            if group == 'driver':
                return redirect('driver-page')

            if group == 'admin':
                return redirect('admin-page')
        else:
            messages.info(request,'Username or Password is incorrect')

    context = {}
    return render(request,'myapp/HomePage.html', context)

# Log out function
def LogoutUser(request):
    logout(request)
    return redirect('/login')

# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='driver')
def DriverPage(request):
    return render(request,'myapp/DriverPage.html')

# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='driver')
def ReservationListPage(request):
   reservation = Reservation.objects.all()
   schedule = Schedule.objects.all()

   return render(request,'myapp/ReservationList.html',
                  {'reservation':reservation,'schedule':schedule})


def ReservationFormPanel(request,scheduleID):
    # get the primary key that has been pass
    schedules = Schedule.objects.get(scheduleID=scheduleID)
    form = ReservationForm(request.POST or None, instance=schedules)

    # function
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # deduct a slot for the vacant seats
            if schedules.scheduleSeatVacancies != 0:
                schedules.scheduleSeatVacancies -= 1

                # add reservation
                instance.reservationID += instance.scheduleSeatVacancies
                schedules.save()
                instance.save( )
                messages.info(request, 'Your reservation was submitted successfully!')
            else:
                messages.info(request, 'There is no more vacant seats left from your selected schedule')

            # redirection page
            return HttpResponseRedirect('/reservation')
    context={
        "title": 'Reservation',
        "form":form,
        'Reservation': schedules,
        'Schedule': schedules
    }
    return render(request,'myapp/ReservationFormPanel.html', context)




# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='admin')
def AdminPage(request):
    # call the redirection page 
    return render(request,'myapp/AdminPage.html')


# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='student')
def ReservationPage(request):
    schedule = Schedule.objects.all()
    return render(request,'myapp/ReservationPage.html',
                  {'schedule':schedule})




# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='admin')
def AddBus(request):
    form = AddBusForm
    submitted = False
    if request.method == "POST":
        form = AddBusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Bus was successfully added!')
            return HttpResponseRedirect('/cecadmin/addbus')
        else:
            form = AddBusForm
            if 'submitted' in request.GET:
                submitted = True

    return render(request,'admin/addBus.html',
                  {'form': form, 'submitted': submitted})


# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='admin')
def AddSchedule(request):
    form = AddScheduleForm
    submitted = False
    if request.method == "POST":
        form = AddScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Schedule was successfully added!')
            return HttpResponseRedirect('/cecadmin/addschedule')
        else:
            form = AddScheduleForm
            if 'submitted' in request.GET:
                submitted = True

    return render(request,'admin/addSchedule.html',
                  {'form': form, 'submitted': submitted})


# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='admin')
def AddStudent(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='student')
            user.groups.add(group)

            messages.success(request,("Registration Successful"))
            return redirect('add-student')
    else:
        form = RegisterUserForm()

    return render(request,'admin/addStudent.html',{
        'form':form,
    })

# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='admin')
def AssignDriver(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            group = Group.objects.get(name='driver')
            user.groups.add(group)

            messages.success(request, ("Registration Successful!"))
            return redirect('assign-driver')
    else:
        form = RegisterUserForm()

    return render(request, 'admin/addDriver.html', {
        'form': form,
    })
# calling the function for page restrictions
# add student


# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='admin')
def ManageBus(request):
    busses = Busses.objects.all()
    return render(request,'admin/manageBus.html',{'busses':busses})


# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='admin')
def ManageDriver(request):
    driver = User.objects.filter(groups=3)
    return render(request,'admin/manageDriver.html',{'User':driver})


# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='admin')
def ManageSchedule(request):
    schedule = Schedule.objects.all()
    return render(request, 'admin/manageSchedule.html',{'schedule':schedule})

# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='driver')
def DriverManageSchedule(request):
    schedule = Schedule.objects.all()
    return render(request, 'myapp/DriverManageSchedule.html',{'schedule':schedule})



# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='admin')
def ManageStudent(request):
    student = User.objects.filter(groups=2)
    return render(request, 'admin/manageStudent.html',{'User':student})


# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='admin')
def ManageReservation(request):
     reservation = Reservation.objects.all()
     return render(request, 'admin/manageReservation.html',{'reservation':reservation})


# start of update function
# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='admin')
def UpdateStudent(request, username):
    student = User.objects.get(username=username)
    form = UpdateStudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('manage-student')

    return render(request,'admin/updateStudent.html',
                  {'form': form, 'User':student})


def UpdateStudentSave(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        studentID = request.POST.get("studentID")
        studentName = request.POST.get("studentName")
        studentCourse = request.POST.get("studentCourse")
        studentEmail = request.POST.get("studentEmail")
        studentUsername = request.POST.get("studentUsername")

        try:
            Student.studentID = studentID
            Student.studentName = studentName
            Student.studentCourse = studentCourse
            Student.studentEmail = studentEmail
            Student.studentUsername = studentUsername
            Student.save()

            messages.success(request, "Successfully Edited Student")
        except:
            messages.error(request, "Failed to Edit Student")


# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='admin')
def UpdateBus(request, busID):
    busses = Busses.objects.get(busID=busID)
    form = AddBusForm(request.POST or None, instance=busses)
    if form.is_valid():
        form.save()
        return redirect('manage-bus')

    return render(request,'admin/updateBus.html',
                  {'form': form, 'busses':busses})


def UpdateBusSave(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        busID = request.POST.get("")
        busPlateNumber = request.POST.get("")
        busDriver = request.POST.get("")
        numberOfSeats = request.POST.get("")
        numberOfVacancies = request.POST.get("")

        try:

            Busses.busID = busID
            Busses.busPlateNumber = busPlateNumber
            Busses.busDriver = busDriver
            Busses.numberOfSeats = numberOfSeats
            Busses.numberOfVacancies = numberOfVacancies
            Busses.save()

            messages.success(request, "Successfully Updated Bus")
        except:
            messages.error(request, "Failed to Update Bus")



# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='admin')
def UpdateDriver(request, username):
    chief = User.objects.get(username=username)
    form = UpdateDriverForm(request.POST or None, instance=chief)
    if form.is_valid():
        form.save()
        return redirect('manage-driver')

    return render(request,'admin/updateDriver.html',
                  {'form': form, 'User':chief})


def UpdateDriverSave(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        chiefID = request.POST.get("")
        chiefUsername = request.POST.get("")
        chiefName = request.POST.get("")

        try:

            Chief.chiefID = chiefID
            Chief.chiefUsername = chiefUsername
            Chief.chiefName = chiefName
            Chief.save()

            messages.success(request, "Successfully Updated Driver Details")
        except:
            messages.error(request, "Failed to Update Driver Details")


# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='admin')
def UpdateSchedule(request, scheduleID):
    schedule = Schedule.objects.get(scheduleID=scheduleID)
    form = AddScheduleForm(request.POST or None, instance=schedule)
    if form.is_valid():
        form.save()
        return redirect('manage-schedule')

    return render(request,'admin/updateSchedule.html',
                  {'form': form, 'schedule':schedule})


def UpdateScheduleSave(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        scheduleID = request.POST.get("")
        busID = request.POST.get("")
        scheduleDeparture = request.POST.get("")
        scheduleArrival = request.POST.get("")

        try:
            Schedule.scheduleI = scheduleID
            Schedule.busID = busID
            Schedule.scheduleDeparture = scheduleDeparture
            Schedule.scheduleDeparture = scheduleArrival
            Schedule.save()

            messages.success(request, "Successfully Updated Schedule Details")
        except:
            messages.error(request, "Failed to Update Schedule Details")


# calling the function for page restrictions
@login_required(login_url='')
@allowed_users(allowed_roles='driver')
def DriverUpdateSchedule(request, scheduleID):
    schedule = Schedule.objects.get(scheduleID=scheduleID)
    form = AddScheduleForm(request.POST or None, instance=schedule)
    if form.is_valid():
        form.save()
        return redirect('driver-manage-schedule')

    return render(request,'myapp/DriverUpdateSchedule.html',
                  {'form': form, 'schedule':schedule})


def DriverUpdateScheduleSave(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        scheduleID = request.POST.get("")
        busID = request.POST.get("")
        scheduleDeparture = request.POST.get("")
        scheduleArrival = request.POST.get("")

        try:
            Schedule.scheduleI = scheduleID
            Schedule.busID = busID
            Schedule.scheduleDeparture = scheduleDeparture
            Schedule.scheduleDeparture = scheduleArrival
            Schedule.save()

            messages.success(request, "Successfully Updated Schedule Details")
        except:
            messages.error(request, "Failed to Update Schedule Details")

# end of update function

# start of delete function

def DeleteStudent(request, username):
    student = User.objects.get(username=username)
    student.delete()
    return redirect('manage-student')


def DeleteBus(request, busID):
    bus = Busses.objects.get(busID=busID)
    bus.delete()
    return redirect('manage-bus')


def DeleteSchedule(request, scheduleID):
    schedule = Schedule.objects.get(scheduleID=scheduleID)
    schedule.delete()
    return redirect('manage-schedule')


def DeleteDriver(request, username):
    chief = User.objects.get(username=username)
    chief.delete()
    return redirect('manage-driver')

# end of delete function

# start of arrived status function

def ArrivedStatus(request, scheduleID,):
    seatupdate = Schedule.objects.get(scheduleID=scheduleID)

    seatupdate.scheduleSeatVacancies += 1
    seatupdate.save()
    return redirect('reservationlist-page')


def RemoveReservation(request, reservationID,):
    # get the primary that has been pass
    reservation = Reservation.objects.get(reservationID=reservationID)

    # remove reservation once arrived
    reservation.delete()
    return redirect('reservationlist-page')

