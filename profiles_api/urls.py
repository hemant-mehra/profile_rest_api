from django.urls import path,include
from profiles_api.views import HelloApiView,HelloVeiwSet,UserProfileViewSet,UserLoginApiView,UserProfileFeedViewSet
from rest_framework.routers import DefaultRouter

# used for viewsets
router=DefaultRouter()
router.register("hello-viewset",HelloVeiwSet,base_name="hello_viewset")
router.register("profile",UserProfileViewSet)
router.register("feed",UserProfileFeedViewSet)



urlpatterns = [
    path('hello-view/',HelloApiView.as_view()),
    path("login/",UserLoginApiView.as_view()),
    path("",include(router.urls)),
]

