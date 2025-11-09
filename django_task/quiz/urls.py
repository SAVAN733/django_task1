from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import QuizViewSet, QuestionViewSet, AnswerViewSet, EventViewSet

router = DefaultRouter()
router.register("quiz", QuizViewSet)
router.register("question", QuestionViewSet)
router.register("answer", AnswerViewSet)
router.register("event", EventViewSet)

urlpatterns = [
    path("", include(router.urls))
]
