from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models import F

from django.forms import ModelForm
from .models import Busses
from .models import Schedule
from .models import Chief
from .models import Student
from .models import Reservation


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


# create reservation form
class ReservationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['scheduleID'].widget.attrs['readonly'] = True
            self.fields['busID'].widget.attrs['readonly'] = True
            self.fields['scheduleSeatVacancies'].widget.attrs['readonly'] = True
            self.fields['reservationID'].widget.attrs['readonly'] = True



    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.scheduleID
            return instance.busID
            return instance.scheduleSeatVacancies
            return instance.reservationID

        else:
            return self.cleaned_data['scheduleID']
            return self.cleaned_data['busID']
            return self.cleaned_data['scheduleSeatVacancies']
            return instance.reservationID

    class Meta:
        model = Reservation

        fields = ('reservationID','busID','scheduleID','scheduleSeatVacancies','studentID','studentName')

        labels = {
            'reservationID':'',
            'studentID':'',
            'studentName': '',
            'busID': '',
            'scheduleID': '',
            'scheduleSeatVacancies': '',

        }
        widgets = {
            'reservationID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student ID'}),
            'studentID': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Student ID'}),
            'studentName': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Student Name'}),
            'busID': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Bus ID'}),
            'scheduleID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bus ID'}),
            'scheduleSeatVacancies': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seats'}),

        }


# create add course form
class AddBusForm(ModelForm):
    class Meta:
        model = Busses
        fields = ('busID', 'busPlateNumber', 'busDriver','numberOfSeats', 'numberOfVacancies')

        labels = {
            'busID':'',
            'busPlateNum  ber': '',
            'busDriver': '',
            'numberOfSeats': '',
            'numberOfVacancies': '',
        }
        widgets = {
            'busID': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Bus ID'}),
            'busPlateNumber': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Bus Plate Number'}),
            'busDriver': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Bus Driver'}),
            'numberOfSeats': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Number of Seats'}),
            'numberOfVacancies': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Number of Vacancies'}),

        }


class AddScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ('scheduleID', 'busID', 'scheduleDeparture','scheduleArrival','scheduleSeatVacancies')

        labels = {
            'scheduleID':'',
            'busID': '',
            'scheduleDeparture': '',
            'scheduleArrival': '',
            'scheduleSeatVacancies':'',
        }
        widgets = {
            'scheduleID': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Schedule ID'}),
            'busID': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Bus ID'}),
            'scheduleDeparture': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Departure Time'}),
            'scheduleArrival': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Arrival Time'}),
            'scheduleSeatVacancies': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Schedule Vacancies'}),

        }


class AssignDriverForm(ModelForm):
    class Meta:
        model = Chief
        fields = ('chiefID', 'chiefUsername', 'chiefPassword','chiefName')

        labels = {
            'chiefID':'',
            'chiefUsername': '',
            'chiefPassword': '',
            'chiefName': '',
        }
        widgets = {
            'chiefID': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Chief ID'}),
            'chiefUsername': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Chief Username'}),
            'chiefPassword': forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Account Password'}),
            'chiefName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Chief Name'}),
        }


class AddStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('studentID', 'studentName', 'studentCourse','studentEmail','studentUsername','studentPassword')

        labels = {
            'studentID':'',
            'studentName': '',
            'studentCourse': '',
            'studentEmail': '',
            'studentUsername': '',
            'studentPassword': '',
        }
        widgets = {
            'studentID': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Student ID'}),
            'studentName': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Full Name'}),
            'studentCourse': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Course Taken'}),
            'studentEmail': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student Email'}),
            'studentUsername': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'studentPassword': forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'}),

        }



class UpdateStudentForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email')

        labels = {
            'username':'',
            'first_name': '',
            'last_name': '',
            'email': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Student ID'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Full Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Course Taken'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student Email'}),
        }


class UpdateDriverForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        labels = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student ID'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Taken'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student Email'}),
        }

# create reservation form
class DeleteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeleteForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['reservationID'].widget.attrs['readonly'] = True
            self.fields['studentID'].widget.attrs['readonly'] = True
            self.fields['studentName'].widget.attrs['readonly'] = True
            self.fields['busID'].widget.attrs['readonly'] = True
            self.fields['scheduleID'].widget.attrs['readonly'] = True
            self.fields['scheduleSeatVacancies'].widget.attrs['readonly'] = True



    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.reservationID
            return instance.studentID
            return instance.studentName
            return instance.busID
            return instance.scheduleID
            return instance.scheduleSeatVacancies

        else:
            return self.cleaned_data['reservationID']
            return self.cleaned_data['studentID']
            return self.cleaned_data['studentName']
            return self.cleaned_data['busID']
            return self.cleaned_data['studentName']
            return self.cleaned_data['studentID']


    class Meta:
        model = Reservation

        fields = ('reservationID','busID','scheduleID','scheduleSeatVacancies','studentID','studentName')

        labels = {
            'reservationID':'',
            'studentID':'',
            'studentName': '',
            'busID': '',
            'scheduleID': '',
            'scheduleSeatVacancies': '',

        }
        widgets = {
            'reservationID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student ID'}),
            'studentID': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Student ID'}),
            'studentName': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Student Name'}),
            'busID': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Bus ID'}),
            'scheduleID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bus ID'}),
            'scheduleSeatVacancies': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seats'}),

        }

