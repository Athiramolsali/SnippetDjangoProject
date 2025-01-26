from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import (
    TagSerializer,
    CreateSnippetSerializer,
    OverviewSerializer,
    UpdateSnippetSerializer,
)
from .models import Tag,Snippet
# Create your views here.

#Overview of snippets
class Overview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_snippets = Snippet.objects.filter(user=request.user)
        snippet_data_serializer = OverviewSerializer(all_snippets, many=True).data
        return Response(
            {
                "total_snippets": len(snippet_data_serializer),
                "snippets": snippet_data_serializer,
            }
        )
    

#Create Snippet
class CreateSnippet(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CreateSnippetSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get('title', None)
            note = serializer.validated_data.get('note', None)
            tag_title = serializer.validated_data.get('tag', None)

            tag, created = Tag.objects.get_or_create(title=tag_title)
            Snippet.objects.create(
                title=title,
                note=note,
                user=request.user,
                tag=tag
            )
            return Response(
                {"message": "Snippet Created successfully!"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


#Snippet Detail
class DetailApi(APIView):
    def get(self,request):
        all_snippets = Snippet.objects.filter(user=request.user)
        snippet_data_serializer = OverviewSerializer(all_snippets, many=True).data
        return Response({"detail":snippet_data_serializer})
    

#Snippet Update
class SnippetUpdate(APIView):
    permission_classes = [IsAuthenticated]


    def put(self, request, pk):
        # Retrieve the snippet belonging to the authenticated user
        snippet = Snippet.objects.filter(pk=pk, user=request.user).first()

        if not snippet:
            return Response(
                {"detail": "Snippet not found or you do not have permission to update it."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UpdateSnippetSerializer(snippet, data=request.data, partial=True)

        if serializer.is_valid():
            # Extract and remove the `tag` field from validated data
            tag_title = serializer.validated_data.pop('tag', None)

            # If `tag` is provided, update or create it
            if tag_title:
                # Update the existing tag associated with the snippet, or create a new one
                if snippet.tag:
                    snippet.tag.title = tag_title
                    snippet.tag.save()
                else:
                    # If no tag is associated, create or retrieve the new tag
                    tag, _ = Tag.objects.get_or_create(title=tag_title)
                    snippet.tag = tag

            # Update other fields dynamically
            for attr, value in serializer.validated_data.items():
                setattr(snippet, attr, value)

            snippet.save()
            return Response(
                {"message": "Snippet updated successfully!", "data": serializer.data},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
#Tag all list
class TagAllListApi(APIView):
    def get(self,request):
        tag_list = Tag.objects.all()
        tag_serializer = TagSerializer(tag_list,many=True)
        return Response(tag_serializer.data, status=status.HTTP_200_OK)
    

#Tag details api
class TagDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        snippets = tag.snippets.filter(user=request.user)
        snippet_data = OverviewSerializer(snippets, many=True).data
        return Response(snippet_data)


#Delete Snippet
class DeleteSnippet(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        # Fetch the snippet for the authenticated user
        snippet = Snippet.objects.filter(pk=pk, user=request.user).first()

        if not snippet:
            return Response(
                {"detail": "Snippet not found or you do not have permission to delete it."},
                status=status.HTTP_404_NOT_FOUND
            )
        snippet.delete()

        # Return the list of remaining snippets
        snippets = Snippet.objects.filter(user=request.user)
        serializer = OverviewSerializer(snippets, many=True)
        return Response(
            {
                "message": "Snippet deleted successfully!",
                "remaining_snippets": serializer.data,
            },
            status=status.HTTP_200_OK
        )


    








