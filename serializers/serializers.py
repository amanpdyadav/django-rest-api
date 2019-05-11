from rest_framework import serializers

from authentication.passwordHasher import hashpassword
from tnaapp.models import Member, Info, Events, Gallery, EventAttendees, Account


class getMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'post_type', 'post', 'first_name', 'last_name',
                  'email', 'address', 'date_of_birth', 'phone', 'url',
                  'fb_url', 'tw_url', 'ln_url', 'github', 'google', 'skype',)

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'token', 'password', 'post_type', 'post',
                  'first_name',  'last_name', 'email', 'address',
                  'date_of_birth', 'phone', 'url', 'fb_url', 'tw_url',
                  'ln_url', 'github', 'google', 'skype', 'ev_token')


    def create(self, validated_data):
        validated_data['password'] = hashpassword(validated_data['password'])
        return Member.objects.create(**validated_data)


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('id','title', 'description', 'date_posted', 'owner',)


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id','owner', 'title', 'description', 'location', 'datetime', 'registration',)


class GallerySerializer(serializers.ModelSerializer):
    gallery = MemberSerializer()
    class Meta:
        model = Gallery
        fields = ('id','gallery', 'title', 'description',)


class EventAttendeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAttendees
        fields = ('event', 'name', 'no_adults', 'no_family', 'no_children', 'no_vegetarian', 'total',)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('year', 'month', 'day', 'beneficiary', 'amount', 'ref_num',)