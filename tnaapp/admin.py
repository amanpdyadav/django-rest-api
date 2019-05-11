# -*- coding: utf-8 -*-
import os

from django.contrib import admin
from django.contrib.auth.models import Group

from models import Info, InfoPictures, Events, EventsPictures, Member, \
    ProfilePictures, Gallery, GalleryPictures, \
    HomePictures, EventAttendees, Account, AccountFile
from tna import settings


class PhotoAdmin(admin.ModelAdmin):
    actions=['really_delete_selected']

    def get_actions(self, request):
        actions = super(PhotoAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            os.remove(os.path.join(settings.MEDIA_ROOT, str(obj.url)))
            obj.delete()

        if queryset.count() == 1:
            message_bit = "1 photoblog entry was"
        else:
            message_bit = "%s photoblog entries were" % queryset.count()
        self.message_user(request, "%s successfully deleted." % message_bit)
    really_delete_selected.short_description = "Delete selected entries"


admin.site.register(Member)
admin.site.register(HomePictures, PhotoAdmin)
admin.site.unregister(Group)
admin.site.register(ProfilePictures, PhotoAdmin)
admin.site.register(Info)
admin.site.register(InfoPictures, PhotoAdmin)
admin.site.register(Events)
admin.site.register(EventsPictures, PhotoAdmin)
admin.site.register(Gallery)
admin.site.register(GalleryPictures, PhotoAdmin)
admin.site.register(EventAttendees)


admin.site.register(AccountFile)
admin.site.register(Account)