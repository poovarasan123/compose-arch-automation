@echo off
setlocal
 

:: Run the Python script with the module name
python compose_arch.py

echo.
echo ✅ Clean Architecture setup completed for %MODULE_NAME%!
pause
endlocal
