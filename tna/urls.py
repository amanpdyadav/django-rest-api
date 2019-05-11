from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from tnaapp import homeview, accountview, contactview, eventview, galleryview, infoview, \
    loginview, memberview, datalist, register_event, passwordReset, helper_functions

admin.autodiscover()

urlpatterns = patterns(
    '',
    url('^api/login/$',            loginview.login),
    url('^api/all/$',              homeview.getAllData),
    url('^api/info/$',             infoview.infoHandler),
    url('^api/events/$',           eventview.eventsHandler),
    url('^api/member/$',           memberview.memberHandler),
    url('^api/gallery/$',          galleryview.galleryHandler),
    url('^api/uploadAccount/$',    accountview.upload),
    url('^api/contact/$',          contactview.contact),

    url('^api/updateprofilepic/$', memberview.uploadProfilePic),

    url('^api/resetpassword/(?P<pr_token>\w+)/$',    passwordReset.passwordReset),
    url('^api/passwordresetrequest/$',               passwordReset.passwordResetRequest),

    url('^api/resendverification/$',                 helper_functions.resendVerification),
    url('^api/verifyemail/(?P<ev_token>\w+)/$',      helper_functions.emailVerification),

    url('^api/verifymember/(?P<mem_id>\w+)/$',       accountview.verifyMember),
    url('^api/verifypayment/(?P<attendee_id>\w+)/$', accountview.verifyEventPayment),

    url('^api/registerforevent/(?P<event_id>\d+)/$', register_event.registrationForEvent),

    url(r'^api/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # # admin
    url(r'^admin/',                                 include(admin.site.urls)),

    # # Data Generate
    url(r'^data/', datalist.generateData),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)