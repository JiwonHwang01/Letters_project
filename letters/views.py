from django.shortcuts import render, redirect
from letters.models import User, Letter
from django.contrib.auth import authenticate, login, get_user
from letters.forms import LetterForm

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
        user = None
    print(user)
    print(get_user(request))
    return render(request, 'letters/write_letter.html', {'user':user})
    
def post_letter(request):
    
    # 사용자가 POST 요청을 통해 폼을 제출한 경우
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            letter = form.save(commit=False)
            # 여기에서 sender를 현재 로그인한 사용자로 설정하거나, token을 통해 식별된 사용자로 설정합니다.
            letter.sender = request.user
            letter.save()
            return redirect('letters/')  # 익명 편지 작성 성공 페이지로 이동
    else:
        form = LetterForm()

    return render(request, 'write_anonymous_letter.html', {'form': form})

def copyToClipBoard():
    print("clipboard")
    return