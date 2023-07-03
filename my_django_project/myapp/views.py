import json

from django import forms
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
    JsonResponse,
)
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

# from django.views.generic import DetailView, ListView, UpdateView

from myapp.models.person import Person


@method_decorator(csrf_exempt, name="dispatch")
class PersonView(View):

    # 단건조회(pk가 있는경우), 목록조회
    def get(self, request, pk=None):
        if pk is not None:
            # person = Person.objects.filter(id=pk).values()
            person = Person.objects.filter(id=pk).values().first()
            if not person:
                return JsonResponse({"error": "Person not found"}, status=404)
            return JsonResponse(person)
        else:
            people = Person.objects.all()
            return JsonResponse(list(people.values()), safe=False)

    # 수정
    def put(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        data = json.loads(request.body)

        person.age = data.get("age") or person.age
        person.sex = data.get("sex") or person.sex
        person.first_name = data.get("first_name") or person.first_name
        person.last_name = data.get("last_name") or person.last_name

        person.save()
        return JsonResponse(data)

        # form = self.form_class(data, instance=person)
        # if form.is_valid():
        #     form.save()
        #     return JsonResponse(data)

        # return JsonResponse({"error": "입력값이 잘못 되었습니다."}, status=400)

    # 삭제
    def delete(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        person.delete()
        return HttpResponse(status=200)

    # 등록
    def post(self, request):
        data = json.loads(request.body)

        p = Person(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            age=data.get("age"),
            sex=data.get("sex"),
        )
        p.save()
        # return HttpResponse(status=200)
        return JsonResponse({"message": "저장이 완료되었습니다"}, status=200)