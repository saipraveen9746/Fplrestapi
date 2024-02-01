from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    web_name = serializers.CharField()
    first_name = serializers.CharField()
    second_name = serializers.CharField()
    team = serializers.IntegerField()
    element_type = serializers.IntegerField()
    minutes = serializers.IntegerField()
    goals_scored = serializers.IntegerField()
    assists = serializers.IntegerField()
    clean_sheets = serializers.IntegerField()
    saves = serializers.IntegerField()
    influence = serializers.CharField()
    total_points = serializers.IntegerField()
    photo = serializers.CharField()
    selected_by_percent = serializers.CharField()
    value_form = serializers.CharField()
    value_season = serializers.CharField()
    def create(self, validated_data):
        return Player.objects.create(**validated_data)


class PlayerUpdateSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        # Maps each player instance by its ID for easier update
        player_mapping = {player.id: player for player in instance}

        updated_players = []
        for player_data in validated_data:
            player_id = player_data['id']
            player_instance = player_mapping.get(player_id, None)

            if player_instance is not None:
                player_serializer = PlayerDetailSerializer(instance=player_instance, data=player_data, partial=True)
                if player_serializer.is_valid():
                    updated_players.append(player_serializer.save())
                else:
                    # Handle serializer errors here if needed
                    pass

        return updated_players


class Playerposition(serializers.Serializer):
    id = serializers.IntegerField()
    plural_name = serializers.CharField()
    singular_name = serializers.CharField()

    def create(self, validated_data):
        return Player.objects.create(**validated_data)

class Teamdata(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

    def create(self, validated_data):
        return Player.objects.create(**validated_data)
class HGpoint(serializers.Serializer):
    web_name = serializers.CharField()
    total_points = serializers.IntegerField()
    goals_scored = serializers.IntegerField()
    assists = serializers.IntegerField()
    clean_sheets = serializers.IntegerField()
    saves = serializers.IntegerField()
class MWserializer(serializers.Serializer):
    id = serializers.IntegerField()
    stats = serializers.CharField()
    explain = serializers.CharField()





