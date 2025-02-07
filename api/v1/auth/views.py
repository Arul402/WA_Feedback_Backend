from django.http import JsonResponse

def example_view(request):
    return JsonResponse({"message": "This is an example view from auth"})
