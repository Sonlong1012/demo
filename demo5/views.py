from django.shortcuts import redirect, render
from .models import Member
from django.db.models import Q  # Import Q for complex queries
from django.contrib.auth.hashers import make_password

def index(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'

    if query:
        mem = Member.objects.filter(
            Q(email__icontains=query) |  # Case-insensitive search for first name
            Q(firstname__icontains=query) |  # Case-insensitive search for first name
            Q(lastname__icontains=query) |  # Case-insensitive search for last name
            Q(country__icontains=query)  # Case-insensitive search for country
        )
    else:
        mem = Member.objects.all()

    return render(request, 'index.html', {'mem': mem, 'query': query})


def add(request):
    return render(request, 'add.html')


def addrec(request):
    # Lấy thông tin từ dữ liệu POST gửi từ biểu mẫu thêm thành viên
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['country']
    e = request.POST['email']
    a = request.POST['age']
    s = request.POST['salary']
    i = request.POST['image']
    b = request.POST['password']
    # Tạo đối tượng `Member` mới với thông tin này và lưu vào cơ sở dữ liệu
    mem = Member(firstname=x, lastname=y, country=z, email=e, age=a, salary=s, image=i, password=b)
    mem.save()
    return redirect("/")


def delete(request, id):
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect("/")


def register(request):
    if request.method == 'POST':
        # Get form data
        x = request.POST.get('first', '')
        y = request.POST.get('last', '')
        e = request.POST.get('email', '')
        b = request.POST.get('password', '')
        c = request.POST.get('confirm_password', '')

        # Kiểm tra có cả hai trường mật khẩu
        if b and c:
            # # Kiểm tra xác nhận mật khẩu
            if b == c:
                # mật khẩu băm
                hashed_password = make_password(b)

                # Tạo đối tượng Member và lưu vào cơ sở dữ liệu
                mem = Member(firstname=x, lastname=y, email=e, password=hashed_password)
                mem.save()

                # chuyển đến trang index
                return redirect("index")
            else:
                # Mật khẩu không khớp, xử lý lỗi
                return render(request, 'register.html', {'error': 'Password and Confirm Password do not match'})

    # Hiển thị mẫu đăng ký
    return render(request, 'register.html')



def update(request, id):
    mem = Member.objects.get(id=id)
    return render(request, 'update.html', {'mem': mem})


# Hàm xử lý biểu mẫu
def handle_form_submission(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        hashed_password = make_password(password)


def uprec(request, id):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['country']
    e = request.POST['email']
    a = request.POST['age']
    s = request.POST['salary']
    i = request.POST['image']
    b = request.POST['password']
    c = request.POST['confirm password']
    mem = Member.objects.get(id=id)
    mem.firstname = x
    mem.lastname = y
    mem.country = z
    mem.email = e
    mem.age = a
    mem.salary = s
    mem.image = i
    mem.password = b
    mem.confirmpassword = c
    mem.save()
    return redirect("/")


from django.shortcuts import render

# Create your views here.
