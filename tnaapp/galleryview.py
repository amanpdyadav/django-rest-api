# -*- coding: utf-8 -*-
import json

from django.core.files.storage import default_storage
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from authentication.authentication import isAuthenticated
from helper_functions import notlogged, getCleanObject
from models import GalleryPictures, Gallery
from tna.settings import MEDIA_ROOT
from tnaapp.helper_functions import JSONResponse
from tnaapp.homeview import getGalleries


# Method: DELETE
# DELETE GALLERY
# {
#   type: 'gallery',
#   gallery_id: 1
# }
#
# DELETE SINGLE PIC
# {
#   type: 'picture',
#   gallery_id: 1 ,
#   pic_id: 1
# }
#
# UPDATE GALLERY POST
# {
#   type: 'gallery',
#   gallery_id: 1 ,
#   title: '',
#   description: '',
# }
#
# UPDATE COVER PHOTO POST
# {
#   type: 'cover_photo',
#   gallery_id: 1 ,
#   pic_id: 1,
#   title: '',
#   description: '',
# }
#
# UPLOAD GALLERY PUT
# {
#   title: '',
#   description: '',
# }


@csrf_exempt
def galleryHandler(request):
    authMember = isAuthenticated(request)
    if not authMember:
        notlogged()
    else:
        if request.method == 'PUT':
            return uploadgallery(request, authMember)
        elif request.method == 'POST':
            res = JSONParser().parse(request)
            if res['type'] == 'gallery':
                return updategallery(request, res['gallery_id'])
            if res['type'] == 'cover_photo':
                return updatecover_photo(request, res['gallery_id'], res['pic_id'])
        elif request.method == 'DELETE':
            res = JSONParser().parse(request)
            if res['type'] == 'gallery':
                return deletegallery(request, res['gallery_id'])
            elif res['type'] == 'picture':
                return deletegallery(request, res['gallery_id'], res['pic_id'])



def updatecover_photo(gallery_id, pic_id):
    pics_relate_to_gallery = GalleryPictures.objects.filter(gallery_id=gallery_id)
    for p in pics_relate_to_gallery:
        p.cover_photo = ""
        p.save()

    pic = GalleryPictures.objects.get(id=pic_id)
    pic.cover_photo = pic.url
    pic.save()
    galleryQuerySet = Gallery.objects.filter(id=gallery_id)
    return JSONResponse(getCleanObject(json.loads(serialize('json', galleryQuerySet))), status=200)


def updategallery(request, gallery_id):
    try:
        gallery_obj = Gallery.objects.get(id=gallery_id)
    except:
        return JSONResponse({"message": "Gallery not found with given id."}, status=400)

    res = JSONParser().parse(request)
    files = request.FILES.getlist("files")
    if not res['title'] or not ['description']:
        return JSONResponse({"message": "Please add both title and description."}, status=400)

    if res['title']:
        gallery_obj.title = res['title']
    if res['description']:
        gallery_obj.description = res['description']
    gallery_obj.save()

    if len(files) > 0:
        try:
            for file in files:
                pic = GalleryPictures(url=file, gallery=gallery_obj)
                pic.save()
            galleryQuerySet = Gallery.objects.filter(id=gallery_id)
            return JSONResponse(getCleanObject(json.loads(serialize('json', galleryQuerySet))), status=200)
        except:
            gallery_obj.delete()
            return JSONResponse({"message": "Unexpected error occurred. May be too much file to upload."}, status=400)

    if not GalleryPictures.objects.filter(gallery=gallery_obj):
        return JSONResponse({"message": "Please upload at least one image file."}, status=400)


def uploadgallery(request, authUser):
    res = JSONParser().parse(request)
    files = request.FILES.getlist("files")
    if not res['title'] or not res['description']:
        return JSONResponse({'message': 'Both title and description is required'}, status=400)
    if len(files) > 0:
        gallery_obj = Gallery(owner=authUser, title=res['title'], description=res['description'])
        gallery_obj.save()
        check_first = True
        try:
            for file in files:
                pic = GalleryPictures(url=file, gallery=gallery_obj)
                pic.save()
                if check_first:
                    pic.cover_photo = pic.url
                    check_first = False
                    pic.save()
            galleryQuerySet = Gallery.objects.filter(id=gallery_obj.id)
            return JSONResponse(getCleanObject(json.loads(serialize('json', galleryQuerySet))), status=200)
        except:
            gallery_obj.delete()
            return JSONResponse({'message': 'Unexpected error, may be too much files to upload.'}, status=400)
    else:
        return JSONResponse({'message': 'No Image files selected'}, status=400)


def deletegallery(request, gallery_id):
    try:
        galler_obj = Gallery.objects.get(owner=request.user, id=gallery_id)
    except:
        return JSONResponse({"message": "Gallery not found with given id."}, status=400)
    piclist = GalleryPictures.objects.filter(gallery=galler_obj)
    for pic in piclist:
        default_storage.delete(MEDIA_ROOT + '/' + str(pic.url))
    pic.delete()
    galler_obj.delete()
    return JSONResponse({'gallery': getGalleries()}, status=200)


def delete_single_pic(request, gallery_id, pic_id):
    try:
        pic = GalleryPictures.objects.get(gallery__owner=request.user, id=pic_id)
    except:
        return JSONResponse({"message": "Pics not found with given id."}, status=400)

    if pic.cover_photo:
        return JSONResponse({"message": "Cover photo can not be deleted."}, status=400)
    default_storage.delete(MEDIA_ROOT + '/' + str(pic.url))
    pic.delete()
    check_empty = GalleryPictures.objects.filter(gallery__owner=request.user)
    if check_empty.count() == 0:
        Gallery.objects.get(id=gallery_id).delete()

    galleryQuerySet = GalleryPictures.objects.filter(id=gallery_id)
    return JSONResponse(getCleanObject(json.loads(serialize('json', galleryQuerySet))), status=200)
