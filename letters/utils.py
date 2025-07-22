import uuid
import base64
import codecs
import hashlib
from django.conf import settings

def generate_random_slug_code(length=12):
    """
    UUID 기반으로 랜덤한 URL-safe 문자열 생성 (우편함 URL용)
    """
    code = base64.urlsafe_b64encode(
        codecs.encode(uuid.uuid4().bytes, "base64").rstrip()
    ).decode()[:length]
    return code

def generate_letter_hash_id(letter_id, length=16):
    """
    편지 ID를 기반으로 해시 ID 생성
    보안을 위해 SECRET_KEY와 함께 해싱
    """
    secret_key = getattr(settings, 'SECRET_KEY', 'default-secret')
    
    # 편지 ID와 SECRET_KEY를 조합하여 해시 생성
    hash_input = f"{letter_id}-{secret_key}-letter"
    hash_object = hashlib.sha256(hash_input.encode())
    hex_digest = hash_object.hexdigest()
    
    # 첫 번째 길이만큼만 사용 (기본 16자리)
    return hex_digest[:length]

def generate_user_slug_code(length=12, existing_codes_checker=None):
    """
    사용자 우편함 URL 생성 (중복 확인 포함)
    existing_codes_checker: 중복 확인 함수 (예: lambda code: User.objects.filter(lettercase_url=code).exists())
    """
    from letters.models import User
    from django.db import DatabaseError
    
    if existing_codes_checker is None:
        def safe_checker(code):
            try:
                return User.objects.filter(lettercase_url=code).exists()
            except DatabaseError:
                # DB 오류 시 안전하게 True 반환 (재시도 유도)
                return True
        existing_codes_checker = safe_checker
    
    code = None
    max_attempts = 50  # 시도 횟수 증가
    attempts = 0
    
    try:
        while (not code or existing_codes_checker(code)) and attempts < max_attempts:
            code = generate_random_slug_code(length)
            attempts += 1
        
        if attempts >= max_attempts:
            # 최대 시도 횟수 도달 시 더 긴 코드로 재시도
            for extended_length in [length + 4, length + 8, length + 16]:
                code = generate_random_slug_code(extended_length)
                if not existing_codes_checker(code):
                    break
            else:
                # 모든 시도가 실패하면 예외 발생
                raise ValueError("고유한 사용자 코드 생성에 실패했습니다.")
        
        return code
        
    except Exception as e:
        # 모든 다른 오류는 ValueError로 변환
        raise ValueError(f"사용자 코드 생성 중 오류 발생: {str(e)}")

def verify_letter_hash_id(hash_id, letter_id):
    """
    편지 해시 ID 검증
    """
    expected_hash = generate_letter_hash_id(letter_id)
    return hash_id == expected_hash 