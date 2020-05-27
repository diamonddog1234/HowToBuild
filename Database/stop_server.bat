@ECHO OFF

rem This file is UTF-8 encoded, so we need to update the current code page while executing it
for /f "tokens=2 delims=:." %%a in ('"%SystemRoot%\System32\chcp.com"') do (
    set "_OLD_CODEPAGE=%%a"
)
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" 65001 > nul
)

REM The script sets environment variables helpful for PostgreSQL

@SET PATH="C:\Program Files\PostgreSQL\12\bin";%PATH%
@SET PGDATA=data
@SET PGDATABASE=postgres
@SET PGUSER=postgres
@SET PGPORT=5431
@SET PGLOCALEDIR=C:\Program Files\PostgreSQL\12\share\locale

pg_ctl stop
         
