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
    # print(get_user(request))
    return render(request, 'letters/my_page.html', {'letter_list':all_letters, 'username':get_user(request)})

def write_letter(request, token):
    # 여기에서 token이 유효한지 판단
    try:
        user = User.objects.get(lettercase_url=token)
    except User.DoesNotExist:
        request.session['fail_reason'] = 'url_not_found'
        return redirect('/letters/')
    
    return render(request, 'letters/write_letter.html', {'user':user})
    
def post_letter(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username = request.POST.get("user"))
            form = LetterForm(request.POST)
            
        except User.DoesNotExist:
            # print("PostLetter Exception : DoesNotExist")
            request.session['fail_reason'] = 'user_not_exist'
            return redirect('/letters/')
        
        print(form)
        if form.is_valid():
                letter = form.save(commit=False)
                # print("valid")
                letter.user = user
                letter.save()
                return redirect('/letters/')  # 익명 편지 작성 성공
    
    else:
        form = LetterForm()
        request.session['fail_reason'] = 'post_request_invalid'

    return redirect('/letters/')
    # 실패이유는 request.session.pop('fail-reason',None)을 사용해서 세션 꺼내쓰기
