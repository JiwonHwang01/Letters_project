from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib import messages
from letters.models import User, Letter
from django.contrib.auth import authenticate, login, get_user
from letters.forms import LetterForm
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

def index(request):
    return render(request, 'letters/index.html')

def letter(request, hash_id):
    """해시 ID로 편지 상세보기"""
    letter_obj = Letter.get_by_hash_id(hash_id)
    if not letter_obj:
        raise Http404("편지를 찾을 수 없습니다.")
    return render(request, 'letters/letter_detail.html', {'letter': letter_obj})

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
            user = User.objects.get(username=request.POST.get("user"))
            form = LetterForm(request.POST)
            
        except User.DoesNotExist:
            request.session['fail_reason'] = 'user_not_exist'
            return redirect('/letters/')
        
        if form.is_valid():
            try:
                # 데이터베이스 트랜잭션으로 편지 저장 과정 보호
                with transaction.atomic():
                    letter = form.save(commit=False)
                    letter.user = user
                    letter.save()
                    
                # 성공 메시지 추가
                messages.success(request, f'✉️ {user.username}님에게 편지가 성공적으로 전달되었습니다!')
                return redirect('/letters/')  # 편지 작성 성공
                
            except Exception as e:
                # 편지 저장 중 오류 발생시 사용자에게 알림
                request.session['fail_reason'] = 'letter_save_error'
                return redirect('/letters/')
        else:
            # 폼 검증 실패
            request.session['fail_reason'] = 'form_validation_error'
            return redirect('/letters/')
    
    else:
        request.session['fail_reason'] = 'post_request_invalid'
        return redirect('/letters/')
    # 실패이유는 request.session.pop('fail-reason',None)을 사용해서 세션 꺼내쓰기
