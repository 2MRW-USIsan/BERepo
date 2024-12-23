@echo off
:: 引数を確認
set MODE=%1

:: 空の引数チェック
if "%MODE%"=="" (
    echo No mode specified. Use --mode dev, --mode stag, or --mode prod.
    exit /b 1
)

:: モードに応じた処理
if "%MODE%"=="dev" (
    echo Switching to development environment...
    copy /Y backend\.env.dev backend\.env
) else if "%MODE%"=="stag" (
    echo Switching to staging environment...
    copy /Y backend\.env.stag backend\.env
) else if "%MODE%"=="prod" (
    echo Switching to production environment...
    copy /Y backend\.env.prod backend\.env
) else (
    echo Invalid mode: "%MODE%". Use --mode dev, --mode stag, or --mode prod.
    exit /b 1
)

:: Djangoサーバーの起動
python manage.py runserver
