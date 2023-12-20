
from django.contrib import admin
from django.urls import path
from iacademy import views
from django.conf import settings
from django.conf.urls.static import static
from .import views,hod_views,staff_views,student_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),

    # Login Path
    path('',views.LOGIN, name ='login'),
    path('user_login/',views.user_login, name='user_login'),
    path('user_logout/',views.user_logout, name='user_logout'),
    path('register/', views.user_register,name='user_register'),
    path('register_student/',views.register_student, name = 'register_student' ),
    path('register_staff/',views.register_staff, name = 'register_staff' ),

    # Profile Upadate Path
    path('profile', views.update_profile, name ='profile'),
    path('profile/update', views.profile_update, name = 'profile_update'),
    
    #This is Hod panel path STudent
    path('hod/home', hod_views.HOME, name = 'hod_home'),
    path('hod/add/student', hod_views.ADD_STUDENT, name = 'add_student'),
    path('hod/student/view',hod_views.VIEW_STUDENT, name = 'view_student'),
    path('hod/student/view',hod_views.VIEW_STUDENT, name = 'view_student'),
    path('hod/student/edit/<str:id>',hod_views.EDIT_STUDENT, name = 'edit_student'),
    path('hod/student/update',hod_views.UPDATE_STUDENT, name = 'update_student'),
    path('hod/student/delete/<str:admin>', hod_views.DELETE_STUDENT, name = 'delete_student'),

    # This is Hod Section Staff path
    path('hod/staff/add_staff',hod_views.ADD_STAFF, name = 'add_staff'),
    path('hod/staff/view_staff',hod_views.VIEW_STAFF, name = 'view_staff'),
    path('hod/staff/edit_staff/<str:id>',hod_views.EDIT_STAFF, name = 'edit_staff'),
    path('hod/staff/update_staff/',hod_views.UPDATE_STAFF, name = 'update_staff'),
    path('hod/staff/delete_staff/<str:admin>', hod_views.DELETE_STAFF, name = 'delete_staff'),
    path('hod/staff/view_leave', hod_views.VIEW_LEAVE , name='view_leave'),
    path('hod/staff/approved_leave/<str:id>',hod_views.Approved_Leave , name = 'approved_leave'),
    path('hod/staff/disapproved_leave/<str:id>',hod_views.DisApproved_Leave , name = 'disapproved_leave'),
    path('hod/staff/feedback', hod_views.STAFF_FEEDBACK, name = 'staff_feedback'),
    path('hod/staff/feedback/save', hod_views.STAFF_FEEDBACK_SAVE, name = 'staff_feedback_save'),


    #This is Hod add courses path
    path('hod/course/add',hod_views.ADD_COURSE, name = 'add_course'),
    path('hod/course/view_courses',hod_views.VIEW_COURSE, name = 'view_course'),
    path('hod/course/edit_courses/<str:id>',hod_views.EDIT_COURSE, name = 'edit_course'),
    path('hod/course/update_curses',hod_views.UPDATE_COURSE, name = 'update_course'),
    path('hod/course/delete_courses/<str:id>' , hod_views.DELETE_COURSE, name = 'delete_course'),

    # This is Hod Section  Subject path
    path('hod/Subject/add_subject', hod_views.ADD_SUBJECT, name = 'add_subject'),
    path('hod/Subject/view_subject', hod_views.VIEW_SUBJECT, name = 'view_subject'),
    path('hod/Subject/edit_subject/<str:id>', hod_views.EDIT_SUBJECT, name = 'edit_subject'),
    path('hod/Subject/update_subject',hod_views.UPDATE_SUBJECT, name = 'update_subject'),
    path('hod/Subject/delete_subject/<str:id>',hod_views.DELETE_SUBJECT, name = 'delete_subject'),

    # This is Hod Section Session path
    path('hod/session/add_session',hod_views.ADD_SESSION , name = 'add_session'),
    path('hod/session/view_session', hod_views.VIEW_SESSION, name = 'view_session'),
    path('hod/session/edit_session/<str:id>', hod_views.EDIT_SESSION, name = 'edit_session'),
    path('hod/session/update_session',hod_views.UPDATE_SESSION, name = 'update_session'),
    path('hod/session/delete_session/<str:id>',hod_views.DELETE_SESSION, name = 'delete_session'),

    #Send Notification Path
    path('hod/staff/send_notification', hod_views.Send_Staff_Notification, name = 'send_staff_notification'),
    path('hod/staff/save_notification', hod_views.Save_Notification, name = 'save_notification'),


    # STAFF SECTION URL START
    path('staff/home',staff_views.HOME, name = 'staff_home'),
    path('staff/notifications',staff_views.NOTIFICATIONS , name = 'notifications'),
    path('staff/mark_as_done/<str:status>',staff_views.Mark_As_Done, name = 'mark_as_done'),
    path('staff/apply_leave',staff_views.Apply_Leave, name = 'apply_leave'),
    path('staff/save_leave_data', staff_views.Save_Leave_Data, name='save_leave_data'),
    path('staff/feedback',staff_views.STAFF_FEEDBACK, name= 'feedback'),
    path('staff/feedback/save', staff_views.STAFF_FEEDBACK_SAVE, name = 'feedback_save')


] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
