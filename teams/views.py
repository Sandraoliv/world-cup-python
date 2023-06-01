from django.shortcuts import render
from exceptions import *
from .models import Team
from django.forms.models import model_to_dict
from rest_framework.views import APIView, Request, Response, status


class TeamView(APIView):
    def get(self, request: Request) -> Response:
        teams = Team.objects.all()

        team_list = []
        for team in teams:
            team_dict = model_to_dict(team)
            team_list.append(team_dict)
        return Response(team_list, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
       
        try:
            teams = Team.objects.create(**request.data)
            team_dict = model_to_dict(teams)
            return Response(team_dict, status.HTTP_201_CREATED)
        except NegativeTitlesError:
            return Response({"error": "titles cannot be negative"}, status.HTTP_400_BAD_REQUEST)
        except InvalidYearCupError:
            return Response({"error": "there was no world cup this year"}, status.HTTP_400_BAD_REQUEST)
        except ImpossibleTitlesError:
            return Response({"error": "impossible to have more titles than disputed cups"}, status.HTTP_400_BAD_REQUEST)
