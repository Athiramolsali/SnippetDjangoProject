from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CreateSnippet,Overview,DetailApi,SnippetUpdate,TagAllListApi,TagDetailAPI,DeleteSnippet


urlpatterns = [
    path('user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create-snippet', CreateSnippet.as_view(), name='create-snippet'),
    path('overview', Overview.as_view(), name='overview'),
    path('detail', DetailApi.as_view(), name='detail'),
    path('snippets/<int:pk>/update/', SnippetUpdate.as_view(), name='snippet_update'),
    path('taglist', TagAllListApi.as_view(), name='taglist'),
    path('tagdetail', TagDetailAPI.as_view(), name='tagdetail'),
    path('snippets/<int:pk>/delete/', DeleteSnippet.as_view(), name='snippet_delete'),



    
    
    ]