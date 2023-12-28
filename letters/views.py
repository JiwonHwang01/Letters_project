from django.shortcuts import render, redirect
from letters.models import User, Letter
from django.contrib.auth import authenticate, login, get_user
from letters.forms import LetterForm
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'letters/index.html')

def letter(request, data_id):
    letter = Letter.objects.get(id=data_id)
    return render(request, 'letters/letter_detail.html',{'letter':letter})

def mypage(request):
    username = get_user(request)
    all_letters = Letter.objects.filter(user=username).order_by("-pub_date")
    print(get_user(request))
    return render(request, 'letters/my_page.html', {'letter_list':all_letters, 'username':get_user(request)})

def write_letter(request, token):
    # 여기에서 token을 사용해 사용자 식별 및 인증 로직을 추가
    try:
        user = User.objects.get(lettercase_url=token)
    except User.DoesNotExist:
        print("WriteLetter Exception : DoesNotExist")
        user = None
    
    return render(request, 'letters/write_letter.html', {'user':user})
    
def post_letter(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username = request.POST.get("user"))
            form = LetterForm(request.POST)
            #form.fields['user'].queryset = User.objects.filter(username=request.POST.get("user"))
        except User.DoesNotExist:
            print("PostLetter Exception : DoesNotExist")
            return redirect('/letters/', status = 404)
        
        print(form)
        if form.is_valid():
                letter = form.save(commit=False)
                print("valid")
                letter.user = user
                letter.save()
                return redirect('/letters/', status = 200)  # 익명 편지 작성 성공
    
    else:
        print("PostLetter Invalidation : Post Request Invalid")
        form = LetterForm()

    return redirect('/letters/', status = 400)

