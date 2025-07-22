from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db import transaction
from django.contrib import messages
from accounts.forms import UserForm
from letters.models import User
from letters.utils import generate_user_slug_code

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        
        if form.is_valid():
            try:
                # 데이터베이스 트랜잭션으로 회원가입 과정 보호
                with transaction.atomic():
                    # commit=False로 먼저 객체만 생성
                    user = form.save(commit=False)
                    # lettercase_url 생성 (실패 시 롤백됨)
                    user.lettercase_url = generate_user_slug_code()
                    # 모든 필드가 설정된 후 한번에 저장
                    user.save()
                    # 성공시에만 로그인 처리
                    login(request, user)
                
                return redirect('/letters/')
                
            except Exception as e:
                # 회원가입 중 오류 발생시 사용자에게 알림
                messages.error(request, '회원가입 중 오류가 발생했습니다. 다시 시도해주세요.')
                request.session['fail_reason'] = {'error': '회원가입 처리 오류'}
        else:
            request.session['fail_reason'] = form.errors
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})