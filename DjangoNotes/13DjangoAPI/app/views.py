from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status

from app.models import StudentEnquiry
from app.serializers import StudentEnquirySerializer
from app.forms import StudentEnquiryForm


class StudentEnquiryViewSet(viewsets.ModelViewSet):
    queryset = StudentEnquiry.objects.all()
    serializer_class = StudentEnquirySerializer

    def create(self, request):
        """Create a new StudentEnquiry"""
        serializer = StudentEnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'StudentEnquiry Inserted successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def list(self, request):
        """List all StudentEnquiries or filter by name or mobile"""
        name = request.query_params.get('name')
        mobile = request.query_params.get('mobile')

        if name:
            studentEnquiries = StudentEnquiry.objects.filter(name__icontains=name)
        elif mobile:
            studentEnquiries = StudentEnquiry.objects.filter(mobile__icontains=mobile)
        else:
            studentEnquiries = StudentEnquiry.objects.all()

        serializer = StudentEnquirySerializer(studentEnquiries, many=True)
        return Response({
            'count': studentEnquiries.count(),
            'data': serializer.data
        })
        
    from rest_framework.decorators import action

    @action(detail=False, methods=['get'], url_path='get_by_mobile')
    def get_by_mobile(self, request):
        """Get StudentEnquiry by mobile using ?mobile= """
        mobile = request.query_params.get('mobile')
        if not mobile:
            return Response({'error': 'mobile parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        studentEnquiries = StudentEnquiry.objects.filter(mobile__icontains=mobile)
        serializer = StudentEnquirySerializer(studentEnquiries, many=True)
        return Response({
            'count': studentEnquiries.count(),
            'data': serializer.data
        })



    def update(self, request, pk=None):
        """Update an entire StudentEnquiry"""
        studentEnquiry = get_object_or_404(StudentEnquiry, pk=pk)
        serializer = StudentEnquirySerializer(studentEnquiry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'StudentEnquiry Updated successfully',
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete a StudentEnquiry"""
        studentEnquiry = get_object_or_404(StudentEnquiry, pk=pk)
        studentEnquiry.delete()
        return Response({'message': 'StudentEnquiry deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    


# HTML Views for Forms and Templates
def student_create(request):
    if request.method == 'POST':
        form = StudentEnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentEnquiryForm()
    return render(request, 'student_create.html', {'form': form})


def student_list(request):
    students = StudentEnquiry.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(StudentEnquiry, pk=pk)
    return render(request, 'student_detail.html', {'student': student})
