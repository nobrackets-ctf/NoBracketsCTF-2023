#!/bin/bash

while :
do
    su -c "exec socat TCP-LISTEN:7331,reuseaddr,fork EXEC:'/marchand/Marchand.py,stderr'" - user;
done