from urllib import response

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import NoteSerializer 

from .models import Note
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class NoteAPIView(APIView):

    def get(self,request):
        notes=Note.objects.all()
        serializer=NoteSerializer(notes,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class NoteDetailAPIView(APIView):
    def get(self,request,id):
        note=Note.objects.get(id=id)
        serializer=NoteSerializer(note)
        return Response(serializer.data)
    
  
    def put(self, request, id):
        note = Note.objects.get(id=id)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        note = Note.objects.get(id=id)
        note.delete()
        return Response({"message": "Note deleted successfully"})
    

class NoteListCreateAPIView(ListCreateAPIView):
    queryset=Note.objects.all()
    serializer_class=NoteSerializer

class NoteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Note.objects.all()
    serializer_class=NoteSerializer
    