from django.shortcuts import render

# Create your views here.
import json

from django.shortcuts import render
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .serializers import PlayerSerializer, Playerposition,Teamdata,MWserializer,PlayerUpdateSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from .models import Player
from django.http import HttpResponse
from rest_framework import generics















class Playersview(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            elements = data.get('elements', [])
            element_types = data.get('element_types', [])
            team = data.get('teams', [])

            player_serializer = PlayerSerializer(elements, many=True)
            player_data = player_serializer.data

            position_serializer = Playerposition(element_types, many=True)
            position_data = position_serializer.data

            team_serializer = Teamdata(team, many=True)
            aboutteam = team_serializer.data

            combined_data = {}
            for player in player_data:
                player_id = player['element_type']
                for position in position_data:
                    if position['id'] == player_id:
                        player['position'] = position['singular_name']
                        combined_data[player['id']] = player
                        break

                team_id = player['team']
                for team in aboutteam:
                    if team['id'] == team_id:
                        player['team_name'] = team['name']
                        combined_data[player['id']] = player
                        break

            return Response(list(combined_data.values()), status=status.HTTP_200_OK)
        else:
            return Response("Failed to fetch data", status=response.status_code)





class HighestView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            elements = data.get('elements', [])

            sorted_players = sorted(elements, key=lambda x: x.get('total_points', 0), reverse=True)

            ranked_players = []
            for idx, player in enumerate(sorted_players, start=1):
                player_info = {
                    'rank': idx,
                    'name': player.get('web_name', ''),
                    'total_points': player.get('total_points', 0),
                    'goals': player.get('goals_scored', 0),
                    'assists': player.get('assists', 0),
                    'cleansheets': player.get('clean_sheets', 0),
                    'saves': player.get('saves', 0),
                    'id': player.get('id'),
                    'image': player.get('photo')
                }
                ranked_players.append(player_info)

            return Response(ranked_players, status=status.HTTP_200_OK)
        else:
            return Response("Failed to fetch data", status=response.status_code)



# @api_view(('GET',))
# def matchweeklive(request, id):
#     url = f'https://fantasy.premierleague.com/api/event/{id}/live/'
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         data = response.json()
#         mw = data['elements']
#         serializer = MWserializer(mw, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     else:
#         return Response("Failed to fetch data", status=response.status_code)













class PlayerSave(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            players_data = data.get('elements', [])  # Assuming 'elements' contains player data

            for player_data in players_data:
                web_name = player_data.get('web_name')
                first_name = player_data.get('first_name')
                second_name = player_data.get('second_name')
                team = player_data.get('team')
                element_type = player_data.get('element_type')
                minutes = player_data.get('minutes')
                goals_scored = player_data.get('goals_scored')
                assists = player_data.get('assists')
                clean_sheets = player_data.get('clean_sheets')
                saves = player_data.get('saves')
                photo = player_data.get('photo')
                influence = player_data.get('influence')
                total_points = player_data.get('total_points')
                selected_by_percent = player_data.get('selected_by_percent')
                value_form = player_data.get('value_form')
                value_season = player_data.get('value_season')

                # Create or update Player instances
                player, created = Player.objects.get_or_create(
                    web_name=web_name,
                    first_name=first_name,
                    second_name=second_name,
                    defaults={
                        'team': team,
                        'element_type': element_type,
                        'minutes':minutes,
                        'goals_scored':goals_scored,
                        'assists':assists,
                        'clean_sheets':clean_sheets,
                        'saves':saves,
                        'photo':photo,
                        'influence':influence,
                        'total_points':total_points,
                        'selected_by_percent':selected_by_percent,
                        'value_form' : value_form,
                        'value_season':value_season




                    }
                )

                # Save the Player instance
                player.save()

            return Response({'message': 'Data saved successfully'})
        else:
            return Response({'message': 'Failed to fetch data from the API'})















def Plsave(request):
    team_names = {
        1:'Arsenal',
        2:'Aston Villa',
        3:'Bournemouth',
        4:'Brentford',
        5:'Brighton',
        6:'Burnley',
        7:'Chelsea',
        8:'Crystal Palace',
        9:'Everton',
        10:'Fulham',
        11:'Liverpool',
        12:'Luton',
        13:'Man city',
        14:'Man United',
        15:'Newcastle United',
        16:'Nottingham Forest',
        17:'Sheffield Unied',
        18:'Spurs',
        19:'West Ham',
        20:'Wolves'


    }


    players = Player.objects.all()  # Retrieve all Player objects

    for player in players:
        team_number = player.team
        if team_number in team_names:
            player.team_name = team_names[team_number]
            player.save()

    return HttpResponse("Teams updated successfully")

def Position(request):
    team_elementsss = {
        1:"Goalkeeper",
        2:"Defender",
        3:"Midfielder",
        4:"Forward"
    }

    position = Player.objects.all()
    for i in position:
        position_num = i.element_type
        if position_num in team_elementsss:
            i.position = team_elementsss[position_num]
            i.save()
    return HttpResponse('position updated successfully')


class Teamcreate(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self,request,player_id):
        team = get_object_or_404(Player,id=player_id)




