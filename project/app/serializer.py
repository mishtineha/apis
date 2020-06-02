from rest_framework import serializers,exceptions
from app.models import Profile,Address
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.response import Response


class ProfileSerializer(serializers.ModelSerializer):
    friends = serializers.SerializerMethodField('is_friends')

    def is_friends(self,Profile):
        if Profile.Friends:
            f_name = []
            for f in Profile.Friends.all():
                f_name.append(f.Name)
            return f_name
        else:
            return None

    username = serializers.SerializerMethodField('is_username')
    def is_username(self,Profile):
        return Profile.user.username

    city = serializers.SerializerMethodField('is_city')

    def is_city(self, Profile):
        if Profile.per_add:
            return Profile.per_add.city
        else:
            return None

    state = serializers.SerializerMethodField('is_state')

    def is_state(self, Profile):
        if Profile.per_add:
            return Profile.per_add.state
        else:
            return None

    country = serializers.SerializerMethodField('is_country')

    def is_country(self, profile):
        if profile.per_add:
            return profile.per_add.country
        else:
            return None
    class Meta:
        model = Profile
        fields = (
            'id',
            'username',
            'Name',
            'gender',
            'profile_pic',
            'city',
            'state',
            'phone_number',
            'country',
            'friends'
            )
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ProfileSerializer2(serializers.ModelSerializer):
    friends = serializers.SerializerMethodField('is_friends')

    def is_friends(self, Profile):
        if Profile.Friends:
            f_name = []
            for f in Profile.Friends.all():
                f_name.append(f.Name)
            return f_name
        else:
            return None

    username = serializers.SerializerMethodField('is_username')

    def is_username(self, Profile):
        return Profile.user.username

    city = serializers.SerializerMethodField('is_city')
    def is_city(self,Profile):
        if Profile.per_add:
            return Profile.per_add.city
        else:
            return None
    
    state = serializers.SerializerMethodField('is_state')
    def is_state(self,Profile):
        if Profile.per_add:
            return Profile.per_add.state
        else:
            return None

    country = serializers.SerializerMethodField('is_country')
    def is_country(self,profile):
        if profile.per_add:
            return profile.per_add.country
        else:
            return None

    class Meta:
        model = Profile
        fields = (
            'id',
            'username',
            'Name',
            'gender',
            'profile_pic',
            'city',
            'state',
            'country',
            'friends'
            )
           
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self,data):
        username = data.get("username","")
        password = data.get("password","")
        if username and password:
            user = authenticate(username = username,password = password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    msg = "user is not active"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "unable to login with this credential"
                raise exceptions.ValidationError(msg)
        else:
            raise exceptions.ValidationError("Error message")
        return data

class UserSerializer(serializers.Serializer):
    def validate(self,data):
        try:
            x = data['username']
            x = data['Name']
            x = data['password']
            x = data['phone_number']
            x = data['gender']
            x = data['dob']
            x = data['friends']
            try:
                x = int(data['phone_number'])
            except:
               return ({'response':"phone_number must contain only integer"},False)
            return (data,True)
        except Exception as e:
            return ({'response': str(e)+" not found"},False)


    def create(self,Validated_data):

        try:
            u = get_user_model().objects.get(username = Validated_data['username'])
            return {'response':"username already exist"}
        except:
            pass
        try:
            p = Profile.objects.get(phone_number=Validated_data['phone_number'])
            return {'response': "phone number already exist"}

        except:
            pass
        friends = Validated_data['friends'].split(",")
        f = Profile.objects.filter(user__username__in=friends)
        if len(f) != len(friends):
            return {"response" :"friend's username does not exist"}

        user = get_user_model().objects.create(
            username = Validated_data['username'],
            )
        user.set_password(Validated_data['password'])
       
        
        P1 = Profile.objects.create(user = user,
                                    Name = Validated_data['Name'],
                                    phone_number = Validated_data['phone_number'],
                                    gender = Validated_data['gender'],
                                    dob = Validated_data['dob'],
                                    )
        for friend in f:
            P1.Friends.add(friend)
        P1.save()
        
        user.save()
        return {'response':"user created successfully"}



         
