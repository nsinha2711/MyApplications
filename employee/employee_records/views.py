from django.shortcuts import render, redirect
from .models import Employee
from django.http import HttpResponse
from django.shortcuts import render
from .forms import EmployeeForm
from django.db.models import Q
import re
from django.views.generic import ListView
from employee.config import pagination


def emp(request):
    print(request.method)
    if request.method == "POST":

        form = EmployeeForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except Exception as e:
                return "error"
        else:
            return form.errors
        # content = {'form':form}
    else:
        form = EmployeeForm()

    return render(request, "home.html", {"form": form})

def show(request):
    employees = Employee.objects.get_queryset().order_by('id')
    print(employees)
    pages = pagination(request, employees, 3)
    print(pages)
    context = {
        "items": pages[0],
        "page_range": pages[1]
    }

    return render(request, "show.html", context)

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee':employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    print(employee)
    form = EmployeeForm(request.POST, instance=employee)
    print(form)
    print(form.is_valid())
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, "edit.html",{"employee":employee})

def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")


# def normalize_query(query_string,
#                     findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
#                     normspace=re.compile(r'\s{2,}').sub):
#
#     return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]
#
# def get_query(query_string, search_fields):
#
#     query = None # Query to search for every search term
#     terms = normalize_query(query_string)
#     for term in terms:
#         or_query = None # Query to search for a given term in each field
#         for field_name in search_fields:
#             q = Q(**{"%s__icontains" % field_name: term})
#             if or_query is None:
#                 or_query = q
#             else:
#                 or_query = or_query | q
#         if query is None:
#             query = or_query
#         else:
#             query = query & or_query
#     return query
#
# def search(request):
#     query_string = ''
#     found_entries = None
#     if ('q' in request.GET) and request.GET['q'].strip():
#         query_string = request.GET['q']
#         print(query_string)
#         entry_query = get_query(query_string, ['name', 'pan_number', 'age', "gender", "email", "city"])
#         print(entry_query)
#         found_entries = Employee.objects.filter(entry_query).order_by('-name')
#         print(found_entries)
#     return render('/show', {'query_string': query_string, 'found_entries': found_entries })

# def paginating(request):
#     template = "employee/show.html"
#     object_list = Employee.objects.all()
#     pages = pagination(request, object_list, 1)
#     context = {
#         "items": pages[0],
#         "page_range": pages[1]
#                }
#     return render(request, template, context)