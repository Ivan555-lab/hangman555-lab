from django.shortcuts import render
from .models import Course

class ManagecourseListView(ListView):
    model = Course
    template_name = 'courses/manage/course/list.html'

    def get_queryset(self):
        qs = super(ManagecourseListView, self).get_queryset()
        return qs.filter(owner=self.request.user)

# Create your views here.
