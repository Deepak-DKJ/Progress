from .serializers import ChapterItemSerializer
from django.http import HttpResponse
from .models import ChapterItem
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
# Create your views here.
class ChapterItemList(ListAPIView):
    queryset = ChapterItem.objects.all()
    serializer_class = ChapterItemSerializer

class ChapterItemCreate(CreateAPIView):
    queryset = ChapterItem.objects.all()
    serializer_class = ChapterItemSerializer

class ChapterItemDestroy(DestroyAPIView):
    queryset = ChapterItem.objects.all()
    serializer_class = ChapterItemSerializer
    lookup_field = 'id'

class ChapterItemUpdate(UpdateAPIView):
    queryset = ChapterItem.objects.all()
    serializer_class = ChapterItemSerializer
    lookup_field = 'id'
    
def home(request):
    return HttpResponse("Home Page")