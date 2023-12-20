from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from iacademy.models import Course, Staff_Feedback, Staff_leave, Student, Staff, Subject,Staff_notification
from django.contrib import messages

@login_required(login_url='/')
def HOME (request):
    return render (request, 'staff/home.html') 


@login_required(login_url='/')
def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id

        notification = Staff_notification.objects.filter(staff_id = staff_id)
        context = {
            'notification': notification,
        }

        return render (request, 'staff/notification.html',context)

@login_required(login_url='/')
def Mark_As_Done(request,status):
    notification = Staff_notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notifications')

@login_required(login_url='/')
def Apply_Leave(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
        
        staff_history = Staff_leave.objects.filter(staff_id=staff_id)

        context = {
            'staff_history': staff_history,
        }
    return render(request, 'staff/apply_leave.html',context)

@login_required(login_url='/')
def Save_Leave_Data(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        staff = Staff.objects.get(admin = request.user.id)

        leave = Staff_leave(
          staff_id = staff,
          date = leave_date,
          message = leave_message,

        )

        leave.save()
        messages.success(request,'Successfully Applied!')

        return redirect('apply_leave')
    

#========  FeedBack Function ==========

def STAFF_FEEDBACK(request):
    staff_id = Staff.objects.get(admin = request.user.id)
    feedback_history = Staff_Feedback.objects.filter(staff_id=staff_id)

    context = {
        'feedback_history':feedback_history,
    }
    return render(request, 'staff/feedback.html', context)


def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        
        staff = Staff.objects.get(admin=request.user.id)
        feedback = Staff_Feedback(
            staff_id = staff, 
            feedback = feedback,
            feedback_reply = "",
        )

        feedback.save()
        return redirect('feedback')