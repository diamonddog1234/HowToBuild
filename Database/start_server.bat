@ECHO OFF

for /f "tokens=2 delims=:." %%a in ('"%SystemRoot%\System32\chcp.com"') do (
    set "_OLD_CODEPAGE=%%a"
)
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" 65001 > nul
)

@SET PATH="C:\Program Files\PostgreSQL\12\bin";%PATH%
@SET PGDATA=data
@SET PGDATABASE=how_to_build
@SET PGUSER=postgres
@SET PGPORT=5431
@SET PGLOCALEDIR=C:\Program Files\PostgreSQL\12\share\locale

postgres
pause            
