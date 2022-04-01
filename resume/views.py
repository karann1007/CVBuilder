from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import Profile, Education, Skill


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def add_profile(request, format=None):
    data = request.data
    user = request.user
    profile = Profile()
    profile.user = user
    profile.name = data['profile_name']
    profile.first_name = data['first_name']
    profile.last_name = data['last_name']
    profile.email = data['email']
    profile.phone = data['phone']
    profile.about = data['about']
    profile.city = data['city']
    profile.street = data['street']
    profile.state = data['state']
    profile.country = data['country']
    profile.pincode = data['pincode']
    # profile.image = data['city']
    profile.previous_work = data['previous_work']
    profile.projects = data['projects']
    profile.extra_curricular = data['extra_curricular']
    # for e in Education.objects.filter(user=user):
    #     profile.education.add(profile)
    # profile.education = [e.name for e in Education.objects.filter(user=user)]
    # profile.skills = [e.name for e in Skill.objects.filter(user=user)]
    # for e in Skill.objects.filter(user=user):
    #     profile.skills.add(e.id)
    profile.save()
    return Response({'response':
        {'profile_id': profile.id,
         'profile_name' : profile.profile_name,
         'first_name': profile.first_name,
         'last_name': profile.last_name,
         'email': profile.email,
         'phone': profile.phone,
         'street': profile.street,
         'city': profile.city,
         'state': profile.state,
         'country': profile.country,
         'pincode': profile.pincode,
         'about': profile.about,
         'previous_work': profile.previous_work,
         'projects': profile.projects,
         'extra_curricular': profile.extra_curricular
         # 'education' : [{'education_id':e.id,
         #                 'education_name' : e.name ,
         #                 'school': e.school,
         #                 'score' : e.score ,
         #                 'start_date' : e.start_date ,
         #                 'end_date' : e.end_date } for e in profil] ,
         # 'skills' : [{  'skill_id' : e.id,
         #                'skill_name' : e.name ,
         #                'rating': e.rating,} for e in profile.skills]
         } }, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@renderer_classes([JSONRenderer])
def add_education(request, format=None):
    education = Education()
    data = request.data
    education.user = request.user
    education.name = data['education_name']
    education.school = data['school']
    education.score = data['score']
    education.start_date = data['start_date']
    education.end_date = data['end_date']
    education.save()
    return Response("Education saved")


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def add_skill(request, format=None):
    skill = Skill()
    data = request.data
    skill.user = request.user
    skill.name = data['skill_name']
    skill.rating = data['rating']
    skill.save()
    return Response("Skill saved")


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_user_profiles(request, format=None):
    profiles = Profile.objects.filter(user=request.user)
    return Response({'response': [
        {'profile_id': e.id,
         'profile_name' :e.profile_name,
         'first_name': e.first_name,
         'last_name': e.last_name,
         'email': e.email,
         'phone': e.phone,
         'street': e.street,
         'city': e.city,
         'state': e.state,
         'country': e.country,
         'pincode': e.pincode,
         'about': e.about,
         'previous_work': e.previous_work,
         'projects': e.projects,
         'extra_curricular' : e.extra_curricular
         } for e in profiles]}, status=status.HTTP_200_OK)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_profile_by_id(request, format=None):
    pk = request.GET.get("id", None)
    profile = Profile.objects.filter(id=pk)[0]
    return Response({'response':
        {'profile_id': profile.id,
         'profile_name' : profile.profile_name,
         'first_name': profile.first_name,
         'last_name': profile.last_name,
         'email': profile.email,
         'phone': profile.phone,
         'street': profile.street,
         'city': profile.city,
         'state': profile.state,
         'country': profile.country,
         'pincode': profile.pincode,
         'about': profile.about,
         'previous_work': profile.previous_work,
         'projects': profile.projects,
         'extra_curricular' : profile.extra_curricular
         # 'skill' : [{'skill_id':e.id,'skill_name' : e.name , 'rating' : e.rating} for e in Skill.objects.filter(user=request.user)],
         # 'education' :[{'education_id':e.id,'education_name': e.name ,'score':e.score , 'school': e.school , 'start_date' : e.start_date , 'end_date':e.end_date } for  e in  Education.objects.filter(user=request.user)]
         } }, status=status.HTTP_200_OK)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_education(request, format=None):
    educations = Education.objects.filter(user=request.user)
    return Response({'response' : [{ 'education_id' : e.id , 'education' : e.name ,'school':e.school , 'score': e.score , 'start_date': e.start_date ,'end_date' : e.end_date} for e in educations]}, status=status.HTTP_200_OK)



@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_skills(request, format=None):
    skills = Skill.objects.filter(user=request.user)
    return Response({'response': [
        {'skill_id': e.id, 'skill': e.name, 'rating': e.rating} for e in skills]}, status=status.HTTP_200_OK)







from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import CreateUserSerializer, UserSerializer

class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })



from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
