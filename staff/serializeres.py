from rest_framework.serializers import ModelSerializer

from .models import Worker
from .models import Education
from .models import Career
from .models import Reward
from .models import Publication
from .models import ScienceInterest


class WorkersListSerializer(ModelSerializer):
    '''Сериализатор для страницы со списком всех сотрудников'''

    class Meta:
        model = Worker
        fields = [
            'id',
            'last_name',
            'first_name',
            'middle_name',
            'photo',
            'position',
            'academic_rank',
            'mail',
        ]


class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'study_finishing', 'study_description']


class CareerSerializer(ModelSerializer):
    class Meta:
        model = Career
        fields = ['id', 'career_description', 'career_period']


class RewardSerializer(ModelSerializer):
    class Meta:
        model = Reward
        fields = ['id', 'reward_year', 'reward_description']


class ScienceInterestSerializer(ModelSerializer):
    class Meta:
        model = ScienceInterest
        fields = ['id', 'science_interest']


class PublicationSerializer(ModelSerializer):
    class Meta:
        model = Publication
        fields = [
            'id',
            'publication_year',
            'publication_description',
            'publication_link'
        ]


class WorkersPageSerializer(ModelSerializer):
    '''Сериализатор для личной страницы сотрудника'''

    education = EducationSerializer(many=True, read_only=True)
    career = CareerSerializer(many=True, read_only=True)
    rewards = RewardSerializer(many=True, read_only=True)
    science_interests = ScienceInterestSerializer(many=True, read_only=True)
    publications = PublicationSerializer(many=True, read_only=True)

    class Meta:
        model = Worker
        fields = [
            'id',
            'last_name',
            'first_name',
            'middle_name',
            'photo',
            'position',
            'academic_rank',
            'mail',
            'phone',
            'adress',
            'google_academy',

            'education',
            'career',
            'rewards',
            'science_interests',
            'publications'
        ]