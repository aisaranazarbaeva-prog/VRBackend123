from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContactMessage
from .serializers import ContactMessageSerializer

@api_view(['GET'])
def get_contacts(request):
    return Response({
        "phone": "+7 912 608-44-94",
        "email": "info@npp-law.ru",
        "telegram": "@Postvr",
        "workHours": "9:00–21:00"
    })

@api_view(['POST'])
def send_message(request):
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "ok"})
    return Response(serializer.errors, status=400)