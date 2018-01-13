from .models import UserProfileInfo
from .serializers import ProfileSerializer, ProfileSerializer2
from rest_framework import generics, permissions
from .permissions import IsOnwer
from .forms import UserForm, UserProfileInfoForm
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'snippets/registration.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


class ProfileList(generics.ListAPIView):
    queryset = UserProfileInfo.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


# class ProfileDetail(APIView):
#     def get_object(self, owner):
#         try:
#             return UserProfileInfo.objects.get(user__username=owner)
#         except UserProfileInfo.DoesNotExist:
#             raise Http404
#
#     def get(self, request, owner, format=None):
#         owner = self.get_object(owner)
#         serializer = ProfileSerializer(owner)
#         return Response(serializer.data)
#
#     def put(self, request, owner, format=None):
#         owner = self.get_object(owner)
#         serializer = ProfileSerializer(owner, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = UserProfileInfo.objects.all()
    serializer_class = ProfileSerializer2
    permission_classes = (IsOnwer, )



