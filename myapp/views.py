from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from .serializers import UploadedFileSerializer
from .models import UploadedFile, User



def driveUI(request):
  template = loader.get_template('drive.html')
  return HttpResponse(template.render())

def signup(request):
  template = loader.get_template('signup.html')
  return HttpResponse(template.render())

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

@csrf_exempt
def createUser(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            if not email or not password:
                return JsonResponse({"message": "Missing required fields"}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"message": "User already exists","status":False}, status=400)

            User.objects.create(email=email, password=password)
            return JsonResponse({"message": "User registered successfully","status":True}, status=201)

        except Exception as e:
            return JsonResponse({"message": str(e)}, status=500)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)
    
@csrf_exempt
def login_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            user = User.objects.filter(email=email, password=password).first()

            if user:
                return JsonResponse({"message": "Login successful!", "status":True})
            else:
                return JsonResponse({"message": "Invalid credentials","status":False}, status=401)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)
    return JsonResponse({"message": "Invalid request method."}, status=405)

@csrf_exempt
def fileUpload(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    uploaded_file = request.FILES.get('file')

    if not uploaded_file:
        return JsonResponse({'error': 'No file uploaded'}, status=400)

    file_instance = UploadedFile.objects.create(
        file=uploaded_file,
        name=uploaded_file.name,
        content_type=uploaded_file.content_type
    )

    serializer = UploadedFileSerializer(file_instance)
    return JsonResponse(serializer.data)

