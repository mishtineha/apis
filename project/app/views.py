from django.shortcuts import render
from rest_framework.views import APIView
from app.serializer import ProfileSerializer,ProfileSerializer2,LoginSerializer,UserSerializer,AddressSerializer
from app.models import Profile,Address
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from django.contrib.auth import login as django_login,logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import mixins
#from django.contrib.auth.models import User

class ProfileAPIView(APIView):
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    def get(self,request):
        profile = Profile.objects.filter(user = self.request.user)
        serializer = ProfileSerializer(profile,many=True)
        return Response(serializer.data,status = 200)
    def patch(self,request):
        profile = Profile.objects.get(user = self.request.user)
        serializer = ProfileSerializer(profile,data = request.data,partial=True)

        if serializer.is_valid():
            try:
                friends = request.data['friends'].split(",")
                f = Profile.objects.filter(user__username__in=friends)
                if len(f) != len(friends):
                    return Response(data="friend's username does not exist")
                for friend in f:
                    profile.Friends.add(friend)
                profile.save()

            except:
                pass
            u = profile.user
            try:
                u.username = request.data["username"]
                try:
                    u.save()
                except Exception as e:
                    return Response(data="username already exist")
            except KeyError:
                pass
            serializer.save()
            return Response(data = serializer.data)
        return Response(data = "wrong parameters")

class ProfileAPIView2(generics.GenericAPIView,mixins.ListModelMixin):
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer2
    #queryset = Profile.objects.all()
    def get_queryset(self):
        queryset = Profile.objects.exclude(user = self.request.user)
        return queryset
    
    lookup_field = 'id'
    filterset_fields = ('gender','per_add__city')
    def get(self,request):
        queryset = Profile.objects.exclude(user = self.request.user)
        return self.list(request)


class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        django_login(request,user)
        token, created = Token.objects.get_or_create(user = user)
        return Response({'token':token.key},status = 200)

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )
    def post(self,request):
        django_logout(request)
        return Response(status = 200)

class CreateUserView(APIView):
    permission_class = (AllowAny,)
    def post(self,request):
        # serializer = UserSerializer(data = request.data)
        response,is_valid = UserSerializer.validate(self,data = request.data)
        if is_valid:
            response = UserSerializer.create(self,Validated_data= response)


        return Response(response,status = 200)

class Addressview(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    def post(self,request):
        serializer = AddressSerializer(data = request.data)
        if serializer.is_valid():
            a = Address(Street_add=request.data['street_add'],
                                        city = request.data['city'],
                                        state = request.data['state'],
                                        pincode = request.data['pincode'],
                                        country = request.data['country'])
            a.save()
            p = Profile.objects.get(user = self.request.user)
            p.per_add = a
            p.save()
            return Response(data=request.data)
        return Response(data="wrong parameters")


    def patch(self,request):
        add = Profile.objects.get(user = self.request.user).per_add
        serializer = AddressSerializer(add,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data="wrong parameters")

class Company_addressview(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    def post(self,request):
        serializer = AddressSerializer(data = request.data)
        if serializer.is_valid():
            a = Address(Street_add=request.data['street_add'],
                                        city = request.data['city'],
                                        state = request.data['state'],
                                        pincode = request.data['pincode'],
                                        country = request.data['country'])
            a.save()
            p = Profile.objects.get(user = self.request.user)
            p.company_add = a
            p.save()
            return Response(data=request.data)
        return Response(data="wrong parameters")


    def patch(self,request):
        add = Profile.objects.get(user = self.request.user).company_add
        serializer = AddressSerializer(add,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data="wrong parameters")



