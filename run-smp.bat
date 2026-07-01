@echo off

taskkill /F /IM elife-rc-smp.exe >nul 2>&1

cd smp
elife-rc-smp.exe&pause

