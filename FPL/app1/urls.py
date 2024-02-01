

from django.urls import path

from .views import Playersview,HighestView,PlayerSave
from  . import views

urlpatterns = [
    path('player-details/',Playersview.as_view(), name='player-details'),
    path('hgrated/',HighestView.as_view(),name='high_rated'),
    path('playersave/',PlayerSave.as_view(),name='playersave'),
    # path('matchweek/<int:id>/',views.matchweeklive,name='matchweek'),
    # path('update/',views.update_team,name='ssa'),
    # path('plrsave/',views.Position),
    # path('teamsave/',views.Plsave),
]


