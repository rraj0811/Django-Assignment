from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Cars.forms import InputForm
from .models import Cars, otherDetails
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.http import HttpResponse


# Create your views here.

def base(request):

    return render(request, 'cars/base.html')


@login_required
def index(request):

    return render(request, 'cars/index.html')


@login_required
def available(request):

    # cars_queryset = Cars.objects.all()
    # serialized_data = CarSerializer(cars_queryset, many=True)
    # context = JSONRenderer().render(serialized_data.data)
    # json1 = json.dumps(context)
    # print(context)

    context = {
        'cars' : Cars.objects.all(),
    }
    # print(context['cars'])

    return render(request, 'cars/available.html', context)

# @app.route('/images/<string:pid>', methods=['GET', 'POST'])
@login_required
def get_image(pid, request):
    print(pid)
    return render(request, 'disp.html', {'img' : pid})

@login_required
def search(request):
    query = request.GET['query']
    context = {
        'cars' : Cars.objects.filter(CarName__icontains = query),
    }

    return render(request, 'cars/search.html', context)

@login_required()
def book(request,id):
    
    car_details = Cars.objects.filter(id=id).first()
    if request.method == 'POST':
       form = InputForm(request.POST)
       if form.is_valid():
        form.save()
        Cars.objects.filter(id=id).update(IsAvailable="No")
        subject = "Booked a car"
        email_template_name = "cars/book_email.txt"
        c = {"name":request.user.username,
        "email": request.user.email,
        "carName" : car_details.CarName,
        "carNumber": car_details.CarNumber,
        "Fare": (car_details.CostPerDay) * form.cleaned_data.get('NumberOfDays'),
        'domain':'127.0.0.1:8000',
        'site_name': 'Website',
        "uid": urlsafe_base64_encode(force_bytes(request.user.pk)),
        "user": request.user,
        'token': default_token_generator.make_token(request.user),
        'protocol': 'http',
        }
        email = render_to_string(email_template_name, c)
        try:
            send_mail(subject, email, 'sunnycool1811@gmail.com' , [request.user.email], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        # messages.success(request, 'A message with reset password instructions has been sent to your inbox.')

        # account_sid = os.environ["AC9238a848f877b195c8d6f4dbf965287b"]
        # auth_token = os.environ["2690d4a43cec7f26a707e1f8f1cafcfd"]

        # client = Client(account_sid, auth_token)

        # client.messages.create(
        #     to = request.user.phonenumber,
        #     from_= "9381335252",
        #     body="You have booked a car"
        # )
        return render(request, "cars/thank.html")
    else:
        form=InputForm()
    return render(request, "cars/book.html", {'form':form,'car_details':car_details})

