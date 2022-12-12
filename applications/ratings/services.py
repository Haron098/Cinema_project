from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from applications.ratings.models import Rating

User = get_user_model()


def add_rating(obj, user, star):
    obj_type = ContentType.objects.get_for_model(obj)
    Rating.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()
    rating = Rating.objects.create(
        content_type=obj_type, object_id=obj.id, user=user, star=star)
    return rating


def remove_rating(obj, user):
    obj_type = ContentType.objects.get_for_model(obj)
    Rating.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()


def is_reviewer(obj, user) -> bool:
    if not user.is_authenticated:
        return False
    obj_type = ContentType.objects.get_for_model(obj)
    ratings = Rating.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user)
    return ratings.exists()


def get_reviewers(obj):
    obj_type = ContentType.objects.get_for_model(obj)
    return User.objects.filter(
        ratings__content_type=obj_type, ratings__object_id=obj.id)
